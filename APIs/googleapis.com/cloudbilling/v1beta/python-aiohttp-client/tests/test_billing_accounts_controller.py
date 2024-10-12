# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.estimate_cost_scenario_for_billing_account_request import EstimateCostScenarioForBillingAccountRequest
from openapi_server.models.estimate_cost_scenario_for_billing_account_response import EstimateCostScenarioForBillingAccountResponse
from openapi_server.models.google_cloud_billing_billingaccountservices_v1beta_list_billing_account_services_response import GoogleCloudBillingBillingaccountservicesV1betaListBillingAccountServicesResponse
from openapi_server.models.google_cloud_billing_billingaccountskugroups_v1beta_list_billing_account_sku_groups_response import GoogleCloudBillingBillingaccountskugroupsV1betaListBillingAccountSkuGroupsResponse


pytestmark = pytest.mark.asyncio

async def test_cloudbilling_billing_accounts_estimate_cost_scenario(client):
    """Test case for cloudbilling_billing_accounts_estimate_cost_scenario

    
    """
    body = {"costScenario":{"commitments":[{"vmResourceBasedCud":{"machineSeries":"machineSeries","guestAccelerator":{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount"},"memorySizeGb":0.8008281904610115,"region":"region","virtualCpuCount":"virtualCpuCount","plan":"COMMITMENT_PLAN_UNSPECIFIED"},"name":"name"},{"vmResourceBasedCud":{"machineSeries":"machineSeries","guestAccelerator":{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount"},"memorySizeGb":0.8008281904610115,"region":"region","virtualCpuCount":"virtualCpuCount","plan":"COMMITMENT_PLAN_UNSPECIFIED"},"name":"name"}],"workloads":[{"cloudCdnEgressWorkload":{"cacheEgressDestination":"CACHE_EGRESS_DESTINATION_UNSPECIFIED","cacheEgressRate":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}}},"cloudInterconnectEgressWorkload":{"interconnectConnectionLocation":"INTERCONNECT_CONNECTION_LOCATION_UNSPECIFIED","egressRate":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}}},"cloudInterconnectWorkload":{"interconnectType":"INTERCONNECT_TYPE_UNSPECIFIED","interconnectAttachments":[{"bandwidth":"BANDWIDTH_UNSPECIFIED","vlanCount":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}}},{"bandwidth":"BANDWIDTH_UNSPECIFIED","vlanCount":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}}}],"linkType":"LINK_TYPE_UNSPECIFIED","provisionedLinkCount":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}}},"vmToVmEgressWorkload":{"interRegionEgress":{"egressRate":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"destinationRegion":"destinationRegion","sourceRegion":"sourceRegion"},"intraRegionEgress":{"egressRate":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}}}},"name":"name","cloudCdnWorkload":{"cacheFillRate":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"cacheLookUpRate":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"cacheFillRegions":{"destinationRegion":"CACHE_FILL_DESTINATION_REGION_UNSPECIFIED","sourceRegion":"CACHE_FILL_SOURCE_REGION_UNSPECIFIED"},"cacheFillOriginService":"CACHE_FILL_ORIGIN_SERVICE_UNSPECIFIED"},"standardTierEgressWorkload":{"egressRate":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"sourceRegion":"sourceRegion"},"cloudStorageWorkload":{"dataStored":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"storageClass":"storageClass","operationB":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"operationA":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"dualRegion":{"name":"name"},"region":{"name":"name"},"dataRetrieval":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"multiRegion":{"name":"name"}},"computeVmWorkload":{"licenses":["licenses","licenses"],"preemptible":True,"guestAccelerator":{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount"},"instancesRunning":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"persistentDisks":[{"diskSize":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"provisionedIops":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"scope":"SCOPE_UNSPECIFIED","diskType":"diskType"},{"diskSize":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"provisionedIops":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"scope":"SCOPE_UNSPECIFIED","diskType":"diskType"}],"region":"region","enableConfidentialCompute":True,"machineType":{"predefinedMachineType":{"machineType":"machineType"},"customMachineType":{"machineSeries":"machineSeries","memorySizeGb":1.4658129805029452,"virtualCpuCount":"virtualCpuCount"}}},"cloudStorageEgressWorkload":{"sourceContinent":"SOURCE_CONTINENT_UNSPECIFIED","egressRate":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"destinationContinent":"DESTINATION_CONTINENT_UNSPECIFIED"},"premiumTierEgressWorkload":{"egressRate":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"destinationContinent":"DESTINATION_CONTINENT_UNSPECIFIED","sourceRegion":"sourceRegion"}},{"cloudCdnEgressWorkload":{"cacheEgressDestination":"CACHE_EGRESS_DESTINATION_UNSPECIFIED","cacheEgressRate":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}}},"cloudInterconnectEgressWorkload":{"interconnectConnectionLocation":"INTERCONNECT_CONNECTION_LOCATION_UNSPECIFIED","egressRate":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}}},"cloudInterconnectWorkload":{"interconnectType":"INTERCONNECT_TYPE_UNSPECIFIED","interconnectAttachments":[{"bandwidth":"BANDWIDTH_UNSPECIFIED","vlanCount":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}}},{"bandwidth":"BANDWIDTH_UNSPECIFIED","vlanCount":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}}}],"linkType":"LINK_TYPE_UNSPECIFIED","provisionedLinkCount":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}}},"vmToVmEgressWorkload":{"interRegionEgress":{"egressRate":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"destinationRegion":"destinationRegion","sourceRegion":"sourceRegion"},"intraRegionEgress":{"egressRate":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}}}},"name":"name","cloudCdnWorkload":{"cacheFillRate":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"cacheLookUpRate":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"cacheFillRegions":{"destinationRegion":"CACHE_FILL_DESTINATION_REGION_UNSPECIFIED","sourceRegion":"CACHE_FILL_SOURCE_REGION_UNSPECIFIED"},"cacheFillOriginService":"CACHE_FILL_ORIGIN_SERVICE_UNSPECIFIED"},"standardTierEgressWorkload":{"egressRate":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"sourceRegion":"sourceRegion"},"cloudStorageWorkload":{"dataStored":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"storageClass":"storageClass","operationB":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"operationA":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"dualRegion":{"name":"name"},"region":{"name":"name"},"dataRetrieval":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"multiRegion":{"name":"name"}},"computeVmWorkload":{"licenses":["licenses","licenses"],"preemptible":True,"guestAccelerator":{"acceleratorType":"acceleratorType","acceleratorCount":"acceleratorCount"},"instancesRunning":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"persistentDisks":[{"diskSize":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"provisionedIops":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"scope":"SCOPE_UNSPECIFIED","diskType":"diskType"},{"diskSize":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"provisionedIops":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"scope":"SCOPE_UNSPECIFIED","diskType":"diskType"}],"region":"region","enableConfidentialCompute":True,"machineType":{"predefinedMachineType":{"machineType":"machineType"},"customMachineType":{"machineSeries":"machineSeries","memorySizeGb":1.4658129805029452,"virtualCpuCount":"virtualCpuCount"}}},"cloudStorageEgressWorkload":{"sourceContinent":"SOURCE_CONTINENT_UNSPECIFIED","egressRate":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"destinationContinent":"DESTINATION_CONTINENT_UNSPECIFIED"},"premiumTierEgressWorkload":{"egressRate":{"usageRateTimeline":{"unit":"unit","usageRateTimelineEntries":[{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}},{"usageRate":6.027456183070403,"effectiveTime":{"estimationTimeFrameOffset":"estimationTimeFrameOffset"}}]}},"destinationContinent":"DESTINATION_CONTINENT_UNSPECIFIED","sourceRegion":"sourceRegion"}}],"scenarioConfig":{"estimateDuration":"estimateDuration"}}}
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
        path='/v1beta/{billing_accountestimate_cost_scenari}'.format(billing_account='billing_account_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudbilling_billing_accounts_services_list(client):
    """Test case for cloudbilling_billing_accounts_services_list

    
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
        path='/v1beta/{parent}/services'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cloudbilling_billing_accounts_sku_groups_list(client):
    """Test case for cloudbilling_billing_accounts_sku_groups_list

    
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
        path='/v1beta/{parent}/skuGroups'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

