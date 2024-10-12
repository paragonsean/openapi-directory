# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.edit import Edit
from openapi_server.models.queued_response import QueuedResponse
from openapi_server.models.render_response import RenderResponse


pytestmark = pytest.mark.asyncio

async def test_get_render(client):
    """Test case for get_render

    Get Render Status
    """
    headers = { 
        'Accept': 'application/json',
        'DeveloperKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/render/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_render(client):
    """Test case for post_render

    Render Asset
    """
    body = {"output":{"scaleTo":"preview","thumbnail":{"capture":1,"scale":0.3},"size":{"width":1200,"height":800},"destinations":[{"provider":"shotstack","exclude":False},{"provider":"shotstack","exclude":False}],"format":"mp4","fps":25,"range":{"length":6,"start":3},"aspectRatio":"969","poster":{"capture":1},"resolution":"sd","quality":"medium"},"disk":"local","callback":"https://my-server.com/callback.php","timeline":{"soundtrack":{"volume":0.8008281904610115,"src":"https://s3-ap-northeast-1.amazonaws.com/my-bucket/music.mp3","effect":"fadeIn"},"cache":True,"fonts":[{"src":"https://s3-ap-northeast-1.amazonaws.com/my-bucket/open-sans.ttf"},{"src":"https://s3-ap-northeast-1.amazonaws.com/my-bucket/open-sans.ttf"}],"background":"#000000","tracks":[{"clips":[{"filter":"greyscale","fit":"crop","offset":{"x":0.1,"y":-0.2},"effect":"zoomIn","length":5,"start":2,"scale":0,"position":"center","asset":{"volume":1,"trim":2,"src":"https://s3-ap-northeast-1.amazonaws.com/my-bucket/video.mp4","type":"video","crop":{"top":0.15,"left":0.6027456,"bottom":0.15,"right":0.14658129}},"opacity":5.962133916683182,"transition":{"in":"fade","out":"fade"}},{"filter":"greyscale","fit":"crop","offset":{"x":0.1,"y":-0.2},"effect":"zoomIn","length":5,"start":2,"scale":0,"position":"center","asset":{"volume":1,"trim":2,"src":"https://s3-ap-northeast-1.amazonaws.com/my-bucket/video.mp4","type":"video","crop":{"top":0.15,"left":0.6027456,"bottom":0.15,"right":0.14658129}},"opacity":5.962133916683182,"transition":{"in":"fade","out":"fade"}}]},{"clips":[{"filter":"greyscale","fit":"crop","offset":{"x":0.1,"y":-0.2},"effect":"zoomIn","length":5,"start":2,"scale":0,"position":"center","asset":{"volume":1,"trim":2,"src":"https://s3-ap-northeast-1.amazonaws.com/my-bucket/video.mp4","type":"video","crop":{"top":0.15,"left":0.6027456,"bottom":0.15,"right":0.14658129}},"opacity":5.962133916683182,"transition":{"in":"fade","out":"fade"}},{"filter":"greyscale","fit":"crop","offset":{"x":0.1,"y":-0.2},"effect":"zoomIn","length":5,"start":2,"scale":0,"position":"center","asset":{"volume":1,"trim":2,"src":"https://s3-ap-northeast-1.amazonaws.com/my-bucket/video.mp4","type":"video","crop":{"top":0.15,"left":0.6027456,"bottom":0.15,"right":0.14658129}},"opacity":5.962133916683182,"transition":{"in":"fade","out":"fade"}}]}]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'DeveloperKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/render',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

