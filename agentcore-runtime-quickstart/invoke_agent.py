import json
import uuid
import boto3

agent_arn = "<Add your ARN>"
prompt = "Tell me a joke"

# Initialize the AgentCore client
agent_core_client = boto3.client('bedrock-agentcore')

# Prepare the payload
payload = json.dumps({"prompt": prompt}).encode()

# Invoke the agent
response = agent_core_client.invoke_agent_runtime(
    agentRuntimeArn=agent_arn,
    runtimeSessionId=str(uuid.uuid4()),
    payload=payload,
    qualifier="DEFAULT"
)

content = []
for chunk in response.get("response", []):
    content.append(chunk.decode('utf-8'))
print(json.loads(''.join(content)))
