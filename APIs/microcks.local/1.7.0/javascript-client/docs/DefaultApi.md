# MicrocksApiV17.DefaultApi

All URIs are relative to *http://microcks.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getResource**](DefaultApi.md#getResource) | **GET** /resources/{name} | Get Resource
[**getResourcesByService**](DefaultApi.md#getResourcesByService) | **GET** /resources/service/{serviceId} | Get Resources by Service



## getResource

> Resource getResource(name)

Get Resource

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.DefaultApi();
let name = "name_example"; // String | Unique name/business identifier of the Service or API resource
apiInstance.getResource(name, (error, data, response) => {
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
 **name** | **String**| Unique name/business identifier of the Service or API resource | 

### Return type

[**Resource**](Resource.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getResourcesByService

> [Resource] getResourcesByService(serviceId)

Get Resources by Service

### Example

```javascript
import MicrocksApiV17 from 'microcks_api_v1_7';
let defaultClient = MicrocksApiV17.ApiClient.instance;
// Configure OAuth2 access token for authorization: jwt-bearer
let jwt-bearer = defaultClient.authentications['jwt-bearer'];
jwt-bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrocksApiV17.DefaultApi();
let serviceId = "serviceId_example"; // String | Unique identifier of the Service or API the resources are attached to
apiInstance.getResourcesByService(serviceId, (error, data, response) => {
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
 **serviceId** | **String**| Unique identifier of the Service or API the resources are attached to | 

### Return type

[**[Resource]**](Resource.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

