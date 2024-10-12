

# FleetObservabilityFleetObservabilityBaseFeatureState

Base state for fleet observability feature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | The high-level, machine-readable status of this Feature. |  [optional] |
|**errors** | [**List&lt;FleetObservabilityFeatureError&gt;**](FleetObservabilityFeatureError.md) | Errors after reconciling the monitoring and logging feature if the code is not OK. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| CODE_UNSPECIFIED | &quot;CODE_UNSPECIFIED&quot; |
| OK | &quot;OK&quot; |
| ERROR | &quot;ERROR&quot; |



