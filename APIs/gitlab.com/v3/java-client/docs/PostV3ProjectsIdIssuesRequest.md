

# PostV3ProjectsIdIssuesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**title** | **String** | The title of an issue |  |
|**createdAt** | **OffsetDateTime** | Date time when the issue was created. Available only for admins and project owners. |  [optional] |
|**mergeRequestForResolvingDiscussions** | **Integer** | The IID of a merge request for which to resolve discussions |  [optional] |
|**description** | **String** | The description of an issue |  [optional] |
|**assigneeId** | **Integer** | The ID of a user to assign issue |  [optional] |
|**milestoneId** | **Integer** | The ID of a milestone to assign issue |  [optional] |
|**labels** | **String** | Comma-separated list of label names |  [optional] |
|**dueDate** | **String** | Date time string in the format YEAR-MONTH-DAY |  [optional] |
|**confidential** | **Boolean** | Boolean parameter if the issue should be confidential |  [optional] |



