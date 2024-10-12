# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.search_google_locations_request import SearchGoogleLocationsRequest
from openapi_server.models.search_google_locations_response import SearchGoogleLocationsResponse


pytestmark = pytest.mark.asyncio

async def test_mybusinessbusinessinformation_google_locations_search(client):
    """Test case for mybusinessbusinessinformation_google_locations_search

    
    """
    body = {"query":"query","pageSize":0,"location":{"metadata":{"canHaveBusinessCalls":True,"hasGoogleUpdated":True,"placeId":"placeId","hasVoiceOfMerchant":True,"canModifyServiceList":True,"canOperateLocalPost":True,"canOperateHealthData":True,"canOperateLodgingData":True,"hasPendingEdits":True,"mapsUri":"mapsUri","canDelete":True,"newReviewUri":"newReviewUri","canHaveFoodMenus":True,"duplicateLocation":"duplicateLocation"},"serviceArea":{"places":{"placeInfos":[{"placeId":"placeId","placeName":"placeName"},{"placeId":"placeId","placeName":"placeName"}]},"regionCode":"regionCode","businessType":"BUSINESS_TYPE_UNSPECIFIED"},"profile":{"description":"description"},"moreHours":[{"periods":[{"closeDay":"DAY_OF_WEEK_UNSPECIFIED","openDay":"DAY_OF_WEEK_UNSPECIFIED","closeTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5},"openTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5}},{"closeDay":"DAY_OF_WEEK_UNSPECIFIED","openDay":"DAY_OF_WEEK_UNSPECIFIED","closeTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5},"openTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5}}],"hoursTypeId":"hoursTypeId"},{"periods":[{"closeDay":"DAY_OF_WEEK_UNSPECIFIED","openDay":"DAY_OF_WEEK_UNSPECIFIED","closeTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5},"openTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5}},{"closeDay":"DAY_OF_WEEK_UNSPECIFIED","openDay":"DAY_OF_WEEK_UNSPECIFIED","closeTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5},"openTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5}}],"hoursTypeId":"hoursTypeId"}],"regularHours":{"periods":[{"closeDay":"DAY_OF_WEEK_UNSPECIFIED","openDay":"DAY_OF_WEEK_UNSPECIFIED","closeTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5},"openTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5}},{"closeDay":"DAY_OF_WEEK_UNSPECIFIED","openDay":"DAY_OF_WEEK_UNSPECIFIED","closeTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5},"openTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5}}]},"serviceItems":[{"structuredServiceItem":{"description":"description","serviceTypeId":"serviceTypeId"},"price":{"nanos":2,"units":"units","currencyCode":"currencyCode"},"freeFormServiceItem":{"label":{"displayName":"displayName","description":"description","languageCode":"languageCode"},"category":"category"}},{"structuredServiceItem":{"description":"description","serviceTypeId":"serviceTypeId"},"price":{"nanos":2,"units":"units","currencyCode":"currencyCode"},"freeFormServiceItem":{"label":{"displayName":"displayName","description":"description","languageCode":"languageCode"},"category":"category"}}],"languageCode":"languageCode","relationshipData":{"parentLocation":{"relationType":"RELATION_TYPE_UNSPECIFIED","placeId":"placeId"},"childrenLocations":[{"relationType":"RELATION_TYPE_UNSPECIFIED","placeId":"placeId"},{"relationType":"RELATION_TYPE_UNSPECIFIED","placeId":"placeId"}],"parentChain":"parentChain"},"specialHours":{"specialHourPeriods":[{"endDate":{"month":9,"year":3,"day":7},"closeTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5},"closed":True,"openTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5},"startDate":{"month":9,"year":3,"day":7}},{"endDate":{"month":9,"year":3,"day":7},"closeTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5},"closed":True,"openTime":{"hours":1,"seconds":2,"nanos":5,"minutes":5},"startDate":{"month":9,"year":3,"day":7}}]},"title":"title","adWordsLocationExtensions":{"adPhone":"adPhone"},"phoneNumbers":{"primaryPhone":"primaryPhone","additionalPhones":["additionalPhones","additionalPhones"]},"labels":["labels","labels"],"websiteUri":"websiteUri","name":"name","categories":{"primaryCategory":{"moreHoursTypes":[{"displayName":"displayName","localizedDisplayName":"localizedDisplayName","hoursTypeId":"hoursTypeId"},{"displayName":"displayName","localizedDisplayName":"localizedDisplayName","hoursTypeId":"hoursTypeId"}],"displayName":"displayName","name":"name","serviceTypes":[{"displayName":"displayName","serviceTypeId":"serviceTypeId"},{"displayName":"displayName","serviceTypeId":"serviceTypeId"}]},"additionalCategories":[{"moreHoursTypes":[{"displayName":"displayName","localizedDisplayName":"localizedDisplayName","hoursTypeId":"hoursTypeId"},{"displayName":"displayName","localizedDisplayName":"localizedDisplayName","hoursTypeId":"hoursTypeId"}],"displayName":"displayName","name":"name","serviceTypes":[{"displayName":"displayName","serviceTypeId":"serviceTypeId"},{"displayName":"displayName","serviceTypeId":"serviceTypeId"}]},{"moreHoursTypes":[{"displayName":"displayName","localizedDisplayName":"localizedDisplayName","hoursTypeId":"hoursTypeId"},{"displayName":"displayName","localizedDisplayName":"localizedDisplayName","hoursTypeId":"hoursTypeId"}],"displayName":"displayName","name":"name","serviceTypes":[{"displayName":"displayName","serviceTypeId":"serviceTypeId"},{"displayName":"displayName","serviceTypeId":"serviceTypeId"}]}]},"storefrontAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":4},"latlng":{"latitude":0.8008281904610115,"longitude":6.027456183070403},"openInfo":{"canReopen":True,"openingDate":{"month":9,"year":3,"day":7},"status":"OPEN_FOR_BUSINESS_UNSPECIFIED"},"storeCode":"storeCode"}}
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
        path='/v1/googleLocations:search',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

