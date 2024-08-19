

# ImportJob

An ImportJob can be used to create CryptoKeys and CryptoKeyVersions using pre-existing key material, generated outside of Cloud KMS. When an ImportJob is created, Cloud KMS will generate a \"wrapping key\", which is a public/private key pair. You use the wrapping key to encrypt (also known as wrap) the pre-existing key material to protect it during the import process. The nature of the wrapping key depends on the choice of import_method. When the wrapping key generation is complete, the state will be set to ACTIVE and the public_key can be fetched. The fetched public key can then be used to wrap your pre-existing key material. Once the key material is wrapped, it can be imported into a new CryptoKeyVersion in an existing CryptoKey by calling ImportCryptoKeyVersion. Multiple CryptoKeyVersions can be imported with a single ImportJob. Cloud KMS uses the private key portion of the wrapping key to unwrap the key material. Only Cloud KMS has access to the private key. An ImportJob expires 3 days after it is created. Once expired, Cloud KMS will no longer be able to import or unwrap any key material that was wrapped with the ImportJob's public key. For more information, see [Importing a key](https://cloud.google.com/kms/docs/importing-a-key).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attestation** | [**KeyOperationAttestation**](KeyOperationAttestation.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time at which this ImportJob was created. |  [optional] [readonly] |
|**expireEventTime** | **String** | Output only. The time this ImportJob expired. Only present if state is EXPIRED. |  [optional] [readonly] |
|**expireTime** | **String** | Output only. The time at which this ImportJob is scheduled for expiration and can no longer be used to import key material. |  [optional] [readonly] |
|**generateTime** | **String** | Output only. The time this ImportJob&#39;s key material was generated. |  [optional] [readonly] |
|**importMethod** | [**ImportMethodEnum**](#ImportMethodEnum) | Required. Immutable. The wrapping method to be used for incoming key material. |  [optional] |
|**name** | **String** | Output only. The resource name for this ImportJob in the format &#x60;projects/_*_/locations/_*_/keyRings/_*_/importJobs/_*&#x60;. |  [optional] [readonly] |
|**protectionLevel** | [**ProtectionLevelEnum**](#ProtectionLevelEnum) | Required. Immutable. The protection level of the ImportJob. This must match the protection_level of the version_template on the CryptoKey you attempt to import into. |  [optional] |
|**publicKey** | [**WrappingPublicKey**](WrappingPublicKey.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of the ImportJob, indicating if it can be used. |  [optional] [readonly] |



## Enum: ImportMethodEnum

| Name | Value |
|---- | -----|
| IMPORT_METHOD_UNSPECIFIED | &quot;IMPORT_METHOD_UNSPECIFIED&quot; |
| RSA_OAEP_3072_SHA1_AES_256 | &quot;RSA_OAEP_3072_SHA1_AES_256&quot; |
| RSA_OAEP_4096_SHA1_AES_256 | &quot;RSA_OAEP_4096_SHA1_AES_256&quot; |
| RSA_OAEP_3072_SHA256_AES_256 | &quot;RSA_OAEP_3072_SHA256_AES_256&quot; |
| RSA_OAEP_4096_SHA256_AES_256 | &quot;RSA_OAEP_4096_SHA256_AES_256&quot; |
| RSA_OAEP_3072_SHA256 | &quot;RSA_OAEP_3072_SHA256&quot; |
| RSA_OAEP_4096_SHA256 | &quot;RSA_OAEP_4096_SHA256&quot; |



## Enum: ProtectionLevelEnum

| Name | Value |
|---- | -----|
| PROTECTION_LEVEL_UNSPECIFIED | &quot;PROTECTION_LEVEL_UNSPECIFIED&quot; |
| SOFTWARE | &quot;SOFTWARE&quot; |
| HSM | &quot;HSM&quot; |
| EXTERNAL | &quot;EXTERNAL&quot; |
| EXTERNAL_VPC | &quot;EXTERNAL_VPC&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| IMPORT_JOB_STATE_UNSPECIFIED | &quot;IMPORT_JOB_STATE_UNSPECIFIED&quot; |
| PENDING_GENERATION | &quot;PENDING_GENERATION&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| EXPIRED | &quot;EXPIRED&quot; |



