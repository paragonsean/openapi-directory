

# CreateOrganizationAlertsProfileRequestAlertCondition

The conditions that determine if the alert triggers

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bitRateBps** | **Integer** | The threshold the metric must cross to be valid for alerting. Used only for WAN Utilization alerts. |  [optional] |
|**duration** | **Integer** | The total duration in seconds that the threshold should be crossed before alerting |  [optional] |
|**_interface** | [**InterfaceEnum**](#InterfaceEnum) | The uplink observed for the alert.  interface must be one of the following: wan1, wan2, cellular |  [optional] |
|**jitterMs** | **Integer** | The threshold the metric must cross to be valid for alerting. Used only for VoIP Jitter alerts. |  [optional] |
|**latencyMs** | **Integer** | The threshold the metric must cross to be valid for alerting. Used only for WAN Latency alerts. |  [optional] |
|**lossRatio** | **Float** | The threshold the metric must cross to be valid for alerting. Used only for Packet Loss alerts. |  [optional] |
|**mos** | **Float** | The threshold the metric must drop below to be valid for alerting. Used only for VoIP MOS alerts. |  [optional] |
|**window** | **Integer** | The look back period in seconds for sensing the alert |  [optional] |



## Enum: InterfaceEnum

| Name | Value |
|---- | -----|
| CELLULAR | &quot;cellular&quot; |
| WAN1 | &quot;wan1&quot; |
| WAN2 | &quot;wan2&quot; |



