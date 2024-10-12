

# HierarchiesBatchRequest

Request to perform a single operation on a batch of hierarchies. Exactly one of \"get\", \"put\" or \"delete\" must be set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**delete** | [**HierarchiesRequestBatchGetDelete**](HierarchiesRequestBatchGetDelete.md) |  |  [optional] |
|**get** | [**HierarchiesRequestBatchGetDelete**](HierarchiesRequestBatchGetDelete.md) |  |  [optional] |
|**put** | [**List&lt;TimeSeriesHierarchy&gt;**](TimeSeriesHierarchy.md) | \&quot;put\&quot; should be set while creating or updating hierarchies. |  [optional] |



