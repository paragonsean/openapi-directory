

# GooglePrivacyDlpV2CryptoKey

This is a data encryption key (DEK) (as opposed to a key encryption key (KEK) stored by Cloud Key Management Service (Cloud KMS). When using Cloud KMS to wrap or unwrap a DEK, be sure to set an appropriate IAM policy on the KEK to ensure an attacker cannot unwrap the DEK.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kmsWrapped** | [**GooglePrivacyDlpV2KmsWrappedCryptoKey**](GooglePrivacyDlpV2KmsWrappedCryptoKey.md) |  |  [optional] |
|**_transient** | [**GooglePrivacyDlpV2TransientCryptoKey**](GooglePrivacyDlpV2TransientCryptoKey.md) |  |  [optional] |
|**unwrapped** | [**GooglePrivacyDlpV2UnwrappedCryptoKey**](GooglePrivacyDlpV2UnwrappedCryptoKey.md) |  |  [optional] |



