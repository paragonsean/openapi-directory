# BinaryAuthorizationApi.PkixPublicKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publicKeyPem** | **String** | A PEM-encoded public key, as described in https://tools.ietf.org/html/rfc7468#section-13 | [optional] 
**signatureAlgorithm** | **String** | The signature algorithm used to verify a message against a signature using this key. These signature algorithm must match the structure and any object identifiers encoded in &#x60;public_key_pem&#x60; (i.e. this algorithm must match that of the public key). | [optional] 



## Enum: SignatureAlgorithmEnum


* `SIGNATURE_ALGORITHM_UNSPECIFIED` (value: `"SIGNATURE_ALGORITHM_UNSPECIFIED"`)

* `RSA_PSS_2048_SHA256` (value: `"RSA_PSS_2048_SHA256"`)

* `RSA_SIGN_PSS_2048_SHA256` (value: `"RSA_SIGN_PSS_2048_SHA256"`)

* `RSA_PSS_3072_SHA256` (value: `"RSA_PSS_3072_SHA256"`)

* `RSA_SIGN_PSS_3072_SHA256` (value: `"RSA_SIGN_PSS_3072_SHA256"`)

* `RSA_PSS_4096_SHA256` (value: `"RSA_PSS_4096_SHA256"`)

* `RSA_SIGN_PSS_4096_SHA256` (value: `"RSA_SIGN_PSS_4096_SHA256"`)

* `RSA_PSS_4096_SHA512` (value: `"RSA_PSS_4096_SHA512"`)

* `RSA_SIGN_PSS_4096_SHA512` (value: `"RSA_SIGN_PSS_4096_SHA512"`)

* `RSA_SIGN_PKCS1_2048_SHA256` (value: `"RSA_SIGN_PKCS1_2048_SHA256"`)

* `RSA_SIGN_PKCS1_3072_SHA256` (value: `"RSA_SIGN_PKCS1_3072_SHA256"`)

* `RSA_SIGN_PKCS1_4096_SHA256` (value: `"RSA_SIGN_PKCS1_4096_SHA256"`)

* `RSA_SIGN_PKCS1_4096_SHA512` (value: `"RSA_SIGN_PKCS1_4096_SHA512"`)

* `ECDSA_P256_SHA256` (value: `"ECDSA_P256_SHA256"`)

* `EC_SIGN_P256_SHA256` (value: `"EC_SIGN_P256_SHA256"`)

* `ECDSA_P384_SHA384` (value: `"ECDSA_P384_SHA384"`)

* `EC_SIGN_P384_SHA384` (value: `"EC_SIGN_P384_SHA384"`)

* `ECDSA_P521_SHA512` (value: `"ECDSA_P521_SHA512"`)

* `EC_SIGN_P521_SHA512` (value: `"EC_SIGN_P521_SHA512"`)




