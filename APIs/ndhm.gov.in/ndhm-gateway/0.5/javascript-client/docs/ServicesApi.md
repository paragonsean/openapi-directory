# Gateway.ServicesApi

All URIs are relative to *https://dev.ndhm.gov.in/gateway*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v05HiServicesServiceIdGet**](ServicesApi.md#v05HiServicesServiceIdGet) | **GET** /v0.5/hi-services/{service-id} | Get bridge service details/profile by the serviceId provided.



## v05HiServicesServiceIdGet

> ServiceProfileResponse v05HiServicesServiceIdGet(authorization, serviceId)

Get bridge service details/profile by the serviceId provided.

This API is meant for displaying the bridge service details by the serviceId provided . 

### Example

```javascript
import Gateway from 'gateway';

let apiInstance = new Gateway.ServicesApi();
let authorization = "authorization_example"; // String | Access token which was issued after successful login with gateway auth server.
let serviceId = "serviceId_example"; // String | 
apiInstance.v05HiServicesServiceIdGet(authorization, serviceId, (error, data, response) => {
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
 **authorization** | **String**| Access token which was issued after successful login with gateway auth server. | 
 **serviceId** | **String**|  | 

### Return type

[**ServiceProfileResponse**](ServiceProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

