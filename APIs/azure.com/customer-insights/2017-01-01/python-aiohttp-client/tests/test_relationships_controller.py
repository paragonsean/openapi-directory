# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.relationship_list_result import RelationshipListResult
from openapi_server.models.relationship_resource_format import RelationshipResourceFormat


pytestmark = pytest.mark.asyncio

async def test_relationships_create_or_update(client):
    """Test case for relationships_create_or_update

    
    """
    parameters = {"properties":{"relationshipName":"relationshipName","profileType":"profileType","displayName":{"key":"displayName"},"relatedProfileType":"relatedProfileType","relationshipGuidId":"relationshipGuidId","expiryDateTimeUtc":"2000-01-23T04:56:07.000+00:00","tenantId":"tenantId","description":{"key":"description"},"provisioningState":"Provisioning","fields":[{"isRequired":True,"enumValidValues":[{"localizedValueNames":{"key":"localizedValueNames"},"value":0},{"localizedValueNames":{"key":"localizedValueNames"},"value":0}],"fieldName":"fieldName","isEnum":True,"isLocalizedString":True,"isImage":True,"schemaItemPropLink":"schemaItemPropLink","isName":True,"isFlagEnum":True,"arrayValueSeparator":"arrayValueSeparator","isAvailableInGraph":True,"dataSourcePrecedenceRules":[{"dataSource":{"name":"name","id":0,"dataSourceType":"Connector","dataSourceReferenceId":"dataSourceReferenceId","status":"None"},"precedence":6},{"dataSource":{"name":"name","id":0,"dataSourceType":"Connector","dataSourceReferenceId":"dataSourceReferenceId","status":"None"},"precedence":6}],"isArray":True,"fieldType":"fieldType","propertyId":"propertyId","maxLength":6},{"isRequired":True,"enumValidValues":[{"localizedValueNames":{"key":"localizedValueNames"},"value":0},{"localizedValueNames":{"key":"localizedValueNames"},"value":0}],"fieldName":"fieldName","isEnum":True,"isLocalizedString":True,"isImage":True,"schemaItemPropLink":"schemaItemPropLink","isName":True,"isFlagEnum":True,"arrayValueSeparator":"arrayValueSeparator","isAvailableInGraph":True,"dataSourcePrecedenceRules":[{"dataSource":{"name":"name","id":0,"dataSourceType":"Connector","dataSourceReferenceId":"dataSourceReferenceId","status":"None"},"precedence":6},{"dataSource":{"name":"name","id":0,"dataSourceType":"Connector","dataSourceReferenceId":"dataSourceReferenceId","status":"None"},"precedence":6}],"isArray":True,"fieldType":"fieldType","propertyId":"propertyId","maxLength":6}],"cardinality":"OneToOne","lookupMappings":[{"fieldMappings":[{"profileFieldName":"profileFieldName","relatedProfileKeyProperty":"relatedProfileKeyProperty"},{"profileFieldName":"profileFieldName","relatedProfileKeyProperty":"relatedProfileKeyProperty"}]},{"fieldMappings":[{"profileFieldName":"profileFieldName","relatedProfileKeyProperty":"relatedProfileKeyProperty"},{"profileFieldName":"profileFieldName","relatedProfileKeyProperty":"relatedProfileKeyProperty"}]}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/relationships/{relationship_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', relationship_name='relationship_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_relationships_delete(client):
    """Test case for relationships_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/relationships/{relationship_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', relationship_name='relationship_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_relationships_get(client):
    """Test case for relationships_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/relationships/{relationship_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', relationship_name='relationship_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_relationships_list_by_hub(client):
    """Test case for relationships_list_by_hub

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/relationships'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

