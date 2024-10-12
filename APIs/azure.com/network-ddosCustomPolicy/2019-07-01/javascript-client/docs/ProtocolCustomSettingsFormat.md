# NetworkManagementClient.ProtocolCustomSettingsFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **String** | The protocol for which the DDoS protection policy is being customized. | [optional] 
**sourceRateOverride** | **String** | The customized DDoS protection source rate. | [optional] 
**triggerRateOverride** | **String** | The customized DDoS protection trigger rate. | [optional] 
**triggerSensitivityOverride** | **String** | The customized DDoS protection trigger rate sensitivity degrees. High: Trigger rate set with most sensitivity w.r.t. normal traffic. Default: Trigger rate set with moderate sensitivity w.r.t. normal traffic. Low: Trigger rate set with less sensitivity w.r.t. normal traffic. Relaxed: Trigger rate set with least sensitivity w.r.t. normal traffic. | [optional] 



## Enum: ProtocolEnum


* `Tcp` (value: `"Tcp"`)

* `Udp` (value: `"Udp"`)

* `Syn` (value: `"Syn"`)





## Enum: TriggerSensitivityOverrideEnum


* `Relaxed` (value: `"Relaxed"`)

* `Low` (value: `"Low"`)

* `Default` (value: `"Default"`)

* `High` (value: `"High"`)




