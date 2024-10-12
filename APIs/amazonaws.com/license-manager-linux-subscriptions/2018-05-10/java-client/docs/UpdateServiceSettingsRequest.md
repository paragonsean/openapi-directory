

# UpdateServiceSettingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowUpdate** | **Boolean** | Describes if updates are allowed to the service settings for Linux subscriptions. If you allow updates, you can aggregate Linux subscription data in more than one home Region. |  [optional] |
|**linuxSubscriptionsDiscovery** | [**LinuxSubscriptionsDiscoveryEnum**](#LinuxSubscriptionsDiscoveryEnum) | Describes if the discovery of Linux subscriptions is enabled. |  |
|**linuxSubscriptionsDiscoverySettings** | [**UpdateServiceSettingsRequestLinuxSubscriptionsDiscoverySettings**](UpdateServiceSettingsRequestLinuxSubscriptionsDiscoverySettings.md) |  |  |



## Enum: LinuxSubscriptionsDiscoveryEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



