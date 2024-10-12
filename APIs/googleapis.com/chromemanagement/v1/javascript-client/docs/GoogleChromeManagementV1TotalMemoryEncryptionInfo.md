# ChromeManagementApi.GoogleChromeManagementV1TotalMemoryEncryptionInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryptionAlgorithm** | **String** | Memory encryption algorithm. | [optional] 
**encryptionState** | **String** | The state of memory encryption on the device. | [optional] 
**keyLength** | **String** | The length of the encryption keys. | [optional] 
**maxKeys** | **String** | The maximum number of keys that can be used for encryption. | [optional] 



## Enum: EncryptionAlgorithmEnum


* `UNSPECIFIED` (value: `"MEMORY_ENCRYPTION_ALGORITHM_UNSPECIFIED"`)

* `UNKNOWN` (value: `"MEMORY_ENCRYPTION_ALGORITHM_UNKNOWN"`)

* `AES_XTS_128` (value: `"MEMORY_ENCRYPTION_ALGORITHM_AES_XTS_128"`)

* `AES_XTS_256` (value: `"MEMORY_ENCRYPTION_ALGORITHM_AES_XTS_256"`)





## Enum: EncryptionStateEnum


* `UNSPECIFIED` (value: `"MEMORY_ENCRYPTION_STATE_UNSPECIFIED"`)

* `UNKNOWN` (value: `"MEMORY_ENCRYPTION_STATE_UNKNOWN"`)

* `DISABLED` (value: `"MEMORY_ENCRYPTION_STATE_DISABLED"`)

* `TME` (value: `"MEMORY_ENCRYPTION_STATE_TME"`)

* `MKTME` (value: `"MEMORY_ENCRYPTION_STATE_MKTME"`)




