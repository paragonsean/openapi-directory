

# ImportTask

An array of information related to the import task request that includes status information, times, IDs, the Amazon S3 Object URL for the import file, and more.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**importTaskId** | [**String**](String.md) |  |  [optional] |
|**clientRequestToken** | [**String**](String.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**importUrl** | [**String**](String.md) |  |  [optional] |
|**status** | [**ImportStatus**](ImportStatus.md) |  |  [optional] |
|**importRequestTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**importCompletionTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**importDeletedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**serverImportSuccess** | [**Integer**](Integer.md) |  |  [optional] |
|**serverImportFailure** | [**Integer**](Integer.md) |  |  [optional] |
|**applicationImportSuccess** | [**Integer**](Integer.md) |  |  [optional] |
|**applicationImportFailure** | [**Integer**](Integer.md) |  |  [optional] |
|**errorsAndFailedEntriesZip** | [**String**](String.md) |  |  [optional] |



