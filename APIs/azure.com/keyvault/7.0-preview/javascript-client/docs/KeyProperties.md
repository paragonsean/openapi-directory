# KeyVaultClient.KeyProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crv** | **String** | Elliptic curve name. For valid values, see JsonWebKeyCurveName. | [optional] 
**exportable** | **Boolean** | Indicates if the private key can be exported. | [optional] 
**keySize** | **Number** | The key size in bits. For example: 2048, 3072, or 4096 for RSA. | [optional] 
**kty** | **String** | The type of key pair to be used for the certificate. | [optional] 
**reuseKey** | **Boolean** | Indicates if the same key pair will be used on certificate renewal. | [optional] 



## Enum: CrvEnum


* `256` (value: `"P-256"`)

* `384` (value: `"P-384"`)

* `521` (value: `"P-521"`)

* `256K` (value: `"P-256K"`)





## Enum: KtyEnum


* `EC` (value: `"EC"`)

* `EC-HSM` (value: `"EC-HSM"`)

* `RSA` (value: `"RSA"`)

* `RSA-HSM` (value: `"RSA-HSM"`)

* `oct` (value: `"oct"`)




