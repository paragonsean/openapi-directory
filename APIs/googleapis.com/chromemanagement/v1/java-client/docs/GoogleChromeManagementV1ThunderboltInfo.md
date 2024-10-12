

# GoogleChromeManagementV1ThunderboltInfo

Thunderbolt bus info. * This field provides device information, which is static and will not change over time. * Data for this field is controlled via policy: [ReportDeviceSecurityStatus](https://chromeenterprise.google/policies/#ReportDeviceSecurityStatus) * Data Collection Frequency: At device startup * Default Data Reporting Frequency: At device startup - Policy Controlled: No * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: Yes * Reported for affiliated users only: N/A * Granular permission needed: TELEMETRY_API_BUS_DEVICE_INFO

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**securityLevel** | [**SecurityLevelEnum**](#SecurityLevelEnum) | Security level of the Thunderbolt bus. |  [optional] |



## Enum: SecurityLevelEnum

| Name | Value |
|---- | -----|
| LEVEL_UNSPECIFIED | &quot;THUNDERBOLT_SECURITY_LEVEL_UNSPECIFIED&quot; |
| NONE_LEVEL | &quot;THUNDERBOLT_SECURITY_NONE_LEVEL&quot; |
| USER_LEVEL | &quot;THUNDERBOLT_SECURITY_USER_LEVEL&quot; |
| SECURE_LEVEL | &quot;THUNDERBOLT_SECURITY_SECURE_LEVEL&quot; |
| DP_ONLY_LEVEL | &quot;THUNDERBOLT_SECURITY_DP_ONLY_LEVEL&quot; |
| USB_ONLY_LEVEL | &quot;THUNDERBOLT_SECURITY_USB_ONLY_LEVEL&quot; |
| NO_PCIE_LEVEL | &quot;THUNDERBOLT_SECURITY_NO_PCIE_LEVEL&quot; |



