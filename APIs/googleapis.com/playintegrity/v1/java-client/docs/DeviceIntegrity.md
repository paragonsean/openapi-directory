

# DeviceIntegrity

Contains the device attestation information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceRecognitionVerdict** | [**List&lt;DeviceRecognitionVerdictEnum&gt;**](#List&lt;DeviceRecognitionVerdictEnum&gt;) | Details about the integrity of the device the app is running on. |  [optional] |
|**recentDeviceActivity** | [**RecentDeviceActivity**](RecentDeviceActivity.md) |  |  [optional] |



## Enum: List&lt;DeviceRecognitionVerdictEnum&gt;

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| MEETS_BASIC_INTEGRITY | &quot;MEETS_BASIC_INTEGRITY&quot; |
| MEETS_DEVICE_INTEGRITY | &quot;MEETS_DEVICE_INTEGRITY&quot; |
| MEETS_STRONG_INTEGRITY | &quot;MEETS_STRONG_INTEGRITY&quot; |
| MEETS_VIRTUAL_INTEGRITY | &quot;MEETS_VIRTUAL_INTEGRITY&quot; |



