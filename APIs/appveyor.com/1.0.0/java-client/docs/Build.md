

# Build


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**branch** | **String** |  |  [optional] |
|**buildId** | **Integer** |  |  [optional] |
|**message** | **String** |  |  [optional] |
|**version** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**updated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**authorName** | **String** |  |  [optional] |
|**authorUsername** | **String** |  |  [optional] |
|**buildNumber** | **Integer** |  |  [optional] |
|**commitId** | **String** |  |  [optional] |
|**committed** | **OffsetDateTime** |  |  [optional] |
|**committerName** | **String** |  |  [optional] |
|**committerUsername** | **String** |  |  [optional] |
|**finished** | **OffsetDateTime** |  |  [optional] |
|**isTag** | **Boolean** |  |  [optional] |
|**jobs** | [**List&lt;BuildJob&gt;**](BuildJob.md) | Always empty in getProjectHistory and startDeployment responses. |  [optional] |
|**messageExtended** | **String** |  |  [optional] |
|**messages** | [**List&lt;BuildMessage&gt;**](BuildMessage.md) |  |  [optional] |
|**projectId** | **Integer** |  |  [optional] |
|**pullRequestId** | **Integer** |  |  [optional] |
|**pullRequestName** | **String** |  |  [optional] |
|**started** | **OffsetDateTime** |  |  [optional] |
|**status** | **Status** |  |  [optional] |



