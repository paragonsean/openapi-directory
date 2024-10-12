# AwsLicenseManagerLinuxSubscriptions.UpdateServiceSettingsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowUpdate** | **Boolean** | Describes if updates are allowed to the service settings for Linux subscriptions. If you allow updates, you can aggregate Linux subscription data in more than one home Region. | [optional] 
**linuxSubscriptionsDiscovery** | **String** | Describes if the discovery of Linux subscriptions is enabled. | 
**linuxSubscriptionsDiscoverySettings** | [**UpdateServiceSettingsRequestLinuxSubscriptionsDiscoverySettings**](UpdateServiceSettingsRequestLinuxSubscriptionsDiscoverySettings.md) |  | 



## Enum: LinuxSubscriptionsDiscoveryEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




