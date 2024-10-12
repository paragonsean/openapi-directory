# MerakiDashboardApi.UpdateNetworkApplianceSettingsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientTrackingMethod** | **String** | Client tracking method of a network | [optional] 
**deploymentMode** | **String** | Deployment mode of a network | [optional] 
**dynamicDns** | [**UpdateNetworkApplianceSettingsRequestDynamicDns**](UpdateNetworkApplianceSettingsRequestDynamicDns.md) |  | [optional] 



## Enum: ClientTrackingMethodEnum


* `IP address` (value: `"IP address"`)

* `MAC address` (value: `"MAC address"`)

* `Unique client identifier` (value: `"Unique client identifier"`)





## Enum: DeploymentModeEnum


* `passthrough` (value: `"passthrough"`)

* `routed` (value: `"routed"`)




