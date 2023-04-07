import gradio as gr
import os

#App interface
with gr.Blocks() as demo:

  gr.Markdown(
    """
    # Welcome Cherished User 👋 !
    Start predicting customer churn.
    """)
  with gr.Row():
        Contract = gr.Dropdown(label="Contract", choices=["Month-to-month", "One year", "Two year"])
        tenure = gr.Slider(label="Tenure (months)", minimum=0, maximum=72, step=1, interactive=True)
        MonthlyCharges = gr.Number(label="Monthly Charges")
        TotalCharges = gr.Number(label="Total Charges")

  with gr.Row():
        gender = gr.Dropdown(label="Gender", choices=["Male", "Female"])
        SeniorCitizen = gr.Radio(label="Senior Citizen", choices=["Yes", "No"])
        Partner = gr.Radio(label="Partner", choices=["Yes", "No"])
        Dependents = gr.Radio(label="Dependents", choices=["Yes", "No"]) 

  with gr.Row():
        InternetService = gr.Dropdown(label="Internet Service", choices=["DSL", "Fiber Optic", "No"])
        OnlineSecurity = gr.Dropdown(label="Online Security", choices=["Yes", "No", "No internet service"])
        OnlineBackup = gr.Dropdown(label="Online Backup", choices=["Yes", "No", "No internet service"])
        DeviceProtection = gr.Dropdown(label="Device Protection", choices=["Yes", "No", "No internet service"])
        TechSupport = gr.Dropdown(label="Tech Support", choices=["Yes", "No", "No internet service"])
        StreamingTV = gr.Dropdown(label="TV Streaming", choices=["Yes", "No", "No internet service"])
        StreamingMovies = gr.Dropdown(label="Movie Streaming", choices=["Yes", "No", "No internet service"])         

  with gr.Row():
        PhoneService = gr.Radio(label="Phone Service", choices=["Yes", "No"])
        MultipleLines = gr.Dropdown(label="Multiple Lines", choices=[
                                    "Yes", "No", "No phone service"])  
        
  with gr.Row():
        PaperlessBilling = gr.Radio(label="Paperless Billing", choices=["Yes", "No"])
        PaymentMethod = gr.Dropdown(label="Payment Method", choices=["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])

  submit_btn = gr.Button("Predict Customer Churn").style(full_width=True)       

demo.launch(inbrowser=True, share=False)        
