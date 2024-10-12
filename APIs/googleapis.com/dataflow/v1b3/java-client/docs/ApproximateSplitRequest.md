

# ApproximateSplitRequest

A suggestion by the service to the worker to dynamically split the WorkItem.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fractionConsumed** | **Double** | A fraction at which to split the work item, from 0.0 (beginning of the input) to 1.0 (end of the input). |  [optional] |
|**fractionOfRemainder** | **Double** | The fraction of the remainder of work to split the work item at, from 0.0 (split at the current position) to 1.0 (end of the input). |  [optional] |
|**position** | [**Position**](Position.md) |  |  [optional] |



