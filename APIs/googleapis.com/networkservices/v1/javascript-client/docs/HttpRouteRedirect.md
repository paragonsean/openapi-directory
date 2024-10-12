# NetworkServicesApi.HttpRouteRedirect

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostRedirect** | **String** | The host that will be used in the redirect response instead of the one that was supplied in the request. | [optional] 
**httpsRedirect** | **Boolean** | If set to true, the URL scheme in the redirected request is set to https. If set to false, the URL scheme of the redirected request will remain the same as that of the request. The default is set to false. | [optional] 
**pathRedirect** | **String** | The path that will be used in the redirect response instead of the one that was supplied in the request. path_redirect can not be supplied together with prefix_redirect. Supply one alone or neither. If neither is supplied, the path of the original request will be used for the redirect. | [optional] 
**portRedirect** | **Number** | The port that will be used in the redirected request instead of the one that was supplied in the request. | [optional] 
**prefixRewrite** | **String** | Indicates that during redirection, the matched prefix (or path) should be swapped with this value. This option allows URLs be dynamically created based on the request. | [optional] 
**responseCode** | **String** | The HTTP Status code to use for the redirect. | [optional] 
**stripQuery** | **Boolean** | if set to true, any accompanying query portion of the original URL is removed prior to redirecting the request. If set to false, the query portion of the original URL is retained. The default is set to false. | [optional] 



## Enum: ResponseCodeEnum


* `RESPONSE_CODE_UNSPECIFIED` (value: `"RESPONSE_CODE_UNSPECIFIED"`)

* `MOVED_PERMANENTLY_DEFAULT` (value: `"MOVED_PERMANENTLY_DEFAULT"`)

* `FOUND` (value: `"FOUND"`)

* `SEE_OTHER` (value: `"SEE_OTHER"`)

* `TEMPORARY_REDIRECT` (value: `"TEMPORARY_REDIRECT"`)

* `PERMANENT_REDIRECT` (value: `"PERMANENT_REDIRECT"`)




