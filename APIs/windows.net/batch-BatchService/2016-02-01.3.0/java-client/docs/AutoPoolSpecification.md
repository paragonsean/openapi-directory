

# AutoPoolSpecification

Specifies characteristics for a temporary 'auto pool'. The Batch service will create this auto pool, run all the tasks for the job on it, and will delete the pool once the job has completed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoPoolIdPrefix** | **String** | A prefix to be added to the unique identifier when a pool is automatically created. The prefix can be up to 20 characters long. |  [optional] |
|**keepAlive** | **Boolean** | Whether to keep an auto pool alive after its lifetime expires. |  [optional] |
|**pool** | [**PoolSpecification**](PoolSpecification.md) |  |  [optional] |
|**poolLifetimeOption** | [**PoolLifetimeOptionEnum**](#PoolLifetimeOptionEnum) | The minimum lifetime of created auto pools, and how multiple jobs on a schedule are assigned to pools. |  |



## Enum: PoolLifetimeOptionEnum

| Name | Value |
|---- | -----|
| JOBSCHEDULE | &quot;jobschedule&quot; |
| JOB | &quot;job&quot; |
| UNMAPPED | &quot;unmapped&quot; |



