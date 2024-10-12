

# CallBroadcast

Call broadcast can be used to send out a voice message to a group of numbers. It supports IVR scripting, scheduling, retry logic, playing pre-recorded sounds, answering machine detection

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**answeringMachineConfig** | [**AnsweringMachineConfigEnum**](#AnsweringMachineConfigEnum) | Specifies which action should be taken if answering machine was detected, default value: AM_AND_LIVE. Available values: AM_ONLY - run AMD (Answering Machine Detection), hang up if LA (Live Answer); AM_AND_LIVE - run AMD, play separate live vs. machine sound; LIVE_WITH_AMD, run AMD, hang up if machine answers; LIVE_IMMEDIATE - no AMD, play live sound immediately |  [optional] |
|**dialplanXml** | **String** | IVR xml is a document which describes the dialplan to setup the IVR broadcast |  [optional] |
|**fromNumber** | **String** | Phone number in E.164 format (11-digit) or short code for text. Example: 12132000384, 67076 |  [optional] |
|**id** | **Long** | A unique id of broadcast (readonly) |  [optional] |
|**labels** | **Set&lt;String&gt;** | Labels of a broadcast |  [optional] |
|**lastModified** | **Long** | The time when a given resource was updated, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT  |  [optional] [readonly] |
|**localTimeRestriction** | [**LocalTimeRestriction**](LocalTimeRestriction.md) |  |  [optional] |
|**maxActive** | **Integer** | Sets a maximum number of calls to be dialed by CallFire at once |  [optional] |
|**maxActiveTransfers** | **Integer** | A maximum number of active transfers |  [optional] |
|**name** | **String** | A name of a broadcast |  [optional] |
|**recipients** | [**List&lt;Recipient&gt;**](Recipient.md) | Recipients of a call broadcast, can be either existing contacts or a new ones |  [optional] |
|**resumeNextDay** | **Boolean** | If true resumes the unfinished campaign to the next day |  [optional] |
|**retryConfig** | [**RetryConfig**](RetryConfig.md) |  |  [optional] |
|**schedules** | [**List&lt;Schedule&gt;**](Schedule.md) | A list of schedule objects which specifies a range of time when broadcast should be started and stopped. Supports the scheduling per day of week |  [optional] |
|**sounds** | [**CallBroadcastSounds**](CallBroadcastSounds.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | A status of a broadcast (read only). SETUP - campaign isn&#39;t configured yet; START_PENDING - waiting for contact batch population; RUNNING - campaign is running; STOPPED - campaign is stopped; FINISHED - campaign is finished; ARCHIVED - campaign was archived |  [optional] [readonly] |



## Enum: AnsweringMachineConfigEnum

| Name | Value |
|---- | -----|
| AM_ONLY | &quot;AM_ONLY&quot; |
| AM_AND_LIVE | &quot;AM_AND_LIVE&quot; |
| LIVE_WITH_AMD | &quot;LIVE_WITH_AMD&quot; |
| LIVE_IMMEDIATE | &quot;LIVE_IMMEDIATE&quot; |



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



