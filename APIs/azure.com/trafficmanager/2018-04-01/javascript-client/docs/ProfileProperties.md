# TrafficManagerManagementClient.ProfileProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dnsConfig** | [**DnsConfig**](DnsConfig.md) |  | [optional] 
**endpoints** | [**[Endpoint]**](Endpoint.md) | The list of endpoints in the Traffic Manager profile. | [optional] 
**maxReturn** | **Number** | Maximum number of endpoints to be returned for MultiValue routing type. | [optional] 
**monitorConfig** | [**MonitorConfig**](MonitorConfig.md) |  | [optional] 
**profileStatus** | **String** | The status of the Traffic Manager profile. | [optional] 
**trafficRoutingMethod** | **String** | The traffic routing method of the Traffic Manager profile. | [optional] 
**trafficViewEnrollmentStatus** | **String** | Indicates whether Traffic View is &#39;Enabled&#39; or &#39;Disabled&#39; for the Traffic Manager profile. Null, indicates &#39;Disabled&#39;. Enabling this feature will increase the cost of the Traffic Manage profile. | [optional] 



## Enum: ProfileStatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: TrafficRoutingMethodEnum


* `Performance` (value: `"Performance"`)

* `Priority` (value: `"Priority"`)

* `Weighted` (value: `"Weighted"`)

* `Geographic` (value: `"Geographic"`)

* `MultiValue` (value: `"MultiValue"`)

* `Subnet` (value: `"Subnet"`)





## Enum: TrafficViewEnrollmentStatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




