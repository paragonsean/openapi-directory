# AdHybridHealthService.FeedbackApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicesAddAlertFeedback**](FeedbackApi.md#servicesAddAlertFeedback) | **POST** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/feedbacktype/alerts/feedback | 
[**servicesListAlertFeedback**](FeedbackApi.md#servicesListAlertFeedback) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/feedbacktype/alerts/{shortName}/alertfeedback | 



## servicesAddAlertFeedback

> AlertFeedback servicesAddAlertFeedback(serviceName, apiVersion, alertFeedback)



Adds an alert feedback submitted by customer.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.FeedbackApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let alertFeedback = new AdHybridHealthService.AlertFeedback(); // AlertFeedback | The alert feedback.
apiInstance.servicesAddAlertFeedback(serviceName, apiVersion, alertFeedback, (error, data, response) => {
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
 **alertFeedback** | [**AlertFeedback**](AlertFeedback.md)| The alert feedback. | 

### Return type

[**AlertFeedback**](AlertFeedback.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## servicesListAlertFeedback

> AlertFeedbacks servicesListAlertFeedback(serviceName, shortName, apiVersion)



Gets a list of all alert feedback for a given tenant and alert type.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.FeedbackApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let shortName = "shortName_example"; // String | The name of the alert.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.servicesListAlertFeedback(serviceName, shortName, apiVersion, (error, data, response) => {
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
 **shortName** | **String**| The name of the alert. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**AlertFeedbacks**](AlertFeedbacks.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

