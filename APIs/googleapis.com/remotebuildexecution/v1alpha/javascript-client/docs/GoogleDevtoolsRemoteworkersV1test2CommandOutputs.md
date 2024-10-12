# RemoteBuildExecutionApi.GoogleDevtoolsRemoteworkersV1test2CommandOutputs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exitCode** | **Number** | exit_code is only fully reliable if the status&#39; code is OK. If the task exceeded its deadline or was cancelled, the process may still produce an exit code as it is cancelled, and this will be populated, but a successful (zero) is unlikely to be correct unless the status code is OK. | [optional] 
**outputs** | [**GoogleDevtoolsRemoteworkersV1test2Digest**](GoogleDevtoolsRemoteworkersV1test2Digest.md) |  | [optional] 


