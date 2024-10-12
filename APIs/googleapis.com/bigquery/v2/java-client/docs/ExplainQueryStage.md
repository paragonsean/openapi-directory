

# ExplainQueryStage

A single stage of query execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completedParallelInputs** | **String** | Number of parallel input segments completed. |  [optional] |
|**computeMode** | [**ComputeModeEnum**](#ComputeModeEnum) | Output only. Compute mode for this stage. |  [optional] [readonly] |
|**computeMsAvg** | **String** | Milliseconds the average shard spent on CPU-bound tasks. |  [optional] |
|**computeMsMax** | **String** | Milliseconds the slowest shard spent on CPU-bound tasks. |  [optional] |
|**computeRatioAvg** | **Double** | Relative amount of time the average shard spent on CPU-bound tasks. |  [optional] |
|**computeRatioMax** | **Double** | Relative amount of time the slowest shard spent on CPU-bound tasks. |  [optional] |
|**endMs** | **String** | Stage end time represented as milliseconds since the epoch. |  [optional] |
|**id** | **String** | Unique ID for the stage within the plan. |  [optional] |
|**inputStages** | **List&lt;String&gt;** | IDs for stages that are inputs to this stage. |  [optional] |
|**name** | **String** | Human-readable name for the stage. |  [optional] |
|**parallelInputs** | **String** | Number of parallel input segments to be processed |  [optional] |
|**readMsAvg** | **String** | Milliseconds the average shard spent reading input. |  [optional] |
|**readMsMax** | **String** | Milliseconds the slowest shard spent reading input. |  [optional] |
|**readRatioAvg** | **Double** | Relative amount of time the average shard spent reading input. |  [optional] |
|**readRatioMax** | **Double** | Relative amount of time the slowest shard spent reading input. |  [optional] |
|**recordsRead** | **String** | Number of records read into the stage. |  [optional] |
|**recordsWritten** | **String** | Number of records written by the stage. |  [optional] |
|**shuffleOutputBytes** | **String** | Total number of bytes written to shuffle. |  [optional] |
|**shuffleOutputBytesSpilled** | **String** | Total number of bytes written to shuffle and spilled to disk. |  [optional] |
|**slotMs** | **String** | Slot-milliseconds used by the stage. |  [optional] |
|**startMs** | **String** | Stage start time represented as milliseconds since the epoch. |  [optional] |
|**status** | **String** | Current status for this stage. |  [optional] |
|**steps** | [**List&lt;ExplainQueryStep&gt;**](ExplainQueryStep.md) | List of operations within the stage in dependency order (approximately chronological). |  [optional] |
|**waitMsAvg** | **String** | Milliseconds the average shard spent waiting to be scheduled. |  [optional] |
|**waitMsMax** | **String** | Milliseconds the slowest shard spent waiting to be scheduled. |  [optional] |
|**waitRatioAvg** | **Double** | Relative amount of time the average shard spent waiting to be scheduled. |  [optional] |
|**waitRatioMax** | **Double** | Relative amount of time the slowest shard spent waiting to be scheduled. |  [optional] |
|**writeMsAvg** | **String** | Milliseconds the average shard spent on writing output. |  [optional] |
|**writeMsMax** | **String** | Milliseconds the slowest shard spent on writing output. |  [optional] |
|**writeRatioAvg** | **Double** | Relative amount of time the average shard spent on writing output. |  [optional] |
|**writeRatioMax** | **Double** | Relative amount of time the slowest shard spent on writing output. |  [optional] |



## Enum: ComputeModeEnum

| Name | Value |
|---- | -----|
| COMPUTE_MODE_UNSPECIFIED | &quot;COMPUTE_MODE_UNSPECIFIED&quot; |
| BIGQUERY | &quot;BIGQUERY&quot; |
| BI_ENGINE | &quot;BI_ENGINE&quot; |



