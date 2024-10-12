# ApiManagementClient.OpenIdConnectProvidersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**openIdConnectProvidersCreateOrUpdate**](OpenIdConnectProvidersApi.md#openIdConnectProvidersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/openidConnectProviders/{opid} | 
[**openIdConnectProvidersDelete**](OpenIdConnectProvidersApi.md#openIdConnectProvidersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/openidConnectProviders/{opid} | 
[**openIdConnectProvidersGet**](OpenIdConnectProvidersApi.md#openIdConnectProvidersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/openidConnectProviders/{opid} | 
[**openIdConnectProvidersListByService**](OpenIdConnectProvidersApi.md#openIdConnectProvidersListByService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/openidConnectProviders | 
[**openIdConnectProvidersUpdate**](OpenIdConnectProvidersApi.md#openIdConnectProvidersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/openidConnectProviders/{opid} | 



## openIdConnectProvidersCreateOrUpdate

> openIdConnectProvidersCreateOrUpdate(resourceGroupName, serviceName, opid, apiVersion, subscriptionId, parameters)



Creates or updates the OpenID Connect Provider.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.OpenIdConnectProvidersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let opid = "opid_example"; // String | Identifier of the OpenID Connect Provider.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ApiManagementClient.OpenidConnectProviderCreateContract(); // OpenidConnectProviderCreateContract | Create parameters.
apiInstance.openIdConnectProvidersCreateOrUpdate(resourceGroupName, serviceName, opid, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **opid** | **String**| Identifier of the OpenID Connect Provider. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**OpenidConnectProviderCreateContract**](OpenidConnectProviderCreateContract.md)| Create parameters. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## openIdConnectProvidersDelete

> openIdConnectProvidersDelete(resourceGroupName, serviceName, opid, ifMatch, apiVersion, subscriptionId)



Deletes specific OpenID Connect Provider of the API Management service instance.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.OpenIdConnectProvidersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let opid = "opid_example"; // String | Identifier of the OpenID Connect Provider.
let ifMatch = "ifMatch_example"; // String | The entity state (Etag) version of the OpenID Connect Provider to delete. A value of \"*\" can be used for If-Match to unconditionally apply the operation.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.openIdConnectProvidersDelete(resourceGroupName, serviceName, opid, ifMatch, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **opid** | **String**| Identifier of the OpenID Connect Provider. | 
 **ifMatch** | **String**| The entity state (Etag) version of the OpenID Connect Provider to delete. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## openIdConnectProvidersGet

> OpenidConnectProviderContract openIdConnectProvidersGet(resourceGroupName, serviceName, opid, apiVersion, subscriptionId)



Gets specific OpenID Connect Provider.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.OpenIdConnectProvidersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let opid = "opid_example"; // String | Identifier of the OpenID Connect Provider.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.openIdConnectProvidersGet(resourceGroupName, serviceName, opid, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **opid** | **String**| Identifier of the OpenID Connect Provider. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**OpenidConnectProviderContract**](OpenidConnectProviderContract.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## openIdConnectProvidersListByService

> OpenIdConnectProviderCollection openIdConnectProvidersListByService(resourceGroupName, serviceName, apiVersion, subscriptionId, opts)



Lists all OpenID Connect Providers.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.OpenIdConnectProvidersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example", // String | | Field | Supported operators    | Supported functions                         | |-------|------------------------|---------------------------------------------| | id    | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |
  'top': 56, // Number | Number of records to return.
  'skip': 56 // Number | Number of records to skip.
};
apiInstance.openIdConnectProvidersListByService(resourceGroupName, serviceName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **filter** | **String**| | Field | Supported operators    | Supported functions                         | |-------|------------------------|---------------------------------------------| | id    | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | [optional] 
 **top** | **Number**| Number of records to return. | [optional] 
 **skip** | **Number**| Number of records to skip. | [optional] 

### Return type

[**OpenIdConnectProviderCollection**](OpenIdConnectProviderCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## openIdConnectProvidersUpdate

> openIdConnectProvidersUpdate(resourceGroupName, serviceName, opid, ifMatch, apiVersion, subscriptionId, parameters)



Updates the specific OpenID Connect Provider.

### Example

```javascript
import ApiManagementClient from 'api_management_client';
let defaultClient = ApiManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApiManagementClient.OpenIdConnectProvidersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let serviceName = "serviceName_example"; // String | The name of the API Management service.
let opid = "opid_example"; // String | Identifier of the OpenID Connect Provider.
let ifMatch = "ifMatch_example"; // String | The entity state (Etag) version of the OpenID Connect Provider to update. A value of \"*\" can be used for If-Match to unconditionally apply the operation.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ApiManagementClient.OpenidConnectProviderUpdateContract(); // OpenidConnectProviderUpdateContract | Update parameters.
apiInstance.openIdConnectProvidersUpdate(resourceGroupName, serviceName, opid, ifMatch, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **serviceName** | **String**| The name of the API Management service. | 
 **opid** | **String**| Identifier of the OpenID Connect Provider. | 
 **ifMatch** | **String**| The entity state (Etag) version of the OpenID Connect Provider to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**OpenidConnectProviderUpdateContract**](OpenidConnectProviderUpdateContract.md)| Update parameters. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

