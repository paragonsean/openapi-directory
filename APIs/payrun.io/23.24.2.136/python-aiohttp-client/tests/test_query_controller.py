# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.query import Query


pytestmark = pytest.mark.asyncio

async def test_get_query_response(client):
    """Test case for get_query_response

    Get the query result
    """
    body = {"Query":{"Variables":{"Variable":[{"@Name":"@Name","@Value":"@Value"},{"@Name":"@Name","@Value":"@Value"}]},"ExcludeNullOrEmptyElements":True,"Groups":{"Group":[{"Condition":[{"@ValueB":"@ValueB","@ValueA":"@ValueA"},{"@ValueB":"@ValueB","@ValueA":"@ValueA"}],"Order":[{"@Property":"@Property"},{"@Property":"@Property"}],"@UniqueKeyVariable":"@UniqueKeyVariable","@Predicate":"@Predicate","@Selector":"@Selector","Filter":[{"@Property":"@Property","@IsOr":True,"@Value":"@Value"},{"@Property":"@Property","@IsOr":True,"@Value":"@Value"}],"Output":[{"@Output":"Element","@MaxLength":"@MaxLength"},{"@Output":"Element","@MaxLength":"@MaxLength"}],"@LoopExpression":"@LoopExpression","@GroupName":"@GroupName","@ItemName":"@ItemName"},{"Condition":[{"@ValueB":"@ValueB","@ValueA":"@ValueA"},{"@ValueB":"@ValueB","@ValueA":"@ValueA"}],"Order":[{"@Property":"@Property"},{"@Property":"@Property"}],"@UniqueKeyVariable":"@UniqueKeyVariable","@Predicate":"@Predicate","@Selector":"@Selector","Filter":[{"@Property":"@Property","@IsOr":True,"@Value":"@Value"},{"@Property":"@Property","@IsOr":True,"@Value":"@Value"}],"Output":[{"@Output":"Element","@MaxLength":"@MaxLength"},{"@Output":"Element","@MaxLength":"@MaxLength"}],"@LoopExpression":"@LoopExpression","@GroupName":"@GroupName","@ItemName":"@ItemName"}]},"Encoding":"Encoding","RootNodeName":"RootNodeName","SuppressMetricAttributes":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Query',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

