# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.video import Video
from openapi_server.models.video_abuse_report import VideoAbuseReport
from openapi_server.models.video_get_rating_response import VideoGetRatingResponse
from openapi_server.models.video_list_response import VideoListResponse


pytestmark = pytest.mark.asyncio

async def test_youtube_videos_delete(client):
    """Test case for youtube_videos_delete

    
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
                    ('id', 'id_example'),
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/youtube/v3/videos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_videos_get_rating(client):
    """Test case for youtube_videos_get_rating

    
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
                    ('id', ['id_example']),
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/youtube/v3/videos/getRating',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_youtube_videos_insert(client):
    """Test case for youtube_videos_insert

    
    """
    body = openapi_server.Video()
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
                    ('part', ['part_example']),
                    ('autoLevels', True),
                    ('notifySubscribers', True),
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example'),
                    ('onBehalfOfContentOwnerChannel', 'on_behalf_of_content_owner_channel_example'),
                    ('stabilize', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/octet-stream',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/youtube/v3/videos',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_videos_list(client):
    """Test case for youtube_videos_list

    
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
                    ('part', ['part_example']),
                    ('chart', 'chart_example'),
                    ('hl', 'hl_example'),
                    ('id', ['id_example']),
                    ('locale', 'locale_example'),
                    ('maxHeight', 56),
                    ('maxResults', 56),
                    ('maxWidth', 56),
                    ('myRating', 'my_rating_example'),
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example'),
                    ('pageToken', 'page_token_example'),
                    ('regionCode', 'region_code_example'),
                    ('videoCategoryId', 'video_category_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/youtube/v3/videos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_videos_rate(client):
    """Test case for youtube_videos_rate

    
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
                    ('id', 'id_example'),
                    ('rating', 'rating_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/youtube/v3/videos/rate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_videos_report_abuse(client):
    """Test case for youtube_videos_report_abuse

    
    """
    body = {"comments":"comments","reasonId":"reasonId","secondaryReasonId":"secondaryReasonId","language":"language","videoId":"videoId"}
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
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/youtube/v3/videos/reportAbuse',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_youtube_videos_update(client):
    """Test case for youtube_videos_update

    
    """
    body = {"snippet":{"defaultLanguage":"defaultLanguage","publishedAt":"2000-01-23T04:56:07.000+00:00","defaultAudioLanguage":"defaultAudioLanguage","localized":{"description":"description","title":"title"},"description":"description","thumbnails":{"standard":{"width":6,"url":"url","height":0},"high":{"width":6,"url":"url","height":0},"maxres":{"width":6,"url":"url","height":0},"medium":{"width":6,"url":"url","height":0}},"title":"title","categoryId":"categoryId","channelId":"channelId","channelTitle":"channelTitle","liveBroadcastContent":"none","tags":["tags","tags"]},"fileDetails":{"container":"container","fileName":"fileName","creationTime":"creationTime","fileSize":"fileSize","videoStreams":[{"codec":"codec","vendor":"vendor","rotation":"none","frameRateFps":1.4658129805029452,"aspectRatio":6.027456183070403,"heightPixels":5,"bitrateBps":"bitrateBps","widthPixels":5},{"codec":"codec","vendor":"vendor","rotation":"none","frameRateFps":1.4658129805029452,"aspectRatio":6.027456183070403,"heightPixels":5,"bitrateBps":"bitrateBps","widthPixels":5}],"audioStreams":[{"channelCount":0,"codec":"codec","vendor":"vendor","bitrateBps":"bitrateBps"},{"channelCount":0,"codec":"codec","vendor":"vendor","bitrateBps":"bitrateBps"}],"bitrateBps":"bitrateBps","durationMs":"durationMs","fileType":"video"},"monetizationDetails":{"access":{"exception":["exception","exception"],"allowed":True}},"localizations":{"key":{"description":"description","title":"title"}},"kind":"youtube#video","recordingDetails":{"locationDescription":"locationDescription","recordingDate":"2000-01-23T04:56:07.000+00:00","location":{"altitude":2.3021358869347655,"latitude":7.061401241503109,"longitude":9.301444243932576}},"projectDetails":"{}","contentDetails":{"duration":"duration","licensedContent":True,"countryRestriction":{"exception":["exception","exception"],"allowed":True},"caption":"true","contentRating":{"ifcoRating":"ifcoUnspecified","lsfRating":"lsfUnspecified","cicfRating":"cicfUnspecified","tvpgRating":"tvpgUnspecified","menaMpaaRating":"menaMpaaUnspecified","ilfilmRating":"ilfilmUnspecified","nmcRating":"nmcUnspecified","nkclvRating":"nkclvUnspecified","catvfrRating":"catvfrUnspecified","egfilmRating":"egfilmUnspecified","cccRating":"cccUnspecified","resorteviolenciaRating":"resorteviolenciaUnspecified","chvrsRating":"chvrsUnspecified","nbcplRating":"nbcplUnspecified","chfilmRating":"chfilmUnspecified","anatelRating":"anatelUnspecified","smsaRating":"smsaUnspecified","smaisRating":"smaisUnspecified","kfcbRating":"kfcbUnspecified","skfilmRating":"skfilmUnspecified","acbRating":"acbUnspecified","mibacRating":"mibacUnspecified","djctqRatingReasons":["djctqRatingReasonUnspecified","djctqRatingReasonUnspecified"],"ytRating":"ytUnspecified","kijkwijzerRating":"kijkwijzerUnspecified","mdaRating":"mdaUnspecified","fcoRating":"fcoUnspecified","mekuRating":"mekuUnspecified","mccaaRating":"mccaaUnspecified","cncRating":"cncUnspecified","rteRating":"rteUnspecified","nbcRating":"nbcUnspecified","moctwRating":"moctwUnspecified","mocRating":"mocUnspecified","csaRating":"csaUnspecified","mpaaRating":"mpaaUnspecified","pefilmRating":"pefilmUnspecified","cscfRating":"cscfUnspecified","bfvcRating":"bfvcUnspecified","mccypRating":"mccypUnspecified","mpaatRating":"mpaatUnspecified","mcstRating":"mcstUnspecified","eefilmRating":"eefilmUnspecified","grfilmRating":"grfilmUnspecified","bmukkRating":"bmukkUnspecified","cbfcRating":"cbfcUnspecified","djctqRating":"djctqUnspecified","rcnofRating":"rcnofUnspecified","fmocRating":"fmocUnspecified","mtrcbRating":"mtrcbUnspecified","oflcRating":"oflcUnspecified","agcomRating":"agcomUnspecified","russiaRating":"russiaUnspecified","cceRating":"cceUnspecified","fskRating":"fskUnspecified","rtcRating":"rtcUnspecified","nfvcbRating":"nfvcbUnspecified","incaaRating":"incaaUnspecified","medietilsynetRating":"medietilsynetUnspecified","eirinRating":"eirinUnspecified","fpbRatingReasons":["fpbRatingReasonUnspecified","fpbRatingReasonUnspecified"],"icaaRating":"icaaUnspecified","catvRating":"catvUnspecified","fcbmRating":"fcbmUnspecified","fpbRating":"fpbUnspecified","bbfcRating":"bbfcUnspecified","kmrbRating":"kmrbUnspecified","nfrcRating":"nfrcUnspecified","cnaRating":"cnaUnspecified","czfilmRating":"czfilmUnspecified","ecbmctRating":"ecbmctUnspecified"},"definition":"sd","hasCustomThumbnail":True,"projection":"rectangular","regionRestriction":{"blocked":["blocked","blocked"],"allowed":["allowed","allowed"]},"dimension":"dimension"},"topicDetails":{"relevantTopicIds":["relevantTopicIds","relevantTopicIds"],"topicIds":["topicIds","topicIds"],"topicCategories":["topicCategories","topicCategories"]},"liveStreamingDetails":{"activeLiveChatId":"activeLiveChatId","actualStartTime":"2000-01-23T04:56:07.000+00:00","scheduledStartTime":"2000-01-23T04:56:07.000+00:00","scheduledEndTime":"2000-01-23T04:56:07.000+00:00","actualEndTime":"2000-01-23T04:56:07.000+00:00","concurrentViewers":"concurrentViewers"},"processingDetails":{"processingStatus":"processing","processingFailureReason":"uploadFailed","thumbnailsAvailability":"thumbnailsAvailability","fileDetailsAvailability":"fileDetailsAvailability","editorSuggestionsAvailability":"editorSuggestionsAvailability","tagSuggestionsAvailability":"tagSuggestionsAvailability","processingIssuesAvailability":"processingIssuesAvailability","processingProgress":{"partsProcessed":"partsProcessed","timeLeftMs":"timeLeftMs","partsTotal":"partsTotal"}},"ageGating":{"alcoholContent":True,"restricted":True,"videoGameRating":"anyone"},"etag":"etag","suggestions":{"processingWarnings":["unknownContainer","unknownContainer"],"editorSuggestions":["videoAutoLevels","videoAutoLevels"],"processingErrors":["audioFile","audioFile"],"processingHints":["nonStreamableMov","nonStreamableMov"],"tagSuggestions":[{"tag":"tag","categoryRestricts":["categoryRestricts","categoryRestricts"]},{"tag":"tag","categoryRestricts":["categoryRestricts","categoryRestricts"]}]},"id":"id","player":{"embedHeight":"embedHeight","embedWidth":"embedWidth","embedHtml":"embedHtml"},"statistics":{"dislikeCount":"dislikeCount","likeCount":"likeCount","viewCount":"viewCount","commentCount":"commentCount","favoriteCount":"favoriteCount"},"status":{"license":"youtube","selfDeclaredMadeForKids":True,"failureReason":"conversion","privacyStatus":"public","publishAt":"2000-01-23T04:56:07.000+00:00","uploadStatus":"uploaded","publicStatsViewable":True,"rejectionReason":"copyright","embeddable":True,"madeForKids":True}}
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
                    ('part', ['part_example']),
                    ('onBehalfOfContentOwner', 'on_behalf_of_content_owner_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/youtube/v3/videos',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

