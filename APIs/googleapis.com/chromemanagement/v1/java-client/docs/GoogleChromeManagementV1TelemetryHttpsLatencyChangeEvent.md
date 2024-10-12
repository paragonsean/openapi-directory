

# GoogleChromeManagementV1TelemetryHttpsLatencyChangeEvent

Https latency routine is run periodically and `TelemetryHttpsLatencyChangeEvent` is triggered if a latency problem was detected or if the device has recovered from a latency problem. * Granular permission needed: TELEMETRY_API_NETWORK_REPORT

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**httpsLatencyRoutineData** | [**GoogleChromeManagementV1HttpsLatencyRoutineData**](GoogleChromeManagementV1HttpsLatencyRoutineData.md) |  |  [optional] |
|**httpsLatencyState** | [**HttpsLatencyStateEnum**](#HttpsLatencyStateEnum) | Current HTTPS latency state. |  [optional] |



## Enum: HttpsLatencyStateEnum

| Name | Value |
|---- | -----|
| HTTPS_LATENCY_STATE_UNSPECIFIED | &quot;HTTPS_LATENCY_STATE_UNSPECIFIED&quot; |
| RECOVERY | &quot;RECOVERY&quot; |
| PROBLEM | &quot;PROBLEM&quot; |



