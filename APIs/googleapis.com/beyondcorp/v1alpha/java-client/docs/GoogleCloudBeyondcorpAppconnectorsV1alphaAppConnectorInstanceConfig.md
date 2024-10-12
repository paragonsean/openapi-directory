

# GoogleCloudBeyondcorpAppconnectorsV1alphaAppConnectorInstanceConfig

AppConnectorInstanceConfig defines the instance config of a AppConnector.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**imageConfig** | [**GoogleCloudBeyondcorpAppconnectorsV1alphaImageConfig**](GoogleCloudBeyondcorpAppconnectorsV1alphaImageConfig.md) |  |  [optional] |
|**instanceConfig** | **Map&lt;String, Object&gt;** | The SLM instance agent configuration. |  [optional] |
|**notificationConfig** | [**GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfig**](GoogleCloudBeyondcorpAppconnectorsV1alphaNotificationConfig.md) |  |  [optional] |
|**sequenceNumber** | **String** | Required. A monotonically increasing number generated and maintained by the API provider. Every time a config changes in the backend, the sequenceNumber should be bumped up to reflect the change. |  [optional] |



