

# MLModel

<p> Represents the output of a <code>GetMLModel</code> operation. </p> <p>The content consists of the detailed metadata and the current status of the <code>MLModel</code>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mlModelId** | [**String**](String.md) |  |  [optional] |
|**trainingDataSourceId** | [**String**](String.md) |  |  [optional] |
|**createdByIamUser** | [**String**](String.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastUpdatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**status** | [**EntityStatus**](EntityStatus.md) |  |  [optional] |
|**sizeInBytes** | **Integer** | Long integer type that is a 64-bit signed number. |  [optional] |
|**endpointInfo** | [**MLModelEndpointInfo**](MLModelEndpointInfo.md) |  |  [optional] |
|**trainingParameters** | [**Map**](Map.md) |  |  [optional] |
|**inputDataLocationS3** | [**String**](String.md) |  |  [optional] |
|**algorithm** | [**Algorithm**](Algorithm.md) |  |  [optional] |
|**mlModelType** | [**MLModelType**](MLModelType.md) |  |  [optional] |
|**scoreThreshold** | **Float** |  |  [optional] |
|**scoreThresholdLastUpdatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**message** | [**String**](String.md) |  |  [optional] |
|**computeTime** | **Integer** | Long integer type that is a 64-bit signed number. |  [optional] |
|**finishedAt** | **OffsetDateTime** | A timestamp represented in epoch time. |  [optional] |
|**startedAt** | **OffsetDateTime** | A timestamp represented in epoch time. |  [optional] |



