# Conjur.SecretsApi

All URIs are relative to *http://conjur.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSecret**](SecretsApi.md#createSecret) | **POST** /secrets/{account}/{kind}/{identifier} | Creates a secret value within the specified variable.
[**getSecret**](SecretsApi.md#getSecret) | **GET** /secrets/{account}/{kind}/{identifier} | Fetches the value of a secret from the specified Secret.
[**getSecrets**](SecretsApi.md#getSecrets) | **GET** /secrets | Fetch multiple secrets



## createSecret

> createSecret(account, kind, identifier, opts)

Creates a secret value within the specified variable.

Creates a secret value within the specified Secret.   Note: Conjur will allow you to add a secret to any resource, but the best practice is to store and retrieve secret data only using Secret resources. 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.SecretsApi();
let account = "account_example"; // String | Organization account name
let kind = "kind_example"; // String | Type of resource - in almost all cases this should be `variable`
let identifier = "identifier_example"; // String | URL-encoded variable ID
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'expirations': "expirations_example", // String | Tells the server to reset the variables expiration date
  'body': "body_example" // String | Secret data
};
apiInstance.createSecret(account, kind, identifier, opts, (error, data, response) => {
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
 **account** | **String**| Organization account name | 
 **kind** | **String**| Type of resource - in almost all cases this should be &#x60;variable&#x60; | 
 **identifier** | **String**| URL-encoded variable ID | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **expirations** | **String**| Tells the server to reset the variables expiration date | [optional] 
 **body** | **String**| Secret data | [optional] 

### Return type

null (empty response body)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: Not defined


## getSecret

> String getSecret(account, kind, identifier, opts)

Fetches the value of a secret from the specified Secret.

Fetches the value of a secret from the specified Secret. The latest version will be retrieved unless the version parameter is specified. The twenty most recent secret versions are retained.  The secret data is returned in the response body.  Note: Conjur will allow you to add a secret to any resource, but the best practice is to store and retrieve secret data only using Secret resources. 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.SecretsApi();
let account = "account_example"; // String | Organization account name
let kind = "kind_example"; // String | Type of resource - in almost all cases this should be `variable`
let identifier = "identifier_example"; // String | URL-encoded variable ID
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'version': 56 // Number | (**Optional**) Version you want to retrieve (Conjur keeps the last 20 versions of a secret)
};
apiInstance.getSecret(account, kind, identifier, opts, (error, data, response) => {
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
 **account** | **String**| Organization account name | 
 **kind** | **String**| Type of resource - in almost all cases this should be &#x60;variable&#x60; | 
 **identifier** | **String**| URL-encoded variable ID | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **version** | **Number**| (**Optional**) Version you want to retrieve (Conjur keeps the last 20 versions of a secret) | [optional] 

### Return type

**String**

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## getSecrets

> Object getSecrets(variableIds, opts)

Fetch multiple secrets

Fetches multiple secret values in one invocation. It’s faster to fetch secrets in batches than to fetch them one at a time.

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.SecretsApi();
let variableIds = "myorg:variable:secret1,myorg:variable:secret1"; // String | Comma-delimited, URL-encoded resource IDs of the variables.
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'acceptEncoding': "acceptEncoding_example" // String | Set the encoding of the response object
};
apiInstance.getSecrets(variableIds, opts, (error, data, response) => {
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
 **variableIds** | **String**| Comma-delimited, URL-encoded resource IDs of the variables. | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **acceptEncoding** | **String**| Set the encoding of the response object | [optional] 

### Return type

**Object**

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

