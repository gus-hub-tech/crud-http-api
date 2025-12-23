# crud-http-api

A serverless CRUD API built with AWS Lambda, API Gateway, and DynamoDB for fast, scalable data operations.

## Architecture
<img width="627" height="122" alt="crud " src="https://github.com/user-attachments/assets/50940de1-1a48-4323-a6cc-46a2b56c0dcf" />

## Quick Setup

### 1. Create DynamoDB Table
- **Table name**: `http-crud-tutorial-items`
- **Partition key**: `id` (String)

<img width="1902" height="287" alt="dynodb-table" src="https://github.com/user-attachments/assets/bd16e9e2-7321-405b-b40c-899ff96dbb0c" />


### 2. Create Lambda Function
- **Function name**: `http-crud-tutorial-function`
- **Runtime**: Latest Node.js or Python
- **Role**: Create new with "Simple microservice permissions"

<img width="1876" height="580" alt="lambda" src="https://github.com/user-attachments/assets/db999ef4-4e40-49fa-8312-a748ab657251" />

### 3. Create HTTP API
- **API name**: `http-crud-tutorial-api`
- **IP type**: IPv4

<img width="1858" height="302" alt="http-api" src="https://github.com/user-attachments/assets/b82e98fc-42e8-43b0-8348-2ff189fce28c" />


### 4. Configure Routes

| Method | Path | Description |
|--------|------|-------------|
| GET | `/items/{id}` | Get single item |
| GET | `/items` | Get all items |
| PUT | `/items` | Create/update item |
| DELETE | `/items/{id}` | Delete item |

<img width="1481" height="672" alt="api-routes" src="https://github.com/user-attachments/assets/e4506093-be60-4490-816d-01d80fce3979" />


### 5. Create Integration
- **Type**: Lambda function
- **Function**: `http-crud-tutorial-function`
- Attach to all routes


<img width="1848" height="688" alt="attached-intergration" src="https://github.com/user-attachments/assets/1832ee5a-077d-47c0-9076-5e233cd9ce97" />


## Testing

Use the invoke URL from your API Gateway console:

<img width="676" height="112" alt="api-test" src="https://github.com/user-attachments/assets/fcfaade8-bea8-4302-a885-bf75d5b8766a" />


```bash
# Create item
curl -X PUT https://your-api-id.execute-api.region.amazonaws.com/items \
  -H "Content-Type: application/json" \
  -d '{"id": "123", "name": "Sample Item"}'

# Get all items
curl https://your-api-id.execute-api.region.amazonaws.com/items

# Get single item
curl https://your-api-id.execute-api.region.amazonaws.com/items/123

# Delete item
curl -X DELETE https://your-api-id.execute-api.region.amazonaws.com/items/123
```
<img width="1847" height="716" alt="dynamodb" src="https://github.com/user-attachments/assets/93eedc3b-97a2-4751-94ca-3ac49a07bd7a" />




## Features

- ✅ Serverless architecture
- ✅ Auto-scaling with DynamoDB
- ✅ RESTful API design
- ✅ AWS managed services
- ✅ Cost-effective pay-per-use model
