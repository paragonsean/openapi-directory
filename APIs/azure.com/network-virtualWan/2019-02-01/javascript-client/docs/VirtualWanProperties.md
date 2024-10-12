# VirtualWanasAServiceManagementClient.VirtualWanProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowBranchToBranchTraffic** | **Boolean** | True if branch to branch traffic is allowed. | [optional] 
**allowVnetToVnetTraffic** | **Boolean** | True if Vnet to Vnet traffic is allowed. | [optional] 
**disableVpnEncryption** | **Boolean** | Vpn encryption to be disabled or not. | [optional] 
**office365LocalBreakoutCategory** | [**OfficeTrafficCategory**](OfficeTrafficCategory.md) |  | [optional] 
**p2SVpnServerConfigurations** | [**[P2SVpnServerConfiguration]**](P2SVpnServerConfiguration.md) | List of all P2SVpnServerConfigurations associated with the virtual wan. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**securityProviderName** | **String** | The Security Provider name. | [optional] 
**virtualHubs** | [**[HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork]**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) | List of VirtualHubs in the VirtualWAN. | [optional] [readonly] 
**vpnSites** | [**[HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork]**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) | List of VpnSites in the VirtualWAN. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




