

# JsonWebKey

As of http://tools.ietf.org/html/draft-ietf-jose-json-web-key-18

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**crv** | [**CrvEnum**](#CrvEnum) | Elliptic curve name. For valid values, see JsonWebKeyCurveName. |  [optional] |
|**d** | **String** | RSA private exponent, or the D component of an EC private key. |  [optional] |
|**dp** | **String** | RSA private key parameter. |  [optional] |
|**dq** | **String** | RSA private key parameter. |  [optional] |
|**e** | **String** | RSA public exponent. |  [optional] |
|**k** | **String** | Symmetric key. |  [optional] |
|**keyHsm** | **String** | HSM Token, used with &#39;Bring Your Own Key&#39;. |  [optional] |
|**keyOps** | **List&lt;String&gt;** |  |  [optional] |
|**kid** | **String** | Key identifier. |  [optional] |
|**kty** | [**KtyEnum**](#KtyEnum) | JsonWebKey Key Type (kty), as defined in https://tools.ietf.org/html/draft-ietf-jose-json-web-algorithms-40. |  [optional] |
|**n** | **String** | RSA modulus. |  [optional] |
|**p** | **String** | RSA secret prime. |  [optional] |
|**q** | **String** | RSA secret prime, with p &lt; q. |  [optional] |
|**qi** | **String** | RSA private key parameter. |  [optional] |
|**x** | **String** | X component of an EC public key. |  [optional] |
|**y** | **String** | Y component of an EC public key. |  [optional] |



## Enum: CrvEnum

| Name | Value |
|---- | -----|
| _256 | &quot;P-256&quot; |
| _384 | &quot;P-384&quot; |
| _521 | &quot;P-521&quot; |
| _256_K | &quot;P-256K&quot; |



## Enum: KtyEnum

| Name | Value |
|---- | -----|
| EC | &quot;EC&quot; |
| EC_HSM | &quot;EC-HSM&quot; |
| RSA | &quot;RSA&quot; |
| RSA_HSM | &quot;RSA-HSM&quot; |
| OCT | &quot;oct&quot; |



