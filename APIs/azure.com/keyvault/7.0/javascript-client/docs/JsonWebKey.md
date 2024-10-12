# KeyVaultClient.JsonWebKey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crv** | **String** | Elliptic curve name. For valid values, see JsonWebKeyCurveName. | [optional] 
**d** | **String** | RSA private exponent, or the D component of an EC private key. | [optional] 
**dp** | **String** | RSA private key parameter. | [optional] 
**dq** | **String** | RSA private key parameter. | [optional] 
**e** | **String** | RSA public exponent. | [optional] 
**k** | **String** | Symmetric key. | [optional] 
**keyHsm** | **String** | HSM Token, used with &#39;Bring Your Own Key&#39;. | [optional] 
**keyOps** | **[String]** |  | [optional] 
**kid** | **String** | Key identifier. | [optional] 
**kty** | **String** | JsonWebKey Key Type (kty), as defined in https://tools.ietf.org/html/draft-ietf-jose-json-web-algorithms-40. | [optional] 
**n** | **String** | RSA modulus. | [optional] 
**p** | **String** | RSA secret prime. | [optional] 
**q** | **String** | RSA secret prime, with p &lt; q. | [optional] 
**qi** | **String** | RSA private key parameter. | [optional] 
**x** | **String** | X component of an EC public key. | [optional] 
**y** | **String** | Y component of an EC public key. | [optional] 



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




