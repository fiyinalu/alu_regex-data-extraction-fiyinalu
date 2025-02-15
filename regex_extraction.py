import re

def extract_data(text):
    # Regex patterns
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"  # Matches emails
    url_pattern = r"https?://[a-zA-Z0-9./_-]+"  # Matches URLs
    phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"  # Matches phone numbers
    hashtag_pattern = r"#\w+"  # Matches hashtags
    
    # Extracting data
    emails = ", ".join(re.findall(email_pattern, text))
    urls = ", ".join(re.findall(url_pattern, text))
    phone_numbers = ", ".join(re.findall(phone_pattern, text))
    hashtags = ", ".join(re.findall(hashtag_pattern, text))
    
    # Displaying extracted data
    print("Extracted Emails:", emails)
    print("Extracted URLs:", urls)
    print("Extracted Phone Numbers:", phone_numbers)
    print("Extracted Hashtags:", hashtags)

# Sample input text
test_text = """
    Contact us at support@example.com or info@company.co.uk. 
    Visit our website: https://www.example.com or http://sub.example.org/page.
    Call (123) 456-7890 or 123-456-7890 for more details.
    Stay updated with #TechNews and #Coding.
"""

# Running the function
extract_data(test_text)
