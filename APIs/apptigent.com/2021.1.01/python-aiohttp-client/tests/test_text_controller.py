# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.decode_string_request import DecodeStringRequest
from openapi_server.models.input_case_conversion import InputCaseConversion
from openapi_server.models.input_generate_hash import InputGenerateHash
from openapi_server.models.input_generate_unique_id import InputGenerateUniqueID
from openapi_server.models.input_join_strings import InputJoinStrings
from openapi_server.models.input_redact_string import InputRedactString
from openapi_server.models.input_replace_string import InputReplaceString
from openapi_server.models.input_split_string import InputSplitString
from openapi_server.models.input_string import InputString
from openapi_server.models.input_string_comparison import InputStringComparison
from openapi_server.models.input_string_contains import InputStringContains
from openapi_server.models.input_string_to_file import InputStringToFile
from openapi_server.models.input_text_to_speech import InputTextToSpeech
from openapi_server.models.input_translate_string import InputTranslateString
from openapi_server.models.input_trim_string import InputTrimString
from openapi_server.models.input_verify_hash import InputVerifyHash
from openapi_server.models.output_boolean import OutputBoolean
from openapi_server.models.output_string import OutputString
from openapi_server.models.output_string_array import OutputStringArray
from openapi_server.models.shorten_link_request import ShortenLinkRequest
from openapi_server.models.url_decode_request import UrlDecodeRequest
from openapi_server.models.validate_email_request import ValidateEmailRequest


pytestmark = pytest.mark.asyncio

async def test_compare_strings(client):
    """Test case for compare_strings

    Text - Compare strings
    """
    string_comparison = openapi_server.InputStringComparison()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CompareStrings',
        headers=headers,
        json=string_comparison,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_contains_string(client):
    """Test case for contains_string

    Text - Contains string
    """
    string_contains = openapi_server.InputStringContains()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/ContainsString',
        headers=headers,
        json=string_contains,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_convert_case(client):
    """Test case for convert_case

    Text - Convert case
    """
    case_conversion = openapi_server.InputCaseConversion()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/ConvertCase',
        headers=headers,
        json=case_conversion,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_decode_string(client):
    """Test case for decode_string

    Text - Decode string
    """
    string_input = openapi_server.DecodeStringRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/DecodeString',
        headers=headers,
        json=string_input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_encode_string(client):
    """Test case for encode_string

    Text - Encode string
    """
    string_input = openapi_server.InputString()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/EncodeString',
        headers=headers,
        json=string_input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_guid(client):
    """Test case for generate_guid

    Text - Generate GUID
    """
    generate_unique_id = openapi_server.InputGenerateUniqueID()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/GenerateGuid',
        headers=headers,
        json=generate_unique_id,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_hash(client):
    """Test case for generate_hash

    Text - Generate hash
    """
    generate_hash = openapi_server.InputGenerateHash()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/GenerateHash',
        headers=headers,
        json=generate_hash,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_join_strings(client):
    """Test case for join_strings

    Text - Join strings
    """
    join_strings = openapi_server.InputJoinStrings()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/JoinStrings',
        headers=headers,
        json=join_strings,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_redact_string(client):
    """Test case for redact_string

    Text - Redact string
    """
    redact_string = openapi_server.InputRedactString()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/RedactString',
        headers=headers,
        json=redact_string,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replace_string(client):
    """Test case for replace_string

    Text - Replace string
    """
    replace_string = openapi_server.InputReplaceString()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/ReplaceString',
        headers=headers,
        json=replace_string,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shorten_link(client):
    """Test case for shorten_link

    Text - Shorten hyperlink
    """
    string_input = openapi_server.ShortenLinkRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/ShortenLink',
        headers=headers,
        json=string_input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_speech_to_text(client):
    """Test case for speech_to_text

    Text - Speech to Text
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'apiKeyHeader': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('language', English (United States))
    response = await client.request(
        method='POST',
        path='/api/utilities/SpeechToText',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_split_string(client):
    """Test case for split_string

    Text - Split string
    """
    split_string = openapi_server.InputSplitString()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/SplitString',
        headers=headers,
        json=split_string,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_string_to_file(client):
    """Test case for string_to_file

    Text - String to File
    """
    input_string_to_file = openapi_server.InputStringToFile()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/StringToFile',
        headers=headers,
        json=input_string_to_file,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_text_to_speech(client):
    """Test case for text_to_speech

    Text - Text to Speech
    """
    text_to_speech = openapi_server.InputTextToSpeech()
    headers = { 
        'Accept': 'audio/mp3',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/TextToSpeech',
        headers=headers,
        json=text_to_speech,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_translate_string(client):
    """Test case for translate_string

    Text - Translate string
    """
    translate_string = openapi_server.InputTranslateString()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/TranslateString',
        headers=headers,
        json=translate_string,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trim_string(client):
    """Test case for trim_string

    Text - Trim string
    """
    trim_string = openapi_server.InputTrimString()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/TrimString',
        headers=headers,
        json=trim_string,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_url_decode(client):
    """Test case for url_decode

    Text - Decode URL
    """
    string_input = openapi_server.UrlDecodeRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/URLDecode',
        headers=headers,
        json=string_input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_url_encode(client):
    """Test case for url_encode

    Text - Encode URL
    """
    string_input = openapi_server.InputString()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/URLEncode',
        headers=headers,
        json=string_input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_email(client):
    """Test case for validate_email

    Text - Validate email
    """
    string_input = openapi_server.ValidateEmailRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/ValidateEmail',
        headers=headers,
        json=string_input,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_hash(client):
    """Test case for verify_hash

    Text - Verify hash
    """
    verify_hash = openapi_server.InputVerifyHash()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/VerifyHash',
        headers=headers,
        json=verify_hash,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

