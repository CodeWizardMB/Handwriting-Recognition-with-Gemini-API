### Simple Guide to Install and Run Your Program

#### Step 1: Install Python
1. **Download Python**: 
   - Visit the [Python website](https://www.python.org/downloads/).
   - Click the "Download Python" button and follow the installation instructions. During installation, check the box that says "Add Python to PATH."

#### Step 2: Install Required Libraries
1. **Open Command Prompt or Terminal**:
   - On Windows: Search for "cmd" and open Command Prompt.
   - On macOS or Linux: Open Terminal.

2. **Install Libraries**:
   - Copy and paste this command into the Command Prompt or Terminal, then press Enter:
     ```bash
     pip install opencv-python google-generativeai language-tool-python pyttsx3 SpeechRecognition python-docx python-pptx PyMuPDF googletrans==4.0.0-rc1 Flask
     ```
   - This will install all the necessary libraries.

#### Step 3: Get Your API Key
1. **Obtain the API Key**:
   - Sign up for the Google Gemini API to get your API key. This key allows your program to connect to Google's services.

2. **Set Up the API Key**:
   - **Windows**:
     - Open Command Prompt and type:
       ```bash
       setx API_KEY "your-api-key-here"
       ```
   - **macOS/Linux**:
     - Open Terminal and type:
       ```bash
       export API_KEY="your-api-key-here"
       ```
   - Replace `"your-api-key-here"` with the actual API key.

#### Step 4: Run the Program
1. **Download or Copy the Program Code**:
   - Save the Python code provided into files named `main.py`, `chatbot.py`, and `app.py`.

2. **Run the Handwriting Recognition Program**:
   - Open Command Prompt or Terminal in the directory where `main.py` is saved.
   - Type the following command and press Enter:
     ```bash
     python main.py
     ```
   - This will run the basic functionality of handwriting recognition, translation, and grammatical correction (without the chatbot).

3. **Run the Chatbot Program**:
   - To include the chatbot functionality, run the following command:
     ```bash
     python chatbot.py
     ```
   - This will allow you to chat with the AI about the content in the uploaded image or document, with responses in both text and voice.

4. **Run the Website**:
   - To run the website, navigate to the directory where `app.py` is located and type:
     ```bash
     python app.py
     ```
   - This will start a local server. Open your web browser and go to `http://127.0.0.1:5000/` to view the website. The HTML code for the website is stored in the `statics` folder under the name `index.html`.

### What the Program Does:
- **Handwriting Recognition**: You can capture an image or upload photos/documents to recognize handwriting.
- **Translation**: The program can translate recognized text into your preferred language.
- **Grammatical Correction**: It checks and corrects grammar in the recognized text.
- **Chat with AI**: The `chatbot.py` program allows you to chat with an AI about the content in the uploaded image or document. The AI responds with both text and voice.
- **Website Interface**: A web interface is available, which can be accessed by running `app.py`. The website is built with HTML stored in the `statics` folder.

### Common Issues:
- **Python not recognized**: Ensure Python is installed correctly and added to your PATH.
- **Library installation issues**: If the `pip install` command fails, try running it again or check your internet connection.
  
### Youtube Links:
- https://youtu.be/5UMPKnLE0H4
