# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cluster import Cluster
from openapi_server.models.cluster_group import ClusterGroup
from openapi_server.models.cluster_type import ClusterType
from openapi_server.models.vm_interface import VMInterface
from openapi_server.models.virtual_machine_with_config_context import VirtualMachineWithConfigContext
from openapi_server.models.virtualization_cluster_groups_list200_response import VirtualizationClusterGroupsList200Response
from openapi_server.models.virtualization_cluster_types_list200_response import VirtualizationClusterTypesList200Response
from openapi_server.models.virtualization_clusters_list200_response import VirtualizationClustersList200Response
from openapi_server.models.virtualization_interfaces_list200_response import VirtualizationInterfacesList200Response
from openapi_server.models.virtualization_virtual_machines_list200_response import VirtualizationVirtualMachinesList200Response
from openapi_server.models.writable_cluster import WritableCluster
from openapi_server.models.writable_vm_interface import WritableVMInterface
from openapi_server.models.writable_virtual_machine_with_config_context import WritableVirtualMachineWithConfigContext


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_groups_bulk_delete(client):
    """Test case for virtualization_cluster_groups_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/virtualization/cluster-groups/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_groups_bulk_partial_update(client):
    """Test case for virtualization_cluster_groups_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","cluster_count":6,"description":"description","id":1,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/virtualization/cluster-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_groups_bulk_update(client):
    """Test case for virtualization_cluster_groups_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","cluster_count":6,"description":"description","id":1,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/virtualization/cluster-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_groups_create(client):
    """Test case for virtualization_cluster_groups_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","cluster_count":6,"description":"description","id":1,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/virtualization/cluster-groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_groups_delete(client):
    """Test case for virtualization_cluster_groups_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/virtualization/cluster-groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_groups_list(client):
    """Test case for virtualization_cluster_groups_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('contact', 'contact_example'),
                    ('contact_role', 'contact_role_example'),
                    ('contact_group', 'contact_group_example'),
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
                    ('tag__n', 'tag__n_example'),
                    ('contact__n', 'contact__n_example'),
                    ('contact_role__n', 'contact_role__n_example'),
                    ('contact_group__n', 'contact_group__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/cluster-groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_groups_partial_update(client):
    """Test case for virtualization_cluster_groups_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","cluster_count":6,"description":"description","id":1,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/virtualization/cluster-groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_groups_read(client):
    """Test case for virtualization_cluster_groups_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/cluster-groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_groups_update(client):
    """Test case for virtualization_cluster_groups_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","cluster_count":6,"description":"description","id":1,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/virtualization/cluster-groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_types_bulk_delete(client):
    """Test case for virtualization_cluster_types_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/virtualization/cluster-types/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_types_bulk_partial_update(client):
    """Test case for virtualization_cluster_types_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","cluster_count":6,"description":"description","id":1,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/virtualization/cluster-types/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_types_bulk_update(client):
    """Test case for virtualization_cluster_types_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","cluster_count":6,"description":"description","id":1,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/virtualization/cluster-types/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_types_create(client):
    """Test case for virtualization_cluster_types_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","cluster_count":6,"description":"description","id":1,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/virtualization/cluster-types/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_types_delete(client):
    """Test case for virtualization_cluster_types_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/virtualization/cluster-types/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_types_list(client):
    """Test case for virtualization_cluster_types_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('slug', 'slug_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
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
        path='/api/virtualization/cluster-types/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_types_partial_update(client):
    """Test case for virtualization_cluster_types_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","cluster_count":6,"description":"description","id":1,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/virtualization/cluster-types/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_types_read(client):
    """Test case for virtualization_cluster_types_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/cluster-types/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_cluster_types_update(client):
    """Test case for virtualization_cluster_types_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","name":"name","cluster_count":6,"description":"description","id":1,"slug":"slug","url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/virtualization/cluster-types/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_clusters_bulk_delete(client):
    """Test case for virtualization_clusters_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/virtualization/clusters/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_clusters_bulk_partial_update(client):
    """Test case for virtualization_clusters_bulk_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","type":2,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"site":5,"name":"name","virtualmachine_count":7,"id":1,"device_count":0,"tenant":5,"group":6,"status":"planned"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/virtualization/clusters/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_clusters_bulk_update(client):
    """Test case for virtualization_clusters_bulk_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","type":2,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"site":5,"name":"name","virtualmachine_count":7,"id":1,"device_count":0,"tenant":5,"group":6,"status":"planned"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/virtualization/clusters/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_clusters_create(client):
    """Test case for virtualization_clusters_create

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","type":2,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"site":5,"name":"name","virtualmachine_count":7,"id":1,"device_count":0,"tenant":5,"group":6,"status":"planned"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/virtualization/clusters/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_clusters_delete(client):
    """Test case for virtualization_clusters_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/virtualization/clusters/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_clusters_list(client):
    """Test case for virtualization_clusters_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('contact', 'contact_example'),
                    ('contact_role', 'contact_role_example'),
                    ('contact_group', 'contact_group_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('group_id', 'group_id_example'),
                    ('group', 'group_example'),
                    ('type_id', 'type_id_example'),
                    ('type', 'type_example'),
                    ('status', 'status_example'),
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
                    ('tag__n', 'tag__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('contact__n', 'contact__n_example'),
                    ('contact_role__n', 'contact_role__n_example'),
                    ('contact_group__n', 'contact_group__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
                    ('group_id__n', 'group_id__n_example'),
                    ('group__n', 'group__n_example'),
                    ('type_id__n', 'type_id__n_example'),
                    ('type__n', 'type__n_example'),
                    ('status__n', 'status__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/clusters/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_clusters_partial_update(client):
    """Test case for virtualization_clusters_partial_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","type":2,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"site":5,"name":"name","virtualmachine_count":7,"id":1,"device_count":0,"tenant":5,"group":6,"status":"planned"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/virtualization/clusters/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_clusters_read(client):
    """Test case for virtualization_clusters_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/clusters/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_clusters_update(client):
    """Test case for virtualization_clusters_update

    
    """
    body = {"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","type":2,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"site":5,"name":"name","virtualmachine_count":7,"id":1,"device_count":0,"tenant":5,"group":6,"status":"planned"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/virtualization/clusters/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_interfaces_bulk_delete(client):
    """Test case for virtualization_interfaces_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/virtualization/interfaces/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_interfaces_bulk_partial_update(client):
    """Test case for virtualization_interfaces_bulk_partial_update

    
    """
    body = {"parent":2,"last_updated":"2000-01-23T04:56:07.000+00:00","l2vpn_termination":"l2vpn_termination","untagged_vlan":9,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","vrf":2,"count_fhrp_groups":6,"enabled":True,"url":"https://openapi-generator.tech","mtu":36945,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"mode":"access","tagged_vlans":[7,7],"count_ipaddresses":1,"mac_address":"mac_address","name":"name","virtual_machine":3,"bridge":0,"id":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/virtualization/interfaces/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_interfaces_bulk_update(client):
    """Test case for virtualization_interfaces_bulk_update

    
    """
    body = {"parent":2,"last_updated":"2000-01-23T04:56:07.000+00:00","l2vpn_termination":"l2vpn_termination","untagged_vlan":9,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","vrf":2,"count_fhrp_groups":6,"enabled":True,"url":"https://openapi-generator.tech","mtu":36945,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"mode":"access","tagged_vlans":[7,7],"count_ipaddresses":1,"mac_address":"mac_address","name":"name","virtual_machine":3,"bridge":0,"id":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/virtualization/interfaces/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_interfaces_create(client):
    """Test case for virtualization_interfaces_create

    
    """
    body = {"parent":2,"last_updated":"2000-01-23T04:56:07.000+00:00","l2vpn_termination":"l2vpn_termination","untagged_vlan":9,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","vrf":2,"count_fhrp_groups":6,"enabled":True,"url":"https://openapi-generator.tech","mtu":36945,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"mode":"access","tagged_vlans":[7,7],"count_ipaddresses":1,"mac_address":"mac_address","name":"name","virtual_machine":3,"bridge":0,"id":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/virtualization/interfaces/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_interfaces_delete(client):
    """Test case for virtualization_interfaces_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/virtualization/interfaces/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_interfaces_list(client):
    """Test case for virtualization_interfaces_list

    
    """
    params = [('id', 'id_example'),
                    ('name', 'name_example'),
                    ('enabled', 'enabled_example'),
                    ('mtu', 'mtu_example'),
                    ('description', 'description_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('cluster_id', 'cluster_id_example'),
                    ('cluster', 'cluster_example'),
                    ('virtual_machine_id', 'virtual_machine_id_example'),
                    ('virtual_machine', 'virtual_machine_example'),
                    ('parent_id', 'parent_id_example'),
                    ('bridge_id', 'bridge_id_example'),
                    ('mac_address', 'mac_address_example'),
                    ('vrf_id', 'vrf_id_example'),
                    ('vrf', 'vrf_example'),
                    ('l2vpn_id', 'l2vpn_id_example'),
                    ('l2vpn', 'l2vpn_example'),
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
                    ('mtu__n', 'mtu__n_example'),
                    ('mtu__lte', 'mtu__lte_example'),
                    ('mtu__lt', 'mtu__lt_example'),
                    ('mtu__gte', 'mtu__gte_example'),
                    ('mtu__gt', 'mtu__gt_example'),
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
                    ('tag__n', 'tag__n_example'),
                    ('cluster_id__n', 'cluster_id__n_example'),
                    ('cluster__n', 'cluster__n_example'),
                    ('virtual_machine_id__n', 'virtual_machine_id__n_example'),
                    ('virtual_machine__n', 'virtual_machine__n_example'),
                    ('parent_id__n', 'parent_id__n_example'),
                    ('bridge_id__n', 'bridge_id__n_example'),
                    ('mac_address__n', 'mac_address__n_example'),
                    ('mac_address__ic', 'mac_address__ic_example'),
                    ('mac_address__nic', 'mac_address__nic_example'),
                    ('mac_address__iew', 'mac_address__iew_example'),
                    ('mac_address__niew', 'mac_address__niew_example'),
                    ('mac_address__isw', 'mac_address__isw_example'),
                    ('mac_address__nisw', 'mac_address__nisw_example'),
                    ('mac_address__ie', 'mac_address__ie_example'),
                    ('mac_address__nie', 'mac_address__nie_example'),
                    ('vrf_id__n', 'vrf_id__n_example'),
                    ('vrf__n', 'vrf__n_example'),
                    ('l2vpn_id__n', 'l2vpn_id__n_example'),
                    ('l2vpn__n', 'l2vpn__n_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/interfaces/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_interfaces_partial_update(client):
    """Test case for virtualization_interfaces_partial_update

    
    """
    body = {"parent":2,"last_updated":"2000-01-23T04:56:07.000+00:00","l2vpn_termination":"l2vpn_termination","untagged_vlan":9,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","vrf":2,"count_fhrp_groups":6,"enabled":True,"url":"https://openapi-generator.tech","mtu":36945,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"mode":"access","tagged_vlans":[7,7],"count_ipaddresses":1,"mac_address":"mac_address","name":"name","virtual_machine":3,"bridge":0,"id":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/virtualization/interfaces/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_interfaces_read(client):
    """Test case for virtualization_interfaces_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/interfaces/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_interfaces_update(client):
    """Test case for virtualization_interfaces_update

    
    """
    body = {"parent":2,"last_updated":"2000-01-23T04:56:07.000+00:00","l2vpn_termination":"l2vpn_termination","untagged_vlan":9,"created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","description":"description","vrf":2,"count_fhrp_groups":6,"enabled":True,"url":"https://openapi-generator.tech","mtu":36945,"tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"mode":"access","tagged_vlans":[7,7],"count_ipaddresses":1,"mac_address":"mac_address","name":"name","virtual_machine":3,"bridge":0,"id":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/virtualization/interfaces/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_virtual_machines_bulk_delete(client):
    """Test case for virtualization_virtual_machines_bulk_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/virtualization/virtual-machines/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_virtual_machines_bulk_partial_update(client):
    """Test case for virtualization_virtual_machines_bulk_partial_update

    
    """
    body = {"cluster":0,"memory":1210617418,"role":3,"config_context":"{}","primary_ip":"primary_ip","description":"description","platform":2,"id":5,"tenant":4,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","vcpus":0.7486281948385884,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"disk":314780940,"site":2,"local_context_data":"{}","name":"name","device":6,"primary_ip6":9,"primary_ip4":7,"status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/virtualization/virtual-machines/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_virtual_machines_bulk_update(client):
    """Test case for virtualization_virtual_machines_bulk_update

    
    """
    body = {"cluster":0,"memory":1210617418,"role":3,"config_context":"{}","primary_ip":"primary_ip","description":"description","platform":2,"id":5,"tenant":4,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","vcpus":0.7486281948385884,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"disk":314780940,"site":2,"local_context_data":"{}","name":"name","device":6,"primary_ip6":9,"primary_ip4":7,"status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/virtualization/virtual-machines/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_virtual_machines_create(client):
    """Test case for virtualization_virtual_machines_create

    
    """
    body = {"cluster":0,"memory":1210617418,"role":3,"config_context":"{}","primary_ip":"primary_ip","description":"description","platform":2,"id":5,"tenant":4,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","vcpus":0.7486281948385884,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"disk":314780940,"site":2,"local_context_data":"{}","name":"name","device":6,"primary_ip6":9,"primary_ip4":7,"status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/virtualization/virtual-machines/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_virtual_machines_delete(client):
    """Test case for virtualization_virtual_machines_delete

    
    """
    headers = { 
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/virtualization/virtual-machines/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_virtual_machines_list(client):
    """Test case for virtualization_virtual_machines_list

    
    """
    params = [('id', 'id_example'),
                    ('cluster', 'cluster_example'),
                    ('vcpus', 'vcpus_example'),
                    ('memory', 'memory_example'),
                    ('disk', 'disk_example'),
                    ('created', 'created_example'),
                    ('last_updated', 'last_updated_example'),
                    ('q', 'q_example'),
                    ('tag', 'tag_example'),
                    ('tenant_group_id', 'tenant_group_id_example'),
                    ('tenant_group', 'tenant_group_example'),
                    ('tenant_id', 'tenant_id_example'),
                    ('tenant', 'tenant_example'),
                    ('contact', 'contact_example'),
                    ('contact_role', 'contact_role_example'),
                    ('contact_group', 'contact_group_example'),
                    ('local_context_data', 'local_context_data_example'),
                    ('status', 'status_example'),
                    ('cluster_group_id', 'cluster_group_id_example'),
                    ('cluster_group', 'cluster_group_example'),
                    ('cluster_type_id', 'cluster_type_id_example'),
                    ('cluster_type', 'cluster_type_example'),
                    ('cluster_id', 'cluster_id_example'),
                    ('device_id', 'device_id_example'),
                    ('device', 'device_example'),
                    ('region_id', 'region_id_example'),
                    ('region', 'region_example'),
                    ('site_group_id', 'site_group_id_example'),
                    ('site_group', 'site_group_example'),
                    ('site_id', 'site_id_example'),
                    ('site', 'site_example'),
                    ('name', 'name_example'),
                    ('role_id', 'role_id_example'),
                    ('role', 'role_example'),
                    ('platform_id', 'platform_id_example'),
                    ('platform', 'platform_example'),
                    ('mac_address', 'mac_address_example'),
                    ('has_primary_ip', 'has_primary_ip_example'),
                    ('id__n', 'id__n_example'),
                    ('id__lte', 'id__lte_example'),
                    ('id__lt', 'id__lt_example'),
                    ('id__gte', 'id__gte_example'),
                    ('id__gt', 'id__gt_example'),
                    ('cluster__n', 'cluster__n_example'),
                    ('vcpus__n', 'vcpus__n_example'),
                    ('vcpus__lte', 'vcpus__lte_example'),
                    ('vcpus__lt', 'vcpus__lt_example'),
                    ('vcpus__gte', 'vcpus__gte_example'),
                    ('vcpus__gt', 'vcpus__gt_example'),
                    ('memory__n', 'memory__n_example'),
                    ('memory__lte', 'memory__lte_example'),
                    ('memory__lt', 'memory__lt_example'),
                    ('memory__gte', 'memory__gte_example'),
                    ('memory__gt', 'memory__gt_example'),
                    ('disk__n', 'disk__n_example'),
                    ('disk__lte', 'disk__lte_example'),
                    ('disk__lt', 'disk__lt_example'),
                    ('disk__gte', 'disk__gte_example'),
                    ('disk__gt', 'disk__gt_example'),
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
                    ('tag__n', 'tag__n_example'),
                    ('tenant_group_id__n', 'tenant_group_id__n_example'),
                    ('tenant_group__n', 'tenant_group__n_example'),
                    ('tenant_id__n', 'tenant_id__n_example'),
                    ('tenant__n', 'tenant__n_example'),
                    ('contact__n', 'contact__n_example'),
                    ('contact_role__n', 'contact_role__n_example'),
                    ('contact_group__n', 'contact_group__n_example'),
                    ('status__n', 'status__n_example'),
                    ('cluster_group_id__n', 'cluster_group_id__n_example'),
                    ('cluster_group__n', 'cluster_group__n_example'),
                    ('cluster_type_id__n', 'cluster_type_id__n_example'),
                    ('cluster_type__n', 'cluster_type__n_example'),
                    ('cluster_id__n', 'cluster_id__n_example'),
                    ('device_id__n', 'device_id__n_example'),
                    ('device__n', 'device__n_example'),
                    ('region_id__n', 'region_id__n_example'),
                    ('region__n', 'region__n_example'),
                    ('site_group_id__n', 'site_group_id__n_example'),
                    ('site_group__n', 'site_group__n_example'),
                    ('site_id__n', 'site_id__n_example'),
                    ('site__n', 'site__n_example'),
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
                    ('role_id__n', 'role_id__n_example'),
                    ('role__n', 'role__n_example'),
                    ('platform_id__n', 'platform_id__n_example'),
                    ('platform__n', 'platform__n_example'),
                    ('mac_address__n', 'mac_address__n_example'),
                    ('mac_address__ic', 'mac_address__ic_example'),
                    ('mac_address__nic', 'mac_address__nic_example'),
                    ('mac_address__iew', 'mac_address__iew_example'),
                    ('mac_address__niew', 'mac_address__niew_example'),
                    ('mac_address__isw', 'mac_address__isw_example'),
                    ('mac_address__nisw', 'mac_address__nisw_example'),
                    ('mac_address__ie', 'mac_address__ie_example'),
                    ('mac_address__nie', 'mac_address__nie_example'),
                    ('ordering', 'ordering_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/virtual-machines/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_virtual_machines_partial_update(client):
    """Test case for virtualization_virtual_machines_partial_update

    
    """
    body = {"cluster":0,"memory":1210617418,"role":3,"config_context":"{}","primary_ip":"primary_ip","description":"description","platform":2,"id":5,"tenant":4,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","vcpus":0.7486281948385884,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"disk":314780940,"site":2,"local_context_data":"{}","name":"name","device":6,"primary_ip6":9,"primary_ip4":7,"status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/virtualization/virtual-machines/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_virtual_machines_read(client):
    """Test case for virtualization_virtual_machines_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/virtualization/virtual-machines/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtualization_virtual_machines_update(client):
    """Test case for virtualization_virtual_machines_update

    
    """
    body = {"cluster":0,"memory":1210617418,"role":3,"config_context":"{}","primary_ip":"primary_ip","description":"description","platform":2,"id":5,"tenant":4,"last_updated":"2000-01-23T04:56:07.000+00:00","comments":"comments","created":"2000-01-23T04:56:07.000+00:00","custom_fields":"{}","display":"display","vcpus":0.7486281948385884,"url":"https://openapi-generator.tech","tags":[{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"},{"color":"color","display":"display","name":"name","id":9,"slug":"slug","url":"https://openapi-generator.tech"}],"disk":314780940,"site":2,"local_context_data":"{}","name":"name","device":6,"primary_ip6":9,"primary_ip4":7,"status":"offline"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/virtualization/virtual-machines/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

