# InfluxOssApiService.HTTPNotificationRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** |  | [optional] [readonly] 
**description** | **String** | An optional description of the notification rule. | [optional] 
**endpointID** | **String** |  | 
**every** | **String** | The notification repetition interval. | [optional] 
**id** | **String** |  | [optional] [readonly] 
**labels** | [**[Label]**](Label.md) |  | [optional] 
**lastRunError** | **String** |  | [optional] [readonly] 
**lastRunStatus** | **String** |  | [optional] [readonly] 
**latestCompleted** | **Date** | Timestamp of latest scheduled, completed run, RFC3339. | [optional] [readonly] 
**limit** | **Number** | Don&#39;t notify me more than &amp;lt;limit&amp;gt; times every &amp;lt;limitEvery&amp;gt; seconds. If set, limitEvery cannot be empty. | [optional] 
**limitEvery** | **Number** | Don&#39;t notify me more than &amp;lt;limit&amp;gt; times every &amp;lt;limitEvery&amp;gt; seconds. If set, limit cannot be empty. | [optional] 
**links** | [**NotificationRuleBaseLinks**](NotificationRuleBaseLinks.md) |  | [optional] 
**name** | **String** | Human-readable name describing the notification rule. | 
**offset** | **String** | Duration to delay after the schedule, before executing check. | [optional] 
**orgID** | **String** | The ID of the organization that owns this notification rule. | 
**ownerID** | **String** | The ID of creator used to create this notification rule. | [optional] [readonly] 
**runbookLink** | **String** |  | [optional] 
**sleepUntil** | **String** |  | [optional] 
**status** | [**TaskStatusType**](TaskStatusType.md) |  | 
**statusRules** | [**[StatusRule]**](StatusRule.md) | List of status rules the notification rule attempts to match. | 
**tagRules** | [**[TagRule]**](TagRule.md) | List of tag rules the notification rule attempts to match. | [optional] 
**taskID** | **String** | The ID of the task associated with this notification rule. | [optional] 
**updatedAt** | **Date** |  | [optional] [readonly] 
**type** | **String** |  | 
**url** | **String** |  | [optional] 



## Enum: LastRunStatusEnum


* `failed` (value: `"failed"`)

* `success` (value: `"success"`)

* `canceled` (value: `"canceled"`)





## Enum: TypeEnum


* `http` (value: `"http"`)




