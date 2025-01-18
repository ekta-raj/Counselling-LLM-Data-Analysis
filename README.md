# Coundelling LLM Data Analysis 


### 1. **Bar Chart Analysis (`bar_chart.py`)**
   - **Purpose**: Visualizes the performance of models across various competencies using a grouped bar chart.
   - **Key Features**:
     - Reads data from `table2.xlsx`.
     - Compares accuracy metrics like intake, treatment planning, and counseling skills across different models.
     - Saves the visualization as a PNG file.
   - **Output**: `model_performance_comparison_chart.png`

---

### 2. **Contamination Analysis (`contamination_analysis.py`)**
   - **Purpose**: Analyzes potential data contamination by comparing model-generated text with human-written counterparts using BERTScore.
   - **Key Features**:
     - Reads BERTScore results from `contamination_test_results_with_scores.csv`.
     - Plots a histogram of BERT scores and identifies high-contamination samples.
     - Provides statistical summaries and lists samples with high/low scores.
   - **Output**: Insights on contamination, including summary statistics and visualizations.

---

### 3. **Excel Data Conversion (`convert_table3.py`)**
   - **Purpose**: Processes and calculates percentage differences between models' performance metrics in Excel sheets.
   - **Key Features**:
     - Reads data from `table3.xlsx` with multiple sheets.
     - Calculates percentage differences for metrics across different rows/models.
     - Saves updated results into `updated_table3.xlsx`.
   - **Output**: `updated_table3.xlsx`

---

### 4. **Data Contamination Detection (`data_contamination.py`)**
   - **Purpose**: Detects and evaluates data contamination by generating and comparing text using GPT-2 and BERTScore.
   - **Key Features**:
     - Generates second halves of questions using GPT-2.
     - Compares generated text with original data using BERTScore.
     - Saves results with similarity scores into a CSV file.
   - **Output**: `contamination_test_results_with_scores.csv`

---

### 5. **Radar Chart Visualization (`radar_chart.py`)**
   - **Purpose**: Creates radar charts to visualize model performance across competencies.
   - **Key Features**:
     - Extracts accuracy metrics from `table2.xlsx`.
     - Generates a radar chart for each model's performance.
     - Saves the radar chart as an image file.
   - **Output**: `radar_chart.png`

---

### 6. **Web Scraper for Counseling Exams (`scrape_counseling.py`)**
   - **Purpose**: Automates data collection from counseling exam websites.
   - **Key Features**:
     - Logs into the website, navigates through questions, and extracts exam data.
     - Collects information such as question text, options, correct answers, and explanations.
     - Saves the data into a CSV file.
   - **Output**: `counseling_exam_4_questions.csv`

---

## How to Use

1. **Install Dependencies**:
   - Required libraries include `pandas`, `matplotlib`, `transformers`, `bert_score`, `selenium`, and `plotly`.
   - Install via pip:
     ```bash
     pip install pandas matplotlib transformers bert-score selenium plotly
     ```

2. **Run Scripts**:
   - Execute each script based on its specific task. For example:
     ```bash
     python bar_chart.py
     python contamination_analysis.py
     ```
