# Smart CV & Job Description Analyzer (File-ready version)

def read_file(file_path):
    """Helper function to read text from a file safely."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. Using sample text instead.")
        return ""

def analyze_match(cv_text, job_description):
    # Convert texts to lowercase and split into words
    cv_words = set(cv_text.lower().split())
    job_words = set(job_description.lower().split())
    
    # Find common words (matching skills/keywords)
    common_words = cv_words.intersection(job_words)
    
    # Calculate a basic match percentage
    if len(job_words) == 0:
        match_percentage = 0
    else:
        match_percentage = (len(common_words) / len(job_words)) * 100
        
    print(f"--- Analysis Results ---")
    print(f"Matching Words Count: {len(common_words)}")
    print(f"Estimated Match Rate: %{match_percentage:.2f}")
    print(f"Common Keywords: {', '.join(list(common_words)[:10])}")

if __name__ == "__main__":
    # For now, if files don't exist yet, we use fallback strings
    # Later you can add 'cv.txt' and 'job.txt' to your repo!
    sample_cv = read_file("cv.txt")
    if not sample_cv:
        sample_cv = "Computer Engineering student in Warsaw, skilled in Python, C, Git, and Linux, looking for an internship."

    sample_job = read_file("job.txt")
    if not sample_job:
        sample_job = "We are looking for a Computer Engineering intern with Python, Git, and problem-solving skills."

    analyze_match(sample_cv, sample_job)
