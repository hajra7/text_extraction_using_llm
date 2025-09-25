# Food Extraction using LLMs

This project uses **Large Language Models (LLMs)** to extract **food and drink names** from text in multiple languages (English, Korean, Hindi, Telugu, etc.).  

It currently supports:
- **OpenAI** models (e.g., `gpt-4o-mini`)
- **Gemini** models (e.g., `gemini-2.0-flash`)

---

##  Setup

### 1. Clone the repository
```bash
git clone https://github.com/hajra7/text_extraction_using_llm.git
cd text_extraction_using_llm
```

### 2. Create and activate a virtual environment
```bash
python -m venv env
# Activate:
# Windows
env\Scripts\activate
# Linux/Mac
source env/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create and edit .env file
```bash
# Choose provider: openai | gemini
PROVIDER=openai

# --- OpenAI ---
OPENAI_API_KEY=your_openai_key_here
OPENAI_MODEL=gpt-4o-mini

# --- Gemini ---
GEMINI_API_KEY=your_gemini_key_here
GEMINI_MODEL=gemini-2.0-flash
```

##  Usage

### Run the script:
```bash
python extract_food.py
```

### Enter a sentence when prompted, for example:
```bash
Enter a sentence: I had chicken biryani and green tea.
```
 ### Output:
 ```bash 
Foods found: ["chicken biryani", "green tea"]
```

## Multilingual examples

### Korean

Input: ``` 오늘 저녁에 김치찌개와 불고기를 먹었어요. ```

Output: ``` ["김치찌개", "불고기"] ```

### Hindi

Input → ``` मैंने आलू पराठा और चाय नाश्ते में खाया। ```

Output → ``` ["आलू पराठा", "चाय"] ```

### Telugu

Input → ``` ఈ రోజు ఉదయం నేను ఇడ్లీ సాంబార్ తిన్నాను. ```

Output → ``` ["ఇడ్లీ", "సాంబార్"] ```

## Notes

Use .env.example as a template for ```.env```.

You can switch providers by editing the ```PROVIDER``` variable in ```.env```.

Extracted results are saved automatically to ```food_outputs/extracted_foods.json```.


