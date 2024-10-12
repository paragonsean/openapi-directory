# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_onboarding_url_request import GetOnboardingUrlRequest
from openapi_server.models.get_onboarding_url_response import GetOnboardingUrlResponse
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_post_get_onboarding_url(client):
    """Test case for post_get_onboarding_url

    Get a link to a Adyen-hosted onboarding page
    """
    body = {"accountHolderCode":"accountHolderCode","collectInformation":{"bankDetails":True,"individualDetails":True,"businessDetails":True,"legalArrangementDetails":True,"pciQuestionnaire":True,"shareholderDetails":True},"mobileOAuthCallbackUrl":"mobileOAuthCallbackUrl","showPages":{"manualBankAccountPage":True,"shareholderDetailsSummaryPage":True,"checksOverviewPage":True,"bankVerificationPage":True,"businessDetailsSummaryPage":True,"welcomePage":True,"legalArrangementsDetailsSummaryPage":True,"individualDetailsSummaryPage":True,"bankDetailsSummaryPage":True},"editMode":True,"shopperLocale":"shopperLocale","platformName":"platformName","returnUrl":"returnUrl"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/cal/services/Hop/v6/getOnboardingUrl',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

