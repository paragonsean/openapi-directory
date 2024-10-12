# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_get_item_input import BatchGetItemInput
from openapi_server.models.batch_get_item_output import BatchGetItemOutput
from openapi_server.models.batch_write_item_input import BatchWriteItemInput
from openapi_server.models.batch_write_item_output import BatchWriteItemOutput
from openapi_server.models.create_table_input import CreateTableInput
from openapi_server.models.create_table_output import CreateTableOutput
from openapi_server.models.delete_item_input import DeleteItemInput
from openapi_server.models.delete_item_output import DeleteItemOutput
from openapi_server.models.delete_table_input import DeleteTableInput
from openapi_server.models.delete_table_output import DeleteTableOutput
from openapi_server.models.describe_table_input import DescribeTableInput
from openapi_server.models.describe_table_output import DescribeTableOutput
from openapi_server.models.get_item_input import GetItemInput
from openapi_server.models.get_item_output import GetItemOutput
from openapi_server.models.list_tables_input import ListTablesInput
from openapi_server.models.list_tables_output import ListTablesOutput
from openapi_server.models.put_item_input import PutItemInput
from openapi_server.models.put_item_output import PutItemOutput
from openapi_server.models.query_input import QueryInput
from openapi_server.models.query_output import QueryOutput
from openapi_server.models.scan_input import ScanInput
from openapi_server.models.scan_output import ScanOutput
from openapi_server.models.update_item_input import UpdateItemInput
from openapi_server.models.update_item_output import UpdateItemOutput
from openapi_server.models.update_table_input import UpdateTableInput
from openapi_server.models.update_table_output import UpdateTableOutput


pytestmark = pytest.mark.asyncio

async def test_batch_get_item(client):
    """Test case for batch_get_item

    
    """
    body = {"RequestItems":{"key":{"Keys":[{"HashKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""},"RangeKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""}},{"HashKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""},"RangeKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""}},{"HashKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""},"RangeKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""}},{"HashKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""},"RangeKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""}},{"HashKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""},"RangeKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""}}],"AttributesToGet":[null,null],"ConsistentRead":True}}}
    params = [('RequestItems', 'request_items_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DynamoDB_20111205.BatchGetItem',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_write_item(client):
    """Test case for batch_write_item

    
    """
    body = {"RequestItems":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DynamoDB_20111205.BatchWriteItem',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_table(client):
    """Test case for create_table

    
    """
    body = {"TableName":"","ProvisionedThroughput":{"WriteCapacityUnits":"","ReadCapacityUnits":""},"KeySchema":{"HashKeyElement":{"AttributeType":"","AttributeName":""},"RangeKeyElement":{"AttributeType":"","AttributeName":""}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DynamoDB_20111205.CreateTable',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_item(client):
    """Test case for delete_item

    
    """
    body = {"TableName":"","Expected":{"key":{"Exists":"","Value":{"SS":"","BS":"","B":"","S":"","NS":"","N":""}}},"Key":{"HashKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""},"RangeKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""}},"ReturnValues":"NONE"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DynamoDB_20111205.DeleteItem',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_table(client):
    """Test case for delete_table

    
    """
    body = {"TableName":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DynamoDB_20111205.DeleteTable',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_table(client):
    """Test case for describe_table

    
    """
    body = {"TableName":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DynamoDB_20111205.DescribeTable',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_item(client):
    """Test case for get_item

    
    """
    body = {"TableName":"","AttributesToGet":[null,null],"Key":{"HashKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""},"RangeKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""}},"ConsistentRead":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DynamoDB_20111205.GetItem',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tables(client):
    """Test case for list_tables

    
    """
    body = {"Limit":8,"ExclusiveStartTableName":""}
    params = [('Limit', 'limit_example'),
                    ('ExclusiveStartTableName', 'exclusive_start_table_name_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DynamoDB_20111205.ListTables',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_item(client):
    """Test case for put_item

    
    """
    body = {"TableName":"","Item":{"key":{"SS":"","BS":"","B":"","S":"","NS":"","N":""}},"Expected":{"key":{"Exists":"","Value":{"SS":"","BS":"","B":"","S":"","NS":"","N":""}}},"ReturnValues":"NONE"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DynamoDB_20111205.PutItem',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query(client):
    """Test case for query

    
    """
    body = {"TableName":"","ScanIndexForward":"","RangeKeyCondition":{"ComparisonOperator":"EQ","AttributeValueList":[{"SS":"","BS":"","B":"","S":"","NS":"","N":""},{"SS":"","BS":"","B":"","S":"","NS":"","N":""}]},"HashKeyValue":{"SS":"","BS":"","B":"","S":"","NS":"","N":""},"ExclusiveStartKey":{"HashKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""},"RangeKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""}},"AttributesToGet":[null,null],"Limit":"","Count":"","ConsistentRead":True}
    params = [('Limit', 'limit_example'),
                    ('ExclusiveStartKey', 'exclusive_start_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DynamoDB_20111205.Query',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scan(client):
    """Test case for scan

    
    """
    body = {"TableName":"","ScanFilter":"","ExclusiveStartKey":{"HashKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""},"RangeKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""}},"AttributesToGet":[null,null],"Limit":"","Count":""}
    params = [('Limit', 'limit_example'),
                    ('ExclusiveStartKey', 'exclusive_start_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DynamoDB_20111205.Scan',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_item(client):
    """Test case for update_item

    
    """
    body = {"TableName":"","Expected":{"key":{"Exists":"","Value":{"SS":"","BS":"","B":"","S":"","NS":"","N":""}}},"Key":{"HashKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""},"RangeKeyElement":{"SS":"","BS":"","B":"","S":"","NS":"","N":""}},"AttributeUpdates":{"key":{"Action":"ADD","Value":{"SS":"","BS":"","B":"","S":"","NS":"","N":""}}},"ReturnValues":"NONE"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DynamoDB_20111205.UpdateItem',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_table(client):
    """Test case for update_table

    
    """
    body = {"TableName":"","ProvisionedThroughput":{"WriteCapacityUnits":"","ReadCapacityUnits":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'x_amz_target': 'x_amz_target_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/#X-Amz-Target=DynamoDB_20111205.UpdateTable',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

