# FrontDoorManagementClient.RedirectConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customFragment** | **String** | Fragment to add to the redirect URL. Fragment is the part of the URL that comes after #. Do not include the #. | [optional] 
**customHost** | **String** | Host to redirect. Leave empty to use the incoming host as the destination host. | [optional] 
**customPath** | **String** | The full path to redirect. Path cannot be empty and must start with /. Leave empty to use the incoming path as destination path. | [optional] 
**customQueryString** | **String** | The set of query strings to be placed in the redirect URL. Setting this value would replace any existing query string; leave empty to preserve the incoming query string. Query string must be in &lt;key&gt;&#x3D;&lt;value&gt; format. The first ? and &amp; will be added automatically so do not include them in the front, but do separate multiple query strings with &amp;. | [optional] 
**redirectProtocol** | **String** | The protocol of the destination to where the traffic is redirected | [optional] 
**redirectType** | **String** | The redirect type the rule will use when redirecting traffic. | [optional] 



## Enum: RedirectProtocolEnum


* `HttpOnly` (value: `"HttpOnly"`)

* `HttpsOnly` (value: `"HttpsOnly"`)

* `MatchRequest` (value: `"MatchRequest"`)





## Enum: RedirectTypeEnum


* `Moved` (value: `"Moved"`)

* `Found` (value: `"Found"`)

* `TemporaryRedirect` (value: `"TemporaryRedirect"`)

* `PermanentRedirect` (value: `"PermanentRedirect"`)




