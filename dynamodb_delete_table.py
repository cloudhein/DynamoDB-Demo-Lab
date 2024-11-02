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


# Delete Dynamodb Table
def delete_table(Transactions):
    table = dynamodb.Table(Transactions)
    table.delete()

# Call the delete function to delete the table
delete_table('Transactions')

###########################################################
#table_name = 'Transactions'

# Get the table resource
#table = dynamodb.Table(table_name)

# Delete the table
#response = table.delete()