# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_a_batch_of_business_transaction_classification_results200_response import GetABatchOfBusinessTransactionClassificationResults200Response


pytestmark = pytest.mark.asyncio

async def test_get_a_batch_of_business_transaction_classification_results_1(client):
    """Test case for get_a_batch_of_business_transaction_classification_results_1

    Get a batch of business transaction classification results.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/classifier/business/batch/{id}'.format(id='247ee045-3d04-4b3c-872b-a9160b810f33'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

