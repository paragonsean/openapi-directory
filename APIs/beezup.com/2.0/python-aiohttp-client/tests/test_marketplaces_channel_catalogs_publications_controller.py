# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_publications import AccountPublications
from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.publish_catalog_to_marketplace_request import PublishCatalogToMarketplaceRequest


pytestmark = pytest.mark.asyncio

async def test_get_publications(client):
    """Test case for get_publications

    Fetch the publication history for an account, sorted by descending start date
    """
    params = [('channelCatalogId', 'channel_catalog_id_example'),
                    ('count', 56),
                    ('publicationTypes', ['publication_types_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/user/marketplaces/channelcatalogs/publications/{marketplace_technical_code}/{account_id}/history'.format(marketplace_technical_code='marketplace_technical_code_example', account_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publish_catalog_to_marketplace(client):
    """Test case for publish_catalog_to_marketplace

    [PREVIEW] Launch a publication of the catalog to the marketplace
    """
    body = openapi_server.PublishCatalogToMarketplaceRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v2/user/marketplaces/channelcatalogs/publications/{marketplace_technical_code}/{account_id}/publish'.format(marketplace_technical_code='marketplace_technical_code_example', account_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

