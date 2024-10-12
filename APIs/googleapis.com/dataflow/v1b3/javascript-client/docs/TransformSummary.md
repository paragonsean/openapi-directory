# DataflowApi.TransformSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayData** | [**[DisplayData]**](DisplayData.md) | Transform-specific display data. | [optional] 
**id** | **String** | SDK generated id of this transform instance. | [optional] 
**inputCollectionName** | **[String]** | User names for all collection inputs to this transform. | [optional] 
**kind** | **String** | Type of transform. | [optional] 
**name** | **String** | User provided name for this transform instance. | [optional] 
**outputCollectionName** | **[String]** | User names for all collection outputs to this transform. | [optional] 



## Enum: KindEnum


* `UNKNOWN_KIND` (value: `"UNKNOWN_KIND"`)

* `PAR_DO_KIND` (value: `"PAR_DO_KIND"`)

* `GROUP_BY_KEY_KIND` (value: `"GROUP_BY_KEY_KIND"`)

* `FLATTEN_KIND` (value: `"FLATTEN_KIND"`)

* `READ_KIND` (value: `"READ_KIND"`)

* `WRITE_KIND` (value: `"WRITE_KIND"`)

* `CONSTANT_KIND` (value: `"CONSTANT_KIND"`)

* `SINGLETON_KIND` (value: `"SINGLETON_KIND"`)

* `SHUFFLE_KIND` (value: `"SHUFFLE_KIND"`)




