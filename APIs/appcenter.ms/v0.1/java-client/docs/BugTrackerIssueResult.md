

# BugTrackerIssueResult

Object returned in response to getting a bug tracker issue related to a crash group id

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bugTrackerType** | [**BugTrackerTypeEnum**](#BugTrackerTypeEnum) |  |  [optional] |
|**eventType** | **String** |  |  [optional] |
|**id** | **String** |  |  [optional] |
|**mobileCenterId** | **String** |  |  [optional] |
|**repoName** | **String** |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**url** | **String** |  |  [optional] |



## Enum: BugTrackerTypeEnum

| Name | Value |
|---- | -----|
| GITHUB | &quot;github&quot; |
| VSTS | &quot;vsts&quot; |
| JIRA | &quot;jira&quot; |



