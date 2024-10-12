# MariaDbManagementClient.AdvisorsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**advisorsGet**](AdvisorsApi.md#advisorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMariaDB/servers/{serverName}/advisors/{advisorName} | 
[**advisorsListByServer**](AdvisorsApi.md#advisorsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMariaDB/servers/{serverName}/advisors | 



## advisorsGet

> Advisor advisorsGet(apiVersion, subscriptionId, resourceGroupName, serverName, advisorName)



Get a recommendation action advisor.

### Example

```javascript
import MariaDbManagementClient from 'maria_db_management_client';
let defaultClient = MariaDbManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MariaDbManagementClient.AdvisorsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let serverName = "serverName_example"; // String | The name of the server.
let advisorName = "advisorName_example"; // String | The advisor name for recommendation action.
apiInstance.advisorsGet(apiVersion, subscriptionId, resourceGroupName, serverName, advisorName, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **serverName** | **String**| The name of the server. | 
 **advisorName** | **String**| The advisor name for recommendation action. | 

### Return type

[**Advisor**](Advisor.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## advisorsListByServer

> AdvisorsResultList advisorsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName)



List recommendation action advisors.

### Example

```javascript
import MariaDbManagementClient from 'maria_db_management_client';
let defaultClient = MariaDbManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MariaDbManagementClient.AdvisorsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let serverName = "serverName_example"; // String | The name of the server.
apiInstance.advisorsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **serverName** | **String**| The name of the server. | 

### Return type

[**AdvisorsResultList**](AdvisorsResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

