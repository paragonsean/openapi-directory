# RemoteBuildExecutionApi.GoogleDevtoolsRemoteworkersV1test2FileMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | **Blob** | If the file is small enough, its contents may also or alternatively be listed here. | [optional] 
**digest** | [**GoogleDevtoolsRemoteworkersV1test2Digest**](GoogleDevtoolsRemoteworkersV1test2Digest.md) |  | [optional] 
**isExecutable** | **Boolean** | Properties of the file | [optional] 
**path** | **String** | The path of this file. If this message is part of the CommandOutputs.outputs fields, the path is relative to the execution root and must correspond to an entry in CommandTask.outputs.files. If this message is part of a Directory message, then the path is relative to the root of that directory. All paths MUST be delimited by forward slashes. | [optional] 


