

# KeyVerifyParameters

The key verify parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alg** | [**AlgEnum**](#AlgEnum) | The signing/verification algorithm. For more information on possible algorithm types, see JsonWebKeySignatureAlgorithm. |  |
|**digest** | **String** | The digest used for signing. |  |
|**value** | **String** | The signature to be verified. |  |



## Enum: AlgEnum

| Name | Value |
|---- | -----|
| PS256 | &quot;PS256&quot; |
| PS384 | &quot;PS384&quot; |
| PS512 | &quot;PS512&quot; |
| RS256 | &quot;RS256&quot; |
| RS384 | &quot;RS384&quot; |
| RS512 | &quot;RS512&quot; |
| RSNULL | &quot;RSNULL&quot; |
| ES256 | &quot;ES256&quot; |
| ES384 | &quot;ES384&quot; |
| ES512 | &quot;ES512&quot; |
| ES256_K | &quot;ES256K&quot; |



