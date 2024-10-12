# BitbucketApi.SshApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersSelectedUserSshKeysGet**](SshApi.md#usersSelectedUserSshKeysGet) | **GET** /users/{selected_user}/ssh-keys | List SSH keys
[**usersSelectedUserSshKeysKeyIdDelete**](SshApi.md#usersSelectedUserSshKeysKeyIdDelete) | **DELETE** /users/{selected_user}/ssh-keys/{key_id} | Delete a SSH key
[**usersSelectedUserSshKeysKeyIdGet**](SshApi.md#usersSelectedUserSshKeysKeyIdGet) | **GET** /users/{selected_user}/ssh-keys/{key_id} | Get a SSH key
[**usersSelectedUserSshKeysKeyIdPut**](SshApi.md#usersSelectedUserSshKeysKeyIdPut) | **PUT** /users/{selected_user}/ssh-keys/{key_id} | Update a SSH key
[**usersSelectedUserSshKeysPost**](SshApi.md#usersSelectedUserSshKeysPost) | **POST** /users/{selected_user}/ssh-keys | Add a new SSH key



## usersSelectedUserSshKeysGet

> PaginatedSshUserKeys usersSelectedUserSshKeysGet(selectedUser)

List SSH keys

Returns a paginated list of the user&#39;s SSH public keys.  Example:  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys {     \&quot;page\&quot;: 1,     \&quot;pagelen\&quot;: 10,     \&quot;size\&quot;: 1,     \&quot;values\&quot;: [         {             \&quot;comment\&quot;: \&quot;user@myhost\&quot;,             \&quot;created_on\&quot;: \&quot;2018-03-14T13:17:05.196003+00:00\&quot;,             \&quot;key\&quot;: \&quot;ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKqP3Cr632C2dNhhgKVcon4ldUSAeKiku2yP9O9/bDtY\&quot;,             \&quot;label\&quot;: \&quot;\&quot;,             \&quot;last_used\&quot;: \&quot;2018-03-20T13:18:05.196003+00:00\&quot;,             \&quot;links\&quot;: {                 \&quot;self\&quot;: {                     \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys/b15b6026-9c02-4626-b4ad-b905f99f763a\&quot;                 }             },             \&quot;owner\&quot;: {                 \&quot;display_name\&quot;: \&quot;Mark Adams\&quot;,                 \&quot;links\&quot;: {                     \&quot;avatar\&quot;: {                         \&quot;href\&quot;: \&quot;https://bitbucket.org/account/markadams-atl/avatar/32/\&quot;                     },                     \&quot;html\&quot;: {                         \&quot;href\&quot;: \&quot;https://bitbucket.org/markadams-atl/\&quot;                     },                     \&quot;self\&quot;: {                         \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}\&quot;                     }                 },                 \&quot;type\&quot;: \&quot;user\&quot;,                 \&quot;username\&quot;: \&quot;markadams-atl\&quot;,                 \&quot;nickname\&quot;: \&quot;markadams-atl\&quot;,                 \&quot;uuid\&quot;: \&quot;{d7dd0e2d-3994-4a50-a9ee-d260b6cefdab}\&quot;             },             \&quot;type\&quot;: \&quot;ssh_key\&quot;,             \&quot;uuid\&quot;: \&quot;{b15b6026-9c02-4626-b4ad-b905f99f763a}\&quot;         }     ] } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.SshApi();
let selectedUser = "selectedUser_example"; // String | This can either be the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`, OR an Atlassian Account ID. 
apiInstance.usersSelectedUserSshKeysGet(selectedUser, (error, data, response) => {
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
 **selectedUser** | **String**| This can either be the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;, OR an Atlassian Account ID.  | 

### Return type

[**PaginatedSshUserKeys**](PaginatedSshUserKeys.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersSelectedUserSshKeysKeyIdDelete

> usersSelectedUserSshKeysKeyIdDelete(keyId, selectedUser)

Delete a SSH key

Deletes a specific SSH public key from a user&#39;s account  Example: &#x60;&#x60;&#x60; $ curl -X DELETE https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys/{b15b6026-9c02-4626-b4ad-b905f99f763a} &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.SshApi();
let keyId = "keyId_example"; // String | The SSH key's UUID value.
let selectedUser = "selectedUser_example"; // String | This can either be the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`, OR an Atlassian Account ID. 
apiInstance.usersSelectedUserSshKeysKeyIdDelete(keyId, selectedUser, (error, data, response) => {
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
 **keyId** | **String**| The SSH key&#39;s UUID value. | 
 **selectedUser** | **String**| This can either be the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;, OR an Atlassian Account ID.  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersSelectedUserSshKeysKeyIdGet

> SshAccountKey usersSelectedUserSshKeysKeyIdGet(keyId, selectedUser)

Get a SSH key

Returns a specific SSH public key belonging to a user.  Example: &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys/{fbe4bbab-f6f7-4dde-956b-5c58323c54b3}  {     \&quot;comment\&quot;: \&quot;user@myhost\&quot;,     \&quot;created_on\&quot;: \&quot;2018-03-14T13:17:05.196003+00:00\&quot;,     \&quot;key\&quot;: \&quot;ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKqP3Cr632C2dNhhgKVcon4ldUSAeKiku2yP9O9/bDtY\&quot;,     \&quot;label\&quot;: \&quot;\&quot;,     \&quot;last_used\&quot;: \&quot;2018-03-20T13:18:05.196003+00:00\&quot;,     \&quot;links\&quot;: {         \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys/b15b6026-9c02-4626-b4ad-b905f99f763a\&quot;         }     },     \&quot;owner\&quot;: {         \&quot;display_name\&quot;: \&quot;Mark Adams\&quot;,         \&quot;links\&quot;: {             \&quot;avatar\&quot;: {                 \&quot;href\&quot;: \&quot;https://bitbucket.org/account/markadams-atl/avatar/32/\&quot;             },             \&quot;html\&quot;: {                 \&quot;href\&quot;: \&quot;https://bitbucket.org/markadams-atl/\&quot;             },             \&quot;self\&quot;: {                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}\&quot;             }         },         \&quot;type\&quot;: \&quot;user\&quot;,         \&quot;username\&quot;: \&quot;markadams-atl\&quot;,         \&quot;nickname\&quot;: \&quot;markadams-atl\&quot;,         \&quot;uuid\&quot;: \&quot;{d7dd0e2d-3994-4a50-a9ee-d260b6cefdab}\&quot;     },     \&quot;type\&quot;: \&quot;ssh_key\&quot;,     \&quot;uuid\&quot;: \&quot;{b15b6026-9c02-4626-b4ad-b905f99f763a}\&quot; } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.SshApi();
let keyId = "keyId_example"; // String | The SSH key's UUID value.
let selectedUser = "selectedUser_example"; // String | This can either be the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`, OR an Atlassian Account ID. 
apiInstance.usersSelectedUserSshKeysKeyIdGet(keyId, selectedUser, (error, data, response) => {
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
 **keyId** | **String**| The SSH key&#39;s UUID value. | 
 **selectedUser** | **String**| This can either be the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;, OR an Atlassian Account ID.  | 

### Return type

[**SshAccountKey**](SshAccountKey.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersSelectedUserSshKeysKeyIdPut

> SshAccountKey usersSelectedUserSshKeysKeyIdPut(keyId, selectedUser, opts)

Update a SSH key

Updates a specific SSH public key on a user&#39;s account  Note: Only the &#39;comment&#39; field can be updated using this API. To modify the key or comment values, you must delete and add the key again.  Example: &#x60;&#x60;&#x60; $ curl -X PUT -H \&quot;Content-Type: application/json\&quot; -d &#39;{\&quot;label\&quot;: \&quot;Work key\&quot;}&#39; https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys/{b15b6026-9c02-4626-b4ad-b905f99f763a}  {     \&quot;comment\&quot;: \&quot;\&quot;,     \&quot;created_on\&quot;: \&quot;2018-03-14T13:17:05.196003+00:00\&quot;,     \&quot;key\&quot;: \&quot;ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKqP3Cr632C2dNhhgKVcon4ldUSAeKiku2yP9O9/bDtY\&quot;,     \&quot;label\&quot;: \&quot;Work key\&quot;,     \&quot;last_used\&quot;: \&quot;2018-03-20T13:18:05.196003+00:00\&quot;,     \&quot;links\&quot;: {         \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys/b15b6026-9c02-4626-b4ad-b905f99f763a\&quot;         }     },     \&quot;owner\&quot;: {         \&quot;display_name\&quot;: \&quot;Mark Adams\&quot;,         \&quot;links\&quot;: {             \&quot;avatar\&quot;: {                 \&quot;href\&quot;: \&quot;https://bitbucket.org/account/markadams-atl/avatar/32/\&quot;             },             \&quot;html\&quot;: {                 \&quot;href\&quot;: \&quot;https://bitbucket.org/markadams-atl/\&quot;             },             \&quot;self\&quot;: {                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}\&quot;             }         },         \&quot;type\&quot;: \&quot;user\&quot;,         \&quot;username\&quot;: \&quot;markadams-atl\&quot;,         \&quot;nickname\&quot;: \&quot;markadams-atl\&quot;,         \&quot;uuid\&quot;: \&quot;{d7dd0e2d-3994-4a50-a9ee-d260b6cefdab}\&quot;     },     \&quot;type\&quot;: \&quot;ssh_key\&quot;,     \&quot;uuid\&quot;: \&quot;{b15b6026-9c02-4626-b4ad-b905f99f763a}\&quot; } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.SshApi();
let keyId = "keyId_example"; // String | The SSH key's UUID value.
let selectedUser = "selectedUser_example"; // String | This can either be the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`, OR an Atlassian Account ID. 
let opts = {
  'sshAccountKey': new BitbucketApi.SshAccountKey() // SshAccountKey | The updated SSH key object
};
apiInstance.usersSelectedUserSshKeysKeyIdPut(keyId, selectedUser, opts, (error, data, response) => {
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
 **keyId** | **String**| The SSH key&#39;s UUID value. | 
 **selectedUser** | **String**| This can either be the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;, OR an Atlassian Account ID.  | 
 **sshAccountKey** | [**SshAccountKey**](SshAccountKey.md)| The updated SSH key object | [optional] 

### Return type

[**SshAccountKey**](SshAccountKey.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usersSelectedUserSshKeysPost

> SshAccountKey usersSelectedUserSshKeysPost(selectedUser, opts)

Add a new SSH key

Adds a new SSH public key to the specified user account and returns the resulting key.  Example: &#x60;&#x60;&#x60; $ curl -X POST -H \&quot;Content-Type: application/json\&quot; -d &#39;{\&quot;key\&quot;: \&quot;ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKqP3Cr632C2dNhhgKVcon4ldUSAeKiku2yP9O9/bDtY user@myhost\&quot;}&#39; https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys  {     \&quot;comment\&quot;: \&quot;user@myhost\&quot;,     \&quot;created_on\&quot;: \&quot;2018-03-14T13:17:05.196003+00:00\&quot;,     \&quot;key\&quot;: \&quot;ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKqP3Cr632C2dNhhgKVcon4ldUSAeKiku2yP9O9/bDtY\&quot;,     \&quot;label\&quot;: \&quot;\&quot;,     \&quot;last_used\&quot;: \&quot;2018-03-20T13:18:05.196003+00:00\&quot;,     \&quot;links\&quot;: {         \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys/b15b6026-9c02-4626-b4ad-b905f99f763a\&quot;         }     },     \&quot;owner\&quot;: {         \&quot;display_name\&quot;: \&quot;Mark Adams\&quot;,         \&quot;links\&quot;: {             \&quot;avatar\&quot;: {                 \&quot;href\&quot;: \&quot;https://bitbucket.org/account/markadams-atl/avatar/32/\&quot;             },             \&quot;html\&quot;: {                 \&quot;href\&quot;: \&quot;https://bitbucket.org/markadams-atl/\&quot;             },             \&quot;self\&quot;: {                 \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}\&quot;             }         },         \&quot;type\&quot;: \&quot;user\&quot;,         \&quot;username\&quot;: \&quot;markadams-atl\&quot;,         \&quot;nickname\&quot;: \&quot;markadams-atl\&quot;,         \&quot;uuid\&quot;: \&quot;{d7dd0e2d-3994-4a50-a9ee-d260b6cefdab}\&quot;     },     \&quot;type\&quot;: \&quot;ssh_key\&quot;,     \&quot;uuid\&quot;: \&quot;{b15b6026-9c02-4626-b4ad-b905f99f763a}\&quot; } &#x60;&#x60;&#x60;

### Example

```javascript
import BitbucketApi from 'bitbucket_api';
let defaultClient = BitbucketApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basic
let basic = defaultClient.authentications['basic'];
basic.username = 'YOUR USERNAME';
basic.password = 'YOUR PASSWORD';

let apiInstance = new BitbucketApi.SshApi();
let selectedUser = "selectedUser_example"; // String | This can either be the UUID of the account, surrounded by curly-braces, for example: `{account UUID}`, OR an Atlassian Account ID. 
let opts = {
  'sshAccountKey': new BitbucketApi.SshAccountKey() // SshAccountKey | The new SSH key object. Note that the username property has been deprecated due to [privacy changes](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-gdpr/#removal-of-usernames-from-user-referencing-apis).
};
apiInstance.usersSelectedUserSshKeysPost(selectedUser, opts, (error, data, response) => {
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
 **selectedUser** | **String**| This can either be the UUID of the account, surrounded by curly-braces, for example: &#x60;{account UUID}&#x60;, OR an Atlassian Account ID.  | 
 **sshAccountKey** | [**SshAccountKey**](SshAccountKey.md)| The new SSH key object. Note that the username property has been deprecated due to [privacy changes](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-gdpr/#removal-of-usernames-from-user-referencing-apis). | [optional] 

### Return type

[**SshAccountKey**](SshAccountKey.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

