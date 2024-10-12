# NetworkManagementClient.ApplicationGatewaysApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationGatewaysBackendHealth**](ApplicationGatewaysApi.md#applicationGatewaysBackendHealth) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName}/backendhealth | 
[**applicationGatewaysCreateOrUpdate**](ApplicationGatewaysApi.md#applicationGatewaysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName} | 
[**applicationGatewaysDelete**](ApplicationGatewaysApi.md#applicationGatewaysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName} | 
[**applicationGatewaysGet**](ApplicationGatewaysApi.md#applicationGatewaysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName} | 
[**applicationGatewaysList**](ApplicationGatewaysApi.md#applicationGatewaysList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways | 
[**applicationGatewaysListAll**](ApplicationGatewaysApi.md#applicationGatewaysListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/applicationGateways | 
[**applicationGatewaysStart**](ApplicationGatewaysApi.md#applicationGatewaysStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName}/start | 
[**applicationGatewaysStop**](ApplicationGatewaysApi.md#applicationGatewaysStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName}/stop | 



## applicationGatewaysBackendHealth

> ApplicationGatewayBackendHealth applicationGatewaysBackendHealth(resourceGroupName, applicationGatewayName, apiVersion, subscriptionId, opts)



Gets the backend health of the specified application gateway in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'expand': "expand_example" // String | Expands BackendAddressPool and BackendHttpSettings referenced in backend health.
};
apiInstance.applicationGatewaysBackendHealth(resourceGroupName, applicationGatewayName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **applicationGatewayName** | **String**| The name of the application gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **expand** | **String**| Expands BackendAddressPool and BackendHttpSettings referenced in backend health. | [optional] 

### Return type

[**ApplicationGatewayBackendHealth**](ApplicationGatewayBackendHealth.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## applicationGatewaysCreateOrUpdate

> ApplicationGateway applicationGatewaysCreateOrUpdate(resourceGroupName, applicationGatewayName, apiVersion, subscriptionId, parameters)



Creates or updates the specified application gateway.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new NetworkManagementClient.ApplicationGateway(); // ApplicationGateway | Parameters supplied to the create or update application gateway operation.
apiInstance.applicationGatewaysCreateOrUpdate(resourceGroupName, applicationGatewayName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **applicationGatewayName** | **String**| The name of the application gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ApplicationGateway**](ApplicationGateway.md)| Parameters supplied to the create or update application gateway operation. | 

### Return type

[**ApplicationGateway**](ApplicationGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## applicationGatewaysDelete

> applicationGatewaysDelete(resourceGroupName, applicationGatewayName, apiVersion, subscriptionId)



Deletes the specified application gateway.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.applicationGatewaysDelete(resourceGroupName, applicationGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **applicationGatewayName** | **String**| The name of the application gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## applicationGatewaysGet

> ApplicationGateway applicationGatewaysGet(resourceGroupName, applicationGatewayName, apiVersion, subscriptionId)



Gets the specified application gateway.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.applicationGatewaysGet(resourceGroupName, applicationGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **applicationGatewayName** | **String**| The name of the application gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ApplicationGateway**](ApplicationGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## applicationGatewaysList

> ApplicationGatewayListResult applicationGatewaysList(resourceGroupName, apiVersion, subscriptionId)



Lists all application gateways in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.applicationGatewaysList(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ApplicationGatewayListResult**](ApplicationGatewayListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## applicationGatewaysListAll

> ApplicationGatewayListResult applicationGatewaysListAll(apiVersion, subscriptionId)



Gets all the application gateways in a subscription.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.applicationGatewaysListAll(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ApplicationGatewayListResult**](ApplicationGatewayListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## applicationGatewaysStart

> applicationGatewaysStart(resourceGroupName, applicationGatewayName, apiVersion, subscriptionId)



Starts the specified application gateway.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.applicationGatewaysStart(resourceGroupName, applicationGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **applicationGatewayName** | **String**| The name of the application gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## applicationGatewaysStop

> applicationGatewaysStop(resourceGroupName, applicationGatewayName, apiVersion, subscriptionId)



Stops the specified application gateway in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.applicationGatewaysStop(resourceGroupName, applicationGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **applicationGatewayName** | **String**| The name of the application gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

