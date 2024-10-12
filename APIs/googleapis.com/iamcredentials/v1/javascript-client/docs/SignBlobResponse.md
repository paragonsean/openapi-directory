# IamServiceAccountCredentialsApi.SignBlobResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyId** | **String** | The ID of the key used to sign the blob. The key used for signing will remain valid for at least 12 hours after the blob is signed. To verify the signature, you can retrieve the public key in several formats from the following endpoints: - RSA public key wrapped in an X.509 v3 certificate: &#x60;https://www.googleapis.com/service_accounts/v1/metadata/x509/{ACCOUNT_EMAIL}&#x60; - Raw key in JSON format: &#x60;https://www.googleapis.com/service_accounts/v1/metadata/raw/{ACCOUNT_EMAIL}&#x60; - JSON Web Key (JWK): &#x60;https://www.googleapis.com/service_accounts/v1/metadata/jwk/{ACCOUNT_EMAIL}&#x60; | [optional] 
**signedBlob** | **Blob** | The signature for the blob. Does not include the original blob. After the key pair referenced by the &#x60;key_id&#x60; response field expires, Google no longer exposes the public key that can be used to verify the blob. As a result, the receiver can no longer verify the signature. | [optional] 


