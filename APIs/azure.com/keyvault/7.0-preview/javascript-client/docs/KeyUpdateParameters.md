# KeyVaultClient.KeyUpdateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**KeyAttributes**](KeyAttributes.md) |  | [optional] 
**keyOps** | **[String]** | Json web key operations. For more information on possible key operations, see JsonWebKeyOperation. | [optional] 
**tags** | **{String: String}** | Application specific metadata in the form of key-value pairs. | [optional] 



## Enum: [KeyOpsEnum]


* `encrypt` (value: `"encrypt"`)

* `decrypt` (value: `"decrypt"`)

* `sign` (value: `"sign"`)

* `verify` (value: `"verify"`)

* `wrapKey` (value: `"wrapKey"`)

* `unwrapKey` (value: `"unwrapKey"`)




