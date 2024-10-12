

# CommitWorkspaceChangesRequest

`CommitWorkspaceChanges` request message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**author** | [**CommitAuthor**](CommitAuthor.md) |  |  [optional] |
|**commitMessage** | **String** | Optional. The commit&#39;s message. |  [optional] |
|**paths** | **List&lt;String&gt;** | Optional. Full file paths to commit including filename, rooted at workspace root. If left empty, all files will be committed. |  [optional] |



