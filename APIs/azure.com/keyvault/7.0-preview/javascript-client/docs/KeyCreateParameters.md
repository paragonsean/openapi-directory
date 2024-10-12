# KeyVaultClient.KeyCreateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**KeyAttributes**](KeyAttributes.md) |  | [optional] 
**crv** | **String** | Elliptic curve name. For valid values, see JsonWebKeyCurveName. | [optional] 
**keyOps** | **[String]** |  | [optional] 
**keySize** | **Number** | The key size in bits. For example: 2048, 3072, or 4096 for RSA. | [optional] 
**kty** | **String** | The type of key to create. For valid values, see JsonWebKeyType. | 
**tags** | **{String: String}** | Application specific metadata in the form of key-value pairs. | [optional] 



## Enum: CrvEnum


* `256` (value: `"P-256"`)

* `384` (value: `"P-384"`)

* `521` (value: `"P-521"`)

* `256K` (value: `"P-256K"`)





## Enum: [KeyOpsEnum]


* `encrypt` (value: `"encrypt"`)

* `decrypt` (value: `"decrypt"`)

* `sign` (value: `"sign"`)

* `verify` (value: `"verify"`)

* `wrapKey` (value: `"wrapKey"`)

* `unwrapKey` (value: `"unwrapKey"`)





## Enum: KtyEnum


* `EC` (value: `"EC"`)

* `EC-HSM` (value: `"EC-HSM"`)

* `RSA` (value: `"RSA"`)

* `RSA-HSM` (value: `"RSA-HSM"`)

* `oct` (value: `"oct"`)




