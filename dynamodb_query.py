import json
import boto3
from boto3.dynamodb.conditions import Key
import constants

# Initialize DynamoDB resource with specified region
client = boto3.resource(
    'dynamodb',
    region_name=constants.AWS_REGION,
    aws_access_key_id=constants.access_key,
    aws_secret_access_key=constants.secret_access_key
)
table = client.Table('Transactions')

# Example 1: Get Item By Id
response = table.get_item(
    Key={
        'TransactionType': 'PURCHASE_USA',
        'Date': '2024-10-15'
    }
)

if 'Item' in response:
    print("Retrieved Item:")
    print(response['Item'])
else:
    print("Item not found.")

print('\n-----\n')

# Example 2: Query by Partition Key / Sort Key Criteria
response = table.query(
    KeyConditionExpression=Key('TransactionType').eq('PURCHASE_USA') & Key('Date').lt('2024-10-15')
)

items = response.get('Items', [])
if items:
    print("Queried Items:")
    for item in items:
        print(item)
else:
    print("No items found matching the query.")
