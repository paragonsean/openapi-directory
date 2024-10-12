# CloudKeyManagementServiceKmsApi.ImportJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attestation** | [**KeyOperationAttestation**](KeyOperationAttestation.md) |  | [optional] 
**createTime** | **String** | Output only. The time at which this ImportJob was created. | [optional] [readonly] 
**expireEventTime** | **String** | Output only. The time this ImportJob expired. Only present if state is EXPIRED. | [optional] [readonly] 
**expireTime** | **String** | Output only. The time at which this ImportJob is scheduled for expiration and can no longer be used to import key material. | [optional] [readonly] 
**generateTime** | **String** | Output only. The time this ImportJob&#39;s key material was generated. | [optional] [readonly] 
**importMethod** | **String** | Required. Immutable. The wrapping method to be used for incoming key material. | [optional] 
**name** | **String** | Output only. The resource name for this ImportJob in the format &#x60;projects/_*_/locations/_*_/keyRings/_*_/importJobs/_*&#x60;. | [optional] [readonly] 
**protectionLevel** | **String** | Required. Immutable. The protection level of the ImportJob. This must match the protection_level of the version_template on the CryptoKey you attempt to import into. | [optional] 
**publicKey** | [**WrappingPublicKey**](WrappingPublicKey.md) |  | [optional] 
**state** | **String** | Output only. The current state of the ImportJob, indicating if it can be used. | [optional] [readonly] 



## Enum: ImportMethodEnum


* `IMPORT_METHOD_UNSPECIFIED` (value: `"IMPORT_METHOD_UNSPECIFIED"`)

* `RSA_OAEP_3072_SHA1_AES_256` (value: `"RSA_OAEP_3072_SHA1_AES_256"`)

* `RSA_OAEP_4096_SHA1_AES_256` (value: `"RSA_OAEP_4096_SHA1_AES_256"`)

* `RSA_OAEP_3072_SHA256_AES_256` (value: `"RSA_OAEP_3072_SHA256_AES_256"`)

* `RSA_OAEP_4096_SHA256_AES_256` (value: `"RSA_OAEP_4096_SHA256_AES_256"`)

* `RSA_OAEP_3072_SHA256` (value: `"RSA_OAEP_3072_SHA256"`)

* `RSA_OAEP_4096_SHA256` (value: `"RSA_OAEP_4096_SHA256"`)





## Enum: ProtectionLevelEnum


* `PROTECTION_LEVEL_UNSPECIFIED` (value: `"PROTECTION_LEVEL_UNSPECIFIED"`)

* `SOFTWARE` (value: `"SOFTWARE"`)

* `HSM` (value: `"HSM"`)

* `EXTERNAL` (value: `"EXTERNAL"`)

* `EXTERNAL_VPC` (value: `"EXTERNAL_VPC"`)





## Enum: StateEnum


* `IMPORT_JOB_STATE_UNSPECIFIED` (value: `"IMPORT_JOB_STATE_UNSPECIFIED"`)

* `PENDING_GENERATION` (value: `"PENDING_GENERATION"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `EXPIRED` (value: `"EXPIRED"`)




