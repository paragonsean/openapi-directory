# OtoroshiAdminApi.GlobalJwtVerifierAlgoSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **String** | The secret value for the HMAC function | 
**size** | **Number** | Size for SHA function. can be 256, 384 or 512 | 
**type** | **String** | String with value JWKSAlgoSettings | 
**privateKey** | **String** | The private key for the RSA function | [optional] 
**publicKey** | **String** | The public key for the RSA function | 
**headers** | **{String: String}** | The headers for the http call | [optional] 
**kty** | **String** | The type of key: RSA or EC | [optional] 
**timeout** | **Number** | The timeout of the http call | [optional] 
**ttl** | **Number** | The ttl of the keyset | [optional] 
**url** | **String** | The url for the http call | [optional] 


