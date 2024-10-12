# BatchService.AutoPoolSpecification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoPoolIdPrefix** | **String** | A prefix to be added to the unique identifier when a pool is automatically created. The prefix can be up to 20 characters long. | [optional] 
**keepAlive** | **Boolean** | Whether to keep an auto pool alive after its lifetime expires. | [optional] 
**pool** | [**PoolSpecification**](PoolSpecification.md) |  | [optional] 
**poolLifetimeOption** | **String** | The minimum lifetime of created auto pools, and how multiple jobs on a schedule are assigned to pools. | 



## Enum: PoolLifetimeOptionEnum


* `jobschedule` (value: `"jobschedule"`)

* `job` (value: `"job"`)

* `unmapped` (value: `"unmapped"`)




