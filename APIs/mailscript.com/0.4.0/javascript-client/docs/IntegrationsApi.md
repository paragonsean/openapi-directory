# Mailscript.IntegrationsApi

All URIs are relative to *https://api.mailscript.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteIntegration**](IntegrationsApi.md#deleteIntegration) | **DELETE** /integrations/{integration} | Delete an integration
[**getAllIntegrations**](IntegrationsApi.md#getAllIntegrations) | **GET** /integrations | Get all integrations for the user



## deleteIntegration

> deleteIntegration(integration)

Delete an integration

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.IntegrationsApi();
let integration = "integration_example"; // String | ID of the integration
apiInstance.deleteIntegration(integration, (error, data, response) => {
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
 **integration** | **String**| ID of the integration | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllIntegrations

> GetAllIntegrationsResponse getAllIntegrations()

Get all integrations for the user

### Example

```javascript
import Mailscript from 'mailscript';
let defaultClient = Mailscript.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Mailscript.IntegrationsApi();
apiInstance.getAllIntegrations((error, data, response) => {
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

[**GetAllIntegrationsResponse**](GetAllIntegrationsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

