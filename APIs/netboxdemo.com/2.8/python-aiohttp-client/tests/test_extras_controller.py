# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.config_context import ConfigContext
from openapi_server.models.export_template import ExportTemplate
from openapi_server.models.extras_config_contexts_list200_response import ExtrasConfigContextsList200Response
from openapi_server.models.extras_export_templates_list200_response import ExtrasExportTemplatesList200Response
from openapi_server.models.extras_graphs_list200_response import ExtrasGraphsList200Response
from openapi_server.models.extras_image_attachments_list200_response import ExtrasImageAttachmentsList200Response
from openapi_server.models.extras_object_changes_list200_response import ExtrasObjectChangesList200Response
from openapi_server.models.extras_tags_list200_response import ExtrasTagsList200Response
from openapi_server.models.graph import Graph
from openapi_server.models.image_attachment import ImageAttachment
from openapi_server.models.object_change import ObjectChange
from openapi_server.models.tag import Tag
from openapi_server.models.writable_config_context import WritableConfigContext
from openapi_server.models.writable_export_template import WritableExportTemplate


pytestmark = pytest.mark.asyncio

async def test_extras_config_contexts_create(client):
    """Test case for extras_config_contexts_create

    
    """
    body = {"tenants":[3,3],"tenant_groups":[9,9],"is_active":True,"regions":[5,5],"data":"data","roles":[2,2],"description":"description","weight":6642,"cluster_groups":[0,0],"sites":[7,7],"platforms":[5,5],"tags":["tags","tags"],"name":"name","id":1,"clusters":[6,6]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/extras/config-contexts/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_config_contexts_delete(client):
    """Test case for extras_config_contexts_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/config-contexts/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_config_contexts_list(client):
    """Test case for extras_config_contexts_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('is_active', 'is_active_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('platform_id', 'platform_id_example'),
                    ('platform', 'platform_example'),
                    ('cluster_group_id', 'cluster_group_id_example'),
                    ('cluster_group', 'cluster_group_example'),
                    ('cluster_id', 'cluster_id_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('tag', 'tag_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('role_id__n', 'role_id__n_example'),
                    ('role__n', 'role__n_example'),
                    ('platform_id__n', 'platform_id__n_example'),
                    ('platform__n', 'platform__n_example'),
                    ('cluster_group_id__n', 'cluster_group_id__n_example'),
                    ('cluster_group__n', 'cluster_group__n_example'),
                    ('cluster_id__n', 'cluster_id__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('tag__n', 'tag__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/config-contexts/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_config_contexts_partial_update(client):
    """Test case for extras_config_contexts_partial_update

    
    """
    body = {"tenants":[3,3],"tenant_groups":[9,9],"is_active":True,"regions":[5,5],"data":"data","roles":[2,2],"description":"description","weight":6642,"cluster_groups":[0,0],"sites":[7,7],"platforms":[5,5],"tags":["tags","tags"],"name":"name","id":1,"clusters":[6,6]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/config-contexts/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_config_contexts_read(client):
    """Test case for extras_config_contexts_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/config-contexts/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_config_contexts_update(client):
    """Test case for extras_config_contexts_update

    
    """
    body = {"tenants":[3,3],"tenant_groups":[9,9],"is_active":True,"regions":[5,5],"data":"data","roles":[2,2],"description":"description","weight":6642,"cluster_groups":[0,0],"sites":[7,7],"platforms":[5,5],"tags":["tags","tags"],"name":"name","id":1,"clusters":[6,6]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/config-contexts/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_field_choices_list(client):
    """Test case for extras_custom_field_choices_list

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/_custom_field_choices/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_field_choices_read(client):
    """Test case for extras_custom_field_choices_read

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/_custom_field_choices/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_export_templates_create(client):
    """Test case for extras_export_templates_create

    
    """
    body = {"content_type":"content_type","mime_type":"mime_type","name":"name","description":"description","file_extension":"file_extension","id":0,"template_code":"template_code","template_language":"django"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/extras/export-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_export_templates_delete(client):
    """Test case for extras_export_templates_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/export-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_export_templates_list(client):
    """Test case for extras_export_templates_list

    
    """
    params = [('id', 'id_example'),
                    ('content_type', 'content_type_example'),
                    ('name', 'name_example'),
                    ('template_language', 'template_language_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('content_type__n', 'content_type__n_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('template_language__n', 'template_language__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/export-templates/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_export_templates_partial_update(client):
    """Test case for extras_export_templates_partial_update

    
    """
    body = {"content_type":"content_type","mime_type":"mime_type","name":"name","description":"description","file_extension":"file_extension","id":0,"template_code":"template_code","template_language":"django"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/export-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_export_templates_read(client):
    """Test case for extras_export_templates_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/export-templates/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_export_templates_update(client):
    """Test case for extras_export_templates_update

    
    """
    body = {"content_type":"content_type","mime_type":"mime_type","name":"name","description":"description","file_extension":"file_extension","id":0,"template_code":"template_code","template_language":"django"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/export-templates/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_graphs_create(client):
    """Test case for extras_graphs_create

    
    """
    body = {"link":"https://openapi-generator.tech","name":"name","weight":4803,"id":6,"source":"source","type":"type","template_language":"django"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/extras/graphs/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_graphs_delete(client):
    """Test case for extras_graphs_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/graphs/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_graphs_list(client):
    """Test case for extras_graphs_list

    
    """
    params = [('id', 'id_example'),
                    ('type', 'type_example'),
                    ('name', 'name_example'),
                    ('template_language', 'template_language_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('type__n', 'type__n_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('template_language__n', 'template_language__n_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/graphs/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_graphs_partial_update(client):
    """Test case for extras_graphs_partial_update

    
    """
    body = {"link":"https://openapi-generator.tech","name":"name","weight":4803,"id":6,"source":"source","type":"type","template_language":"django"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/graphs/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_graphs_read(client):
    """Test case for extras_graphs_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/graphs/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_graphs_update(client):
    """Test case for extras_graphs_update

    
    """
    body = {"link":"https://openapi-generator.tech","name":"name","weight":4803,"id":6,"source":"source","type":"type","template_language":"django"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/graphs/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_image_attachments_create(client):
    """Test case for extras_image_attachments_create

    
    """
    body = {"image":"https://openapi-generator.tech","parent":{"key":"parent"},"image_height":4803,"content_type":"content_type","created":"2000-01-23T04:56:07.000+00:00","name":"name","id":6,"image_width":19536,"object_id":1210617418}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/extras/image-attachments/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_image_attachments_delete(client):
    """Test case for extras_image_attachments_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/image-attachments/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_image_attachments_list(client):
    """Test case for extras_image_attachments_list

    
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/image-attachments/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_image_attachments_partial_update(client):
    """Test case for extras_image_attachments_partial_update

    
    """
    body = {"image":"https://openapi-generator.tech","parent":{"key":"parent"},"image_height":4803,"content_type":"content_type","created":"2000-01-23T04:56:07.000+00:00","name":"name","id":6,"image_width":19536,"object_id":1210617418}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/image-attachments/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_image_attachments_read(client):
    """Test case for extras_image_attachments_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/image-attachments/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_image_attachments_update(client):
    """Test case for extras_image_attachments_update

    
    """
    body = {"image":"https://openapi-generator.tech","parent":{"key":"parent"},"image_height":4803,"content_type":"content_type","created":"2000-01-23T04:56:07.000+00:00","name":"name","id":6,"image_width":19536,"object_id":1210617418}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/image-attachments/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_object_changes_list(client):
    """Test case for extras_object_changes_list

    
    """
    params = [('id', 'id_example'),
                    ('user', 'user_example'),
                    ('user_name', 'user_name_example'),
                    ('request_id', 'request_id_example'),
                    ('action', 'action_example'),
                    ('changed_object_type', 'changed_object_type_example'),
                    ('changed_object_id', 'changed_object_id_example'),
                    ('object_repr', 'object_repr_example'),
                    ('q', 'q_example'),
                    ('time', 'time_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('user__n', 'user__n_example'),
                    ('user_name__n', 'user_name__n_example'),
                    ('user_name__ic', 'user_name__ic_example'),
                    ('user_name__nic', 'user_name__nic_example'),
                    ('user_name__iew', 'user_name__iew_example'),
                    ('user_name__niew', 'user_name__niew_example'),
                    ('user_name__isw', 'user_name__isw_example'),
                    ('user_name__nisw', 'user_name__nisw_example'),
                    ('user_name__ie', 'user_name__ie_example'),
                    ('user_name__nie', 'user_name__nie_example'),
                    ('action__n', 'action__n_example'),
                    ('changed_object_type__n', 'changed_object_type__n_example'),
                    ('changed_object_id__n', 'changed_object_id__n_example'),
                    ('changed_object_id__lte', 'changed_object_id__lte_example'),
                    ('changed_object_id__lt', 'changed_object_id__lt_example'),
                    ('changed_object_id__gte', 'changed_object_id__gte_example'),
                    ('changed_object_id__gt', 'changed_object_id__gt_example'),
                    ('object_repr__n', 'object_repr__n_example'),
                    ('object_repr__ic', 'object_repr__ic_example'),
                    ('object_repr__nic', 'object_repr__nic_example'),
                    ('object_repr__iew', 'object_repr__iew_example'),
                    ('object_repr__niew', 'object_repr__niew_example'),
                    ('object_repr__isw', 'object_repr__isw_example'),
                    ('object_repr__nisw', 'object_repr__nisw_example'),
                    ('object_repr__ie', 'object_repr__ie_example'),
                    ('object_repr__nie', 'object_repr__nie_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/object-changes/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_object_changes_read(client):
    """Test case for extras_object_changes_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/object-changes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_reports_list(client):
    """Test case for extras_reports_list

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/reports/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_reports_read(client):
    """Test case for extras_reports_read

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/reports/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_reports_run(client):
    """Test case for extras_reports_run

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/extras/reports/{id}/run'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_scripts_list(client):
    """Test case for extras_scripts_list

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/scripts/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_scripts_read(client):
    """Test case for extras_scripts_read

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/scripts/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_tags_create(client):
    """Test case for extras_tags_create

    
    """
    body = {"color":"color","tagged_items":1,"name":"name","description":"description","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/extras/tags/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_tags_delete(client):
    """Test case for extras_tags_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/tags/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_tags_list(client):
    """Test case for extras_tags_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('color', 'color_example'),
                    ('q', 'q_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('color__n', 'color__n_example'),
                    ('color__ic', 'color__ic_example'),
                    ('color__nic', 'color__nic_example'),
                    ('color__iew', 'color__iew_example'),
                    ('color__niew', 'color__niew_example'),
                    ('color__isw', 'color__isw_example'),
                    ('color__nisw', 'color__nisw_example'),
                    ('color__ie', 'color__ie_example'),
                    ('color__nie', 'color__nie_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/tags/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_tags_partial_update(client):
    """Test case for extras_tags_partial_update

    
    """
    body = {"color":"color","tagged_items":1,"name":"name","description":"description","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/tags/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_tags_read(client):
    """Test case for extras_tags_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/tags/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_tags_update(client):
    """Test case for extras_tags_update

    
    """
    body = {"color":"color","tagged_items":1,"name":"name","description":"description","id":6,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/tags/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

