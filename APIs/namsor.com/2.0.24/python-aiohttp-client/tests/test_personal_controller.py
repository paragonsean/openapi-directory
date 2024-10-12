# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_corridor_in import BatchCorridorIn
from openapi_server.models.batch_corridor_out import BatchCorridorOut
from openapi_server.models.batch_first_last_name_diasporaed_out import BatchFirstLastNameDiasporaedOut
from openapi_server.models.batch_first_last_name_gendered_out import BatchFirstLastNameGenderedOut
from openapi_server.models.batch_first_last_name_geo_in import BatchFirstLastNameGeoIn
from openapi_server.models.batch_first_last_name_geo_subclassification_out import BatchFirstLastNameGeoSubclassificationOut
from openapi_server.models.batch_first_last_name_geo_zipped_in import BatchFirstLastNameGeoZippedIn
from openapi_server.models.batch_first_last_name_in import BatchFirstLastNameIn
from openapi_server.models.batch_first_last_name_origined_out import BatchFirstLastNameOriginedOut
from openapi_server.models.batch_first_last_name_us_race_ethnicity_out import BatchFirstLastNameUSRaceEthnicityOut
from openapi_server.models.batch_personal_name_gendered_out import BatchPersonalNameGenderedOut
from openapi_server.models.batch_personal_name_geo_in import BatchPersonalNameGeoIn
from openapi_server.models.batch_personal_name_geo_out import BatchPersonalNameGeoOut
from openapi_server.models.batch_personal_name_geo_subclassification_out import BatchPersonalNameGeoSubclassificationOut
from openapi_server.models.batch_personal_name_geo_subdivision_in import BatchPersonalNameGeoSubdivisionIn
from openapi_server.models.batch_personal_name_in import BatchPersonalNameIn
from openapi_server.models.batch_personal_name_parsed_out import BatchPersonalNameParsedOut
from openapi_server.models.batch_personal_name_religioned_out import BatchPersonalNameReligionedOut
from openapi_server.models.corridor_out import CorridorOut
from openapi_server.models.first_last_name_diasporaed_out import FirstLastNameDiasporaedOut
from openapi_server.models.first_last_name_gendered_out import FirstLastNameGenderedOut
from openapi_server.models.first_last_name_geo_subclassification_out import FirstLastNameGeoSubclassificationOut
from openapi_server.models.first_last_name_origined_out import FirstLastNameOriginedOut
from openapi_server.models.first_last_name_us_race_ethnicity_out import FirstLastNameUSRaceEthnicityOut
from openapi_server.models.personal_name_gendered_out import PersonalNameGenderedOut
from openapi_server.models.personal_name_geo_out import PersonalNameGeoOut
from openapi_server.models.personal_name_parsed_out import PersonalNameParsedOut
from openapi_server.models.personal_name_religioned_out import PersonalNameReligionedOut


pytestmark = pytest.mark.asyncio

async def test_corridor(client):
    """Test case for corridor

    [USES 20 UNITS PER NAME COUPLE] Infer several classifications for a cross border interaction between names (ex. remit, travel, intl com)
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/corridor/{country_iso2_from}/{first_name_from}/{last_name_from}/{country_iso2_to}/{first_name_to}/{last_name_to}'.format(country_iso2_from='country_iso2_from_example', first_name_from='first_name_from_example', last_name_from='last_name_from_example', country_iso2_to='country_iso2_to_example', first_name_to='first_name_to_example', last_name_to='last_name_to_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_corridor_batch(client):
    """Test case for corridor_batch

    [USES 20 UNITS PER NAME PAIR] Infer several classifications for up to 100 cross border interaction between names (ex. remit, travel, intl com)
    """
    body = {"corridorFromTo":[{"firstLastNameGeoTo":{"firstName":"firstName","lastName":"lastName","countryIso2":"countryIso2","id":"id"},"firstLastNameGeoFrom":{"firstName":"firstName","lastName":"lastName","countryIso2":"countryIso2","id":"id"},"id":"id"},{"firstLastNameGeoTo":{"firstName":"firstName","lastName":"lastName","countryIso2":"countryIso2","id":"id"},"firstLastNameGeoFrom":{"firstName":"firstName","lastName":"lastName","countryIso2":"countryIso2","id":"id"},"id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/corridorBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_country(client):
    """Test case for country

    [USES 10 UNITS PER NAME] Infer the likely country of residence of a personal full name, or one surname. Assumes names as they are in the country of residence OR the country of origin.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/country/{personal_name_full}'.format(personal_name_full='personal_name_full_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_country_batch(client):
    """Test case for country_batch

    [USES 10 UNITS PER NAME] Infer the likely country of residence of up to 100 personal full names, or surnames. Assumes names as they are in the country of residence OR the country of origin.
    """
    body = {"personalNames":[{"name":"name","id":"id"},{"name":"name","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/countryBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diaspora(client):
    """Test case for diaspora

    [USES 20 UNITS PER NAME] Infer the likely ethnicity/diaspora of a personal name, given a country of residence ISO2 code (ex. US, CA, AU, NZ etc.)
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/diaspora/{country_iso2}/{first_name}/{last_name}'.format(country_iso2='country_iso2_example', first_name='first_name_example', last_name='last_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diaspora_batch(client):
    """Test case for diaspora_batch

    [USES 20 UNITS PER NAME] Infer the likely ethnicity/diaspora of up to 100 personal names, given a country of residence ISO2 code (ex. US, CA, AU, NZ etc.)
    """
    body = {"personalNames":[{"firstName":"firstName","lastName":"lastName","countryIso2":"countryIso2","id":"id"},{"firstName":"firstName","lastName":"lastName","countryIso2":"countryIso2","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/diasporaBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gender(client):
    """Test case for gender

    Infer the likely gender of a name.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/gender/{first_name}/{last_name}'.format(first_name='first_name_example', last_name='last_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gender1(client):
    """Test case for gender1

    Infer the likely gender of a just a fiven name, assuming default 'US' local context. Please use preferably full names and local geographic context for better accuracy.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/gender/{first_name}'.format(first_name='first_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gender_batch(client):
    """Test case for gender_batch

    Infer the likely gender of up to 100 names, detecting automatically the cultural context.
    """
    body = {"personalNames":[{"firstName":"firstName","lastName":"lastName","id":"id"},{"firstName":"firstName","lastName":"lastName","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/genderBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gender_full(client):
    """Test case for gender_full

    Infer the likely gender of a full name, ex. John H. Smith
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/genderFull/{full_name}'.format(full_name='full_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gender_full_batch(client):
    """Test case for gender_full_batch

    Infer the likely gender of up to 100 full names, detecting automatically the cultural context.
    """
    body = {"personalNames":[{"name":"name","id":"id"},{"name":"name","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/genderFullBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gender_full_geo(client):
    """Test case for gender_full_geo

    Infer the likely gender of a full name, given a local context (ISO2 country code).
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/genderFullGeo/{full_name}/{country_iso2}'.format(full_name='full_name_example', country_iso2='country_iso2_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gender_full_geo_batch(client):
    """Test case for gender_full_geo_batch

    Infer the likely gender of up to 100 full names, with a given cultural context (country ISO2 code).
    """
    body = {"personalNames":[{"name":"name","countryIso2":"countryIso2","id":"id"},{"name":"name","countryIso2":"countryIso2","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/genderFullGeoBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gender_geo(client):
    """Test case for gender_geo

    Infer the likely gender of a name, given a local context (ISO2 country code).
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/genderGeo/{first_name}/{last_name}/{country_iso2}'.format(first_name='first_name_example', last_name='last_name_example', country_iso2='country_iso2_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gender_geo_batch(client):
    """Test case for gender_geo_batch

    Infer the likely gender of up to 100 names, each given a local context (ISO2 country code).
    """
    body = {"personalNames":[{"firstName":"firstName","lastName":"lastName","countryIso2":"countryIso2","id":"id"},{"firstName":"firstName","lastName":"lastName","countryIso2":"countryIso2","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/genderGeoBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_origin(client):
    """Test case for origin

    [USES 10 UNITS PER NAME] Infer the likely country of origin of a personal name. Assumes names as they are in the country of origin. For US, CA, AU, NZ and other melting-pots : use 'diaspora' instead.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/origin/{first_name}/{last_name}'.format(first_name='first_name_example', last_name='last_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_origin_batch(client):
    """Test case for origin_batch

    [USES 10 UNITS PER NAME] Infer the likely country of origin of up to 100 names, detecting automatically the cultural context.
    """
    body = {"personalNames":[{"firstName":"firstName","lastName":"lastName","id":"id"},{"firstName":"firstName","lastName":"lastName","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/originBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_parse_name(client):
    """Test case for parse_name

    Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. 
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/parseName/{name_full}'.format(name_full='name_full_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_parse_name_batch(client):
    """Test case for parse_name_batch

    Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John.
    """
    body = {"personalNames":[{"name":"name","id":"id"},{"name":"name","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/parseNameBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_parse_name_geo(client):
    """Test case for parse_name_geo

    Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. For better accuracy, provide a geographic context.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/parseName/{name_full}/{country_iso2}'.format(name_full='name_full_example', country_iso2='country_iso2_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_parse_name_geo_batch(client):
    """Test case for parse_name_geo_batch

    Infer the likely first/last name structure of a name, ex. John Smith or SMITH, John or SMITH; John. Giving a local context improves precision. 
    """
    body = {"personalNames":[{"name":"name","countryIso2":"countryIso2","id":"id"},{"name":"name","countryIso2":"countryIso2","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/parseNameGeoBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_religion_full(client):
    """Test case for religion_full

    [USES 10 UNITS PER NAME] Infer the likely religion of a personal full name. NB: only for INDIA (as of current version).
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/religionFull/{country_iso2}/{sub_division_iso31662}/{personal_name_full}'.format(country_iso2='country_iso2_example', sub_division_iso31662='sub_division_iso31662_example', personal_name_full='personal_name_full_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_religion_full_batch(client):
    """Test case for religion_full_batch

    [USES 10 UNITS PER NAME] Infer the likely religion of up to 100 personal full names. NB: only for India as of currently.
    """
    body = {"personalNames":[{"subdivisionIso":"subdivisionIso","name":"name","countryIso2":"countryIso2","id":"id"},{"subdivisionIso":"subdivisionIso","name":"name","countryIso2":"countryIso2","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/religionFullBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subclassification(client):
    """Test case for subclassification

    [USES 10 UNITS PER NAME] Infer the likely origin of a name at a country subclassification level (state or regeion). Initially, this is only supported for India (ISO2 code 'IN').
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/subclassification/{country_iso2}/{first_name}/{last_name}'.format(country_iso2='country_iso2_example', first_name='first_name_example', last_name='last_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subclassification_batch(client):
    """Test case for subclassification_batch

    [USES 10 UNITS PER NAME] Infer the likely origin of a list of up to 100 names at a country subclassification level (state or regeion). Initially, this is only supported for India (ISO2 code 'IN').
    """
    body = {"personalNames":[{"firstName":"firstName","lastName":"lastName","countryIso2":"countryIso2","id":"id"},{"firstName":"firstName","lastName":"lastName","countryIso2":"countryIso2","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/subclassificationBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subclassification_full(client):
    """Test case for subclassification_full

    [USES 10 UNITS PER NAME] Infer the likely origin of a name at a country subclassification level (state or regeion). Initially, this is only supported for India (ISO2 code 'IN').
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/subclassificationFull/{country_iso2}/{full_name}'.format(country_iso2='country_iso2_example', full_name='full_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_subclassification_full_batch(client):
    """Test case for subclassification_full_batch

    [USES 10 UNITS PER NAME] Infer the likely origin of a list of up to 100 names at a country subclassification level (state or regeion). Initially, this is only supported for India (ISO2 code 'IN').
    """
    body = {"personalNames":[{"name":"name","countryIso2":"countryIso2","id":"id"},{"name":"name","countryIso2":"countryIso2","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/subclassificationFullBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_us_race_ethnicity(client):
    """Test case for us_race_ethnicity

    [USES 10 UNITS PER NAME] Infer a US resident's likely race/ethnicity according to US Census taxonomy W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino). Optionally add header X-OPTION-USRACEETHNICITY-TAXONOMY: USRACEETHNICITY-6CLASSES for two additional classes, AI_AN (American Indian or Alaskan Native) and PI (Pacific Islander).
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/usRaceEthnicity/{first_name}/{last_name}'.format(first_name='first_name_example', last_name='last_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_us_race_ethnicity_batch(client):
    """Test case for us_race_ethnicity_batch

    [USES 10 UNITS PER NAME] Infer up-to 100 US resident's likely race/ethnicity according to US Census taxonomy. Output is W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino). Optionally add header X-OPTION-USRACEETHNICITY-TAXONOMY: USRACEETHNICITY-6CLASSES for two additional classes, AI_AN (American Indian or Alaskan Native) and PI (Pacific Islander).
    """
    body = {"personalNames":[{"firstName":"firstName","lastName":"lastName","countryIso2":"countryIso2","id":"id"},{"firstName":"firstName","lastName":"lastName","countryIso2":"countryIso2","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/usRaceEthnicityBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_us_race_ethnicity_zip5(client):
    """Test case for us_race_ethnicity_zip5

    [USES 10 UNITS PER NAME] Infer a US resident's likely race/ethnicity according to US Census taxonomy, using (optional) ZIP5 code info. Output is W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino). Optionally add header X-OPTION-USRACEETHNICITY-TAXONOMY: USRACEETHNICITY-6CLASSES for two additional classes, AI_AN (American Indian or Alaskan Native) and PI (Pacific Islander).
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/usRaceEthnicityZIP5/{first_name}/{last_name}/{zip5_code}'.format(first_name='first_name_example', last_name='last_name_example', zip5_code='zip5_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_us_zip_race_ethnicity_batch(client):
    """Test case for us_zip_race_ethnicity_batch

    [USES 10 UNITS PER NAME] Infer up-to 100 US resident's likely race/ethnicity according to US Census taxonomy, with (optional) ZIP code. Output is W_NL (white, non latino), HL (hispano latino),  A (asian, non latino), B_NL (black, non latino). Optionally add header X-OPTION-USRACEETHNICITY-TAXONOMY: USRACEETHNICITY-6CLASSES for two additional classes, AI_AN (American Indian or Alaskan Native) and PI (Pacific Islander).
    """
    body = {"personalNames":[{"firstName":"firstName","lastName":"lastName","zipCode":"zipCode","countryIso2":"countryIso2","id":"id"},{"firstName":"firstName","lastName":"lastName","zipCode":"zipCode","countryIso2":"countryIso2","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/usZipRaceEthnicityBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

