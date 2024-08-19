

# BulkDownloadRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiLimit** | **Integer** |  |  [optional] |
|**continueFromJobId** | **Integer** |  |  [optional] |
|**docsHubDetails** | [**BulkDownloadRequestDocsHubDetails**](BulkDownloadRequestDocsHubDetails.md) |  |  [optional] |
|**filterDateField** | **String** |  |  [optional] |
|**filterNulls** | **Boolean** |  |  [optional] |
|**format** | [**FormatEnum**](#FormatEnum) |  |  |
|**from** | **OffsetDateTime** |  |  [optional] |
|**limit** | **Integer** |  |  [optional] |
|**notificationUrl** | **String** |  |  [optional] |
|**objectName** | **String** |  |  |
|**pageSize** | **Integer** |  |  [optional] |
|**query** | [**BulkDownloadRequestQuery**](BulkDownloadRequestQuery.md) |  |  [optional] |
|**selectFields** | **String** |  |  [optional] |
|**to** | **OffsetDateTime** |  |  [optional] |
|**where** | **String** |  |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| APPLICATION_JSON | &quot;application/json&quot; |
| TXT_CSV | &quot;txt/csv&quot; |
| APPLICATION_JSONL | &quot;application/jsonl&quot; |



