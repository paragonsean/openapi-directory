

# ActionsCreateOrUpdateRepoSecretRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptedValue** | **String** | Value for your secret, encrypted with [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from the [Get a repository public key](https://docs.github.com/enterprise-server@3.2/rest/reference/actions#get-a-repository-public-key) endpoint. |  [optional] |
|**keyId** | **String** | ID of the key you used to encrypt the secret. |  [optional] |



