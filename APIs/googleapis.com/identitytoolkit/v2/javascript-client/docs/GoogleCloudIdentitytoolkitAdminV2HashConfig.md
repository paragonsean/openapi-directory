# IdentityToolkitApi.GoogleCloudIdentitytoolkitAdminV2HashConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **String** | Output only. Different password hash algorithms used in Identity Toolkit. | [optional] [readonly] 
**memoryCost** | **Number** | Output only. Memory cost for hash calculation. Used by scrypt and other similar password derivation algorithms. See https://tools.ietf.org/html/rfc7914 for explanation of field. | [optional] [readonly] 
**rounds** | **Number** | Output only. How many rounds for hash calculation. Used by scrypt and other similar password derivation algorithms. | [optional] [readonly] 
**saltSeparator** | **String** | Output only. Non-printable character to be inserted between the salt and plain text password in base64. | [optional] [readonly] 
**signerKey** | **String** | Output only. Signer key in base64. | [optional] [readonly] 



## Enum: AlgorithmEnum


* `HASH_ALGORITHM_UNSPECIFIED` (value: `"HASH_ALGORITHM_UNSPECIFIED"`)

* `HMAC_SHA256` (value: `"HMAC_SHA256"`)

* `HMAC_SHA1` (value: `"HMAC_SHA1"`)

* `HMAC_MD5` (value: `"HMAC_MD5"`)

* `SCRYPT` (value: `"SCRYPT"`)

* `PBKDF_SHA1` (value: `"PBKDF_SHA1"`)

* `MD5` (value: `"MD5"`)

* `HMAC_SHA512` (value: `"HMAC_SHA512"`)

* `SHA1` (value: `"SHA1"`)

* `BCRYPT` (value: `"BCRYPT"`)

* `PBKDF2_SHA256` (value: `"PBKDF2_SHA256"`)

* `SHA256` (value: `"SHA256"`)

* `SHA512` (value: `"SHA512"`)

* `STANDARD_SCRYPT` (value: `"STANDARD_SCRYPT"`)




