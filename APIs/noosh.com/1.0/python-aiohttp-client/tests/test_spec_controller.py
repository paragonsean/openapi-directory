# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.property_param_list_vo import PropertyParamListVO
from openapi_server.models.spec_http_status_vo import SpecHTTPStatusVO
from openapi_server.models.spec_list_vo import SpecListVO
from openapi_server.models.spec_persist_vo import SpecPersistVO
from openapi_server.models.spec_type_fields_list_vo import SpecTypeFieldsListVO
from openapi_server.models.spec_update_persist_vo import SpecUpdatePersistVO
from openapi_server.models.spec_vo import SpecVO
from openapi_server.models.v1_x1_spec_updating_po import V1X1SpecUpdatingPO
from openapi_server.models.v1x1_spec_expand_vo import V1x1SpecExpandVO
from openapi_server.models.wg_spec_prd_type_reg_persist_vo import WgSpecPrdTypeRegPersistVO
from openapi_server.models.workgroup_attribute_list_vo import WorkgroupAttributeListVO


pytestmark = pytest.mark.asyncio

async def test_get_product_type_list_of_workgroup(client):
    """Test case for get_product_type_list_of_workgroup

    Get product type of workgroup level
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/productTypes'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_spec(client):
    """Test case for get_spec

    List a specific spec of project Level
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/1.1/workgroups/{workgroup_id}/projects/{project_id}/specs/{spec_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', spec_id='spec_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_spec_list(client):
    """Test case for get_spec_list

    List specs of project Level
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/specs'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_spec_product_type_list_of_workgroup(client):
    """Test case for get_spec_product_type_list_of_workgroup

    Get product type of spec level by workgroupId
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/productTypesOfSpecTypes'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_spec_type_fields(client):
    """Test case for get_spec_type_fields

    Get Spec Type Fields
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/1.1/workgroups/{workgroup_id}/specTypes/{spec_type_id}/specTypeFields'.format(workgroup_id='workgroup_id_example', spec_type_id='spec_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_spec(client):
    """Test case for post_spec

    Create a Spec
    """
    body = {"quantity_5":1,"quantity_4":1,"spec_template_id":1,"versions":[{"qty":1,"description":"sample description"},{"qty":1,"description":"sample description"}],"jsonBody":False,"product_type_id":1,"spec_name":"sample spec_name","quantity_1":1,"sku":"sample sku","quantity_3":1,"spec_type_id":1,"quantity_2":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/specs'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_spec_product_type_list_of_workgroup(client):
    """Test case for post_spec_product_type_list_of_workgroup

    Register product types for spec types
    """
    body = {"enableDifferentiatePrdTypePreference":False,"spec_prdType_list":[{"prdType_labels":["sample prdType_labels","sample prdType_labels"],"spec_type_id":1},{"prdType_labels":["sample prdType_labels","sample prdType_labels"],"spec_type_id":1}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/v1/workgroups/{workgroup_id}/productTypesOfSpecTypes'.format(workgroup_id='workgroup_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_put_spec(client):
    """Test case for put_spec

    Update a specific Spec
    """
    body = {"quantity_5":1,"quantity_4":1,"product_type_id":1,"first_level_custom_fields":{"property_attributes":[{"attribute_id":1,"attribute_value":"","label":"sample label","param_name":"sample param_name","param_id":1},{"attribute_id":1,"attribute_value":"","label":"sample label","param_name":"sample param_name","param_id":1}],"property_id":1,"property_name":"sample property_name"},"versions":[{"qty":1,"description":"sample description"},{"qty":1,"description":"sample description"}],"second_level_custom_fields":[{"property_attributes":[{"attribute_id":1,"attribute_value":"","label":"sample label","param_name":"sample param_name","param_id":1},{"attribute_id":1,"attribute_value":"","label":"sample label","param_name":"sample param_name","param_id":1}],"property_id":1,"property_name":"sample property_name"},{"property_attributes":[{"attribute_id":1,"attribute_value":"","label":"sample label","param_name":"sample param_name","param_id":1},{"attribute_id":1,"attribute_value":"","label":"sample label","param_name":"sample param_name","param_id":1}],"property_id":1,"property_name":"sample property_name"}],"spec_name":"sample spec_name","quantity_1":1,"sku":"sample sku","quantity_3":1,"spec_type_id":1,"header_custom_fields":{"property_attributes":[{"attribute_id":1,"attribute_value":"","label":"sample label","param_name":"sample param_name","param_id":1},{"attribute_id":1,"attribute_value":"","label":"sample label","param_name":"sample param_name","param_id":1}],"property_id":1,"property_name":"sample property_name"},"quantity_2":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/1.1/workgroups/{workgroup_id}/projects/{project_id}/specs/{spec_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', spec_id='spec_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_workgroups_workgroup_id_projects_project_id_specs_spec_id_get(client):
    """Test case for v1_workgroups_workgroup_id_projects_project_id_specs_spec_id_get

    List a specific spec of project Level
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/specs/{spec_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', spec_id='spec_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_v1_workgroups_workgroup_id_projects_project_id_specs_spec_id_put(client):
    """Test case for v1_workgroups_workgroup_id_projects_project_id_specs_spec_id_put

    Update a specific Spec
    """
    body = {"quantity_5":1,"quantity_4":1,"inks_and_paper":[{"custom_fields":[{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"},{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"}],"paper_id":1},{"custom_fields":[{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"},{"number_value":"","string_value":"sample string_value","date_value":"2000-01-23","param_name":"sample param_name"}],"paper_id":1}],"product_type_id":1,"spec_name":"sample spec_name","quantity_1":1,"sku":"sample sku","quantity_3":1,"quantity_2":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/specs/{spec_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', spec_id='spec_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_workgroups_workgroup_id_spec_types_spec_type_id_spec_type_fields_get(client):
    """Test case for v1_workgroups_workgroup_id_spec_types_spec_type_id_spec_type_fields_get

    Get Spec Type Fields
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/specTypes/{spec_type_id}/specTypeFields'.format(workgroup_id='workgroup_id_example', spec_type_id='spec_type_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

