# MerakiDashboardApi.CreateOrganizationAlertsProfileRequestAlertCondition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bitRateBps** | **Number** | The threshold the metric must cross to be valid for alerting. Used only for WAN Utilization alerts. | [optional] 
**duration** | **Number** | The total duration in seconds that the threshold should be crossed before alerting | [optional] 
**_interface** | **String** | The uplink observed for the alert.  interface must be one of the following: wan1, wan2, cellular | [optional] 
**jitterMs** | **Number** | The threshold the metric must cross to be valid for alerting. Used only for VoIP Jitter alerts. | [optional] 
**latencyMs** | **Number** | The threshold the metric must cross to be valid for alerting. Used only for WAN Latency alerts. | [optional] 
**lossRatio** | **Number** | The threshold the metric must cross to be valid for alerting. Used only for Packet Loss alerts. | [optional] 
**mos** | **Number** | The threshold the metric must drop below to be valid for alerting. Used only for VoIP MOS alerts. | [optional] 
**window** | **Number** | The look back period in seconds for sensing the alert | [optional] 



## Enum: InterfaceEnum


* `cellular` (value: `"cellular"`)

* `wan1` (value: `"wan1"`)

* `wan2` (value: `"wan2"`)




