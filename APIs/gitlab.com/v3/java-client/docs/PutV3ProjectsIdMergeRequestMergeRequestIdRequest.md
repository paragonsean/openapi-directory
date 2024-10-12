

# PutV3ProjectsIdMergeRequestMergeRequestIdRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** | The title of the merge request |  [optional] |
|**targetBranch** | **String** | The target branch |  [optional] |
|**stateEvent** | [**StateEventEnum**](#StateEventEnum) | Status of the merge request |  [optional] |
|**description** | **String** | The description of the merge request |  [optional] |
|**assigneeId** | **Integer** | The ID of a user to assign the merge request |  [optional] |
|**milestoneId** | **Integer** | The ID of a milestone to assign the merge request |  [optional] |
|**labels** | **String** | Comma-separated list of label names |  [optional] |
|**removeSourceBranch** | **Boolean** | Remove source branch when merging |  [optional] |



## Enum: StateEventEnum

| Name | Value |
|---- | -----|
| CLOSE | &quot;close&quot; |
| REOPEN | &quot;reopen&quot; |
| MERGE | &quot;merge&quot; |



