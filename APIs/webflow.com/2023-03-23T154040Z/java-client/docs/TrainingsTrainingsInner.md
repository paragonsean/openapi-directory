

# TrainingsTrainingsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdBy** | **String** |  |  |
|**createdTime** | **String** |  |  |
|**dataBundleIds** | **List&lt;String&gt;** |  |  |
|**dataScientistAssistance** | **Boolean** |  |  [optional] |
|**deploymentEnvironmentId** | **String** |  |  [optional] |
|**description** | **String** |  |  |
|**evaluation** | **Object** |  |  |
|**gpuHours** | **BigDecimal** |  |  |
|**instanceType** | [**InstanceTypeEnum**](#InstanceTypeEnum) |  |  |
|**metadata** | **Object** |  |  |
|**modelId** | **String** |  |  |
|**name** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**trainingId** | **String** |  |  |
|**updatedBy** | **String** |  |  |
|**updatedTime** | **String** |  |  |
|**warmStartConfig** | [**TrainingWarmStartConfig**](TrainingWarmStartConfig.md) |  |  [optional] |



## Enum: InstanceTypeEnum

| Name | Value |
|---- | -----|
| SMALL_GPU | &quot;small-gpu&quot; |
| MEDIUM_GPU | &quot;medium-gpu&quot; |
| LARGE_GPU | &quot;large-gpu&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| WAITING_FOR_APPROVAL | &quot;waiting-for-approval&quot; |
| PENDING | &quot;pending&quot; |
| RUNNING | &quot;running&quot; |
| SUCCEEDED | &quot;succeeded&quot; |
| FAILED | &quot;failed&quot; |
| CANCELLED | &quot;cancelled&quot; |



