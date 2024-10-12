

# Error


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorCode** | **String** | Unique numeric code that can be used for switching client behavior or to drive translated or customised error messages |  [optional] |
|**errorData** | [**ErrorData**](ErrorData.md) |  |  [optional] |
|**errorMessage** | **String** | English language message indicating the nature of the error |  [optional] |
|**localisationDetails** | [**LocalisationDetails**](LocalisationDetails.md) |  |  [optional] |
|**location** | **String** | the property or object that caused the error |  [optional] |
|**locationType** | [**LocationTypeEnum**](#LocationTypeEnum) | the location type in the request that was the cause of the error  |  [optional] |
|**reasonCode** | **String** | a camel-cased string that can be used by clients to localise client error messages (deprecated) |  [optional] |



## Enum: LocationTypeEnum

| Name | Value |
|---- | -----|
| REQUEST_BODY | &quot;requestBody&quot; |
| QUERY_PARAM | &quot;queryParam&quot; |
| REQUEST_PARAM | &quot;requestParam&quot; |
| HEADER | &quot;header&quot; |
| PATH_PARAM | &quot;pathParam&quot; |



