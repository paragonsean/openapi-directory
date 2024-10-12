# CloudDataplexApi.GoogleCloudDataplexV1TriggerSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron** | **String** | Required. Cron (https://en.wikipedia.org/wiki/Cron) schedule for running scans periodically.To explicitly set a timezone in the cron tab, apply a prefix in the cron tab: \&quot;CRON_TZ&#x3D;${IANA_TIME_ZONE}\&quot; or \&quot;TZ&#x3D;${IANA_TIME_ZONE}\&quot;. The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database (wikipedia (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List)). For example, CRON_TZ&#x3D;America/New_York 1 * * * *, or TZ&#x3D;America/New_York 1 * * * *.This field is required for Schedule scans. | [optional] 


