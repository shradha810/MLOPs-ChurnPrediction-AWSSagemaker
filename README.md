# End-to-End serverless AWS MLOps architecture: Predicting Customer Churn with SageMaker, CodeCommit, Lambda, API Gateway, and SageMaker Autoscaling
https://www.linkedin.com/pulse/end-to-end-serverless-aws-mlops-architecture-customer-shradha-agarwal-jejyc

This project utilizes a combination of AWS services to create a comprehensive solution for predicting customer churn using a dataset from a mobile phone operator. The key components of this project include:

- **Amazon SageMaker**: Used for data preprocessing, model training and deployment.
- **AWS Lambda and API Gateway**: Enables public access to clients who can query the application and get the prediction. Also, secures the backend infrastructure, where AWS Lambda operates within a protected private network
- **CodeCommit**: Utilized for code versioning.
- **SageMaker AutoScaling**: Ensures high availability of the system.

The integration of these services allows for an end-to-end process of predicting customer churn, from training the model to making predictions accessible through an API. Additionally, CodeCommit ensures proper version control and collaboration among team members, while SageMaker AutoScaling ensures the system can handle varying workloads and maintain high availability.
