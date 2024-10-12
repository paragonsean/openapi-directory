# ChromeManagementApi.GoogleChromeManagementV1CpuInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **String** | Output only. Architecture type for the CPU. * This field provides device information, which is static and will not change over time. * Data for this field is controlled via policy: [ReportDeviceCpuInfo](https://chromeenterprise.google/policies/#ReportDeviceCpuInfo) * Data Collection Frequency: Only at Upload * Default Data Reporting Frequency: 3 hours - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: No * Reported for affiliated users only: N/A | [optional] [readonly] 
**keylockerConfigured** | **Boolean** | Output only. Whether keylocker is configured.&#x60;TRUE&#x60; &#x3D; Enabled; &#x60;FALSE&#x60; &#x3D; disabled. Only reported if keylockerSupported &#x3D; &#x60;TRUE&#x60;. | [optional] [readonly] 
**keylockerSupported** | **Boolean** | Output only. Whether keylocker is supported. | [optional] [readonly] 
**maxClockSpeed** | **Number** | Output only. The max CPU clock speed in kHz. | [optional] [readonly] 
**model** | **String** | Output only. The CPU model name. Example: Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz | [optional] [readonly] 



## Enum: ArchitectureEnum


* `ARCHITECTURE_UNSPECIFIED` (value: `"ARCHITECTURE_UNSPECIFIED"`)

* `X64` (value: `"X64"`)




