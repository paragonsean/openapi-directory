# RemoteBuildExecutionApi.BuildBazelRemoteExecutionV2OutputFile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | **Blob** | The contents of the file if inlining was requested. The server SHOULD NOT inline file contents unless requested by the client in the GetActionResultRequest message. The server MAY omit inlining, even if requested, and MUST do so if inlining would cause the response to exceed message size limits. Clients SHOULD NOT populate this field when uploading to the cache. | [optional] 
**digest** | [**BuildBazelRemoteExecutionV2Digest**](BuildBazelRemoteExecutionV2Digest.md) |  | [optional] 
**isExecutable** | **Boolean** | True if file is executable, false otherwise. | [optional] 
**nodeProperties** | [**BuildBazelRemoteExecutionV2NodeProperties**](BuildBazelRemoteExecutionV2NodeProperties.md) |  | [optional] 
**path** | **String** | The full path of the file relative to the working directory, including the filename. The path separator is a forward slash &#x60;/&#x60;. Since this is a relative path, it MUST NOT begin with a leading forward slash. | [optional] 


