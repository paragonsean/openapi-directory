# VirtualWanasAServiceManagementClient.HubVirtualNetworkConnectionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowHubToRemoteVnetTransit** | **Boolean** | VirtualHub to RemoteVnet transit to enabled or not. | [optional] 
**allowRemoteVnetToUseHubVnetGateways** | **Boolean** | Allow RemoteVnet to use Virtual Hub&#39;s gateways. | [optional] 
**enableInternetSecurity** | **Boolean** | Enable internet security | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**remoteVirtualNetwork** | [**HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) |  | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




