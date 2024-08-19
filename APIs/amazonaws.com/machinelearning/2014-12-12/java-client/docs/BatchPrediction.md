

# BatchPrediction

<p> Represents the output of a <code>GetBatchPrediction</code> operation.</p> <p> The content consists of the detailed metadata, the status, and the data file information of a <code>Batch Prediction</code>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batchPredictionId** | [**String**](String.md) |  |  [optional] |
|**mlModelId** | [**String**](String.md) |  |  [optional] |
|**batchPredictionDataSourceId** | [**String**](String.md) |  |  [optional] |
|**inputDataLocationS3** | [**String**](String.md) |  |  [optional] |
|**createdByIamUser** | [**String**](String.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastUpdatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**status** | [**EntityStatus**](EntityStatus.md) |  |  [optional] |
|**outputUri** | [**String**](String.md) |  |  [optional] |
|**message** | [**String**](String.md) |  |  [optional] |
|**computeTime** | **Integer** | Long integer type that is a 64-bit signed number. |  [optional] |
|**finishedAt** | **OffsetDateTime** | A timestamp represented in epoch time. |  [optional] |
|**startedAt** | **OffsetDateTime** | A timestamp represented in epoch time. |  [optional] |
|**totalRecordCount** | **Integer** | Long integer type that is a 64-bit signed number. |  [optional] |
|**invalidRecordCount** | **Integer** | Long integer type that is a 64-bit signed number. |  [optional] |



