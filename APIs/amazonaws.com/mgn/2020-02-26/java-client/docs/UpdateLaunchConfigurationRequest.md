

# UpdateLaunchConfigurationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountID** | **String** | Update Launch configuration Account ID. |  [optional] |
|**bootMode** | [**BootModeEnum**](#BootModeEnum) | Update Launch configuration boot mode request. |  [optional] |
|**copyPrivateIp** | **Boolean** | Update Launch configuration copy Private IP request. |  [optional] |
|**copyTags** | **Boolean** | Update Launch configuration copy Tags request. |  [optional] |
|**enableMapAutoTagging** | **Boolean** | Enable map auto tagging. |  [optional] |
|**launchDisposition** | [**LaunchDispositionEnum**](#LaunchDispositionEnum) | Update Launch configuration launch disposition request. |  [optional] |
|**licensing** | [**CreateLaunchConfigurationTemplateRequestLicensing**](CreateLaunchConfigurationTemplateRequestLicensing.md) |  |  [optional] |
|**mapAutoTaggingMpeID** | **String** | Launch configuration map auto tagging MPE ID. |  [optional] |
|**name** | **String** | Update Launch configuration name request. |  [optional] |
|**postLaunchActions** | [**CreateLaunchConfigurationTemplateRequestPostLaunchActions**](CreateLaunchConfigurationTemplateRequestPostLaunchActions.md) |  |  [optional] |
|**sourceServerID** | **String** | Update Launch configuration by Source Server ID request. |  |
|**targetInstanceTypeRightSizingMethod** | [**TargetInstanceTypeRightSizingMethodEnum**](#TargetInstanceTypeRightSizingMethodEnum) | Update Launch configuration Target instance right sizing request. |  [optional] |



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



