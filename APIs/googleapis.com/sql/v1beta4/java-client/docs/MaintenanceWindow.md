

# MaintenanceWindow

Maintenance window. This specifies when a Cloud SQL instance is restarted for system maintenance purposes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**day** | **Integer** | day of week (1-7), starting on Monday. |  [optional] |
|**hour** | **Integer** | hour of day - 0 to 23. |  [optional] |
|**kind** | **String** | This is always &#x60;sql#maintenanceWindow&#x60;. |  [optional] |
|**updateTrack** | [**UpdateTrackEnum**](#UpdateTrackEnum) | Maintenance timing setting: &#x60;canary&#x60; (Earlier) or &#x60;stable&#x60; (Later). [Learn more](https://cloud.google.com/sql/docs/mysql/instance-settings#maintenance-timing-2ndgen). |  [optional] |



## Enum: UpdateTrackEnum

| Name | Value |
|---- | -----|
| SQL_UPDATE_TRACK_UNSPECIFIED | &quot;SQL_UPDATE_TRACK_UNSPECIFIED&quot; |
| CANARY | &quot;canary&quot; |
| STABLE | &quot;stable&quot; |
| WEEK5 | &quot;week5&quot; |



