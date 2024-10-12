# TimeSeriesInsightsClient.InstancesBatchRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_delete** | [**InstancesRequestBatchGetOrDelete**](InstancesRequestBatchGetOrDelete.md) |  | [optional] 
**get** | [**InstancesRequestBatchGetOrDelete**](InstancesRequestBatchGetOrDelete.md) |  | [optional] 
**put** | [**[TimeSeriesInstance]**](TimeSeriesInstance.md) | Time series instances to be created or updated. | [optional] 
**update** | [**[TimeSeriesInstance]**](TimeSeriesInstance.md) | Time series instances to be updated onlRequest to perform a single operation on a batch of instances. y. If instance does not exist, an error is returned. | [optional] 


