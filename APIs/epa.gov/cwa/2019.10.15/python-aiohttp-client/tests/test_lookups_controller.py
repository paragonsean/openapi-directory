# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rest_lookups_bp_tribes_get200_response import RestLookupsBpTribesGet200Response
from openapi_server.models.rest_lookups_cwa_parameters_get200_response import RestLookupsCwaParametersGet200Response
from openapi_server.models.rest_lookups_cwa_pollutants_get200_response import RestLookupsCwaPollutantsGet200Response
from openapi_server.models.rest_lookups_federal_agencies_get200_response import RestLookupsFederalAgenciesGet200Response
from openapi_server.models.rest_lookups_icis_inspection_types_get200_response import RestLookupsIcisInspectionTypesGet200Response
from openapi_server.models.rest_lookups_icis_law_sections_get200_response import RestLookupsIcisLawSectionsGet200Response
from openapi_server.models.rest_lookups_naics_codes_get200_response import RestLookupsNaicsCodesGet200Response
from openapi_server.models.rest_lookups_npdes_parameters_get200_response import RestLookupsNpdesParametersGet200Response
from openapi_server.models.rest_lookups_wbd_code_lu_get200_response import RestLookupsWbdCodeLuGet200Response
from openapi_server.models.rest_lookups_wbd_name_lu_get200_response import RestLookupsWbdNameLuGet200Response


pytestmark = pytest.mark.asyncio

async def test_rest_lookups_bp_tribes_get(client):
    """Test case for rest_lookups_bp_tribes_get

    ECHO BP Tribes Lookup Service
    """
    params = [('output', 'output_example'),
                    ('callback', 'param_callback_example'),
                    ('search_term', 'search_term_example'),
                    ('search_code', 'search_code_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/rest_lookups.bp_tribes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_rest_lookups_bp_tribes_post(client):
    """Test case for rest_lookups_bp_tribes_post

    ECHO BP Tribes Lookup Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'param_callback': 'param_callback_example',
        'search_term': 'search_term_example',
        'search_code': 'search_code_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/rest_lookups.bp_tribes',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_lookups_cwa_parameters_get(client):
    """Test case for rest_lookups_cwa_parameters_get

    ECHO CWA Parameter Lookup Service
    """
    params = [('output', 'output_example'),
                    ('callback', 'param_callback_example'),
                    ('search_term', 'search_term_example'),
                    ('search_code', 'search_code_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/rest_lookups.cwa_parameters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_rest_lookups_cwa_parameters_post(client):
    """Test case for rest_lookups_cwa_parameters_post

    ECHO CWA Parameter Lookup Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'param_callback': 'param_callback_example',
        'search_term': 'search_term_example',
        'search_code': 'search_code_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/rest_lookups.cwa_parameters',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_lookups_cwa_pollutants_get(client):
    """Test case for rest_lookups_cwa_pollutants_get

    ECHO CWA Pollutants Lookup Service
    """
    params = [('output', 'output_example'),
                    ('callback', 'param_callback_example'),
                    ('search_term', 'search_term_example'),
                    ('search_code', 'search_code_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/rest_lookups.cwa_pollutants',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_rest_lookups_cwa_pollutants_post(client):
    """Test case for rest_lookups_cwa_pollutants_post

    ECHO CWA Pollutants Lookup Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'param_callback': 'param_callback_example',
        'search_term': 'search_term_example',
        'search_code': 'search_code_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/rest_lookups.cwa_pollutants',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_lookups_federal_agencies_get(client):
    """Test case for rest_lookups_federal_agencies_get

    ECHO Federal Agency Lookup Service
    """
    params = [('output', 'output_example'),
                    ('callback', 'param_callback_example'),
                    ('search_term', 'search_term_example'),
                    ('search_code', 'search_code_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/rest_lookups.federal_agencies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_rest_lookups_federal_agencies_post(client):
    """Test case for rest_lookups_federal_agencies_post

    ECHO Federal Agency Lookup Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'param_callback': 'param_callback_example',
        'search_term': 'search_term_example',
        'search_code': 'search_code_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/rest_lookups.federal_agencies',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_lookups_icis_inspection_types_get(client):
    """Test case for rest_lookups_icis_inspection_types_get

    ECHO ICIS NPDES Inspection Types Lookup Service
    """
    params = [('output', 'output_example'),
                    ('callback', 'param_callback_example'),
                    ('search_term', 'search_term_example'),
                    ('search_code', 'search_code_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/rest_lookups.icis_inspection_types',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_rest_lookups_icis_inspection_types_post(client):
    """Test case for rest_lookups_icis_inspection_types_post

    ECHO ICIS NPDES Inspection Types Lookup Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'param_callback': 'param_callback_example',
        'search_term': 'search_term_example',
        'search_code': 'search_code_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/rest_lookups.icis_inspection_types',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_lookups_icis_law_sections_get(client):
    """Test case for rest_lookups_icis_law_sections_get

    ECHO ICIS NPDES Law Sections Lookup Service
    """
    params = [('output', 'output_example'),
                    ('callback', 'param_callback_example'),
                    ('statute_code', 'statute_code_example'),
                    ('status_flag', 'status_flag_example'),
                    ('search_term', 'search_term_example'),
                    ('search_code', 'search_code_example'),
                    ('sort_order', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/rest_lookups.icis_law_sections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_rest_lookups_icis_law_sections_post(client):
    """Test case for rest_lookups_icis_law_sections_post

    ECHO ICIS NPDES Law Sections Lookup Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'param_callback': 'param_callback_example',
        'statute_code': 'statute_code_example',
        'status_flag': 'status_flag_example',
        'search_term': 'search_term_example',
        'search_code': 'search_code_example',
        'sort_order': 3.4
        }
    response = await client.request(
        method='POST',
        path='/echo/rest_lookups.icis_law_sections',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_lookups_naics_codes_get(client):
    """Test case for rest_lookups_naics_codes_get

    ECHO NAICS Codes Lookup Service
    """
    params = [('output', 'output_example'),
                    ('callback', 'param_callback_example'),
                    ('search_term', 'search_term_example'),
                    ('search_code', 'search_code_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/rest_lookups.naics_codes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_rest_lookups_naics_codes_post(client):
    """Test case for rest_lookups_naics_codes_post

    ECHO NAICS Codes Lookup Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'param_callback': 'param_callback_example',
        'search_term': 'search_term_example',
        'search_code': 'search_code_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/rest_lookups.naics_codes',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_lookups_npdes_parameters_get(client):
    """Test case for rest_lookups_npdes_parameters_get

    ECHO NPDES Parameters Lookup Service
    """
    params = [('output', 'output_example'),
                    ('callback', 'param_callback_example'),
                    ('search_term', 'search_term_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/rest_lookups.npdes_parameters',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_rest_lookups_npdes_parameters_post(client):
    """Test case for rest_lookups_npdes_parameters_post

    ECHO NPDES Parameters Lookup Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'param_callback': 'param_callback_example',
        'search_term': 'search_term_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/rest_lookups.npdes_parameters',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_lookups_wbd_code_lu_get(client):
    """Test case for rest_lookups_wbd_code_lu_get

    ECHO WBD Code Lookup Service
    """
    params = [('output', 'output_example'),
                    ('callback', 'param_callback_example'),
                    ('wbd_code', 'wbd_code_example'),
                    ('wbd_level', 'wbd_level_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/rest_lookups.wbd_code_lu',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_rest_lookups_wbd_code_lu_post(client):
    """Test case for rest_lookups_wbd_code_lu_post

    ECHO WBD Code Lookup Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'param_callback': 'param_callback_example',
        'wbd_code': 'wbd_code_example',
        'wbd_level': 'wbd_level_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/rest_lookups.wbd_code_lu',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rest_lookups_wbd_name_lu_get(client):
    """Test case for rest_lookups_wbd_name_lu_get

    ECHO WBD Name Lookup Service
    """
    params = [('output', 'output_example'),
                    ('callback', 'param_callback_example'),
                    ('wbd_name', 'wbd_name_example'),
                    ('wbd_level', 'wbd_level_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/echo/rest_lookups.wbd_name_lu',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_rest_lookups_wbd_name_lu_post(client):
    """Test case for rest_lookups_wbd_name_lu_post

    ECHO WBD Name Lookup Service
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'output': 'output_example',
        'param_callback': 'param_callback_example',
        'wbd_name': 'wbd_name_example',
        'wbd_level': 'wbd_level_example'
        }
    response = await client.request(
        method='POST',
        path='/echo/rest_lookups.wbd_name_lu',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

