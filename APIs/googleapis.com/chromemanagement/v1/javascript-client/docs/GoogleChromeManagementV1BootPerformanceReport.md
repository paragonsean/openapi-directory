# ChromeManagementApi.GoogleChromeManagementV1BootPerformanceReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootUpDuration** | **String** | Total time to boot up. | [optional] 
**bootUpTime** | **String** | The timestamp when power came on. | [optional] 
**reportTime** | **String** | Timestamp when the report was collected. | [optional] 
**shutdownDuration** | **String** | Total time since shutdown start to power off. | [optional] 
**shutdownReason** | **String** | The shutdown reason. | [optional] 
**shutdownTime** | **String** | The timestamp when shutdown. | [optional] 



## Enum: ShutdownReasonEnum


* `SHUTDOWN_REASON_UNSPECIFIED` (value: `"SHUTDOWN_REASON_UNSPECIFIED"`)

* `USER_REQUEST` (value: `"USER_REQUEST"`)

* `SYSTEM_UPDATE` (value: `"SYSTEM_UPDATE"`)

* `LOW_BATTERY` (value: `"LOW_BATTERY"`)

* `OTHER` (value: `"OTHER"`)




