import pandas as pd
import matplotlib.pyplot as plt

results = pd.read_csv('contamination_test_results_with_scores.csv')

# Step 1: Plot the distribution of BERT scores
plt.figure(figsize=(10, 6))
plt.hist(results['bert_score'].dropna(), bins=20, color='blue', edgecolor='black')
plt.title('Distribution of BERT Scores')
plt.xlabel('BERT Score')
plt.ylabel('Frequency')
plt.show()

# Step 2: Set a threshold for contamination (e.g., 0.8 or 0.9)
contamination_threshold = 0.9

# Step 3: Identify contaminated samples
contaminated_samples = results[results['bert_score'] >= contamination_threshold]

print(f"Number of contaminated samples: {len(contaminated_samples)}")
print(f"Percentage of contaminated samples: {len(contaminated_samples) / len(results) * 100:.2f}%")

# Step 4: Summary statistics of BERT scores
mean_score = results['bert_score'].mean()
median_score = results['bert_score'].median()
std_score = results['bert_score'].std()

print(f"Mean BERT Score: {mean_score:.3f}")
print(f"Median BERT Score: {median_score:.3f}")
print(f"Standard Deviation of BERT Scores: {std_score:.3f}")

# Step 5: Inspect high and low scoring samples
high_scoring_samples = results[results['bert_score'] >= 0.87].head(5)  # Top 5 highest scoring samples
low_scoring_samples = results[results['bert_score'] <= 0.75].head(5)   # Top 5 lowest scoring samples

print("High scoring samples (potential contamination):")
print(high_scoring_samples[['First Half', 'generated_second_half', 'Second Half', 'bert_score']])

print("\nLow scoring samples (likely no contamination):")
print(low_scoring_samples[['First Half', 'generated_second_half', 'Second Half', 'bert_score']])
