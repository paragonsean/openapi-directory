

# CreateDataFlowDebugSessionRequest

Request body structure for creating data flow debug session.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**computeType** | **String** | Compute type of the cluster. The value will be overwritten by the same setting in integration runtime if provided. |  [optional] |
|**coreCount** | **Integer** | Core count of the cluster. The value will be overwritten by the same setting in integration runtime if provided. |  [optional] |
|**integrationRuntime** | [**IntegrationRuntimeDebugResource**](IntegrationRuntimeDebugResource.md) |  |  [optional] |
|**timeToLive** | **Integer** | Time to live setting of the cluster in minutes. |  [optional] |



