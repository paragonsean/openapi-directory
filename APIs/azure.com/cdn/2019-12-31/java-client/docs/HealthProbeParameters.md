

# HealthProbeParameters

The JSON object that contains the properties to send health probes to origin.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**probeIntervalInSeconds** | **Integer** | The number of seconds between health probes.Default is 240sec. |  [optional] |
|**probePath** | **String** | The path relative to the origin that is used to determine the health of the origin. |  [optional] |
|**probeProtocol** | [**ProbeProtocolEnum**](#ProbeProtocolEnum) | Protocol to use for health probe. |  [optional] |
|**probeRequestType** | [**ProbeRequestTypeEnum**](#ProbeRequestTypeEnum) | The type of health probe request that is made. |  [optional] |



## Enum: ProbeProtocolEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| HTTP | &quot;Http&quot; |
| HTTPS | &quot;Https&quot; |



## Enum: ProbeRequestTypeEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| GET | &quot;GET&quot; |
| HEAD | &quot;HEAD&quot; |



