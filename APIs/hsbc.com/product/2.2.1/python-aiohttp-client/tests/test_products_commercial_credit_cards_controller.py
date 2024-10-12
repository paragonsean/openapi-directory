# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ccc_definition_meta import CCCDefinitionMeta
from openapi_server.models.error_definition400 import ErrorDefinition400
from openapi_server.models.error_definition408 import ErrorDefinition408
from openapi_server.models.error_definition429 import ErrorDefinition429
from openapi_server.models.error_definition500 import ErrorDefinition500
from openapi_server.models.error_definition503 import ErrorDefinition503


pytestmark = pytest.mark.asyncio

async def test_open_banking_v22_commercial_credit_cards_get(client):
    """Test case for open_banking_v22_commercial_credit_cards_get

    
    """
    headers = { 
        'Accept': 'application/prs.openbanking.opendata.v2.2+json',
    }
    response = await client.request(
        method='GET',
        path='/open-banking/v2.2/commercial-credit-cards',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_x_open_banking_v22_commercial_credit_cards_segment_segment_get(client):
    """Test case for x_open_banking_v22_commercial_credit_cards_segment_segment_get

    
    """
    headers = { 
        'Accept': 'application/prs.openbanking.opendata.v2.2+json',
    }
    response = await client.request(
        method='GET',
        path='/x-open-banking/v2.2/commercial-credit-cards/segment/{segment}'.format(segment='segment_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

