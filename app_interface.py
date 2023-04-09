import gradio as gr
import pickle
import numpy as np
import pandas as pd



#load the saved ml components
with open('model_components.pkl', "rb") as file:
        loaded_ml_components= pickle.load(file) 


#extract individual ml components
logistic_model= loaded_ml_components ["model"] 
model_pipeline= loaded_ml_components ["pipeline"]



# Function to predict
def churn_predict (gender, SeniorCitizen,Partner, Dependents, tenure, PhoneService, 
                   MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies,
                            Contract, PaperlessBilling, PaymentMethod, MonthlyCharges,TotalCharges):
  
  input_df= pd.DataFrame({ 
      'gender' : [gender],
      'SeniorCitizen' : [SeniorCitizen],
      'Partner' : [Partner],
      'Dependents' : [Dependents],
      'tenure' : [tenure ],
      'PhoneService' : [PhoneService], 
      'MultipleLines' : [MultipleLines], 
      'InternetService' : [InternetService],
      'OnlineSecurity' : [OnlineSecurity], 
      'OnlineBackup' : [OnlineBackup],
      'DeviceProtection' : [DeviceProtection], 
      'TechSupport' : [TechSupport], 
      'StreamingTV' : [StreamingTV], 
      'StreamingMovies' : [ StreamingMovies ],
      'Contract' : [Contract],
      'PaperlessBilling' : [PaperlessBilling],
      'PaymentMethod' : [PaymentMethod],
      'MonthlyCharges' : [MonthlyCharges],
      'TotalCharges' : [TotalCharges]
 })
  # Apply the pipeline to preprocess the data
  preprocessed_data = model_pipeline.transform(input_df)
    
    # Make a prediction using the model
  prediction =logistic_model.predict(preprocessed_data)
  
  return 'Yes' if prediction[0] == 1 else "No"



  

#App interface
input_component=[]
with gr.Blocks() as demo:

  gr.Markdown(
    """
    # Welcome Cherished User 👋 !
    Start predicting customer churn.
    """)
  with gr.Row():
       input_component.append(gr.components.Radio(["Month-to-month", "One year", "Two year"],label="Contract",)),
       input_component.append(gr.components.Slider(label="Tenure", minimum=0, maximum=72, step=1, interactive=True)),
       input_component.append(gr.components.Number(label="Monthly Charges")),
       input_component.append(gr.components.Number(label="Total Charges"))

  with gr.Row():
        input_component.append(gr.components.Radio(label="Gender", choices=["Male", "Female"])),
        input_component.append(gr.components.Radio(label="Senior Citizen", choices=["Yes", "No"])),
        input_component.append(gr.components.Radio(label="Partner", choices=["Yes", "No"])),
        input_component.append(gr.components.Radio(label="Dependents", choices=["Yes", "No"])) 
 
  with gr.Row():
        input_component.append( gr.components.Radio(label="Internet Service", choices=["DSL", "Fiber Optic", "No"])),
        input_component.append( gr.components.Radio(label="Online Security", choices=["Yes", "No", "No internet service"])),
        input_component.append( gr.components.Radio(label="Online Backup", choices=["Yes", "No", "No internet service"])),
        input_component.append( gr.components.Radio(label="Device Protection", choices=["Yes", "No", "No internet service"])),
        input_component.append(gr.components.Radio(label="Tech Support", choices=["Yes", "No", "No internet service"])),
        input_component.append(gr.components.Radio(label="TV Streaming", choices=["Yes", "No", "No internet service"])),
        input_component.append( gr.components.Radio(label="Movie Streaming", choices=["Yes", "No", "No internet service"]))  ,       

  with gr.Row():
        input_component.append(gr.components.Radio(label="Phone Service", choices=["Yes", "No"])),
        input_component.append( gr.components.Radio(label="Multiple Lines", choices=[
                                    "Yes", "No", "No phone service"]))  ,
        
  with gr.Row():
        input_component.append(gr.Radio(label="Paperless Billing", choices=["Yes", "No"])),
        input_component.append(gr.Radio(label="Payment Method", choices=["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]))

   

  
  submit_button = gr.Button("Predict Customer Churn").style(full_width=True)
  output_component = gr.Label(label="Churn Prediction")
  submit_button.click(fn = churn_predict,outputs = output_component, inputs=input_component)
  demo.launch()        

