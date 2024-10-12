

# GoogleChromeManagementV1AudioStatusReport

Status data for storage. * This field is telemetry information and this will change over time as the device is utilized. * Data for this field is controlled via policy: [ReportDeviceAudioStatus](https://chromeenterprise.google/policies/#ReportDeviceAudioStatus) * Data Collection Frequency: 10 minutes * Default Data Reporting Frequency: 3 hours - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: No * Reported for affiliated users only: N/A * Granular permission needed: TELEMETRY_API_AUDIO_REPORT

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inputDevice** | **String** | Output only. Active input device&#39;s name. |  [optional] [readonly] |
|**inputGain** | **Integer** | Output only. Active input device&#39;s gain in [0, 100]. |  [optional] [readonly] |
|**inputMute** | **Boolean** | Output only. Is active input device mute or not. |  [optional] [readonly] |
|**outputDevice** | **String** | Output only. Active output device&#39;s name. |  [optional] [readonly] |
|**outputMute** | **Boolean** | Output only. Is active output device mute or not. |  [optional] [readonly] |
|**outputVolume** | **Integer** | Output only. Active output device&#39;s volume in [0, 100]. |  [optional] [readonly] |
|**reportTime** | **String** | Output only. Timestamp of when the sample was collected on device. |  [optional] [readonly] |



