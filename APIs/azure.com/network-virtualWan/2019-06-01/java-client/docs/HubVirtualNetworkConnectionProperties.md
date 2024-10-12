

# HubVirtualNetworkConnectionProperties

Parameters for HubVirtualNetworkConnection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowHubToRemoteVnetTransit** | **Boolean** | VirtualHub to RemoteVnet transit to enabled or not. |  [optional] |
|**allowRemoteVnetToUseHubVnetGateways** | **Boolean** | Allow RemoteVnet to use Virtual Hub&#39;s gateways. |  [optional] |
|**enableInternetSecurity** | **Boolean** | Enable internet security. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**remoteVirtualNetwork** | [**HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork**](HubVirtualNetworkConnectionPropertiesRemoteVirtualNetwork.md) |  |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



