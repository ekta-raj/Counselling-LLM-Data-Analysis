import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('table2.xlsx', sheet_name='table2.csv')

models = df['setting'].values
competencies = [
    'Accuracy_Overall',
    'Accuracy_intake, assessment, and diagnosis',
    'Accuracy_treatment planning',
    'Accuracy_counseling skills and interventions',
    'Accuracy_professional practice and ethics',
    'Accuracy_core counseling attributes'
]

# Set the width of the bars
barWidth = 0.15

# Create an index for each competency
r1 = np.arange(len(competencies))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

# Extract data for each model
model_1 = df.loc[0, competencies].values.tolist()  # counselingQA-gpt4o_few-shot_None_3
model_2 = df.loc[1, competencies].values.tolist()  # Meta-Llama-3-70B-Instruct_few-shot_None_3
model_3 = df.loc[2, competencies].values.tolist()  # Llama3-OpenBioLLM-70B_few-shot_None_3
model_4 = df.loc[3, competencies].values.tolist()  # Llama3-Med42-70B_few-shot_None_3

plt.figure(figsize=(10, 6))

plt.bar(r1, model_1, color='blue', width=barWidth, edgecolor='grey', label=models[0])
plt.bar(r2, model_2, color='green', width=barWidth, edgecolor='grey', label=models[1])
plt.bar(r3, model_3, color='red', width=barWidth, edgecolor='grey', label=models[2])
plt.bar(r4, model_4, color='purple', width=barWidth, edgecolor='grey', label=models[3])

# Add labels and title
plt.xlabel('Competencies', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(competencies))], competencies, rotation=45, ha='right')
plt.ylabel('Accuracy')
plt.title('Model Performance Comparison Across Competencies')

plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout for better viewing
plt.tight_layout()

# Save the figure as a PNG file
plt.savefig('model_performance_comparison_chart.png')

# Display the chart
plt.show()
