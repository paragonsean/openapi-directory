# CallFireApiDocumentation.CallBroadcast

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answeringMachineConfig** | **String** | Specifies which action should be taken if answering machine was detected, default value: AM_AND_LIVE. Available values: AM_ONLY - run AMD (Answering Machine Detection), hang up if LA (Live Answer); AM_AND_LIVE - run AMD, play separate live vs. machine sound; LIVE_WITH_AMD, run AMD, hang up if machine answers; LIVE_IMMEDIATE - no AMD, play live sound immediately | [optional] 
**dialplanXml** | **String** | IVR xml is a document which describes the dialplan to setup the IVR broadcast | [optional] 
**fromNumber** | **String** | Phone number in E.164 format (11-digit) or short code for text. Example: 12132000384, 67076 | [optional] 
**id** | **Number** | A unique id of broadcast (readonly) | [optional] 
**labels** | **[String]** | Labels of a broadcast | [optional] 
**lastModified** | **Number** | The time when a given resource was updated, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT  | [optional] [readonly] 
**localTimeRestriction** | [**LocalTimeRestriction**](LocalTimeRestriction.md) |  | [optional] 
**maxActive** | **Number** | Sets a maximum number of calls to be dialed by CallFire at once | [optional] 
**maxActiveTransfers** | **Number** | A maximum number of active transfers | [optional] 
**name** | **String** | A name of a broadcast | [optional] 
**recipients** | [**[Recipient]**](Recipient.md) | Recipients of a call broadcast, can be either existing contacts or a new ones | [optional] 
**resumeNextDay** | **Boolean** | If true resumes the unfinished campaign to the next day | [optional] 
**retryConfig** | [**RetryConfig**](RetryConfig.md) |  | [optional] 
**schedules** | [**[Schedule]**](Schedule.md) | A list of schedule objects which specifies a range of time when broadcast should be started and stopped. Supports the scheduling per day of week | [optional] 
**sounds** | [**CallBroadcastSounds**](CallBroadcastSounds.md) |  | [optional] 
**status** | **String** | A status of a broadcast (read only). SETUP - campaign isn&#39;t configured yet; START_PENDING - waiting for contact batch population; RUNNING - campaign is running; STOPPED - campaign is stopped; FINISHED - campaign is finished; ARCHIVED - campaign was archived | [optional] [readonly] 



## Enum: AnsweringMachineConfigEnum


* `AM_ONLY` (value: `"AM_ONLY"`)

* `AM_AND_LIVE` (value: `"AM_AND_LIVE"`)

* `LIVE_WITH_AMD` (value: `"LIVE_WITH_AMD"`)

* `LIVE_IMMEDIATE` (value: `"LIVE_IMMEDIATE"`)





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




