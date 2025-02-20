import streamlit as st
import openai
import os
from dotenv import load_dotenv

from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv()

# -- Page configuration with sidebar expanded by default --
st.set_page_config(
    page_title="BlogCraft",
    page_icon="✍️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# -- Custom CSS to enhance the UI --
st.markdown(
    """
    <style>
    /* General body styling */
    body {
        background-color: #f4f6f9;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Center title with custom color */
    .main .block-container {
        padding: 2rem 2rem;
    }
    h1 {
        color: #2c3e50;
        text-align: center;
    }
    /* Input styling */
    .stTextInput, .stNumberInput, .stTextArea, .stSelectbox {
        margin-bottom: 1rem;
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #ecf0f1;
    }
    /* Button styling */
    .stButton>button {
        background-color: #2ecc71;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-size: 1rem;
    }
    .stButton>button:hover {
        background-color: #27ae60;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -- Sidebar: Mode selection --
mode = st.sidebar.radio(
    "Select Blog Generation Mode",
    [
        "Blog Generation (OpenAI)",
        "Blog Generation (Open Source)"
    ]
)

# If OpenAI mode is selected, ask for the API key in the sidebar.
if mode == "Blog Generation (OpenAI)":
    openai_api_key = st.sidebar.text_input(
        "Enter your OpenAI API Key",
        type="password",
        help="Provide your OpenAI API key to generate the blog."
    )
    # Use the provided key if available; otherwise fallback to the env variable.
    openai.api_key = openai_api_key or os.getenv("OPENAI_API_KEY")

# -- Page title and instructions --
st.title("BlogCraft ✍️")
st.markdown(
    "Provide a **Blog Topic**, the desired **Number of Words**, and select **For Whom** you are writing the blog. "
    "BlogCraft will generate a detailed, engaging blog post that naturally incorporates your inputs."
)

# -- Collect user inputs --
blog_topic = st.text_input(
    "Blog Topic", placeholder="e.g., The Future of Renewable Energy")
num_words = st.text_input("Number of Words", placeholder="e.g., 300")
style = st.selectbox(
    "Writing the blog for",
    ("Researchers", "Data Scientists", "Common People", "A 5 Year old"),
    index=0
)

# -- Define the function for the Open Source model (Local Llama-2) --


def get_llama2_local_response(topic: str, words: str, audience: str) -> str:
    """
    Generates a blog post using a locally downloaded Llama-2 model (GGML) via CTransformers.

    Requirements:
      - The GGML file (e.g., llama-2-7b-chat.ggmlv3.q8_0.bin) in the same directory or provide the full path.
      - ctransformers installed.
    """
    # Initialize the LLM with your local Llama-2 GGML file
    llm = CTransformers(
        model='llama-2-7b-chat.ggmlv3.q8_0.bin',  # Adjust filename/path if needed
        model_type='llama',
        config={
            'max_new_tokens': 256,   # Adjust tokens as needed
            'temperature': 0.01      # Control the 'creativity' of the response
        }
    )

    # Prompt template
    template = """
        Write a blog for a {audience} job profile on the topic "{topic}" in about {words} words.
        The blog should be well-structured, with an introduction, body, and conclusion. 
        Keep the tone clear, engaging, and appropriate for the specified audience.
    """
    # Build the prompt
    prompt = PromptTemplate(
        input_variables=["audience", "topic", "words"],
        template=template
    )

    # Format and generate
    final_prompt = prompt.format(audience=audience, topic=topic, words=words)
    response = llm(final_prompt)
    return response.strip()


# -- Generate blog on button click --
if st.button("Generate Blog"):
    # Basic validation
    if not blog_topic.strip():
        st.error("Please enter a blog topic.")
    elif not num_words.strip().isdigit():
        st.error("Please enter a valid number for 'Number of Words'.")
    else:
        if mode == "Blog Generation (OpenAI)":
            if not openai.api_key:
                st.error(
                    "OpenAI API key not found. Please enter your OpenAI API key in the sidebar.")
            else:
                # Build the prompt for OpenAI
                messages = [
                    {
                        "role": "system",
                        "content": (
                            "You are an expert blog writer. Generate a detailed, engaging, and well-structured blog post in English "
                            "tailored to a specific audience. Naturally incorporate the provided blog topic. "
                            "Aim for the approximate word count requested."
                        )
                    },
                    {
                        "role": "user",
                        "content": (
                            f"Blog Topic: {blog_topic}\n"
                            f"Number of Words: {num_words}\n"
                            f"For Whom: {style}\n\n"
                            "Please generate a comprehensive blog post based on the above information."
                        )
                    }
                ]
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
                        messages=messages,
                        temperature=0.1,
                    )
                    blog_text = response.choices[0].message.content.strip()
                    st.subheader("Generated Blog (OpenAI)")
                    st.write(blog_text)
                except Exception as e:
                    st.error(f"Error generating blog via OpenAI: {e}")

        else:
            # "Blog Generation (Open Source)" mode with local Llama-2
            try:
                blog_text = get_llama2_local_response(
                    blog_topic, num_words, style)
                st.subheader("Generated Blog (Open Source - Local Llama-2)")
                st.write(blog_text)
            except Exception as e:
                st.error(f"Error generating blog via local Llama-2: {e}")
