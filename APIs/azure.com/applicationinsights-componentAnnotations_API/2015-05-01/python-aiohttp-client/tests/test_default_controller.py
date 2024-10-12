# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.annotation import Annotation
from openapi_server.models.annotation_error import AnnotationError
from openapi_server.models.annotations_list_result import AnnotationsListResult


pytestmark = pytest.mark.asyncio

async def test_annotations_create(client):
    """Test case for annotations_create

    
    """
    annotation_properties = {"Category":"Category","EventTime":"2000-01-23T04:56:07.000+00:00","RelatedAnnotation":"null","Id":"Id","Properties":"Properties","AnnotationName":"AnnotationName"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/components/{resource_name}/Annotations'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', resource_name='resource_name_example'),
        headers=headers,
        json=annotation_properties,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_annotations_delete(client):
    """Test case for annotations_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/components/{resource_name}/Annotations/{annotation_id}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', resource_name='resource_name_example', annotation_id='annotation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_annotations_get(client):
    """Test case for annotations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/components/{resource_name}/Annotations/{annotation_id}'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', resource_name='resource_name_example', annotation_id='annotation_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_annotations_list(client):
    """Test case for annotations_list

    
    """
    params = [('api-version', 'api_version_example'),
                    ('start', 'start_example'),
                    ('end', 'end_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Insights/components/{resource_name}/Annotations'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

