

# AutoPoolSpecification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoPoolIdPrefix** | **String** | The Batch service assigns each auto Pool a unique identifier on creation. To distinguish between Pools created for different purposes, you can specify this element to add a prefix to the ID that is assigned. The prefix can be up to 20 characters long. |  [optional] |
|**keepAlive** | **Boolean** | If false, the Batch service deletes the Pool once its lifetime (as determined by the poolLifetimeOption setting) expires; that is, when the Job or Job Schedule completes. If true, the Batch service does not delete the Pool automatically. It is up to the user to delete auto Pools created with this option. |  [optional] |
|**pool** | [**PoolSpecification**](PoolSpecification.md) |  |  [optional] |
|**poolLifetimeOption** | [**PoolLifetimeOptionEnum**](#PoolLifetimeOptionEnum) |  |  |



## Enum: PoolLifetimeOptionEnum

| Name | Value |
|---- | -----|
| JOBSCHEDULE | &quot;jobschedule&quot; |
| JOB | &quot;job&quot; |



