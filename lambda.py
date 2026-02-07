import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("StudentRegister")

def lambda_handler(event, context):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Content-Type": "application/json"
    }
    
    try:
        # Handle data from both Test Event and API Gateway
        body = json.loads(event["body"]) if "body" in event else event
        
        # Save to DynamoDB
        table.put_item(Item={
            "studentId": str(body.get("studentId")),
            "name": body.get("name"),
            "email": body.get("email"),
            "course": body.get("course")
        })

        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps({"message": "Student registered successfully!"})
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "headers": headers,
            "body": json.dumps({"error": str(e)})
        }