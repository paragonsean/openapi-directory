

# VpnSiteLinkProperties

Parameters for VpnSite.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bgpProperties** | [**VpnLinkBgpSettings**](VpnLinkBgpSettings.md) |  |  [optional] |
|**ipAddress** | **String** | The ip-address for the vpn-site-link. |  [optional] |
|**linkProperties** | [**VpnLinkProviderProperties**](VpnLinkProviderProperties.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



