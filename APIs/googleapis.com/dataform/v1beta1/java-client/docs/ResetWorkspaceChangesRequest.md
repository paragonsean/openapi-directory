

# ResetWorkspaceChangesRequest

`ResetWorkspaceChanges` request message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clean** | **Boolean** | Optional. If set to true, untracked files will be deleted. |  [optional] |
|**paths** | **List&lt;String&gt;** | Optional. Full file paths to reset back to their committed state including filename, rooted at workspace root. If left empty, all files will be reset. |  [optional] |



