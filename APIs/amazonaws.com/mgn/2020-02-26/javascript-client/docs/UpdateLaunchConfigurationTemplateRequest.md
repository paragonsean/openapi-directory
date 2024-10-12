# ApplicationMigrationService.UpdateLaunchConfigurationTemplateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associatePublicIpAddress** | **Boolean** | Associate public Ip address. | [optional] 
**bootMode** | **String** | Launch configuration template boot mode. | [optional] 
**copyPrivateIp** | **Boolean** | Copy private Ip. | [optional] 
**copyTags** | **Boolean** | Copy tags. | [optional] 
**enableMapAutoTagging** | **Boolean** | Enable map auto tagging. | [optional] 
**largeVolumeConf** | [**CreateLaunchConfigurationTemplateRequestLargeVolumeConf**](CreateLaunchConfigurationTemplateRequestLargeVolumeConf.md) |  | [optional] 
**launchConfigurationTemplateID** | **String** | Launch Configuration Template ID. | 
**launchDisposition** | **String** | Launch disposition. | [optional] 
**licensing** | [**CreateLaunchConfigurationTemplateRequestLicensing**](CreateLaunchConfigurationTemplateRequestLicensing.md) |  | [optional] 
**mapAutoTaggingMpeID** | **String** | Launch configuration template map auto tagging MPE ID. | [optional] 
**postLaunchActions** | [**CreateLaunchConfigurationTemplateRequestPostLaunchActions**](CreateLaunchConfigurationTemplateRequestPostLaunchActions.md) |  | [optional] 
**smallVolumeConf** | [**CreateLaunchConfigurationTemplateRequestLargeVolumeConf**](CreateLaunchConfigurationTemplateRequestLargeVolumeConf.md) |  | [optional] 
**smallVolumeMaxSize** | **Number** | Small volume maximum size. | [optional] 
**targetInstanceTypeRightSizingMethod** | **String** | Target instance type right-sizing method. | [optional] 



## Enum: BootModeEnum


* `LEGACY_BIOS` (value: `"LEGACY_BIOS"`)

* `UEFI` (value: `"UEFI"`)





## Enum: LaunchDispositionEnum


* `STOPPED` (value: `"STOPPED"`)

* `STARTED` (value: `"STARTED"`)





## Enum: TargetInstanceTypeRightSizingMethodEnum


* `NONE` (value: `"NONE"`)

* `BASIC` (value: `"BASIC"`)




