import json
import boto3
from decimal import Decimal

client = boto3.client('dynamodb')
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table('http-crud-tutorial-items')
tableName = 'http-crud-tutorial-items'


def lambda_handler(event, context):
    print("Full event received:")
    print(json.dumps(event, indent=2, default=str))
    
    statusCode = 200
    headers = {
        "Content-Type": "application/json"
    }

    try:
        # Try to get routeKey (HTTP API) or fall back to resource + httpMethod (REST API)
        route_key = None
        
        if 'routeKey' in event:
            route_key = event['routeKey']
        elif 'resource' in event and 'httpMethod' in event:
            # Construct a routeKey-like string from REST API event
            route_key = f"{event['httpMethod']} {event['resource']}"
        else:
            # Event doesn't match expected API Gateway format
            statusCode = 400
            body = {
                "error": "Invalid event format",
                "message": "This Lambda expects to be invoked by API Gateway",
                "receivedKeys": list(event.keys()),
                "hint": "Make sure API Gateway is configured as a trigger"
            }
            return {
                "statusCode": statusCode,
                "headers": headers,
                "body": json.dumps(body)
            }

        # Handle routes
        if route_key == "DELETE /items/{id}":
            table.delete_item(
                Key={'id': event['pathParameters']['id']})
            body = 'Deleted item ' + event['pathParameters']['id']
            
        elif route_key == "GET /items/{id}":
            response = table.get_item(
                Key={'id': event['pathParameters']['id']})
            item = response["Item"]
            body = [
                {'price': float(item['price']), 'id': item['id'], 'name': item['name']}
            ]
            
        elif route_key == "GET /items":
            response = table.scan()
            items = response["Items"]
            print("ITEMS----")
            print(items)
            body = []
            for item in items:
                body.append({
                    'price': float(item['price']), 
                    'id': item['id'], 
                    'name': item['name']
                })
                
        elif route_key == "PUT /items":
            requestJSON = json.loads(event['body'])
            table.put_item(
                Item={
                    'id': requestJSON['id'],
                    'price': Decimal(str(requestJSON['price'])),
                    'name': requestJSON['name']
                })
            body = 'Put item ' + requestJSON['id']
            
        else:
            statusCode = 400
            body = f'Unsupported route: {route_key}'
            
    except KeyError as e:
        statusCode = 400
        body = {
            "error": "Missing required field",
            "field": str(e),
            "message": f"The request is missing required field: {str(e)}"
        }
    except Exception as e:
        statusCode = 500
        body = {
            "error": "Internal server error",
            "message": str(e)
        }
    
    return {
        "statusCode": statusCode,
        "headers": headers,
        "body": json.dumps(body)
    }
