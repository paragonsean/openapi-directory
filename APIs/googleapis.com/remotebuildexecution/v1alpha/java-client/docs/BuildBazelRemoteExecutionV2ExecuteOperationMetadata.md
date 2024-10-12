

# BuildBazelRemoteExecutionV2ExecuteOperationMetadata

Metadata about an ongoing execution, which will be contained in the metadata field of the Operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionDigest** | [**BuildBazelRemoteExecutionV2Digest**](BuildBazelRemoteExecutionV2Digest.md) |  |  [optional] |
|**partialExecutionMetadata** | [**BuildBazelRemoteExecutionV2ExecutedActionMetadata**](BuildBazelRemoteExecutionV2ExecutedActionMetadata.md) |  |  [optional] |
|**stage** | [**StageEnum**](#StageEnum) | The current stage of execution. |  [optional] |
|**stderrStreamName** | **String** | If set, the client can use this resource name with ByteStream.Read to stream the standard error from the endpoint hosting streamed responses. |  [optional] |
|**stdoutStreamName** | **String** | If set, the client can use this resource name with ByteStream.Read to stream the standard output from the endpoint hosting streamed responses. |  [optional] |



## Enum: StageEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| CACHE_CHECK | &quot;CACHE_CHECK&quot; |
| QUEUED | &quot;QUEUED&quot; |
| EXECUTING | &quot;EXECUTING&quot; |
| COMPLETED | &quot;COMPLETED&quot; |



