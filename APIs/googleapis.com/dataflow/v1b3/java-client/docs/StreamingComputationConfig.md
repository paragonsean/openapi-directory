

# StreamingComputationConfig

Configuration information for a single streaming computation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**computationId** | **String** | Unique identifier for this computation. |  [optional] |
|**instructions** | [**List&lt;ParallelInstruction&gt;**](ParallelInstruction.md) | Instructions that comprise the computation. |  [optional] |
|**stageName** | **String** | Stage name of this computation. |  [optional] |
|**systemName** | **String** | System defined name for this computation. |  [optional] |
|**transformUserNameToStateFamily** | **Map&lt;String, String&gt;** | Map from user name of stateful transforms in this stage to their state family. |  [optional] |



