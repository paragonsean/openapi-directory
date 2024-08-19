# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ad_unit import AdUnit
from openapi_server.models.ad_unit_mapping import AdUnitMapping
from openapi_server.models.app import App
from openapi_server.models.batch_create_ad_unit_mappings_request import BatchCreateAdUnitMappingsRequest
from openapi_server.models.batch_create_ad_unit_mappings_response import BatchCreateAdUnitMappingsResponse
from openapi_server.models.generate_campaign_report_request import GenerateCampaignReportRequest
from openapi_server.models.generate_campaign_report_response import GenerateCampaignReportResponse
from openapi_server.models.generate_mediation_report_request import GenerateMediationReportRequest
from openapi_server.models.generate_mediation_report_response import GenerateMediationReportResponse
from openapi_server.models.generate_network_report_request import GenerateNetworkReportRequest
from openapi_server.models.generate_network_report_response import GenerateNetworkReportResponse
from openapi_server.models.list_ad_sources_response import ListAdSourcesResponse
from openapi_server.models.list_ad_unit_mappings_response import ListAdUnitMappingsResponse
from openapi_server.models.list_ad_units_response import ListAdUnitsResponse
from openapi_server.models.list_adapters_response import ListAdaptersResponse
from openapi_server.models.list_apps_response import ListAppsResponse
from openapi_server.models.list_mediation_groups_response import ListMediationGroupsResponse
from openapi_server.models.list_publisher_accounts_response import ListPublisherAccountsResponse
from openapi_server.models.mediation_ab_experiment import MediationAbExperiment
from openapi_server.models.mediation_group import MediationGroup
from openapi_server.models.publisher_account import PublisherAccount
from openapi_server.models.stop_mediation_ab_experiment_request import StopMediationAbExperimentRequest


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_ad_sources_adapters_list(client):
    """Test case for admob_accounts_ad_sources_adapters_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta/{parent}/adapters'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_ad_sources_list(client):
    """Test case for admob_accounts_ad_sources_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta/{parent}/adSources'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_ad_unit_mappings_batch_create(client):
    """Test case for admob_accounts_ad_unit_mappings_batch_create

    
    """
    body = {"requests":[{"adUnitMapping":{"displayName":"displayName","name":"name","adUnitConfigurations":{"key":"adUnitConfigurations"},"adapterId":"adapterId","state":"STATE_UNSPECIFIED"},"parent":"parent"},{"adUnitMapping":{"displayName":"displayName","name":"name","adUnitConfigurations":{"key":"adUnitConfigurations"},"adapterId":"adapterId","state":"STATE_UNSPECIFIED"},"parent":"parent"}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1beta/{parent}/adUnitMappings:batchCreate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_ad_units_ad_unit_mappings_create(client):
    """Test case for admob_accounts_ad_units_ad_unit_mappings_create

    
    """
    body = {"displayName":"displayName","name":"name","adUnitConfigurations":{"key":"adUnitConfigurations"},"adapterId":"adapterId","state":"STATE_UNSPECIFIED"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1beta/{parent}/adUnitMappings'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_ad_units_ad_unit_mappings_list(client):
    """Test case for admob_accounts_ad_units_ad_unit_mappings_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta/{parent}/adUnitMappings'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_ad_units_create(client):
    """Test case for admob_accounts_ad_units_create

    
    """
    body = {"displayName":"displayName","appId":"appId","name":"name","adFormat":"adFormat","adUnitId":"adUnitId","adTypes":["adTypes","adTypes"],"rewardSettings":{"unitType":"unitType","unitAmount":"unitAmount"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1beta/{parent}/adUnits'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_ad_units_list(client):
    """Test case for admob_accounts_ad_units_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta/{parent}/adUnits'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_apps_create(client):
    """Test case for admob_accounts_apps_create

    
    """
    body = {"manualAppInfo":{"displayName":"displayName"},"linkedAppInfo":{"displayName":"displayName","androidAppStores":["ANDROID_APP_STORE_UNSPECIFIED","ANDROID_APP_STORE_UNSPECIFIED"],"appStoreId":"appStoreId"},"appId":"appId","name":"name","appApprovalState":"APP_APPROVAL_STATE_UNSPECIFIED","platform":"platform"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1beta/{parent}/apps'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_apps_list(client):
    """Test case for admob_accounts_apps_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta/{parent}/apps'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_campaign_report_generate(client):
    """Test case for admob_accounts_campaign_report_generate

    
    """
    body = {"reportSpec":{"dateRange":{"endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0}},"metrics":["METRIC_UNSPECIFIED","METRIC_UNSPECIFIED"],"languageCode":"languageCode","dimensions":["DIMENSION_UNSPECIFIED","DIMENSION_UNSPECIFIED"]}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta/{parent}/campaignReport:generate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_get(client):
    """Test case for admob_accounts_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_list(client):
    """Test case for admob_accounts_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta/accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_mediation_groups_create(client):
    """Test case for admob_accounts_mediation_groups_create

    
    """
    body = {"mediationAbExperimentState":"EXPERIMENT_STATE_UNSPECIFIED","mediationGroupId":"mediationGroupId","targeting":{"targetedRegionCodes":["targetedRegionCodes","targetedRegionCodes"],"idfaTargeting":"IDFA_TARGETING_UNSPECIFIED","adUnitIds":["adUnitIds","adUnitIds"],"format":"format","excludedRegionCodes":["excludedRegionCodes","excludedRegionCodes"],"platform":"platform"},"displayName":"displayName","name":"name","state":"STATE_UNSPECIFIED","mediationGroupLines":{"key":{"experimentVariant":"VARIANT_UNSPECIFIED","cpmMicros":"cpmMicros","displayName":"displayName","adUnitMappings":{"key":"adUnitMappings"},"adSourceId":"adSourceId","id":"id","state":"STATE_UNSPECIFIED","cpmMode":"CPM_MODE_UNSPECIFIED"}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1beta/{parent}/mediationGroups'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_mediation_groups_list(client):
    """Test case for admob_accounts_mediation_groups_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta/{parent}/mediationGroups'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_mediation_groups_mediation_ab_experiments_create(client):
    """Test case for admob_accounts_mediation_groups_mediation_ab_experiments_create

    
    """
    body = {"mediationGroupId":"mediationGroupId","treatmentTrafficPercentage":"treatmentTrafficPercentage","variantLeader":"VARIANT_LEADER_UNSPECIFIED","displayName":"displayName","controlMediationLines":[{"mediationGroupLine":{"experimentVariant":"VARIANT_UNSPECIFIED","cpmMicros":"cpmMicros","displayName":"displayName","adUnitMappings":{"key":"adUnitMappings"},"adSourceId":"adSourceId","id":"id","state":"STATE_UNSPECIFIED","cpmMode":"CPM_MODE_UNSPECIFIED"}},{"mediationGroupLine":{"experimentVariant":"VARIANT_UNSPECIFIED","cpmMicros":"cpmMicros","displayName":"displayName","adUnitMappings":{"key":"adUnitMappings"},"adSourceId":"adSourceId","id":"id","state":"STATE_UNSPECIFIED","cpmMode":"CPM_MODE_UNSPECIFIED"}}],"name":"name","experimentId":"experimentId","startTime":"startTime","treatmentMediationLines":[{"mediationGroupLine":{"experimentVariant":"VARIANT_UNSPECIFIED","cpmMicros":"cpmMicros","displayName":"displayName","adUnitMappings":{"key":"adUnitMappings"},"adSourceId":"adSourceId","id":"id","state":"STATE_UNSPECIFIED","cpmMode":"CPM_MODE_UNSPECIFIED"}},{"mediationGroupLine":{"experimentVariant":"VARIANT_UNSPECIFIED","cpmMicros":"cpmMicros","displayName":"displayName","adUnitMappings":{"key":"adUnitMappings"},"adSourceId":"adSourceId","id":"id","state":"STATE_UNSPECIFIED","cpmMode":"CPM_MODE_UNSPECIFIED"}}],"endTime":"endTime","state":"EXPERIMENT_STATE_UNSPECIFIED"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1beta/{parent}/mediationAbExperiments'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_mediation_groups_mediation_ab_experiments_stop(client):
    """Test case for admob_accounts_mediation_groups_mediation_ab_experiments_stop

    
    """
    body = {"variantChoice":"VARIANT_CHOICE_UNSPECIFIED"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1beta/{namesto}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_mediation_groups_patch(client):
    """Test case for admob_accounts_mediation_groups_patch

    
    """
    body = {"mediationAbExperimentState":"EXPERIMENT_STATE_UNSPECIFIED","mediationGroupId":"mediationGroupId","targeting":{"targetedRegionCodes":["targetedRegionCodes","targetedRegionCodes"],"idfaTargeting":"IDFA_TARGETING_UNSPECIFIED","adUnitIds":["adUnitIds","adUnitIds"],"format":"format","excludedRegionCodes":["excludedRegionCodes","excludedRegionCodes"],"platform":"platform"},"displayName":"displayName","name":"name","state":"STATE_UNSPECIFIED","mediationGroupLines":{"key":{"experimentVariant":"VARIANT_UNSPECIFIED","cpmMicros":"cpmMicros","displayName":"displayName","adUnitMappings":{"key":"adUnitMappings"},"adSourceId":"adSourceId","id":"id","state":"STATE_UNSPECIFIED","cpmMode":"CPM_MODE_UNSPECIFIED"}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v1beta/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_mediation_report_generate(client):
    """Test case for admob_accounts_mediation_report_generate

    
    """
    body = {"reportSpec":{"sortConditions":[{"metric":"METRIC_UNSPECIFIED","dimension":"DIMENSION_UNSPECIFIED","order":"SORT_ORDER_UNSPECIFIED"},{"metric":"METRIC_UNSPECIFIED","dimension":"DIMENSION_UNSPECIFIED","order":"SORT_ORDER_UNSPECIFIED"}],"dimensionFilters":[{"matchesAny":{"values":["values","values"]},"dimension":"DIMENSION_UNSPECIFIED"},{"matchesAny":{"values":["values","values"]},"dimension":"DIMENSION_UNSPECIFIED"}],"dateRange":{"endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0}},"timeZone":"timeZone","localizationSettings":{"languageCode":"languageCode","currencyCode":"currencyCode"},"metrics":["METRIC_UNSPECIFIED","METRIC_UNSPECIFIED"],"maxReportRows":0,"dimensions":["DIMENSION_UNSPECIFIED","DIMENSION_UNSPECIFIED"]}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta/{parent}/mediationReport:generate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admob_accounts_network_report_generate(client):
    """Test case for admob_accounts_network_report_generate

    
    """
    body = {"reportSpec":{"sortConditions":[{"metric":"METRIC_UNSPECIFIED","dimension":"DIMENSION_UNSPECIFIED","order":"SORT_ORDER_UNSPECIFIED"},{"metric":"METRIC_UNSPECIFIED","dimension":"DIMENSION_UNSPECIFIED","order":"SORT_ORDER_UNSPECIFIED"}],"dimensionFilters":[{"matchesAny":{"values":["values","values"]},"dimension":"DIMENSION_UNSPECIFIED"},{"matchesAny":{"values":["values","values"]},"dimension":"DIMENSION_UNSPECIFIED"}],"dateRange":{"endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0}},"timeZone":"timeZone","localizationSettings":{"languageCode":"languageCode","currencyCode":"currencyCode"},"metrics":["METRIC_UNSPECIFIED","METRIC_UNSPECIFIED"],"maxReportRows":0,"dimensions":["DIMENSION_UNSPECIFIED","DIMENSION_UNSPECIFIED"]}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta/{parent}/networkReport:generate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

