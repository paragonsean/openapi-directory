# InfluxOssApiService.NotificationRuleDiscriminator

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
**channel** | **String** |  | 
**messageTemplate** | **String** | The message template as a flux interpolated string. | 
**type** | **String** |  | 
**bodyTemplate** | **String** |  | [optional] 
**subjectTemplate** | **String** |  | 
**to** | **String** |  | 
**url** | **String** |  | [optional] 
**disableWebPagePreview** | **Boolean** | Disables preview of web links in the sent messages when \&quot;true\&quot;. Defaults to \&quot;false\&quot; . | [optional] 
**parseMode** | **String** | Parse mode of the message text per https://core.telegram.org/bots/api#formatting-options . Defaults to \&quot;MarkdownV2\&quot; . | [optional] 



## Enum: LastRunStatusEnum


* `failed` (value: `"failed"`)

* `success` (value: `"success"`)

* `canceled` (value: `"canceled"`)





## Enum: TypeEnum


* `slack` (value: `"slack"`)

* `smtp` (value: `"smtp"`)

* `pagerduty` (value: `"pagerduty"`)

* `http` (value: `"http"`)

* `telegram` (value: `"telegram"`)





## Enum: ParseModeEnum


* `MarkdownV2` (value: `"MarkdownV2"`)

* `HTML` (value: `"HTML"`)

* `Markdown` (value: `"Markdown"`)




