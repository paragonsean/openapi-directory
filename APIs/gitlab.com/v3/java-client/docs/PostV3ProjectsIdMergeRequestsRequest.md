

# PostV3ProjectsIdMergeRequestsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** | The title of the merge request |  |
|**sourceBranch** | **String** | The source branch |  |
|**targetBranch** | **String** | The target branch |  |
|**targetProjectId** | **Integer** | The target project of the merge request defaults to the :id of the project |  [optional] |
|**description** | **String** | The description of the merge request |  [optional] |
|**assigneeId** | **Integer** | The ID of a user to assign the merge request |  [optional] |
|**milestoneId** | **Integer** | The ID of a milestone to assign the merge request |  [optional] |
|**labels** | **String** | Comma-separated list of label names |  [optional] |
|**removeSourceBranch** | **Boolean** | Remove source branch when merging |  [optional] |



