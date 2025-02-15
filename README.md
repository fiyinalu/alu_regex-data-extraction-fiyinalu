```markdown
# ALU Regex Data Extraction

# 📌 Description
This project extracts specific types of data from large text responses using Regular Expressions (Regex). It can identify:  
✔️ Email addresses  
✔️ URLs  
✔️ Phone numbers  
✔️ Hashtags  

# 🛠 Technologies Used
- Python (with `re` module for regex processing)
- Git & GitHub for version control

# 🚀 How to Use the Extractor
This script helps extract predefined data from text. By default, it scans for emails, URLs, phone numbers, and hashtags.

# 🔹 Running the Script
1. *Clone the repository 
   ```bash
   git clone https://github.com/fiyinalu/alu_regex-data-extraction-fiyinalu.git
   cd alu_regex-data-extraction-fiyinalu
   ```
2. Run the script  
   Ensure Python is installed, then execute:  
   ```bash
   python regex_extraction.py
   ```

# 🔹 Customizing for Your Data
If you want to extract data from your own text:  
1. Open `regex_extraction.py` in a code editor (VS Code, PyCharm, etc.).
2. Locate the variable:
   ```python
   test_text = """
       Contact us at support@example.com or info@company.co.uk. 
       Visit our website: https://www.example.com or http://sub.example.org/page.
       Call (123) 456-7890 or 123-456-7890 for more details.
       Stay updated with #TechNews and #Coding.
   """
   ```
3. Replace it with your own text and save the file.  
4. Run the script again with `python regex_extraction.py`.

# 📝 Notes
- This script currently supports email, URL, phone number, and hashtag extraction.
- If you need to add credit cards, HTML tags, or currency amounts, you can modify the regex patterns.
