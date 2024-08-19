# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_first_last_name_gender_in import BatchFirstLastNameGenderIn
from openapi_server.models.batch_first_last_name_gendered_out import BatchFirstLastNameGenderedOut
from openapi_server.models.batch_first_last_name_in import BatchFirstLastNameIn
from openapi_server.models.batch_match_personal_first_last_name_in import BatchMatchPersonalFirstLastNameIn
from openapi_server.models.batch_name_match_candidates_out import BatchNameMatchCandidatesOut
from openapi_server.models.batch_name_matched_out import BatchNameMatchedOut
from openapi_server.models.batch_personal_name_gendered_out import BatchPersonalNameGenderedOut
from openapi_server.models.batch_personal_name_in import BatchPersonalNameIn
from openapi_server.models.batch_personal_name_parsed_out import BatchPersonalNameParsedOut
from openapi_server.models.first_last_name_gendered_out import FirstLastNameGenderedOut
from openapi_server.models.name_match_candidates_out import NameMatchCandidatesOut
from openapi_server.models.name_matched_out import NameMatchedOut
from openapi_server.models.personal_name_gendered_out import PersonalNameGenderedOut
from openapi_server.models.personal_name_parsed_out import PersonalNameParsedOut


pytestmark = pytest.mark.asyncio

async def test_chinese_name_candidates(client):
    """Test case for chinese_name_candidates

    Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/chineseNameCandidates/{chinese_surname_latin}/{chinese_given_name_latin}'.format(chinese_surname_latin='chinese_surname_latin_example', chinese_given_name_latin='chinese_given_name_latin_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chinese_name_candidates_batch(client):
    """Test case for chinese_name_candidates_batch

    Identify Chinese name candidates, based on the romanized name (firstName = chineseGivenName; lastName=chineseSurname), ex. Wang Xiaoming
    """
    body = {"personalNames":[{"firstName":"firstName","lastName":"lastName","id":"id"},{"firstName":"firstName","lastName":"lastName","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/chineseNameCandidatesBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chinese_name_candidates_gender_batch(client):
    """Test case for chinese_name_candidates_gender_batch

    Identify Chinese name candidates, based on the romanized name (firstName = chineseGivenName; lastName=chineseSurname) ex. Wang Xiaoming.
    """
    body = {"personalNames":[{"firstName":"firstName","lastName":"lastName","gender":"gender","id":"id"},{"firstName":"firstName","lastName":"lastName","gender":"gender","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/chineseNameCandidatesGenderBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chinese_name_gender_candidates(client):
    """Test case for chinese_name_gender_candidates

    Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming - having a known gender ('male' or 'female')
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/chineseNameGenderCandidates/{chinese_surname_latin}/{chinese_given_name_latin}/{known_gender}'.format(chinese_surname_latin='chinese_surname_latin_example', chinese_given_name_latin='chinese_given_name_latin_example', known_gender='known_gender_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chinese_name_match(client):
    """Test case for chinese_name_match

    Return a score for matching Chinese name ex. 王晓明 with a romanized name ex. Wang Xiaoming
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/chineseNameMatch/{chinese_surname_latin}/{chinese_given_name_latin}/{chinese_name}'.format(chinese_surname_latin='chinese_surname_latin_example', chinese_given_name_latin='chinese_given_name_latin_example', chinese_name='chinese_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chinese_name_match_batch(client):
    """Test case for chinese_name_match_batch

    Identify Chinese name candidates, based on the romanized name (firstName = chineseGivenName; lastName=chineseSurname), ex. Wang Xiaoming
    """
    body = {"personalNames":[{"id":"id","name2":{"name":"name","id":"id"},"name1":{"firstName":"firstName","lastName":"lastName","id":"id"}},{"id":"id","name2":{"name":"name","id":"id"},"name1":{"firstName":"firstName","lastName":"lastName","id":"id"}}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/chineseNameMatchBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gender_chinese_name(client):
    """Test case for gender_chinese_name

    Infer the likely gender of a Chinese full name ex. 王晓明
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/genderChineseName/{chinese_name}'.format(chinese_name='chinese_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gender_chinese_name_batch(client):
    """Test case for gender_chinese_name_batch

    Infer the likely gender of up to 100 full names ex. 王晓明
    """
    body = {"personalNames":[{"name":"name","id":"id"},{"name":"name","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/genderChineseNameBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gender_chinese_name_pinyin(client):
    """Test case for gender_chinese_name_pinyin

    Infer the likely gender of a Chinese name in LATIN (Pinyin).
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/genderChineseNamePinyin/{chinese_surname_latin}/{chinese_given_name_latin}'.format(chinese_surname_latin='chinese_surname_latin_example', chinese_given_name_latin='chinese_given_name_latin_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gender_chinese_name_pinyin_batch(client):
    """Test case for gender_chinese_name_pinyin_batch

    Infer the likely gender of up to 100 Chinese names in LATIN (Pinyin).
    """
    body = {"personalNames":[{"firstName":"firstName","lastName":"lastName","id":"id"},{"firstName":"firstName","lastName":"lastName","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/genderChineseNamePinyinBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_parse_chinese_name(client):
    """Test case for parse_chinese_name

    Infer the likely first/last name structure of a name, ex. 王晓明 -> 王(surname) 晓明(given name)
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/parseChineseName/{chinese_name}'.format(chinese_name='chinese_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_parse_chinese_name_batch(client):
    """Test case for parse_chinese_name_batch

    Infer the likely first/last name structure of a name, ex. 王晓明 -> 王(surname) 晓明(given name).
    """
    body = {"personalNames":[{"name":"name","id":"id"},{"name":"name","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/parseChineseNameBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pinyin_chinese_name(client):
    """Test case for pinyin_chinese_name

    Romanize the Chinese name to Pinyin, ex. 王晓明 -> Wang (surname) Xiaoming (given name)
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/pinyinChineseName/{chinese_name}'.format(chinese_name='chinese_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pinyin_chinese_name_batch(client):
    """Test case for pinyin_chinese_name_batch

    Romanize a list of Chinese name to Pinyin, ex. 王晓明 -> Wang (surname) Xiaoming (given name).
    """
    body = {"personalNames":[{"name":"name","id":"id"},{"name":"name","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/pinyinChineseNameBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

