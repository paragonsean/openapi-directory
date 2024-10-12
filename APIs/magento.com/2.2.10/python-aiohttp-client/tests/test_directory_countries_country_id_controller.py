# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.directory_data_country_information_interface import DirectoryDataCountryInformationInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_directory_country_information_acquirer_v1_get_country_info_get(client):
    """Test case for directory_country_information_acquirer_v1_get_country_info_get

    directory/countries/{countryId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/directory/countries/{country_id}'.format(country_id='country_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

