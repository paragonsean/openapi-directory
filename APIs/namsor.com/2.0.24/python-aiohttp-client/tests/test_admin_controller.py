# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_classifier_taxonomy_out import APIClassifierTaxonomyOut
from openapi_server.models.api_classifiers_status_out import APIClassifiersStatusOut
from openapi_server.models.api_key_out import APIKeyOut
from openapi_server.models.api_period_usage_out import APIPeriodUsageOut
from openapi_server.models.api_services_out import APIServicesOut
from openapi_server.models.api_usage_aggregated_out import APIUsageAggregatedOut
from openapi_server.models.api_usage_history_out import APIUsageHistoryOut
from openapi_server.models.region_out import RegionOut
from openapi_server.models.software_version_out import SoftwareVersionOut


pytestmark = pytest.mark.asyncio

async def test_anonymize(client):
    """Test case for anonymize

    Activate/deactivate anonymization for a source.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/anonymize/{source}/{anonymized}/{token}'.format(source='source_example', anonymized=True, token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_key_info(client):
    """Test case for api_key_info

    Read API Key info.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/apiKeyInfo',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_status(client):
    """Test case for api_status

    Prints the current status of the classifiers. A classifier name in apiStatus corresponds to a service name in apiServices.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/apiStatus',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_usage(client):
    """Test case for api_usage

    Print current API usage.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/apiUsage',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_usage_history(client):
    """Test case for api_usage_history

    Print historical API usage.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/apiUsageHistory',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_usage_history_aggregate(client):
    """Test case for api_usage_history_aggregate

    Print historical API usage (in an aggregated view, by service, by day/hour/min).
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/apiUsageHistoryAggregate',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_available_services(client):
    """Test case for available_services

    List of classification services and usage cost in Units per classification (default is 1=ONE Unit). Some API endpoints (ex. Corridor) combine multiple classifiers.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/apiServices',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_learnable(client):
    """Test case for learnable

    Activate/deactivate learning from a source.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/learnable/{source}/{learnable}/{token}'.format(source='source_example', learnable=True, token='token_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_regions(client):
    """Test case for regions

    Print basic source statistics.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/regions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_software_version(client):
    """Test case for software_version

    Get the current software version
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/softwareVersion',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_taxonomy_classes(client):
    """Test case for taxonomy_classes

    Print the taxonomy classes valid for the given classifier.
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/NamSorAPIv2/api2/json/taxonomyClasses/{classifier_name}'.format(classifier_name='classifier_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

