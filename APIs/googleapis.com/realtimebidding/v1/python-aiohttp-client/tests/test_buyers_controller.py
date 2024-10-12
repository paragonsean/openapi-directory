# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.creative import Creative
from openapi_server.models.get_remarketing_tag_response import GetRemarketingTagResponse
from openapi_server.models.list_buyers_response import ListBuyersResponse
from openapi_server.models.list_creatives_response import ListCreativesResponse
from openapi_server.models.list_user_lists_response import ListUserListsResponse
from openapi_server.models.user_list import UserList


pytestmark = pytest.mark.asyncio

async def test_realtimebidding_buyers_creatives_create(client):
    """Test case for realtimebidding_buyers_creatives_create

    
    """
    body = {"declaredVendorIds":[2,2],"creativeServingDecision":{"dealsPolicyCompliance":{"topics":[{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]},{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]}],"status":"STATUS_UNSPECIFIED"},"detectedAttributes":["ATTRIBUTE_UNSPECIFIED","ATTRIBUTE_UNSPECIFIED"],"chinaPolicyCompliance":{"topics":[{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]},{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]}],"status":"STATUS_UNSPECIFIED"},"detectedLanguages":["detectedLanguages","detectedLanguages"],"lastStatusUpdate":"lastStatusUpdate","detectedAdvertisers":[{"brandName":"brandName","brandId":"brandId","advertiserName":"advertiserName","advertiserId":"advertiserId"},{"brandName":"brandName","brandId":"brandId","advertiserName":"advertiserName","advertiserId":"advertiserId"}],"adTechnologyProviders":{"detectedGvlIds":["detectedGvlIds","detectedGvlIds"],"unidentifiedProviderDomains":["unidentifiedProviderDomains","unidentifiedProviderDomains"],"detectedProviderIds":["detectedProviderIds","detectedProviderIds"]},"detectedClickThroughUrls":["detectedClickThroughUrls","detectedClickThroughUrls"],"detectedProductCategories":[7,7],"detectedVendorIds":[3,3],"platformPolicyCompliance":{"topics":[{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]},{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]}],"status":"STATUS_UNSPECIFIED"},"detectedSensitiveCategories":[9,9],"detectedDomains":["detectedDomains","detectedDomains"],"networkPolicyCompliance":{"topics":[{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]},{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]}],"status":"STATUS_UNSPECIFIED"},"russiaPolicyCompliance":{"topics":[{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]},{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]}],"status":"STATUS_UNSPECIFIED"}},"impressionTrackingUrls":["impressionTrackingUrls","impressionTrackingUrls"],"apiUpdateTime":"apiUpdateTime","agencyId":"agencyId","video":{"videoUrl":"videoUrl","videoVastXml":"videoVastXml","videoMetadata":{"duration":"duration","isVpaid":True,"mediaFiles":[{"bitrate":"bitrate","mimeType":"VIDEO_MIME_TYPE_UNSPECIFIED"},{"bitrate":"bitrate","mimeType":"VIDEO_MIME_TYPE_UNSPECIFIED"}],"skipOffset":"skipOffset","isValidVast":True,"vastVersion":"VAST_VERSION_UNSPECIFIED"}},"version":6,"advertiserName":"advertiserName","creativeId":"creativeId","restrictedCategories":["RESTRICTED_CATEGORY_UNSPECIFIED","RESTRICTED_CATEGORY_UNSPECIFIED"],"accountId":"accountId","adChoicesDestinationUrl":"adChoicesDestinationUrl","native":{"image":{"width":1,"url":"url","height":1},"clickLinkUrl":"clickLinkUrl","body":"body","advertiserName":"advertiserName","callToAction":"callToAction","appIcon":{"width":1,"url":"url","height":1},"clickTrackingUrl":"clickTrackingUrl","videoUrl":"videoUrl","logo":{"width":1,"url":"url","height":1},"videoVastXml":"videoVastXml","starRating":1.4894159098541704,"headline":"headline","priceDisplayText":"priceDisplayText"},"name":"name","declaredAttributes":["ATTRIBUTE_UNSPECIFIED","ATTRIBUTE_UNSPECIFIED"],"declaredClickThroughUrls":["declaredClickThroughUrls","declaredClickThroughUrls"],"html":{"snippet":"snippet","width":7,"height":4},"declaredRestrictedCategories":["RESTRICTED_CATEGORY_UNSPECIFIED","RESTRICTED_CATEGORY_UNSPECIFIED"],"dealIds":["dealIds","dealIds"],"creativeFormat":"CREATIVE_FORMAT_UNSPECIFIED","renderUrl":"renderUrl"}
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
        path='/v1/{parent}/creatives'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realtimebidding_buyers_creatives_list(client):
    """Test case for realtimebidding_buyers_creatives_list

    
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
                    ('pageToken', 'page_token_example'),
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/creatives'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realtimebidding_buyers_creatives_patch(client):
    """Test case for realtimebidding_buyers_creatives_patch

    
    """
    body = {"declaredVendorIds":[2,2],"creativeServingDecision":{"dealsPolicyCompliance":{"topics":[{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]},{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]}],"status":"STATUS_UNSPECIFIED"},"detectedAttributes":["ATTRIBUTE_UNSPECIFIED","ATTRIBUTE_UNSPECIFIED"],"chinaPolicyCompliance":{"topics":[{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]},{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]}],"status":"STATUS_UNSPECIFIED"},"detectedLanguages":["detectedLanguages","detectedLanguages"],"lastStatusUpdate":"lastStatusUpdate","detectedAdvertisers":[{"brandName":"brandName","brandId":"brandId","advertiserName":"advertiserName","advertiserId":"advertiserId"},{"brandName":"brandName","brandId":"brandId","advertiserName":"advertiserName","advertiserId":"advertiserId"}],"adTechnologyProviders":{"detectedGvlIds":["detectedGvlIds","detectedGvlIds"],"unidentifiedProviderDomains":["unidentifiedProviderDomains","unidentifiedProviderDomains"],"detectedProviderIds":["detectedProviderIds","detectedProviderIds"]},"detectedClickThroughUrls":["detectedClickThroughUrls","detectedClickThroughUrls"],"detectedProductCategories":[7,7],"detectedVendorIds":[3,3],"platformPolicyCompliance":{"topics":[{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]},{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]}],"status":"STATUS_UNSPECIFIED"},"detectedSensitiveCategories":[9,9],"detectedDomains":["detectedDomains","detectedDomains"],"networkPolicyCompliance":{"topics":[{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]},{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]}],"status":"STATUS_UNSPECIFIED"},"russiaPolicyCompliance":{"topics":[{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]},{"missingCertificate":True,"helpCenterUrl":"helpCenterUrl","policyTopic":"policyTopic","evidences":[{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}},{"domainCall":{"totalHttpCallCount":1,"topHttpCallDomains":[{"domain":"domain","httpCallCount":6},{"domain":"domain","httpCallCount":6}]},"downloadSize":{"topUrlDownloadSizeBreakdowns":[{"normalizedUrl":"normalizedUrl","downloadSizeKb":5},{"normalizedUrl":"normalizedUrl","downloadSizeKb":5}],"totalDownloadSizeKb":5},"httpCookie":{"maxCookieCount":2,"cookieNames":["cookieNames","cookieNames"]},"destinationNotWorking":{"lastCheckTime":"lastCheckTime","urlRejected":"URL_REJECTED_UNSPECIFIED","redirectionError":"REDIRECTION_ERROR_UNSPECIFIED","httpError":0,"invalidPage":"INVALID_PAGE_UNSPECIFIED","expandedUrl":"expandedUrl","dnsError":"DNS_ERROR_UNSPECIFIED","platform":"PLATFORM_UNSPECIFIED"},"destinationNotCrawlable":{"reason":"REASON_UNSPECIFIED","crawlTime":"crawlTime","crawledUrl":"crawledUrl"},"destinationUrl":{"destinationUrl":"destinationUrl"},"httpCall":{"urls":["urls","urls"]}}]}],"status":"STATUS_UNSPECIFIED"}},"impressionTrackingUrls":["impressionTrackingUrls","impressionTrackingUrls"],"apiUpdateTime":"apiUpdateTime","agencyId":"agencyId","video":{"videoUrl":"videoUrl","videoVastXml":"videoVastXml","videoMetadata":{"duration":"duration","isVpaid":True,"mediaFiles":[{"bitrate":"bitrate","mimeType":"VIDEO_MIME_TYPE_UNSPECIFIED"},{"bitrate":"bitrate","mimeType":"VIDEO_MIME_TYPE_UNSPECIFIED"}],"skipOffset":"skipOffset","isValidVast":True,"vastVersion":"VAST_VERSION_UNSPECIFIED"}},"version":6,"advertiserName":"advertiserName","creativeId":"creativeId","restrictedCategories":["RESTRICTED_CATEGORY_UNSPECIFIED","RESTRICTED_CATEGORY_UNSPECIFIED"],"accountId":"accountId","adChoicesDestinationUrl":"adChoicesDestinationUrl","native":{"image":{"width":1,"url":"url","height":1},"clickLinkUrl":"clickLinkUrl","body":"body","advertiserName":"advertiserName","callToAction":"callToAction","appIcon":{"width":1,"url":"url","height":1},"clickTrackingUrl":"clickTrackingUrl","videoUrl":"videoUrl","logo":{"width":1,"url":"url","height":1},"videoVastXml":"videoVastXml","starRating":1.4894159098541704,"headline":"headline","priceDisplayText":"priceDisplayText"},"name":"name","declaredAttributes":["ATTRIBUTE_UNSPECIFIED","ATTRIBUTE_UNSPECIFIED"],"declaredClickThroughUrls":["declaredClickThroughUrls","declaredClickThroughUrls"],"html":{"snippet":"snippet","width":7,"height":4},"declaredRestrictedCategories":["RESTRICTED_CATEGORY_UNSPECIFIED","RESTRICTED_CATEGORY_UNSPECIFIED"],"dealIds":["dealIds","dealIds"],"creativeFormat":"CREATIVE_FORMAT_UNSPECIFIED","renderUrl":"renderUrl"}
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
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realtimebidding_buyers_list(client):
    """Test case for realtimebidding_buyers_list

    
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
        path='/v1/buyers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realtimebidding_buyers_user_lists_close(client):
    """Test case for realtimebidding_buyers_user_lists_close

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameclos}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realtimebidding_buyers_user_lists_create(client):
    """Test case for realtimebidding_buyers_user_lists_create

    
    """
    body = {"displayName":"displayName","membershipDurationDays":"membershipDurationDays","name":"name","urlRestriction":{"restrictionType":"RESTRICTION_TYPE_UNSPECIFIED","endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0},"url":"url"},"description":"description","status":"STATUS_UNSPECIFIED"}
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
        path='/v1/{parent}/userLists'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realtimebidding_buyers_user_lists_get(client):
    """Test case for realtimebidding_buyers_user_lists_get

    
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
                    ('view', 'view_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realtimebidding_buyers_user_lists_get_remarketing_tag(client):
    """Test case for realtimebidding_buyers_user_lists_get_remarketing_tag

    
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
        path='/v1/{nameget_remarketing_ta}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realtimebidding_buyers_user_lists_list(client):
    """Test case for realtimebidding_buyers_user_lists_list

    
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
        path='/v1/{parent}/userLists'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realtimebidding_buyers_user_lists_open(client):
    """Test case for realtimebidding_buyers_user_lists_open

    
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
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameope}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realtimebidding_buyers_user_lists_update(client):
    """Test case for realtimebidding_buyers_user_lists_update

    
    """
    body = {"displayName":"displayName","membershipDurationDays":"membershipDurationDays","name":"name","urlRestriction":{"restrictionType":"RESTRICTION_TYPE_UNSPECIFIED","endDate":{"month":6,"year":1,"day":0},"startDate":{"month":6,"year":1,"day":0},"url":"url"},"description":"description","status":"STATUS_UNSPECIFIED"}
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
        method='PUT',
        path='/v1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

