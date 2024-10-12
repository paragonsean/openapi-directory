# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.pack import Pack
from openapi_server.models.pack_response import PackResponse


pytestmark = pytest.mark.asyncio

async def test_root_post(client):
    """Test case for root_post

    
    """
    pack = {"template":"demo.tmpl","seed":True,"allowableOverhang":0.8008281904610115,"boxTypes":[{"price":0,"name":"name","weightTare":0.5962133916683182,"rateTable":"{}","weightMax":0.14658129805029452,"dimensions":"{}"},{"price":0,"name":"name","weightTare":0.5962133916683182,"rateTable":"{}","weightMax":0.14658129805029452,"dimensions":"{}"}],"rules":[{"targetItemRefIds":[6,6],"options":"{}","itemRefId":1,"operation":"exclude","parameters":["parameters","parameters"]},{"targetItemRefIds":[6,6],"options":"{}","itemRefId":1,"operation":"exclude","parameters":["parameters","parameters"]}],"usableSpace":0.7457744773683765,"layFlat":False,"includeImages":True,"random":False,"randomMaxWeight":1,"corners":True,"boxTypeSets":["usps","usps"],"zone":1,"sequenceSort":False,"key":"key","randomMaxDimension":1,"sequenceHeatMap":False,"includeScripts":True,"imgSize":7,"cohortPacking":False,"placementStyle":"default","cohortMax":5,"itemSets":[{"sequence":"sequence","quantity":2,"color":"color","name":"name","weight":3.616076749251911,"refId":9,"dimensions":"{}"},{"sequence":"sequence","quantity":2,"color":"color","name":"name","weight":3.616076749251911,"refId":9,"dimensions":"{}"}],"n":7,"eye":"{}","coordOrder":[2,2],"maxSequenceDistance":4,"packOrigin":"{}","interlock":False}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/',
        headers=headers,
        json=pack,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

