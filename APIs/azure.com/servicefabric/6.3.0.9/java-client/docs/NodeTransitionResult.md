

# NodeTransitionResult

Represents information about an operation in a terminal state (Completed or Faulted).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorCode** | **Integer** | If OperationState is Completed, this is 0.  If OperationState is Faulted, this is an error code indicating the reason. |  [optional] |
|**nodeResult** | [**NodeResult**](NodeResult.md) |  |  [optional] |



