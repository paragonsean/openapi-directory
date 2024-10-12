# OtoroshiAdminApi.ApikeysApi

All URIs are relative to *http://otoroshi-api.oto.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allApiKeys**](ApikeysApi.md#allApiKeys) | **GET** /api/apikeys | Get all api keys
[**apiKey**](ApikeysApi.md#apiKey) | **GET** /api/services/{serviceId}/apikeys/{clientId} | Get an api key
[**apiKeyFromGroup**](ApikeysApi.md#apiKeyFromGroup) | **GET** /api/groups/{groupId}/apikeys/{clientId} | Get an api key
[**apiKeyFromGroupQuotas**](ApikeysApi.md#apiKeyFromGroupQuotas) | **GET** /api/groups/{groupId}/apikeys/{clientId}/quotas | Get the quota state of an api key
[**apiKeyGroup**](ApikeysApi.md#apiKeyGroup) | **GET** /api/services/{serviceId}/apikeys/{clientId}/group | Get the group of an api key
[**apiKeyQuotas**](ApikeysApi.md#apiKeyQuotas) | **GET** /api/services/{serviceId}/apikeys/{clientId}/quotas | Get the quota state of an api key
[**apiKeys**](ApikeysApi.md#apiKeys) | **GET** /api/services/{serviceId}/apikeys | Get all api keys for the group of a service
[**apiKeysFromGroup**](ApikeysApi.md#apiKeysFromGroup) | **GET** /api/groups/{groupId}/apikeys | Get all api keys for the group of a service
[**createApiKey**](ApikeysApi.md#createApiKey) | **POST** /api/services/{serviceId}/apikeys | Create a new api key for a service
[**createApiKeyFromGroup**](ApikeysApi.md#createApiKeyFromGroup) | **POST** /api/groups/{groupId}/apikeys | Create a new api key for a group
[**deleteApiKey**](ApikeysApi.md#deleteApiKey) | **DELETE** /api/services/{serviceId}/apikeys/{clientId} | Delete an api key
[**deleteApiKeyFromGroup**](ApikeysApi.md#deleteApiKeyFromGroup) | **DELETE** /api/groups/{groupId}/apikeys/{clientId} | Delete an api key
[**patchApiKey**](ApikeysApi.md#patchApiKey) | **PATCH** /api/services/{serviceId}/apikeys/{clientId} | Update an api key with a diff
[**patchApiKeyFromGroup**](ApikeysApi.md#patchApiKeyFromGroup) | **PATCH** /api/groups/{groupId}/apikeys/{clientId} | Update an api key with a diff
[**resetApiKeyFromGroupQuotas**](ApikeysApi.md#resetApiKeyFromGroupQuotas) | **DELETE** /api/groups/{groupId}/apikeys/{clientId}/quotas | Reset the quota state of an api key
[**resetApiKeyQuotas**](ApikeysApi.md#resetApiKeyQuotas) | **DELETE** /api/services/{serviceId}/apikeys/{clientId}/quotas | Reset the quota state of an api key
[**updateApiKey**](ApikeysApi.md#updateApiKey) | **PUT** /api/services/{serviceId}/apikeys/{clientId} | Update an api key
[**updateApiKeyFromGroup**](ApikeysApi.md#updateApiKeyFromGroup) | **PUT** /api/groups/{groupId}/apikeys/{clientId} | Update an api key



## allApiKeys

> [ApiKey] allApiKeys()

Get all api keys

Get all api keys

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ApikeysApi();
apiInstance.allApiKeys((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[ApiKey]**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiKey

> ApiKey apiKey(serviceId, clientId)

Get an api key

Get an api key for a specified service descriptor

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ApikeysApi();
let serviceId = "serviceId_example"; // String | The api key service id
let clientId = "clientId_example"; // String | the api key id
apiInstance.apiKey(serviceId, clientId, (error, data, response) => {
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
 **serviceId** | **String**| The api key service id | 
 **clientId** | **String**| the api key id | 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiKeyFromGroup

> ApiKey apiKeyFromGroup(groupId, clientId)

Get an api key

Get an api key for a specified service group

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ApikeysApi();
let groupId = "groupId_example"; // String | The api key group id
let clientId = "clientId_example"; // String | the api key id
apiInstance.apiKeyFromGroup(groupId, clientId, (error, data, response) => {
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
 **groupId** | **String**| The api key group id | 
 **clientId** | **String**| the api key id | 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiKeyFromGroupQuotas

> Quotas apiKeyFromGroupQuotas(groupId, clientId)

Get the quota state of an api key

Get the quota state of an api key

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ApikeysApi();
let groupId = "groupId_example"; // String | The api key group id
let clientId = "clientId_example"; // String | the api key id
apiInstance.apiKeyFromGroupQuotas(groupId, clientId, (error, data, response) => {
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
 **groupId** | **String**| The api key group id | 
 **clientId** | **String**| the api key id | 

### Return type

[**Quotas**](Quotas.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiKeyGroup

> Group apiKeyGroup(serviceId, clientId)

Get the group of an api key

Get the group of an api key

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ApikeysApi();
let serviceId = "serviceId_example"; // String | The api key service id
let clientId = "clientId_example"; // String | the api key id
apiInstance.apiKeyGroup(serviceId, clientId, (error, data, response) => {
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
 **serviceId** | **String**| The api key service id | 
 **clientId** | **String**| the api key id | 

### Return type

[**Group**](Group.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiKeyQuotas

> Quotas apiKeyQuotas(serviceId, clientId)

Get the quota state of an api key

Get the quota state of an api key

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ApikeysApi();
let serviceId = "serviceId_example"; // String | The api key service id
let clientId = "clientId_example"; // String | the api key id
apiInstance.apiKeyQuotas(serviceId, clientId, (error, data, response) => {
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
 **serviceId** | **String**| The api key service id | 
 **clientId** | **String**| the api key id | 

### Return type

[**Quotas**](Quotas.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiKeys

> [ApiKey] apiKeys(serviceId)

Get all api keys for the group of a service

Get all api keys for the group of a service

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ApikeysApi();
let serviceId = "serviceId_example"; // String | The api key service id
apiInstance.apiKeys(serviceId, (error, data, response) => {
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
 **serviceId** | **String**| The api key service id | 

### Return type

[**[ApiKey]**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiKeysFromGroup

> [ApiKey] apiKeysFromGroup(groupId)

Get all api keys for the group of a service

Get all api keys for the group of a service

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ApikeysApi();
let groupId = "groupId_example"; // String | The api key group id
apiInstance.apiKeysFromGroup(groupId, (error, data, response) => {
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
 **groupId** | **String**| The api key group id | 

### Return type

[**[ApiKey]**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createApiKey

> ApiKey createApiKey(serviceId, opts)

Create a new api key for a service



### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ApikeysApi();
let serviceId = "serviceId_example"; // String | The api key service id
let opts = {
  'apiKey': new OtoroshiAdminApi.ApiKey() // ApiKey | 
};
apiInstance.createApiKey(serviceId, opts, (error, data, response) => {
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
 **serviceId** | **String**| The api key service id | 
 **apiKey** | [**ApiKey**](ApiKey.md)|  | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createApiKeyFromGroup

> ApiKey createApiKeyFromGroup(groupId, opts)

Create a new api key for a group

Create a new api key for a group

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ApikeysApi();
let groupId = "groupId_example"; // String | The api key group id
let opts = {
  'apiKey': new OtoroshiAdminApi.ApiKey() // ApiKey | 
};
apiInstance.createApiKeyFromGroup(groupId, opts, (error, data, response) => {
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
 **groupId** | **String**| The api key group id | 
 **apiKey** | [**ApiKey**](ApiKey.md)|  | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteApiKey

> Deleted deleteApiKey(serviceId, clientId)

Delete an api key

Delete an api key for a specified service descriptor

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ApikeysApi();
let serviceId = "serviceId_example"; // String | The api key service id
let clientId = "clientId_example"; // String | the api key id
apiInstance.deleteApiKey(serviceId, clientId, (error, data, response) => {
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
 **serviceId** | **String**| The api key service id | 
 **clientId** | **String**| the api key id | 

### Return type

[**Deleted**](Deleted.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteApiKeyFromGroup

> Deleted deleteApiKeyFromGroup(groupId, clientId)

Delete an api key

Delete an api key for a specified service group

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ApikeysApi();
let groupId = "groupId_example"; // String | The api key group id
let clientId = "clientId_example"; // String | the api key id
apiInstance.deleteApiKeyFromGroup(groupId, clientId, (error, data, response) => {
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
 **groupId** | **String**| The api key group id | 
 **clientId** | **String**| the api key id | 

### Return type

[**Deleted**](Deleted.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchApiKey

> ApiKey patchApiKey(serviceId, clientId, opts)

Update an api key with a diff

Update an api key for a specified service descriptor with a diff

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ApikeysApi();
let serviceId = "serviceId_example"; // String | The api key service id
let clientId = "clientId_example"; // String | the api key id
let opts = {
  'patchInner': [new OtoroshiAdminApi.PatchInner()] // [PatchInner] | 
};
apiInstance.patchApiKey(serviceId, clientId, opts, (error, data, response) => {
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
 **serviceId** | **String**| The api key service id | 
 **clientId** | **String**| the api key id | 
 **patchInner** | [**[PatchInner]**](PatchInner.md)|  | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## patchApiKeyFromGroup

> ApiKey patchApiKeyFromGroup(groupId, clientId, opts)

Update an api key with a diff

Update an api key for a specified service descriptor with a diff

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ApikeysApi();
let groupId = "groupId_example"; // String | The api key group id
let clientId = "clientId_example"; // String | the api key id
let opts = {
  'patchInner': [new OtoroshiAdminApi.PatchInner()] // [PatchInner] | 
};
apiInstance.patchApiKeyFromGroup(groupId, clientId, opts, (error, data, response) => {
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
 **groupId** | **String**| The api key group id | 
 **clientId** | **String**| the api key id | 
 **patchInner** | [**[PatchInner]**](PatchInner.md)|  | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## resetApiKeyFromGroupQuotas

> Quotas resetApiKeyFromGroupQuotas(groupId, clientId)

Reset the quota state of an api key

Reset the quota state of an api key

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ApikeysApi();
let groupId = "groupId_example"; // String | The api key group id
let clientId = "clientId_example"; // String | the api key id
apiInstance.resetApiKeyFromGroupQuotas(groupId, clientId, (error, data, response) => {
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
 **groupId** | **String**| The api key group id | 
 **clientId** | **String**| the api key id | 

### Return type

[**Quotas**](Quotas.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resetApiKeyQuotas

> Quotas resetApiKeyQuotas(serviceId, clientId)

Reset the quota state of an api key

Reset the quota state of an api key

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ApikeysApi();
let serviceId = "serviceId_example"; // String | The api key service id
let clientId = "clientId_example"; // String | the api key id
apiInstance.resetApiKeyQuotas(serviceId, clientId, (error, data, response) => {
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
 **serviceId** | **String**| The api key service id | 
 **clientId** | **String**| the api key id | 

### Return type

[**Quotas**](Quotas.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateApiKey

> ApiKey updateApiKey(serviceId, clientId, opts)

Update an api key

Update an api key for a specified service descriptor

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ApikeysApi();
let serviceId = "serviceId_example"; // String | The api key service id
let clientId = "clientId_example"; // String | the api key id
let opts = {
  'apiKey': new OtoroshiAdminApi.ApiKey() // ApiKey | 
};
apiInstance.updateApiKey(serviceId, clientId, opts, (error, data, response) => {
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
 **serviceId** | **String**| The api key service id | 
 **clientId** | **String**| the api key id | 
 **apiKey** | [**ApiKey**](ApiKey.md)|  | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateApiKeyFromGroup

> ApiKey updateApiKeyFromGroup(groupId, clientId, opts)

Update an api key

Update an api key for a specified service group

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ApikeysApi();
let groupId = "groupId_example"; // String | The api key group id
let clientId = "clientId_example"; // String | the api key id
let opts = {
  'apiKey': new OtoroshiAdminApi.ApiKey() // ApiKey | 
};
apiInstance.updateApiKeyFromGroup(groupId, clientId, opts, (error, data, response) => {
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
 **groupId** | **String**| The api key group id | 
 **clientId** | **String**| the api key id | 
 **apiKey** | [**ApiKey**](ApiKey.md)|  | [optional] 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

