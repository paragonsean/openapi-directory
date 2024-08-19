

# FormDocumentReport


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentName** | **String** | Reference to the data that the report is for. |  [optional] |
|**errors** | **List&lt;String&gt;** | List of errors per page. |  [optional] |
|**pages** | **Integer** | Total number of pages trained on. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the training operation. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| PARTIAL_SUCCESS | &quot;partialSuccess&quot; |
| FAILURE | &quot;failure&quot; |



