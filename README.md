## Project Overview 

In this project, the focus is on analyzing the 3D asymmetry of the upper and lower parts of faces. The program reads facial asymmetry data from a CSV file and performs either **statistical analysis** on a single adult's face or **correlation analysis** between two adults' facial asymmetry values.

## Features

1. **Statistical Analysis** (`type="stats"`):
    - Returns the 3D asymmetry values for nine facial landmarks.
    - Provides minimum, maximum, average, and standard deviation of the 3D asymmetry for both the upper and lower face.

2. **Correlation Analysis** (`type="corr"`):
    - Computes the correlation between the 3D asymmetry values of two adults across all nine facial landmarks.

## Input

The program expects the following input:
1. `csvfile`: A CSV file with the facial asymmetry data for multiple adults.
2. `adults`: A string (single adult ID) or a list of two adult IDs for comparison.
3. `type`: A string indicating the analysis type (`"stats"` for statistics or `"corr"` for correlation).


## Outputs

Depending on the input type, the program returns:
- For `"stats"`:
  - A list of 3D asymmetry values for the nine facial landmarks.
  - Lists of the minimum, maximum, average, and standard deviation of 3D asymmetry for the upper and lower face.
  
- For `"corr"`:
  - A single correlation value representing the similarity between two adults' facial asymmetry.

## Example Usage

```python
# Statistical analysis for a single adult
asym3D1, mn1, mx1, avg1, std1 = main('asymmetry_sample.csv', 'C4996', 'stats')

# Correlation analysis between two adults
corr = main('asymmetry_sample.csv', ['G8328', 'C4996'], 'corr')
```

## How to Run

- Clone this repository.
- Run the script by providing the necessary inputs (csvfile, adults, and type).

