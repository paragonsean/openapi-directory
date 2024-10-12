# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.age_rating_declaration_response import AgeRatingDeclarationResponse
from openapi_server.models.age_rating_declaration_update_request import AgeRatingDeclarationUpdateRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_age_rating_declarations_update_instance(client):
    """Test case for age_rating_declarations_update_instance

    
    """
    body = {"data":{"attributes":{"alcoholTobaccoOrDrugUseOrReferences":"NONE","gamblingAndContests":True,"gamblingSimulated":"NONE","sexualContentGraphicAndNudity":"NONE","violenceRealistic":"NONE","gambling":True,"horrorOrFearThemes":"NONE","profanityOrCrudeHumor":"NONE","seventeenPlus":True,"violenceRealisticProlongedGraphicOrSadistic":"NONE","contests":"NONE","matureOrSuggestiveThemes":"NONE","unrestrictedWebAccess":True,"violenceCartoonOrFantasy":"NONE","kidsAgeBand":"FIVE_AND_UNDER","medicalOrTreatmentInformation":"NONE","sexualContentOrNudity":"NONE"},"id":"id","type":"ageRatingDeclarations"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/ageRatingDeclarations/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

