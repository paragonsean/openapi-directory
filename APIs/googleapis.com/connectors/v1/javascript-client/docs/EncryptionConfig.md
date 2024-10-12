# ConnectorsApi.EncryptionConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryptionType** | **String** | Optional. Encryption type for the region. | [optional] 
**kmsKeyName** | **String** | Optional. KMS crypto key. This field accepts identifiers of the form &#x60;projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/ {crypto_key}&#x60; | [optional] 



## Enum: EncryptionTypeEnum


* `ENCRYPTION_TYPE_UNSPECIFIED` (value: `"ENCRYPTION_TYPE_UNSPECIFIED"`)

* `GMEK` (value: `"GMEK"`)

* `CMEK` (value: `"CMEK"`)




