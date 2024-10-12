

# TextBroadcast

A text campaign allows you to send a text message to a number of recipients. It supports scheduling, retry logic and pattern-based messages

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bigMessageStrategy** | [**BigMessageStrategyEnum**](#BigMessageStrategyEnum) | If message length exceeds 160 characters, multiple messages will be sent, SEND_MULTIPLE strategy is chosen by default. Available values: SEND_MULTIPLE - send text as multiple messages, DO_NOT_SEND - do not send text if it exceeds 160 characters, TRIM - trims text message to 160 characters |  [optional] |
|**fromNumber** | **String** | A phone number in E.164 format (11-digit) or short code. Example: 12132000384, 67076, etc |  [optional] |
|**id** | **Long** | A unique id of a broadcast |  [optional] |
|**labels** | **Set&lt;String&gt;** | A labels of a broadcast |  [optional] |
|**lastModified** | **Long** | A time when the given resource was updated, formatted in unix time milliseconds (read only). Example: 1473781817000 |  [optional] [readonly] |
|**localTimeRestriction** | [**LocalTimeRestriction**](LocalTimeRestriction.md) |  |  [optional] |
|**maxActive** | **Integer** | A maximum number of texts that CallFire dials at once |  [optional] |
|**media** | [**List&lt;Media&gt;**](Media.md) | ~ |  [optional] |
|**message** | **String** | A text message |  [optional] |
|**name** | **String** | A name of a broadcast |  [optional] |
|**recipients** | [**List&lt;TextRecipient&gt;**](TextRecipient.md) | Recipients of a text campaign, can be an existing contacts or a new one |  [optional] |
|**resumeNextDay** | **Boolean** | ~ |  [optional] |
|**schedules** | [**List&lt;Schedule&gt;**](Schedule.md) | ~ |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | A status of a broadcast. SETUP - campaign isn&#39;t configured yet; START_PENDING - waiting for contact batch population; RUNNING - campaign is running; STOPPED - campaign is stopped; FINISHED - campaign is finished; ARCHIVED - campaign was archived |  [optional] [readonly] |



## Enum: BigMessageStrategyEnum

| Name | Value |
|---- | -----|
| SEND_MULTIPLE | &quot;SEND_MULTIPLE&quot; |
| DO_NOT_SEND | &quot;DO_NOT_SEND&quot; |
| TRIM | &quot;TRIM&quot; |
| MMS | &quot;MMS&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| TEST | &quot;TEST&quot; |
| SETUP | &quot;SETUP&quot; |
| START_PENDING | &quot;START_PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SCHEDULED | &quot;SCHEDULED&quot; |
| STOPPED | &quot;STOPPED&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |
| FINISHED | &quot;FINISHED&quot; |
| ARCHIVED | &quot;ARCHIVED&quot; |
| VALIDATING_START | &quot;VALIDATING_START&quot; |
| VALIDATING_EMAIL | &quot;VALIDATING_EMAIL&quot; |
| BLOCKED_SUSPICIOUS | &quot;BLOCKED_SUSPICIOUS&quot; |
| DECLINED | &quot;DECLINED&quot; |
| APPROVED | &quot;APPROVED&quot; |



