

# InstancesBatchRequest

Request to perform a single operation on a batch of instances. Exactly one of \"get\", \"put\", \"update\" or \"delete\" must be set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**delete** | [**InstancesRequestBatchGetOrDelete**](InstancesRequestBatchGetOrDelete.md) |  |  [optional] |
|**get** | [**InstancesRequestBatchGetOrDelete**](InstancesRequestBatchGetOrDelete.md) |  |  [optional] |
|**put** | [**List&lt;TimeSeriesInstance&gt;**](TimeSeriesInstance.md) | Time series instances to be created or updated. |  [optional] |
|**update** | [**List&lt;TimeSeriesInstance&gt;**](TimeSeriesInstance.md) | Time series instances to be updated onlRequest to perform a single operation on a batch of instances. y. If instance does not exist, an error is returned. |  [optional] |



