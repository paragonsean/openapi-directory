# CdnManagementClient.UrlRedirectActionParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**odataType** | **String** |  | 
**customFragment** | **String** | Fragment to add to the redirect URL. Fragment is the part of the URL that comes after #. Do not include the #. | [optional] 
**customHostname** | **String** | Host to redirect. Leave empty to use the incoming host as the destination host. | [optional] 
**customPath** | **String** | The full path to redirect. Path cannot be empty and must start with /. Leave empty to use the incoming path as destination path. | [optional] 
**customQueryString** | **String** | The set of query strings to be placed in the redirect URL. Setting this value would replace any existing query string; leave empty to preserve the incoming query string. Query string must be in &lt;key&gt;&#x3D;&lt;value&gt; format. ? and &amp; will be added automatically so do not include them. | [optional] 
**destinationProtocol** | **String** | Protocol to use for the redirect. The default value is MatchRequest | [optional] 
**redirectType** | **String** | The redirect type the rule will use when redirecting traffic. | 



## Enum: OdataTypeEnum


* `#Microsoft.Azure.Cdn.Models.DeliveryRuleUrlRedirectActionParameters` (value: `"#Microsoft.Azure.Cdn.Models.DeliveryRuleUrlRedirectActionParameters"`)





## Enum: DestinationProtocolEnum


* `MatchRequest` (value: `"MatchRequest"`)

* `Http` (value: `"Http"`)

* `Https` (value: `"Https"`)





## Enum: RedirectTypeEnum


* `Moved` (value: `"Moved"`)

* `Found` (value: `"Found"`)

* `TemporaryRedirect` (value: `"TemporaryRedirect"`)

* `PermanentRedirect` (value: `"PermanentRedirect"`)




