

# ApiListByService200ResponseValueInnerPropertiesApiVersionSet

An API Version Set contains the common configuration for a set of API Versions relating 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of API Version Set. |  [optional] |
|**id** | **String** | Identifier for existing API Version Set. Omit this value to create a new Version Set. |  [optional] |
|**name** | **String** | The display Name of the API Version Set. |  [optional] |
|**versionHeaderName** | **String** | Name of HTTP header parameter that indicates the API Version if versioningScheme is set to &#x60;header&#x60;. |  [optional] |
|**versionQueryName** | **String** | Name of query parameter that indicates the API Version if versioningScheme is set to &#x60;query&#x60;. |  [optional] |
|**versioningScheme** | [**VersioningSchemeEnum**](#VersioningSchemeEnum) | An value that determines where the API Version identifer will be located in a HTTP request. |  [optional] |



## Enum: VersioningSchemeEnum

| Name | Value |
|---- | -----|
| SEGMENT | &quot;Segment&quot; |
| QUERY | &quot;Query&quot; |
| HEADER | &quot;Header&quot; |



