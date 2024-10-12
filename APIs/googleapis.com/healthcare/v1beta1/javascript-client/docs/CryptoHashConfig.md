# CloudHealthcareApi.CryptoHashConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cryptoKey** | **Blob** | An AES 128/192/256 bit key. Causes the hash to be computed based on this key. A default key is generated for each Deidentify operation and is used when neither crypto_key nor kms_wrapped is specified. Must not be set if kms_wrapped is set. | [optional] 
**kmsWrapped** | [**KmsWrappedCryptoKey**](KmsWrappedCryptoKey.md) |  | [optional] 


