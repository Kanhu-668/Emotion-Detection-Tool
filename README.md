# 🎭 Emotion Detection Tool (Emoji Mood Analyzer)

A simple and fun **Python-based Emotion Detection Tool** that identifies emotions from text input using keyword analysis — and displays the result with expressive emojis! 😄  

Developed as part of the **Motion Cut Internship Project** by **Champion Kanhu**.

---

## 🌟 Features

✅ Detects five basic emotions:
- **Joy** 😊  
- **Sadness** 😢  
- **Anger** 😠  
- **Fear** 😨  
- **Love** ❤️  

✅ Uses simple keyword-based detection  
✅ Clean, beginner-friendly code  
✅ Optional stopword removal using `nltk`  
✅ Continuous user interaction until "exit" is entered  

---

## 🧩 How It Works

1. The user enters a sentence describing their feeling.  
2. The program tokenizes and processes the text.  
3. It matches words against emotion-specific keyword lists.  
4. Displays the **dominant emotion** with a corresponding emoji.  

---

## 💻 Example Run

Welcome to the Emotion Detection Tool! 🎭
Type 'exit' to quit.

Enter a sentence describing your feeling: I am so happy and excited today!
Detected Emotion: Joy 😊

Enter a sentence describing your feeling: I miss my loved ones
Detected Emotion: Love ❤️

Enter a sentence describing your feeling: I am scared of the dark
Detected Emotion: Fear 😨

Enter a sentence describing your feeling: exit
Goodbye! Take care! 👋

python
Copy code
