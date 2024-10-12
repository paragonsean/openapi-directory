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
from openapi_server.models.extras_recent_activity_list200_response import ExtrasRecentActivityList200Response
from openapi_server.models.extras_tags_list200_response import ExtrasTagsList200Response
from openapi_server.models.extras_topology_maps_list200_response import ExtrasTopologyMapsList200Response
from openapi_server.models.graph import Graph
from openapi_server.models.image_attachment import ImageAttachment
from openapi_server.models.object_change import ObjectChange
from openapi_server.models.tag import Tag
from openapi_server.models.topology_map import TopologyMap
from openapi_server.models.user_action import UserAction
from openapi_server.models.writable_config_context import WritableConfigContext
from openapi_server.models.writable_graph import WritableGraph
from openapi_server.models.writable_topology_map import WritableTopologyMap


pytestmark = pytest.mark.asyncio

async def test_extras_choices_list(client):
    """Test case for extras_choices_list

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/_choices/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_choices_read(client):
    """Test case for extras_choices_read

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/_choices/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_config_contexts_create(client):
    """Test case for extras_config_contexts_create

    
    """
    body = {"tenants":[7,7],"tenant_groups":[2,2],"is_active":True,"regions":[1,1],"data":"data","roles":[5,5],"name":"name","description":"description","weight":30478,"sites":[5,5],"id":0,"platforms":[6,6]}
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
    params = [('name', 'name_example'),
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
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
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
    body = {"tenants":[7,7],"tenant_groups":[2,2],"is_active":True,"regions":[1,1],"data":"data","roles":[5,5],"name":"name","description":"description","weight":30478,"sites":[5,5],"id":0,"platforms":[6,6]}
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
    body = {"tenants":[7,7],"tenant_groups":[2,2],"is_active":True,"regions":[1,1],"data":"data","roles":[5,5],"name":"name","description":"description","weight":30478,"sites":[5,5],"id":0,"platforms":[6,6]}
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

async def test_extras_export_templates_create(client):
    """Test case for extras_export_templates_create

    
    """
    body = {"content_type":6,"mime_type":"mime_type","name":"name","description":"description","file_extension":"file_extension","id":1,"template_code":"template_code"}
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
    params = [('content_type', 'content_type_example'),
                    ('name', 'name_example'),
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
    body = {"content_type":6,"mime_type":"mime_type","name":"name","description":"description","file_extension":"file_extension","id":1,"template_code":"template_code"}
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
    body = {"content_type":6,"mime_type":"mime_type","name":"name","description":"description","file_extension":"file_extension","id":1,"template_code":"template_code"}
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
    body = {"link":"https://openapi-generator.tech","name":"name","weight":4803,"id":0,"source":"source","type":6}
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
    params = [('type', 'type_example'),
                    ('name', 'name_example'),
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
    body = {"link":"https://openapi-generator.tech","name":"name","weight":4803,"id":0,"source":"source","type":6}
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
    body = {"link":"https://openapi-generator.tech","name":"name","weight":4803,"id":0,"source":"source","type":6}
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
    body = {"image":"https://openapi-generator.tech","parent":"parent","image_height":4803,"content_type":"content_type","created":"2000-01-23T04:56:07.000+00:00","name":"name","id":6,"image_width":19536,"object_id":1210617418}
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
    body = {"image":"https://openapi-generator.tech","parent":"parent","image_height":4803,"content_type":"content_type","created":"2000-01-23T04:56:07.000+00:00","name":"name","id":6,"image_width":19536,"object_id":1210617418}
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
    body = {"image":"https://openapi-generator.tech","parent":"parent","image_height":4803,"content_type":"content_type","created":"2000-01-23T04:56:07.000+00:00","name":"name","id":6,"image_width":19536,"object_id":1210617418}
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
    params = [('user', 'user_example'),
                    ('user_name', 'user_name_example'),
                    ('request_id', 'request_id_example'),
                    ('action', 'action_example'),
                    ('changed_object_type', 'changed_object_type_example'),
                    ('object_repr', 'object_repr_example'),
                    ('q', 'q_example'),
                    ('time', 'time_example'),
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

async def test_extras_recent_activity_list(client):
    """Test case for extras_recent_activity_list

    
    """
    params = [('user', 'user_example'),
                    ('username', 'username_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/recent-activity/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_recent_activity_read(client):
    """Test case for extras_recent_activity_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/recent-activity/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_tags_create(client):
    """Test case for extras_tags_create

    
    """
    body = {"tagged_items":1,"name":"name","id":6,"slug":"slug"}
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
    params = [('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('q', 'q_example'),
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
    body = {"tagged_items":1,"name":"name","id":6,"slug":"slug"}
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
    body = {"tagged_items":1,"name":"name","id":6,"slug":"slug"}
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


pytestmark = pytest.mark.asyncio

async def test_extras_topology_maps_create(client):
    """Test case for extras_topology_maps_create

    
    """
    body = {"device_patterns":"device_patterns","site":6,"name":"name","description":"description","id":0,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/extras/topology-maps/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_topology_maps_delete(client):
    """Test case for extras_topology_maps_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/topology-maps/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_topology_maps_list(client):
    """Test case for extras_topology_maps_list

    
    """
    params = [('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/topology-maps/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_topology_maps_partial_update(client):
    """Test case for extras_topology_maps_partial_update

    
    """
    body = {"device_patterns":"device_patterns","site":6,"name":"name","description":"description","id":0,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/topology-maps/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_topology_maps_read(client):
    """Test case for extras_topology_maps_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/topology-maps/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_topology_maps_render(client):
    """Test case for extras_topology_maps_render

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/topology-maps/{id}/render'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_topology_maps_update(client):
    """Test case for extras_topology_maps_update

    
    """
    body = {"device_patterns":"device_patterns","site":6,"name":"name","description":"description","id":0,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/topology-maps/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

