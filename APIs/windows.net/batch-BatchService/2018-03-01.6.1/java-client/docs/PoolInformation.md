

# PoolInformation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoPoolSpecification** | [**AutoPoolSpecification**](AutoPoolSpecification.md) |  |  [optional] |
|**poolId** | **String** | You must ensure that the pool referenced by this property exists. If the pool does not exist at the time the Batch service tries to schedule a job, no tasks for the job will run until you create a pool with that id. Note that the Batch service will not reject the job request; it will simply not run tasks until the pool exists. You must specify either the pool ID or the auto pool specification, but not both. |  [optional] |



