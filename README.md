# Electronics-Project-Idea-Generator

**Generate creative electronics project ideas based on the components you have.**  

Upload a picture of your electronic components, and this tool uses AI to identify them and suggest unique project ideas tailored to your inventory.  

## Features  
- **Component Recognition**: Identifies electronic components, sensors, and microcontrollers from uploaded images.  
- **Project Idea Generation**: Suggests 5 unique project ideas based on the recognized components.  
- **User-Friendly Interface**: Simple upload and generate workflow using Streamlit.  
- **AI-Powered**: Leverages Groq API and LLaMA 4 Scout model for accurate component identification and creative idea generation.  

## Tech Stack  
- **Python**  
- **Groq API** (for AI model inference)  
- **Streamlit** (for the web interface)  
- **LLaMA 4 Scout** (AI model for component recognition and idea generation)  
- **base64** (for image encoding)  

## Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/aliii-codes/Electronics-Project-Idea-Generator.git
   cd Electronics-Project-Idea-Generator
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Set up Groq API:  
   - Create a `.env` file in the root directory.  
   - Add your Groq API key:  
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```  

## Usage  
1. Run the application:  
   ```bash
   streamlit run main.py
   ```  
2. Upload an image of your electronic components.  
3. Click "Generate Ideas" to get project suggestions.  

**Example:**  
Upload an image containing an ESP32, SG90 servo, and DHT11 sensor. The tool will identify these components and suggest projects like a weather station, home automation system, or robotic arm.  

## Project Structure  
```
Electronics-Project-Idea-Generator/  
├── main.py          # Main application file  
├── .env             # Environment variables (not included in repo)  
├── LICENSE          # MIT License  
└── README.md        # Project documentation  
```  

## License  
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
