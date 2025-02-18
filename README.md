# BlogCraft 📝✍️

**BlogCraft** is an AI-powered blog generation tool that helps you create detailed, engaging, and well-structured blog posts with ease. Built with [Streamlit](https://streamlit.io), it leverages both OpenAI and Hugging Face's open source models (like [Falcon-7B Instruct](https://huggingface.co/tiiuae/falcon-7b-instruct)) to deliver high-quality content based on a simple blog topic and related interests.

---

## Features 🚀

- **Dual Mode Generation:**  
  Choose between using OpenAI's GPT-4 or the open source Falcon-7B Instruct model for generating your blog posts.
- **User-Friendly Interface:**  
  A modern, aesthetic UI with custom CSS for a clean and engaging experience.

- **Easy to Configure:**  
  Set up with minimal configuration using environment variables and a simple `.env` file.

- **Flexible Prompts:**  
  Simply provide a blog topic and relevant interests; let the AI craft a comprehensive blog post that naturally incorporates your inputs.

---

## Demo 📺

Check out our live demo: [BlogCraft Demo](https://your-demo-url-here.com)  

---

## Installation 💻

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/alphatechlogics/BlogCraft.git
   cd BlogCraft
   ```

2. **Create a Virtual Environment and Install Dependencies:**

   ```bash
   python3 -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**

   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     ```

4. **Run the Application:**
   ```bash
   streamlit run app.py
   ```

---

## Usage 🛠️

1. **Open the Sidebar:**  
   The sidebar is open by default, allowing you to select your preferred blog generation mode.

2. **Select Mode:**

   - **Blog Generation (OpenAI):** Enter your OpenAI API key (input is password masked).
   - **Blog Generation (Open Source):** No API key is required.

3. **Enter Your Inputs:**  
   Provide the **Blog Topic** and **Relevant Interests** (comma-separated).

4. **Generate Your Blog:**  
   Click the **Generate Blog** button to see your AI-crafted blog post!

---

## Models Used 🤖

- **OpenAI GPT-4:**  
  Utilizes the `gpt-4o` model for high-quality blog generation.  
  [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)

- **Falcon-7B Instruct:**  
  An efficient open source alternative from Hugging Face optimized for instruction-following.  
  [Falcon-7B Instruct on Hugging Face](https://huggingface.co/tiiuae/falcon-7b-instruct)


---

## Resources & References 🔗

- [Streamlit Documentation](https://docs.streamlit.io)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Falcon-7B Instruct on Hugging Face](https://huggingface.co/tiiuae/falcon-7b-instruct)
- [LangChain Documentation](https://python.langchain.com/)

---

Enjoy crafting amazing blogs with **BlogCraft**! ✍️📝

