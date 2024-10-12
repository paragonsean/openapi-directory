# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_list_available_email_templates_0(client):
    """Test case for list_available_email_templates_0

    List Available Email Templates
    """
    params = [('modified_after', '2020-01-01T01:01:01.000000'),
                    ('modified_before', '2020-02-01T01:01:01.000000'),
                    ('limit', '1'),
                    ('offset', '0')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/templates/email/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_see_email_template_information_0(client):
    """Test case for see_email_template_information_0

    See Email Template Information
    """
    params = [('email_template_id', '{{email_template_id}}')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/templates/email/info',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

