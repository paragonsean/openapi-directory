# ChromeManagementApi.GoogleChromeManagementV1BatteryStatusReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batteryHealth** | **String** | Output only. Battery health. | [optional] [readonly] 
**cycleCount** | **Number** | Output only. Cycle count. | [optional] [readonly] 
**fullChargeCapacity** | **String** | Output only. Full charge capacity (mAmpere-hours). | [optional] [readonly] 
**reportTime** | **String** | Output only. Timestamp of when the sample was collected on device | [optional] [readonly] 
**sample** | [**[GoogleChromeManagementV1BatterySampleReport]**](GoogleChromeManagementV1BatterySampleReport.md) | Output only. Sampling data for the battery sorted in a decreasing order of report_time. | [optional] [readonly] 
**serialNumber** | **String** | Output only. Battery serial number. | [optional] [readonly] 



## Enum: BatteryHealthEnum


* `HEALTH_UNSPECIFIED` (value: `"BATTERY_HEALTH_UNSPECIFIED"`)

* `HEALTH_NORMAL` (value: `"BATTERY_HEALTH_NORMAL"`)

* `REPLACE_SOON` (value: `"BATTERY_REPLACE_SOON"`)

* `REPLACE_NOW` (value: `"BATTERY_REPLACE_NOW"`)




