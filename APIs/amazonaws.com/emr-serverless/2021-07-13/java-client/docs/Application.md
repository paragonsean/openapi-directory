

# Application

Information about an application. Amazon EMR Serverless uses applications to run jobs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationId** | [**String**](String.md) |  |  |
|**name** | [**String**](String.md) |  |  [optional] |
|**arn** | [**String**](String.md) |  |  |
|**releaseLabel** | [**String**](String.md) |  |  |
|**type** | [**String**](String.md) |  |  |
|**state** | [**ApplicationState**](ApplicationState.md) |  |  |
|**stateDetails** | [**String**](String.md) |  |  [optional] |
|**initialCapacity** | [**Map**](Map.md) |  |  [optional] |
|**maximumCapacity** | [**ApplicationMaximumCapacity**](ApplicationMaximumCapacity.md) |  |  [optional] |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**updatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**tags** | [**Map**](Map.md) |  |  [optional] |
|**autoStartConfiguration** | [**ApplicationAutoStartConfiguration**](ApplicationAutoStartConfiguration.md) |  |  [optional] |
|**autoStopConfiguration** | [**ApplicationAutoStopConfiguration**](ApplicationAutoStopConfiguration.md) |  |  [optional] |
|**networkConfiguration** | [**ApplicationNetworkConfiguration**](ApplicationNetworkConfiguration.md) |  |  [optional] |
|**architecture** | [**Architecture**](Architecture.md) |  |  [optional] |
|**imageConfiguration** | [**ApplicationImageConfiguration**](ApplicationImageConfiguration.md) |  |  [optional] |
|**workerTypeSpecifications** | [**Map**](Map.md) |  |  [optional] |



