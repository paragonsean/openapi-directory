

# LiveStreamHealthStatus


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configurationIssues** | [**List&lt;LiveStreamConfigurationIssue&gt;**](LiveStreamConfigurationIssue.md) | The configurations issues on this stream |  [optional] |
|**lastUpdateTimeSeconds** | **String** | The last time this status was updated (in seconds) |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status code of this stream |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| GOOD | &quot;good&quot; |
| OK | &quot;ok&quot; |
| BAD | &quot;bad&quot; |
| NO_DATA | &quot;noData&quot; |
| REVOKED | &quot;revoked&quot; |



