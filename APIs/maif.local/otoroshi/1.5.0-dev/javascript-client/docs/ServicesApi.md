# OtoroshiAdminApi.ServicesApi

All URIs are relative to *http://otoroshi-api.oto.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allServices**](ServicesApi.md#allServices) | **GET** /api/services | Get all services
[**createService**](ServicesApi.md#createService) | **POST** /api/services | Create a new service descriptor
[**createServiceTemplate**](ServicesApi.md#createServiceTemplate) | **POST** /api/services/{serviceId}/template | Create a service descriptor error template
[**deleteService**](ServicesApi.md#deleteService) | **DELETE** /api/services/{serviceId} | Delete a service descriptor
[**deleteServiceTemplate**](ServicesApi.md#deleteServiceTemplate) | **DELETE** /api/services/{serviceId}/template | Delete a service descriptor error template
[**patchService**](ServicesApi.md#patchService) | **PATCH** /api/services/{serviceId} | Update a service descriptor with a diff
[**service**](ServicesApi.md#service) | **GET** /api/services/{serviceId} | Get a service descriptor
[**serviceAddTarget**](ServicesApi.md#serviceAddTarget) | **POST** /api/services/{serviceId}/targets | Add a target to a service descriptor
[**serviceDeleteTarget**](ServicesApi.md#serviceDeleteTarget) | **DELETE** /api/services/{serviceId}/targets | Delete a service descriptor target
[**serviceGroupServices**](ServicesApi.md#serviceGroupServices) | **GET** /api/groups/{serviceGroupId}/services | Get all services descriptor for a group
[**serviceTargets**](ServicesApi.md#serviceTargets) | **GET** /api/services/{serviceId}/targets | Get a service descriptor targets
[**serviceTemplate**](ServicesApi.md#serviceTemplate) | **GET** /api/services/{serviceId}/template | Get a service descriptor error template
[**updateService**](ServicesApi.md#updateService) | **PUT** /api/services/{serviceId} | Update a service descriptor
[**updateServiceTargets**](ServicesApi.md#updateServiceTargets) | **PATCH** /api/services/{serviceId}/targets | Update a service descriptor targets
[**updateServiceTemplate**](ServicesApi.md#updateServiceTemplate) | **PUT** /api/services/{serviceId}/template | Update an error template to a service descriptor



## allServices

> [Service] allServices()

Get all services

Get all services

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ServicesApi();
apiInstance.allServices((error, data, response) => {
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

[**[Service]**](Service.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createService

> Service createService(opts)

Create a new service descriptor

Create a new service descriptor

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ServicesApi();
let opts = {
  'service': new OtoroshiAdminApi.Service() // Service | 
};
apiInstance.createService(opts, (error, data, response) => {
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
 **service** | [**Service**](Service.md)|  | [optional] 

### Return type

[**Service**](Service.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createServiceTemplate

> ErrorTemplate createServiceTemplate(serviceId, opts)

Create a service descriptor error template

Update a service descriptor targets

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ServicesApi();
let serviceId = "serviceId_example"; // String | The service id
let opts = {
  'errorTemplate': new OtoroshiAdminApi.ErrorTemplate() // ErrorTemplate | 
};
apiInstance.createServiceTemplate(serviceId, opts, (error, data, response) => {
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
 **serviceId** | **String**| The service id | 
 **errorTemplate** | [**ErrorTemplate**](ErrorTemplate.md)|  | [optional] 

### Return type

[**ErrorTemplate**](ErrorTemplate.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteService

> Deleted deleteService(serviceId)

Delete a service descriptor

Delete a service descriptor

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ServicesApi();
let serviceId = "serviceId_example"; // String | The service id
apiInstance.deleteService(serviceId, (error, data, response) => {
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
 **serviceId** | **String**| The service id | 

### Return type

[**Deleted**](Deleted.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteServiceTemplate

> Deleted deleteServiceTemplate(serviceId)

Delete a service descriptor error template

Delete a service descriptor error template

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ServicesApi();
let serviceId = "serviceId_example"; // String | The service id
apiInstance.deleteServiceTemplate(serviceId, (error, data, response) => {
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
 **serviceId** | **String**| The service id | 

### Return type

[**Deleted**](Deleted.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchService

> Service patchService(serviceId, opts)

Update a service descriptor with a diff

Update a service descriptor with a diff

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ServicesApi();
let serviceId = "serviceId_example"; // String | The service id
let opts = {
  'patchInner': [new OtoroshiAdminApi.PatchInner()] // [PatchInner] | 
};
apiInstance.patchService(serviceId, opts, (error, data, response) => {
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
 **serviceId** | **String**| The service id | 
 **patchInner** | [**[PatchInner]**](PatchInner.md)|  | [optional] 

### Return type

[**Service**](Service.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## service

> Service service(serviceId)

Get a service descriptor

Get a service descriptor

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ServicesApi();
let serviceId = "serviceId_example"; // String | The service id
apiInstance.service(serviceId, (error, data, response) => {
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
 **serviceId** | **String**| The service id | 

### Return type

[**Service**](Service.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceAddTarget

> [Target] serviceAddTarget(serviceId, opts)

Add a target to a service descriptor

Add a target to a service descriptor

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ServicesApi();
let serviceId = "serviceId_example"; // String | The service id
let opts = {
  'target': new OtoroshiAdminApi.Target() // Target | 
};
apiInstance.serviceAddTarget(serviceId, opts, (error, data, response) => {
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
 **serviceId** | **String**| The service id | 
 **target** | [**Target**](Target.md)|  | [optional] 

### Return type

[**[Target]**](Target.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serviceDeleteTarget

> [Target] serviceDeleteTarget(serviceId)

Delete a service descriptor target

Delete a service descriptor target

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ServicesApi();
let serviceId = "serviceId_example"; // String | The service id
apiInstance.serviceDeleteTarget(serviceId, (error, data, response) => {
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
 **serviceId** | **String**| The service id | 

### Return type

[**[Target]**](Target.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceGroupServices

> [ApiKey] serviceGroupServices(serviceGroupId)

Get all services descriptor for a group

Get all services descriptor for a group

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ServicesApi();
let serviceGroupId = "serviceGroupId_example"; // String | The service group id
apiInstance.serviceGroupServices(serviceGroupId, (error, data, response) => {
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
 **serviceGroupId** | **String**| The service group id | 

### Return type

[**[ApiKey]**](ApiKey.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceTargets

> [Target] serviceTargets(serviceId)

Get a service descriptor targets

Get a service descriptor targets

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ServicesApi();
let serviceId = "serviceId_example"; // String | The service id
apiInstance.serviceTargets(serviceId, (error, data, response) => {
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
 **serviceId** | **String**| The service id | 

### Return type

[**[Target]**](Target.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceTemplate

> ErrorTemplate serviceTemplate(serviceId)

Get a service descriptor error template

Get a service descriptor error template

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ServicesApi();
let serviceId = "serviceId_example"; // String | The service id
apiInstance.serviceTemplate(serviceId, (error, data, response) => {
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
 **serviceId** | **String**| The service id | 

### Return type

[**ErrorTemplate**](ErrorTemplate.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateService

> Service updateService(serviceId, opts)

Update a service descriptor

Update a service descriptor

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ServicesApi();
let serviceId = "serviceId_example"; // String | The service id
let opts = {
  'service': new OtoroshiAdminApi.Service() // Service | 
};
apiInstance.updateService(serviceId, opts, (error, data, response) => {
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
 **serviceId** | **String**| The service id | 
 **service** | [**Service**](Service.md)|  | [optional] 

### Return type

[**Service**](Service.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateServiceTargets

> [Target] updateServiceTargets(serviceId, opts)

Update a service descriptor targets

Update a service descriptor targets

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ServicesApi();
let serviceId = "serviceId_example"; // String | The service id
let opts = {
  'patchInner': [new OtoroshiAdminApi.PatchInner()] // [PatchInner] | 
};
apiInstance.updateServiceTargets(serviceId, opts, (error, data, response) => {
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
 **serviceId** | **String**| The service id | 
 **patchInner** | [**[PatchInner]**](PatchInner.md)|  | [optional] 

### Return type

[**[Target]**](Target.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateServiceTemplate

> ErrorTemplate updateServiceTemplate(serviceId, opts)

Update an error template to a service descriptor

Update an error template to a service descriptor

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.ServicesApi();
let serviceId = "serviceId_example"; // String | The service id
let opts = {
  'errorTemplate': new OtoroshiAdminApi.ErrorTemplate() // ErrorTemplate | 
};
apiInstance.updateServiceTemplate(serviceId, opts, (error, data, response) => {
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
 **serviceId** | **String**| The service id | 
 **errorTemplate** | [**ErrorTemplate**](ErrorTemplate.md)|  | [optional] 

### Return type

[**ErrorTemplate**](ErrorTemplate.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

