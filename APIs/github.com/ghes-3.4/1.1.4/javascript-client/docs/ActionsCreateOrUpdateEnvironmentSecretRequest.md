# GitHubV3RestApi.ActionsCreateOrUpdateEnvironmentSecretRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryptedValue** | **String** | Value for your secret, encrypted with [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from the [Get an environment public key](https://docs.github.com/enterprise-server@3.4/rest/reference/actions#get-an-environment-public-key) endpoint. | 
**keyId** | **String** | ID of the key you used to encrypt the secret. | 


