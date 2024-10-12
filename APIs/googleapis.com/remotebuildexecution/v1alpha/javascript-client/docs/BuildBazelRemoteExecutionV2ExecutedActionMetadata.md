# RemoteBuildExecutionApi.BuildBazelRemoteExecutionV2ExecutedActionMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auxiliaryMetadata** | **[{String: Object}]** | Details that are specific to the kind of worker used. For example, on POSIX-like systems this could contain a message with getrusage(2) statistics. | [optional] 
**executionCompletedTimestamp** | **String** | When the worker completed executing the action command. | [optional] 
**executionStartTimestamp** | **String** | When the worker started executing the action command. | [optional] 
**inputFetchCompletedTimestamp** | **String** | When the worker finished fetching action inputs. | [optional] 
**inputFetchStartTimestamp** | **String** | When the worker started fetching action inputs. | [optional] 
**outputUploadCompletedTimestamp** | **String** | When the worker finished uploading action outputs. | [optional] 
**outputUploadStartTimestamp** | **String** | When the worker started uploading action outputs. | [optional] 
**queuedTimestamp** | **String** | When was the action added to the queue. | [optional] 
**virtualExecutionDuration** | **String** | New in v2.3: the amount of time the worker spent executing the action command, potentially computed using a worker-specific virtual clock. The virtual execution duration is only intended to cover the \&quot;execution\&quot; of the specified action and not time in queue nor any overheads before or after execution such as marshalling inputs/outputs. The server SHOULD avoid including time spent the client doesn&#39;t have control over, and MAY extend or reduce the execution duration to account for delays or speedups that occur during execution itself (e.g., lazily loading data from the Content Addressable Storage, live migration of virtual machines, emulation overhead). The method of timekeeping used to compute the virtual execution duration MUST be consistent with what is used to enforce the Action&#39;s &#x60;timeout&#x60;. There is no relationship between the virtual execution duration and the values of &#x60;execution_start_timestamp&#x60; and &#x60;execution_completed_timestamp&#x60;. | [optional] 
**worker** | **String** | The name of the worker which ran the execution. | [optional] 
**workerCompletedTimestamp** | **String** | When the worker completed the action, including all stages. | [optional] 
**workerStartTimestamp** | **String** | When the worker received the action. | [optional] 


