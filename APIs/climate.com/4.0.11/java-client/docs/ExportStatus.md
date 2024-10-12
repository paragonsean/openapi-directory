

# ExportStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checksum** | **String** | Base64 encoded MD5 hash of the export&#39;s contents. |  [optional] |
|**error** | **String** | Message indicating reason for validation failure. |  [optional] |
|**size** | **Long** | Size of the export&#39;s contents in bytes. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Current status of the export request:   * &#x60;PROCESSING&#x60; - Export request has been received by Climate and is being processed.   * &#x60;INVALID&#x60; - Export request has failed validity check.   * &#x60;EXPIRED&#x60; - Export contents have expired, and are no longer available for retrieval.   * &#x60;COMPLETED&#x60; - The export request has been successfully processed, and its contents are available for retrieval.   * &#x60;NO_DATA&#x60; - The export request completed successfully but generated no data.  |  |
|**xNextToken** | **String** | Token which may be used when executing an identical export in the future, but which only wants export data which was not previously exported. Assume a given field export request matches 12 fields today. And tomorrow it matches 15 fields. By passing the xNextToken in the definition section of tomorrow&#39;s field export request, only the 3 additional fields would be exported. Note, all other parameters passed in the definition section must be identical to the original request.  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PROCESSING | &quot;PROCESSING&quot; |
| INVALID | &quot;INVALID&quot; |
| EXPIRED | &quot;EXPIRED&quot; |
| COMPLETED | &quot;COMPLETED&quot; |
| NO_DATA | &quot;NO_DATA&quot; |



