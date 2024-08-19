# GitHubV3RestApi.DependabotApi

All URIs are relative to *https://github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dependabotAddSelectedRepoToOrgSecret**](DependabotApi.md#dependabotAddSelectedRepoToOrgSecret) | **PUT** /orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id} | Add selected repository to an organization secret
[**dependabotCreateOrUpdateOrgSecret**](DependabotApi.md#dependabotCreateOrUpdateOrgSecret) | **PUT** /orgs/{org}/dependabot/secrets/{secret_name} | Create or update an organization secret
[**dependabotCreateOrUpdateRepoSecret**](DependabotApi.md#dependabotCreateOrUpdateRepoSecret) | **PUT** /repos/{owner}/{repo}/dependabot/secrets/{secret_name} | Create or update a repository secret
[**dependabotDeleteOrgSecret**](DependabotApi.md#dependabotDeleteOrgSecret) | **DELETE** /orgs/{org}/dependabot/secrets/{secret_name} | Delete an organization secret
[**dependabotDeleteRepoSecret**](DependabotApi.md#dependabotDeleteRepoSecret) | **DELETE** /repos/{owner}/{repo}/dependabot/secrets/{secret_name} | Delete a repository secret
[**dependabotGetOrgPublicKey**](DependabotApi.md#dependabotGetOrgPublicKey) | **GET** /orgs/{org}/dependabot/secrets/public-key | Get an organization public key
[**dependabotGetOrgSecret**](DependabotApi.md#dependabotGetOrgSecret) | **GET** /orgs/{org}/dependabot/secrets/{secret_name} | Get an organization secret
[**dependabotGetRepoPublicKey**](DependabotApi.md#dependabotGetRepoPublicKey) | **GET** /repos/{owner}/{repo}/dependabot/secrets/public-key | Get a repository public key
[**dependabotGetRepoSecret**](DependabotApi.md#dependabotGetRepoSecret) | **GET** /repos/{owner}/{repo}/dependabot/secrets/{secret_name} | Get a repository secret
[**dependabotListOrgSecrets**](DependabotApi.md#dependabotListOrgSecrets) | **GET** /orgs/{org}/dependabot/secrets | List organization secrets
[**dependabotListRepoSecrets**](DependabotApi.md#dependabotListRepoSecrets) | **GET** /repos/{owner}/{repo}/dependabot/secrets | List repository secrets
[**dependabotListSelectedReposForOrgSecret**](DependabotApi.md#dependabotListSelectedReposForOrgSecret) | **GET** /orgs/{org}/dependabot/secrets/{secret_name}/repositories | List selected repositories for an organization secret
[**dependabotRemoveSelectedRepoFromOrgSecret**](DependabotApi.md#dependabotRemoveSelectedRepoFromOrgSecret) | **DELETE** /orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id} | Remove selected repository from an organization secret
[**dependabotSetSelectedReposForOrgSecret**](DependabotApi.md#dependabotSetSelectedReposForOrgSecret) | **PUT** /orgs/{org}/dependabot/secrets/{secret_name}/repositories | Set selected repositories for an organization secret



## dependabotAddSelectedRepoToOrgSecret

> dependabotAddSelectedRepoToOrgSecret(org, secretName, repositoryId)

Add selected repository to an organization secret

Adds a repository to an organization secret when the &#x60;visibility&#x60; for repository access is set to &#x60;selected&#x60;. The visibility is set when you [Create or update an organization secret](https://docs.github.com/enterprise-server@3.4/rest/reference/dependabot#create-or-update-an-organization-secret). You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;dependabot_secrets&#x60; organization permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.DependabotApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let secretName = "secretName_example"; // String | The name of the secret.
let repositoryId = 56; // Number | 
apiInstance.dependabotAddSelectedRepoToOrgSecret(org, secretName, repositoryId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **secretName** | **String**| The name of the secret. | 
 **repositoryId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## dependabotCreateOrUpdateOrgSecret

> Object dependabotCreateOrUpdateOrgSecret(org, secretName, dependabotCreateOrUpdateOrgSecretRequest)

Create or update an organization secret

Creates or updates an organization secret with an encrypted value. Encrypt your secret using [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;dependabot_secrets&#x60; organization permission to use this endpoint.  #### Example encrypting a secret using Node.js  Encrypt your secret using the [libsodium-wrappers](https://www.npmjs.com/package/libsodium-wrappers) library.  &#x60;&#x60;&#x60; const sodium &#x3D; require(&#39;libsodium-wrappers&#39;) const secret &#x3D; &#39;plain-text-secret&#39; // replace with the secret you want to encrypt const key &#x3D; &#39;base64-encoded-public-key&#39; // replace with the Base64 encoded public key  //Check if libsodium is ready and then proceed. sodium.ready.then(() &#x3D;&gt; {   // Convert Secret &amp; Base64 key to Uint8Array.   let binkey &#x3D; sodium.from_base64(key, sodium.base64_variants.ORIGINAL)   let binsec &#x3D; sodium.from_string(secret)    //Encrypt the secret using LibSodium   let encBytes &#x3D; sodium.crypto_box_seal(binsec, binkey)    // Convert encrypted Uint8Array to Base64   let output &#x3D; sodium.to_base64(encBytes, sodium.base64_variants.ORIGINAL)    console.log(output) }); &#x60;&#x60;&#x60;  #### Example encrypting a secret using Python  Encrypt your secret using [pynacl](https://pynacl.readthedocs.io/en/latest/public/#nacl-public-sealedbox) with Python 3.  &#x60;&#x60;&#x60; from base64 import b64encode from nacl import encoding, public  def encrypt(public_key: str, secret_value: str) -&gt; str:   \&quot;\&quot;\&quot;Encrypt a Unicode string using the public key.\&quot;\&quot;\&quot;   public_key &#x3D; public.PublicKey(public_key.encode(\&quot;utf-8\&quot;), encoding.Base64Encoder())   sealed_box &#x3D; public.SealedBox(public_key)   encrypted &#x3D; sealed_box.encrypt(secret_value.encode(\&quot;utf-8\&quot;))   return b64encode(encrypted).decode(\&quot;utf-8\&quot;) &#x60;&#x60;&#x60;  #### Example encrypting a secret using C#  Encrypt your secret using the [Sodium.Core](https://www.nuget.org/packages/Sodium.Core/) package.  &#x60;&#x60;&#x60; var secretValue &#x3D; System.Text.Encoding.UTF8.GetBytes(\&quot;mySecret\&quot;); var publicKey &#x3D; Convert.FromBase64String(\&quot;2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvvcCU&#x3D;\&quot;);  var sealedPublicKeyBox &#x3D; Sodium.SealedPublicKeyBox.Create(secretValue, publicKey);  Console.WriteLine(Convert.ToBase64String(sealedPublicKeyBox)); &#x60;&#x60;&#x60;  #### Example encrypting a secret using Ruby  Encrypt your secret using the [rbnacl](https://github.com/RubyCrypto/rbnacl) gem.  &#x60;&#x60;&#x60;ruby require \&quot;rbnacl\&quot; require \&quot;base64\&quot;  key &#x3D; Base64.decode64(\&quot;+ZYvJDZMHUfBkJdyq5Zm9SKqeuBQ4sj+6sfjlH4CgG0&#x3D;\&quot;) public_key &#x3D; RbNaCl::PublicKey.new(key)  box &#x3D; RbNaCl::Boxes::Sealed.from_public_key(public_key) encrypted_secret &#x3D; box.encrypt(\&quot;my_secret\&quot;)  # Print the base64 encoded secret puts Base64.strict_encode64(encrypted_secret) &#x60;&#x60;&#x60;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.DependabotApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let secretName = "secretName_example"; // String | The name of the secret.
let dependabotCreateOrUpdateOrgSecretRequest = {"encrypted_value":"c2VjcmV0","key_id":"012345678912345678","selected_repository_ids":["1296269","1296280"],"visibility":"selected"}; // DependabotCreateOrUpdateOrgSecretRequest | 
apiInstance.dependabotCreateOrUpdateOrgSecret(org, secretName, dependabotCreateOrUpdateOrgSecretRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **secretName** | **String**| The name of the secret. | 
 **dependabotCreateOrUpdateOrgSecretRequest** | [**DependabotCreateOrUpdateOrgSecretRequest**](DependabotCreateOrUpdateOrgSecretRequest.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dependabotCreateOrUpdateRepoSecret

> Object dependabotCreateOrUpdateRepoSecret(owner, repo, secretName, dependabotCreateOrUpdateRepoSecretRequest)

Create or update a repository secret

Creates or updates a repository secret with an encrypted value. Encrypt your secret using [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;dependabot_secrets&#x60; repository permission to use this endpoint.  #### Example encrypting a secret using Node.js  Encrypt your secret using the [libsodium-wrappers](https://www.npmjs.com/package/libsodium-wrappers) library.  &#x60;&#x60;&#x60; const sodium &#x3D; require(&#39;libsodium-wrappers&#39;) const secret &#x3D; &#39;plain-text-secret&#39; // replace with the secret you want to encrypt const key &#x3D; &#39;base64-encoded-public-key&#39; // replace with the Base64 encoded public key  //Check if libsodium is ready and then proceed. sodium.ready.then(() &#x3D;&gt; {   // Convert Secret &amp; Base64 key to Uint8Array.   let binkey &#x3D; sodium.from_base64(key, sodium.base64_variants.ORIGINAL)   let binsec &#x3D; sodium.from_string(secret)    //Encrypt the secret using LibSodium   let encBytes &#x3D; sodium.crypto_box_seal(binsec, binkey)    // Convert encrypted Uint8Array to Base64   let output &#x3D; sodium.to_base64(encBytes, sodium.base64_variants.ORIGINAL)    console.log(output) }); &#x60;&#x60;&#x60;  #### Example encrypting a secret using Python  Encrypt your secret using [pynacl](https://pynacl.readthedocs.io/en/latest/public/#nacl-public-sealedbox) with Python 3.  &#x60;&#x60;&#x60; from base64 import b64encode from nacl import encoding, public  def encrypt(public_key: str, secret_value: str) -&gt; str:   \&quot;\&quot;\&quot;Encrypt a Unicode string using the public key.\&quot;\&quot;\&quot;   public_key &#x3D; public.PublicKey(public_key.encode(\&quot;utf-8\&quot;), encoding.Base64Encoder())   sealed_box &#x3D; public.SealedBox(public_key)   encrypted &#x3D; sealed_box.encrypt(secret_value.encode(\&quot;utf-8\&quot;))   return b64encode(encrypted).decode(\&quot;utf-8\&quot;) &#x60;&#x60;&#x60;  #### Example encrypting a secret using C#  Encrypt your secret using the [Sodium.Core](https://www.nuget.org/packages/Sodium.Core/) package.  &#x60;&#x60;&#x60; var secretValue &#x3D; System.Text.Encoding.UTF8.GetBytes(\&quot;mySecret\&quot;); var publicKey &#x3D; Convert.FromBase64String(\&quot;2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvvcCU&#x3D;\&quot;);  var sealedPublicKeyBox &#x3D; Sodium.SealedPublicKeyBox.Create(secretValue, publicKey);  Console.WriteLine(Convert.ToBase64String(sealedPublicKeyBox)); &#x60;&#x60;&#x60;  #### Example encrypting a secret using Ruby  Encrypt your secret using the [rbnacl](https://github.com/RubyCrypto/rbnacl) gem.  &#x60;&#x60;&#x60;ruby require \&quot;rbnacl\&quot; require \&quot;base64\&quot;  key &#x3D; Base64.decode64(\&quot;+ZYvJDZMHUfBkJdyq5Zm9SKqeuBQ4sj+6sfjlH4CgG0&#x3D;\&quot;) public_key &#x3D; RbNaCl::PublicKey.new(key)  box &#x3D; RbNaCl::Boxes::Sealed.from_public_key(public_key) encrypted_secret &#x3D; box.encrypt(\&quot;my_secret\&quot;)  # Print the base64 encoded secret puts Base64.strict_encode64(encrypted_secret) &#x60;&#x60;&#x60;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.DependabotApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let secretName = "secretName_example"; // String | The name of the secret.
let dependabotCreateOrUpdateRepoSecretRequest = {"encrypted_value":"c2VjcmV0","key_id":"012345678912345678"}; // DependabotCreateOrUpdateRepoSecretRequest | 
apiInstance.dependabotCreateOrUpdateRepoSecret(owner, repo, secretName, dependabotCreateOrUpdateRepoSecretRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **secretName** | **String**| The name of the secret. | 
 **dependabotCreateOrUpdateRepoSecretRequest** | [**DependabotCreateOrUpdateRepoSecretRequest**](DependabotCreateOrUpdateRepoSecretRequest.md)|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dependabotDeleteOrgSecret

> dependabotDeleteOrgSecret(org, secretName)

Delete an organization secret

Deletes a secret in an organization using the secret name. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;dependabot_secrets&#x60; organization permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.DependabotApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let secretName = "secretName_example"; // String | The name of the secret.
apiInstance.dependabotDeleteOrgSecret(org, secretName, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **secretName** | **String**| The name of the secret. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## dependabotDeleteRepoSecret

> dependabotDeleteRepoSecret(owner, repo, secretName)

Delete a repository secret

Deletes a secret in a repository using the secret name. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;dependabot_secrets&#x60; repository permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.DependabotApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let secretName = "secretName_example"; // String | The name of the secret.
apiInstance.dependabotDeleteRepoSecret(owner, repo, secretName, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **secretName** | **String**| The name of the secret. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## dependabotGetOrgPublicKey

> DependabotPublicKey dependabotGetOrgPublicKey(org)

Get an organization public key

Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;dependabot_secrets&#x60; organization permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.DependabotApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
apiInstance.dependabotGetOrgPublicKey(org, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**| The organization name. The name is not case sensitive. | 

### Return type

[**DependabotPublicKey**](DependabotPublicKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dependabotGetOrgSecret

> OrganizationDependabotSecret dependabotGetOrgSecret(org, secretName)

Get an organization secret

Gets a single organization secret without revealing its encrypted value. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;dependabot_secrets&#x60; organization permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.DependabotApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let secretName = "secretName_example"; // String | The name of the secret.
apiInstance.dependabotGetOrgSecret(org, secretName, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **secretName** | **String**| The name of the secret. | 

### Return type

[**OrganizationDependabotSecret**](OrganizationDependabotSecret.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dependabotGetRepoPublicKey

> DependabotPublicKey dependabotGetRepoPublicKey(owner, repo)

Get a repository public key

Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;dependabot_secrets&#x60; repository permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.DependabotApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
apiInstance.dependabotGetRepoPublicKey(owner, repo, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 

### Return type

[**DependabotPublicKey**](DependabotPublicKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dependabotGetRepoSecret

> DependabotSecret dependabotGetRepoSecret(owner, repo, secretName)

Get a repository secret

Gets a single repository secret without revealing its encrypted value. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;dependabot_secrets&#x60; repository permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.DependabotApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let secretName = "secretName_example"; // String | The name of the secret.
apiInstance.dependabotGetRepoSecret(owner, repo, secretName, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **secretName** | **String**| The name of the secret. | 

### Return type

[**DependabotSecret**](DependabotSecret.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dependabotListOrgSecrets

> DependabotListOrgSecrets200Response dependabotListOrgSecrets(org, opts)

List organization secrets

Lists all secrets available in an organization without revealing their encrypted values. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;dependabot_secrets&#x60; organization permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.DependabotApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.dependabotListOrgSecrets(org, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**DependabotListOrgSecrets200Response**](DependabotListOrgSecrets200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dependabotListRepoSecrets

> DependabotListRepoSecrets200Response dependabotListRepoSecrets(owner, repo, opts)

List repository secrets

Lists all secrets available in a repository without revealing their encrypted values. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;dependabot_secrets&#x60; repository permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.DependabotApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.dependabotListRepoSecrets(owner, repo, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**DependabotListRepoSecrets200Response**](DependabotListRepoSecrets200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dependabotListSelectedReposForOrgSecret

> ActionsListSelectedReposForOrgSecret200Response dependabotListSelectedReposForOrgSecret(org, secretName, opts)

List selected repositories for an organization secret

Lists all repositories that have been selected when the &#x60;visibility&#x60; for repository access to a secret is set to &#x60;selected&#x60;. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;dependabot_secrets&#x60; organization permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.DependabotApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let secretName = "secretName_example"; // String | The name of the secret.
let opts = {
  'page': 1, // Number | Page number of the results to fetch.
  'perPage': 30 // Number | The number of results per page (max 100).
};
apiInstance.dependabotListSelectedReposForOrgSecret(org, secretName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **secretName** | **String**| The name of the secret. | 
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]

### Return type

[**ActionsListSelectedReposForOrgSecret200Response**](ActionsListSelectedReposForOrgSecret200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dependabotRemoveSelectedRepoFromOrgSecret

> dependabotRemoveSelectedRepoFromOrgSecret(org, secretName, repositoryId)

Remove selected repository from an organization secret

Removes a repository from an organization secret when the &#x60;visibility&#x60; for repository access is set to &#x60;selected&#x60;. The visibility is set when you [Create or update an organization secret](https://docs.github.com/enterprise-server@3.4/rest/reference/dependabot#create-or-update-an-organization-secret). You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;dependabot_secrets&#x60; organization permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.DependabotApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let secretName = "secretName_example"; // String | The name of the secret.
let repositoryId = 56; // Number | 
apiInstance.dependabotRemoveSelectedRepoFromOrgSecret(org, secretName, repositoryId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **secretName** | **String**| The name of the secret. | 
 **repositoryId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## dependabotSetSelectedReposForOrgSecret

> dependabotSetSelectedReposForOrgSecret(org, secretName, dependabotSetSelectedReposForOrgSecretRequest)

Set selected repositories for an organization secret

Replaces all repositories for an organization secret when the &#x60;visibility&#x60; for repository access is set to &#x60;selected&#x60;. The visibility is set when you [Create or update an organization secret](https://docs.github.com/enterprise-server@3.4/rest/reference/dependabot#create-or-update-an-organization-secret). You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;dependabot_secrets&#x60; organization permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.DependabotApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let secretName = "secretName_example"; // String | The name of the secret.
let dependabotSetSelectedReposForOrgSecretRequest = {"selected_repository_ids":[64780797]}; // DependabotSetSelectedReposForOrgSecretRequest | 
apiInstance.dependabotSetSelectedReposForOrgSecret(org, secretName, dependabotSetSelectedReposForOrgSecretRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **secretName** | **String**| The name of the secret. | 
 **dependabotSetSelectedReposForOrgSecretRequest** | [**DependabotSetSelectedReposForOrgSecretRequest**](DependabotSetSelectedReposForOrgSecretRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

