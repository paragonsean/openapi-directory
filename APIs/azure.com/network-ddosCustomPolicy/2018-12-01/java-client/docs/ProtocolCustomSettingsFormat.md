

# ProtocolCustomSettingsFormat

DDoS custom policy properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | The protocol for which the DDoS protection policy is being customized. |  [optional] |
|**sourceRateOverride** | **String** | The customized DDoS protection source rate. |  [optional] |
|**triggerRateOverride** | **String** | The customized DDoS protection trigger rate. |  [optional] |
|**triggerSensitivityOverride** | [**TriggerSensitivityOverrideEnum**](#TriggerSensitivityOverrideEnum) | The customized DDoS protection trigger rate sensitivity degrees. High: Trigger rate set with most sensitivity w.r.t. normal traffic. Default: Trigger rate set with moderate sensitivity w.r.t. normal traffic. Low: Trigger rate set with less sensitivity w.r.t. normal traffic. Relaxed: Trigger rate set with least sensitivity w.r.t. normal traffic. |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| TCP | &quot;Tcp&quot; |
| UDP | &quot;Udp&quot; |
| SYN | &quot;Syn&quot; |



## Enum: TriggerSensitivityOverrideEnum

| Name | Value |
|---- | -----|
| RELAXED | &quot;Relaxed&quot; |
| LOW | &quot;Low&quot; |
| DEFAULT | &quot;Default&quot; |
| HIGH | &quot;High&quot; |



