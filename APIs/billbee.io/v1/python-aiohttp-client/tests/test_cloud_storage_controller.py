# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_cloud_storage_api_model import RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCloudStorageApiModel


pytestmark = pytest.mark.asyncio

async def test_cloud_storage_api_get_list(client):
    """Test case for cloud_storage_api_get_list

    Gets a list of all connected cloud storage devices
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cloudstorages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

