

# CreateNodeFromTemplateJobRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobTags** | [**List&lt;JobResourceTags&gt;**](JobResourceTags.md) | Tags for the job. |  [optional] |
|**nodeDescription** | **String** | A description for the node. |  [optional] |
|**nodeName** | **String** | A name for the node. |  |
|**outputPackageName** | **String** | An output package name for the node. |  |
|**outputPackageVersion** | **String** | An output package version for the node. |  |
|**templateParameters** | **Map&lt;String, String&gt;** | Template parameters for the node. |  |
|**templateType** | [**TemplateTypeEnum**](#TemplateTypeEnum) | The type of node. |  |



## Enum: TemplateTypeEnum

| Name | Value |
|---- | -----|
| RTSP_CAMERA_STREAM | &quot;RTSP_CAMERA_STREAM&quot; |



