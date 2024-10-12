

# AnalysisArchiveTransitionHistory

A rule for auto-archiving image analysis by time and/or tag-history

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  [optional] |
|**imageDigest** | **String** |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] |
|**ruleId** | **String** |  |  [optional] |
|**transition** | [**TransitionEnum**](#TransitionEnum) |  |  [optional] |
|**transitionTaskId** | **String** | The task that created &amp; updated this entry |  [optional] |



## Enum: TransitionEnum

| Name | Value |
|---- | -----|
| ARCHIVE | &quot;archive&quot; |
| DELETE | &quot;delete&quot; |



