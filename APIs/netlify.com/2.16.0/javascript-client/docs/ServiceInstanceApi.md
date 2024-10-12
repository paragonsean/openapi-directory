# NetlifysApiDocumentation.ServiceInstanceApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createServiceInstance**](ServiceInstanceApi.md#createServiceInstance) | **POST** /sites/{site_id}/services/{addon}/instances | 
[**deleteServiceInstance**](ServiceInstanceApi.md#deleteServiceInstance) | **DELETE** /sites/{site_id}/services/{addon}/instances/{instance_id} | 
[**listServiceInstancesForSite**](ServiceInstanceApi.md#listServiceInstancesForSite) | **GET** /sites/{site_id}/service-instances | 
[**showServiceInstance**](ServiceInstanceApi.md#showServiceInstance) | **GET** /sites/{site_id}/services/{addon}/instances/{instance_id} | 
[**updateServiceInstance**](ServiceInstanceApi.md#updateServiceInstance) | **PUT** /sites/{site_id}/services/{addon}/instances/{instance_id} | 



## createServiceInstance

> ServiceInstance createServiceInstance(siteId, addon, config)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.ServiceInstanceApi();
let siteId = "siteId_example"; // String | 
let addon = "addon_example"; // String | 
let config = {key: null}; // Object | 
apiInstance.createServiceInstance(siteId, addon, config, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **addon** | **String**|  | 
 **config** | **Object**|  | 

### Return type

[**ServiceInstance**](ServiceInstance.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteServiceInstance

> deleteServiceInstance(siteId, addon, instanceId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.ServiceInstanceApi();
let siteId = "siteId_example"; // String | 
let addon = "addon_example"; // String | 
let instanceId = "instanceId_example"; // String | 
apiInstance.deleteServiceInstance(siteId, addon, instanceId, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **addon** | **String**|  | 
 **instanceId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServiceInstancesForSite

> [ServiceInstance] listServiceInstancesForSite(siteId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.ServiceInstanceApi();
let siteId = "siteId_example"; // String | 
apiInstance.listServiceInstancesForSite(siteId, (error, data, response) => {
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
 **siteId** | **String**|  | 

### Return type

[**[ServiceInstance]**](ServiceInstance.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showServiceInstance

> ServiceInstance showServiceInstance(siteId, addon, instanceId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.ServiceInstanceApi();
let siteId = "siteId_example"; // String | 
let addon = "addon_example"; // String | 
let instanceId = "instanceId_example"; // String | 
apiInstance.showServiceInstance(siteId, addon, instanceId, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **addon** | **String**|  | 
 **instanceId** | **String**|  | 

### Return type

[**ServiceInstance**](ServiceInstance.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateServiceInstance

> updateServiceInstance(siteId, addon, instanceId, config)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.ServiceInstanceApi();
let siteId = "siteId_example"; // String | 
let addon = "addon_example"; // String | 
let instanceId = "instanceId_example"; // String | 
let config = {key: null}; // Object | 
apiInstance.updateServiceInstance(siteId, addon, instanceId, config, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **addon** | **String**|  | 
 **instanceId** | **String**|  | 
 **config** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

