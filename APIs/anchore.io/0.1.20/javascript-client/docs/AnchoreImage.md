# AnchoreEngineApiServer.AnchoreImage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysisStatus** | **String** | A state value for the current status of the analysis progress of the image | [optional] 
**annotations** | **Object** |  | [optional] 
**createdAt** | **Date** |  | [optional] 
**imageDigest** | **String** |  | [optional] 
**imageContent** | **Object** | A metadata content record for a specific image, containing different content type entries | [optional] 
**imageDetail** | [**[ImageDetail]**](ImageDetail.md) | Details specific to an image reference and type such as tag and image source | [optional] 
**imageStatus** | **String** | State of the image | [optional] 
**lastUpdated** | **Date** |  | [optional] 
**recordVersion** | **String** | The version of the record, used for internal schema updates and data migrations. | [optional] 
**userId** | **String** |  | [optional] 



## Enum: AnalysisStatusEnum


* `not_analyzed` (value: `"not_analyzed"`)

* `analyzing` (value: `"analyzing"`)

* `analyzed` (value: `"analyzed"`)

* `analysis_failed` (value: `"analysis_failed"`)





## Enum: ImageStatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)

* `disabled` (value: `"disabled"`)




