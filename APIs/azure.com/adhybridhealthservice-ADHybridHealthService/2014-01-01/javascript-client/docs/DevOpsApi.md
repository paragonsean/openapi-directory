# AdHybridHealthService.DevOpsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reportsGetDevOps**](DevOpsApi.md#reportsGetDevOps) | **GET** /providers/Microsoft.ADHybridHealthService/reports/DevOps/IsDevOps | 



## reportsGetDevOps

> Result reportsGetDevOps(apiVersion)



Checks if the user is enabled for Dev Ops access.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.DevOpsApi();
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.reportsGetDevOps(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**Result**](Result.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

