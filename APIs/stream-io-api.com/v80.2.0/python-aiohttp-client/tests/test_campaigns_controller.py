# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.create_campaign_request import CreateCampaignRequest
from openapi_server.models.create_campaign_response import CreateCampaignResponse
from openapi_server.models.create_segment_request import CreateSegmentRequest
from openapi_server.models.create_segment_response import CreateSegmentResponse
from openapi_server.models.delete_campaign_response import DeleteCampaignResponse
from openapi_server.models.delete_segment_response import DeleteSegmentResponse
from openapi_server.models.query_campaigns_request import QueryCampaignsRequest
from openapi_server.models.query_campaigns_response import QueryCampaignsResponse
from openapi_server.models.query_recipients_request import QueryRecipientsRequest
from openapi_server.models.query_recipients_response import QueryRecipientsResponse
from openapi_server.models.query_segments_request import QuerySegmentsRequest
from openapi_server.models.query_segments_response import QuerySegmentsResponse
from openapi_server.models.resume_campaign_response import ResumeCampaignResponse
from openapi_server.models.schedule_campaign_request import ScheduleCampaignRequest
from openapi_server.models.schedule_campaign_response import ScheduleCampaignResponse
from openapi_server.models.stop_campaign_response import StopCampaignResponse
from openapi_server.models.test_campaign_request import TestCampaignRequest
from openapi_server.models.test_campaign_response import TestCampaignResponse
from openapi_server.models.update_campaign_request import UpdateCampaignRequest
from openapi_server.models.update_campaign_response import UpdateCampaignResponse
from openapi_server.models.update_segment_request import UpdateSegmentRequest
from openapi_server.models.update_segment_response import UpdateSegmentResponse


pytestmark = pytest.mark.asyncio

async def test_create_campaign(client):
    """Test case for create_campaign

    Create campaign
    """
    body = {"campaign":{"attachments":[{"author_name":"author_name","original_width":6,"thumb_url":"thumb_url","giphy":{"fixed_height":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"original":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"}},"color":"color","footer":"footer","image_url":"image_url","footer_icon":"footer_icon","title_link":"title_link","asset_url":"asset_url","title":"title","type":"type","author_icon":"author_icon","author_link":"author_link","og_scrape_url":"og_scrape_url","pretext":"pretext","original_height":0,"text":"text","fields":[{"short":True,"title":"title","value":"value"},{"short":True,"title":"title","value":"value"}],"actions":[{"name":"name","style":"style","text":"text","type":"type","value":"value"},{"name":"name","style":"style","text":"text","type":"type","value":"value"}],"fallback":"fallback"},{"author_name":"author_name","original_width":6,"thumb_url":"thumb_url","giphy":{"fixed_height":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"original":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"}},"color":"color","footer":"footer","image_url":"image_url","footer_icon":"footer_icon","title_link":"title_link","asset_url":"asset_url","title":"title","type":"type","author_icon":"author_icon","author_link":"author_link","og_scrape_url":"og_scrape_url","pretext":"pretext","original_height":0,"text":"text","fields":[{"short":True,"title":"title","value":"value"},{"short":True,"title":"title","value":"value"}],"actions":[{"name":"name","style":"style","text":"text","type":"type","value":"value"},{"name":"name","style":"style","text":"text","type":"type","value":"value"}],"fallback":"fallback"}],"defaults":{"key":"defaults"},"name":"name","description":"description","text":"text","channel_type":"channel_type","segment_id":"segment_id","sender_id":"sender_id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/campaigns',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_segment(client):
    """Test case for create_segment

    Create segment
    """
    body = {"segment":{"filter":{"key":""},"name":"name","description":"description","type":"user"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/segments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_campaign(client):
    """Test case for delete_campaign

    Delete campaign
    """
    params = [('recipients', True)]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/campaigns/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_segment(client):
    """Test case for delete_segment

    Delete segment
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/segments/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_campaigns(client):
    """Test case for query_campaigns

    Query campaigns
    """
    params = [('payload', openapi_server.QueryCampaignsRequest())]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/campaigns',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_recipients(client):
    """Test case for query_recipients

    Query recipients
    """
    params = [('payload', openapi_server.QueryRecipientsRequest())]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/recipients',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_query_segments(client):
    """Test case for query_segments

    Query segments
    """
    params = [('payload', openapi_server.QuerySegmentsRequest())]
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/segments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resume_campaign(client):
    """Test case for resume_campaign

    Resume campaign
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/campaigns/{id}/resume'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_schedule_campaign(client):
    """Test case for schedule_campaign

    Schedule campaign
    """
    body = {"scheduled_for":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/campaigns/{id}/schedule'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_campaign(client):
    """Test case for stop_campaign

    Stop campaign
    """
    headers = { 
        'Accept': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/campaigns/{id}/stop'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_campaign(client):
    """Test case for test_campaign

    Test campaign
    """
    body = {"users":["users","users"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/campaigns/{id}/test'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_campaign(client):
    """Test case for update_campaign

    Update campaign
    """
    body = {"campaign":{"attachments":[{"author_name":"author_name","original_width":6,"thumb_url":"thumb_url","giphy":{"fixed_height":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"original":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"}},"color":"color","footer":"footer","image_url":"image_url","footer_icon":"footer_icon","title_link":"title_link","asset_url":"asset_url","title":"title","type":"type","author_icon":"author_icon","author_link":"author_link","og_scrape_url":"og_scrape_url","pretext":"pretext","original_height":0,"text":"text","fields":[{"short":True,"title":"title","value":"value"},{"short":True,"title":"title","value":"value"}],"actions":[{"name":"name","style":"style","text":"text","type":"type","value":"value"},{"name":"name","style":"style","text":"text","type":"type","value":"value"}],"fallback":"fallback"},{"author_name":"author_name","original_width":6,"thumb_url":"thumb_url","giphy":{"fixed_height":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"original":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_height_downsampled":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"},"fixed_width_still":{"frames":"frames","size":"size","width":"width","url":"url","height":"height"}},"color":"color","footer":"footer","image_url":"image_url","footer_icon":"footer_icon","title_link":"title_link","asset_url":"asset_url","title":"title","type":"type","author_icon":"author_icon","author_link":"author_link","og_scrape_url":"og_scrape_url","pretext":"pretext","original_height":0,"text":"text","fields":[{"short":True,"title":"title","value":"value"},{"short":True,"title":"title","value":"value"}],"actions":[{"name":"name","style":"style","text":"text","type":"type","value":"value"},{"name":"name","style":"style","text":"text","type":"type","value":"value"}],"fallback":"fallback"}],"defaults":{"key":"defaults"},"name":"name","description":"description","text":"text","channel_type":"channel_type","segment_id":"segment_id","sender_id":"sender_id"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/campaigns/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_segment(client):
    """Test case for update_segment

    Update segment
    """
    body = {"segment":{"filter":{"key":""},"name":"name","description":"description","type":"user"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'stream-auth-type': 'special-key',
        'api_key': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/segments/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

