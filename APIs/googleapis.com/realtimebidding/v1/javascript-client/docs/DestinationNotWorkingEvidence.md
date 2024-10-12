# RealTimeBiddingApi.DestinationNotWorkingEvidence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsError** | **String** | DNS lookup errors. | [optional] 
**expandedUrl** | **String** | The full non-working URL. | [optional] 
**httpError** | **Number** | HTTP error code (for example, 404 or 5xx) | [optional] 
**invalidPage** | **String** | Page was crawled successfully, but was detected as either a page with no content or an error page. | [optional] 
**lastCheckTime** | **String** | Approximate time when the ad destination was last checked. | [optional] 
**platform** | **String** | Platform of the non-working URL. | [optional] 
**redirectionError** | **String** | HTTP redirect chain error. | [optional] 
**urlRejected** | **String** | Rejected because of malformed URLs or invalid requests. | [optional] 



## Enum: DnsErrorEnum


* `DNS_ERROR_UNSPECIFIED` (value: `"DNS_ERROR_UNSPECIFIED"`)

* `ERROR_DNS` (value: `"ERROR_DNS"`)

* `GOOGLE_CRAWLER_DNS_ISSUE` (value: `"GOOGLE_CRAWLER_DNS_ISSUE"`)





## Enum: InvalidPageEnum


* `INVALID_PAGE_UNSPECIFIED` (value: `"INVALID_PAGE_UNSPECIFIED"`)

* `EMPTY_OR_ERROR_PAGE` (value: `"EMPTY_OR_ERROR_PAGE"`)





## Enum: PlatformEnum


* `PLATFORM_UNSPECIFIED` (value: `"PLATFORM_UNSPECIFIED"`)

* `PERSONAL_COMPUTER` (value: `"PERSONAL_COMPUTER"`)

* `ANDROID` (value: `"ANDROID"`)

* `IOS` (value: `"IOS"`)





## Enum: RedirectionErrorEnum


* `REDIRECTION_ERROR_UNSPECIFIED` (value: `"REDIRECTION_ERROR_UNSPECIFIED"`)

* `TOO_MANY_REDIRECTS` (value: `"TOO_MANY_REDIRECTS"`)

* `INVALID_REDIRECT` (value: `"INVALID_REDIRECT"`)

* `EMPTY_REDIRECT` (value: `"EMPTY_REDIRECT"`)

* `REDIRECT_ERROR_UNKNOWN` (value: `"REDIRECT_ERROR_UNKNOWN"`)





## Enum: UrlRejectedEnum


* `URL_REJECTED_UNSPECIFIED` (value: `"URL_REJECTED_UNSPECIFIED"`)

* `BAD_REQUEST` (value: `"BAD_REQUEST"`)

* `MALFORMED_URL` (value: `"MALFORMED_URL"`)

* `URL_REJECTED_UNKNOWN` (value: `"URL_REJECTED_UNKNOWN"`)




