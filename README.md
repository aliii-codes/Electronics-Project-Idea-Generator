# 🛠️ Electronics Project Idea Generator  
**Turn your spare components into innovative electronics projects!**  

[![GitHub stars](https://img.shields.io/github/stars/aliii-codes/Electronics-Project-Idea-Generator?style=for-the-badge)](https://github.com/aliii-codes/Electronics-Project-Idea-Generator/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/aliii-codes/Electronics-Project-Idea-Generator?style=for-the-badge)](https://github.com/aliii-codes/Electronics-Project-Idea-Generator/network)
[![GitHub issues](https://img.shields.io/github/issues/aliii-codes/Electronics-Project-Idea-Generator?style=for-the-badge)](https://github.com/aliii-codes/Electronics-Project-Idea-Generator/issues)
[![License](https://img.shields.io/github/license/aliii-codes/Electronics-Project-Idea-Generator?style=for-the-badge)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/Groq-000000?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com/)

---

## ✨ Features  

| 🎨 Feature | 🚀 Benefit |
|------------|-----------|
| **Component Recognition** | Identifies electronic components, sensors, and microcontrollers from uploaded images. |
| **Project Idea Generation** | Suggests 5 unique project ideas tailored to your inventory. |
| **User-Friendly Interface** | Simple upload and generate workflow powered by Streamlit. |
| **AI-Powered** | Leverages Groq API and LLaMA 4 Scout for accurate identification and creative ideas. |

---

## 🛠 Tech Stack  

| Category       | Technologies                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **Backend**    | Python, Groq API, LLaMA 4 Scout                                            |
| **Frontend**   | Streamlit                                                                  |
| **Utilities**  | base64 (for image encoding)                                                |

---

## 🚀 Installation  

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/aliii-codes/Electronics-Project-Idea-Generator.git
   cd Electronics-Project-Idea-Generator
   ```  

2. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```  

3. **Set up Groq API:**  
   - Create a `.env` file in the root directory.  
   - Add your Groq API key:  
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```  
   - **Obtain API Key:** Sign up at [Groq](https://groq.com/) to get your API key.  

---

## 🕹️ Usage  

1. **Run the application:**  
   ```bash
   streamlit run main.py
   ```  

2. **Upload an image** of your electronic components.  
3. **Click "Generate Ideas"** to receive project suggestions.  

**Example:**  
Upload an image containing an ESP32, SG90 servo, and DHT11 sensor. The tool will identify these components and suggest projects like a weather station, home automation system, or robotic arm.  

---

## 📁 Project Structure  

```
Electronics-Project-Idea-Generator/  
├── main.py          # Main application file  
├── .env             # Environment variables (not included in repo)  
├── LICENSE          # MIT License  
└── README.md        # Project documentation  
```  

---

## 🤝 Contributing  

1. Fork the repository.  
2. Create a new branch:  
   ```bash
   git checkout -b feature/your-feature-name
   ```  
3. Commit your changes:  
   ```bash
   git commit -m "Add your feature"
   ```  
4. Push to the branch:  
   ```bash
   git push origin feature/your-feature-name
   ```  
5. Open a pull request.  

---

## 🐞 Bug Reports & Feature Requests  
Found a bug or have a feature request? [Open an issue](https://github.com/aliii-codes/Electronics-Project-Idea-Generator/issues).  

---

## 📜 License & Acknowledgements  
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  

**Shoutout to:**  
- [Groq](https://groq.com/) for their powerful AI inference API.  
- [Streamlit](https://streamlit.io/) for making app development effortless.  
- [LLaMA 4 Scout](https://llama.meta.com/) for enabling accurate component recognition and creative idea generation.
