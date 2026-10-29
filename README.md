
# AI-Powered Resume Analysis App 🚀

An AI-powered Resume Analysis Application built with Python, Streamlit, and Groq API. The application analyzes uploaded resumes in PDF format and provides insights to help job seekers understand their strengths, identify missing skills, and improve their resumes.

## ✨ Features

- 📄 **PDF Resume Upload:** Upload your resume in PDF format.
- 🤖 **AI-Powered Analysis:** Analyze resume content using a large language model through the Groq API.
- 📊 **ATS Score:** Get an AI-generated resume score out of 100.
- 📝 **Resume Summary:** Generate a concise summary of your resume.
- 💪 **Strengths and Weaknesses:** Identify positive aspects and areas that need improvement.
- 🎯 **Missing Skills:** Discover skills that may need to be added or developed.
- 💡 **Improvement Suggestions:** Receive recommendations to improve your resume.
- 💼 **Suitable Job Roles:** Explore job roles that align with your resume.
- 🎤 **Interview Preparation:** Generate five interview questions with answers.
- ⬇️ **Download Results:** Download the analysis as a text file.

## 🛠️ Technologies Used

- Python
- Streamlit
- Groq API
- PyPDF2
- Large Language Models (LLMs)
- Prompt Engineering

## ⚙️ How It Works

1. Upload a resume in PDF format.
2. Extract the text from the PDF using PyPDF2.
3. Submit the extracted resume text to the AI model through the Groq API.
4. Generate resume insights based on a predefined analysis prompt.
5. Display the analysis results in the Streamlit interface.
6. Download the generated report as a text file.

## 📁 Project Structure

Resume_Analysis_App/
│
├── app.py             # Streamlit application interface
├── analyzer.py        # AI-powered resume analysis
├── pdf_reader.py      # PDF text extraction
├── prompts.py         # Resume analysis prompt
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/dhilleswar07/Resume_Analysis_App.git
cd Resume_Analysis_App
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Groq API Key

Create a `.env` file only if you also configure your application to load it using a package such as `python-dotenv`.

Alternatively, create the following file for Streamlit secrets:

`.streamlit/secrets.toml`

Add your API key:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Never commit your API key or secrets file to GitHub.

### 5. Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to use the application.

## 🔐 API Configuration

This project uses the Groq API to analyze resume content.

Get an API key from:

https://console.groq.com/

Configure `GROQ_API_KEY` in your environment or Streamlit secrets before running the application.

## ⚠️ Important Notes

- The application currently supports PDF resumes.
- Scanned PDFs may require OCR if their text cannot be extracted.
- The generated ATS score is an AI-generated estimate, not a score from a real employer's ATS.
- Recommendations depend on the resume content and the AI model's output.
- Review AI-generated suggestions before making changes to your resume.
- Do not upload confidential personal information unless you understand how it will be processed.

## 🔮 Future Enhancements

- Support for DOCX resume uploads.
- Job description matching and skill-gap analysis.
- Downloadable PDF reports.
- Improved resume scoring and evaluation.
- Enhanced user interface and visual analytics.
- Resume tailoring for specific job roles.

## 👨‍💻 Author

**Dhilleswar Jogi**

GitHub: https://github.com/dhilleswar07

LinkedIn: https://www.linkedin.com/in/dhilleswar07/

## 📄 License

Add a license file if you intend to distribute this project under an open-source license.
