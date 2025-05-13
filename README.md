# Project Overview
- The purpose of this project is to explore whether market participants react appropriately to events, potentially revealing systematic biases in market response patterns.

# Steps Involved
- Please reference (pg 4-14): https://docs.google.com/document/d/1diOv2hFvtE_QGZuBMnQ_X4hwjzPwJoGdZuz1dDqIHGM/edit?usp=sharing

# Important Files & Folders
- empirical_analysis.ipynb is the main file used for the bulk of the statistical analysis
- master_data.csv holds the primary data used in empirical_analysis.ipynb and was generated in the Data Processing folder
- final_observational_data.xlsx holds the main observational data collected in an easy-to-read tabular format!
- Data Processing (folder) contains all preprocessing steps to prepare the data, which can be overlooked unless the reader is interested in the details!
  - If the reader wishes, they can follow Data Processing in this order: universe_selection.py (1), return_data_download.py (2), and main_data.py (3)

# Current Findings
- Finds no evidence that a stock experiencing a bad event exhibits a material pattern in subsequent returns.
- Finds, a stock experiencing a good event tends to exhibit a pattern of subsequent negative returns, demonstrating that market participants overreact to good events.
