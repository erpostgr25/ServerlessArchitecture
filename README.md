# ServerlessArchitecture
## Assignment 1: Automated Instance Management Using AWS Lambda and Boto3  
1) Lambda function to automate instance start/stop based on tagging deployed successfully  
2) Instance created with tag Auto-Start and Auto-Stop  
   <img width="582" height="66" alt="image" src="https://github.com/user-attachments/assets/038d44c4-77e3-4507-8a79-4a81889f1ea8" />  
3) Required permission applied  
   <img width="1501" height="848" alt="lambda-function-role" src="https://github.com/user-attachments/assets/66413af1-404a-4e45-a4f8-42d8e739ebe5" />  
4) Tested positive and negative scenario by manual invocation of lambda function  
   Positive  
   <img width="1721" height="302" alt="Testfunction-Success" src="https://github.com/user-attachments/assets/e2d87c67-d30e-4da7-8d0b-20a634ccc4ac" />  
   Negative  
   <img width="1708" height="192" alt="Testfunction-FalseSuccess" src="https://github.com/user-attachments/assets/e9fbc8bf-1f43-42da-a9ed-4e967ad572d6" />  
## Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3  
1) Lambda function to cleanup 30days old file deployed successfully
2) File uploaded before the cleanup
   <img width="807" height="416" alt="uploadedfile" src="https://github.com/user-attachments/assets/7bc80deb-f9bd-4c92-af03-1b3dd6059cc5" />  
3) Required permission applied
   <img width="883" height="582" alt="permission" src="https://github.com/user-attachments/assets/c11c5361-fbe9-4914-a354-f51cf110f306" />
4) After manual invocation of Lambda function old file deleted successfully and rest remain as it is.  
   <img width="718" height="337" alt="SuccessfullDelete" src="https://github.com/user-attachments/assets/02ff59f0-146f-47b2-ab0c-d00c8b0937c3" />
   <img width="810" height="442" alt="AfterDelete" src="https://github.com/user-attachments/assets/71f2a7f3-c4da-475d-ac7d-70ff28ee8f09" />
   <img width="1585" height="507" alt="CloudWatchLogs" src="https://github.com/user-attachments/assets/f334168a-513f-467b-a29e-a94c1e95e2e7" />  
## Assignment 7: DynamoDB Item Change Alert Using AWS Lambda, Boto3, and SNS  
1) DynamoDB table and Item created
   <img width="1197" height="811" alt="tableandItem" src="https://github.com/user-attachments/assets/a0d82833-4c13-4244-a643-a946905c3168" />
2) SNS topic and subscription created
   <img width="1572" height="725" alt="dbtopic" src="https://github.com/user-attachments/assets/add79111-b02c-46c4-bac6-69f51cd56310" />
   <img width="1561" height="310" alt="subscription" src="https://github.com/user-attachments/assets/fe6f49bc-ef9a-4504-bf19-2f52b943b5d9" />
3) Lambda function deployed to send MODIFY table notification to subscriber  
4) Required permission applied on lambda function
   <img width="1233" height="616" alt="permission-Role" src="https://github.com/user-attachments/assets/32c91271-4214-4928-87df-ac78bb14dce0" />
5) DynamoDB stream and trigger created
   <img width="1527" height="753" alt="DBStream and Trigger - enabled" src="https://github.com/user-attachments/assets/2753e788-2805-4674-b498-50322b214e6d" />  
6) Tested Modify table notification  
   <img width="1492" height="987" alt="Successful-email-notification-On-Modify" src="https://github.com/user-attachments/assets/3716cc3c-d9dc-45b0-b3b2-bf8dd8e7e39d" />  
   <img width="1492" height="922" alt="CloudWatch-log" src="https://github.com/user-attachments/assets/9e25aa1b-daad-4ca4-a531-380be73f0a15" />  
## Assignment 14: Monitor EC2 Instance State Changes Using AWS Lambda, Boto3, and SNS  
1) Lambda function to send notification of EC2 state change deployed successfully  
2) Required permission applied on lambda function
   <img width="1612" height="888" alt="permission" src="https://github.com/user-attachments/assets/bc7092b9-87bb-4150-80af-d71fef2aac57" />  
3) Eventbridge and trigger created for lambda
   <img width="1892" height="620" alt="Eventbridgerule" src="https://github.com/user-attachments/assets/42ced740-f1db-48d3-be73-f44c9e08e58a" />  
4) SNS topic and subscription created  
   <img width="1645" height="697" alt="EC2-topic-and-subscription" src="https://github.com/user-attachments/assets/30f1f45a-c25a-4dc1-a2ac-4a19f221d80a" />  
5) Verified the flow by stopping one of the random instance
   <img width="1478" height="517" alt="EC2-SNS-notification" src="https://github.com/user-attachments/assets/e32eb04f-47ac-43bf-9d66-a6138a866490" />  
   <img width="1471" height="577" alt="stopstate" src="https://github.com/user-attachments/assets/fc00749d-5301-4ba7-822e-9332e5f74890" />  
   <img width="1713" height="932" alt="cloudWatch" src="https://github.com/user-attachments/assets/03a7e7b9-4d8c-46da-88a0-b1c299948b7e" />  




   

