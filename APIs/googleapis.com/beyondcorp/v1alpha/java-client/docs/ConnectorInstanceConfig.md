

# ConnectorInstanceConfig

ConnectorInstanceConfig defines the instance config of a connector.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**imageConfig** | [**ImageConfig**](ImageConfig.md) |  |  [optional] |
|**instanceConfig** | **Map&lt;String, Object&gt;** | The SLM instance agent configuration. |  [optional] |
|**notificationConfig** | [**NotificationConfig**](NotificationConfig.md) |  |  [optional] |
|**sequenceNumber** | **String** | Required. A monotonically increasing number generated and maintained by the API provider. Every time a config changes in the backend, the sequenceNumber should be bumped up to reflect the change. |  [optional] |



