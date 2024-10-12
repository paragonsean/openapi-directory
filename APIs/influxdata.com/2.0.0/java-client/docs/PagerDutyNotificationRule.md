

# PagerDutyNotificationRule


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**description** | **String** | An optional description of the notification rule. |  [optional] |
|**endpointID** | **String** |  |  |
|**every** | **String** | The notification repetition interval. |  [optional] |
|**id** | **String** |  |  [optional] [readonly] |
|**labels** | [**List&lt;Label&gt;**](Label.md) |  |  [optional] |
|**lastRunError** | **String** |  |  [optional] [readonly] |
|**lastRunStatus** | [**LastRunStatusEnum**](#LastRunStatusEnum) |  |  [optional] [readonly] |
|**latestCompleted** | **OffsetDateTime** | Timestamp of latest scheduled, completed run, RFC3339. |  [optional] [readonly] |
|**limit** | **Integer** | Don&#39;t notify me more than &amp;lt;limit&amp;gt; times every &amp;lt;limitEvery&amp;gt; seconds. If set, limitEvery cannot be empty. |  [optional] |
|**limitEvery** | **Integer** | Don&#39;t notify me more than &amp;lt;limit&amp;gt; times every &amp;lt;limitEvery&amp;gt; seconds. If set, limit cannot be empty. |  [optional] |
|**links** | [**NotificationRuleBaseLinks**](NotificationRuleBaseLinks.md) |  |  [optional] |
|**name** | **String** | Human-readable name describing the notification rule. |  |
|**offset** | **String** | Duration to delay after the schedule, before executing check. |  [optional] |
|**orgID** | **String** | The ID of the organization that owns this notification rule. |  |
|**ownerID** | **String** | The ID of creator used to create this notification rule. |  [optional] [readonly] |
|**runbookLink** | **String** |  |  [optional] |
|**sleepUntil** | **String** |  |  [optional] |
|**status** | **TaskStatusType** |  |  |
|**statusRules** | [**List&lt;StatusRule&gt;**](StatusRule.md) | List of status rules the notification rule attempts to match. |  |
|**tagRules** | [**List&lt;TagRule&gt;**](TagRule.md) | List of tag rules the notification rule attempts to match. |  [optional] |
|**taskID** | **String** | The ID of the task associated with this notification rule. |  [optional] |
|**updatedAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**messageTemplate** | **String** |  |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |



## Enum: LastRunStatusEnum

| Name | Value |
|---- | -----|
| FAILED | &quot;failed&quot; |
| SUCCESS | &quot;success&quot; |
| CANCELED | &quot;canceled&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PAGERDUTY | &quot;pagerduty&quot; |



