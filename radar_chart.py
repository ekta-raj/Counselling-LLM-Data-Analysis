import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go

df = pd.read_excel('table2.xlsx', sheet_name='table2.csv')

# Extract relevant columns for the radar chart
categories = [
    'Accuracy_Overall',
    'Accuracy_intake, assessment, and diagnosis',
    'Accuracy_treatment planning',
    'Accuracy_counseling skills and interventions',
    'Accuracy_professional practice and ethics',
    'Accuracy_core counseling attributes'
]

models = df['setting'].values

# Create radar chart data
fig1 = go.Figure()

for i, model in enumerate(models):
    fig1.add_trace(go.Scatterpolar(
        r=[
            df.loc[i, 'Accuracy_Overall'],
            df.loc[i, 'Accuracy_intake, assessment, and diagnosis'],
            df.loc[i, 'Accuracy_treatment planning'],
            df.loc[i, 'Accuracy_counseling skills and interventions'],
            df.loc[i, 'Accuracy_professional practice and ethics'],
            df.loc[i, 'Accuracy_core counseling attributes']
        ],
        theta=categories,
        fill='toself',
        name=model
    ))

# Update layout with adjusted radial axis range for better readability
fig1.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0.5, 1])  # Adjust the radial axis range
    ),
    title="Radar Chart of Models' Accuracies Across Competencies"
)

fig1.show()

fig1.write_image("radar_chart.png")  # Saves the chart as 'radar_chart.png' in the current directory
