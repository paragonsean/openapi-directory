

# VirtualWanProperties

Parameters for VirtualWAN

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowBranchToBranchTraffic** | **Boolean** | True if branch to branch traffic is allowed. |  [optional] |
|**allowVnetToVnetTraffic** | **Boolean** | True if Vnet to Vnet traffic is allowed. |  [optional] |
|**disableVpnEncryption** | **Boolean** | Vpn encryption to be disabled or not. |  [optional] |
|**office365LocalBreakoutCategory** | **OfficeTrafficCategory** |  |  [optional] |
|**p2SVpnServerConfigurations** | [**List&lt;P2SVpnServerConfiguration&gt;**](P2SVpnServerConfiguration.md) | list of all P2SVpnServerConfigurations associated with the virtual wan. |  [optional] |
|**provisioningState** | **ProvisioningState** |  |  [optional] |
|**securityProviderName** | **String** | The Security Provider name. |  [optional] |
|**virtualHubs** | [**List&lt;HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork&gt;**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) | List of VirtualHubs in the VirtualWAN. |  [optional] [readonly] |
|**vpnSites** | [**List&lt;HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork&gt;**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) |  |  [optional] [readonly] |



