# BatchService.AutoPoolSpecification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoPoolIdPrefix** | **String** | Gets or sets a prefix to be added to the unique identifier when a pool is automatically created. The prefix can be up to 20 characters long. | [optional] 
**keepAlive** | **Boolean** | Gets or sets whether to keep an auto pool alive after its lifetime expires. | [optional] 
**pool** | [**PoolSpecification**](PoolSpecification.md) |  | [optional] 
**poolLifetimeOption** | **String** | Gets or sets the minimum lifetime of created auto pools, and how multiple jobs on a schedule are assigned to pools. | 



## Enum: PoolLifetimeOptionEnum


* `jobschedule` (value: `"jobschedule"`)

* `job` (value: `"job"`)

* `unmapped` (value: `"unmapped"`)




