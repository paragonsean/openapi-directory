# ConnectorsApi.Provider

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. Created time. | [optional] [readonly] 
**description** | **String** | Output only. Description of the resource. | [optional] [readonly] 
**displayName** | **String** | Output only. Display name. | [optional] [readonly] 
**documentationUri** | **String** | Output only. Link to documentation page. | [optional] [readonly] 
**externalUri** | **String** | Output only. Link to external page. | [optional] [readonly] 
**labels** | **{String: String}** | Output only. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources | [optional] [readonly] 
**launchStage** | **String** | Output only. Flag to mark the version indicating the launch stage. | [optional] [readonly] 
**name** | **String** | Output only. Resource name of the Provider. Format: projects/{project}/locations/{location}/providers/{provider} Only global location is supported for Provider resource. | [optional] [readonly] 
**updateTime** | **String** | Output only. Updated time. | [optional] [readonly] 
**webAssetsLocation** | **String** | Output only. Cloud storage location of icons etc consumed by UI. | [optional] [readonly] 



## Enum: LaunchStageEnum


* `LAUNCH_STAGE_UNSPECIFIED` (value: `"LAUNCH_STAGE_UNSPECIFIED"`)

* `PREVIEW` (value: `"PREVIEW"`)

* `GA` (value: `"GA"`)

* `DEPRECATED` (value: `"DEPRECATED"`)

* `PRIVATE_PREVIEW` (value: `"PRIVATE_PREVIEW"`)




