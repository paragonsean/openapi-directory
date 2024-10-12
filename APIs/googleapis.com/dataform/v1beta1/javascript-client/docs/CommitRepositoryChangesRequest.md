# DataformApi.CommitRepositoryChangesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitMetadata** | [**CommitMetadata**](CommitMetadata.md) |  | [optional] 
**fileOperations** | [**{String: FileOperation}**](FileOperation.md) | A map to the path of the file to the operation. The path is the full file path including filename, from repository root. | [optional] 
**requiredHeadCommitSha** | **String** | Optional. The commit SHA which must be the repository&#39;s current HEAD before applying this commit; otherwise this request will fail. If unset, no validation on the current HEAD commit SHA is performed. | [optional] 


