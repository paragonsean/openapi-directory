# AdHybridHealthService.ReportsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicesListAllRiskyIpDownloadReport**](ReportsApi.md#servicesListAllRiskyIpDownloadReport) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/reports/riskyIp/blobUris | 
[**servicesListCurrentRiskyIpDownloadReport**](ReportsApi.md#servicesListCurrentRiskyIpDownloadReport) | **POST** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/reports/riskyIp/generateBlobUri | 
[**servicesListUserBadPasswordReport**](ReportsApi.md#servicesListUserBadPasswordReport) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/reports/badpassword/details/user | 



## servicesListAllRiskyIpDownloadReport

> RiskyIPBlobUris servicesListAllRiskyIpDownloadReport(serviceName, apiVersion)



Gets all Risky IP report URIs for the last 7 days.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ReportsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.servicesListAllRiskyIpDownloadReport(serviceName, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**RiskyIPBlobUris**](RiskyIPBlobUris.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesListCurrentRiskyIpDownloadReport

> RiskyIPBlobUris servicesListCurrentRiskyIpDownloadReport(serviceName, apiVersion)



Initiate the generation of a new Risky IP report. Returns the URI for the new one.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ReportsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.servicesListCurrentRiskyIpDownloadReport(serviceName, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**RiskyIPBlobUris**](RiskyIPBlobUris.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesListUserBadPasswordReport

> ErrorReportUsersEntries servicesListUserBadPasswordReport(serviceName, apiVersion, opts)



Gets the bad password login attempt report for an user

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ReportsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'dataSource': "dataSource_example" // String | The source of data, if its test data or customer data.
};
apiInstance.servicesListUserBadPasswordReport(serviceName, apiVersion, opts, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **dataSource** | **String**| The source of data, if its test data or customer data. | [optional] 

### Return type

[**ErrorReportUsersEntries**](ErrorReportUsersEntries.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

