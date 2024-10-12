# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.sms200_response import Sms200Response


pytestmark = pytest.mark.asyncio

async def test_sms(client):
    """Test case for sms

    
    """
    params = [('text', 'text_example'),
                    ('to', 'to_example'),
                    ('from', '_from_example'),
                    ('foreign_id', 'foreign_id_example'),
                    ('label', 'label_example'),
                    ('udh', 'udh_example'),
                    ('delay', 'delay_example'),
                    ('debug', 0),
                    ('no_reload', 0),
                    ('unicode', 0),
                    ('flash', 0),
                    ('utf8', 0),
                    ('details', 0),
                    ('return_msg_id', 0),
                    ('json', 0),
                    ('performance_tracking', 0)]
    headers = { 
        'Accept': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/sms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

