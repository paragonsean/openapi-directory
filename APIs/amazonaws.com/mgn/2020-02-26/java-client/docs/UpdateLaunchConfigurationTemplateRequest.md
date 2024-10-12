

# UpdateLaunchConfigurationTemplateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**associatePublicIpAddress** | **Boolean** | Associate public Ip address. |  [optional] |
|**bootMode** | [**BootModeEnum**](#BootModeEnum) | Launch configuration template boot mode. |  [optional] |
|**copyPrivateIp** | **Boolean** | Copy private Ip. |  [optional] |
|**copyTags** | **Boolean** | Copy tags. |  [optional] |
|**enableMapAutoTagging** | **Boolean** | Enable map auto tagging. |  [optional] |
|**largeVolumeConf** | [**CreateLaunchConfigurationTemplateRequestLargeVolumeConf**](CreateLaunchConfigurationTemplateRequestLargeVolumeConf.md) |  |  [optional] |
|**launchConfigurationTemplateID** | **String** | Launch Configuration Template ID. |  |
|**launchDisposition** | [**LaunchDispositionEnum**](#LaunchDispositionEnum) | Launch disposition. |  [optional] |
|**licensing** | [**CreateLaunchConfigurationTemplateRequestLicensing**](CreateLaunchConfigurationTemplateRequestLicensing.md) |  |  [optional] |
|**mapAutoTaggingMpeID** | **String** | Launch configuration template map auto tagging MPE ID. |  [optional] |
|**postLaunchActions** | [**CreateLaunchConfigurationTemplateRequestPostLaunchActions**](CreateLaunchConfigurationTemplateRequestPostLaunchActions.md) |  |  [optional] |
|**smallVolumeConf** | [**CreateLaunchConfigurationTemplateRequestLargeVolumeConf**](CreateLaunchConfigurationTemplateRequestLargeVolumeConf.md) |  |  [optional] |
|**smallVolumeMaxSize** | **Integer** | Small volume maximum size. |  [optional] |
|**targetInstanceTypeRightSizingMethod** | [**TargetInstanceTypeRightSizingMethodEnum**](#TargetInstanceTypeRightSizingMethodEnum) | Target instance type right-sizing method. |  [optional] |



## Enum: BootModeEnum

| Name | Value |
|---- | -----|
| LEGACY_BIOS | &quot;LEGACY_BIOS&quot; |
| UEFI | &quot;UEFI&quot; |



## Enum: LaunchDispositionEnum

| Name | Value |
|---- | -----|
| STOPPED | &quot;STOPPED&quot; |
| STARTED | &quot;STARTED&quot; |



## Enum: TargetInstanceTypeRightSizingMethodEnum

| Name | Value |
|---- | -----|
| NONE | &quot;NONE&quot; |
| BASIC | &quot;BASIC&quot; |



