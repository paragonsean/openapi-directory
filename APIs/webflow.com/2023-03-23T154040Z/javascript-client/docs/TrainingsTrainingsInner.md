# LucidtechApi.TrainingsTrainingsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdBy** | **String** |  | 
**createdTime** | **String** |  | 
**dataBundleIds** | **[String]** |  | 
**dataScientistAssistance** | **Boolean** |  | [optional] 
**deploymentEnvironmentId** | **String** |  | [optional] 
**description** | **String** |  | 
**evaluation** | **Object** |  | 
**gpuHours** | **Number** |  | 
**instanceType** | **String** |  | 
**metadata** | **Object** |  | 
**modelId** | **String** |  | 
**name** | **String** |  | 
**status** | **String** |  | 
**trainingId** | **String** |  | 
**updatedBy** | **String** |  | 
**updatedTime** | **String** |  | 
**warmStartConfig** | [**TrainingWarmStartConfig**](TrainingWarmStartConfig.md) |  | [optional] 



## Enum: InstanceTypeEnum


* `small-gpu` (value: `"small-gpu"`)

* `medium-gpu` (value: `"medium-gpu"`)

* `large-gpu` (value: `"large-gpu"`)





## Enum: StatusEnum


* `waiting-for-approval` (value: `"waiting-for-approval"`)

* `pending` (value: `"pending"`)

* `running` (value: `"running"`)

* `succeeded` (value: `"succeeded"`)

* `failed` (value: `"failed"`)

* `cancelled` (value: `"cancelled"`)




