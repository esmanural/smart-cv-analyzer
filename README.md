# smart-cv-analyzer

A lightweight Python CLI tool designed to analyze the match rate between a resume (CV) and a job description by comparing technical keywords.

## Features
* **External File Processing:** Reads directly from `cv.txt` and `job.txt` with built-in error handling (`try-except`) and fallback support.
* **Keyword Extraction:** Cleans, normalizes, and intersects text data to identify overlapping technical skills.
* **Match Scoring:** Calculates an estimated compatibility percentage and lists top matching keywords.

## Project Structure
* `main.py`: Core logic for file reading and keyword comparison.
* `cv.txt`: Sample resume text for testing.
* `job.txt`: Sample job posting text for testing.

## How to Run
1. Ensure Python 3 is installed on your machine.
2. Clone the repository and navigate to the project folder.
3. Run the script in your terminal:
   ```bash
   python main.py
