# ExaVault.SSHKeysApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addSSHKey**](SSHKeysApi.md#addSSHKey) | **POST** /ssh-keys | Create a new SSH Key
[**deleteSSHKey**](SSHKeysApi.md#deleteSSHKey) | **DELETE** /ssh-keys/{id} | Delete an SSH Key
[**getSSHKey**](SSHKeysApi.md#getSSHKey) | **GET** /ssh-keys/{id} | Get metadata for an SSH Key
[**getSSHKeysList**](SSHKeysApi.md#getSSHKeysList) | **GET** /ssh-keys | Get metadata for a list of SSH Keys



## addSSHKey

> SSHKeyResponse addSSHKey(evApiKey, evAccessToken, opts)

Create a new SSH Key

Create a new SSH Key for a user. Provide the Public Key as formatted from the ssh-keygen command (openssh format or RFC-4716 format).  If you&#39;d prefer to let us generate your key automatically, you can log in to your account via the web portal and set up new keys via the SSH Keys page. 

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.SSHKeysApi();
let evApiKey = "evApiKey_example"; // String | API key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'addSSHKeyRequestBody': new ExaVault.AddSSHKeyRequestBody() // AddSSHKeyRequestBody | 
};
apiInstance.addSSHKey(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **addSSHKeyRequestBody** | [**AddSSHKeyRequestBody**](AddSSHKeyRequestBody.md)|  | [optional] 

### Return type

[**SSHKeyResponse**](SSHKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSSHKey

> deleteSSHKey(id, evApiKey, evAccessToken)

Delete an SSH Key

Delete the specified SSH key. This will not delete or deactivate the user tied to the key.

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.SSHKeysApi();
let id = "id_example"; // String | 
let evApiKey = "evApiKey_example"; // String | API key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
apiInstance.deleteSSHKey(id, evApiKey, evAccessToken, (error, data, response) => {
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
 **id** | **String**|  | 
 **evApiKey** | **String**| API key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSSHKey

> SSHKeyResponse getSSHKey(id, evApiKey, evAccessToken)

Get metadata for an SSH Key

Return the information for a single SSH Key

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.SSHKeysApi();
let id = "id_example"; // String | 
let evApiKey = "evApiKey_example"; // String | API key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
apiInstance.getSSHKey(id, evApiKey, evAccessToken, (error, data, response) => {
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
 **id** | **String**|  | 
 **evApiKey** | **String**| API key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 

### Return type

[**SSHKeyResponse**](SSHKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSSHKeysList

> SSHKeyCollectionResponse getSSHKeysList(evApiKey, evAccessToken, opts)

Get metadata for a list of SSH Keys

Returns a list of SSH Keys within the account. Can be filtered for a single user.

### Example

```javascript
import ExaVault from 'exa_vault';

let apiInstance = new ExaVault.SSHKeysApi();
let evApiKey = "evApiKey_example"; // String | API key required to make the API call.
let evAccessToken = "5dc97cc607985eb8da033220e7447647e7915fbf73808"; // String | Access token required to make the API call.
let opts = {
  'userId': "userId_example", // String |  Only return results for the given user ID. This is not the username, but the numeric ID of the user.
  'limit': 56, // Number |  Limits the results by the given number. Cannot be set higher than 100.
  'offset': 56 // Number |  Determines which item to start on for pagination. Use zero (0) to start at the beginning of the list.
};
apiInstance.getSSHKeysList(evApiKey, evAccessToken, opts, (error, data, response) => {
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
 **evApiKey** | **String**| API key required to make the API call. | 
 **evAccessToken** | **String**| Access token required to make the API call. | 
 **userId** | **String**|  Only return results for the given user ID. This is not the username, but the numeric ID of the user. | [optional] 
 **limit** | **Number**|  Limits the results by the given number. Cannot be set higher than 100. | [optional] 
 **offset** | **Number**|  Determines which item to start on for pagination. Use zero (0) to start at the beginning of the list. | [optional] 

### Return type

[**SSHKeyCollectionResponse**](SSHKeyCollectionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

