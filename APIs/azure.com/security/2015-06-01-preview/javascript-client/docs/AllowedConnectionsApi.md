# SecurityCenter.AllowedConnectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**allowedConnectionsGet**](AllowedConnectionsApi.md#allowedConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/allowedConnections/{connectionType} | 
[**allowedConnectionsList**](AllowedConnectionsApi.md#allowedConnectionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/allowedConnections | 
[**allowedConnectionsListByHomeRegion**](AllowedConnectionsApi.md#allowedConnectionsListByHomeRegion) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/allowedConnections | 



## allowedConnectionsGet

> AllowedConnectionsResource allowedConnectionsGet(subscriptionId, resourceGroupName, ascLocation, connectionType, apiVersion)



Gets the list of all possible traffic between resources for the subscription and location, based on connection type.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AllowedConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let connectionType = "connectionType_example"; // String | The type of allowed connections (Internal, External)
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.allowedConnectionsGet(subscriptionId, resourceGroupName, ascLocation, connectionType, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **connectionType** | **String**| The type of allowed connections (Internal, External) | 
 **apiVersion** | **String**| API version for the operation | 

### Return type

[**AllowedConnectionsResource**](AllowedConnectionsResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## allowedConnectionsList

> AllowedConnectionsList allowedConnectionsList(subscriptionId, apiVersion)



Gets the list of all possible traffic between resources for the subscription

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AllowedConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.allowedConnectionsList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **apiVersion** | **String**| API version for the operation | 

### Return type

[**AllowedConnectionsList**](AllowedConnectionsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## allowedConnectionsListByHomeRegion

> AllowedConnectionsList allowedConnectionsListByHomeRegion(subscriptionId, ascLocation, apiVersion)



Gets the list of all possible traffic between resources for the subscription and location.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.AllowedConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.allowedConnectionsListByHomeRegion(subscriptionId, ascLocation, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **apiVersion** | **String**| API version for the operation | 

### Return type

[**AllowedConnectionsList**](AllowedConnectionsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

