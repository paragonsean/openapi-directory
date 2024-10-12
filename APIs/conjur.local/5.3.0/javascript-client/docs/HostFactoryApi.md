# Conjur.HostFactoryApi

All URIs are relative to *http://conjur.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createHost**](HostFactoryApi.md#createHost) | **POST** /host_factories/hosts | Creates a Host using the Host Factory.
[**createToken**](HostFactoryApi.md#createToken) | **POST** /host_factory_tokens | Creates one or more host identity tokens.
[**revokeToken**](HostFactoryApi.md#revokeToken) | **DELETE** /host_factory_tokens/{token} | Revokes a token, immediately disabling it.



## createHost

> CreateHost201Response createHost(id, opts)

Creates a Host using the Host Factory.

Creates a Host using the Host Factory and returns a JSON description of it.  Requires a host factory token, which can be created using the create tokens API. In practice, this token is usually provided automatically as part of Conjur integration with your host provisioning infrastructure.  Note: If the token was created with a CIDR restriction, you must make this API request from a whitelisted address. 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.HostFactoryApi();
let id = "id_example"; // String | Identifier of the host to be created. It will be created within the account of the host factory.
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'annotations': {key: null} // Object | Annotations to apply to the new host
};
apiInstance.createHost(id, opts, (error, data, response) => {
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
 **id** | **String**| Identifier of the host to be created. It will be created within the account of the host factory. | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **annotations** | [**Object**](Object.md)| Annotations to apply to the new host | [optional] 

### Return type

[**CreateHost201Response**](CreateHost201Response.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## createToken

> [CreateToken200ResponseInner] createToken(expiration, hostFactory, opts)

Creates one or more host identity tokens.

Creates one or more tokens which can be used to bootstrap host identity. Responds with a JSON document containing the tokens and their restrictions.  If the tokens are created with a CIDR restriction, Conjur will only accept them from the whitelisted IP ranges.  ##### Permissions required # &#x60;execute&#x60; privilege on the Host Factory.\&quot; 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.HostFactoryApi();
let expiration = "expiration_example"; // String | `ISO 8601 datetime` denoting a requested expiration time.
let hostFactory = "hostFactory_example"; // String | Fully qualified host factory ID
let opts = {
  'xRequestId': "test-id", // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
  'cidr': ["null"], // [String] | Number of host tokens to create
  'count': 56 // Number | Number of host tokens to create
};
apiInstance.createToken(expiration, hostFactory, opts, (error, data, response) => {
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
 **expiration** | **String**| &#x60;ISO 8601 datetime&#x60; denoting a requested expiration time. | 
 **hostFactory** | **String**| Fully qualified host factory ID | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 
 **cidr** | [**[String]**](String.md)| Number of host tokens to create | [optional] 
 **count** | **Number**| Number of host tokens to create | [optional] 

### Return type

[**[CreateToken200ResponseInner]**](CreateToken200ResponseInner.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## revokeToken

> revokeToken(token, opts)

Revokes a token, immediately disabling it.

Revokes a token, immediately disabling it.  ##### Permissions required  &#x60;update&#x60; privilege on the host factory.\&quot; 

### Example

```javascript
import Conjur from 'conjur';
let defaultClient = Conjur.ApiClient.instance;
// Configure API key authorization: conjurAuth
let conjurAuth = defaultClient.authentications['conjurAuth'];
conjurAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//conjurAuth.apiKeyPrefix = 'Token';

let apiInstance = new Conjur.HostFactoryApi();
let token = "2c0vfj61pmah3efbgpcz2x9vzcy1ycskfkyqy0kgk1fv014880f4"; // String | The host factory token to revoke
let opts = {
  'xRequestId': "test-id" // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
};
apiInstance.revokeToken(token, opts, (error, data, response) => {
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
 **token** | **String**| The host factory token to revoke | 
 **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] 

### Return type

null (empty response body)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

