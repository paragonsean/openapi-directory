# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.estimate_expand_vo import EstimateExpandVO
from openapi_server.models.estimate_list_expand_vo import EstimateListExpandVO
from openapi_server.models.estimate_po import EstimatePO
from openapi_server.models.http_status_vo import HTTPStatusVO


pytestmark = pytest.mark.asyncio

async def test_get_estimate(client):
    """Test case for get_estimate

    Get a specific estimate of project
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/estimates/{estimate_id}'.format(workgroup_id='workgroup_id_example', project_id='project_id_example', estimate_id='estimate_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_estimate_list(client):
    """Test case for get_estimate_list

    List the Estimates
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/estimates'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_estimate(client):
    """Test case for post_estimate

    Create a Estimate
    """
    body = {"comments":"sample comments","description":"sample description","estimate_items":[{"quantity_1_shipping":"","quantity_1_tax":"","quantity_4_shipping":"","paper_items":[{"quantity_5":1,"quantity_4":1,"qty_uom":"sample qty_uom","price_1":"","price_2":"","price_3":"","price_4":"","price_5":"","paper_id":1,"size":"sample size","min_uom_qty":1,"unit_price_5":"","quantity_1":1,"sku":"sample sku","unit_price_4":"","price_per_tonne":"","unit_price_3":"","quantity_3":1,"unit_price_2":"","quantity_2":1,"unit_price_1":""},{"quantity_5":1,"quantity_4":1,"qty_uom":"sample qty_uom","price_1":"","price_2":"","price_3":"","price_4":"","price_5":"","paper_id":1,"size":"sample size","min_uom_qty":1,"unit_price_5":"","quantity_1":1,"sku":"sample sku","unit_price_4":"","price_per_tonne":"","unit_price_3":"","quantity_3":1,"unit_price_2":"","quantity_2":1,"unit_price_1":""}],"quantity_2_price":"","quantity_5_price":"","quantity_3_shipping":"","quantity_3_tax":"","quantity_1_price":"","quantity_5_tax":"","quantity_2_shipping":"","quantity_2_tax":"","quantity_5_shipping":"","rfe_item_id":1,"quantity_4_price":"","quantity_4_tax":"","quantity_3_price":""},{"quantity_1_shipping":"","quantity_1_tax":"","quantity_4_shipping":"","paper_items":[{"quantity_5":1,"quantity_4":1,"qty_uom":"sample qty_uom","price_1":"","price_2":"","price_3":"","price_4":"","price_5":"","paper_id":1,"size":"sample size","min_uom_qty":1,"unit_price_5":"","quantity_1":1,"sku":"sample sku","unit_price_4":"","price_per_tonne":"","unit_price_3":"","quantity_3":1,"unit_price_2":"","quantity_2":1,"unit_price_1":""},{"quantity_5":1,"quantity_4":1,"qty_uom":"sample qty_uom","price_1":"","price_2":"","price_3":"","price_4":"","price_5":"","paper_id":1,"size":"sample size","min_uom_qty":1,"unit_price_5":"","quantity_1":1,"sku":"sample sku","unit_price_4":"","price_per_tonne":"","unit_price_3":"","quantity_3":1,"unit_price_2":"","quantity_2":1,"unit_price_1":""}],"quantity_2_price":"","quantity_5_price":"","quantity_3_shipping":"","quantity_3_tax":"","quantity_1_price":"","quantity_5_tax":"","quantity_2_shipping":"","quantity_2_tax":"","quantity_5_shipping":"","rfe_item_id":1,"quantity_4_price":"","quantity_4_tax":"","quantity_3_price":""}],"estimate_title":"sample estimate_title","expiration_date":"2000-01-23","rfe_id":1,"owner_reference":"sample owner_reference"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/v1/workgroups/{workgroup_id}/projects/{project_id}/estimates'.format(workgroup_id='workgroup_id_example', project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

