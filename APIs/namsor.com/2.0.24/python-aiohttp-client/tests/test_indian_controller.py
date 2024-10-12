# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_first_last_name_geo_in import BatchFirstLastNameGeoIn
from openapi_server.models.batch_first_last_name_geo_subclassification_out import BatchFirstLastNameGeoSubclassificationOut
from openapi_server.models.batch_personal_name_castegroup_out import BatchPersonalNameCastegroupOut
from openapi_server.models.batch_personal_name_geo_in import BatchPersonalNameGeoIn
from openapi_server.models.batch_personal_name_geo_subclassification_out import BatchPersonalNameGeoSubclassificationOut
from openapi_server.models.batch_personal_name_religioned_out import BatchPersonalNameReligionedOut
from openapi_server.models.batch_personal_name_subdivision_in import BatchPersonalNameSubdivisionIn
from openapi_server.models.first_last_name_geo_subclassification_out import FirstLastNameGeoSubclassificationOut
from openapi_server.models.personal_name_castegroup_out import PersonalNameCastegroupOut
from openapi_server.models.personal_name_geo_subclassification_out import PersonalNameGeoSubclassificationOut
from openapi_server.models.personal_name_religioned_out import PersonalNameReligionedOut


pytestmark = pytest.mark.asyncio

async def test_castegroup_indian_full(client):
    """Test case for castegroup_indian_full

    [USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of a personal full name.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/castegroupIndianFull/{sub_division_iso31662}/{personal_name_full}'.format(sub_division_iso31662='sub_division_iso31662_example', personal_name_full='personal_name_full_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_castegroup_indian_full_batch(client):
    """Test case for castegroup_indian_full_batch

    [USES 10 UNITS PER NAME] Infer the likely Indian name castegroup of up to 100 personal full names. 
    """
    body = {"personalNames":[{"subdivisionIso":"subdivisionIso","name":"name","id":"id"},{"subdivisionIso":"subdivisionIso","name":"name","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/castegroupIndianFullBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_religion(client):
    """Test case for religion

    [USES 10 UNITS PER NAME] Infer the likely religion of a personal Indian full name, provided the Indian state or Union territory (NB/ this can be inferred using the subclassification endpoint).
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/religionIndianFull/{sub_division_iso31662}/{personal_name_full}'.format(sub_division_iso31662='sub_division_iso31662_example', personal_name_full='personal_name_full_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_religion_indian_full_batch(client):
    """Test case for religion_indian_full_batch

    [USES 10 UNITS PER NAME] Infer the likely religion of up to 100 personal full Indian names, provided the subclassification at State or Union territory level (NB/ can be inferred using the subclassification endpoint).
    """
    body = {"personalNames":[{"subdivisionIso":"subdivisionIso","name":"name","id":"id"},{"subdivisionIso":"subdivisionIso","name":"name","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/religionIndianFullBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subclassification_indian(client):
    """Test case for subclassification_indian

    [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on the name.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/subclassificationIndian/{first_name}/{last_name}'.format(first_name='first_name_example', last_name='last_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subclassification_indian_batch(client):
    """Test case for subclassification_indian_batch

    [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on a list of up to 100 names.
    """
    body = {"personalNames":[{"firstName":"firstName","lastName":"lastName","countryIso2":"countryIso2","id":"id"},{"firstName":"firstName","lastName":"lastName","countryIso2":"countryIso2","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/subclassificationIndianBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subclassification_indian_full(client):
    """Test case for subclassification_indian_full

    [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on the name.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/subclassificationIndianFull/{full_name}'.format(full_name='full_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subclassification_indian_full_batch(client):
    """Test case for subclassification_indian_full_batch

    [USES 10 UNITS PER NAME] Infer the likely Indian state of Union territory according to ISO 3166-2:IN based on a list of up to 100 names.
    """
    body = {"personalNames":[{"name":"name","countryIso2":"countryIso2","id":"id"},{"name":"name","countryIso2":"countryIso2","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/subclassificationIndianFullBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

