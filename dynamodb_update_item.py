import boto3
import constants

# Get the service resource.
#dynamodb = boto3.resource('dynamodb')
dynamodb = boto3.resource(
    'dynamodb',
    region_name=constants.AWS_REGION,
    aws_access_key_id=constants.access_key,
    aws_secret_access_key=constants.secret_access_key
)

# Update an item with update_item()
table = dynamodb.Table('Transactions')
table.update_item(
    Key={
        'TransactionType': 'PURCHASE_USA',
        'Date': '2024-10-15'
    },
    UpdateExpression='SET amount = :val1, description = :val2',
    ExpressionAttributeValues={
        ':val1': 200,
        ":val2": "Updated Description"
    }
)



