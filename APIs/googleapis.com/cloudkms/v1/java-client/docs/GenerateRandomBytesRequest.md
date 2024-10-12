

# GenerateRandomBytesRequest

Request message for KeyManagementService.GenerateRandomBytes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lengthBytes** | **Integer** | The length in bytes of the amount of randomness to retrieve. Minimum 8 bytes, maximum 1024 bytes. |  [optional] |
|**protectionLevel** | [**ProtectionLevelEnum**](#ProtectionLevelEnum) | The ProtectionLevel to use when generating the random data. Currently, only HSM protection level is supported. |  [optional] |



## Enum: ProtectionLevelEnum

| Name | Value |
|---- | -----|
| PROTECTION_LEVEL_UNSPECIFIED | &quot;PROTECTION_LEVEL_UNSPECIFIED&quot; |
| SOFTWARE | &quot;SOFTWARE&quot; |
| HSM | &quot;HSM&quot; |
| EXTERNAL | &quot;EXTERNAL&quot; |
| EXTERNAL_VPC | &quot;EXTERNAL_VPC&quot; |



