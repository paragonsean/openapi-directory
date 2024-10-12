# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_delete_jobs_request import BatchDeleteJobsRequest
from openapi_server.models.client_event import ClientEvent
from openapi_server.models.company import Company
from openapi_server.models.complete_query_response import CompleteQueryResponse
from openapi_server.models.create_client_event_request import CreateClientEventRequest
from openapi_server.models.create_company_request import CreateCompanyRequest
from openapi_server.models.create_job_request import CreateJobRequest
from openapi_server.models.job import Job
from openapi_server.models.list_companies_response import ListCompaniesResponse
from openapi_server.models.list_jobs_response import ListJobsResponse
from openapi_server.models.operation import Operation
from openapi_server.models.search_jobs_request import SearchJobsRequest
from openapi_server.models.search_jobs_response import SearchJobsResponse
from openapi_server.models.update_job_request import UpdateJobRequest


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_client_events_create(client):
    """Test case for jobs_projects_client_events_create

    
    """
    body = {"clientEvent":{"eventId":"eventId","jobEvent":{"jobs":["jobs","jobs"],"type":"JOB_EVENT_TYPE_UNSPECIFIED"},"createTime":"createTime","requestId":"requestId","parentEventId":"parentEventId","extraInfo":{"key":"extraInfo"}}}
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
        path='/v3p1beta1/{parent}/clientEvents'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_companies_create(client):
    """Test case for jobs_projects_companies_create

    
    """
    body = {"company":{"displayName":"displayName","keywordSearchableJobCustomAttributes":["keywordSearchableJobCustomAttributes","keywordSearchableJobCustomAttributes"],"externalId":"externalId","derivedInfo":{"headquartersLocation":{"radiusInMiles":2.3021358869347655,"postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":5},"locationType":"LOCATION_TYPE_UNSPECIFIED","latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}}},"headquartersAddress":"headquartersAddress","eeoText":"eeoText","suspended":True,"websiteUri":"websiteUri","careerSiteUri":"careerSiteUri","hiringAgency":True,"imageUri":"imageUri","size":"COMPANY_SIZE_UNSPECIFIED","name":"name"}}
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
        path='/v3p1beta1/{parent}/companies'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_companies_list(client):
    """Test case for jobs_projects_companies_list

    
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
        path='/v3p1beta1/{parent}/companies'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_complete(client):
    """Test case for jobs_projects_complete

    
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
                    ('companyName', 'company_name_example'),
                    ('languageCode', 'language_code_example'),
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
        path='/v3p1beta1/{namecomplet}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_jobs_batch_delete(client):
    """Test case for jobs_projects_jobs_batch_delete

    
    """
    body = {"filter":"filter"}
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
        path='/v3p1beta1/{parent}/jobs:batchDelete'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_jobs_create(client):
    """Test case for jobs_projects_jobs_create

    
    """
    body = {"job":{"addresses":["addresses","addresses"],"processingOptions":{"htmlSanitization":"HTML_SANITIZATION_UNSPECIFIED","disableStreetAddressResolution":True},"companyName":"companyName","description":"description","jobBenefits":["JOB_BENEFIT_UNSPECIFIED","JOB_BENEFIT_UNSPECIFIED"],"title":"title","compensationInfo":{"entries":[{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"unit":"COMPENSATION_UNIT_UNSPECIFIED","description":"description","range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"expectedUnitsPerYear":6.027456183070403,"type":"COMPENSATION_TYPE_UNSPECIFIED"},{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"unit":"COMPENSATION_UNIT_UNSPECIFIED","description":"description","range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"expectedUnitsPerYear":6.027456183070403,"type":"COMPENSATION_TYPE_UNSPECIFIED"}],"annualizedBaseCompensationRange":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"annualizedTotalCompensationRange":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}},"jobStartTime":"jobStartTime","requisitionId":"requisitionId","qualifications":"qualifications","incentives":"incentives","responsibilities":"responsibilities","department":"department","visibility":"VISIBILITY_UNSPECIFIED","postingExpireTime":"postingExpireTime","degreeTypes":["DEGREE_TYPE_UNSPECIFIED","DEGREE_TYPE_UNSPECIFIED"],"postingRegion":"POSTING_REGION_UNSPECIFIED","derivedInfo":{"jobCategories":["JOB_CATEGORY_UNSPECIFIED","JOB_CATEGORY_UNSPECIFIED"],"locations":[{"radiusInMiles":2.3021358869347655,"postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":5},"locationType":"LOCATION_TYPE_UNSPECIFIED","latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}},{"radiusInMiles":2.3021358869347655,"postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":5},"locationType":"LOCATION_TYPE_UNSPECIFIED","latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}}]},"postingPublishTime":"postingPublishTime","languageCode":"languageCode","jobLevel":"JOB_LEVEL_UNSPECIFIED","postingCreateTime":"postingCreateTime","name":"name","employmentTypes":["EMPLOYMENT_TYPE_UNSPECIFIED","EMPLOYMENT_TYPE_UNSPECIFIED"],"applicationInfo":{"emails":["emails","emails"],"uris":["uris","uris"],"instruction":"instruction"},"postingUpdateTime":"postingUpdateTime","companyDisplayName":"companyDisplayName","promotionValue":7,"customAttributes":{"key":{"filterable":True,"stringValues":["stringValues","stringValues"],"longValues":["longValues","longValues"]}},"jobEndTime":"jobEndTime"}}
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
        path='/v3p1beta1/{parent}/jobs'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_jobs_delete(client):
    """Test case for jobs_projects_jobs_delete

    
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
        path='/v3p1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_jobs_list(client):
    """Test case for jobs_projects_jobs_list

    
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
        path='/v3p1beta1/{parent}/jobs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_jobs_patch(client):
    """Test case for jobs_projects_jobs_patch

    
    """
    body = {"job":{"addresses":["addresses","addresses"],"processingOptions":{"htmlSanitization":"HTML_SANITIZATION_UNSPECIFIED","disableStreetAddressResolution":True},"companyName":"companyName","description":"description","jobBenefits":["JOB_BENEFIT_UNSPECIFIED","JOB_BENEFIT_UNSPECIFIED"],"title":"title","compensationInfo":{"entries":[{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"unit":"COMPENSATION_UNIT_UNSPECIFIED","description":"description","range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"expectedUnitsPerYear":6.027456183070403,"type":"COMPENSATION_TYPE_UNSPECIFIED"},{"amount":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"unit":"COMPENSATION_UNIT_UNSPECIFIED","description":"description","range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"expectedUnitsPerYear":6.027456183070403,"type":"COMPENSATION_TYPE_UNSPECIFIED"}],"annualizedBaseCompensationRange":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"annualizedTotalCompensationRange":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}}},"jobStartTime":"jobStartTime","requisitionId":"requisitionId","qualifications":"qualifications","incentives":"incentives","responsibilities":"responsibilities","department":"department","visibility":"VISIBILITY_UNSPECIFIED","postingExpireTime":"postingExpireTime","degreeTypes":["DEGREE_TYPE_UNSPECIFIED","DEGREE_TYPE_UNSPECIFIED"],"postingRegion":"POSTING_REGION_UNSPECIFIED","derivedInfo":{"jobCategories":["JOB_CATEGORY_UNSPECIFIED","JOB_CATEGORY_UNSPECIFIED"],"locations":[{"radiusInMiles":2.3021358869347655,"postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":5},"locationType":"LOCATION_TYPE_UNSPECIFIED","latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}},{"radiusInMiles":2.3021358869347655,"postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":5},"locationType":"LOCATION_TYPE_UNSPECIFIED","latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}}]},"postingPublishTime":"postingPublishTime","languageCode":"languageCode","jobLevel":"JOB_LEVEL_UNSPECIFIED","postingCreateTime":"postingCreateTime","name":"name","employmentTypes":["EMPLOYMENT_TYPE_UNSPECIFIED","EMPLOYMENT_TYPE_UNSPECIFIED"],"applicationInfo":{"emails":["emails","emails"],"uris":["uris","uris"],"instruction":"instruction"},"postingUpdateTime":"postingUpdateTime","companyDisplayName":"companyDisplayName","promotionValue":7,"customAttributes":{"key":{"filterable":True,"stringValues":["stringValues","stringValues"],"longValues":["longValues","longValues"]}},"jobEndTime":"jobEndTime"},"updateMask":"updateMask"}
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
        method='PATCH',
        path='/v3p1beta1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_jobs_search(client):
    """Test case for jobs_projects_jobs_search

    
    """
    body = {"requestMetadata":{"domain":"domain","sessionId":"sessionId","userId":"userId","deviceInfo":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","id":"id"}},"offset":7,"searchMode":"SEARCH_MODE_UNSPECIFIED","orderBy":"orderBy","pageSize":9,"diversificationLevel":"DIVERSIFICATION_LEVEL_UNSPECIFIED","jobView":"JOB_VIEW_UNSPECIFIED","histogramQueries":[{"histogramQuery":"histogramQuery"},{"histogramQuery":"histogramQuery"}],"requirePreciseResultSize":True,"histogramFacets":{"customAttributeHistogramFacets":[{"longValueHistogramBucketingOption":{"requiresMinMax":True,"bucketBounds":[0.8008281904610115,0.8008281904610115]},"stringValueHistogram":True,"key":"key"},{"longValueHistogramBucketingOption":{"requiresMinMax":True,"bucketBounds":[0.8008281904610115,0.8008281904610115]},"stringValueHistogram":True,"key":"key"}],"compensationHistogramFacets":[{"bucketingOption":{"requiresMinMax":True,"bucketBounds":[0.8008281904610115,0.8008281904610115]},"type":"COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED"},{"bucketingOption":{"requiresMinMax":True,"bucketBounds":[0.8008281904610115,0.8008281904610115]},"type":"COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED"}],"simpleHistogramFacets":["SEARCH_TYPE_UNSPECIFIED","SEARCH_TYPE_UNSPECIFIED"]},"customRankingInfo":{"importanceLevel":"IMPORTANCE_LEVEL_UNSPECIFIED","rankingExpression":"rankingExpression"},"disableKeywordMatch":True,"enableBroadening":True,"pageToken":"pageToken","jobQuery":{"companyDisplayNames":["companyDisplayNames","companyDisplayNames"],"excludedJobs":["excludedJobs","excludedJobs"],"query":"query","disableSpellCheck":True,"locationFilters":[{"distanceInMiles":2.3021358869347655,"regionCode":"regionCode","address":"address","telecommutePreference":"TELECOMMUTE_PREFERENCE_UNSPECIFIED","latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}},{"distanceInMiles":2.3021358869347655,"regionCode":"regionCode","address":"address","telecommutePreference":"TELECOMMUTE_PREFERENCE_UNSPECIFIED","latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}}],"companyNames":["companyNames","companyNames"],"languageCodes":["languageCodes","languageCodes"],"queryLanguageCode":"queryLanguageCode","customAttributeFilter":"customAttributeFilter","jobCategories":["JOB_CATEGORY_UNSPECIFIED","JOB_CATEGORY_UNSPECIFIED"],"compensationFilter":{"range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"includeJobsWithUnspecifiedCompensationRange":True,"units":["COMPENSATION_UNIT_UNSPECIFIED","COMPENSATION_UNIT_UNSPECIFIED"],"type":"FILTER_TYPE_UNSPECIFIED"},"publishTimeRange":{"startTime":"startTime","endTime":"endTime"},"commuteFilter":{"departureTime":{"hours":6,"seconds":5,"nanos":5,"minutes":1},"roadTraffic":"ROAD_TRAFFIC_UNSPECIFIED","allowImpreciseAddresses":True,"travelDuration":"travelDuration","startCoordinates":{"latitude":1.4658129805029452,"longitude":5.962133916683182},"commuteMethod":"COMMUTE_METHOD_UNSPECIFIED"},"employmentTypes":["EMPLOYMENT_TYPE_UNSPECIFIED","EMPLOYMENT_TYPE_UNSPECIFIED"]}}
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
        path='/v3p1beta1/{parent}/jobs:search'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_jobs_search_for_alert(client):
    """Test case for jobs_projects_jobs_search_for_alert

    
    """
    body = {"requestMetadata":{"domain":"domain","sessionId":"sessionId","userId":"userId","deviceInfo":{"deviceType":"DEVICE_TYPE_UNSPECIFIED","id":"id"}},"offset":7,"searchMode":"SEARCH_MODE_UNSPECIFIED","orderBy":"orderBy","pageSize":9,"diversificationLevel":"DIVERSIFICATION_LEVEL_UNSPECIFIED","jobView":"JOB_VIEW_UNSPECIFIED","histogramQueries":[{"histogramQuery":"histogramQuery"},{"histogramQuery":"histogramQuery"}],"requirePreciseResultSize":True,"histogramFacets":{"customAttributeHistogramFacets":[{"longValueHistogramBucketingOption":{"requiresMinMax":True,"bucketBounds":[0.8008281904610115,0.8008281904610115]},"stringValueHistogram":True,"key":"key"},{"longValueHistogramBucketingOption":{"requiresMinMax":True,"bucketBounds":[0.8008281904610115,0.8008281904610115]},"stringValueHistogram":True,"key":"key"}],"compensationHistogramFacets":[{"bucketingOption":{"requiresMinMax":True,"bucketBounds":[0.8008281904610115,0.8008281904610115]},"type":"COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED"},{"bucketingOption":{"requiresMinMax":True,"bucketBounds":[0.8008281904610115,0.8008281904610115]},"type":"COMPENSATION_HISTOGRAM_REQUEST_TYPE_UNSPECIFIED"}],"simpleHistogramFacets":["SEARCH_TYPE_UNSPECIFIED","SEARCH_TYPE_UNSPECIFIED"]},"customRankingInfo":{"importanceLevel":"IMPORTANCE_LEVEL_UNSPECIFIED","rankingExpression":"rankingExpression"},"disableKeywordMatch":True,"enableBroadening":True,"pageToken":"pageToken","jobQuery":{"companyDisplayNames":["companyDisplayNames","companyDisplayNames"],"excludedJobs":["excludedJobs","excludedJobs"],"query":"query","disableSpellCheck":True,"locationFilters":[{"distanceInMiles":2.3021358869347655,"regionCode":"regionCode","address":"address","telecommutePreference":"TELECOMMUTE_PREFERENCE_UNSPECIFIED","latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}},{"distanceInMiles":2.3021358869347655,"regionCode":"regionCode","address":"address","telecommutePreference":"TELECOMMUTE_PREFERENCE_UNSPECIFIED","latLng":{"latitude":1.4658129805029452,"longitude":5.962133916683182}}],"companyNames":["companyNames","companyNames"],"languageCodes":["languageCodes","languageCodes"],"queryLanguageCode":"queryLanguageCode","customAttributeFilter":"customAttributeFilter","jobCategories":["JOB_CATEGORY_UNSPECIFIED","JOB_CATEGORY_UNSPECIFIED"],"compensationFilter":{"range":{"minCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"},"maxCompensation":{"nanos":0,"units":"units","currencyCode":"currencyCode"}},"includeJobsWithUnspecifiedCompensationRange":True,"units":["COMPENSATION_UNIT_UNSPECIFIED","COMPENSATION_UNIT_UNSPECIFIED"],"type":"FILTER_TYPE_UNSPECIFIED"},"publishTimeRange":{"startTime":"startTime","endTime":"endTime"},"commuteFilter":{"departureTime":{"hours":6,"seconds":5,"nanos":5,"minutes":1},"roadTraffic":"ROAD_TRAFFIC_UNSPECIFIED","allowImpreciseAddresses":True,"travelDuration":"travelDuration","startCoordinates":{"latitude":1.4658129805029452,"longitude":5.962133916683182},"commuteMethod":"COMMUTE_METHOD_UNSPECIFIED"},"employmentTypes":["EMPLOYMENT_TYPE_UNSPECIFIED","EMPLOYMENT_TYPE_UNSPECIFIED"]}}
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
        path='/v3p1beta1/{parent}/jobs:searchForAlert'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jobs_projects_operations_get(client):
    """Test case for jobs_projects_operations_get

    
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
        path='/v3p1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

