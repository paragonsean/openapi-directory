

# RawDecryptResponse

Response message for KeyManagementService.RawDecrypt.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**plaintext** | **byte[]** | The decrypted data. |  [optional] |
|**plaintextCrc32c** | **String** | Integrity verification field. A CRC32C checksum of the returned RawDecryptResponse.plaintext. An integrity check of plaintext can be performed by computing the CRC32C checksum of plaintext and comparing your results to this field. Discard the response in case of non-matching checksum values, and perform a limited number of retries. A persistent mismatch may indicate an issue in your computation of the CRC32C checksum. Note: receiving this response message indicates that KeyManagementService is able to successfully decrypt the ciphertext. Note: This field is defined as int64 for reasons of compatibility across different languages. However, it is a non-negative integer, which will never exceed 2^32-1, and can be safely downconverted to uint32 in languages that support this type. |  [optional] |
|**protectionLevel** | [**ProtectionLevelEnum**](#ProtectionLevelEnum) | The ProtectionLevel of the CryptoKeyVersion used in decryption. |  [optional] |
|**verifiedAdditionalAuthenticatedDataCrc32c** | **Boolean** | Integrity verification field. A flag indicating whether RawDecryptRequest.additional_authenticated_data_crc32c was received by KeyManagementService and used for the integrity verification of additional_authenticated_data. A false value of this field indicates either that // RawDecryptRequest.additional_authenticated_data_crc32c was left unset or that it was not delivered to KeyManagementService. If you&#39;ve set RawDecryptRequest.additional_authenticated_data_crc32c but this field is still false, discard the response and perform a limited number of retries. |  [optional] |
|**verifiedCiphertextCrc32c** | **Boolean** | Integrity verification field. A flag indicating whether RawDecryptRequest.ciphertext_crc32c was received by KeyManagementService and used for the integrity verification of the ciphertext. A false value of this field indicates either that RawDecryptRequest.ciphertext_crc32c was left unset or that it was not delivered to KeyManagementService. If you&#39;ve set RawDecryptRequest.ciphertext_crc32c but this field is still false, discard the response and perform a limited number of retries. |  [optional] |
|**verifiedInitializationVectorCrc32c** | **Boolean** | Integrity verification field. A flag indicating whether RawDecryptRequest.initialization_vector_crc32c was received by KeyManagementService and used for the integrity verification of initialization_vector. A false value of this field indicates either that RawDecryptRequest.initialization_vector_crc32c was left unset or that it was not delivered to KeyManagementService. If you&#39;ve set RawDecryptRequest.initialization_vector_crc32c but this field is still false, discard the response and perform a limited number of retries. |  [optional] |



## Enum: ProtectionLevelEnum

| Name | Value |
|---- | -----|
| PROTECTION_LEVEL_UNSPECIFIED | &quot;PROTECTION_LEVEL_UNSPECIFIED&quot; |
| SOFTWARE | &quot;SOFTWARE&quot; |
| HSM | &quot;HSM&quot; |
| EXTERNAL | &quot;EXTERNAL&quot; |
| EXTERNAL_VPC | &quot;EXTERNAL_VPC&quot; |



