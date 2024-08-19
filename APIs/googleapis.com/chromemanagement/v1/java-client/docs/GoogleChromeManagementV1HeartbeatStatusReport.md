

# GoogleChromeManagementV1HeartbeatStatusReport

Heartbeat status report of a device. * Available for Kiosks * This field provides online/offline/unknown status of a device and will only be included if the status has changed (e.g. Online -> Offline) * Data for this field is controlled via policy: [HeartbeatEnabled](https://chromeenterprise.google/policies/#HeartbeatEnabled) [More Info](https://support.google.com/chrome/a/answer/6179663#:~:text=On%20the%20Chrome,device%20status%20alerts) * Heartbeat Frequency: 2 mins * Note: If a device goes offline, it can take up to 12 minutes for the online status of the device to be updated * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: N/A * Reported for affiliated users only: N/A * Granular permission needed: TELEMETRY_API_DEVICE_ACTIVITY_REPORT

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reportTime** | **String** | Timestamp of when status changed was detected |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State the device changed to |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ONLINE | &quot;ONLINE&quot; |
| OFFLINE | &quot;OFFLINE&quot; |



