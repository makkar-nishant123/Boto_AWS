
import logging
logger = logging.getLogger(__name__)
from botocore.exceptiomport ClientError
import boto3

api_client = boto3.client('apigateway')
# Create rest api
rest_api = api_client.create_rest_api(
    name='GreatApi'
)



rest_api_id = rest_api["id"]

# Get the rest api's root id
root_resource_id = api_client.get_resources(
    restApiId=rest_api_id
)['items'][0]['id']
    
# Create an api resource
api_resource = api_client.create_resource(
    restApiId=rest_api_id,
    parentId=root_resource_id,
    pathPart='greeting'
)

api_resource_id = api_resource['id']

# Add a post method to the rest api resource
api_method = api_client.put_method(
    restApiId=rest_api_id,
    resourceId=api_resource_id,
    httpMethod='GET',
    authorizationType='NONE',
    requestParameters={
    'method.request.querystring.greeter': False
    }
)

print(api_method)

put_method_res = api_client.put_method_response(
    restApiId=rest_api_id,
    resourceId=api_resource_id,
    httpMethod='GET',
    statusCode='200'
)

print(put_method_res)

# The uri comes from a base lambda string with the function ARN attached to it
arn_uri="arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:<user_id>:function:HelloWorld/invocations"
