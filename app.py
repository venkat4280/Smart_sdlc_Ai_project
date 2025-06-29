import gradio as gr
from ai_story_generator import extract_and_classify
from code_generator import generate_code
from test_case_generator import generate_tests
from bug_fixer import fix_code
from code_summarizer import summarize_code
from text_to_code import text_to_code
from chatbot_agent import chat_with_agent

with gr.Blocks(theme=gr.themes.Soft(primary_hue="blue", secondary_hue="purple")) as demo:
    gr.Markdown("# 💡 Smart SDLC AI Assistant")
    gr.Markdown("Streamline your software development lifecycle with AI-powered tools.")

    with gr.Tab("📄 Requirement Analysis"):
        pdf_input = gr.File(label="Upload PDF")
        output = gr.Textbox(label="User Stories")
        analyze_btn = gr.Button("Analyze")
        analyze_btn.click(fn=extract_and_classify, inputs=pdf_input, outputs=output)

    with gr.Tab("🧠 Text to Code"):
        prompt = gr.Textbox(label="Describe what you want to build")
        code_output = gr.Code(label="Generated Code")
        gen_btn = gr.Button("Generate Code")
        gen_btn.click(fn=text_to_code, inputs=prompt, outputs=code_output)

    with gr.Tab("🛠️ Code Generator"):
        story_input = gr.Textbox(label="User Story or Task")
        lang = gr.Dropdown(["Python", "JavaScript", "Java"], label="Language")
        code = gr.Code(label="Generated Code")
        gen_code_btn = gr.Button("Generate")
        gen_code_btn.click(fn=generate_code, inputs=[story_input, lang], outputs=code)

    with gr.Tab("✅ Test Case Generator"):
        code_input = gr.Code(label="Code to Test")
        test_output = gr.Code(label="Generated Tests")
        test_btn = gr.Button("Generate Tests")
        test_btn.click(fn=generate_tests, inputs=code_input, outputs=test_output)

    with gr.Tab("🐞 Bug Fixer"):
        buggy_code = gr.Code(label="Buggy Code")
        fixed_code = gr.Code(label="Fixed Code")
        fix_btn = gr.Button("Fix Code")
        fix_btn.click(fn=fix_code, inputs=buggy_code, outputs=fixed_code)

    with gr.Tab("📚 Code Summarizer"):
        code_block = gr.Code(label="Code")
        summary = gr.Textbox(label="Summary")
        sum_btn = gr.Button("Summarize")
        sum_btn.click(fn=summarize_code, inputs=code_block, outputs=summary)

    with gr.Tab("🤖 Chatbot Assistant"):
        chat_input = gr.Textbox(label="Ask me anything")
        chat_output = gr.Textbox(label="Response")
        chat_btn = gr.Button("Ask")
        chat_btn.click(fn=chat_with_agent, inputs=chat_input, outputs=chat_output)

demo.launch(share=True)