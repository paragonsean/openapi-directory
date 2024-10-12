

# AutoPoolSpecification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoPoolIdPrefix** | **String** | The Batch service assigns each auto pool a unique identifier on creation. To distinguish between pools created for different purposes, you can specify this element to add a prefix to the ID that is assigned. The prefix can be up to 20 characters long. |  [optional] |
|**keepAlive** | **Boolean** | If false, the Batch service deletes the pool once its lifetime (as determined by the poolLifetimeOption setting) expires; that is, when the job or job schedule completes. If true, the Batch service does not delete the pool automatically. It is up to the user to delete auto pools created with this option. |  [optional] |
|**pool** | [**PoolSpecification**](PoolSpecification.md) |  |  [optional] |
|**poolLifetimeOption** | [**PoolLifetimeOptionEnum**](#PoolLifetimeOptionEnum) | When the pool lifetime is jobSchedule the pool exists for the lifetime of the job schedule. The Batch Service creates the pool when it creates the first job on the schedule. You may apply this option only to job schedules, not to jobs. When the pool lifetime is job the pool exists for the lifetime of the job to which it is dedicated. The Batch service creates the pool when it creates the job. If the &#39;job&#39; option is applied to a job schedule, the Batch service creates a new auto pool for every job created on the schedule. |  |



## Enum: PoolLifetimeOptionEnum

| Name | Value |
|---- | -----|
| JOB_SCHEDULE | &quot;jobSchedule&quot; |
| JOB | &quot;job&quot; |



