

# MacVerifyResponse

Response message for KeyManagementService.MacVerify.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The resource name of the CryptoKeyVersion used for verification. Check this field to verify that the intended resource was used for verification. |  [optional] |
|**protectionLevel** | [**ProtectionLevelEnum**](#ProtectionLevelEnum) | The ProtectionLevel of the CryptoKeyVersion used for verification. |  [optional] |
|**success** | **Boolean** | This field indicates whether or not the verification operation for MacVerifyRequest.mac over MacVerifyRequest.data was successful. |  [optional] |
|**verifiedDataCrc32c** | **Boolean** | Integrity verification field. A flag indicating whether MacVerifyRequest.data_crc32c was received by KeyManagementService and used for the integrity verification of the data. A false value of this field indicates either that MacVerifyRequest.data_crc32c was left unset or that it was not delivered to KeyManagementService. If you&#39;ve set MacVerifyRequest.data_crc32c but this field is still false, discard the response and perform a limited number of retries. |  [optional] |
|**verifiedMacCrc32c** | **Boolean** | Integrity verification field. A flag indicating whether MacVerifyRequest.mac_crc32c was received by KeyManagementService and used for the integrity verification of the data. A false value of this field indicates either that MacVerifyRequest.mac_crc32c was left unset or that it was not delivered to KeyManagementService. If you&#39;ve set MacVerifyRequest.mac_crc32c but this field is still false, discard the response and perform a limited number of retries. |  [optional] |
|**verifiedSuccessIntegrity** | **Boolean** | Integrity verification field. This value is used for the integrity verification of [MacVerifyResponse.success]. If the value of this field contradicts the value of [MacVerifyResponse.success], discard the response and perform a limited number of retries. |  [optional] |



## Enum: ProtectionLevelEnum

| Name | Value |
|---- | -----|
| PROTECTION_LEVEL_UNSPECIFIED | &quot;PROTECTION_LEVEL_UNSPECIFIED&quot; |
| SOFTWARE | &quot;SOFTWARE&quot; |
| HSM | &quot;HSM&quot; |
| EXTERNAL | &quot;EXTERNAL&quot; |
| EXTERNAL_VPC | &quot;EXTERNAL_VPC&quot; |



