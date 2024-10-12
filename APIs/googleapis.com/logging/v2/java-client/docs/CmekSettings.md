

# CmekSettings

Describes the customer-managed encryption key (CMEK) settings associated with a project, folder, organization, billing account, or flexible resource.Note: CMEK for the Log Router can currently only be configured for Google Cloud organizations. Once configured, it applies to all projects and folders in the Google Cloud organization.See Enabling CMEK for Log Router (https://cloud.google.com/logging/docs/routing/managed-encryption) for more information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kmsKeyName** | **String** | Optional. The resource name for the configured Cloud KMS key.KMS key name format: \&quot;projects/[PROJECT_ID]/locations/[LOCATION]/keyRings/[KEYRING]/cryptoKeys/[KEY]\&quot; For example:\&quot;projects/my-project/locations/us-central1/keyRings/my-ring/cryptoKeys/my-key\&quot;To enable CMEK for the Log Router, set this field to a valid kms_key_name for which the associated service account has the needed cloudkms.cryptoKeyEncrypterDecrypter roles assigned for the key.The Cloud KMS key used by the Log Router can be updated by changing the kms_key_name to a new valid key name or disabled by setting the key name to an empty string. Encryption operations that are in progress will be completed with the key that was in use when they started. Decryption operations will be completed using the key that was used at the time of encryption unless access to that key has been revoked.To disable CMEK for the Log Router, set this field to an empty string.See Enabling CMEK for Log Router (https://cloud.google.com/logging/docs/routing/managed-encryption) for more information. |  [optional] |
|**kmsKeyVersionName** | **String** | Output only. The CryptoKeyVersion resource name for the configured Cloud KMS key.KMS key name format: \&quot;projects/[PROJECT_ID]/locations/[LOCATION]/keyRings/[KEYRING]/cryptoKeys/[KEY]/cryptoKeyVersions/[VERSION]\&quot; For example:\&quot;projects/my-project/locations/us-central1/keyRings/my-ring/cryptoKeys/my-key/cryptoKeyVersions/1\&quot;This is a read-only field used to convey the specific configured CryptoKeyVersion of kms_key that has been configured. It will be populated in cases where the CMEK settings are bound to a single key version.If this field is populated, the kms_key is tied to a specific CryptoKeyVersion. |  [optional] [readonly] |
|**name** | **String** | Output only. The resource name of the CMEK settings. |  [optional] [readonly] |
|**serviceAccountId** | **String** | Output only. The service account that will be used by the Log Router to access your Cloud KMS key.Before enabling CMEK for Log Router, you must first assign the cloudkms.cryptoKeyEncrypterDecrypter role to the service account that the Log Router will use to access your Cloud KMS key. Use GetCmekSettings to obtain the service account ID.See Enabling CMEK for Log Router (https://cloud.google.com/logging/docs/routing/managed-encryption) for more information. |  [optional] [readonly] |



