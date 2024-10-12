# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.offers_offer_id_changelog_get200_response import OffersOfferIdChangelogGet200Response


pytestmark = pytest.mark.asyncio

async def test_offers_offer_id_changelog_get(client):
    """Test case for offers_offer_id_changelog_get

    Get list of changelog history for the offer. Returns offer object with contact and user objects if they are provided
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/offers/{offer_id}/changelog'.format(offer_id='offer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

