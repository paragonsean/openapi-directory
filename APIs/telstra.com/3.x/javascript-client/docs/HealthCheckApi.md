# MessagingApiV3X.HealthCheckApi

All URIs are relative to *https://products.api.telstra.com/messaging/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthCheck**](HealthCheckApi.md#healthCheck) | **GET** /health-check | health check



## healthCheck

> HealthCheck200Response healthCheck(authorization, opts)

health check

Use this endpoint to check the operational status of the messaging service. A 200 OK response means the service is up. If you receive a 504 response, the service is temporarily down. Check the [API Live Status page] (https://dev.telstra.com/api/status) to see if there&#39;s an active incident.

### Example

```javascript
import MessagingApiV3X from 'messaging_api_v3_x';
let defaultClient = MessagingApiV3X.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MessagingApiV3X.HealthCheckApi();
let authorization = "Bearer <access_token>"; // String | 
let opts = {
  'telstraApiVersion': "3.1.0" // String | 
};
apiInstance.healthCheck(authorization, opts, (error, data, response) => {
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
 **authorization** | **String**|  | 
 **telstraApiVersion** | **String**|  | [optional] 

### Return type

[**HealthCheck200Response**](HealthCheck200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

