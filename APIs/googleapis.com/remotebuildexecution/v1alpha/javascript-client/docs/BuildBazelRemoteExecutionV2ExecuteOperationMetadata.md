# RemoteBuildExecutionApi.BuildBazelRemoteExecutionV2ExecuteOperationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionDigest** | [**BuildBazelRemoteExecutionV2Digest**](BuildBazelRemoteExecutionV2Digest.md) |  | [optional] 
**partialExecutionMetadata** | [**BuildBazelRemoteExecutionV2ExecutedActionMetadata**](BuildBazelRemoteExecutionV2ExecutedActionMetadata.md) |  | [optional] 
**stage** | **String** | The current stage of execution. | [optional] 
**stderrStreamName** | **String** | If set, the client can use this resource name with ByteStream.Read to stream the standard error from the endpoint hosting streamed responses. | [optional] 
**stdoutStreamName** | **String** | If set, the client can use this resource name with ByteStream.Read to stream the standard output from the endpoint hosting streamed responses. | [optional] 



## Enum: StageEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `CACHE_CHECK` (value: `"CACHE_CHECK"`)

* `QUEUED` (value: `"QUEUED"`)

* `EXECUTING` (value: `"EXECUTING"`)

* `COMPLETED` (value: `"COMPLETED"`)




