# Data Analysis — Interview Companion

This document summarizes the notebooks in this folder, explains key concepts, highlights important functions, and provides short interview-style questions and answers. No code in the notebooks is modified — this file complements them so the folder is interview-ready.

---

## How to use this file
- Read the matching notebook to see examples and runnable code.
- Use the sections below to understand the purpose of each notebook and to prepare short answers for interviews.

---

## 1. `1 Numpy.ipynb` — Core NumPy
- Purpose: Introduces arrays, vectorized operations, indexing, slicing, broadcasting, and basic linear algebra with NumPy.
- Key concepts:
  - `np.array`, `np.arange`, `np.linspace`, `np.reshape`, `np.transpose`
  - Broadcasting rules and why vectorized ops are faster than Python loops
  - Array indexing (basic, boolean, and fancy indexing)
  - Aggregations: `np.sum`, `np.mean`, `np.std`, `np.max`, `np.min`
- Interview highlights:
  - Why use NumPy arrays over Python lists? (memory layout, speed, vectorized ops)
  - Explain broadcasting with a short example.
  - Time complexity difference between elementwise loop vs vectorized operation.

---

## 2. `2 Pandas.ipynb` — Pandas Basics
- Purpose: Data structures (`Series`, `DataFrame`), basic IO, selection, groupby, missing data handling.
- Key concepts:
  - `pd.read_csv`, `df.head()`, `df.info()`, `df.describe()`
  - Indexing: `loc`, `iloc`, boolean masks
  - Grouping and aggregation: `groupby`, `agg`, `transform`
  - Handling missing values: `isna()`, `dropna()`, `fillna()`
- Interview highlights:
  - Difference between `loc` and `iloc`.
  - How to handle missing data and when to impute vs drop.
  - Explain `groupby` behavior and common pitfalls (e.g., resetting index).

---

## 3. `3 Data manipulation with NumPy and Pandas.ipynb` — Combined Workflows
- Purpose: Practical examples of using NumPy and Pandas together for ETL-like transformations.
- Key concepts:
  - Converting between NumPy arrays and DataFrames: `df.values`, `pd.DataFrame()`
  - Vectorized operations for feature engineering
  - Using `apply` vs vectorized column ops — when to prefer one over the other
- Interview highlights:
  - When is `apply` slower and what to use instead?
  - Show a short example converting array output into new DataFrame columns.

---

## 4. `4 Reading data from multiple sources using pandas.ipynb` — I/O Patterns
- Purpose: Reading from CSV, Excel, SQL, JSON, and multiple files; concatenation and merges.
- Key concepts:
  - `pd.read_csv`, `pd.read_excel`, `pd.read_json`, `pd.read_sql_query`
  - `pd.concat` vs `pd.merge` / `df.join`
  - Use of `chunksize` for large files and streaming processing
- Interview highlights:
  - Explain `merge` types: inner, left, right, outer.
  - How to read very large CSVs without OOM (e.g., `chunksize`, selective columns).

---

## 5. `5 Matplotlib.ipynb` — Plotting Basics
- Purpose: Create visualizations with Matplotlib: line, bar, scatter, histograms, subplots.
- Key concepts:
  - `plt.figure()`, `plt.plot()`, `plt.scatter()`, `plt.bar()`, `plt.subplot()`
  - Labels, legends, axis tuning, saving figures with `plt.savefig()`
  - Customizing styles and using `plt.tight_layout()`
- Interview highlights:
  - When to use Matplotlib vs Seaborn.
  - How to save high-resolution plots and prepare figures for reports.

---

## 6. `6 Seaborn.ipynb` — Statistical Plots
- Purpose: High-level statistical visualizations: `distplot`, `boxplot`, `heatmap`, pairplots.
- Key concepts:
  - Seaborn's interface to Matplotlib and DataFrame-aware plotting
  - Visualizing distributions, correlations, categorical comparisons
  - Using `sns.set_theme()` for consistent style
- Interview highlights:
  - Explain a violin plot and when it's preferable to a boxplot.
  - How to visualize correlation matrices and interpret heatmaps.

---

## 7. `7 sqlite.ipynb` — Lightweight SQL with Python
- Purpose: Demonstrate storing/querying data with SQLite and integrating with pandas (`pd.read_sql_query`).
- Key concepts:
  - `sqlite3` module basics: `connect`, `cursor`, `execute`, and parameterized queries
  - Using `pandas.read_sql_query()` to fetch results directly into DataFrames
  - Creating indexes and simple joins in SQL to optimize queries
- Interview highlights:
  - When to use SQLite vs a production RDBMS.
  - Benefits of parameterized queries for security (SQL injection protection).

---

## Combined Interview Tips (Data Analysis)
- Be ready to explain why you chose a particular function or pattern in the notebook (performance, clarity, memory).
- Always discuss data-cleaning steps and assumptions: null handling, outliers, data types.
- For visualization questions, explain the choice of chart type and what the viewer should interpret.
- Demonstrate how you would productionize: e.g., move heavy transforms into batch jobs, use databases, or serialize preprocessed artifacts.

---

## Quick commands & environment
- Create venv and install core packages:

```
python -m venv env
env\\Scripts\\activate
pip install numpy pandas matplotlib seaborn sqlite3
```

- Run a notebook locally using Jupyter or VS Code Notebook viewer.

---

If you want, I can:
- Insert Markdown cells directly into each notebook (keeps code unchanged) so explanations appear inline — tell me if you prefer inline annotations.
- Generate short flashcards (Q/A) per notebook for interview practice.
