# NetBoxApi.TenancyApi

All URIs are relative to *http://netboxdemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenancyChoicesList**](TenancyApi.md#tenancyChoicesList) | **GET** /tenancy/_choices/ | 
[**tenancyChoicesRead**](TenancyApi.md#tenancyChoicesRead) | **GET** /tenancy/_choices/{id}/ | 
[**tenancyTenantGroupsCreate**](TenancyApi.md#tenancyTenantGroupsCreate) | **POST** /tenancy/tenant-groups/ | 
[**tenancyTenantGroupsDelete**](TenancyApi.md#tenancyTenantGroupsDelete) | **DELETE** /tenancy/tenant-groups/{id}/ | 
[**tenancyTenantGroupsList**](TenancyApi.md#tenancyTenantGroupsList) | **GET** /tenancy/tenant-groups/ | 
[**tenancyTenantGroupsPartialUpdate**](TenancyApi.md#tenancyTenantGroupsPartialUpdate) | **PATCH** /tenancy/tenant-groups/{id}/ | 
[**tenancyTenantGroupsRead**](TenancyApi.md#tenancyTenantGroupsRead) | **GET** /tenancy/tenant-groups/{id}/ | 
[**tenancyTenantGroupsUpdate**](TenancyApi.md#tenancyTenantGroupsUpdate) | **PUT** /tenancy/tenant-groups/{id}/ | 
[**tenancyTenantsCreate**](TenancyApi.md#tenancyTenantsCreate) | **POST** /tenancy/tenants/ | 
[**tenancyTenantsDelete**](TenancyApi.md#tenancyTenantsDelete) | **DELETE** /tenancy/tenants/{id}/ | 
[**tenancyTenantsList**](TenancyApi.md#tenancyTenantsList) | **GET** /tenancy/tenants/ | 
[**tenancyTenantsPartialUpdate**](TenancyApi.md#tenancyTenantsPartialUpdate) | **PATCH** /tenancy/tenants/{id}/ | 
[**tenancyTenantsRead**](TenancyApi.md#tenancyTenantsRead) | **GET** /tenancy/tenants/{id}/ | 
[**tenancyTenantsUpdate**](TenancyApi.md#tenancyTenantsUpdate) | **PUT** /tenancy/tenants/{id}/ | 



## tenancyChoicesList

> tenancyChoicesList()





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.TenancyApi();
apiInstance.tenancyChoicesList((error, data, response) => {
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


## tenancyChoicesRead

> tenancyChoicesRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.TenancyApi();
let id = "id_example"; // String | 
apiInstance.tenancyChoicesRead(id, (error, data, response) => {
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


## tenancyTenantGroupsCreate

> TenantGroup tenancyTenantGroupsCreate(tenantGroup)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.TenancyApi();
let tenantGroup = new NetBoxApi.TenantGroup(); // TenantGroup | 
apiInstance.tenancyTenantGroupsCreate(tenantGroup, (error, data, response) => {
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
 **tenantGroup** | [**TenantGroup**](TenantGroup.md)|  | 

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tenancyTenantGroupsDelete

> tenancyTenantGroupsDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.TenancyApi();
let id = 56; // Number | A unique integer value identifying this tenant group.
apiInstance.tenancyTenantGroupsDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this tenant group. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## tenancyTenantGroupsList

> TenancyTenantGroupsList200Response tenancyTenantGroupsList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.TenancyApi();
let opts = {
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.tenancyTenantGroupsList(opts, (error, data, response) => {
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

[**TenancyTenantGroupsList200Response**](TenancyTenantGroupsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tenancyTenantGroupsPartialUpdate

> TenantGroup tenancyTenantGroupsPartialUpdate(id, tenantGroup)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.TenancyApi();
let id = 56; // Number | A unique integer value identifying this tenant group.
let tenantGroup = new NetBoxApi.TenantGroup(); // TenantGroup | 
apiInstance.tenancyTenantGroupsPartialUpdate(id, tenantGroup, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this tenant group. | 
 **tenantGroup** | [**TenantGroup**](TenantGroup.md)|  | 

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tenancyTenantGroupsRead

> TenantGroup tenancyTenantGroupsRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.TenancyApi();
let id = 56; // Number | A unique integer value identifying this tenant group.
apiInstance.tenancyTenantGroupsRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this tenant group. | 

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tenancyTenantGroupsUpdate

> TenantGroup tenancyTenantGroupsUpdate(id, tenantGroup)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.TenancyApi();
let id = 56; // Number | A unique integer value identifying this tenant group.
let tenantGroup = new NetBoxApi.TenantGroup(); // TenantGroup | 
apiInstance.tenancyTenantGroupsUpdate(id, tenantGroup, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this tenant group. | 
 **tenantGroup** | [**TenantGroup**](TenantGroup.md)|  | 

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tenancyTenantsCreate

> Tenant tenancyTenantsCreate(writableTenant)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.TenancyApi();
let writableTenant = new NetBoxApi.WritableTenant(); // WritableTenant | 
apiInstance.tenancyTenantsCreate(writableTenant, (error, data, response) => {
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
 **writableTenant** | [**WritableTenant**](WritableTenant.md)|  | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tenancyTenantsDelete

> tenancyTenantsDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.TenancyApi();
let id = 56; // Number | A unique integer value identifying this tenant.
apiInstance.tenancyTenantsDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this tenant. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## tenancyTenantsList

> TenancyTenantsList200Response tenancyTenantsList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.TenancyApi();
let opts = {
  'name': "name_example", // String | 
  'idIn': "idIn_example", // String | Multiple values may be separated by commas.
  'q': "q_example", // String | 
  'groupId': "groupId_example", // String | 
  'group': "group_example", // String | 
  'tag': "tag_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.tenancyTenantsList(opts, (error, data, response) => {
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
 **groupId** | **String**|  | [optional] 
 **group** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**TenancyTenantsList200Response**](TenancyTenantsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tenancyTenantsPartialUpdate

> Tenant tenancyTenantsPartialUpdate(id, writableTenant)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.TenancyApi();
let id = 56; // Number | A unique integer value identifying this tenant.
let writableTenant = new NetBoxApi.WritableTenant(); // WritableTenant | 
apiInstance.tenancyTenantsPartialUpdate(id, writableTenant, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this tenant. | 
 **writableTenant** | [**WritableTenant**](WritableTenant.md)|  | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tenancyTenantsRead

> Tenant tenancyTenantsRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.TenancyApi();
let id = 56; // Number | A unique integer value identifying this tenant.
apiInstance.tenancyTenantsRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this tenant. | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## tenancyTenantsUpdate

> Tenant tenancyTenantsUpdate(id, writableTenant)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.TenancyApi();
let id = 56; // Number | A unique integer value identifying this tenant.
let writableTenant = new NetBoxApi.WritableTenant(); // WritableTenant | 
apiInstance.tenancyTenantsUpdate(id, writableTenant, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this tenant. | 
 **writableTenant** | [**WritableTenant**](WritableTenant.md)|  | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

