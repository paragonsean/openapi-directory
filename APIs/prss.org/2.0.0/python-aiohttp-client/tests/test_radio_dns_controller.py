# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_radiodns_spi31_gi_xml_get(client):
    """Test case for radiodns_spi31_gi_xml_get

    Get the group information document.
    """
    headers = { 
        'Accept': 'application/xml',
    }
    response = await client.request(
        method='GET',
        path='/radiodns/spi/3.1/GI.xml',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_radiodns_spi31_id_fqdn_sid_date_pi_xml_get(client):
    """Test case for radiodns_spi31_id_fqdn_sid_date_pi_xml_get

    Get the program information document.
    """
    headers = { 
        'Accept': 'application/xml',
        'x_radiodnsspi_api_key': 'x_radiodnsspi_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/radiodns/spi/3.1/id/{fqdn}/{sid}/{date_pi_xm}'.format(fqdn='fqdn_example', sid='sid_example', _date='_date_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_radiodns_spi31_si_xml_get(client):
    """Test case for radiodns_spi31_si_xml_get

    Get the service information document.
    """
    headers = { 
        'Accept': 'application/xml',
    }
    response = await client.request(
        method='GET',
        path='/radiodns/spi/3.1/SI.xml',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

