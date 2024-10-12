# RecoveryServicesClient.UpgradeDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTimeUtc** | **Date** | UTC time at which the upgrade operation has ended. | [optional] [readonly] 
**lastUpdatedTimeUtc** | **Date** | UTC time at which the upgrade operation status was last updated. | [optional] [readonly] 
**message** | **String** | Message to the user containing information about the upgrade operation. | [optional] [readonly] 
**operationId** | **String** | ID of the vault upgrade operation. | [optional] [readonly] 
**previousResourceId** | **String** | Resource ID of the vault before the upgrade. | [optional] [readonly] 
**startTimeUtc** | **Date** | UTC time at which the upgrade operation has started. | [optional] [readonly] 
**status** | **String** | Status of the vault upgrade operation. | [optional] [readonly] 
**triggerType** | **String** | The way the vault upgrade was triggered. | [optional] [readonly] 
**upgradedResourceId** | **String** | Resource ID of the upgraded vault. | [optional] [readonly] 



## Enum: StatusEnum


* `Unknown` (value: `"Unknown"`)

* `InProgress` (value: `"InProgress"`)

* `Upgraded` (value: `"Upgraded"`)

* `Failed` (value: `"Failed"`)





## Enum: TriggerTypeEnum


* `UserTriggered` (value: `"UserTriggered"`)

* `ForcedUpgrade` (value: `"ForcedUpgrade"`)




