# CallFireApiDocumentation.TextBroadcast

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bigMessageStrategy** | **String** | If message length exceeds 160 characters, multiple messages will be sent, SEND_MULTIPLE strategy is chosen by default. Available values: SEND_MULTIPLE - send text as multiple messages, DO_NOT_SEND - do not send text if it exceeds 160 characters, TRIM - trims text message to 160 characters | [optional] 
**fromNumber** | **String** | A phone number in E.164 format (11-digit) or short code. Example: 12132000384, 67076, etc | [optional] 
**id** | **Number** | A unique id of a broadcast | [optional] 
**labels** | **[String]** | A labels of a broadcast | [optional] 
**lastModified** | **Number** | A time when the given resource was updated, formatted in unix time milliseconds (read only). Example: 1473781817000 | [optional] [readonly] 
**localTimeRestriction** | [**LocalTimeRestriction**](LocalTimeRestriction.md) |  | [optional] 
**maxActive** | **Number** | A maximum number of texts that CallFire dials at once | [optional] 
**media** | [**[Media]**](Media.md) | ~ | [optional] 
**message** | **String** | A text message | [optional] 
**name** | **String** | A name of a broadcast | [optional] 
**recipients** | [**[TextRecipient]**](TextRecipient.md) | Recipients of a text campaign, can be an existing contacts or a new one | [optional] 
**resumeNextDay** | **Boolean** | ~ | [optional] 
**schedules** | [**[Schedule]**](Schedule.md) | ~ | [optional] 
**status** | **String** | A status of a broadcast. SETUP - campaign isn&#39;t configured yet; START_PENDING - waiting for contact batch population; RUNNING - campaign is running; STOPPED - campaign is stopped; FINISHED - campaign is finished; ARCHIVED - campaign was archived | [optional] [readonly] 



## Enum: BigMessageStrategyEnum


* `SEND_MULTIPLE` (value: `"SEND_MULTIPLE"`)

* `DO_NOT_SEND` (value: `"DO_NOT_SEND"`)

* `TRIM` (value: `"TRIM"`)

* `MMS` (value: `"MMS"`)





## Enum: StatusEnum


* `TEST` (value: `"TEST"`)

* `SETUP` (value: `"SETUP"`)

* `START_PENDING` (value: `"START_PENDING"`)

* `RUNNING` (value: `"RUNNING"`)

* `SCHEDULED` (value: `"SCHEDULED"`)

* `STOPPED` (value: `"STOPPED"`)

* `SUSPENDED` (value: `"SUSPENDED"`)

* `FINISHED` (value: `"FINISHED"`)

* `ARCHIVED` (value: `"ARCHIVED"`)

* `VALIDATING_START` (value: `"VALIDATING_START"`)

* `VALIDATING_EMAIL` (value: `"VALIDATING_EMAIL"`)

* `BLOCKED_SUSPICIOUS` (value: `"BLOCKED_SUSPICIOUS"`)

* `DECLINED` (value: `"DECLINED"`)

* `APPROVED` (value: `"APPROVED"`)




