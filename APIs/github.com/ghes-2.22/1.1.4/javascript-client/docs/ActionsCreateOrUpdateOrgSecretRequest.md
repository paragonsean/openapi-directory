# GitHubV3RestApi.ActionsCreateOrUpdateOrgSecretRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryptedValue** | **String** | Value for your secret, encrypted with [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using the public key retrieved from the [Get an organization public key](https://docs.github.com/enterprise-server@2.22/rest/reference/actions#get-an-organization-public-key) endpoint. | [optional] 
**keyId** | **String** | ID of the key you used to encrypt the secret. | [optional] 
**selectedRepositoryIds** | **[String]** | An array of repository ids that can access the organization secret. You can only provide a list of repository ids when the &#x60;visibility&#x60; is set to &#x60;selected&#x60;. You can manage the list of selected repositories using the [List selected repositories for an organization secret](https://docs.github.com/enterprise-server@2.22/rest/reference/actions#list-selected-repositories-for-an-organization-secret), [Set selected repositories for an organization secret](https://docs.github.com/enterprise-server@2.22/rest/reference/actions#set-selected-repositories-for-an-organization-secret), and [Remove selected repository from an organization secret](https://docs.github.com/enterprise-server@2.22/rest/reference/actions#remove-selected-repository-from-an-organization-secret) endpoints. | [optional] 
**visibility** | **String** | Configures the access that repositories have to the organization secret. Can be one of:   \\- &#x60;all&#x60; - All repositories in an organization can access the secret.   \\- &#x60;private&#x60; - Private repositories in an organization can access the secret.   \\- &#x60;selected&#x60; - Only specific repositories can access the secret. | 



## Enum: VisibilityEnum


* `all` (value: `"all"`)

* `private` (value: `"private"`)

* `selected` (value: `"selected"`)




