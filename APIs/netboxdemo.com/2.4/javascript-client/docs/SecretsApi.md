# NetBoxApi.SecretsApi

All URIs are relative to *http://netboxdemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secretsChoicesList**](SecretsApi.md#secretsChoicesList) | **GET** /secrets/_choices/ | 
[**secretsChoicesRead**](SecretsApi.md#secretsChoicesRead) | **GET** /secrets/_choices/{id}/ | 
[**secretsGenerateRsaKeyPairList**](SecretsApi.md#secretsGenerateRsaKeyPairList) | **GET** /secrets/generate-rsa-key-pair/ | 
[**secretsGetSessionKeyCreate**](SecretsApi.md#secretsGetSessionKeyCreate) | **POST** /secrets/get-session-key/ | 
[**secretsSecretRolesCreate**](SecretsApi.md#secretsSecretRolesCreate) | **POST** /secrets/secret-roles/ | 
[**secretsSecretRolesDelete**](SecretsApi.md#secretsSecretRolesDelete) | **DELETE** /secrets/secret-roles/{id}/ | 
[**secretsSecretRolesList**](SecretsApi.md#secretsSecretRolesList) | **GET** /secrets/secret-roles/ | 
[**secretsSecretRolesPartialUpdate**](SecretsApi.md#secretsSecretRolesPartialUpdate) | **PATCH** /secrets/secret-roles/{id}/ | 
[**secretsSecretRolesRead**](SecretsApi.md#secretsSecretRolesRead) | **GET** /secrets/secret-roles/{id}/ | 
[**secretsSecretRolesUpdate**](SecretsApi.md#secretsSecretRolesUpdate) | **PUT** /secrets/secret-roles/{id}/ | 
[**secretsSecretsCreate**](SecretsApi.md#secretsSecretsCreate) | **POST** /secrets/secrets/ | 
[**secretsSecretsDelete**](SecretsApi.md#secretsSecretsDelete) | **DELETE** /secrets/secrets/{id}/ | 
[**secretsSecretsList**](SecretsApi.md#secretsSecretsList) | **GET** /secrets/secrets/ | 
[**secretsSecretsPartialUpdate**](SecretsApi.md#secretsSecretsPartialUpdate) | **PATCH** /secrets/secrets/{id}/ | 
[**secretsSecretsRead**](SecretsApi.md#secretsSecretsRead) | **GET** /secrets/secrets/{id}/ | 
[**secretsSecretsUpdate**](SecretsApi.md#secretsSecretsUpdate) | **PUT** /secrets/secrets/{id}/ | 



## secretsChoicesList

> secretsChoicesList()





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.SecretsApi();
apiInstance.secretsChoicesList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## secretsChoicesRead

> secretsChoicesRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.SecretsApi();
let id = "id_example"; // String | 
apiInstance.secretsChoicesRead(id, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## secretsGenerateRsaKeyPairList

> secretsGenerateRsaKeyPairList()



This endpoint can be used to generate a new RSA key pair. The keys are returned in PEM format.      {         \&quot;public_key\&quot;: \&quot;&lt;public key&gt;\&quot;,         \&quot;private_key\&quot;: \&quot;&lt;private key&gt;\&quot;     }

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.SecretsApi();
apiInstance.secretsGenerateRsaKeyPairList((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## secretsGetSessionKeyCreate

> secretsGetSessionKeyCreate()



Retrieve a temporary session key to use for encrypting and decrypting secrets via the API. The user&#39;s private RSA key is POSTed with the name &#x60;private_key&#x60;. An example:      curl -v -X POST -H \&quot;Authorization: Token &lt;token&gt;\&quot; -H \&quot;Accept: application/json; indent&#x3D;4\&quot; \\     --data-urlencode \&quot;private_key@&lt;filename&gt;\&quot; https://netbox/api/secrets/get-session-key/  This request will yield a base64-encoded session key to be included in an &#x60;X-Session-Key&#x60; header in future requests:      {         \&quot;session_key\&quot;: \&quot;+8t4SI6XikgVmB5+/urhozx9O5qCQANyOk1MNe6taRf&#x3D;\&quot;     }  This endpoint accepts one optional parameter: &#x60;preserve_key&#x60;. If True and a session key exists, the existing session key will be returned instead of a new one.

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.SecretsApi();
apiInstance.secretsGetSessionKeyCreate((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## secretsSecretRolesCreate

> SecretRole secretsSecretRolesCreate(secretRole)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.SecretsApi();
let secretRole = new NetBoxApi.SecretRole(); // SecretRole | 
apiInstance.secretsSecretRolesCreate(secretRole, (error, data, response) => {
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
 **secretRole** | [**SecretRole**](SecretRole.md)|  | 

### Return type

[**SecretRole**](SecretRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## secretsSecretRolesDelete

> secretsSecretRolesDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.SecretsApi();
let id = 56; // Number | A unique integer value identifying this secret role.
apiInstance.secretsSecretRolesDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this secret role. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## secretsSecretRolesList

> SecretsSecretRolesList200Response secretsSecretRolesList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.SecretsApi();
let opts = {
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.secretsSecretRolesList(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**SecretsSecretRolesList200Response**](SecretsSecretRolesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretsSecretRolesPartialUpdate

> SecretRole secretsSecretRolesPartialUpdate(id, secretRole)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.SecretsApi();
let id = 56; // Number | A unique integer value identifying this secret role.
let secretRole = new NetBoxApi.SecretRole(); // SecretRole | 
apiInstance.secretsSecretRolesPartialUpdate(id, secretRole, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this secret role. | 
 **secretRole** | [**SecretRole**](SecretRole.md)|  | 

### Return type

[**SecretRole**](SecretRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## secretsSecretRolesRead

> SecretRole secretsSecretRolesRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.SecretsApi();
let id = 56; // Number | A unique integer value identifying this secret role.
apiInstance.secretsSecretRolesRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this secret role. | 

### Return type

[**SecretRole**](SecretRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretsSecretRolesUpdate

> SecretRole secretsSecretRolesUpdate(id, secretRole)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.SecretsApi();
let id = 56; // Number | A unique integer value identifying this secret role.
let secretRole = new NetBoxApi.SecretRole(); // SecretRole | 
apiInstance.secretsSecretRolesUpdate(id, secretRole, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this secret role. | 
 **secretRole** | [**SecretRole**](SecretRole.md)|  | 

### Return type

[**SecretRole**](SecretRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## secretsSecretsCreate

> Secret secretsSecretsCreate(writableSecret)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.SecretsApi();
let writableSecret = new NetBoxApi.WritableSecret(); // WritableSecret | 
apiInstance.secretsSecretsCreate(writableSecret, (error, data, response) => {
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
 **writableSecret** | [**WritableSecret**](WritableSecret.md)|  | 

### Return type

[**Secret**](Secret.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## secretsSecretsDelete

> secretsSecretsDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.SecretsApi();
let id = 56; // Number | A unique integer value identifying this secret.
apiInstance.secretsSecretsDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this secret. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## secretsSecretsList

> SecretsSecretsList200Response secretsSecretsList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.SecretsApi();
let opts = {
  'name': "name_example", // String | 
  'idIn': "idIn_example", // String | Multiple values may be separated by commas.
  'q': "q_example", // String | 
  'roleId': "roleId_example", // String | 
  'role': "role_example", // String | 
  'deviceId': "deviceId_example", // String | 
  'device': "device_example", // String | 
  'tag': "tag_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.secretsSecretsList(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 
 **idIn** | **String**| Multiple values may be separated by commas. | [optional] 
 **q** | **String**|  | [optional] 
 **roleId** | **String**|  | [optional] 
 **role** | **String**|  | [optional] 
 **deviceId** | **String**|  | [optional] 
 **device** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**SecretsSecretsList200Response**](SecretsSecretsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretsSecretsPartialUpdate

> Secret secretsSecretsPartialUpdate(id, writableSecret)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.SecretsApi();
let id = 56; // Number | A unique integer value identifying this secret.
let writableSecret = new NetBoxApi.WritableSecret(); // WritableSecret | 
apiInstance.secretsSecretsPartialUpdate(id, writableSecret, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this secret. | 
 **writableSecret** | [**WritableSecret**](WritableSecret.md)|  | 

### Return type

[**Secret**](Secret.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## secretsSecretsRead

> Secret secretsSecretsRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.SecretsApi();
let id = 56; // Number | A unique integer value identifying this secret.
apiInstance.secretsSecretsRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this secret. | 

### Return type

[**Secret**](Secret.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretsSecretsUpdate

> Secret secretsSecretsUpdate(id, writableSecret)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.SecretsApi();
let id = 56; // Number | A unique integer value identifying this secret.
let writableSecret = new NetBoxApi.WritableSecret(); // WritableSecret | 
apiInstance.secretsSecretsUpdate(id, writableSecret, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this secret. | 
 **writableSecret** | [**WritableSecret**](WritableSecret.md)|  | 

### Return type

[**Secret**](Secret.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

