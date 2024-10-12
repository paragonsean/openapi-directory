# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.page_result_company_setting_dto import PageResultCompanySettingDto


pytestmark = pytest.mark.asyncio

async def test_company_settings_get(client):
    """Test case for company_settings_get

    Returns a list of company settings. Supports OData querying protocol.  Filtering is forbidden.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companySettings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

