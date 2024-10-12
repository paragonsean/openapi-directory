# RemoteBuildExecutionApi.BuildBazelRemoteExecutionV2OutputSymlink

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodeProperties** | [**BuildBazelRemoteExecutionV2NodeProperties**](BuildBazelRemoteExecutionV2NodeProperties.md) |  | [optional] 
**path** | **String** | The full path of the symlink relative to the working directory, including the filename. The path separator is a forward slash &#x60;/&#x60;. Since this is a relative path, it MUST NOT begin with a leading forward slash. | [optional] 
**target** | **String** | The target path of the symlink. The path separator is a forward slash &#x60;/&#x60;. The target path can be relative to the parent directory of the symlink or it can be an absolute path starting with &#x60;/&#x60;. Support for absolute paths can be checked using the Capabilities API. &#x60;..&#x60; components are allowed anywhere in the target path. | [optional] 


