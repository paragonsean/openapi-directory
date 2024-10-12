# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.admin import Admin
from openapi_server.models.answer import Answer
from openapi_server.models.associate_location_request import AssociateLocationRequest
from openapi_server.models.batch_get_locations_request import BatchGetLocationsRequest
from openapi_server.models.batch_get_locations_response import BatchGetLocationsResponse
from openapi_server.models.batch_get_reviews_request import BatchGetReviewsRequest
from openapi_server.models.batch_get_reviews_response import BatchGetReviewsResponse
from openapi_server.models.complete_verification_request import CompleteVerificationRequest
from openapi_server.models.complete_verification_response import CompleteVerificationResponse
from openapi_server.models.fetch_verification_options_request import FetchVerificationOptionsRequest
from openapi_server.models.fetch_verification_options_response import FetchVerificationOptionsResponse
from openapi_server.models.find_matching_locations_request import FindMatchingLocationsRequest
from openapi_server.models.find_matching_locations_response import FindMatchingLocationsResponse
from openapi_server.models.get_google_updated_lodging_response import GetGoogleUpdatedLodgingResponse
from openapi_server.models.google_updated_location import GoogleUpdatedLocation
from openapi_server.models.list_accounts_response import ListAccountsResponse
from openapi_server.models.list_answers_response import ListAnswersResponse
from openapi_server.models.list_customer_media_items_response import ListCustomerMediaItemsResponse
from openapi_server.models.list_insurance_networks_response import ListInsuranceNetworksResponse
from openapi_server.models.list_invitations_response import ListInvitationsResponse
from openapi_server.models.list_local_posts_response import ListLocalPostsResponse
from openapi_server.models.list_location_admins_response import ListLocationAdminsResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_media_items_response import ListMediaItemsResponse
from openapi_server.models.list_questions_response import ListQuestionsResponse
from openapi_server.models.list_recommended_google_locations_response import ListRecommendedGoogleLocationsResponse
from openapi_server.models.list_reviews_response import ListReviewsResponse
from openapi_server.models.list_verifications_response import ListVerificationsResponse
from openapi_server.models.local_post import LocalPost
from openapi_server.models.location import Location
from openapi_server.models.media_item import MediaItem
from openapi_server.models.media_item_data_ref import MediaItemDataRef
from openapi_server.models.notifications import Notifications
from openapi_server.models.question import Question
from openapi_server.models.report_local_post_insights_request import ReportLocalPostInsightsRequest
from openapi_server.models.report_local_post_insights_response import ReportLocalPostInsightsResponse
from openapi_server.models.report_location_insights_request import ReportLocationInsightsRequest
from openapi_server.models.report_location_insights_response import ReportLocationInsightsResponse
from openapi_server.models.review_reply import ReviewReply
from openapi_server.models.transfer_location_request import TransferLocationRequest
from openapi_server.models.upsert_answer_request import UpsertAnswerRequest
from openapi_server.models.verify_location_request import VerifyLocationRequest
from openapi_server.models.verify_location_response import VerifyLocationResponse


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_create(client):
    """Test case for mybusiness_accounts_create

    
    """
    body = {"permissionLevel":"PERMISSION_LEVEL_UNSPECIFIED","role":"ACCOUNT_ROLE_UNSPECIFIED","accountName":"accountName","organizationInfo":{"phoneNumber":"phoneNumber","postalAddress":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":0},"registeredDomain":"registeredDomain"},"name":"name","state":{"status":"ACCOUNT_STATUS_UNSPECIFIED"},"accountNumber":"accountNumber","type":"ACCOUNT_TYPE_UNSPECIFIED"}
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
                    ('primaryOwner', 'primary_owner_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v4/accounts',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_generate_account_number(client):
    """Test case for mybusiness_accounts_generate_account_number

    
    """
    body = None
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
        path='/v4/{namegenerate_account_numbe}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_invitations_accept(client):
    """Test case for mybusiness_accounts_invitations_accept

    
    """
    body = None
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
        path='/v4/{nameaccep}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_invitations_decline(client):
    """Test case for mybusiness_accounts_invitations_decline

    
    """
    body = None
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
        path='/v4/{namedeclin}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_invitations_list(client):
    """Test case for mybusiness_accounts_invitations_list

    
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
                    ('targetType', 'target_type_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v4/{parent}/invitations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_list(client):
    """Test case for mybusiness_accounts_list

    
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
                    ('name', 'name_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v4/accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_list_recommend_google_locations(client):
    """Test case for mybusiness_accounts_list_recommend_google_locations

    
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
    }
    response = await client.request(
        method='GET',
        path='/v4/{namerecommend_google_location}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_admins_create(client):
    """Test case for mybusiness_accounts_locations_admins_create

    
    """
    body = {"adminName":"adminName","pendingInvitation":True,"role":"ADMIN_ROLE_UNSPECIFIED","name":"name"}
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
        path='/v4/{parent}/admins'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_admins_list(client):
    """Test case for mybusiness_accounts_locations_admins_list

    
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
    }
    response = await client.request(
        method='GET',
        path='/v4/{parent}/admins'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_associate(client):
    """Test case for mybusiness_accounts_locations_associate

    
    """
    body = {"placeId":"placeId"}
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
        path='/v4/{nameassociat}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_batch_get(client):
    """Test case for mybusiness_accounts_locations_batch_get

    
    """
    body = {"locationNames":["locationNames","locationNames"]}
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
        path='/v4/{name}/locations:batchGet'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_batch_get_reviews(client):
    """Test case for mybusiness_accounts_locations_batch_get_reviews

    
    """
    body = {"locationNames":["locationNames","locationNames"],"ignoreRatingOnlyReviews":True,"orderBy":"orderBy","pageSize":0,"pageToken":"pageToken"}
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
        path='/v4/{name}/locations:batchGetReviews'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_clear_association(client):
    """Test case for mybusiness_accounts_locations_clear_association

    
    """
    body = None
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
        path='/v4/{nameclear_associatio}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_create(client):
    """Test case for mybusiness_accounts_locations_create

    
    """
    body = {"locationKey":{"explicitNoPlaceId":True,"plusPageId":"plusPageId","requestId":"requestId","placeId":"placeId"},"metadata":{"mapsUrl":"mapsUrl","duplicate":{"access":"ACCESS_UNSPECIFIED","locationName":"locationName","placeId":"placeId"},"newReviewUrl":"newReviewUrl"},"additionalPhones":["additionalPhones","additionalPhones"],"regularHours":{"periods":[{"closeDay":"DAY_OF_WEEK_UNSPECIFIED","openDay":"DAY_OF_WEEK_UNSPECIFIED","closeTime":"closeTime","openTime":"openTime"},{"closeDay":"DAY_OF_WEEK_UNSPECIFIED","openDay":"DAY_OF_WEEK_UNSPECIFIED","closeTime":"closeTime","openTime":"openTime"}]},"specialHours":{"specialHourPeriods":[{"isClosed":True,"endDate":{"month":5,"year":5,"day":1},"closeTime":"closeTime","openTime":"openTime","startDate":{"month":5,"year":5,"day":1}},{"isClosed":True,"endDate":{"month":5,"year":5,"day":1},"closeTime":"closeTime","openTime":"openTime","startDate":{"month":5,"year":5,"day":1}}]},"primaryCategory":{"moreHoursTypes":[{"displayName":"displayName","localizedDisplayName":"localizedDisplayName","hoursTypeId":"hoursTypeId"},{"displayName":"displayName","localizedDisplayName":"localizedDisplayName","hoursTypeId":"hoursTypeId"}],"displayName":"displayName","serviceTypes":[{"displayName":"displayName","serviceTypeId":"serviceTypeId"},{"displayName":"displayName","serviceTypeId":"serviceTypeId"}],"categoryId":"categoryId"},"websiteUrl":"websiteUrl","additionalCategories":[{"moreHoursTypes":[{"displayName":"displayName","localizedDisplayName":"localizedDisplayName","hoursTypeId":"hoursTypeId"},{"displayName":"displayName","localizedDisplayName":"localizedDisplayName","hoursTypeId":"hoursTypeId"}],"displayName":"displayName","serviceTypes":[{"displayName":"displayName","serviceTypeId":"serviceTypeId"},{"displayName":"displayName","serviceTypeId":"serviceTypeId"}],"categoryId":"categoryId"},{"moreHoursTypes":[{"displayName":"displayName","localizedDisplayName":"localizedDisplayName","hoursTypeId":"hoursTypeId"},{"displayName":"displayName","localizedDisplayName":"localizedDisplayName","hoursTypeId":"hoursTypeId"}],"displayName":"displayName","serviceTypes":[{"displayName":"displayName","serviceTypeId":"serviceTypeId"},{"displayName":"displayName","serviceTypeId":"serviceTypeId"}],"categoryId":"categoryId"}],"locationState":{"isPendingReview":True,"canUpdate":True,"isSuspended":True,"isVerified":True,"isPublished":True,"hasPendingVerification":True,"isDisconnected":True,"canModifyServiceList":True,"isGoogleUpdated":True,"canOperateHealthData":True,"canOperateLodgingData":True,"hasPendingEdits":True,"canDelete":True,"isDisabled":True,"isDuplicate":True,"canHaveFoodMenus":True,"isLocalPostApiDisabled":True,"needsReverification":True},"address":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":0},"locationName":"locationName","serviceArea":{"places":{"placeInfos":[{"name":"name","placeId":"placeId"},{"name":"name","placeId":"placeId"}]},"businessType":"BUSINESS_TYPE_UNSPECIFIED","radius":{"radiusKm":7.0614014,"latlng":{"latitude":0.8008281904610115,"longitude":6.027456183070403}}},"profile":{"description":"description"},"moreHours":[{"periods":[{"closeDay":"DAY_OF_WEEK_UNSPECIFIED","openDay":"DAY_OF_WEEK_UNSPECIFIED","closeTime":"closeTime","openTime":"openTime"},{"closeDay":"DAY_OF_WEEK_UNSPECIFIED","openDay":"DAY_OF_WEEK_UNSPECIFIED","closeTime":"closeTime","openTime":"openTime"}],"hoursTypeId":"hoursTypeId"},{"periods":[{"closeDay":"DAY_OF_WEEK_UNSPECIFIED","openDay":"DAY_OF_WEEK_UNSPECIFIED","closeTime":"closeTime","openTime":"openTime"},{"closeDay":"DAY_OF_WEEK_UNSPECIFIED","openDay":"DAY_OF_WEEK_UNSPECIFIED","closeTime":"closeTime","openTime":"openTime"}],"hoursTypeId":"hoursTypeId"}],"languageCode":"languageCode","relationshipData":{"parentChain":"parentChain"},"adWordsLocationExtensions":{"adPhone":"adPhone"},"labels":["labels","labels"],"primaryPhone":"primaryPhone","priceLists":[{"sourceUrl":"sourceUrl","priceListId":"priceListId","sections":[{"sectionId":"sectionId","sectionType":"SECTION_TYPE_UNSPECIFIED","items":[{"itemId":"itemId","price":{"nanos":2,"units":"units","currencyCode":"currencyCode"},"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]},{"itemId":"itemId","price":{"nanos":2,"units":"units","currencyCode":"currencyCode"},"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]}],"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]},{"sectionId":"sectionId","sectionType":"SECTION_TYPE_UNSPECIFIED","items":[{"itemId":"itemId","price":{"nanos":2,"units":"units","currencyCode":"currencyCode"},"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]},{"itemId":"itemId","price":{"nanos":2,"units":"units","currencyCode":"currencyCode"},"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]}],"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]}],"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]},{"sourceUrl":"sourceUrl","priceListId":"priceListId","sections":[{"sectionId":"sectionId","sectionType":"SECTION_TYPE_UNSPECIFIED","items":[{"itemId":"itemId","price":{"nanos":2,"units":"units","currencyCode":"currencyCode"},"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]},{"itemId":"itemId","price":{"nanos":2,"units":"units","currencyCode":"currencyCode"},"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]}],"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]},{"sectionId":"sectionId","sectionType":"SECTION_TYPE_UNSPECIFIED","items":[{"itemId":"itemId","price":{"nanos":2,"units":"units","currencyCode":"currencyCode"},"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]},{"itemId":"itemId","price":{"nanos":2,"units":"units","currencyCode":"currencyCode"},"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]}],"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]}],"labels":[{"displayName":"displayName","description":"description","languageCode":"languageCode"},{"displayName":"displayName","description":"description","languageCode":"languageCode"}]}],"name":"name","attributes":[{"attributeId":"attributeId","repeatedEnumValue":{"setValues":["setValues","setValues"],"unsetValues":["unsetValues","unsetValues"]},"valueType":"ATTRIBUTE_VALUE_TYPE_UNSPECIFIED","values":["",""],"urlValues":[{"url":"url"},{"url":"url"}]},{"attributeId":"attributeId","repeatedEnumValue":{"setValues":["setValues","setValues"],"unsetValues":["unsetValues","unsetValues"]},"valueType":"ATTRIBUTE_VALUE_TYPE_UNSPECIFIED","values":["",""],"urlValues":[{"url":"url"},{"url":"url"}]}],"latlng":{"latitude":0.8008281904610115,"longitude":6.027456183070403},"openInfo":{"canReopen":True,"openingDate":{"month":5,"year":5,"day":1},"status":"OPEN_FOR_BUSINESS_UNSPECIFIED"},"storeCode":"storeCode"}
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
                    ('requestId', 'request_id_example'),
                    ('validateOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v4/{parent}/locations'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_fetch_verification_options(client):
    """Test case for mybusiness_accounts_locations_fetch_verification_options

    
    """
    body = {"context":{"address":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":0}},"languageCode":"languageCode"}
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
        path='/v4/{namefetch_verification_option}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_find_matches(client):
    """Test case for mybusiness_accounts_locations_find_matches

    
    """
    body = {"maxCacheDuration":"maxCacheDuration","numResults":0,"languageCode":"languageCode"}
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
        path='/v4/{namefind_matche}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_get_google_updated(client):
    """Test case for mybusiness_accounts_locations_get_google_updated

    
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
    }
    response = await client.request(
        method='GET',
        path='/v4/{namegoogle_update}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_insurance_networks_list(client):
    """Test case for mybusiness_accounts_locations_insurance_networks_list

    
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
                    ('languageCode', 'language_code_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v4/{parent}/insuranceNetworks'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_list(client):
    """Test case for mybusiness_accounts_locations_list

    
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
                    ('languageCode', 'language_code_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v4/{parent}/locations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_local_posts_create(client):
    """Test case for mybusiness_accounts_locations_local_posts_create

    
    """
    body = {"summary":"summary","alertType":"ALERT_TYPE_UNSPECIFIED","updateTime":"updateTime","media":[{"sourceUrl":"sourceUrl","createTime":"createTime","googleUrl":"googleUrl","insights":{"viewCount":"viewCount"},"attribution":{"profileName":"profileName","profileUrl":"profileUrl","takedownUrl":"takedownUrl","profilePhotoUrl":"profilePhotoUrl"},"name":"name","description":"description","mediaFormat":"MEDIA_FORMAT_UNSPECIFIED","dataRef":{"resourceName":"resourceName"},"dimensions":{"heightPixels":0,"widthPixels":6},"locationAssociation":{"category":"CATEGORY_UNSPECIFIED","priceListItemId":"priceListItemId"},"thumbnailUrl":"thumbnailUrl"},{"sourceUrl":"sourceUrl","createTime":"createTime","googleUrl":"googleUrl","insights":{"viewCount":"viewCount"},"attribution":{"profileName":"profileName","profileUrl":"profileUrl","takedownUrl":"takedownUrl","profilePhotoUrl":"profilePhotoUrl"},"name":"name","description":"description","mediaFormat":"MEDIA_FORMAT_UNSPECIFIED","dataRef":{"resourceName":"resourceName"},"dimensions":{"heightPixels":0,"widthPixels":6},"locationAssociation":{"category":"CATEGORY_UNSPECIFIED","priceListItemId":"priceListItemId"},"thumbnailUrl":"thumbnailUrl"}],"languageCode":"languageCode","callToAction":{"actionType":"ACTION_TYPE_UNSPECIFIED","url":"url"},"topicType":"LOCAL_POST_TOPIC_TYPE_UNSPECIFIED","offer":{"termsConditions":"termsConditions","redeemOnlineUrl":"redeemOnlineUrl","couponCode":"couponCode"},"createTime":"createTime","name":"name","searchUrl":"searchUrl","state":"LOCAL_POST_STATE_UNSPECIFIED","event":{"schedule":{"endDate":{"month":5,"year":5,"day":1},"startTime":{"hours":7,"seconds":5,"nanos":4,"minutes":1},"endTime":{"hours":7,"seconds":5,"nanos":4,"minutes":1},"startDate":{"month":5,"year":5,"day":1}},"title":"title"}}
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
        path='/v4/{parent}/localPosts'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_local_posts_list(client):
    """Test case for mybusiness_accounts_locations_local_posts_list

    
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
    }
    response = await client.request(
        method='GET',
        path='/v4/{parent}/localPosts'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_local_posts_report_insights(client):
    """Test case for mybusiness_accounts_locations_local_posts_report_insights

    
    """
    body = {"basicRequest":{"metricRequests":[{"metric":"METRIC_UNSPECIFIED","options":["METRIC_OPTION_UNSPECIFIED","METRIC_OPTION_UNSPECIFIED"]},{"metric":"METRIC_UNSPECIFIED","options":["METRIC_OPTION_UNSPECIFIED","METRIC_OPTION_UNSPECIFIED"]}],"timeRange":{"startTime":"startTime","endTime":"endTime"}},"localPostNames":["localPostNames","localPostNames"]}
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
        path='/v4/{name}/localPosts:reportInsights'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_lodging_get_google_updated(client):
    """Test case for mybusiness_accounts_locations_lodging_get_google_updated

    
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
                    ('readMask', 'read_mask_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v4/{nameget_google_update}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_media_create(client):
    """Test case for mybusiness_accounts_locations_media_create

    
    """
    body = {"sourceUrl":"sourceUrl","createTime":"createTime","googleUrl":"googleUrl","insights":{"viewCount":"viewCount"},"attribution":{"profileName":"profileName","profileUrl":"profileUrl","takedownUrl":"takedownUrl","profilePhotoUrl":"profilePhotoUrl"},"name":"name","description":"description","mediaFormat":"MEDIA_FORMAT_UNSPECIFIED","dataRef":{"resourceName":"resourceName"},"dimensions":{"heightPixels":0,"widthPixels":6},"locationAssociation":{"category":"CATEGORY_UNSPECIFIED","priceListItemId":"priceListItemId"},"thumbnailUrl":"thumbnailUrl"}
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
        path='/v4/{parent}/media'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_media_customers_list(client):
    """Test case for mybusiness_accounts_locations_media_customers_list

    
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
    }
    response = await client.request(
        method='GET',
        path='/v4/{parent}/media/customers'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_media_list(client):
    """Test case for mybusiness_accounts_locations_media_list

    
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
    }
    response = await client.request(
        method='GET',
        path='/v4/{parent}/media'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_media_start_upload(client):
    """Test case for mybusiness_accounts_locations_media_start_upload

    
    """
    body = None
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
        path='/v4/{parent}/media:startUpload'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_questions_answers_delete(client):
    """Test case for mybusiness_accounts_locations_questions_answers_delete

    
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
    }
    response = await client.request(
        method='DELETE',
        path='/v4/{parent}/answers:delete'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_questions_answers_list(client):
    """Test case for mybusiness_accounts_locations_questions_answers_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v4/{parent}/answers'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_questions_answers_upsert(client):
    """Test case for mybusiness_accounts_locations_questions_answers_upsert

    
    """
    body = {"answer":{"createTime":"createTime","author":{"displayName":"displayName","type":"AUTHOR_TYPE_UNSPECIFIED","profilePhotoUrl":"profilePhotoUrl"},"name":"name","updateTime":"updateTime","text":"text","upvoteCount":0}}
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
        path='/v4/{parent}/answers:upsert'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_questions_create(client):
    """Test case for mybusiness_accounts_locations_questions_create

    
    """
    body = {"totalAnswerCount":6,"createTime":"createTime","author":{"displayName":"displayName","type":"AUTHOR_TYPE_UNSPECIFIED","profilePhotoUrl":"profilePhotoUrl"},"name":"name","updateTime":"updateTime","text":"text","topAnswers":[{"createTime":"createTime","author":{"displayName":"displayName","type":"AUTHOR_TYPE_UNSPECIFIED","profilePhotoUrl":"profilePhotoUrl"},"name":"name","updateTime":"updateTime","text":"text","upvoteCount":0},{"createTime":"createTime","author":{"displayName":"displayName","type":"AUTHOR_TYPE_UNSPECIFIED","profilePhotoUrl":"profilePhotoUrl"},"name":"name","updateTime":"updateTime","text":"text","upvoteCount":0}],"upvoteCount":1}
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
        path='/v4/{parent}/questions'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_questions_delete(client):
    """Test case for mybusiness_accounts_locations_questions_delete

    
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
    }
    response = await client.request(
        method='DELETE',
        path='/v4/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_questions_list(client):
    """Test case for mybusiness_accounts_locations_questions_list

    
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
                    ('answersPerQuestion', 56),
                    ('filter', 'filter_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v4/{parent}/questions'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_questions_patch(client):
    """Test case for mybusiness_accounts_locations_questions_patch

    
    """
    body = {"totalAnswerCount":6,"createTime":"createTime","author":{"displayName":"displayName","type":"AUTHOR_TYPE_UNSPECIFIED","profilePhotoUrl":"profilePhotoUrl"},"name":"name","updateTime":"updateTime","text":"text","topAnswers":[{"createTime":"createTime","author":{"displayName":"displayName","type":"AUTHOR_TYPE_UNSPECIFIED","profilePhotoUrl":"profilePhotoUrl"},"name":"name","updateTime":"updateTime","text":"text","upvoteCount":0},{"createTime":"createTime","author":{"displayName":"displayName","type":"AUTHOR_TYPE_UNSPECIFIED","profilePhotoUrl":"profilePhotoUrl"},"name":"name","updateTime":"updateTime","text":"text","upvoteCount":0}],"upvoteCount":1}
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
        path='/v4/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_report_insights(client):
    """Test case for mybusiness_accounts_locations_report_insights

    
    """
    body = {"drivingDirectionsRequest":{"numDays":"SEVEN","languageCode":"languageCode"},"locationNames":["locationNames","locationNames"],"basicRequest":{"metricRequests":[{"metric":"METRIC_UNSPECIFIED","options":["METRIC_OPTION_UNSPECIFIED","METRIC_OPTION_UNSPECIFIED"]},{"metric":"METRIC_UNSPECIFIED","options":["METRIC_OPTION_UNSPECIFIED","METRIC_OPTION_UNSPECIFIED"]}],"timeRange":{"startTime":"startTime","endTime":"endTime"}}}
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
        path='/v4/{name}/locations:reportInsights'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_reviews_delete_reply(client):
    """Test case for mybusiness_accounts_locations_reviews_delete_reply

    
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
    }
    response = await client.request(
        method='DELETE',
        path='/v4/{name}/reply'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_reviews_list(client):
    """Test case for mybusiness_accounts_locations_reviews_list

    
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
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v4/{parent}/reviews'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_reviews_update_reply(client):
    """Test case for mybusiness_accounts_locations_reviews_update_reply

    
    """
    body = {"comment":"comment","updateTime":"updateTime"}
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
        method='PUT',
        path='/v4/{name}/reply'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_transfer(client):
    """Test case for mybusiness_accounts_locations_transfer

    
    """
    body = {"toAccount":"toAccount"}
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
        path='/v4/{nametransfe}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_verifications_complete(client):
    """Test case for mybusiness_accounts_locations_verifications_complete

    
    """
    body = {"pin":"pin"}
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
        path='/v4/{namecomplet}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_verifications_list(client):
    """Test case for mybusiness_accounts_locations_verifications_list

    
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
    }
    response = await client.request(
        method='GET',
        path='/v4/{parent}/verifications'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_locations_verify(client):
    """Test case for mybusiness_accounts_locations_verify

    
    """
    body = {"method":"VERIFICATION_METHOD_UNSPECIFIED","context":{"address":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":0}},"languageCode":"languageCode","phoneInput":{"phoneNumber":"phoneNumber"},"addressInput":{"mailerContactName":"mailerContactName"},"emailInput":{"emailAddress":"emailAddress"}}
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
        path='/v4/{nameverif}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusiness_accounts_update_notifications(client):
    """Test case for mybusiness_accounts_update_notifications

    
    """
    body = {"name":"name","topicName":"topicName","notificationTypes":["NOTIFICATION_TYPE_UNSPECIFIED","NOTIFICATION_TYPE_UNSPECIFIED"]}
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
        method='PUT',
        path='/v4/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

