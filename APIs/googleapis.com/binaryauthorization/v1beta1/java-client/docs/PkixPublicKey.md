

# PkixPublicKey

A public key in the PkixPublicKey format (see https://tools.ietf.org/html/rfc5280#section-4.1.2.7 for details). Public keys of this type are typically textually encoded using the PEM format.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**publicKeyPem** | **String** | A PEM-encoded public key, as described in https://tools.ietf.org/html/rfc7468#section-13 |  [optional] |
|**signatureAlgorithm** | [**SignatureAlgorithmEnum**](#SignatureAlgorithmEnum) | The signature algorithm used to verify a message against a signature using this key. These signature algorithm must match the structure and any object identifiers encoded in &#x60;public_key_pem&#x60; (i.e. this algorithm must match that of the public key). |  [optional] |



## Enum: SignatureAlgorithmEnum

| Name | Value |
|---- | -----|
| SIGNATURE_ALGORITHM_UNSPECIFIED | &quot;SIGNATURE_ALGORITHM_UNSPECIFIED&quot; |
| RSA_PSS_2048_SHA256 | &quot;RSA_PSS_2048_SHA256&quot; |
| RSA_SIGN_PSS_2048_SHA256 | &quot;RSA_SIGN_PSS_2048_SHA256&quot; |
| RSA_PSS_3072_SHA256 | &quot;RSA_PSS_3072_SHA256&quot; |
| RSA_SIGN_PSS_3072_SHA256 | &quot;RSA_SIGN_PSS_3072_SHA256&quot; |
| RSA_PSS_4096_SHA256 | &quot;RSA_PSS_4096_SHA256&quot; |
| RSA_SIGN_PSS_4096_SHA256 | &quot;RSA_SIGN_PSS_4096_SHA256&quot; |
| RSA_PSS_4096_SHA512 | &quot;RSA_PSS_4096_SHA512&quot; |
| RSA_SIGN_PSS_4096_SHA512 | &quot;RSA_SIGN_PSS_4096_SHA512&quot; |
| RSA_SIGN_PKCS1_2048_SHA256 | &quot;RSA_SIGN_PKCS1_2048_SHA256&quot; |
| RSA_SIGN_PKCS1_3072_SHA256 | &quot;RSA_SIGN_PKCS1_3072_SHA256&quot; |
| RSA_SIGN_PKCS1_4096_SHA256 | &quot;RSA_SIGN_PKCS1_4096_SHA256&quot; |
| RSA_SIGN_PKCS1_4096_SHA512 | &quot;RSA_SIGN_PKCS1_4096_SHA512&quot; |
| ECDSA_P256_SHA256 | &quot;ECDSA_P256_SHA256&quot; |
| EC_SIGN_P256_SHA256 | &quot;EC_SIGN_P256_SHA256&quot; |
| ECDSA_P384_SHA384 | &quot;ECDSA_P384_SHA384&quot; |
| EC_SIGN_P384_SHA384 | &quot;EC_SIGN_P384_SHA384&quot; |
| ECDSA_P521_SHA512 | &quot;ECDSA_P521_SHA512&quot; |
| EC_SIGN_P521_SHA512 | &quot;EC_SIGN_P521_SHA512&quot; |



