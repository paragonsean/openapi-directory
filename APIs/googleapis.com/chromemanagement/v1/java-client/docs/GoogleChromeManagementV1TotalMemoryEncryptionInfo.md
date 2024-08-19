

# GoogleChromeManagementV1TotalMemoryEncryptionInfo

Memory encryption information of a device. * This field provides device information, which is static and will not change over time. * Data for this field is controlled via policy: [ReportDeviceMemoryInfo](https://chromeenterprise.google/policies/#ReportDeviceMemoryInfo) * Data Collection Frequency: At device startup * Default Data Reporting Frequency: At device startup - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: Yes * Reported for affiliated users only: N/A

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptionAlgorithm** | [**EncryptionAlgorithmEnum**](#EncryptionAlgorithmEnum) | Memory encryption algorithm. |  [optional] |
|**encryptionState** | [**EncryptionStateEnum**](#EncryptionStateEnum) | The state of memory encryption on the device. |  [optional] |
|**keyLength** | **String** | The length of the encryption keys. |  [optional] |
|**maxKeys** | **String** | The maximum number of keys that can be used for encryption. |  [optional] |



## Enum: EncryptionAlgorithmEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;MEMORY_ENCRYPTION_ALGORITHM_UNSPECIFIED&quot; |
| UNKNOWN | &quot;MEMORY_ENCRYPTION_ALGORITHM_UNKNOWN&quot; |
| AES_XTS_128 | &quot;MEMORY_ENCRYPTION_ALGORITHM_AES_XTS_128&quot; |
| AES_XTS_256 | &quot;MEMORY_ENCRYPTION_ALGORITHM_AES_XTS_256&quot; |



## Enum: EncryptionStateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;MEMORY_ENCRYPTION_STATE_UNSPECIFIED&quot; |
| UNKNOWN | &quot;MEMORY_ENCRYPTION_STATE_UNKNOWN&quot; |
| DISABLED | &quot;MEMORY_ENCRYPTION_STATE_DISABLED&quot; |
| TME | &quot;MEMORY_ENCRYPTION_STATE_TME&quot; |
| MKTME | &quot;MEMORY_ENCRYPTION_STATE_MKTME&quot; |



