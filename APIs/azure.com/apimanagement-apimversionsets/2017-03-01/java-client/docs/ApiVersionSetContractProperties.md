

# ApiVersionSetContractProperties

Properties of an API Version Set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Name of API Version Set |  |
|**versioningScheme** | [**VersioningSchemeEnum**](#VersioningSchemeEnum) | An value that determines where the API Version identifer will be located in a HTTP request. |  |
|**description** | **String** | Description of API Version Set. |  [optional] |
|**versionHeaderName** | **String** | Name of HTTP header parameter that indicates the API Version if versioningScheme is set to &#x60;header&#x60;. |  [optional] |
|**versionQueryName** | **String** | Name of query parameter that indicates the API Version if versioningScheme is set to &#x60;query&#x60;. |  [optional] |



## Enum: VersioningSchemeEnum

| Name | Value |
|---- | -----|
| SEGMENT | &quot;Segment&quot; |
| QUERY | &quot;Query&quot; |
| HEADER | &quot;Header&quot; |



