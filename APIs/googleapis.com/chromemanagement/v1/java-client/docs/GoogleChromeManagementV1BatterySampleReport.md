

# GoogleChromeManagementV1BatterySampleReport

Sampling data for battery. * This field is telemetry information and this will change over time as the device is utilized. * Data for this field is controlled via policy: [ReportDevicePowerStatus](https://chromeenterprise.google/policies/#ReportDevicePowerStatus) * Data Collection Frequency: Only at Upload * Default Data Reporting Frequency: 3 hours - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: No * Reported for affiliated users only: N/A

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chargeRate** | **Integer** | Output only. Battery charge percentage. |  [optional] [readonly] |
|**current** | **String** | Output only. Battery current (mA). |  [optional] [readonly] |
|**dischargeRate** | **Integer** | Output only. The battery discharge rate measured in mW. Positive if the battery is being discharged, negative if it&#39;s being charged. |  [optional] [readonly] |
|**remainingCapacity** | **String** | Output only. Battery remaining capacity (mAmpere-hours). |  [optional] [readonly] |
|**reportTime** | **String** | Output only. Timestamp of when the sample was collected on device |  [optional] [readonly] |
|**status** | **String** | Output only. Battery status read from sysfs. Example: Discharging |  [optional] [readonly] |
|**temperature** | **Integer** | Output only. Temperature in Celsius degrees. |  [optional] [readonly] |
|**voltage** | **String** | Output only. Battery voltage (millivolt). |  [optional] [readonly] |



