

# TypesBatchRequest

Request to perform a single operation on a batch of time series types. Exactly one of \"get\", \"put\" or \"delete\" must be set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**delete** | [**TypesRequestBatchGetOrDelete**](TypesRequestBatchGetOrDelete.md) |  |  [optional] |
|**get** | [**TypesRequestBatchGetOrDelete**](TypesRequestBatchGetOrDelete.md) |  |  [optional] |
|**put** | [**List&lt;TimeSeriesType&gt;**](TimeSeriesType.md) | Definition of what time series types to update or create. |  [optional] |



