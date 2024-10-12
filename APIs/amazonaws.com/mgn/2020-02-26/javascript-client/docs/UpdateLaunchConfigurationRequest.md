# ApplicationMigrationService.UpdateLaunchConfigurationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountID** | **String** | Update Launch configuration Account ID. | [optional] 
**bootMode** | **String** | Update Launch configuration boot mode request. | [optional] 
**copyPrivateIp** | **Boolean** | Update Launch configuration copy Private IP request. | [optional] 
**copyTags** | **Boolean** | Update Launch configuration copy Tags request. | [optional] 
**enableMapAutoTagging** | **Boolean** | Enable map auto tagging. | [optional] 
**launchDisposition** | **String** | Update Launch configuration launch disposition request. | [optional] 
**licensing** | [**CreateLaunchConfigurationTemplateRequestLicensing**](CreateLaunchConfigurationTemplateRequestLicensing.md) |  | [optional] 
**mapAutoTaggingMpeID** | **String** | Launch configuration map auto tagging MPE ID. | [optional] 
**name** | **String** | Update Launch configuration name request. | [optional] 
**postLaunchActions** | [**CreateLaunchConfigurationTemplateRequestPostLaunchActions**](CreateLaunchConfigurationTemplateRequestPostLaunchActions.md) |  | [optional] 
**sourceServerID** | **String** | Update Launch configuration by Source Server ID request. | 
**targetInstanceTypeRightSizingMethod** | **String** | Update Launch configuration Target instance right sizing request. | [optional] 



## Enum: BootModeEnum


* `LEGACY_BIOS` (value: `"LEGACY_BIOS"`)

* `UEFI` (value: `"UEFI"`)





## Enum: LaunchDispositionEnum


* `STOPPED` (value: `"STOPPED"`)

* `STARTED` (value: `"STARTED"`)





## Enum: TargetInstanceTypeRightSizingMethodEnum


* `NONE` (value: `"NONE"`)

* `BASIC` (value: `"BASIC"`)




