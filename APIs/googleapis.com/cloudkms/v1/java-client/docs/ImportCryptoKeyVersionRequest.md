

# ImportCryptoKeyVersionRequest

Request message for KeyManagementService.ImportCryptoKeyVersion.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithm** | [**AlgorithmEnum**](#AlgorithmEnum) | Required. The algorithm of the key being imported. This does not need to match the version_template of the CryptoKey this version imports into. |  [optional] |
|**cryptoKeyVersion** | **String** | Optional. The optional name of an existing CryptoKeyVersion to target for an import operation. If this field is not present, a new CryptoKeyVersion containing the supplied key material is created. If this field is present, the supplied key material is imported into the existing CryptoKeyVersion. To import into an existing CryptoKeyVersion, the CryptoKeyVersion must be a child of ImportCryptoKeyVersionRequest.parent, have been previously created via ImportCryptoKeyVersion, and be in DESTROYED or IMPORT_FAILED state. The key material and algorithm must match the previous CryptoKeyVersion exactly if the CryptoKeyVersion has ever contained key material. |  [optional] |
|**importJob** | **String** | Required. The name of the ImportJob that was used to wrap this key material. |  [optional] |
|**rsaAesWrappedKey** | **byte[]** | Optional. This field has the same meaning as wrapped_key. Prefer to use that field in new work. Either that field or this field (but not both) must be specified. |  [optional] |
|**wrappedKey** | **byte[]** | Optional. The wrapped key material to import. Before wrapping, key material must be formatted. If importing symmetric key material, the expected key material format is plain bytes. If importing asymmetric key material, the expected key material format is PKCS#8-encoded DER (the PrivateKeyInfo structure from RFC 5208). When wrapping with import methods (RSA_OAEP_3072_SHA1_AES_256 or RSA_OAEP_4096_SHA1_AES_256 or RSA_OAEP_3072_SHA256_AES_256 or RSA_OAEP_4096_SHA256_AES_256), this field must contain the concatenation of: 1. An ephemeral AES-256 wrapping key wrapped with the public_key using RSAES-OAEP with SHA-1/SHA-256, MGF1 with SHA-1/SHA-256, and an empty label. 2. The formatted key to be imported, wrapped with the ephemeral AES-256 key using AES-KWP (RFC 5649). This format is the same as the format produced by PKCS#11 mechanism CKM_RSA_AES_KEY_WRAP. When wrapping with import methods (RSA_OAEP_3072_SHA256 or RSA_OAEP_4096_SHA256), this field must contain the formatted key to be imported, wrapped with the public_key using RSAES-OAEP with SHA-256, MGF1 with SHA-256, and an empty label. |  [optional] |



## Enum: AlgorithmEnum

| Name | Value |
|---- | -----|
| CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED | &quot;CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED&quot; |
| GOOGLE_SYMMETRIC_ENCRYPTION | &quot;GOOGLE_SYMMETRIC_ENCRYPTION&quot; |
| AES_128_GCM | &quot;AES_128_GCM&quot; |
| AES_256_GCM | &quot;AES_256_GCM&quot; |
| AES_128_CBC | &quot;AES_128_CBC&quot; |
| AES_256_CBC | &quot;AES_256_CBC&quot; |
| AES_128_CTR | &quot;AES_128_CTR&quot; |
| AES_256_CTR | &quot;AES_256_CTR&quot; |
| RSA_SIGN_PSS_2048_SHA256 | &quot;RSA_SIGN_PSS_2048_SHA256&quot; |
| RSA_SIGN_PSS_3072_SHA256 | &quot;RSA_SIGN_PSS_3072_SHA256&quot; |
| RSA_SIGN_PSS_4096_SHA256 | &quot;RSA_SIGN_PSS_4096_SHA256&quot; |
| RSA_SIGN_PSS_4096_SHA512 | &quot;RSA_SIGN_PSS_4096_SHA512&quot; |
| RSA_SIGN_PKCS1_2048_SHA256 | &quot;RSA_SIGN_PKCS1_2048_SHA256&quot; |
| RSA_SIGN_PKCS1_3072_SHA256 | &quot;RSA_SIGN_PKCS1_3072_SHA256&quot; |
| RSA_SIGN_PKCS1_4096_SHA256 | &quot;RSA_SIGN_PKCS1_4096_SHA256&quot; |
| RSA_SIGN_PKCS1_4096_SHA512 | &quot;RSA_SIGN_PKCS1_4096_SHA512&quot; |
| RSA_SIGN_RAW_PKCS1_2048 | &quot;RSA_SIGN_RAW_PKCS1_2048&quot; |
| RSA_SIGN_RAW_PKCS1_3072 | &quot;RSA_SIGN_RAW_PKCS1_3072&quot; |
| RSA_SIGN_RAW_PKCS1_4096 | &quot;RSA_SIGN_RAW_PKCS1_4096&quot; |
| RSA_DECRYPT_OAEP_2048_SHA256 | &quot;RSA_DECRYPT_OAEP_2048_SHA256&quot; |
| RSA_DECRYPT_OAEP_3072_SHA256 | &quot;RSA_DECRYPT_OAEP_3072_SHA256&quot; |
| RSA_DECRYPT_OAEP_4096_SHA256 | &quot;RSA_DECRYPT_OAEP_4096_SHA256&quot; |
| RSA_DECRYPT_OAEP_4096_SHA512 | &quot;RSA_DECRYPT_OAEP_4096_SHA512&quot; |
| RSA_DECRYPT_OAEP_2048_SHA1 | &quot;RSA_DECRYPT_OAEP_2048_SHA1&quot; |
| RSA_DECRYPT_OAEP_3072_SHA1 | &quot;RSA_DECRYPT_OAEP_3072_SHA1&quot; |
| RSA_DECRYPT_OAEP_4096_SHA1 | &quot;RSA_DECRYPT_OAEP_4096_SHA1&quot; |
| EC_SIGN_P256_SHA256 | &quot;EC_SIGN_P256_SHA256&quot; |
| EC_SIGN_P384_SHA384 | &quot;EC_SIGN_P384_SHA384&quot; |
| EC_SIGN_SECP256_K1_SHA256 | &quot;EC_SIGN_SECP256K1_SHA256&quot; |
| HMAC_SHA256 | &quot;HMAC_SHA256&quot; |
| HMAC_SHA1 | &quot;HMAC_SHA1&quot; |
| HMAC_SHA384 | &quot;HMAC_SHA384&quot; |
| HMAC_SHA512 | &quot;HMAC_SHA512&quot; |
| HMAC_SHA224 | &quot;HMAC_SHA224&quot; |
| EXTERNAL_SYMMETRIC_ENCRYPTION | &quot;EXTERNAL_SYMMETRIC_ENCRYPTION&quot; |



