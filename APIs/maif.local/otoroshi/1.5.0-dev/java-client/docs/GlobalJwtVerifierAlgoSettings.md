

# GlobalJwtVerifierAlgoSettings


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**secret** | **String** | The secret value for the HMAC function |  |
|**size** | **Integer** | Size for SHA function. can be 256, 384 or 512 |  |
|**type** | **String** | String with value JWKSAlgoSettings |  |
|**privateKey** | **String** | The private key for the RSA function |  [optional] |
|**publicKey** | **String** | The public key for the RSA function |  |
|**headers** | **Map&lt;String, String&gt;** | The headers for the http call |  [optional] |
|**kty** | **String** | The type of key: RSA or EC |  [optional] |
|**timeout** | **Long** | The timeout of the http call |  [optional] |
|**ttl** | **Long** | The ttl of the keyset |  [optional] |
|**url** | **String** | The url for the http call |  [optional] |



