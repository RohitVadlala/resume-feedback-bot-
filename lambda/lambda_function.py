import json
import boto3

def lambda_handler(event, context):
    try:
        body = json.loads(event['body']) if 'body' in event else {}
        resume = body.get("resume", "")
        job = body.get("job_description", "")

        if not resume or not job:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'resume and job_description are required'})
            }

        prompt = f"""
        Compare the following resume and job description. Provide 3 bullet points on how well the resume fits the job.

        Resume:
        {resume}

        Job Description:
        {job}
        """

        bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

        response = bedrock.invoke_model(
            modelId="anthropic.claude-instant-v1",
            contentType="application/json",
            accept="application/json",
            body=json.dumps({
                "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
                "max_tokens_to_sample": 500,
                "temperature": 0.5,
                "stop_sequences": ["\n\nHuman:"]
            })
        )

        result = json.loads(response['body'].read())
        return {
            'statusCode': 200,
            'body': json.dumps({'feedback': result.get("completion", "")})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
