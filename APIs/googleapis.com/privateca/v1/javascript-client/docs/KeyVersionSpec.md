# CertificateAuthorityApi.KeyVersionSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **String** | The algorithm to use for creating a managed Cloud KMS key for a for a simplified experience. All managed keys will be have their ProtectionLevel as &#x60;HSM&#x60;. | [optional] 
**cloudKmsKeyVersion** | **String** | The resource name for an existing Cloud KMS CryptoKeyVersion in the format &#x60;projects/_*_/locations/_*_/keyRings/_*_/cryptoKeys/_*_/cryptoKeyVersions/_*&#x60;. This option enables full flexibility in the key&#39;s capabilities and properties. | [optional] 



## Enum: AlgorithmEnum


* `SIGN_HASH_ALGORITHM_UNSPECIFIED` (value: `"SIGN_HASH_ALGORITHM_UNSPECIFIED"`)

* `RSA_PSS_2048_SHA256` (value: `"RSA_PSS_2048_SHA256"`)

* `RSA_PSS_3072_SHA256` (value: `"RSA_PSS_3072_SHA256"`)

* `RSA_PSS_4096_SHA256` (value: `"RSA_PSS_4096_SHA256"`)

* `RSA_PKCS1_2048_SHA256` (value: `"RSA_PKCS1_2048_SHA256"`)

* `RSA_PKCS1_3072_SHA256` (value: `"RSA_PKCS1_3072_SHA256"`)

* `RSA_PKCS1_4096_SHA256` (value: `"RSA_PKCS1_4096_SHA256"`)

* `EC_P256_SHA256` (value: `"EC_P256_SHA256"`)

* `EC_P384_SHA384` (value: `"EC_P384_SHA384"`)




