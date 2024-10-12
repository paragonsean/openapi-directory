# DockerHubApi.PostNamespacesDeleteImagesResponseErrorErrinfoAllOfDetailsWarningsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest** | **String** | Digest of the image that caused the warning. | [optional] 
**repository** | **String** | Name of the repository of the image that caused the warning. | [optional] 
**tags** | **[String]** | Current tags if warning is &#x60;current_tag&#x60;. | [optional] 
**warning** | **String** | Warning type. | [optional] 



## Enum: WarningEnum


* `is_active` (value: `"is_active"`)

* `current_tag` (value: `"current_tag"`)




