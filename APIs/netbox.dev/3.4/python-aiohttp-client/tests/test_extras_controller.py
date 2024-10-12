# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.config_context import ConfigContext
from openapi_server.models.content_type import ContentType
from openapi_server.models.custom_field import CustomField
from openapi_server.models.custom_link import CustomLink
from openapi_server.models.export_template import ExportTemplate
from openapi_server.models.extras_config_contexts_list200_response import ExtrasConfigContextsList200Response
from openapi_server.models.extras_content_types_list200_response import ExtrasContentTypesList200Response
from openapi_server.models.extras_custom_fields_list200_response import ExtrasCustomFieldsList200Response
from openapi_server.models.extras_custom_links_list200_response import ExtrasCustomLinksList200Response
from openapi_server.models.extras_export_templates_list200_response import ExtrasExportTemplatesList200Response
from openapi_server.models.extras_image_attachments_list200_response import ExtrasImageAttachmentsList200Response
from openapi_server.models.extras_job_results_list200_response import ExtrasJobResultsList200Response
from openapi_server.models.extras_journal_entries_list200_response import ExtrasJournalEntriesList200Response
from openapi_server.models.extras_object_changes_list200_response import ExtrasObjectChangesList200Response
from openapi_server.models.extras_saved_filters_list200_response import ExtrasSavedFiltersList200Response
from openapi_server.models.extras_tags_list200_response import ExtrasTagsList200Response
from openapi_server.models.extras_webhooks_list200_response import ExtrasWebhooksList200Response
from openapi_server.models.image_attachment import ImageAttachment
from openapi_server.models.job_result import JobResult
from openapi_server.models.journal_entry import JournalEntry
from openapi_server.models.object_change import ObjectChange
from openapi_server.models.saved_filter import SavedFilter
from openapi_server.models.tag import Tag
from openapi_server.models.webhook import Webhook
from openapi_server.models.writable_config_context import WritableConfigContext
from openapi_server.models.writable_custom_field import WritableCustomField
from openapi_server.models.writable_journal_entry import WritableJournalEntry


pytestmark = pytest.mark.asyncio

async def test_extras_config_contexts_bulk_delete(client):
    """Test case for extras_config_contexts_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/config-contexts/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_config_contexts_bulk_partial_update(client):
    """Test case for extras_config_contexts_bulk_partial_update

    
    """
    body = {"tenants":[1,1],"last_updated":"2000-01-23T04:56:07.000+00:00","tenant_groups":[7,7],"cluster_types":[6,6],"is_active":True,"regions":[9,9],"data":"{}","created":"2000-01-23T04:56:07.000+00:00","display":"display","roles":[3,3],"description":"description","weight":3357,"cluster_groups":[0,0],"sites":[4,4],"site_groups":[2,2],"url":"https://openapi-generator.tech","platforms":[7,7],"tags":["tags","tags"],"name":"name","locations":[2,2],"id":5,"device_types":[5,5],"clusters":[1,1]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/config-contexts/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_config_contexts_bulk_update(client):
    """Test case for extras_config_contexts_bulk_update

    
    """
    body = {"tenants":[1,1],"last_updated":"2000-01-23T04:56:07.000+00:00","tenant_groups":[7,7],"cluster_types":[6,6],"is_active":True,"regions":[9,9],"data":"{}","created":"2000-01-23T04:56:07.000+00:00","display":"display","roles":[3,3],"description":"description","weight":3357,"cluster_groups":[0,0],"sites":[4,4],"site_groups":[2,2],"url":"https://openapi-generator.tech","platforms":[7,7],"tags":["tags","tags"],"name":"name","locations":[2,2],"id":5,"device_types":[5,5],"clusters":[1,1]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/config-contexts/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_config_contexts_create(client):
    """Test case for extras_config_contexts_create

    
    """
    body = {"tenants":[1,1],"last_updated":"2000-01-23T04:56:07.000+00:00","tenant_groups":[7,7],"cluster_types":[6,6],"is_active":True,"regions":[9,9],"data":"{}","created":"2000-01-23T04:56:07.000+00:00","display":"display","roles":[3,3],"description":"description","weight":3357,"cluster_groups":[0,0],"sites":[4,4],"site_groups":[2,2],"url":"https://openapi-generator.tech","platforms":[7,7],"tags":["tags","tags"],"name":"name","locations":[2,2],"id":5,"device_types":[5,5],"clusters":[1,1]}
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
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group', 'site_group_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('location_id', 'location_id_example'),
                    ('location', 'location_example'),
                    ('device_type_id', 'device_type_id_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('platform_id', 'platform_id_example'),
                    ('platform', 'platform_example'),
                    ('cluster_type_id', 'cluster_type_id_example'),
                    ('cluster_type', 'cluster_type_example'),
                    ('cluster_group_id', 'cluster_group_id_example'),
                    ('cluster_group', 'cluster_group_example'),
                    ('cluster_id', 'cluster_id_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('tag_id', 'tag_id_example'),
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
                    ('name__empty', 'name__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('location_id__n', 'location_id__n_example'),
                    ('location__n', 'location__n_example'),
                    ('device_type_id__n', 'device_type_id__n_example'),
                    ('role_id__n', 'role_id__n_example'),
                    ('role__n', 'role__n_example'),
                    ('platform_id__n', 'platform_id__n_example'),
                    ('platform__n', 'platform__n_example'),
                    ('cluster_type_id__n', 'cluster_type_id__n_example'),
                    ('cluster_type__n', 'cluster_type__n_example'),
                    ('cluster_group_id__n', 'cluster_group_id__n_example'),
                    ('cluster_group__n', 'cluster_group__n_example'),
                    ('cluster_id__n', 'cluster_id__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('tag_id__n', 'tag_id__n_example'),
                    ('tag__n', 'tag__n_example'),
                    ('ordering', 'ordering_example'),
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
    body = {"tenants":[1,1],"last_updated":"2000-01-23T04:56:07.000+00:00","tenant_groups":[7,7],"cluster_types":[6,6],"is_active":True,"regions":[9,9],"data":"{}","created":"2000-01-23T04:56:07.000+00:00","display":"display","roles":[3,3],"description":"description","weight":3357,"cluster_groups":[0,0],"sites":[4,4],"site_groups":[2,2],"url":"https://openapi-generator.tech","platforms":[7,7],"tags":["tags","tags"],"name":"name","locations":[2,2],"id":5,"device_types":[5,5],"clusters":[1,1]}
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
    body = {"tenants":[1,1],"last_updated":"2000-01-23T04:56:07.000+00:00","tenant_groups":[7,7],"cluster_types":[6,6],"is_active":True,"regions":[9,9],"data":"{}","created":"2000-01-23T04:56:07.000+00:00","display":"display","roles":[3,3],"description":"description","weight":3357,"cluster_groups":[0,0],"sites":[4,4],"site_groups":[2,2],"url":"https://openapi-generator.tech","platforms":[7,7],"tags":["tags","tags"],"name":"name","locations":[2,2],"id":5,"device_types":[5,5],"clusters":[1,1]}
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

async def test_extras_content_types_list(client):
    """Test case for extras_content_types_list

    
    """
    params = [('id', 3.4),
                    ('app_label', 'app_label_example'),
                    ('model', 'model_example'),
                    ('q', 'q_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/content-types/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_content_types_read(client):
    """Test case for extras_content_types_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/content-types/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_fields_bulk_delete(client):
    """Test case for extras_custom_fields_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/custom-fields/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_fields_bulk_partial_update(client):
    """Test case for extras_custom_fields_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","filter_logic":"disabled","group_name":"group_name","object_type":"object_type","created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","weight":18471,"label":"label","type":"text","required":True,"ui_visibility":"read-write","url":"https://openapi-generator.tech","search_weight":19750,"default":"{}","validation_minimum":413233370,"validation_regex":"validation_regex","data_type":"data_type","name":"name","content_types":["content_types","content_types"],"id":0,"validation_maximum":-1517921766,"choices":["choices","choices"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/custom-fields/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_fields_bulk_update(client):
    """Test case for extras_custom_fields_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","filter_logic":"disabled","group_name":"group_name","object_type":"object_type","created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","weight":18471,"label":"label","type":"text","required":True,"ui_visibility":"read-write","url":"https://openapi-generator.tech","search_weight":19750,"default":"{}","validation_minimum":413233370,"validation_regex":"validation_regex","data_type":"data_type","name":"name","content_types":["content_types","content_types"],"id":0,"validation_maximum":-1517921766,"choices":["choices","choices"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/custom-fields/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_fields_create(client):
    """Test case for extras_custom_fields_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","filter_logic":"disabled","group_name":"group_name","object_type":"object_type","created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","weight":18471,"label":"label","type":"text","required":True,"ui_visibility":"read-write","url":"https://openapi-generator.tech","search_weight":19750,"default":"{}","validation_minimum":413233370,"validation_regex":"validation_regex","data_type":"data_type","name":"name","content_types":["content_types","content_types"],"id":0,"validation_maximum":-1517921766,"choices":["choices","choices"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/extras/custom-fields/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_fields_delete(client):
    """Test case for extras_custom_fields_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/custom-fields/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_fields_list(client):
    """Test case for extras_custom_fields_list

    
    """
    params = [('id', 'id_example'),
                    ('content_types', 'content_types_example'),
                    ('name', 'name_example'),
                    ('group_name', 'group_name_example'),
                    ('required', 'required_example'),
                    ('search_weight', 'search_weight_example'),
                    ('filter_logic', 'filter_logic_example'),
                    ('ui_visibility', 'ui_visibility_example'),
                    ('weight', 'weight_example'),
                    ('description', 'description_example'),
                    ('q', 'q_example'),
                    ('type', 'type_example'),
                    ('content_type_id', 'content_type_id_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('content_types__n', 'content_types__n_example'),
                    ('content_types__ic', 'content_types__ic_example'),
                    ('content_types__nic', 'content_types__nic_example'),
                    ('content_types__iew', 'content_types__iew_example'),
                    ('content_types__niew', 'content_types__niew_example'),
                    ('content_types__isw', 'content_types__isw_example'),
                    ('content_types__nisw', 'content_types__nisw_example'),
                    ('content_types__ie', 'content_types__ie_example'),
                    ('content_types__nie', 'content_types__nie_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('group_name__n', 'group_name__n_example'),
                    ('group_name__ic', 'group_name__ic_example'),
                    ('group_name__nic', 'group_name__nic_example'),
                    ('group_name__iew', 'group_name__iew_example'),
                    ('group_name__niew', 'group_name__niew_example'),
                    ('group_name__isw', 'group_name__isw_example'),
                    ('group_name__nisw', 'group_name__nisw_example'),
                    ('group_name__ie', 'group_name__ie_example'),
                    ('group_name__nie', 'group_name__nie_example'),
                    ('group_name__empty', 'group_name__empty_example'),
                    ('search_weight__n', 'search_weight__n_example'),
                    ('search_weight__lte', 'search_weight__lte_example'),
                    ('search_weight__lt', 'search_weight__lt_example'),
                    ('search_weight__gte', 'search_weight__gte_example'),
                    ('search_weight__gt', 'search_weight__gt_example'),
                    ('filter_logic__n', 'filter_logic__n_example'),
                    ('ui_visibility__n', 'ui_visibility__n_example'),
                    ('weight__n', 'weight__n_example'),
                    ('weight__lte', 'weight__lte_example'),
                    ('weight__lt', 'weight__lt_example'),
                    ('weight__gte', 'weight__gte_example'),
                    ('weight__gt', 'weight__gt_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('type__n', 'type__n_example'),
                    ('content_type_id__n', 'content_type_id__n_example'),
                    ('content_type_id__lte', 'content_type_id__lte_example'),
                    ('content_type_id__lt', 'content_type_id__lt_example'),
                    ('content_type_id__gte', 'content_type_id__gte_example'),
                    ('content_type_id__gt', 'content_type_id__gt_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/custom-fields/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_fields_partial_update(client):
    """Test case for extras_custom_fields_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","filter_logic":"disabled","group_name":"group_name","object_type":"object_type","created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","weight":18471,"label":"label","type":"text","required":True,"ui_visibility":"read-write","url":"https://openapi-generator.tech","search_weight":19750,"default":"{}","validation_minimum":413233370,"validation_regex":"validation_regex","data_type":"data_type","name":"name","content_types":["content_types","content_types"],"id":0,"validation_maximum":-1517921766,"choices":["choices","choices"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/custom-fields/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_fields_read(client):
    """Test case for extras_custom_fields_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/custom-fields/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_fields_update(client):
    """Test case for extras_custom_fields_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","filter_logic":"disabled","group_name":"group_name","object_type":"object_type","created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","weight":18471,"label":"label","type":"text","required":True,"ui_visibility":"read-write","url":"https://openapi-generator.tech","search_weight":19750,"default":"{}","validation_minimum":413233370,"validation_regex":"validation_regex","data_type":"data_type","name":"name","content_types":["content_types","content_types"],"id":0,"validation_maximum":-1517921766,"choices":["choices","choices"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/custom-fields/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_links_bulk_delete(client):
    """Test case for extras_custom_links_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/custom-links/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_links_bulk_partial_update(client):
    """Test case for extras_custom_links_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","group_name":"group_name","created":"2000-01-23T04:56:07.000+00:00","display":"display","button_class":"outline-dark","weight":4803,"enabled":True,"url":"https://openapi-generator.tech","name":"name","link_url":"link_url","new_window":True,"content_types":["content_types","content_types"],"id":6,"link_text":"link_text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/custom-links/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_links_bulk_update(client):
    """Test case for extras_custom_links_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","group_name":"group_name","created":"2000-01-23T04:56:07.000+00:00","display":"display","button_class":"outline-dark","weight":4803,"enabled":True,"url":"https://openapi-generator.tech","name":"name","link_url":"link_url","new_window":True,"content_types":["content_types","content_types"],"id":6,"link_text":"link_text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/custom-links/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_links_create(client):
    """Test case for extras_custom_links_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","group_name":"group_name","created":"2000-01-23T04:56:07.000+00:00","display":"display","button_class":"outline-dark","weight":4803,"enabled":True,"url":"https://openapi-generator.tech","name":"name","link_url":"link_url","new_window":True,"content_types":["content_types","content_types"],"id":6,"link_text":"link_text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/extras/custom-links/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_links_delete(client):
    """Test case for extras_custom_links_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/custom-links/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_links_list(client):
    """Test case for extras_custom_links_list

    
    """
    params = [('id', 'id_example'),
                    ('content_types', 'content_types_example'),
                    ('name', 'name_example'),
                    ('enabled', 'enabled_example'),
                    ('link_text', 'link_text_example'),
                    ('link_url', 'link_url_example'),
                    ('weight', 'weight_example'),
                    ('group_name', 'group_name_example'),
                    ('new_window', 'new_window_example'),
                    ('q', 'q_example'),
                    ('content_type_id', 'content_type_id_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('content_types__n', 'content_types__n_example'),
                    ('content_types__ic', 'content_types__ic_example'),
                    ('content_types__nic', 'content_types__nic_example'),
                    ('content_types__iew', 'content_types__iew_example'),
                    ('content_types__niew', 'content_types__niew_example'),
                    ('content_types__isw', 'content_types__isw_example'),
                    ('content_types__nisw', 'content_types__nisw_example'),
                    ('content_types__ie', 'content_types__ie_example'),
                    ('content_types__nie', 'content_types__nie_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('link_text__n', 'link_text__n_example'),
                    ('link_text__ic', 'link_text__ic_example'),
                    ('link_text__nic', 'link_text__nic_example'),
                    ('link_text__iew', 'link_text__iew_example'),
                    ('link_text__niew', 'link_text__niew_example'),
                    ('link_text__isw', 'link_text__isw_example'),
                    ('link_text__nisw', 'link_text__nisw_example'),
                    ('link_text__ie', 'link_text__ie_example'),
                    ('link_text__nie', 'link_text__nie_example'),
                    ('link_url__n', 'link_url__n_example'),
                    ('link_url__ic', 'link_url__ic_example'),
                    ('link_url__nic', 'link_url__nic_example'),
                    ('link_url__iew', 'link_url__iew_example'),
                    ('link_url__niew', 'link_url__niew_example'),
                    ('link_url__isw', 'link_url__isw_example'),
                    ('link_url__nisw', 'link_url__nisw_example'),
                    ('link_url__ie', 'link_url__ie_example'),
                    ('link_url__nie', 'link_url__nie_example'),
                    ('weight__n', 'weight__n_example'),
                    ('weight__lte', 'weight__lte_example'),
                    ('weight__lt', 'weight__lt_example'),
                    ('weight__gte', 'weight__gte_example'),
                    ('weight__gt', 'weight__gt_example'),
                    ('group_name__n', 'group_name__n_example'),
                    ('group_name__ic', 'group_name__ic_example'),
                    ('group_name__nic', 'group_name__nic_example'),
                    ('group_name__iew', 'group_name__iew_example'),
                    ('group_name__niew', 'group_name__niew_example'),
                    ('group_name__isw', 'group_name__isw_example'),
                    ('group_name__nisw', 'group_name__nisw_example'),
                    ('group_name__ie', 'group_name__ie_example'),
                    ('group_name__nie', 'group_name__nie_example'),
                    ('group_name__empty', 'group_name__empty_example'),
                    ('content_type_id__n', 'content_type_id__n_example'),
                    ('content_type_id__lte', 'content_type_id__lte_example'),
                    ('content_type_id__lt', 'content_type_id__lt_example'),
                    ('content_type_id__gte', 'content_type_id__gte_example'),
                    ('content_type_id__gt', 'content_type_id__gt_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/custom-links/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_links_partial_update(client):
    """Test case for extras_custom_links_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","group_name":"group_name","created":"2000-01-23T04:56:07.000+00:00","display":"display","button_class":"outline-dark","weight":4803,"enabled":True,"url":"https://openapi-generator.tech","name":"name","link_url":"link_url","new_window":True,"content_types":["content_types","content_types"],"id":6,"link_text":"link_text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/custom-links/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_links_read(client):
    """Test case for extras_custom_links_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/custom-links/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_custom_links_update(client):
    """Test case for extras_custom_links_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","group_name":"group_name","created":"2000-01-23T04:56:07.000+00:00","display":"display","button_class":"outline-dark","weight":4803,"enabled":True,"url":"https://openapi-generator.tech","name":"name","link_url":"link_url","new_window":True,"content_types":["content_types","content_types"],"id":6,"link_text":"link_text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/custom-links/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_export_templates_bulk_delete(client):
    """Test case for extras_export_templates_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/export-templates/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_export_templates_bulk_partial_update(client):
    """Test case for extras_export_templates_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","mime_type":"mime_type","created":"2000-01-23T04:56:07.000+00:00","display":"display","as_attachment":True,"name":"name","description":"description","content_types":["content_types","content_types"],"file_extension":"file_extension","id":6,"url":"https://openapi-generator.tech","template_code":"template_code"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/export-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_export_templates_bulk_update(client):
    """Test case for extras_export_templates_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","mime_type":"mime_type","created":"2000-01-23T04:56:07.000+00:00","display":"display","as_attachment":True,"name":"name","description":"description","content_types":["content_types","content_types"],"file_extension":"file_extension","id":6,"url":"https://openapi-generator.tech","template_code":"template_code"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/export-templates/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_export_templates_create(client):
    """Test case for extras_export_templates_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","mime_type":"mime_type","created":"2000-01-23T04:56:07.000+00:00","display":"display","as_attachment":True,"name":"name","description":"description","content_types":["content_types","content_types"],"file_extension":"file_extension","id":6,"url":"https://openapi-generator.tech","template_code":"template_code"}
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
                    ('content_types', 'content_types_example'),
                    ('name', 'name_example'),
                    ('description', 'description_example'),
                    ('q', 'q_example'),
                    ('content_type_id', 'content_type_id_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('content_types__n', 'content_types__n_example'),
                    ('content_types__ic', 'content_types__ic_example'),
                    ('content_types__nic', 'content_types__nic_example'),
                    ('content_types__iew', 'content_types__iew_example'),
                    ('content_types__niew', 'content_types__niew_example'),
                    ('content_types__isw', 'content_types__isw_example'),
                    ('content_types__nisw', 'content_types__nisw_example'),
                    ('content_types__ie', 'content_types__ie_example'),
                    ('content_types__nie', 'content_types__nie_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('content_type_id__n', 'content_type_id__n_example'),
                    ('content_type_id__lte', 'content_type_id__lte_example'),
                    ('content_type_id__lt', 'content_type_id__lt_example'),
                    ('content_type_id__gte', 'content_type_id__gte_example'),
                    ('content_type_id__gt', 'content_type_id__gt_example'),
                    ('ordering', 'ordering_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","mime_type":"mime_type","created":"2000-01-23T04:56:07.000+00:00","display":"display","as_attachment":True,"name":"name","description":"description","content_types":["content_types","content_types"],"file_extension":"file_extension","id":6,"url":"https://openapi-generator.tech","template_code":"template_code"}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","mime_type":"mime_type","created":"2000-01-23T04:56:07.000+00:00","display":"display","as_attachment":True,"name":"name","description":"description","content_types":["content_types","content_types"],"file_extension":"file_extension","id":6,"url":"https://openapi-generator.tech","template_code":"template_code"}
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

async def test_extras_image_attachments_bulk_delete(client):
    """Test case for extras_image_attachments_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/image-attachments/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_image_attachments_bulk_partial_update(client):
    """Test case for extras_image_attachments_bulk_partial_update

    
    """
    body = {"image":"https://openapi-generator.tech","parent":"{}","last_updated":"2000-01-23T04:56:07.000+00:00","image_height":4803,"content_type":"content_type","created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","id":6,"image_width":19536,"object_id":2147483647,"url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/image-attachments/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_image_attachments_bulk_update(client):
    """Test case for extras_image_attachments_bulk_update

    
    """
    body = {"image":"https://openapi-generator.tech","parent":"{}","last_updated":"2000-01-23T04:56:07.000+00:00","image_height":4803,"content_type":"content_type","created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","id":6,"image_width":19536,"object_id":2147483647,"url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/image-attachments/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_image_attachments_create(client):
    """Test case for extras_image_attachments_create

    
    """
    body = {"image":"https://openapi-generator.tech","parent":"{}","last_updated":"2000-01-23T04:56:07.000+00:00","image_height":4803,"content_type":"content_type","created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","id":6,"image_width":19536,"object_id":2147483647,"url":"https://openapi-generator.tech"}
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
    params = [('id', 'id_example'),
                    ('content_type_id', 'content_type_id_example'),
                    ('object_id', 'object_id_example'),
                    ('name', 'name_example'),
                    ('q', 'q_example'),
                    ('created', 'created_example'),
                    ('content_type', 'content_type_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('content_type_id__n', 'content_type_id__n_example'),
                    ('object_id__n', 'object_id__n_example'),
                    ('object_id__lte', 'object_id__lte_example'),
                    ('object_id__lt', 'object_id__lt_example'),
                    ('object_id__gte', 'object_id__gte_example'),
                    ('object_id__gt', 'object_id__gt_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('content_type__n', 'content_type__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
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
    body = {"image":"https://openapi-generator.tech","parent":"{}","last_updated":"2000-01-23T04:56:07.000+00:00","image_height":4803,"content_type":"content_type","created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","id":6,"image_width":19536,"object_id":2147483647,"url":"https://openapi-generator.tech"}
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
    body = {"image":"https://openapi-generator.tech","parent":"{}","last_updated":"2000-01-23T04:56:07.000+00:00","image_height":4803,"content_type":"content_type","created":"2000-01-23T04:56:07.000+00:00","display":"display","name":"name","id":6,"image_width":19536,"object_id":2147483647,"url":"https://openapi-generator.tech"}
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

async def test_extras_job_results_list(client):
    """Test case for extras_job_results_list

    
    """
    params = [('id', 'id_example'),
                    ('interval', 'interval_example'),
                    ('status', 'status_example'),
                    ('user', 'user_example'),
                    ('obj_type', 'obj_type_example'),
                    ('name', 'name_example'),
                    ('q', 'q_example'),
                    ('created', 'created_example'),
                    ('created__before', 'created__before_example'),
                    ('created__after', 'created__after_example'),
                    ('scheduled', 'scheduled_example'),
                    ('scheduled__before', 'scheduled__before_example'),
                    ('scheduled__after', 'scheduled__after_example'),
                    ('started', 'started_example'),
                    ('started__before', 'started__before_example'),
                    ('started__after', 'started__after_example'),
                    ('completed', 'completed_example'),
                    ('completed__before', 'completed__before_example'),
                    ('completed__after', 'completed__after_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('interval__n', 'interval__n_example'),
                    ('interval__lte', 'interval__lte_example'),
                    ('interval__lt', 'interval__lt_example'),
                    ('interval__gte', 'interval__gte_example'),
                    ('interval__gt', 'interval__gt_example'),
                    ('status__n', 'status__n_example'),
                    ('user__n', 'user__n_example'),
                    ('obj_type__n', 'obj_type__n_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/job-results/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_job_results_read(client):
    """Test case for extras_job_results_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/job-results/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_journal_entries_bulk_delete(client):
    """Test case for extras_journal_entries_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/journal-entries/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_journal_entries_bulk_partial_update(client):
    """Test case for extras_journal_entries_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","assigned_object":"{}","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","kind":"info","display":"display","assigned_object_type":"assigned_object_type","assigned_object_id":2147483647,"created_by":6,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/journal-entries/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_journal_entries_bulk_update(client):
    """Test case for extras_journal_entries_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","assigned_object":"{}","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","kind":"info","display":"display","assigned_object_type":"assigned_object_type","assigned_object_id":2147483647,"created_by":6,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/journal-entries/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_journal_entries_create(client):
    """Test case for extras_journal_entries_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","assigned_object":"{}","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","kind":"info","display":"display","assigned_object_type":"assigned_object_type","assigned_object_id":2147483647,"created_by":6,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/extras/journal-entries/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_journal_entries_delete(client):
    """Test case for extras_journal_entries_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/journal-entries/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_journal_entries_list(client):
    """Test case for extras_journal_entries_list

    
    """
    params = [('id', 'id_example'),
                    ('assigned_object_type_id', 'assigned_object_type_id_example'),
                    ('assigned_object_id', 'assigned_object_id_example'),
                    ('created', 'created_example'),
                    ('kind', 'kind_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('assigned_object_type', 'assigned_object_type_example'),
                    ('created_by_id', 'created_by_id_example'),
                    ('created_by', 'created_by_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('assigned_object_type_id__n', 'assigned_object_type_id__n_example'),
                    ('assigned_object_id__n', 'assigned_object_id__n_example'),
                    ('assigned_object_id__lte', 'assigned_object_id__lte_example'),
                    ('assigned_object_id__lt', 'assigned_object_id__lt_example'),
                    ('assigned_object_id__gte', 'assigned_object_id__gte_example'),
                    ('assigned_object_id__gt', 'assigned_object_id__gt_example'),
                    ('kind__n', 'kind__n_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('tag__n', 'tag__n_example'),
                    ('assigned_object_type__n', 'assigned_object_type__n_example'),
                    ('created_by_id__n', 'created_by_id__n_example'),
                    ('created_by__n', 'created_by__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/journal-entries/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_journal_entries_partial_update(client):
    """Test case for extras_journal_entries_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","assigned_object":"{}","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","kind":"info","display":"display","assigned_object_type":"assigned_object_type","assigned_object_id":2147483647,"created_by":6,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/journal-entries/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_journal_entries_read(client):
    """Test case for extras_journal_entries_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/journal-entries/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_journal_entries_update(client):
    """Test case for extras_journal_entries_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","assigned_object":"{}","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","kind":"info","display":"display","assigned_object_type":"assigned_object_type","assigned_object_id":2147483647,"created_by":6,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"id":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/journal-entries/{id}'.format(id=56),
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
                    ('changed_object_type_id', 'changed_object_type_id_example'),
                    ('changed_object_id', 'changed_object_id_example'),
                    ('object_repr', 'object_repr_example'),
                    ('q', 'q_example'),
                    ('time', 'time_example'),
                    ('changed_object_type', 'changed_object_type_example'),
                    ('user_id', 'user_id_example'),
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
                    ('user_name__empty', 'user_name__empty_example'),
                    ('action__n', 'action__n_example'),
                    ('changed_object_type_id__n', 'changed_object_type_id__n_example'),
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
                    ('object_repr__empty', 'object_repr__empty_example'),
                    ('changed_object_type__n', 'changed_object_type__n_example'),
                    ('user_id__n', 'user_id__n_example'),
                    ('ordering', 'ordering_example'),
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

async def test_extras_saved_filters_bulk_delete(client):
    """Test case for extras_saved_filters_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/saved-filters/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_saved_filters_bulk_partial_update(client):
    """Test case for extras_saved_filters_bulk_partial_update

    
    """
    body = {"shared":True,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","weight":19536,"enabled":True,"url":"https://openapi-generator.tech","name":"name","content_types":["content_types","content_types"],"id":6,"parameters":"{}","user":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/saved-filters/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_saved_filters_bulk_update(client):
    """Test case for extras_saved_filters_bulk_update

    
    """
    body = {"shared":True,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","weight":19536,"enabled":True,"url":"https://openapi-generator.tech","name":"name","content_types":["content_types","content_types"],"id":6,"parameters":"{}","user":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/saved-filters/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_saved_filters_create(client):
    """Test case for extras_saved_filters_create

    
    """
    body = {"shared":True,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","weight":19536,"enabled":True,"url":"https://openapi-generator.tech","name":"name","content_types":["content_types","content_types"],"id":6,"parameters":"{}","user":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/extras/saved-filters/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_saved_filters_delete(client):
    """Test case for extras_saved_filters_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/saved-filters/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_saved_filters_list(client):
    """Test case for extras_saved_filters_list

    
    """
    params = [('id', 'id_example'),
                    ('content_types', 'content_types_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('description', 'description_example'),
                    ('enabled', 'enabled_example'),
                    ('shared', 'shared_example'),
                    ('weight', 'weight_example'),
                    ('q', 'q_example'),
                    ('content_type_id', 'content_type_id_example'),
                    ('user_id', 'user_id_example'),
                    ('user', 'user_example'),
                    ('usable', 'usable_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('content_types__n', 'content_types__n_example'),
                    ('content_types__ic', 'content_types__ic_example'),
                    ('content_types__nic', 'content_types__nic_example'),
                    ('content_types__iew', 'content_types__iew_example'),
                    ('content_types__niew', 'content_types__niew_example'),
                    ('content_types__isw', 'content_types__isw_example'),
                    ('content_types__nisw', 'content_types__nisw_example'),
                    ('content_types__ie', 'content_types__ie_example'),
                    ('content_types__nie', 'content_types__nie_example'),
                    ('name__n', 'name__n_example'),
                    ('name__ic', 'name__ic_example'),
                    ('name__nic', 'name__nic_example'),
                    ('name__iew', 'name__iew_example'),
                    ('name__niew', 'name__niew_example'),
                    ('name__isw', 'name__isw_example'),
                    ('name__nisw', 'name__nisw_example'),
                    ('name__ie', 'name__ie_example'),
                    ('name__nie', 'name__nie_example'),
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('weight__n', 'weight__n_example'),
                    ('weight__lte', 'weight__lte_example'),
                    ('weight__lt', 'weight__lt_example'),
                    ('weight__gte', 'weight__gte_example'),
                    ('weight__gt', 'weight__gt_example'),
                    ('content_type_id__n', 'content_type_id__n_example'),
                    ('content_type_id__lte', 'content_type_id__lte_example'),
                    ('content_type_id__lt', 'content_type_id__lt_example'),
                    ('content_type_id__gte', 'content_type_id__gte_example'),
                    ('content_type_id__gt', 'content_type_id__gt_example'),
                    ('user_id__n', 'user_id__n_example'),
                    ('user__n', 'user__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/saved-filters/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_saved_filters_partial_update(client):
    """Test case for extras_saved_filters_partial_update

    
    """
    body = {"shared":True,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","weight":19536,"enabled":True,"url":"https://openapi-generator.tech","name":"name","content_types":["content_types","content_types"],"id":6,"parameters":"{}","user":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/saved-filters/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_saved_filters_read(client):
    """Test case for extras_saved_filters_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/saved-filters/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_saved_filters_update(client):
    """Test case for extras_saved_filters_update

    
    """
    body = {"shared":True,"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","display":"display","description":"description","weight":19536,"enabled":True,"url":"https://openapi-generator.tech","name":"name","content_types":["content_types","content_types"],"id":6,"parameters":"{}","user":1,"slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/saved-filters/{id}'.format(id=56),
        headers=headers,
        json=body,
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

async def test_extras_tags_bulk_delete(client):
    """Test case for extras_tags_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/tags/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_tags_bulk_partial_update(client):
    """Test case for extras_tags_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","tagged_items":1,"display":"display","name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/tags/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_tags_bulk_update(client):
    """Test case for extras_tags_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","tagged_items":1,"display":"display","name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/tags/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_tags_create(client):
    """Test case for extras_tags_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","tagged_items":1,"display":"display","name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech"}
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
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('content_type', 'content_type_example'),
                    ('content_type_id', 'content_type_id_example'),
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
                    ('name__empty', 'name__empty_example'),
                    ('slug__n', 'slug__n_example'),
                    ('slug__ic', 'slug__ic_example'),
                    ('slug__nic', 'slug__nic_example'),
                    ('slug__iew', 'slug__iew_example'),
                    ('slug__niew', 'slug__niew_example'),
                    ('slug__isw', 'slug__isw_example'),
                    ('slug__nisw', 'slug__nisw_example'),
                    ('slug__ie', 'slug__ie_example'),
                    ('slug__nie', 'slug__nie_example'),
                    ('slug__empty', 'slug__empty_example'),
                    ('color__n', 'color__n_example'),
                    ('color__ic', 'color__ic_example'),
                    ('color__nic', 'color__nic_example'),
                    ('color__iew', 'color__iew_example'),
                    ('color__niew', 'color__niew_example'),
                    ('color__isw', 'color__isw_example'),
                    ('color__nisw', 'color__nisw_example'),
                    ('color__ie', 'color__ie_example'),
                    ('color__nie', 'color__nie_example'),
                    ('color__empty', 'color__empty_example'),
                    ('description__n', 'description__n_example'),
                    ('description__ic', 'description__ic_example'),
                    ('description__nic', 'description__nic_example'),
                    ('description__iew', 'description__iew_example'),
                    ('description__niew', 'description__niew_example'),
                    ('description__isw', 'description__isw_example'),
                    ('description__nisw', 'description__nisw_example'),
                    ('description__ie', 'description__ie_example'),
                    ('description__nie', 'description__nie_example'),
                    ('description__empty', 'description__empty_example'),
                    ('created__n', 'created__n_example'),
                    ('created__lte', 'created__lte_example'),
                    ('created__lt', 'created__lt_example'),
                    ('created__gte', 'created__gte_example'),
                    ('created__gt', 'created__gt_example'),
                    ('last_updated__n', 'last_updated__n_example'),
                    ('last_updated__lte', 'last_updated__lte_example'),
                    ('last_updated__lt', 'last_updated__lt_example'),
                    ('last_updated__gte', 'last_updated__gte_example'),
                    ('last_updated__gt', 'last_updated__gt_example'),
                    ('ordering', 'ordering_example'),
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","tagged_items":1,"display":"display","name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech"}
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
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","color":"color","created":"2000-01-23T04:56:07.000+00:00","tagged_items":1,"display":"display","name":"name","description":"description","id":6,"slug":"slug","url":"https://openapi-generator.tech"}
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

async def test_extras_webhooks_bulk_delete(client):
    """Test case for extras_webhooks_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/webhooks/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_webhooks_bulk_partial_update(client):
    """Test case for extras_webhooks_bulk_partial_update

    
    """
    body = {"type_update":True,"additional_headers":"additional_headers","last_updated":"2000-01-23T04:56:07.000+00:00","ca_file_path":"ca_file_path","ssl_verification":True,"type_delete":True,"created":"2000-01-23T04:56:07.000+00:00","display":"display","secret":"secret","body_template":"body_template","enabled":True,"url":"https://openapi-generator.tech","http_method":"GET","http_content_type":"http_content_type","type_create":True,"name":"name","content_types":["content_types","content_types"],"id":6,"conditions":"{}","payload_url":"payload_url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/webhooks/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_webhooks_bulk_update(client):
    """Test case for extras_webhooks_bulk_update

    
    """
    body = {"type_update":True,"additional_headers":"additional_headers","last_updated":"2000-01-23T04:56:07.000+00:00","ca_file_path":"ca_file_path","ssl_verification":True,"type_delete":True,"created":"2000-01-23T04:56:07.000+00:00","display":"display","secret":"secret","body_template":"body_template","enabled":True,"url":"https://openapi-generator.tech","http_method":"GET","http_content_type":"http_content_type","type_create":True,"name":"name","content_types":["content_types","content_types"],"id":6,"conditions":"{}","payload_url":"payload_url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/webhooks/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_webhooks_create(client):
    """Test case for extras_webhooks_create

    
    """
    body = {"type_update":True,"additional_headers":"additional_headers","last_updated":"2000-01-23T04:56:07.000+00:00","ca_file_path":"ca_file_path","ssl_verification":True,"type_delete":True,"created":"2000-01-23T04:56:07.000+00:00","display":"display","secret":"secret","body_template":"body_template","enabled":True,"url":"https://openapi-generator.tech","http_method":"GET","http_content_type":"http_content_type","type_create":True,"name":"name","content_types":["content_types","content_types"],"id":6,"conditions":"{}","payload_url":"payload_url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/extras/webhooks/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_webhooks_delete(client):
    """Test case for extras_webhooks_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/extras/webhooks/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_webhooks_list(client):
    """Test case for extras_webhooks_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('type_create', 'type_create_example'),
                    ('type_update', 'type_update_example'),
                    ('type_delete', 'type_delete_example'),
                    ('payload_url', 'payload_url_example'),
                    ('enabled', 'enabled_example'),
                    ('http_method', 'http_method_example'),
                    ('http_content_type', 'http_content_type_example'),
                    ('secret', 'secret_example'),
                    ('ssl_verification', 'ssl_verification_example'),
                    ('ca_file_path', 'ca_file_path_example'),
                    ('q', 'q_example'),
                    ('content_type_id', 'content_type_id_example'),
                    ('content_types', 'content_types_example'),
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
                    ('name__empty', 'name__empty_example'),
                    ('payload_url__n', 'payload_url__n_example'),
                    ('payload_url__ic', 'payload_url__ic_example'),
                    ('payload_url__nic', 'payload_url__nic_example'),
                    ('payload_url__iew', 'payload_url__iew_example'),
                    ('payload_url__niew', 'payload_url__niew_example'),
                    ('payload_url__isw', 'payload_url__isw_example'),
                    ('payload_url__nisw', 'payload_url__nisw_example'),
                    ('payload_url__ie', 'payload_url__ie_example'),
                    ('payload_url__nie', 'payload_url__nie_example'),
                    ('payload_url__empty', 'payload_url__empty_example'),
                    ('http_method__n', 'http_method__n_example'),
                    ('http_content_type__n', 'http_content_type__n_example'),
                    ('http_content_type__ic', 'http_content_type__ic_example'),
                    ('http_content_type__nic', 'http_content_type__nic_example'),
                    ('http_content_type__iew', 'http_content_type__iew_example'),
                    ('http_content_type__niew', 'http_content_type__niew_example'),
                    ('http_content_type__isw', 'http_content_type__isw_example'),
                    ('http_content_type__nisw', 'http_content_type__nisw_example'),
                    ('http_content_type__ie', 'http_content_type__ie_example'),
                    ('http_content_type__nie', 'http_content_type__nie_example'),
                    ('http_content_type__empty', 'http_content_type__empty_example'),
                    ('secret__n', 'secret__n_example'),
                    ('secret__ic', 'secret__ic_example'),
                    ('secret__nic', 'secret__nic_example'),
                    ('secret__iew', 'secret__iew_example'),
                    ('secret__niew', 'secret__niew_example'),
                    ('secret__isw', 'secret__isw_example'),
                    ('secret__nisw', 'secret__nisw_example'),
                    ('secret__ie', 'secret__ie_example'),
                    ('secret__nie', 'secret__nie_example'),
                    ('secret__empty', 'secret__empty_example'),
                    ('ca_file_path__n', 'ca_file_path__n_example'),
                    ('ca_file_path__ic', 'ca_file_path__ic_example'),
                    ('ca_file_path__nic', 'ca_file_path__nic_example'),
                    ('ca_file_path__iew', 'ca_file_path__iew_example'),
                    ('ca_file_path__niew', 'ca_file_path__niew_example'),
                    ('ca_file_path__isw', 'ca_file_path__isw_example'),
                    ('ca_file_path__nisw', 'ca_file_path__nisw_example'),
                    ('ca_file_path__ie', 'ca_file_path__ie_example'),
                    ('ca_file_path__nie', 'ca_file_path__nie_example'),
                    ('ca_file_path__empty', 'ca_file_path__empty_example'),
                    ('content_type_id__n', 'content_type_id__n_example'),
                    ('content_type_id__lte', 'content_type_id__lte_example'),
                    ('content_type_id__lt', 'content_type_id__lt_example'),
                    ('content_type_id__gte', 'content_type_id__gte_example'),
                    ('content_type_id__gt', 'content_type_id__gt_example'),
                    ('content_types__n', 'content_types__n_example'),
                    ('content_types__ic', 'content_types__ic_example'),
                    ('content_types__nic', 'content_types__nic_example'),
                    ('content_types__iew', 'content_types__iew_example'),
                    ('content_types__niew', 'content_types__niew_example'),
                    ('content_types__isw', 'content_types__isw_example'),
                    ('content_types__nisw', 'content_types__nisw_example'),
                    ('content_types__ie', 'content_types__ie_example'),
                    ('content_types__nie', 'content_types__nie_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/webhooks/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_webhooks_partial_update(client):
    """Test case for extras_webhooks_partial_update

    
    """
    body = {"type_update":True,"additional_headers":"additional_headers","last_updated":"2000-01-23T04:56:07.000+00:00","ca_file_path":"ca_file_path","ssl_verification":True,"type_delete":True,"created":"2000-01-23T04:56:07.000+00:00","display":"display","secret":"secret","body_template":"body_template","enabled":True,"url":"https://openapi-generator.tech","http_method":"GET","http_content_type":"http_content_type","type_create":True,"name":"name","content_types":["content_types","content_types"],"id":6,"conditions":"{}","payload_url":"payload_url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/extras/webhooks/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_webhooks_read(client):
    """Test case for extras_webhooks_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/extras/webhooks/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_extras_webhooks_update(client):
    """Test case for extras_webhooks_update

    
    """
    body = {"type_update":True,"additional_headers":"additional_headers","last_updated":"2000-01-23T04:56:07.000+00:00","ca_file_path":"ca_file_path","ssl_verification":True,"type_delete":True,"created":"2000-01-23T04:56:07.000+00:00","display":"display","secret":"secret","body_template":"body_template","enabled":True,"url":"https://openapi-generator.tech","http_method":"GET","http_content_type":"http_content_type","type_create":True,"name":"name","content_types":["content_types","content_types"],"id":6,"conditions":"{}","payload_url":"payload_url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/extras/webhooks/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

