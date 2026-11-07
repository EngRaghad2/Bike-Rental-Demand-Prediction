# Bike Rental Demand Prediction

## Project description
This project predicts the hourly number of rented bicycles (`cnt`) using weather, season, calendar, and time features from the UCI Bike Sharing Dataset.

## Dataset source
UCI Machine Learning Repository, Bike Sharing Dataset:
https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset

The hourly file contains 17,379 observations from 2011–2012. The target is `cnt`.

## Repository structure
- `Data/Original/`: original `hour.csv` and `Readme.txt` (do not edit)
- `Data/Cleaned/`: cleaned modelling data
- `Notebooks/01_EDA_and_Preprocessing.ipynb`: exploration and cleaning
- `Notebooks/02_Modeling_and_Evaluation.ipynb`: model training and evaluation
- `Models/`: saved pipelines and metrics
- `Presentation/`: project presentation
- `main.py`: Streamlit prediction and model comparison app
- `download_data.py`: downloads the official dataset
- `requirements.txt`: required Python libraries

## Python version
Python 3.10 or newer is recommended.

## Setup on Windows
1. Install Python from https://www.python.org/downloads/
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Create an environment: `py -m venv .venv`
5. Activate it: `.venv\Scripts\activate`
6. Install libraries: `python -m pip install -r requirements.txt`
7. Download data: `python download_data.py`
8. Open Jupyter: `jupyter notebook`

## Setup on macOS / Linux
1. Install Python 3.10 or newer.
2. Open a terminal in the project folder.
3. Create an environment: `python3 -m venv .venv`
4. Activate it: `source .venv/bin/activate`
5. Install libraries: `python -m pip install -r requirements.txt`
6. Download data: `python download_data.py`
7. Open Jupyter: `jupyter notebook`

## How to run
1. Run all cells in `Notebooks/01_EDA_and_Preprocessing.ipynb`.
2. Run all cells in `Notebooks/02_Modeling_and_Evaluation.ipynb`.
3. Run the app: `streamlit run main.py`

## Step-by-step project summary
1. Explore the original hourly rental data.
2. Check missing values, duplicates, ranges, and target relationships.
3. Remove identifier and target-leakage columns; save cleaned data.
4. Split data using a fixed random seed.
5. Train and compare Linear Regression, Ridge, Random Forest, and Gradient Boosting.
6. Tune at least two models using cross-validation.
7. Evaluate using MAE, RMSE, and R².
8. Save fitted preprocessing/model pipelines and metrics.
9. Use Streamlit to make predictions and compare saved models.

## Important modelling decisions
- Target: `cnt` (total hourly rentals).
- `casual` and `registered` are excluded because `cnt = casual + registered`; using them would leak the answer into the inputs.
- `instant` is an identifier and is excluded.
- `dteday` is not used as a direct feature in this baseline.
- Categorical columns are one-hot encoded; numeric columns are imputed and scaled inside a Pipeline.
- The scaler/encoder is fitted only on training data through the pipeline to avoid data leakage.
- A random train/test split follows the project brief. Because observations are time-ordered, a chronological split would be a useful future improvement.

## Final results
Run Notebook 02 to generate `Models/model_comparison.csv` and `Models/metrics.json`. Insert the verified values into the presentation before presenting. Do not report placeholder results as actual results.

## Limitations
The dataset is from one bike-sharing system in Washington, DC, during 2011–2012. Results may not generalize to other cities or current conditions. The data describes completed rentals, not unmet demand.
The project includes an interactive Streamlit application for predicting hourly bike rental demand using four regression models.
