# Gitlab.PutV3ProjectsIdMergeRequestMergeRequestIdRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **String** | The title of the merge request | [optional] 
**targetBranch** | **String** | The target branch | [optional] 
**stateEvent** | **String** | Status of the merge request | [optional] 
**description** | **String** | The description of the merge request | [optional] 
**assigneeId** | **Number** | The ID of a user to assign the merge request | [optional] 
**milestoneId** | **Number** | The ID of a milestone to assign the merge request | [optional] 
**labels** | **String** | Comma-separated list of label names | [optional] 
**removeSourceBranch** | **Boolean** | Remove source branch when merging | [optional] 



## Enum: StateEventEnum


* `close` (value: `"close"`)

* `reopen` (value: `"reopen"`)

* `merge` (value: `"merge"`)




