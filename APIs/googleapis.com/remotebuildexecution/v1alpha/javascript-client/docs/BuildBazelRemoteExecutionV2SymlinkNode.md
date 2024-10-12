# RemoteBuildExecutionApi.BuildBazelRemoteExecutionV2SymlinkNode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | The name of the symlink. | [optional] 
**nodeProperties** | [**BuildBazelRemoteExecutionV2NodeProperties**](BuildBazelRemoteExecutionV2NodeProperties.md) |  | [optional] 
**target** | **String** | The target path of the symlink. The path separator is a forward slash &#x60;/&#x60;. The target path can be relative to the parent directory of the symlink or it can be an absolute path starting with &#x60;/&#x60;. Support for absolute paths can be checked using the Capabilities API. &#x60;..&#x60; components are allowed anywhere in the target path as logical canonicalization may lead to different behavior in the presence of directory symlinks (e.g. &#x60;foo/../bar&#x60; may not be the same as &#x60;bar&#x60;). To reduce potential cache misses, canonicalization is still recommended where this is possible without impacting correctness. | [optional] 


