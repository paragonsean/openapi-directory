# RebillyRestApi.Class3DSecureApi

All URIs are relative to *https://api-sandbox.rebilly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get3DSecure**](Class3DSecureApi.md#get3DSecure) | **GET** /3dsecure/{id} | Retrieve a ThreeDSecure entry
[**get3DSecureCollection**](Class3DSecureApi.md#get3DSecureCollection) | **GET** /3dsecure | Retrieve a list of ThreeDSecure entries
[**post3DSecure**](Class3DSecureApi.md#post3DSecure) | **POST** /3dsecure | Create a ThreeDSecure entry



## get3DSecure

> ThreeDSecure get3DSecure(id, opts)

Retrieve a ThreeDSecure entry

Retrieve a ThreeDSecure entry with specified identifier string. 

### Example

```javascript
import RebillyRestApi from 'rebilly_rest_api';
let defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: SecretApiKey
let SecretApiKey = defaultClient.authentications['SecretApiKey'];
SecretApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SecretApiKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new RebillyRestApi.Class3DSecureApi();
let id = "id_example"; // String | The resource identifier string.
let opts = {
  'organizationId': "organizationId_example" // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
};
apiInstance.get3DSecure(id, opts, (error, data, response) => {
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
 **id** | **String**| The resource identifier string. | 
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 

### Return type

[**ThreeDSecure**](ThreeDSecure.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get3DSecureCollection

> [ThreeDSecure] get3DSecureCollection(opts)

Retrieve a list of ThreeDSecure entries

### Example

```javascript
import RebillyRestApi from 'rebilly_rest_api';
let defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: SecretApiKey
let SecretApiKey = defaultClient.authentications['SecretApiKey'];
SecretApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SecretApiKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new RebillyRestApi.Class3DSecureApi();
let opts = {
  'organizationId': "organizationId_example", // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
  'limit': 56, // Number | The collection items limit.
  'offset': 56 // Number | The collection items offset.
};
apiInstance.get3DSecureCollection(opts, (error, data, response) => {
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
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 
 **limit** | **Number**| The collection items limit. | [optional] 
 **offset** | **Number**| The collection items offset. | [optional] 

### Return type

[**[ThreeDSecure]**](ThreeDSecure.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## post3DSecure

> ThreeDSecure post3DSecure(threeDSecure, opts)

Create a ThreeDSecure entry

Create a ThreeDSecure entry. 

### Example

```javascript
import RebillyRestApi from 'rebilly_rest_api';
let defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: SecretApiKey
let SecretApiKey = defaultClient.authentications['SecretApiKey'];
SecretApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SecretApiKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new RebillyRestApi.Class3DSecureApi();
let threeDSecure = new RebillyRestApi.ThreeDSecure(); // ThreeDSecure | ThreeDSecure resource.
let opts = {
  'organizationId': "organizationId_example" // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
};
apiInstance.post3DSecure(threeDSecure, opts, (error, data, response) => {
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
 **threeDSecure** | [**ThreeDSecure**](ThreeDSecure.md)| ThreeDSecure resource. | 
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 

### Return type

[**ThreeDSecure**](ThreeDSecure.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

