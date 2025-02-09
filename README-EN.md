markdown
# 🏆 Football Matches Scraper

This project extracts **championship names, teams, scores, and match dates** from a website and saves them in a **CSV file**.

## 📌 Requirements
Before running the script, install the required libraries using:
bash
pip install -r requirements.txt
## 🚀 How to Run
1️⃣ Run the script using:
bash
python yallakora.py
2️⃣ Enter the desired date in **MM/DD/YYYY** format when prompted.  
3️⃣ Enter the file name, and it will be saved in the folder (outputs).
## 📊 Extracted Data
- 🏆 **Championship Name**  
- ⚽ **Team A**  
- ⚽ **Team B**  
- ⏰ **Match Time**  
- 🔢 **Score**  

## 📁 Output File
After running the script, a **CSV file** containing all available matches will be generated.

## 🔍 Example of Extracted Data:
| Championship        | Team A     | Score  | Team B        | Match Time |
|---------------------|-----------|--------|--------------|------------|
| Premier League     | Liverpool | 2 - 1  | Man City     | 20:00      |
| Champions League   | Real Madrid | 3 - 0  | Bayern Munich | 22:00     |

---

## 🛠️ Tools Used
- `requests` for fetching webpage content  
- `BeautifulSoup` for parsing HTML and extracting data  
- `csv` for saving data in a structured format  

## 📝 Notes
- Ensure that the **target website allows web scraping** by checking its **robots.txt** policy.  
- The script can be modified to work with different websites or extract additional data like **match statistics, team formations, goal details, etc.**  

---

👨‍💻 **Developer:** [Said Ahmed](https://github.com/SaidNexus)  
📌 **If you encounter any issues or have suggestions, feel free to open an Issue!**