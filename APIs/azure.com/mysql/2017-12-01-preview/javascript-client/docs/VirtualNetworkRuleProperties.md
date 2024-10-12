# MySqlManagementClient.VirtualNetworkRuleProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignoreMissingVnetServiceEndpoint** | **Boolean** | Create firewall rule before the virtual network has vnet service endpoint enabled. | [optional] 
**state** | **String** | Virtual Network Rule State | [optional] [readonly] 
**virtualNetworkSubnetId** | **String** | The ARM resource id of the virtual network subnet. | 



## Enum: StateEnum


* `Initializing` (value: `"Initializing"`)

* `InProgress` (value: `"InProgress"`)

* `Ready` (value: `"Ready"`)

* `Deleting` (value: `"Deleting"`)

* `Unknown` (value: `"Unknown"`)




