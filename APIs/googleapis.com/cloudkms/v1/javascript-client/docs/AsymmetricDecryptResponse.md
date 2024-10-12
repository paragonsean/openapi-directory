# CloudKeyManagementServiceKmsApi.AsymmetricDecryptResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plaintext** | **Blob** | The decrypted data originally encrypted with the matching public key. | [optional] 
**plaintextCrc32c** | **String** | Integrity verification field. A CRC32C checksum of the returned AsymmetricDecryptResponse.plaintext. An integrity check of AsymmetricDecryptResponse.plaintext can be performed by computing the CRC32C checksum of AsymmetricDecryptResponse.plaintext and comparing your results to this field. Discard the response in case of non-matching checksum values, and perform a limited number of retries. A persistent mismatch may indicate an issue in your computation of the CRC32C checksum. Note: This field is defined as int64 for reasons of compatibility across different languages. However, it is a non-negative integer, which will never exceed 2^32-1, and can be safely downconverted to uint32 in languages that support this type. | [optional] 
**protectionLevel** | **String** | The ProtectionLevel of the CryptoKeyVersion used in decryption. | [optional] 
**verifiedCiphertextCrc32c** | **Boolean** | Integrity verification field. A flag indicating whether AsymmetricDecryptRequest.ciphertext_crc32c was received by KeyManagementService and used for the integrity verification of the ciphertext. A false value of this field indicates either that AsymmetricDecryptRequest.ciphertext_crc32c was left unset or that it was not delivered to KeyManagementService. If you&#39;ve set AsymmetricDecryptRequest.ciphertext_crc32c but this field is still false, discard the response and perform a limited number of retries. | [optional] 



## Enum: ProtectionLevelEnum


* `PROTECTION_LEVEL_UNSPECIFIED` (value: `"PROTECTION_LEVEL_UNSPECIFIED"`)

* `SOFTWARE` (value: `"SOFTWARE"`)

* `HSM` (value: `"HSM"`)

* `EXTERNAL` (value: `"EXTERNAL"`)

* `EXTERNAL_VPC` (value: `"EXTERNAL_VPC"`)




