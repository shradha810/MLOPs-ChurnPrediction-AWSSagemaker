import os
import json
import boto3
import pickle
import warnings
warnings.simplefilter("ignore")
# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime= boto3.client('runtime.sagemaker')
bucket = "sagemaker-eu-west-2-992382691308"
s3 = boto3.resource('s3')

def lambda_handler(event, context):
    payload = process_data(event)
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME, ContentType='text/csv',Body=payload)
    result = json.loads(response['Body'].read().decode())
    predicted_label = 'True' if result > 0.5 else 'False'
    return predicted_label

def process_data(event):
    event.pop('Phone')
    event['Area Code'] = event['Area Code'].astype(object)
    event.pop('Day Charge')
    event.pop('Eve Charge')
    event.pop('Night Charge')
    event.pop('Intl Charge')
    
    states = [ "AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY"]
    binary_state = [str(int(state == event['State'])) for state in states]
    state = ",".join(binary_state)
    
    area_codes = [ '657', '658', '659', '676', '677', '678', '686', '707', '716', '727', '736', '737', '758', '766', '776', '777', '778', '786', '787', '788', '797', '798', '806', '827', '836', '847', '848', '858', '866', '868', '876', '877', '878']
    binary_area_code = [str(int(number == event['Area Code'])) for number in area_codes]
    area_code = ",".join(binary_area_code)
    
    int_plan_values = ["no", "yes"]
    vmail_plan_values = ["no", "yes"]
    binary_representation = [ str(int(event["Int'l Plan"] == 'no')),str(int(event["Int'l Plan"] == 'yes')), str(int(event['VMail Plan'] == 'no')), str(int(event['VMail Plan'] == 'yes'))]
    int_plan_vmail = ",".join(binary_representation)
    final_catogorical = ",".join([state, area_code, int_plan_vmail])
    
    numerical_values = [ str(event['Account Length']), str(event['VMail Message']), str(event['Day Mins']), str(event['Day Calls']), str(event['Eve Mins']), str(event['Eve Calls']), str(event['Night Mins']), str(event['Night Calls']), str(event['Intl Mins']), str(event['Intl Calls']), str(event['CustServ Calls'])]
    final_numerical = ",".join(numerical_values)
    
    return ",".join([final_catogorical, final_numerical])
