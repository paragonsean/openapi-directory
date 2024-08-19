# VirtualMachineImageTemplate.ImageTemplateProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buildTimeoutInMinutes** | **Number** | Maximum duration to wait while building the image template. Omit or specify 0 to use the default (4 hours). | [optional] 
**customize** | [**[ImageTemplateCustomizer]**](ImageTemplateCustomizer.md) | Specifies the properties used to describe the customization steps of the image, like Image source etc | [optional] 
**distribute** | [**[ImageTemplateDistributor]**](ImageTemplateDistributor.md) | The distribution targets where the image output needs to go to. | 
**lastRunStatus** | [**ImageTemplateLastRunStatus**](ImageTemplateLastRunStatus.md) |  | [optional] 
**provisioningError** | [**ProvisioningError**](ProvisioningError.md) |  | [optional] 
**provisioningState** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 
**source** | [**ImageTemplateSource**](ImageTemplateSource.md) |  | 
**vmProfile** | [**ImageTemplateVmProfile**](ImageTemplateVmProfile.md) |  | [optional] 


