import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
	client = boto3.resource('dynamodb')
	table = client.Table('Transactions')

	#1. Example - Get Item By Id

	response = table.get_item(
		Key={
			'TransactionType': 'PURCHASE_USA',
			'Date': '2024-10-15'
		}
	)

	print(response['Item'])

	print('\n\n\n-----\n\n\n')

	#2. Example 2 - Query by Partition Key / Sort Key Criteria

	response = table.query(
		KeyConditionExpression=Key('TransactionType').eq('PURCHASE_USA') & Key('Date').gt('2024-10-15')
	)

	items = response['Items']
	for item in items:
		print(item)