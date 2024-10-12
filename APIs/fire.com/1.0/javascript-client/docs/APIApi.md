# FireFinancialServicesBusinessApi.APIApi

All URIs are relative to *https://api.fire.com/business*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createApiApplication**](APIApi.md#createApiApplication) | **POST** /v1/apps | Create a new API Application



## createApiApplication

> ApiApplication createApiApplication(newApiApplication)

Create a new API Application

Create a new API Application with specified permissions

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.APIApi();
let newApiApplication = new FireFinancialServicesBusinessApi.NewApiApplication(); // NewApiApplication | Details of the new API Application
apiInstance.createApiApplication(newApiApplication, (error, data, response) => {
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
 **newApiApplication** | [**NewApiApplication**](NewApiApplication.md)| Details of the new API Application | 

### Return type

[**ApiApplication**](ApiApplication.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

