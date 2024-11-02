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


# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='Transactions',
    KeySchema=[
        {
            'AttributeName': 'TransactionType',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Date',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'TransactionType',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Date',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 2,
        'WriteCapacityUnits': 2
    }
)

# Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)