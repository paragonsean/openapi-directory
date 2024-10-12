# CloudSqlAdminApi.MaintenanceWindow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **Number** | day of week (1-7), starting on Monday. | [optional] 
**hour** | **Number** | hour of day - 0 to 23. | [optional] 
**kind** | **String** | This is always &#x60;sql#maintenanceWindow&#x60;. | [optional] 
**updateTrack** | **String** | Maintenance timing setting: &#x60;canary&#x60; (Earlier) or &#x60;stable&#x60; (Later). [Learn more](https://cloud.google.com/sql/docs/mysql/instance-settings#maintenance-timing-2ndgen). | [optional] 



## Enum: UpdateTrackEnum


* `SQL_UPDATE_TRACK_UNSPECIFIED` (value: `"SQL_UPDATE_TRACK_UNSPECIFIED"`)

* `canary` (value: `"canary"`)

* `stable` (value: `"stable"`)

* `week5` (value: `"week5"`)




