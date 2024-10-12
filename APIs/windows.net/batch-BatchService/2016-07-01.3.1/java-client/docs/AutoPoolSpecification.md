

# AutoPoolSpecification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoPoolIdPrefix** | **String** | The Batch service assigns each auto pool a unique identifier on creation. To distinguish between pools created for different purposes, you can specify this element to add a prefix to the id that is assigned. The prefix can be up to 20 characters long. |  [optional] |
|**keepAlive** | **Boolean** | If false, the Batch service deletes the pool once its lifetime (as determined by the poolLifetimeOption setting) expires; that is, when the job or job schedule completes. If true, the Batch service does not delete the pool automatically. It is up to the user to delete auto pools created with this option. |  [optional] |
|**pool** | [**PoolSpecification**](PoolSpecification.md) |  |  [optional] |
|**poolLifetimeOption** | [**PoolLifetimeOptionEnum**](#PoolLifetimeOptionEnum) | When the pool lifetime scope is jobschedule level, the Batch service keeps track of the last autopool created for the jobschedule, and deletes that pool when the jobschedule completes. Batch will also delete this pool if the user updates the auto pool specification in a way that changes this lifetime. |  |



## Enum: PoolLifetimeOptionEnum

| Name | Value |
|---- | -----|
| JOBSCHEDULE | &quot;jobschedule&quot; |
| JOB | &quot;job&quot; |
| UNMAPPED | &quot;unmapped&quot; |



