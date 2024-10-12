# GrowthServices.AdministrationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**administrationEntityGet**](AdministrationApi.md#administrationEntityGet) | **GET** /administration/entity | Get all organizations
[**administrationEntityIdDelete**](AdministrationApi.md#administrationEntityIdDelete) | **DELETE** /administration/entity/{id} | Delete organization
[**administrationEntityPost**](AdministrationApi.md#administrationEntityPost) | **POST** /administration/entity | Create organization
[**administrationEntityPut**](AdministrationApi.md#administrationEntityPut) | **PUT** /administration/entity | Pause organization
[**administrationFileToJsonPost**](AdministrationApi.md#administrationFileToJsonPost) | **POST** /administration/file-to-json | Transform data file to JSON format
[**administrationModelEntityIdGet**](AdministrationApi.md#administrationModelEntityIdGet) | **GET** /administration/model/{entityId} | Get Models for Organization
[**administrationModelEntityIdPost**](AdministrationApi.md#administrationModelEntityIdPost) | **POST** /administration/model/{entityId} | Register new forecasting model
[**administrationModelGet**](AdministrationApi.md#administrationModelGet) | **GET** /administration/model | Get all common Models
[**administrationModelPost**](AdministrationApi.md#administrationModelPost) | **POST** /administration/model | Register new forecasting model
[**administrationPlanningLevelEntityIdIdDelete**](AdministrationApi.md#administrationPlanningLevelEntityIdIdDelete) | **DELETE** /administration/planning-level/{entityId}/{id} | Delete planning level
[**administrationPlanningLevelLockPost**](AdministrationApi.md#administrationPlanningLevelLockPost) | **POST** /administration/planning-level/lock | Lock planning level
[**administrationTokenPost**](AdministrationApi.md#administrationTokenPost) | **POST** /administration/token | Issue a token
[**administrationUserEntityIdGet**](AdministrationApi.md#administrationUserEntityIdGet) | **GET** /administration/user/{entityId} | Get all users
[**administrationUserEntityIdIdDelete**](AdministrationApi.md#administrationUserEntityIdIdDelete) | **DELETE** /administration/user/{entityId}/{id} | Delete user
[**administrationUserLockPut**](AdministrationApi.md#administrationUserLockPut) | **PUT** /administration/user/lock | Lock user
[**administrationUserPost**](AdministrationApi.md#administrationUserPost) | **POST** /administration/user | Create user
[**administrationUserPut**](AdministrationApi.md#administrationUserPut) | **PUT** /administration/user | Update user



## administrationEntityGet

> [EntityResponse] administrationEntityGet(opts)

Get all organizations

This is an iCUE only endpoint or Enterprise feature.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.AdministrationApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.administrationEntityGet(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 

### Return type

[**[EntityResponse]**](EntityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## administrationEntityIdDelete

> administrationEntityIdDelete(id, opts)

Delete organization

This is an iCUE only endpoint or Enterprise feature.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.AdministrationApi();
let id = 56; // Number | 
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.administrationEntityIdDelete(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## administrationEntityPost

> String administrationEntityPost(opts)

Create organization

This is an iCUE only endpoint or Enterprise feature.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.AdministrationApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'newEntityRequest': new GrowthServices.NewEntityRequest() // NewEntityRequest | 
};
apiInstance.administrationEntityPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 
 **newEntityRequest** | [**NewEntityRequest**](NewEntityRequest.md)|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain


## administrationEntityPut

> administrationEntityPut(opts)

Pause organization

This is an iCUE only endpoint or Enterprise feature.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.AdministrationApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'toggleRequest': new GrowthServices.ToggleRequest() // ToggleRequest | 
};
apiInstance.administrationEntityPut(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 
 **toggleRequest** | [**ToggleRequest**](ToggleRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined


## administrationFileToJsonPost

> JsonForecastResponse administrationFileToJsonPost(file, periodicity, opts)

Transform data file to JSON format

Transform data file to JSON format

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.AdministrationApi();
let file = "/path/to/file"; // File | 
let periodicity = 56; // Number | 
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.administrationFileToJsonPost(file, periodicity, opts, (error, data, response) => {
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
 **file** | **File**|  | 
 **periodicity** | **Number**|  | 
 **token** | **String**| User Authentication Token | [optional] 

### Return type

[**JsonForecastResponse**](JsonForecastResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, text/json, text/plain


## administrationModelEntityIdGet

> [MethodDto] administrationModelEntityIdGet(entityId, opts)

Get Models for Organization

Returns models registered for Organization

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.AdministrationApi();
let entityId = 56; // Number | 
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.administrationModelEntityIdGet(entityId, opts, (error, data, response) => {
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
 **entityId** | **Number**|  | 
 **token** | **String**| User Authentication Token | [optional] 

### Return type

[**[MethodDto]**](MethodDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## administrationModelEntityIdPost

> MethodDto administrationModelEntityIdPost(entityId, opts)

Register new forecasting model

Register new forecasting model for single organziation

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.AdministrationApi();
let entityId = 56; // Number | 
let opts = {
  'token': "token_example", // String | User Authentication Token
  'newModelRequest': new GrowthServices.NewModelRequest() // NewModelRequest | 
};
apiInstance.administrationModelEntityIdPost(entityId, opts, (error, data, response) => {
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
 **entityId** | **Number**|  | 
 **token** | **String**| User Authentication Token | [optional] 
 **newModelRequest** | [**NewModelRequest**](NewModelRequest.md)|  | [optional] 

### Return type

[**MethodDto**](MethodDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain


## administrationModelGet

> [MethodDto] administrationModelGet(opts)

Get all common Models

Returns models that are common for all Organizations

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.AdministrationApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.administrationModelGet(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 

### Return type

[**[MethodDto]**](MethodDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## administrationModelPost

> MethodDto administrationModelPost(opts)

Register new forecasting model

Register new forecasting model for all organziations

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.AdministrationApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'newModelRequest': new GrowthServices.NewModelRequest() // NewModelRequest | 
};
apiInstance.administrationModelPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 
 **newModelRequest** | [**NewModelRequest**](NewModelRequest.md)|  | [optional] 

### Return type

[**MethodDto**](MethodDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain


## administrationPlanningLevelEntityIdIdDelete

> administrationPlanningLevelEntityIdIdDelete(entityId, id, opts)

Delete planning level

Delete planning level. This is an Enterprise feature.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.AdministrationApi();
let entityId = 56; // Number | 
let id = 56; // Number | 
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.administrationPlanningLevelEntityIdIdDelete(entityId, id, opts, (error, data, response) => {
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
 **entityId** | **Number**|  | 
 **id** | **Number**|  | 
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## administrationPlanningLevelLockPost

> administrationPlanningLevelLockPost(opts)

Lock planning level

Lock planning level against modification. This is an Enterprise feature.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.AdministrationApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.administrationPlanningLevelLockPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## administrationTokenPost

> String administrationTokenPost(opts)

Issue a token

This is an iCUE only endpoint.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.AdministrationApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'newTokenRequest': new GrowthServices.NewTokenRequest() // NewTokenRequest | 
};
apiInstance.administrationTokenPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 
 **newTokenRequest** | [**NewTokenRequest**](NewTokenRequest.md)|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain


## administrationUserEntityIdGet

> administrationUserEntityIdGet(entityId, opts)

Get all users

Get all users

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.AdministrationApi();
let entityId = 56; // Number | 
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.administrationUserEntityIdGet(entityId, opts, (error, data, response) => {
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
 **entityId** | **Number**|  | 
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## administrationUserEntityIdIdDelete

> administrationUserEntityIdIdDelete(entityId, id, opts)

Delete user

Delete user

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.AdministrationApi();
let entityId = 56; // Number | 
let id = 56; // Number | 
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.administrationUserEntityIdIdDelete(entityId, id, opts, (error, data, response) => {
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
 **entityId** | **Number**|  | 
 **id** | **Number**|  | 
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## administrationUserLockPut

> administrationUserLockPut(opts)

Lock user

After lock user won&#39;t be able to use iCUE API endpoints.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.AdministrationApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'toggleUserRequest': new GrowthServices.ToggleUserRequest() // ToggleUserRequest | 
};
apiInstance.administrationUserLockPut(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 
 **toggleUserRequest** | [**ToggleUserRequest**](ToggleUserRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: Not defined


## administrationUserPost

> String administrationUserPost(opts)

Create user

Create new user for entity/organization. This can be done by entity administrator.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.AdministrationApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'newUserRequest': new GrowthServices.NewUserRequest() // NewUserRequest | 
};
apiInstance.administrationUserPost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 
 **newUserRequest** | [**NewUserRequest**](NewUserRequest.md)|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain


## administrationUserPut

> administrationUserPut(opts)

Update user

Update user

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.AdministrationApi();
let opts = {
  'token': "token_example" // String | User Authentication Token
};
apiInstance.administrationUserPut(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

