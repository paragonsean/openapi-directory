# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_test_card_ranges_request import CreateTestCardRangesRequest
from openapi_server.models.create_test_card_ranges_result import CreateTestCardRangesResult
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_post_create_test_card_ranges(client):
    """Test case for post_create_test_card_ranges

    Creates one or more test card ranges.
    """
    body = {"accountCode":"accountCode","accountTypeCode":"accountTypeCode","testCardRanges":[{"cvc":"cvc","address":{"zip":"zip","streetAddress":"streetAddress"},"rangeStart":"rangeStart","threeDDirectoryServerResponse":"N","cardHolderName":"cardHolderName","threeDUsername":"threeDUsername","expiryMonth":"APRIL","threeDPassword":"threeDPassword","expiryYear":0,"rangeEnd":"rangeEnd"},{"cvc":"cvc","address":{"zip":"zip","streetAddress":"streetAddress"},"rangeStart":"rangeStart","threeDDirectoryServerResponse":"N","cardHolderName":"cardHolderName","threeDUsername":"threeDUsername","expiryMonth":"APRIL","threeDPassword":"threeDPassword","expiryYear":0,"rangeEnd":"rangeEnd"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/pal/services/TestCard/v1/createTestCardRanges',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

