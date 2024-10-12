# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_share_add_response import BulkShareAddResponse
from openapi_server.models.host_share_detail import HostShareDetail
from openapi_server.models.host_share_update import HostShareUpdate
from openapi_server.models.nas_shares_to_add import NasSharesToAdd


pytestmark = pytest.mark.asyncio

async def test_bulk_add_host_shares(client):
    """Test case for bulk_add_host_shares

    Add NAS shares in bulk
    """
    body = {"hostId":"hostId","nasShares":[{"exportPoint":"exportPoint","shareType":"NFS"},{"exportPoint":"exportPoint","shareType":"NFS"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/host/share/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bulk_update_host_share(client):
    """Test case for bulk_update_host_share

    Update network shares
    """
    body = {"updateProperties":{"exportPoint":"exportPoint","password":"password","hostShareParameters":{"isNetAppSnapDiffEnabled":True,"isOnNetAppSnapMirrorDestVolume":True,"isIsilonChangelistEnabled":True},"domain":"domain","username":"username"},"shareId":"shareId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/host/share/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

