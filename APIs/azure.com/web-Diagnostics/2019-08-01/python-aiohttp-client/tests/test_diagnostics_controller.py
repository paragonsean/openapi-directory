# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.analysis_definition import AnalysisDefinition
from openapi_server.models.detector_definition import DetectorDefinition
from openapi_server.models.detector_response import DetectorResponse
from openapi_server.models.detector_response_collection import DetectorResponseCollection
from openapi_server.models.diagnostic_analysis import DiagnosticAnalysis
from openapi_server.models.diagnostic_analysis_collection import DiagnosticAnalysisCollection
from openapi_server.models.diagnostic_category import DiagnosticCategory
from openapi_server.models.diagnostic_category_collection import DiagnosticCategoryCollection
from openapi_server.models.diagnostic_detector_collection import DiagnosticDetectorCollection
from openapi_server.models.diagnostic_detector_response import DiagnosticDetectorResponse
from openapi_server.models.diagnostics_list_hosting_environment_detector_responses_default_response import DiagnosticsListHostingEnvironmentDetectorResponsesDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_diagnostics_execute_site_analysis(client):
    """Test case for diagnostics_execute_site_analysis

    Execute Analysis
    """
    params = [('startTime', '2013-10-20T19:20:30+01:00'),
                    ('endTime', '2013-10-20T19:20:30+01:00'),
                    ('timeGrain', 'time_grain_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/diagnostics/{diagnostic_category}/analyses/{analysis_name}/execute'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', diagnostic_category='diagnostic_category_example', analysis_name='analysis_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_execute_site_analysis_slot(client):
    """Test case for diagnostics_execute_site_analysis_slot

    Execute Analysis
    """
    params = [('startTime', '2013-10-20T19:20:30+01:00'),
                    ('endTime', '2013-10-20T19:20:30+01:00'),
                    ('timeGrain', 'time_grain_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/slots/{slot}/diagnostics/{diagnostic_category}/analyses/{analysis_name}/execute'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', diagnostic_category='diagnostic_category_example', analysis_name='analysis_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_execute_site_detector(client):
    """Test case for diagnostics_execute_site_detector

    Execute Detector
    """
    params = [('startTime', '2013-10-20T19:20:30+01:00'),
                    ('endTime', '2013-10-20T19:20:30+01:00'),
                    ('timeGrain', 'time_grain_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/diagnostics/{diagnostic_category}/detectors/{detector_name}/execute'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', detector_name='detector_name_example', diagnostic_category='diagnostic_category_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_execute_site_detector_slot(client):
    """Test case for diagnostics_execute_site_detector_slot

    Execute Detector
    """
    params = [('startTime', '2013-10-20T19:20:30+01:00'),
                    ('endTime', '2013-10-20T19:20:30+01:00'),
                    ('timeGrain', 'time_grain_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/slots/{slot}/diagnostics/{diagnostic_category}/detectors/{detector_name}/execute'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', detector_name='detector_name_example', diagnostic_category='diagnostic_category_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_get_hosting_environment_detector_response(client):
    """Test case for diagnostics_get_hosting_environment_detector_response

    Get Hosting Environment Detector Response
    """
    params = [('startTime', '2013-10-20T19:20:30+01:00'),
                    ('endTime', '2013-10-20T19:20:30+01:00'),
                    ('timeGrain', 'time_grain_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/detectors/{detector_name}'.format(resource_group_name='resource_group_name_example', name='name_example', detector_name='detector_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_get_site_analysis(client):
    """Test case for diagnostics_get_site_analysis

    Get Site Analysis
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/diagnostics/{diagnostic_category}/analyses/{analysis_name}'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', diagnostic_category='diagnostic_category_example', analysis_name='analysis_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_get_site_analysis_slot(client):
    """Test case for diagnostics_get_site_analysis_slot

    Get Site Analysis
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/slots/{slot}/diagnostics/{diagnostic_category}/analyses/{analysis_name}'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', diagnostic_category='diagnostic_category_example', analysis_name='analysis_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_get_site_detector(client):
    """Test case for diagnostics_get_site_detector

    Get Detector
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/diagnostics/{diagnostic_category}/detectors/{detector_name}'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', diagnostic_category='diagnostic_category_example', detector_name='detector_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_get_site_detector_response(client):
    """Test case for diagnostics_get_site_detector_response

    Get site detector response
    """
    params = [('startTime', '2013-10-20T19:20:30+01:00'),
                    ('endTime', '2013-10-20T19:20:30+01:00'),
                    ('timeGrain', 'time_grain_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/detectors/{detector_name}'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', detector_name='detector_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_get_site_detector_response_slot(client):
    """Test case for diagnostics_get_site_detector_response_slot

    Get site detector response
    """
    params = [('startTime', '2013-10-20T19:20:30+01:00'),
                    ('endTime', '2013-10-20T19:20:30+01:00'),
                    ('timeGrain', 'time_grain_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/slots/{slot}/detectors/{detector_name}'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', detector_name='detector_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_get_site_detector_slot(client):
    """Test case for diagnostics_get_site_detector_slot

    Get Detector
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/slots/{slot}/diagnostics/{diagnostic_category}/detectors/{detector_name}'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', diagnostic_category='diagnostic_category_example', detector_name='detector_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_get_site_diagnostic_category(client):
    """Test case for diagnostics_get_site_diagnostic_category

    Get Diagnostics Category
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/diagnostics/{diagnostic_category}'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', diagnostic_category='diagnostic_category_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_get_site_diagnostic_category_slot(client):
    """Test case for diagnostics_get_site_diagnostic_category_slot

    Get Diagnostics Category
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/slots/{slot}/diagnostics/{diagnostic_category}'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', diagnostic_category='diagnostic_category_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_list_hosting_environment_detector_responses(client):
    """Test case for diagnostics_list_hosting_environment_detector_responses

    List Hosting Environment Detector Responses
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/hostingEnvironments/{name}/detectors'.format(resource_group_name='resource_group_name_example', name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_list_site_analyses(client):
    """Test case for diagnostics_list_site_analyses

    Get Site Analyses
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/diagnostics/{diagnostic_category}/analyses'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', diagnostic_category='diagnostic_category_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_list_site_analyses_slot(client):
    """Test case for diagnostics_list_site_analyses_slot

    Get Site Analyses
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/slots/{slot}/diagnostics/{diagnostic_category}/analyses'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', diagnostic_category='diagnostic_category_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_list_site_detector_responses(client):
    """Test case for diagnostics_list_site_detector_responses

    List Site Detector Responses
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/detectors'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_list_site_detector_responses_slot(client):
    """Test case for diagnostics_list_site_detector_responses_slot

    List Site Detector Responses
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/slots/{slot}/detectors'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_list_site_detectors(client):
    """Test case for diagnostics_list_site_detectors

    Get Detectors
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/diagnostics/{diagnostic_category}/detectors'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', diagnostic_category='diagnostic_category_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_list_site_detectors_slot(client):
    """Test case for diagnostics_list_site_detectors_slot

    Get Detectors
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/slots/{slot}/diagnostics/{diagnostic_category}/detectors'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', diagnostic_category='diagnostic_category_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_list_site_diagnostic_categories(client):
    """Test case for diagnostics_list_site_diagnostic_categories

    Get Diagnostics Categories
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/diagnostics'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_diagnostics_list_site_diagnostic_categories_slot(client):
    """Test case for diagnostics_list_site_diagnostic_categories_slot

    Get Diagnostics Categories
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/sites/{site_name}/slots/{slot}/diagnostics'.format(resource_group_name='resource_group_name_example', site_name='site_name_example', slot='slot_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

