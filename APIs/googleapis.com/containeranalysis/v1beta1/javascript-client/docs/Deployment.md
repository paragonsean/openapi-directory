# ContainerAnalysisApi.Deployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | Address of the runtime element hosting this deployment. | [optional] 
**config** | **String** | Configuration used to create this deployment. | [optional] 
**deployTime** | **String** | Required. Beginning of the lifetime of this deployment. | [optional] 
**platform** | **String** | Platform hosting this deployment. | [optional] 
**resourceUri** | **[String]** | Output only. Resource URI for the artifact being deployed taken from the deployable field with the same name. | [optional] 
**undeployTime** | **String** | End of the lifetime of this deployment. | [optional] 
**userEmail** | **String** | Identity of the user that triggered this deployment. | [optional] 



## Enum: PlatformEnum


* `PLATFORM_UNSPECIFIED` (value: `"PLATFORM_UNSPECIFIED"`)

* `GKE` (value: `"GKE"`)

* `FLEX` (value: `"FLEX"`)

* `CUSTOM` (value: `"CUSTOM"`)




