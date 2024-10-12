# DataflowApi.ExecutionStageSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**componentSource** | [**[ComponentSource]**](ComponentSource.md) | Collections produced and consumed by component transforms of this stage. | [optional] 
**componentTransform** | [**[ComponentTransform]**](ComponentTransform.md) | Transforms that comprise this execution stage. | [optional] 
**id** | **String** | Dataflow service generated id for this stage. | [optional] 
**inputSource** | [**[StageSource]**](StageSource.md) | Input sources for this stage. | [optional] 
**kind** | **String** | Type of transform this stage is executing. | [optional] 
**name** | **String** | Dataflow service generated name for this stage. | [optional] 
**outputSource** | [**[StageSource]**](StageSource.md) | Output sources for this stage. | [optional] 
**prerequisiteStage** | **[String]** | Other stages that must complete before this stage can run. | [optional] 



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




