

# GetNetworkWirelessSettings200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ipv6BridgeEnabled** | **Boolean** | Toggle for enabling or disabling IPv6 bridging in a network (Note: if enabled, SSIDs must also be configured to use bridge mode) |  [optional] |
|**ledLightsOn** | **Boolean** | Toggle for enabling or disabling LED lights on all APs in the network (making them run dark) |  [optional] |
|**locationAnalyticsEnabled** | **Boolean** | Toggle for enabling or disabling location analytics for your network |  [optional] |
|**meshingEnabled** | **Boolean** | Toggle for enabling or disabling meshing in a network |  [optional] |
|**namedVlans** | [**GetNetworkWirelessSettings200ResponseNamedVlans**](GetNetworkWirelessSettings200ResponseNamedVlans.md) |  |  [optional] |
|**upgradeStrategy** | [**UpgradeStrategyEnum**](#UpgradeStrategyEnum) | The upgrade strategy to apply to the network. Must be one of &#39;minimizeUpgradeTime&#39; or &#39;minimizeClientDowntime&#39;. Requires firmware version MR 26.8 or higher&#39; |  [optional] |



## Enum: UpgradeStrategyEnum

| Name | Value |
|---- | -----|
| MINIMIZE_CLIENT_DOWNTIME | &quot;minimizeClientDowntime&quot; |
| MINIMIZE_UPGRADE_TIME | &quot;minimizeUpgradeTime&quot; |



