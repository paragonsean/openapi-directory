

# GetLatestFeedVersionResponse

This element contains the response for a `/getLatestFeedVersion` request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**msg** | **String** | Description of the error, if the &#x60;status&#x60; value was not &#x60;OK&#x60;. |  [optional] |
|**results** | [**GetFeedVersionsResponseResults**](GetFeedVersionsResponseResults.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Indicates the success status of this request. The following values are possible:  * &#x60;OK&#x60; - Request was valid. * &#x60;DEPRECATED&#x60; - Request resolved to a deprecated resource which will not be returned. * &#x60;EMPTYKEY&#x60; - Request was missing API key. * &#x60;MISSINGINPUT&#x60; - A required request parameter was missing. * &#x60;INVALIDINPUT&#x60; - A request parameter was invalid. * &#x60;OTHER&#x60; - Some other error occurred.  |  [optional] |
|**ts** | **Integer** | Indicates the timestamp (in number of seconds since the epoch (January 1 1970 00:00:00 GMT). |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;OK&quot; |
| DEPRECATED | &quot;DEPRECATED&quot; |
| EMPTYKEY | &quot;EMPTYKEY&quot; |
| MISSINGINPUT | &quot;MISSINGINPUT&quot; |
| INVALIDINPUT | &quot;INVALIDINPUT&quot; |
| OTHER | &quot;OTHER&quot; |



