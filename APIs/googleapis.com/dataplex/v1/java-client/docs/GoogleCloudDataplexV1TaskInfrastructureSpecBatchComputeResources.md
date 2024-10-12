

# GoogleCloudDataplexV1TaskInfrastructureSpecBatchComputeResources

Batch compute resources associated with the task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**executorsCount** | **Integer** | Optional. Total number of job executors. Executor Count should be between 2 and 100. Default&#x3D;2 |  [optional] |
|**maxExecutorsCount** | **Integer** | Optional. Max configurable executors. If max_executors_count &gt; executors_count, then auto-scaling is enabled. Max Executor Count should be between 2 and 1000. Default&#x3D;1000 |  [optional] |



