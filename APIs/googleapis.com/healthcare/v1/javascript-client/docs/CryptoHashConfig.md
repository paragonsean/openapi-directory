# CloudHealthcareApi.CryptoHashConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cryptoKey** | **Blob** | An AES 128/192/256 bit key. Causes the hash to be computed based on this key. A default key is generated for each Deidentify operation and is used when neither &#x60;crypto_key&#x60; nor &#x60;kms_wrapped&#x60; is specified. Must not be set if &#x60;kms_wrapped&#x60; is set. | [optional] 
**kmsWrapped** | [**KmsWrappedCryptoKey**](KmsWrappedCryptoKey.md) |  | [optional] 


