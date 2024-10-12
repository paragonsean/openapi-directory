

# GoogleChromeManagementV1DeviceActivityReport

Device activity report. * Granular permission needed: TELEMETRY_API_DEVICE_ACTIVITY_REPORT

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceActivityState** | [**DeviceActivityStateEnum**](#DeviceActivityStateEnum) | Output only. Device activity state. |  [optional] [readonly] |
|**reportTime** | **String** | Output only. Timestamp of when the report was collected. |  [optional] [readonly] |



## Enum: DeviceActivityStateEnum

| Name | Value |
|---- | -----|
| DEVICE_ACTIVITY_STATE_UNSPECIFIED | &quot;DEVICE_ACTIVITY_STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| IDLE | &quot;IDLE&quot; |
| LOCKED | &quot;LOCKED&quot; |



