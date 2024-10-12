

# GooglePrivacyDlpV2KmsWrappedCryptoKey

Include to use an existing data crypto key wrapped by KMS. The wrapped key must be a 128-, 192-, or 256-bit key. Authorization requires the following IAM permissions when sending a request to perform a crypto transformation using a KMS-wrapped crypto key: dlp.kms.encrypt For more information, see [Creating a wrapped key] (https://cloud.google.com/sensitive-data-protection/docs/create-wrapped-key). Note: When you use Cloud KMS for cryptographic operations, [charges apply](https://cloud.google.com/kms/pricing).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cryptoKeyName** | **String** | Required. The resource name of the KMS CryptoKey to use for unwrapping. |  [optional] |
|**wrappedKey** | **byte[]** | Required. The wrapped data crypto key. |  [optional] |



