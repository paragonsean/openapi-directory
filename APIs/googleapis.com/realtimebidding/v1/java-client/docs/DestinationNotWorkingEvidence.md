

# DestinationNotWorkingEvidence

Evidence of the creative's destination URL not functioning properly or having been incorrectly set up.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dnsError** | [**DnsErrorEnum**](#DnsErrorEnum) | DNS lookup errors. |  [optional] |
|**expandedUrl** | **String** | The full non-working URL. |  [optional] |
|**httpError** | **Integer** | HTTP error code (for example, 404 or 5xx) |  [optional] |
|**invalidPage** | [**InvalidPageEnum**](#InvalidPageEnum) | Page was crawled successfully, but was detected as either a page with no content or an error page. |  [optional] |
|**lastCheckTime** | **String** | Approximate time when the ad destination was last checked. |  [optional] |
|**platform** | [**PlatformEnum**](#PlatformEnum) | Platform of the non-working URL. |  [optional] |
|**redirectionError** | [**RedirectionErrorEnum**](#RedirectionErrorEnum) | HTTP redirect chain error. |  [optional] |
|**urlRejected** | [**UrlRejectedEnum**](#UrlRejectedEnum) | Rejected because of malformed URLs or invalid requests. |  [optional] |



## Enum: DnsErrorEnum

| Name | Value |
|---- | -----|
| DNS_ERROR_UNSPECIFIED | &quot;DNS_ERROR_UNSPECIFIED&quot; |
| ERROR_DNS | &quot;ERROR_DNS&quot; |
| GOOGLE_CRAWLER_DNS_ISSUE | &quot;GOOGLE_CRAWLER_DNS_ISSUE&quot; |



## Enum: InvalidPageEnum

| Name | Value |
|---- | -----|
| INVALID_PAGE_UNSPECIFIED | &quot;INVALID_PAGE_UNSPECIFIED&quot; |
| EMPTY_OR_ERROR_PAGE | &quot;EMPTY_OR_ERROR_PAGE&quot; |



## Enum: PlatformEnum

| Name | Value |
|---- | -----|
| PLATFORM_UNSPECIFIED | &quot;PLATFORM_UNSPECIFIED&quot; |
| PERSONAL_COMPUTER | &quot;PERSONAL_COMPUTER&quot; |
| ANDROID | &quot;ANDROID&quot; |
| IOS | &quot;IOS&quot; |



## Enum: RedirectionErrorEnum

| Name | Value |
|---- | -----|
| REDIRECTION_ERROR_UNSPECIFIED | &quot;REDIRECTION_ERROR_UNSPECIFIED&quot; |
| TOO_MANY_REDIRECTS | &quot;TOO_MANY_REDIRECTS&quot; |
| INVALID_REDIRECT | &quot;INVALID_REDIRECT&quot; |
| EMPTY_REDIRECT | &quot;EMPTY_REDIRECT&quot; |
| REDIRECT_ERROR_UNKNOWN | &quot;REDIRECT_ERROR_UNKNOWN&quot; |



## Enum: UrlRejectedEnum

| Name | Value |
|---- | -----|
| URL_REJECTED_UNSPECIFIED | &quot;URL_REJECTED_UNSPECIFIED&quot; |
| BAD_REQUEST | &quot;BAD_REQUEST&quot; |
| MALFORMED_URL | &quot;MALFORMED_URL&quot; |
| URL_REJECTED_UNKNOWN | &quot;URL_REJECTED_UNKNOWN&quot; |



