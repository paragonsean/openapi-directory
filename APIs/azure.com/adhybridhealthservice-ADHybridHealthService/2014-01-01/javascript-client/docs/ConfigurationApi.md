# AdHybridHealthService.ConfigurationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurationAdd**](ConfigurationApi.md#configurationAdd) | **POST** /providers/Microsoft.ADHybridHealthService/configuration | 
[**configurationGet**](ConfigurationApi.md#configurationGet) | **GET** /providers/Microsoft.ADHybridHealthService/configuration | 
[**configurationUpdate**](ConfigurationApi.md#configurationUpdate) | **PATCH** /providers/Microsoft.ADHybridHealthService/configuration | 



## configurationAdd

> Tenant configurationAdd(apiVersion)



Onboards a tenant in Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ConfigurationApi();
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.configurationAdd(apiVersion, (error, data, response) => {
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

[**Tenant**](Tenant.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## configurationGet

> Tenant configurationGet(apiVersion)



Gets the details of a tenant onboarded to Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ConfigurationApi();
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.configurationGet(apiVersion, (error, data, response) => {
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

[**Tenant**](Tenant.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## configurationUpdate

> Tenant configurationUpdate(apiVersion, tenant)



Updates tenant properties for tenants onboarded to Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.ConfigurationApi();
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let tenant = new AdHybridHealthService.Tenant(); // Tenant | The tenant object with the properties set to the updated value.
apiInstance.configurationUpdate(apiVersion, tenant, (error, data, response) => {
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
 **tenant** | [**Tenant**](Tenant.md)| The tenant object with the properties set to the updated value. | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

