# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.get_distance200_response import GetDistance200Response
from openapi_server.models.get_msagroups200_response import GetMsagroups200Response
from openapi_server.models.get_msagroups_msacode200_response import GetMsagroupsMsacode200Response
from openapi_server.models.get_radius200_response import GetRadius200Response
from openapi_server.models.get_radius400_response import GetRadius400Response
from openapi_server.models.get_radius401_response import GetRadius401Response
from openapi_server.models.get_zipc_v1401_response import GetZipcV1401Response
from openapi_server.models.get_zipcode200_response import GetZipcode200Response
from openapi_server.models.get_zipcode401_response import GetZipcode401Response
from openapi_server.models.get_zipcode403_response import GetZipcode403Response
from openapi_server.models.zip_code_response import ZipCodeResponse


pytestmark = pytest.mark.asyncio

async def test_get_distance(client):
    """Test case for get_distance

    Distance Between 2 Zip Codes
    """
    params = [('zipCode1', '90210'),
                    ('zipCode2', '33162')]
    headers = { 
        'Accept': 'application/json',
        'subscription-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/zipc/v1/distance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_msagroups(client):
    """Test case for get_msagroups

    List All MSA Groups
    """
    params = [('limit', 56),
                    ('offset', 56),
                    ('stateCode', 'CA')]
    headers = { 
        'Accept': 'application/json',
        'subscription-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/zipc/v1/msagroups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_msagroups_msacode(client):
    """Test case for get_msagroups_msacode

    Metro/Micro Statistical Area Details
    """
    headers = { 
        'Accept': 'application/json',
        'subscription-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/zipc/v1/msagroups/{msa_code}'.format(msa_code='11580'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_radius(client):
    """Test case for get_radius

    Zip Code Radius
    """
    params = [('zipCode', 'zip_code_example'),
                    ('radius', 56),
                    ('uom', 'mi')]
    headers = { 
        'Accept': 'application/json',
        'subscription-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/zipc/v1/radius',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_zipc_v1(client):
    """Test case for get_zipc_v1

    Validate License Key
    """
    headers = { 
        'Accept': 'application/json',
        'subscription-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/zipc/v1',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_zipcode(client):
    """Test case for get_zipcode

    Zip Code Details
    """
    headers = { 
        'Accept': 'application/json',
        'subscription-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/zipc/v1/zipcodes/{zipcode}'.format(zipcode='zipcode_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_zipcodes(client):
    """Test case for get_zipcodes

    List all Zip Codes
    """
    params = [('offset', 10),
                    ('limit', 10),
                    ('zipcode', '90210,33162'),
                    ('uspsMainCityKey', 'Z20259'),
                    ('zipClassificationCode', 'P'),
                    ('uspsFacilityCode', 'B'),
                    ('uspsDeliveryCode', 'usps_delivery_code_example'),
                    ('uspsCarrierRouteSortCode', 'usps_carrier_route_sort_code_example'),
                    ('uniqueZipNameInd', True),
                    ('uspsFinanceNumber', 'usps_finance_number_example'),
                    ('stateCode', 'CA'),
                    ('stateFipsCode', '06'),
                    ('countyFipsCode', '037'),
                    ('divisionCode', '9'),
                    ('regionCode', '4'),
                    ('msaCode', '31080')]
    headers = { 
        'Accept': 'application/json',
        'subscription-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/zipc/v1/zipcodes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

