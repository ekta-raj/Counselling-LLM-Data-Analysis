import pandas as pd

file_path = '/Users/hongdong-wan/Documents/Undergraduate Research/Counseling-QA/Johnny/data/mct_combined_v3.csv'
data = pd.read_csv(file_path)

questions = data['Question'].dropna().tolist()

def split_question_preserve_words(question):
    words = question.split()  # Split the question by spaces to get a list of words
    mid_point = len(words) // 2  # Find the midpoint in terms of the number of words
    first_half = " ".join(words[:mid_point])  # Join the first half of the words back into a sentence
    second_half = " ".join(words[mid_point:])  # Join the second half of the words back into a sentence
    return first_half, second_half

# Apply the function to all questions
split_questions = [split_question_preserve_words(q) for q in questions]

split_df = pd.DataFrame(split_questions, columns=['First Half', 'Second Half'])

split_df.to_csv('split_questions.csv', index=False)

print(split_df.head())

