

# AnchoreImage

A unique image in the engine. May have multiple tags or references. Unique to an image content across registries or repositories.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analysisStatus** | [**AnalysisStatusEnum**](#AnalysisStatusEnum) | A state value for the current status of the analysis progress of the image |  [optional] |
|**annotations** | **Object** |  |  [optional] |
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**imageDigest** | **String** |  |  [optional] |
|**imageContent** | **Object** | A metadata content record for a specific image, containing different content type entries |  [optional] |
|**imageDetail** | [**List&lt;ImageDetail&gt;**](ImageDetail.md) | Details specific to an image reference and type such as tag and image source |  [optional] |
|**imageStatus** | [**ImageStatusEnum**](#ImageStatusEnum) | State of the image |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] |
|**recordVersion** | **String** | The version of the record, used for internal schema updates and data migrations. |  [optional] |
|**userId** | **String** |  |  [optional] |



## Enum: AnalysisStatusEnum

| Name | Value |
|---- | -----|
| NOT_ANALYZED | &quot;not_analyzed&quot; |
| ANALYZING | &quot;analyzing&quot; |
| ANALYZED | &quot;analyzed&quot; |
| ANALYSIS_FAILED | &quot;analysis_failed&quot; |



## Enum: ImageStatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| INACTIVE | &quot;inactive&quot; |
| DISABLED | &quot;disabled&quot; |



