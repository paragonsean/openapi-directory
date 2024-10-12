

# HealthProbeSettingsUpdateParameters

L7 health probe settings for a backend pool

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**intervalInSeconds** | **Integer** | The number of seconds between health probes. |  [optional] |
|**path** | **String** | The path to use for the health probe. Default is / |  [optional] |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | Protocol scheme to use for this probe |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;Http&quot; |
| HTTPS | &quot;Https&quot; |



