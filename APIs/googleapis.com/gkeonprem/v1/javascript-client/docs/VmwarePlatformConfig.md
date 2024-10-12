# AnthosOnPremApi.VmwarePlatformConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundles** | [**[VmwareBundleConfig]**](VmwareBundleConfig.md) | Output only. The list of bundles installed in the admin cluster. | [optional] [readonly] 
**platformVersion** | **String** | Output only. The platform version e.g. 1.13.2. | [optional] [readonly] 
**requiredPlatformVersion** | **String** | Input only. The required platform version e.g. 1.13.1. If the current platform version is lower than the target version, the platform version will be updated to the target version. If the target version is not installed in the platform (bundle versions), download the target version bundle. | [optional] 
**status** | [**ResourceStatus**](ResourceStatus.md) |  | [optional] 


