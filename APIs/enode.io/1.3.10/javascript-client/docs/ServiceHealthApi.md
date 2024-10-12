# EnodeApi.ServiceHealthApi

All URIs are relative to *https://api.test.enode.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getHealthReady**](ServiceHealthApi.md#getHealthReady) | **GET** /health/ready | Check Service Readiness
[**getHealthVendors**](ServiceHealthApi.md#getHealthVendors) | **GET** /health/vendors | Check Available Vendors



## getHealthReady

> getHealthReady()

Check Service Readiness

Gets the combined health status of the service and all functionalities and dependencies.

### Example

```javascript
import EnodeApi from 'enode_api';

let apiInstance = new EnodeApi.ServiceHealthApi();
apiInstance.getHealthReady((error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHealthVendors

> [GetHealthVendors200ResponseInner] getHealthVendors()

Check Available Vendors

List the supported vendors and their current status.

### Example

```javascript
import EnodeApi from 'enode_api';

let apiInstance = new EnodeApi.ServiceHealthApi();
apiInstance.getHealthVendors((error, data, response) => {
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

[**[GetHealthVendors200ResponseInner]**](GetHealthVendors200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

