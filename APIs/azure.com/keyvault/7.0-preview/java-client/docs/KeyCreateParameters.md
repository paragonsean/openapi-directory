

# KeyCreateParameters

The key create parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**KeyAttributes**](KeyAttributes.md) |  |  [optional] |
|**crv** | [**CrvEnum**](#CrvEnum) | Elliptic curve name. For valid values, see JsonWebKeyCurveName. |  [optional] |
|**keyOps** | [**List&lt;KeyOpsEnum&gt;**](#List&lt;KeyOpsEnum&gt;) |  |  [optional] |
|**keySize** | **Integer** | The key size in bits. For example: 2048, 3072, or 4096 for RSA. |  [optional] |
|**kty** | [**KtyEnum**](#KtyEnum) | The type of key to create. For valid values, see JsonWebKeyType. |  |
|**tags** | **Map&lt;String, String&gt;** | Application specific metadata in the form of key-value pairs. |  [optional] |



## Enum: CrvEnum

| Name | Value |
|---- | -----|
| _256 | &quot;P-256&quot; |
| _384 | &quot;P-384&quot; |
| _521 | &quot;P-521&quot; |
| _256_K | &quot;P-256K&quot; |



## Enum: List&lt;KeyOpsEnum&gt;

| Name | Value |
|---- | -----|
| ENCRYPT | &quot;encrypt&quot; |
| DECRYPT | &quot;decrypt&quot; |
| SIGN | &quot;sign&quot; |
| VERIFY | &quot;verify&quot; |
| WRAP_KEY | &quot;wrapKey&quot; |
| UNWRAP_KEY | &quot;unwrapKey&quot; |



## Enum: KtyEnum

| Name | Value |
|---- | -----|
| EC | &quot;EC&quot; |
| EC_HSM | &quot;EC-HSM&quot; |
| RSA | &quot;RSA&quot; |
| RSA_HSM | &quot;RSA-HSM&quot; |
| OCT | &quot;oct&quot; |



