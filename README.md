# BlogCraft 📝✍️

**BlogCraft** is an AI-powered blog generation tool that helps you create detailed, engaging, and well-structured blog posts with ease. Built with [Streamlit](https://streamlit.io), it leverages both OpenAI and Hugging Face's open source models (like [GPT-2](https://huggingface.co/gpt2)) to deliver high-quality content based on a simple blog topic and related interests.

---

## Features 🚀

- **Dual Mode Generation:**  
  Choose between using OpenAI's GPT-3.5 (or GPT-4 if you have access) or the open source GPT-2 model for generating your blog posts.

- **User-Friendly Interface:**  
  A modern, aesthetic UI with custom CSS for a clean and intuitive experience.

- **Easy to Configure:**  
  Set up with minimal configuration using environment variables and a simple `.env` file.

- **Flexible Prompts:**  
  Simply provide a blog topic and relevant interests; let the AI craft a comprehensive blog post that naturally incorporates your inputs.

---

## Demo 📺

Check out our live demo:  
[BlogCraft Demo](https://your-demo-url-here.com)

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
   The sidebar is open by default and allows you to select your preferred blog generation mode.

2. **Select Mode:**

   - **Blog Generation (OpenAI):**  
     Enter your OpenAI API key (input is password-masked). This mode uses `gpt-4o-mini` (or `gpt-4` if you have access).
   - **Blog Generation (Open Source):**  
     No API key required. Uses the GPT-2 model from Hugging Face by default.

3. **Enter Your Inputs:**  
   Provide a **Blog Topic** and **Relevant Interests** (comma-separated or space-separated).

4. **Generate Your Blog:**  
   Click the **Generate Blog** button to see your AI-crafted blog post appear in the main panel.

---

## Models Used 🤖

- **OpenAI GPT-3.5 or GPT-4:**  
  Utilizes `gpt-3.5-turbo` or `gpt-4` (if your account supports it) for high-quality blog generation.  
  [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)

- **GPT-2 (Open Source):**  
  A popular open source language model from Hugging Face that can generate coherent text once prompted effectively.  
  [GPT-2 on Hugging Face](https://huggingface.co/gpt2)

---

## Customizing Parameters ⚙️

When using the open source GPT-2 mode, you can experiment with:

- **Model Variants**: Try `gpt2`, `gpt2-medium`, `gpt2-large`, or `gpt2-xl`.
- **Generation Settings**: Adjust `max_length`, `temperature`, `top_k`, and `top_p` in the code to control output length and creativity.

Example snippet from `app.py`:

```python
gen_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_length=512,
    do_sample=True,
    top_k=50,
    top_p=0.95,
    pad_token_id=tokenizer.eos_token_id
)
```

---

## Resources & References 🔗

- [Streamlit Documentation](https://docs.streamlit.io)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [GPT-2 on Hugging Face](https://huggingface.co/gpt2)
- [LangChain Documentation](https://python.langchain.com/)

---

Enjoy crafting amazing blogs with **BlogCraft**! ✍️📝
