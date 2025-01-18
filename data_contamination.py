import pandas as pd
from transformers import GPT2LMHeadModel, GPT2Tokenizer, BertTokenizer, BertForSequenceClassification
from bert_score import score as bert_score

# Step 1: Load your dataset
split_questions = pd.read_csv('split_questions.csv')  # Adjust path to your dataset

# Assuming dataset has 'First Half' and 'Second Half' columns
first_half_questions = split_questions['First Half']
original_second_half_questions = split_questions['Second Half']

# Load GPT model to generate second halves
gpt_tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
gpt_model = GPT2LMHeadModel.from_pretrained('gpt2')

# Ensure pad token is set
gpt_tokenizer.pad_token = gpt_tokenizer.eos_token

generated_second_half = []

# Track progress (if resuming from previous work, load this file instead)
output_file = 'generated_results.csv'

# Step 2: Generate the second half of the question based on the first half
i = 0
batch_size = 100  # Save every 100 generations

for question in first_half_questions:
    inputs = gpt_tokenizer(question, return_tensors='pt', padding=True, truncation=True)
    
    # Ensure attention mask is included
    attention_mask = inputs['attention_mask']
    
    # Generate text (pass both input_ids and attention_mask)
    outputs = gpt_model.generate(
        inputs['input_ids'], 
        attention_mask=attention_mask, 
        max_new_tokens=50,  # Generate 50 new tokens beyond the input length
        pad_token_id=gpt_tokenizer.eos_token_id  # Explicitly set the pad token ID
    )
    
    # Decode generated text
    generated_text = gpt_tokenizer.decode(outputs[0], skip_special_tokens=True)
    generated_second_half.append(generated_text)

    i += 1
    
    # Periodic saving after every 'batch_size' generations
    if i % batch_size == 0:
        print(f"Number of questions finished: # {i}")
        
        # Save generated results so far
        split_questions['generated_second_half'] = pd.Series(generated_second_half)
        split_questions.to_csv(output_file, index=False)

# Final save after loop finishes
split_questions['generated_second_half'] = pd.Series(generated_second_half)
split_questions.to_csv(output_file, index=False)

# Load the saved file after generation
split_questions = pd.read_csv('generated_results.csv')

# Load BERT tokenizer and model
bert_tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bert_model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

# Step 3: Compare with original second half using BERTScore
bert_scores = []
for gen, orig in zip(split_questions['generated_second_half'], split_questions['Second Half']):
    try:
        # Calculate BERTScore for each pair
        P, R, F1 = bert_score([gen], [orig], lang='en', verbose=True)
        bert_scores.append(F1.mean().item())  # Save the mean F1 score
        print(f"Success: {gen} vs {orig}")
    except KeyError as e:
        print(f"KeyError with sentence: {gen} vs {orig}")
        print(f"Error message: {e}")
        bert_scores.append(None)

# Step 4: Add the BERTScore results back to your dataframe
split_questions['bert_score'] = pd.Series(bert_scores)

# Step 5: Save the results with BERT scores
split_questions.to_csv('contamination_test_results_with_scores.csv', index=False)

