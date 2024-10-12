# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.input_collection_conversion import InputCollectionConversion
from openapi_server.models.input_collection_conversion_xml import InputCollectionConversionXML
from openapi_server.models.input_collection_count import InputCollectionCount
from openapi_server.models.input_collection_filter import InputCollectionFilter
from openapi_server.models.input_collection_modify import InputCollectionModify
from openapi_server.models.input_collection_replace import InputCollectionReplace
from openapi_server.models.input_collection_search import InputCollectionSearch
from openapi_server.models.input_collection_search_numeric import InputCollectionSearchNumeric
from openapi_server.models.input_collection_sort import InputCollectionSort
from openapi_server.models.input_collection_split import InputCollectionSplit
from openapi_server.models.output_collection_number import OutputCollectionNumber
from openapi_server.models.output_collection_result import OutputCollectionResult
from openapi_server.models.output_collection_string import OutputCollectionString
from openapi_server.models.output_multi_collection import OutputMultiCollection
from openapi_server.models.output_number import OutputNumber
from openapi_server.models.output_string import OutputString


pytestmark = pytest.mark.asyncio

async def test_add_to_collection(client):
    """Test case for add_to_collection

    Collections - Add to collection
    """
    collection_modify = openapi_server.InputCollectionModify()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/AddToCollection',
        headers=headers,
        json=collection_modify,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_contains_number(client):
    """Test case for collection_contains_number

    Collections - Contains number
    """
    collection_search = openapi_server.InputCollectionSearchNumeric()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CollectionContainsNumber',
        headers=headers,
        json=collection_search,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_contains_string(client):
    """Test case for collection_contains_string

    Collections - Contains string
    """
    collection_search = openapi_server.InputCollectionSearch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CollectionContainsString',
        headers=headers,
        json=collection_search,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_ends_with_string(client):
    """Test case for collection_ends_with_string

    Collections - Ends with string
    """
    collection_search = openapi_server.InputCollectionSearch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CollectionEndsWithString',
        headers=headers,
        json=collection_search,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_starts_with_string(client):
    """Test case for collection_starts_with_string

    Collections - Starts with string
    """
    collection_search = openapi_server.InputCollectionSearch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CollectionStartsWithString',
        headers=headers,
        json=collection_search,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_to_json(client):
    """Test case for collection_to_json

    Collections - Collection to JSON
    """
    collection_conversion = openapi_server.InputCollectionConversion()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CollectionToJSON',
        headers=headers,
        json=collection_conversion,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_to_xml(client):
    """Test case for collection_to_xml

    Collections - Collection to XML
    """
    collection_conversion_xml = openapi_server.InputCollectionConversionXML()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CollectionToXML',
        headers=headers,
        json=collection_conversion_xml,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_count_collection(client):
    """Test case for count_collection

    Collections - Count collection
    """
    collection_count = openapi_server.InputCollectionCount()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/CountCollection',
        headers=headers,
        json=collection_count,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_filter_collection(client):
    """Test case for filter_collection

    Collections - Filter collection
    """
    collection_filter = openapi_server.InputCollectionFilter()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/FilterCollection',
        headers=headers,
        json=collection_filter,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_from_collection(client):
    """Test case for remove_from_collection

    Collections - Remove from collection
    """
    collection_modify = openapi_server.InputCollectionModify()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/RemoveFromCollection',
        headers=headers,
        json=collection_modify,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replace_values_in_collection(client):
    """Test case for replace_values_in_collection

    Collections - Replace values in collection
    """
    collection_replace = openapi_server.InputCollectionReplace()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/ReplaceValuesInCollection',
        headers=headers,
        json=collection_replace,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sort_collection(client):
    """Test case for sort_collection

    Collections - Sort collection
    """
    collection_sort = openapi_server.InputCollectionSort()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/SortCollection',
        headers=headers,
        json=collection_sort,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_split_collection(client):
    """Test case for split_collection

    Collections - Split collection
    """
    collection_split = openapi_server.InputCollectionSplit()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKeyHeader': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/utilities/SplitCollection',
        headers=headers,
        json=collection_split,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

