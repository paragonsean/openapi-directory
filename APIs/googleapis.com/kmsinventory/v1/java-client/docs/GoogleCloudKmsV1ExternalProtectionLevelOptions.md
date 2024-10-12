

# GoogleCloudKmsV1ExternalProtectionLevelOptions

ExternalProtectionLevelOptions stores a group of additional fields for configuring a CryptoKeyVersion that are specific to the EXTERNAL protection level and EXTERNAL_VPC protection levels.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ekmConnectionKeyPath** | **String** | The path to the external key material on the EKM when using EkmConnection e.g., \&quot;v0/my/key\&quot;. Set this field instead of external_key_uri when using an EkmConnection. |  [optional] |
|**externalKeyUri** | **String** | The URI for an external resource that this CryptoKeyVersion represents. |  [optional] |



