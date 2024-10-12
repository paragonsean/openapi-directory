

# ReleasesUpdateDetails400Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) |  |  |
|**message** | **String** |  |  |
|**destinations** | [**List&lt;ReleasesUpdateDetails400ResponseAllOfDestinationsInner&gt;**](ReleasesUpdateDetails400ResponseAllOfDestinationsInner.md) |  |  [optional] |
|**mandatoryUpdate** | **Boolean** |  |  [optional] |
|**releaseNotes** | **String** |  |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| BAD_REQUEST | &quot;BadRequest&quot; |
| CONFLICT | &quot;Conflict&quot; |
| NOT_ACCEPTABLE | &quot;NotAcceptable&quot; |
| NOT_FOUND | &quot;NotFound&quot; |
| INTERNAL_SERVER_ERROR | &quot;InternalServerError&quot; |
| UNAUTHORIZED | &quot;Unauthorized&quot; |
| TOO_MANY_REQUESTS | &quot;TooManyRequests&quot; |



