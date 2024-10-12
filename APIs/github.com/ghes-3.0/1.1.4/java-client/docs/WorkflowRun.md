

# WorkflowRun

An invocation of a workflow

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artifactsUrl** | **String** | The URL to the artifacts for the workflow run. |  |
|**cancelUrl** | **String** | The URL to cancel the workflow run. |  |
|**checkSuiteId** | **Integer** | The ID of the associated check suite. |  [optional] |
|**checkSuiteNodeId** | **String** | The node ID of the associated check suite. |  [optional] |
|**checkSuiteUrl** | **String** | The URL to the associated check suite. |  |
|**conclusion** | **String** |  |  |
|**createdAt** | **OffsetDateTime** |  |  |
|**event** | **String** |  |  |
|**headBranch** | **String** |  |  |
|**headCommit** | [**NullableSimpleCommit**](NullableSimpleCommit.md) |  |  |
|**headRepository** | [**MinimalRepository**](MinimalRepository.md) |  |  |
|**headRepositoryId** | **Integer** |  |  [optional] |
|**headSha** | **String** | The SHA of the head commit that points to the version of the workflow being run. |  |
|**htmlUrl** | **String** |  |  |
|**id** | **Integer** | The ID of the workflow run. |  |
|**jobsUrl** | **String** | The URL to the jobs for the workflow run. |  |
|**logsUrl** | **String** | The URL to download the logs for the workflow run. |  |
|**name** | **String** | The name of the workflow run. |  [optional] |
|**nodeId** | **String** |  |  |
|**previousAttemptUrl** | **String** | The URL to the previous attempted run of this workflow, if one exists. |  [optional] |
|**pullRequests** | [**List&lt;PullRequestMinimal&gt;**](PullRequestMinimal.md) |  |  |
|**repository** | [**MinimalRepository**](MinimalRepository.md) |  |  |
|**rerunUrl** | **String** | The URL to rerun the workflow run. |  |
|**runAttempt** | **Integer** | Attempt number of the run, 1 for first attempt and higher if the workflow was re-run. |  [optional] |
|**runNumber** | **Integer** | The auto incrementing run number for the workflow run. |  |
|**runStartedAt** | **OffsetDateTime** | The start time of the latest run. Resets on re-run. |  [optional] |
|**status** | **String** |  |  |
|**updatedAt** | **OffsetDateTime** |  |  |
|**url** | **String** | The URL to the workflow run. |  |
|**workflowId** | **Integer** | The ID of the parent workflow. |  |
|**workflowUrl** | **String** | The URL to the workflow. |  |



