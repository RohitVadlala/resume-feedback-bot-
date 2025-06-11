# 🧠 GenAI Resume Feedback Bot (AWS Bedrock + Claude)

This is a serverless resume analyzer powered by Anthropic's Claude via Amazon Bedrock. It compares a resume with a job description and gives feedback in plain language — deployed using AWS Lambda and API Gateway (free-tier friendly).

## ✨ Features
- Uses `Claude Instant` from Amazon Bedrock
- Serverless with AWS Lambda and API Gateway
- JSON-based input/output for easy integration
- Zero infrastructure management
- Free-tier compatible (no hourly inference profiles)

## 🚀 How It Works
1. User sends resume + job description to API Gateway.
2. Lambda triggers Claude Instant via Bedrock.
3. Model returns 3-point feedback.
4. JSON response is sent back to client.

## 📦 Sample Payload

```json
{
  "resume": "Experienced data analyst with Python and AWS expertise...",
  "job_description": "Hiring a data analyst with AWS and Python skills."
}
