# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_create_jobs_request import BatchCreateJobsRequest
from openapi_server.models.batch_delete_jobs_request import BatchDeleteJobsRequest
from openapi_server.models.batch_update_jobs_request import BatchUpdateJobsRequest
from openapi_server.models.client_event import ClientEvent
from openapi_server.models.company import Company
from openapi_server.models.complete_query_response import CompleteQueryResponse
from openapi_server.models.job import Job
from openapi_server.models.list_companies_response import ListCompaniesResponse
from openapi_server.models.list_jobs_response import ListJobsResponse
from openapi_server.models.list_tenants_response import ListTenantsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.search_jobs_request import SearchJobsRequest
from openapi_server.models.search_jobs_response import SearchJobsResponse
from openapi_server.models.tenant import Tenant


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_tenants_client_events_create(client):
    """Test case for jobs_projects_tenants_client_events_create

    
    """
    body = {"eventId":"eventId","jobEvent":{"jobs":["jobs","jobs"],"type":"JOB_EVENT_TYPE_UNSPECIFIED"},"createTime":"createTime","requestId":"requestId","eventNotes":"eventNotes"}
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
        path='/v4/{parent}/clientEvents'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_tenants_companies_create(client):
    """Test case for jobs_projects_tenants_companies_create

    
    """
    body = {"displayName":"displayName","keywordSearchableJobCustomAttributes":["keywordSearchableJobCustomAttributes","keywordSearchableJobCustomAttributes"],"externalId":"externalId","derivedInfo":{"headquartersLocation":{"postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":5},"locationType":"LOCATION_TYPE_UNSPECIFIED","radiusMiles":2.3021358869347655,"latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}}},"headquartersAddress":"headquartersAddress","eeoText":"eeoText","suspended":True,"websiteUri":"websiteUri","careerSiteUri":"careerSiteUri","hiringAgency":True,"imageUri":"imageUri","size":"COMPANY_SIZE_UNSPECIFIED","name":"name"}
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
        path='/v4/{parent}/companies'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_tenants_companies_list(client):
    """Test case for jobs_projects_tenants_companies_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('requireOpenJobs', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/{parent}/companies'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_tenants_complete_query(client):
    """Test case for jobs_projects_tenants_complete_query

    
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
                    ('company', 'company_example'),
                    ('languageCodes', ['language_codes_example']),
                    ('pageSize', 56),
                    ('query', 'query_example'),
                    ('scope', 'scope_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/{tenantcomplete_quer}'.format(tenant='tenant_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_tenants_create(client):
    """Test case for jobs_projects_tenants_create

    
    """
    body = {"name":"name","externalId":"externalId"}
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
        path='/v4/{parent}/tenants'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_tenants_jobs_batch_create(client):
    """Test case for jobs_projects_tenants_jobs_batch_create

    
    """
    body = {"jobs":[{"addresses":["addresses","addresses"],"processingOptions":{"htmlSanitization":"HTML_SANITIZATION_UNSPECIFIED","disableStreetAddressResolution":True},"description":"description","jobBenefits":["JOB_BENEFIT_UNSPECIFIED","JOB_BENEFIT_UNSPECIFIED"],"title":"title","compensationInfo":{"entries":[{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"unit":"COMPENSATION_UNIT_UNSPECIFIED","description":"description","range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"expectedUnitsPerYear":6.027456183070403,"type":"COMPENSATION_TYPE_UNSPECIFIED"},{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"unit":"COMPENSATION_UNIT_UNSPECIFIED","description":"description","range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"expectedUnitsPerYear":6.027456183070403,"type":"COMPENSATION_TYPE_UNSPECIFIED"}],"annualizedBaseCompensationRange":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"annualizedTotalCompensationRange":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}},"jobStartTime":"jobStartTime","requisitionId":"requisitionId","qualifications":"qualifications","incentives":"incentives","responsibilities":"responsibilities","company":"company","department":"department","visibility":"VISIBILITY_UNSPECIFIED","postingExpireTime":"postingExpireTime","degreeTypes":["DEGREE_TYPE_UNSPECIFIED","DEGREE_TYPE_UNSPECIFIED"],"postingRegion":"POSTING_REGION_UNSPECIFIED","derivedInfo":{"jobCategories":["JOB_CATEGORY_UNSPECIFIED","JOB_CATEGORY_UNSPECIFIED"],"locations":[{"postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":5},"locationType":"LOCATION_TYPE_UNSPECIFIED","radiusMiles":2.3021358869347655,"latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}},{"postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":5},"locationType":"LOCATION_TYPE_UNSPECIFIED","radiusMiles":2.3021358869347655,"latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}}]},"postingPublishTime":"postingPublishTime","languageCode":"languageCode","jobLevel":"JOB_LEVEL_UNSPECIFIED","postingCreateTime":"postingCreateTime","name":"name","employmentTypes":["EMPLOYMENT_TYPE_UNSPECIFIED","EMPLOYMENT_TYPE_UNSPECIFIED"],"applicationInfo":{"emails":["emails","emails"],"uris":["uris","uris"],"instruction":"instruction"},"postingUpdateTime":"postingUpdateTime","companyDisplayName":"companyDisplayName","promotionValue":7,"customAttributes":{"key":{"filterable":True,"keywordSearchable":True,"stringValues":["stringValues","stringValues"],"longValues":["longValues","longValues"]}},"jobEndTime":"jobEndTime"},{"addresses":["addresses","addresses"],"processingOptions":{"htmlSanitization":"HTML_SANITIZATION_UNSPECIFIED","disableStreetAddressResolution":True},"description":"description","jobBenefits":["JOB_BENEFIT_UNSPECIFIED","JOB_BENEFIT_UNSPECIFIED"],"title":"title","compensationInfo":{"entries":[{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"unit":"COMPENSATION_UNIT_UNSPECIFIED","description":"description","range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"expectedUnitsPerYear":6.027456183070403,"type":"COMPENSATION_TYPE_UNSPECIFIED"},{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"unit":"COMPENSATION_UNIT_UNSPECIFIED","description":"description","range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"expectedUnitsPerYear":6.027456183070403,"type":"COMPENSATION_TYPE_UNSPECIFIED"}],"annualizedBaseCompensationRange":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"annualizedTotalCompensationRange":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}},"jobStartTime":"jobStartTime","requisitionId":"requisitionId","qualifications":"qualifications","incentives":"incentives","responsibilities":"responsibilities","company":"company","department":"department","visibility":"VISIBILITY_UNSPECIFIED","postingExpireTime":"postingExpireTime","degreeTypes":["DEGREE_TYPE_UNSPECIFIED","DEGREE_TYPE_UNSPECIFIED"],"postingRegion":"POSTING_REGION_UNSPECIFIED","derivedInfo":{"jobCategories":["JOB_CATEGORY_UNSPECIFIED","JOB_CATEGORY_UNSPECIFIED"],"locations":[{"postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":5},"locationType":"LOCATION_TYPE_UNSPECIFIED","radiusMiles":2.3021358869347655,"latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}},{"postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":5},"locationType":"LOCATION_TYPE_UNSPECIFIED","radiusMiles":2.3021358869347655,"latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}}]},"postingPublishTime":"postingPublishTime","languageCode":"languageCode","jobLevel":"JOB_LEVEL_UNSPECIFIED","postingCreateTime":"postingCreateTime","name":"name","employmentTypes":["EMPLOYMENT_TYPE_UNSPECIFIED","EMPLOYMENT_TYPE_UNSPECIFIED"],"applicationInfo":{"emails":["emails","emails"],"uris":["uris","uris"],"instruction":"instruction"},"postingUpdateTime":"postingUpdateTime","companyDisplayName":"companyDisplayName","promotionValue":7,"customAttributes":{"key":{"filterable":True,"keywordSearchable":True,"stringValues":["stringValues","stringValues"],"longValues":["longValues","longValues"]}},"jobEndTime":"jobEndTime"}]}
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
        path='/v4/{parent}/jobs:batchCreate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_tenants_jobs_batch_delete(client):
    """Test case for jobs_projects_tenants_jobs_batch_delete

    
    """
    body = {"names":["names","names"]}
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
        path='/v4/{parent}/jobs:batchDelete'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_tenants_jobs_batch_update(client):
    """Test case for jobs_projects_tenants_jobs_batch_update

    
    """
    body = {"jobs":[{"addresses":["addresses","addresses"],"processingOptions":{"htmlSanitization":"HTML_SANITIZATION_UNSPECIFIED","disableStreetAddressResolution":True},"description":"description","jobBenefits":["JOB_BENEFIT_UNSPECIFIED","JOB_BENEFIT_UNSPECIFIED"],"title":"title","compensationInfo":{"entries":[{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"unit":"COMPENSATION_UNIT_UNSPECIFIED","description":"description","range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"expectedUnitsPerYear":6.027456183070403,"type":"COMPENSATION_TYPE_UNSPECIFIED"},{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"unit":"COMPENSATION_UNIT_UNSPECIFIED","description":"description","range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"expectedUnitsPerYear":6.027456183070403,"type":"COMPENSATION_TYPE_UNSPECIFIED"}],"annualizedBaseCompensationRange":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"annualizedTotalCompensationRange":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}},"jobStartTime":"jobStartTime","requisitionId":"requisitionId","qualifications":"qualifications","incentives":"incentives","responsibilities":"responsibilities","company":"company","department":"department","visibility":"VISIBILITY_UNSPECIFIED","postingExpireTime":"postingExpireTime","degreeTypes":["DEGREE_TYPE_UNSPECIFIED","DEGREE_TYPE_UNSPECIFIED"],"postingRegion":"POSTING_REGION_UNSPECIFIED","derivedInfo":{"jobCategories":["JOB_CATEGORY_UNSPECIFIED","JOB_CATEGORY_UNSPECIFIED"],"locations":[{"postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":5},"locationType":"LOCATION_TYPE_UNSPECIFIED","radiusMiles":2.3021358869347655,"latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}},{"postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":5},"locationType":"LOCATION_TYPE_UNSPECIFIED","radiusMiles":2.3021358869347655,"latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}}]},"postingPublishTime":"postingPublishTime","languageCode":"languageCode","jobLevel":"JOB_LEVEL_UNSPECIFIED","postingCreateTime":"postingCreateTime","name":"name","employmentTypes":["EMPLOYMENT_TYPE_UNSPECIFIED","EMPLOYMENT_TYPE_UNSPECIFIED"],"applicationInfo":{"emails":["emails","emails"],"uris":["uris","uris"],"instruction":"instruction"},"postingUpdateTime":"postingUpdateTime","companyDisplayName":"companyDisplayName","promotionValue":7,"customAttributes":{"key":{"filterable":True,"keywordSearchable":True,"stringValues":["stringValues","stringValues"],"longValues":["longValues","longValues"]}},"jobEndTime":"jobEndTime"},{"addresses":["addresses","addresses"],"processingOptions":{"htmlSanitization":"HTML_SANITIZATION_UNSPECIFIED","disableStreetAddressResolution":True},"description":"description","jobBenefits":["JOB_BENEFIT_UNSPECIFIED","JOB_BENEFIT_UNSPECIFIED"],"title":"title","compensationInfo":{"entries":[{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"unit":"COMPENSATION_UNIT_UNSPECIFIED","description":"description","range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"expectedUnitsPerYear":6.027456183070403,"type":"COMPENSATION_TYPE_UNSPECIFIED"},{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"unit":"COMPENSATION_UNIT_UNSPECIFIED","description":"description","range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"expectedUnitsPerYear":6.027456183070403,"type":"COMPENSATION_TYPE_UNSPECIFIED"}],"annualizedBaseCompensationRange":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"annualizedTotalCompensationRange":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}},"jobStartTime":"jobStartTime","requisitionId":"requisitionId","qualifications":"qualifications","incentives":"incentives","responsibilities":"responsibilities","company":"company","department":"department","visibility":"VISIBILITY_UNSPECIFIED","postingExpireTime":"postingExpireTime","degreeTypes":["DEGREE_TYPE_UNSPECIFIED","DEGREE_TYPE_UNSPECIFIED"],"postingRegion":"POSTING_REGION_UNSPECIFIED","derivedInfo":{"jobCategories":["JOB_CATEGORY_UNSPECIFIED","JOB_CATEGORY_UNSPECIFIED"],"locations":[{"postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":5},"locationType":"LOCATION_TYPE_UNSPECIFIED","radiusMiles":2.3021358869347655,"latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}},{"postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":5},"locationType":"LOCATION_TYPE_UNSPECIFIED","radiusMiles":2.3021358869347655,"latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}}]},"postingPublishTime":"postingPublishTime","languageCode":"languageCode","jobLevel":"JOB_LEVEL_UNSPECIFIED","postingCreateTime":"postingCreateTime","name":"name","employmentTypes":["EMPLOYMENT_TYPE_UNSPECIFIED","EMPLOYMENT_TYPE_UNSPECIFIED"],"applicationInfo":{"emails":["emails","emails"],"uris":["uris","uris"],"instruction":"instruction"},"postingUpdateTime":"postingUpdateTime","companyDisplayName":"companyDisplayName","promotionValue":7,"customAttributes":{"key":{"filterable":True,"keywordSearchable":True,"stringValues":["stringValues","stringValues"],"longValues":["longValues","longValues"]}},"jobEndTime":"jobEndTime"}],"updateMask":"updateMask"}
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
        path='/v4/{parent}/jobs:batchUpdate'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_tenants_jobs_create(client):
    """Test case for jobs_projects_tenants_jobs_create

    
    """
    body = {"addresses":["addresses","addresses"],"processingOptions":{"htmlSanitization":"HTML_SANITIZATION_UNSPECIFIED","disableStreetAddressResolution":True},"description":"description","jobBenefits":["JOB_BENEFIT_UNSPECIFIED","JOB_BENEFIT_UNSPECIFIED"],"title":"title","compensationInfo":{"entries":[{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"unit":"COMPENSATION_UNIT_UNSPECIFIED","description":"description","range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"expectedUnitsPerYear":6.027456183070403,"type":"COMPENSATION_TYPE_UNSPECIFIED"},{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"unit":"COMPENSATION_UNIT_UNSPECIFIED","description":"description","range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"expectedUnitsPerYear":6.027456183070403,"type":"COMPENSATION_TYPE_UNSPECIFIED"}],"annualizedBaseCompensationRange":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"annualizedTotalCompensationRange":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}},"jobStartTime":"jobStartTime","requisitionId":"requisitionId","qualifications":"qualifications","incentives":"incentives","responsibilities":"responsibilities","company":"company","department":"department","visibility":"VISIBILITY_UNSPECIFIED","postingExpireTime":"postingExpireTime","degreeTypes":["DEGREE_TYPE_UNSPECIFIED","DEGREE_TYPE_UNSPECIFIED"],"postingRegion":"POSTING_REGION_UNSPECIFIED","derivedInfo":{"jobCategories":["JOB_CATEGORY_UNSPECIFIED","JOB_CATEGORY_UNSPECIFIED"],"locations":[{"postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":5},"locationType":"LOCATION_TYPE_UNSPECIFIED","radiusMiles":2.3021358869347655,"latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}},{"postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":5},"locationType":"LOCATION_TYPE_UNSPECIFIED","radiusMiles":2.3021358869347655,"latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}}]},"postingPublishTime":"postingPublishTime","languageCode":"languageCode","jobLevel":"JOB_LEVEL_UNSPECIFIED","postingCreateTime":"postingCreateTime","name":"name","employmentTypes":["EMPLOYMENT_TYPE_UNSPECIFIED","EMPLOYMENT_TYPE_UNSPECIFIED"],"applicationInfo":{"emails":["emails","emails"],"uris":["uris","uris"],"instruction":"instruction"},"postingUpdateTime":"postingUpdateTime","companyDisplayName":"companyDisplayName","promotionValue":7,"customAttributes":{"key":{"filterable":True,"keywordSearchable":True,"stringValues":["stringValues","stringValues"],"longValues":["longValues","longValues"]}},"jobEndTime":"jobEndTime"}
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
        path='/v4/{parent}/jobs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_tenants_jobs_delete(client):
    """Test case for jobs_projects_tenants_jobs_delete

    
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
        method='DELETE',
        path='/v4/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_tenants_jobs_get(client):
    """Test case for jobs_projects_tenants_jobs_get

    
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
        path='/v4/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_tenants_jobs_list(client):
    """Test case for jobs_projects_tenants_jobs_list

    
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
                    ('jobView', 'job_view_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v4/{parent}/jobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_tenants_jobs_patch(client):
    """Test case for jobs_projects_tenants_jobs_patch

    
    """
    body = {"addresses":["addresses","addresses"],"processingOptions":{"htmlSanitization":"HTML_SANITIZATION_UNSPECIFIED","disableStreetAddressResolution":True},"description":"description","jobBenefits":["JOB_BENEFIT_UNSPECIFIED","JOB_BENEFIT_UNSPECIFIED"],"title":"title","compensationInfo":{"entries":[{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"unit":"COMPENSATION_UNIT_UNSPECIFIED","description":"description","range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"expectedUnitsPerYear":6.027456183070403,"type":"COMPENSATION_TYPE_UNSPECIFIED"},{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"unit":"COMPENSATION_UNIT_UNSPECIFIED","description":"description","range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"expectedUnitsPerYear":6.027456183070403,"type":"COMPENSATION_TYPE_UNSPECIFIED"}],"annualizedBaseCompensationRange":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"annualizedTotalCompensationRange":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}},"jobStartTime":"jobStartTime","requisitionId":"requisitionId","qualifications":"qualifications","incentives":"incentives","responsibilities":"responsibilities","company":"company","department":"department","visibility":"VISIBILITY_UNSPECIFIED","postingExpireTime":"postingExpireTime","degreeTypes":["DEGREE_TYPE_UNSPECIFIED","DEGREE_TYPE_UNSPECIFIED"],"postingRegion":"POSTING_REGION_UNSPECIFIED","derivedInfo":{"jobCategories":["JOB_CATEGORY_UNSPECIFIED","JOB_CATEGORY_UNSPECIFIED"],"locations":[{"postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":5},"locationType":"LOCATION_TYPE_UNSPECIFIED","radiusMiles":2.3021358869347655,"latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}},{"postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":5},"locationType":"LOCATION_TYPE_UNSPECIFIED","radiusMiles":2.3021358869347655,"latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}}]},"postingPublishTime":"postingPublishTime","languageCode":"languageCode","jobLevel":"JOB_LEVEL_UNSPECIFIED","postingCreateTime":"postingCreateTime","name":"name","employmentTypes":["EMPLOYMENT_TYPE_UNSPECIFIED","EMPLOYMENT_TYPE_UNSPECIFIED"],"applicationInfo":{"emails":["emails","emails"],"uris":["uris","uris"],"instruction":"instruction"},"postingUpdateTime":"postingUpdateTime","companyDisplayName":"companyDisplayName","promotionValue":7,"customAttributes":{"key":{"filterable":True,"keywordSearchable":True,"stringValues":["stringValues","stringValues"],"longValues":["longValues","longValues"]}},"jobEndTime":"jobEndTime"}
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v4/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_tenants_jobs_search(client):
    """Test case for jobs_projects_tenants_jobs_search

    
    """
    body = {"requestMetadata":{"allowMissingIds":True,"domain":"domain","sessionId":"sessionId","userId":"userId","deviceInfo":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","id":"id"}},"keywordMatchMode":"KEYWORD_MATCH_MODE_UNSPECIFIED","offset":7,"maxPageSize":2,"searchMode":"SEARCH_MODE_UNSPECIFIED","orderBy":"orderBy","diversificationLevel":"DIVERSIFICATION_LEVEL_UNSPECIFIED","jobView":"JOB_VIEW_UNSPECIFIED","histogramQueries":[{"histogramQuery":"histogramQuery"},{"histogramQuery":"histogramQuery"}],"customRankingInfo":{"importanceLevel":"IMPORTANCE_LEVEL_UNSPECIFIED","rankingExpression":"rankingExpression"},"disableKeywordMatch":True,"enableBroadening":True,"pageToken":"pageToken","jobQuery":{"companyDisplayNames":["companyDisplayNames","companyDisplayNames"],"excludedJobs":["excludedJobs","excludedJobs"],"query":"query","disableSpellCheck":True,"locationFilters":[{"distanceInMiles":5.637376656633329,"regionCode":"regionCode","address":"address","telecommutePreference":"TELECOMMUTE_PREFERENCE_UNSPECIFIED","latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}},{"distanceInMiles":5.637376656633329,"regionCode":"regionCode","address":"address","telecommutePreference":"TELECOMMUTE_PREFERENCE_UNSPECIFIED","latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}}],"languageCodes":["languageCodes","languageCodes"],"queryLanguageCode":"queryLanguageCode","companies":["companies","companies"],"customAttributeFilter":"customAttributeFilter","jobCategories":["JOB_CATEGORY_UNSPECIFIED","JOB_CATEGORY_UNSPECIFIED"],"compensationFilter":{"range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"includeJobsWithUnspecifiedCompensationRange":True,"units":["COMPENSATION_UNIT_UNSPECIFIED","COMPENSATION_UNIT_UNSPECIFIED"],"type":"FILTER_TYPE_UNSPECIFIED"},"publishTimeRange":{"startTime":"startTime","endTime":"endTime"},"commuteFilter":{"departureTime":{"hours":0,"seconds":5,"nanos":1,"minutes":6},"roadTraffic":"ROAD_TRAFFIC_UNSPECIFIED","allowImpreciseAddresses":True,"travelDuration":"travelDuration","startCoordinates":{"latitude":1.4658129805029452,"longitude":5.962133916683182},"commuteMethod":"COMMUTE_METHOD_UNSPECIFIED"},"employmentTypes":["EMPLOYMENT_TYPE_UNSPECIFIED","EMPLOYMENT_TYPE_UNSPECIFIED"]}}
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
        path='/v4/{parent}/jobs:search'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_tenants_jobs_search_for_alert(client):
    """Test case for jobs_projects_tenants_jobs_search_for_alert

    
    """
    body = {"requestMetadata":{"allowMissingIds":True,"domain":"domain","sessionId":"sessionId","userId":"userId","deviceInfo":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","id":"id"}},"keywordMatchMode":"KEYWORD_MATCH_MODE_UNSPECIFIED","offset":7,"maxPageSize":2,"searchMode":"SEARCH_MODE_UNSPECIFIED","orderBy":"orderBy","diversificationLevel":"DIVERSIFICATION_LEVEL_UNSPECIFIED","jobView":"JOB_VIEW_UNSPECIFIED","histogramQueries":[{"histogramQuery":"histogramQuery"},{"histogramQuery":"histogramQuery"}],"customRankingInfo":{"importanceLevel":"IMPORTANCE_LEVEL_UNSPECIFIED","rankingExpression":"rankingExpression"},"disableKeywordMatch":True,"enableBroadening":True,"pageToken":"pageToken","jobQuery":{"companyDisplayNames":["companyDisplayNames","companyDisplayNames"],"excludedJobs":["excludedJobs","excludedJobs"],"query":"query","disableSpellCheck":True,"locationFilters":[{"distanceInMiles":5.637376656633329,"regionCode":"regionCode","address":"address","telecommutePreference":"TELECOMMUTE_PREFERENCE_UNSPECIFIED","latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}},{"distanceInMiles":5.637376656633329,"regionCode":"regionCode","address":"address","telecommutePreference":"TELECOMMUTE_PREFERENCE_UNSPECIFIED","latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}}],"languageCodes":["languageCodes","languageCodes"],"queryLanguageCode":"queryLanguageCode","companies":["companies","companies"],"customAttributeFilter":"customAttributeFilter","jobCategories":["JOB_CATEGORY_UNSPECIFIED","JOB_CATEGORY_UNSPECIFIED"],"compensationFilter":{"range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"includeJobsWithUnspecifiedCompensationRange":True,"units":["COMPENSATION_UNIT_UNSPECIFIED","COMPENSATION_UNIT_UNSPECIFIED"],"type":"FILTER_TYPE_UNSPECIFIED"},"publishTimeRange":{"startTime":"startTime","endTime":"endTime"},"commuteFilter":{"departureTime":{"hours":0,"seconds":5,"nanos":1,"minutes":6},"roadTraffic":"ROAD_TRAFFIC_UNSPECIFIED","allowImpreciseAddresses":True,"travelDuration":"travelDuration","startCoordinates":{"latitude":1.4658129805029452,"longitude":5.962133916683182},"commuteMethod":"COMMUTE_METHOD_UNSPECIFIED"},"employmentTypes":["EMPLOYMENT_TYPE_UNSPECIFIED","EMPLOYMENT_TYPE_UNSPECIFIED"]}}
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
        path='/v4/{parent}/jobs:searchForAlert'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_tenants_list(client):
    """Test case for jobs_projects_tenants_list

    
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
        path='/v4/{parent}/tenants'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

