

# DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner

Worker pool of an App Service Environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**computeMode** | [**ComputeModeEnum**](#ComputeModeEnum) | Shared or dedicated app hosting. |  [optional] |
|**instanceNames** | **List&lt;String&gt;** | Names of all instances in the worker pool (read only). |  [optional] [readonly] |
|**workerCount** | **Integer** | Number of instances in the worker pool. |  [optional] |
|**workerSize** | **String** | VM size of the worker pool instances. |  [optional] |
|**workerSizeId** | **Integer** | Worker size ID for referencing this worker pool. |  [optional] |



## Enum: ComputeModeEnum

| Name | Value |
|---- | -----|
| SHARED | &quot;Shared&quot; |
| DEDICATED | &quot;Dedicated&quot; |
| DYNAMIC | &quot;Dynamic&quot; |



