

# HealthProbeSettingsUpdateParameters

L7 health probe settings for a backend pool

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabledState** | [**EnabledStateEnum**](#EnabledStateEnum) | Whether to enable health probes to be made against backends defined under backendPools. Health probes can only be disabled if there is a single enabled backend in single enabled backend pool. |  [optional] |
|**healthProbeMethod** | [**HealthProbeMethodEnum**](#HealthProbeMethodEnum) | Configures which HTTP method to use to probe the backends defined under backendPools. |  [optional] |
|**intervalInSeconds** | **Integer** | The number of seconds between health probes. |  [optional] |
|**path** | **String** | The path to use for the health probe. Default is / |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Protocol scheme to use for this probe |  [optional] |



## Enum: EnabledStateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: HealthProbeMethodEnum

| Name | Value |
|---- | -----|
| GET | &quot;GET&quot; |
| HEAD | &quot;HEAD&quot; |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;Http&quot; |
| HTTPS | &quot;Https&quot; |



