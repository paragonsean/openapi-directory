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
from openapi_server.models.feedback_loop_out import FeedbackLoopOut
from openapi_server.models.first_last_name_gendered_out import FirstLastNameGenderedOut
from openapi_server.models.name_match_candidates_out import NameMatchCandidatesOut
from openapi_server.models.name_matched_out import NameMatchedOut
from openapi_server.models.personal_name_gendered_out import PersonalNameGenderedOut
from openapi_server.models.personal_name_parsed_out import PersonalNameParsedOut


pytestmark = pytest.mark.asyncio

async def test_gender_japanese_name_full(client):
    """Test case for gender_japanese_name_full

    Infer the likely gender of a Japanese full name ex. 王晓明
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/genderJapaneseNameFull/{japanese_name}'.format(japanese_name='japanese_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gender_japanese_name_full_batch(client):
    """Test case for gender_japanese_name_full_batch

    Infer the likely gender of up to 100 full names
    """
    body = {"personalNames":[{"name":"name","id":"id"},{"name":"name","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/genderJapaneseNameFullBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gender_japanese_name_pinyin(client):
    """Test case for gender_japanese_name_pinyin

    Infer the likely gender of a Japanese name in LATIN (Pinyin).
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/genderJapaneseName/{japanese_surname}/{japanese_given_name}'.format(japanese_surname='japanese_surname_example', japanese_given_name='japanese_given_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_gender_japanese_name_pinyin_batch(client):
    """Test case for gender_japanese_name_pinyin_batch

    Infer the likely gender of up to 100 Japanese names in LATIN (Pinyin).
    """
    body = {"personalNames":[{"firstName":"firstName","lastName":"lastName","id":"id"},{"firstName":"firstName","lastName":"lastName","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/genderJapaneseNameBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_japanese_name_gender_kanji_candidates_batch(client):
    """Test case for japanese_name_gender_kanji_candidates_batch

    Identify japanese name candidates in KANJI, based on the romanized name (firstName = japaneseGivenName; lastName=japaneseSurname) with KNOWN gender, ex. Yamamoto Sanae
    """
    body = {"personalNames":[{"firstName":"firstName","lastName":"lastName","gender":"gender","id":"id"},{"firstName":"firstName","lastName":"lastName","gender":"gender","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/japaneseNameGenderKanjiCandidatesBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_japanese_name_kanji_candidates(client):
    """Test case for japanese_name_kanji_candidates

    Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae - and a known gender.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/japaneseNameKanjiCandidates/{japanese_surname_latin}/{japanese_given_name_latin}/{known_gender}'.format(japanese_surname_latin='japanese_surname_latin_example', japanese_given_name_latin='japanese_given_name_latin_example', known_gender='known_gender_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_japanese_name_kanji_candidates1(client):
    """Test case for japanese_name_kanji_candidates1

    Identify japanese name candidates in KANJI, based on the romanized name ex. Yamamoto Sanae
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/japaneseNameKanjiCandidates/{japanese_surname_latin}/{japanese_given_name_latin}'.format(japanese_surname_latin='japanese_surname_latin_example', japanese_given_name_latin='japanese_given_name_latin_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_japanese_name_kanji_candidates_batch(client):
    """Test case for japanese_name_kanji_candidates_batch

    Identify japanese name candidates in KANJI, based on the romanized name (firstName = japaneseGivenName; lastName=japaneseSurname), ex. Yamamoto Sanae
    """
    body = {"personalNames":[{"firstName":"firstName","lastName":"lastName","id":"id"},{"firstName":"firstName","lastName":"lastName","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/japaneseNameKanjiCandidatesBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_japanese_name_latin_candidates(client):
    """Test case for japanese_name_latin_candidates

    Romanize japanese name, based on the name in Kanji.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/japaneseNameLatinCandidates/{japanese_surname_kanji}/{japanese_given_name_kanji}'.format(japanese_surname_kanji='japanese_surname_kanji_example', japanese_given_name_kanji='japanese_given_name_kanji_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_japanese_name_latin_candidates_batch(client):
    """Test case for japanese_name_latin_candidates_batch

    Romanize japanese names, based on the name in KANJI
    """
    body = {"personalNames":[{"firstName":"firstName","lastName":"lastName","id":"id"},{"firstName":"firstName","lastName":"lastName","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/japaneseNameLatinCandidatesBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_japanese_name_match(client):
    """Test case for japanese_name_match

    Return a score for matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/japaneseNameMatch/{japanese_surname_latin}/{japanese_given_name_latin}/{japanese_name}'.format(japanese_surname_latin='japanese_surname_latin_example', japanese_given_name_latin='japanese_given_name_latin_example', japanese_name='japanese_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_japanese_name_match_batch(client):
    """Test case for japanese_name_match_batch

    Return a score for matching a list of Japanese names in KANJI ex. 山本 早苗 with romanized names ex. Yamamoto Sanae
    """
    body = {"personalNames":[{"id":"id","name2":{"name":"name","id":"id"},"name1":{"firstName":"firstName","lastName":"lastName","id":"id"}},{"id":"id","name2":{"name":"name","id":"id"},"name1":{"firstName":"firstName","lastName":"lastName","id":"id"}}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/japaneseNameMatchBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_japanese_name_match_feedback_loop(client):
    """Test case for japanese_name_match_feedback_loop

    [CREDITS 1 UNIT] Feedback loop to better perform matching Japanese name in KANJI ex. 山本 早苗 with a romanized name ex. Yamamoto Sanae
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/japaneseNameMatchFeedbackLoop/{japanese_surname_latin}/{japanese_given_name_latin}/{japanese_name}'.format(japanese_surname_latin='japanese_surname_latin_example', japanese_given_name_latin='japanese_given_name_latin_example', japanese_name='japanese_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_parse_japanese_name(client):
    """Test case for parse_japanese_name

    Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/parseJapaneseName/{japanese_name}'.format(japanese_name='japanese_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_parse_japanese_name_batch(client):
    """Test case for parse_japanese_name_batch

    Infer the likely first/last name structure of a name, ex. 山本 早苗 or Yamamoto Sanae 
    """
    body = {"personalNames":[{"name":"name","id":"id"},{"name":"name","id":"id"}],"facts":[{"name":"name","id":"id"},{"name":"name","id":"id"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/NamSorAPIv2/api2/json/parseJapaneseNameBatch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

