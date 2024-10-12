

# UrlRedirectActionParameters

Defines the parameters for the url redirect action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atOdataType** | [**AtOdataTypeEnum**](#AtOdataTypeEnum) |  |  |
|**customFragment** | **String** | Fragment to add to the redirect URL. Fragment is the part of the URL that comes after #. Do not include the #. |  [optional] |
|**customHostname** | **String** | Host to redirect. Leave empty to use the incoming host as the destination host. |  [optional] |
|**customPath** | **String** | The full path to redirect. Path cannot be empty and must start with /. Leave empty to use the incoming path as destination path. |  [optional] |
|**customQueryString** | **String** | The set of query strings to be placed in the redirect URL. Setting this value would replace any existing query string; leave empty to preserve the incoming query string. Query string must be in &lt;key&gt;&#x3D;&lt;value&gt; format. ? and &amp; will be added automatically so do not include them. |  [optional] |
|**destinationProtocol** | [**DestinationProtocolEnum**](#DestinationProtocolEnum) | Protocol to use for the redirect. The default value is MatchRequest |  [optional] |
|**redirectType** | [**RedirectTypeEnum**](#RedirectTypeEnum) | The redirect type the rule will use when redirecting traffic. |  |



## Enum: AtOdataTypeEnum

| Name | Value |
|---- | -----|
| _MICROSOFT_AZURE_CDN_MODELS_DELIVERY_RULE_URL_REDIRECT_ACTION_PARAMETERS | &quot;#Microsoft.Azure.Cdn.Models.DeliveryRuleUrlRedirectActionParameters&quot; |



## Enum: DestinationProtocolEnum

| Name | Value |
|---- | -----|
| MATCH_REQUEST | &quot;MatchRequest&quot; |
| HTTP | &quot;Http&quot; |
| HTTPS | &quot;Https&quot; |



## Enum: RedirectTypeEnum

| Name | Value |
|---- | -----|
| MOVED | &quot;Moved&quot; |
| FOUND | &quot;Found&quot; |
| TEMPORARY_REDIRECT | &quot;TemporaryRedirect&quot; |
| PERMANENT_REDIRECT | &quot;PermanentRedirect&quot; |



