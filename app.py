import streamlit as st
import openai
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate

# Import Hugging Face libraries for the Falcon model
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

# Load environment variables from .env file
load_dotenv()

# Page configuration with sidebar expanded by default
st.set_page_config(
    page_title="BlogCraft",
    page_icon="✍️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS to enhance the UI
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

# Sidebar: Mode selection
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

# Main input fields (common to both modes)
st.title("BlogCraft ✍️")
st.markdown("Enter a blog topic and the related interests. BlogCraft will generate a detailed and engaging blog post that naturally incorporates your inputs.")

blog_topic = st.text_input(
    "Blog Topic", placeholder="e.g., The Future of Renewable Energy")
interests = st.text_input(
    "Relevant Interests", placeholder="e.g., Sustainability, Technology, Innovation")

if st.button("Generate Blog"):
    if blog_topic.strip() == "":
        st.error("Please enter a blog topic.")
    else:
        if mode == "Blog Generation (OpenAI)":
            # Build the prompt for OpenAI
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are an expert blog writer. Generate a detailed, engaging, and well-structured blog post in English "
                        "tailored to a general audience. Naturally incorporate the provided blog topic and related interests throughout the text."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Blog Topic: {blog_topic}\n"
                        f"Relevant Interests: {interests}\n\n"
                        "Please generate a comprehensive blog post based on the above information."
                    )
                }
            ]
            try:
                response = openai.chat.completions.create(
                    model="gpt-4o",  # Change this model name if necessary.
                    messages=messages,
                    temperature=0.1,
                )
                blog_text = response.choices[0].message.content.strip()
                st.subheader("Generated Blog (OpenAI)")
                st.write(blog_text)
            except Exception as e:
                st.error(f"Error generating blog via OpenAI: {e}")
        elif mode == "Blog Generation (Open Source)":
            # Function to get blog response via Hugging Face Falcon-7B Instruct
            def get_falcon_response(topic, interests):
                model_id = "tiiuae/falcon-7b-instruct"
                # Load tokenizer and model from Hugging Face hub
                tokenizer = AutoTokenizer.from_pretrained(model_id)
                model = AutoModelForCausalLM.from_pretrained(
                    model_id,
                    torch_dtype=torch.bfloat16,
                    trust_remote_code=True,
                    device_map="auto"
                )
                # Create text-generation pipeline
                gen_pipeline = pipeline(
                    "text-generation",
                    model=model,
                    tokenizer=tokenizer,
                    max_length=1024,
                    do_sample=True,
                    truncation=True,
                    top_k=10,
                    eos_token_id=tokenizer.eos_token_id,
                )
                # Build a prompt that includes topic and interests
                prompt = (
                    f"Write a comprehensive and engaging blog post in English. The blog topic is '{topic}', and it should naturally incorporate "
                    f"the following relevant interests: {interests}. Ensure the blog is well-structured, clear, and appealing to a general audience."
                )
                sequences = gen_pipeline(
                    prompt,
                    max_length=1024,
                    do_sample=True,
                    top_k=10,
                    num_return_sequences=1,
                    eos_token_id=tokenizer.eos_token_id,
                )
                return sequences[0]["generated_text"]

            try:
                blog_text = get_falcon_response(blog_topic, interests)
                st.subheader(
                    "Generated Blog (Open Source - Falcon 7B Instruct)")
                st.write(blog_text)
            except Exception as e:
                st.error(
                    f"Error generating blog via the open source model: {e}")
