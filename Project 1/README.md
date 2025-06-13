# 🤖 AI Autocorrect Pro  
### Pinnacle Labs – Artificial Intelligence Internship Project (2025)

Welcome to **AI Autocorrect Pro**, a smart desktop application that helps users automatically correct spelling errors and suggests alternative words in real-time. Built with `Python`, `Tkinter`, and `SymSpell`, this tool is designed for writers, students, and coders who want reliable text correction with a clean, interactive UI.

> 🔗 **Internship Task**: Artificial Intelligence – Project Submission  
> 🏢 **Organization**: Pinnacle Labs  
> 📆 **Batch**: Summer Internship 2025  
> 📌 **Submitted by**: Aaditya Krishna Devadiga

---

## 🎯 Project Goals

- ✅ Build a smart autocorrect tool with a user-friendly GUI.
- ✅ Implement fast and accurate word correction using SymSpell.
- ✅ Add a **Word Suggestions Popup** to assist users while typing.
- ✅ Allow file loading, saving, and text statistics (words, characters).
- ✅ Enable light/dark theme toggle for better accessibility.

---

## 🖥️ Tech Stack

| Tool/Library     | Purpose                        |
|------------------|--------------------------------|
| Python 3.x       | Programming language           |
| Tkinter          | GUI toolkit                    |
| SymSpellPy       | Spell correction algorithm     |
| dictionary_freq.txt | Word frequency data file     |

---

## 🧠 Key Features

### 🔤 Real-Time Word Suggestions
As users type, a popup shows intelligent suggestions for potentially misspelled words using SymSpell's lookup algorithm.

### 🛠 Full Text Autocorrection
Click the **“Correct”** button to apply autocorrection to all detected spelling mistakes.

### 📂 File Management
- **Load Text:** Import `.txt` files to correct
- **Save Output:** Save corrected text to a `.txt` file

### 🌗 Theme Toggle
Switch between **Dark** and **Light** mode for comfort and accessibility.

### 📊 Live Stats
See real-time word and character counts while typing.

---

## 🚀 Getting Started
## ✅ Instructions to Use:
- Create a file named requirements.txt in the same folder as main.py.

- Paste the line above into it.

- Anyone can now install the required package with:

```bash

pip install -r requirements.txt
```
---
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/AI-Autocorrect-Pro.git
cd AI-Autocorrect-Pro
```
---
### 2. Install Dependencies
```bash
pip install symspellpy
```
---
### 3. Run the Application
```bash
python main.py
```
---
## 📌 Most Important 
### 📄 dictionary_freq.txt – Required File
The dictionary_freq.txt file contains words with frequency counts. You can download a standard one from:

🔗 https://github.com/wolfgarbe/SymSpell#frequency-dictionary

---
## 📥 How to Download and Load dictionary_freq.txt
 **The dictionary_freq.txt file is essential for the spell-checking feature to work. It contains words and their frequencies, which SymSpell uses to find the closest correct suggestions.**
- 🔽 Option 1: Download Prebuilt Dictionary (Recommended)
Visit the official SymSpell GitHub repo:
https://github.com/wolfgarbe/SymSpell

- Scroll down to the “Frequency Dictionary” section.

- Download the file named: frequency_dictionary_en_82_765.txt

- Rename it to:dictionary_freq.txt

- Move this file into the same folder as your main.py code file.

---
### Example format:
```
word    frequency
example 10000
python  9500
```
---
## 🧑‍💻 Developed By
- **Aaditya Krishna Devadiga**
- Artificial Intelligence Intern – **Pinnacle Labs**
- 📅 Internship Period: June–July 2025
- 📧 Connect on [LinkedIn](https://www.linkedin.com/in/aaditya-devadiga-0ba539329/)

---
## 📌 License
- This project is open-source and free to use. Attribution appreciated.
- Thanks to SymSpell for their blazing-fast correction engine.
---
## 🏁 Final Note
**This project was created as part of the Pinnacle Internship 2025 program to demonstrate skills in AI-based tool development, GUI design, and user-friendly interaction.
Let’s continue building tools that make language and communication easier!**
