# CloudDataplexApi.GoogleCloudDataplexV1TaskTriggerSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **Boolean** | Optional. Prevent the task from executing. This does not cancel already running tasks. It is intended to temporarily disable RECURRING tasks. | [optional] 
**maxRetries** | **Number** | Optional. Number of retry attempts before aborting. Set to zero to never attempt to retry a failed task. | [optional] 
**schedule** | **String** | Optional. Cron schedule (https://en.wikipedia.org/wiki/Cron) for running tasks periodically. To explicitly set a timezone to the cron tab, apply a prefix in the cron tab: \&quot;CRON_TZ&#x3D;${IANA_TIME_ZONE}\&quot; or \&quot;TZ&#x3D;${IANA_TIME_ZONE}\&quot;. The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, CRON_TZ&#x3D;America/New_York 1 * * * *, or TZ&#x3D;America/New_York 1 * * * *. This field is required for RECURRING tasks. | [optional] 
**startTime** | **String** | Optional. The first run of the task will be after this time. If not specified, the task will run shortly after being submitted if ON_DEMAND and based on the schedule if RECURRING. | [optional] 
**type** | **String** | Required. Immutable. Trigger type of the user-specified Task. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `ON_DEMAND` (value: `"ON_DEMAND"`)

* `RECURRING` (value: `"RECURRING"`)




