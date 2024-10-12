# AdHybridHealthService.AlertsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serviceMembersListAlerts**](AlertsApi.md#serviceMembersListAlerts) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId}/alerts | 
[**servicesListAlerts**](AlertsApi.md#servicesListAlerts) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/alerts | 



## serviceMembersListAlerts

> Alerts serviceMembersListAlerts(serviceMemberId, serviceName, apiVersion, opts)



Gets the details of an alert for a given service and server combination.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AlertsApi();
let serviceMemberId = "serviceMemberId_example"; // String | The server Id for which the alert details needs to be queried.
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The alert property filter to apply.
  'state': "state_example", // String | The alert state to query for.
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | The start date to query for.
  'to': new Date("2013-10-20T19:20:30+01:00") // Date | The end date till when to query for.
};
apiInstance.serviceMembersListAlerts(serviceMemberId, serviceName, apiVersion, opts, (error, data, response) => {
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
 **serviceMemberId** | **String**| The server Id for which the alert details needs to be queried. | 
 **serviceName** | **String**| The name of the service. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **filter** | **String**| The alert property filter to apply. | [optional] 
 **state** | **String**| The alert state to query for. | [optional] 
 **from** | **Date**| The start date to query for. | [optional] 
 **to** | **Date**| The end date till when to query for. | [optional] 

### Return type

[**Alerts**](Alerts.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesListAlerts

> Alerts servicesListAlerts(serviceName, apiVersion, opts)



Gets the alerts for a given service.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AlertsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The alert property filter to apply.
  'state': "state_example", // String | The alert state to query for.
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | The start date to query for.
  'to': new Date("2013-10-20T19:20:30+01:00") // Date | The end date till when to query for.
};
apiInstance.servicesListAlerts(serviceName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| The alert property filter to apply. | [optional] 
 **state** | **String**| The alert state to query for. | [optional] 
 **from** | **Date**| The start date to query for. | [optional] 
 **to** | **Date**| The end date till when to query for. | [optional] 

### Return type

[**Alerts**](Alerts.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

