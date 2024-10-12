# TrafficManagerManagementClient.ProfileProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsConfig** | [**DnsConfig**](DnsConfig.md) |  | [optional] 
**endpoints** | [**[Endpoint]**](Endpoint.md) | The list of endpoints in the Traffic Manager profile. | [optional] 
**monitorConfig** | [**MonitorConfig**](MonitorConfig.md) |  | [optional] 
**profileStatus** | **String** | The status of the Traffic Manager profile. | [optional] 
**trafficRoutingMethod** | **String** | The traffic routing method of the Traffic Manager profile. | [optional] 



## Enum: ProfileStatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: TrafficRoutingMethodEnum


* `Performance` (value: `"Performance"`)

* `Priority` (value: `"Priority"`)

* `Weighted` (value: `"Weighted"`)

* `Geographic` (value: `"Geographic"`)




