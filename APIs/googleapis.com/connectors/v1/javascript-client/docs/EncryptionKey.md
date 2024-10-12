# ConnectorsApi.EncryptionKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kmsKeyName** | **String** | The [KMS key name] with which the content of the Operation is encrypted. The expected format: &#x60;projects/_*_/locations/_*_/keyRings/_*_/cryptoKeys/_*&#x60;. Will be empty string if google managed. | [optional] 
**type** | **String** | Type. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `GOOGLE_MANAGED` (value: `"GOOGLE_MANAGED"`)

* `CUSTOMER_MANAGED` (value: `"CUSTOMER_MANAGED"`)




