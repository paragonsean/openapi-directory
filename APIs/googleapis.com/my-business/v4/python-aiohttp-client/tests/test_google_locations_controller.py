# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.report_google_location_request import ReportGoogleLocationRequest
from openapi_server.models.search_google_locations_request import SearchGoogleLocationsRequest
from openapi_server.models.search_google_locations_response import SearchGoogleLocationsResponse


pytestmark = pytest.mark.asyncio

async def test_mybusiness_google_locations_report(client):
    """Test case for mybusiness_google_locations_report

    
    """
    body = {"reportReasonLanguageCode":"reportReasonLanguageCode","reportReasonElaboration":"reportReasonElaboration","reportReasonBadRecommendation":"BAD_RECOMMENDATION_REASON_UNSPECIFIED","reportReasonBadLocation":"BAD_LOCATION_REASON_UNSPECIFIED","locationGroupName":"locationGroupName"}
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
        path='/v4/{namerepor}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_google_locations_search(client):
    """Test case for mybusiness_google_locations_search

    
    """
    body = {"resultCount":0,"query":"query","location":{"locationKey":{"explicitNoPlaceId":True,"plusPageId":"plusPageId","requestId":"requestId","placeId":"placeId"},"metadata":{"mapsUrl":"mapsUrl","duplicate":{"access":"ACCESS_UNSPECIFIED","locationName":"locationName","placeId":"placeId"},"newReviewUrl":"newReviewUrl"},"additionalPhones":["additionalPhones","additionalPhones"],"regularHours":{"periods":[{"closeDay":"DAY_OF_WEEK_UNSPECIFIED","openDay":"DAY_OF_WEEK_UNSPECIFIED","closeTime":"closeTime","openTime":"openTime"},{"closeDay":"DAY_OF_WEEK_UNSPECIFIED","openDay":"DAY_OF_WEEK_UNSPECIFIED","closeTime":"closeTime","openTime":"openTime"}]},"specialHours":{"specialHourPeriods":[{"isClosed":True,"endDate":{"month":5,"year":5,"day":1},"closeTime":"closeTime","openTime":"openTime","startDate":{"month":5,"year":5,"day":1}},{"isClosed":True,"endDate":{"month":5,"year":5,"day":1},"closeTime":"closeTime","openTime":"openTime","startDate":{"month":5,"year":5,"day":1}}]},"primaryCategory":{"moreHoursTypes":[{"displayName":"displayName","localizedDisplayName":"localizedDisplayName","hoursTypeId":"hoursTypeId"},{"displayName":"displayName","localizedDisplayName":"localizedDisplayName","hoursTypeId":"hoursTypeId"}],"displayName":"displayName","serviceTypes":[{"displayName":"displayName","serviceTypeId":"serviceTypeId"},{"displayName":"displayName","serviceTypeId":"serviceTypeId"}],"categoryId":"categoryId"},"websiteUrl":"websiteUrl","additionalCategories":[{"moreHoursTypes":[{"displayName":"displayName","localizedDisplayName":"localizedDisplayName","hoursTypeId":"hoursTypeId"},{"displayName":"displayName","localizedDisplayName":"localizedDisplayName","hoursTypeId":"hoursTypeId"}],"displayName":"displayName","serviceTypes":[{"displayName":"displayName","serviceTypeId":"serviceTypeId"},{"displayName":"displayName","serviceTypeId":"serviceTypeId"}],"categoryId":"categoryId"},{"moreHoursTypes":[{"displayName":"displayName","localizedDisplayName":"localizedDisplayName","hoursTypeId":"hoursTypeId"},{"displayName":"displayName","localizedDisplayName":"localizedDisplayName","hoursTypeId":"hoursTypeId"}],"displayName":"displayName","serviceTypes":[{"displayName":"displayName","serviceTypeId":"serviceTypeId"},{"displayName":"displayName","serviceTypeId":"serviceTypeId"}],"categoryId":"categoryId"}],"locationState":{"isPendingReview":True,"canUpdate":True,"isSuspended":True,"isVerified":True,"isPublished":True,"hasPendingVerification":True,"isDisconnected":True,"canModifyServiceList":True,"isGoogleUpdated":True,"canOperateHealthData":True,"canOperateLodgingData":True,"hasPendingEdits":True,"canDelete":True,"isDisabled":True,"isDuplicate":True,"canHaveFoodMenus":True,"isLocalPostApiDisabled":True,"needsReverification":True},"address":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":0},"locationName":"locationName","serviceArea":{"places":{"placeInfos":[{"name":"name","placeId":"placeId"},{"name":"name","placeId":"placeId"}]},"businessType":"BUSINESS_TYPE_UNSPECIFIED","radius":{"radiusKm":7.0614014,"latlng":{"latitude":0.8008281904610115,"longitude":6.027456183070403}}},"profile":{"description":"description"},"moreHours":[{"periods":[{"closeDay":"DAY_OF_WEEK_UNSPECIFIED","openDay":"DAY_OF_WEEK_UNSPECIFIED","closeTime":"closeTime","openTime":"openTime"},{"closeDay":"DAY_OF_WEEK_UNSPECIFIED","openDay":"DAY_OF_WEEK_UNSPECIFIED","closeTime":"closeTime","openTime":"openTime"}],"hoursTypeId":"hoursTypeId"},{"periods":[{"closeDay":"DAY_OF_WEEK_UNSPECIFIED","openDay":"DAY_OF_WEEK_UNSPECIFIED","closeTime":"closeTime","openTime":"openTime"},{"closeDay":"DAY_OF_WEEK_UNSPECIFIED","openDay":"DAY_OF_WEEK_UNSPECIFIED","closeTime":"closeTime","openTime":"openTime"}],"hoursTypeId":"hoursTypeId"}],"languageCode":"languageCode","relationshipData":{"parentChain":"parentChain"},"adWordsLocationExtensions":{"adPhone":"adPhone"},"labels":["labels","labels"],"primaryPhone":"primaryPhone","priceLists":[{"sourceUrl":"sourceUrl","priceListId":"priceListId","sections":[{"sectionId":"sectionId","sectionType":"SECTION_TYPE_UNSPECIFIED","items":[{"itemId":"itemId","price":{"nanos":2,"units":"units","currencyCode":"currencyCode"},"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]},{"itemId":"itemId","price":{"nanos":2,"units":"units","currencyCode":"currencyCode"},"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]}],"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]},{"sectionId":"sectionId","sectionType":"SECTION_TYPE_UNSPECIFIED","items":[{"itemId":"itemId","price":{"nanos":2,"units":"units","currencyCode":"currencyCode"},"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]},{"itemId":"itemId","price":{"nanos":2,"units":"units","currencyCode":"currencyCode"},"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]}],"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]}],"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]},{"sourceUrl":"sourceUrl","priceListId":"priceListId","sections":[{"sectionId":"sectionId","sectionType":"SECTION_TYPE_UNSPECIFIED","items":[{"itemId":"itemId","price":{"nanos":2,"units":"units","currencyCode":"currencyCode"},"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]},{"itemId":"itemId","price":{"nanos":2,"units":"units","currencyCode":"currencyCode"},"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]}],"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]},{"sectionId":"sectionId","sectionType":"SECTION_TYPE_UNSPECIFIED","items":[{"itemId":"itemId","price":{"nanos":2,"units":"units","currencyCode":"currencyCode"},"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]},{"itemId":"itemId","price":{"nanos":2,"units":"units","currencyCode":"currencyCode"},"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]}],"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]}],"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]}],"name":"name","attributes":[{"attributeId":"attributeId","repeatedEnumValue":{"setValues":["setValues","setValues"],"unsetValues":["unsetValues","unsetValues"]},"valueType":"ATTRIBUTE_VALUE_TYPE_UNSPECIFIED","values":["",""],"urlValues":[{"url":"url"},{"url":"url"}]},{"attributeId":"attributeId","repeatedEnumValue":{"setValues":["setValues","setValues"],"unsetValues":["unsetValues","unsetValues"]},"valueType":"ATTRIBUTE_VALUE_TYPE_UNSPECIFIED","values":["",""],"urlValues":[{"url":"url"},{"url":"url"}]}],"latlng":{"latitude":0.8008281904610115,"longitude":6.027456183070403},"openInfo":{"canReopen":True,"openingDate":{"month":5,"year":5,"day":1},"status":"OPEN_FOR_BUSINESS_UNSPECIFIED"},"storeCode":"storeCode"}}
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
        path='/v4/googleLocations:search',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

