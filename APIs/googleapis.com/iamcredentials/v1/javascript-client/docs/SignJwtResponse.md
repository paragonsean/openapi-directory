# IamServiceAccountCredentialsApi.SignJwtResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyId** | **String** | The ID of the key used to sign the JWT. The key used for signing will remain valid for at least 12 hours after the JWT is signed. To verify the signature, you can retrieve the public key in several formats from the following endpoints: - RSA public key wrapped in an X.509 v3 certificate: &#x60;https://www.googleapis.com/service_accounts/v1/metadata/x509/{ACCOUNT_EMAIL}&#x60; - Raw key in JSON format: &#x60;https://www.googleapis.com/service_accounts/v1/metadata/raw/{ACCOUNT_EMAIL}&#x60; - JSON Web Key (JWK): &#x60;https://www.googleapis.com/service_accounts/v1/metadata/jwk/{ACCOUNT_EMAIL}&#x60; | [optional] 
**signedJwt** | **String** | The signed JWT. Contains the automatically generated header; the client-supplied payload; and the signature, which is generated using the key referenced by the &#x60;kid&#x60; field in the header. After the key pair referenced by the &#x60;key_id&#x60; response field expires, Google no longer exposes the public key that can be used to verify the JWT. As a result, the receiver can no longer verify the signature. | [optional] 


