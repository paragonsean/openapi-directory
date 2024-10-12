# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.call_summaries_enum_answered_by import CallSummariesEnumAnsweredBy
from openapi_server.models.call_summaries_enum_processing_state_request import CallSummariesEnumProcessingStateRequest
from openapi_server.models.call_summaries_enum_sort_by import CallSummariesEnumSortBy
from openapi_server.models.list_call_summaries_response import ListCallSummariesResponse


pytestmark = pytest.mark.asyncio

async def test_list_call_summaries(client):
    """Test case for list_call_summaries

    
    """
    params = [('From', '_from_example'),
                    ('To', 'to_example'),
                    ('FromCarrier', 'from_carrier_example'),
                    ('ToCarrier', 'to_carrier_example'),
                    ('FromCountryCode', 'from_country_code_example'),
                    ('ToCountryCode', 'to_country_code_example'),
                    ('Branded', True),
                    ('VerifiedCaller', True),
                    ('HasTag', True),
                    ('StartTime', 'start_time_example'),
                    ('EndTime', 'end_time_example'),
                    ('CallType', 'call_type_example'),
                    ('CallState', 'call_state_example'),
                    ('Direction', 'direction_example'),
                    ('ProcessingState', openapi_server.CallSummariesEnumProcessingStateRequest()),
                    ('SortBy', openapi_server.CallSummariesEnumSortBy()),
                    ('Subaccount', 'subaccount_example'),
                    ('AbnormalSession', True),
                    ('AnsweredBy', openapi_server.CallSummariesEnumAnsweredBy()),
                    ('AnsweredByAnnotation', 'answered_by_annotation_example'),
                    ('ConnectivityIssueAnnotation', 'connectivity_issue_annotation_example'),
                    ('QualityIssueAnnotation', 'quality_issue_annotation_example'),
                    ('SpamAnnotation', True),
                    ('CallScoreAnnotation', 'call_score_annotation_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Voice/Summaries',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

