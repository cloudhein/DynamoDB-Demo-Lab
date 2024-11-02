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

item = {
        'TransactionType': 'PURCHASE_USA',
        'Date': '2024-10-15',
        'amount': 1000,
        'description': 'Test Transaction'
    }

# Put item into Dynamodb Table
def put_item(Transactions, item):
    table = dynamodb.Table(Transactions)
    table.put_item(Item=item)

# Call the put function
put_item('Transactions', item)

