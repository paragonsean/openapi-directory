# CloudKeyManagementServiceKmsApi.GenerateRandomBytesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lengthBytes** | **Number** | The length in bytes of the amount of randomness to retrieve. Minimum 8 bytes, maximum 1024 bytes. | [optional] 
**protectionLevel** | **String** | The ProtectionLevel to use when generating the random data. Currently, only HSM protection level is supported. | [optional] 



## Enum: ProtectionLevelEnum


* `PROTECTION_LEVEL_UNSPECIFIED` (value: `"PROTECTION_LEVEL_UNSPECIFIED"`)

* `SOFTWARE` (value: `"SOFTWARE"`)

* `HSM` (value: `"HSM"`)

* `EXTERNAL` (value: `"EXTERNAL"`)

* `EXTERNAL_VPC` (value: `"EXTERNAL_VPC"`)




