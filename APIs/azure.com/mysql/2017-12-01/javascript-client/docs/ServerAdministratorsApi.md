# MySqlManagementClient.ServerAdministratorsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serverAdministratorsCreateOrUpdate**](ServerAdministratorsApi.md#serverAdministratorsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/Administrators/activeDirectory | 
[**serverAdministratorsDelete**](ServerAdministratorsApi.md#serverAdministratorsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/Administrators/activeDirectory | 
[**serverAdministratorsGet**](ServerAdministratorsApi.md#serverAdministratorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/Administrators/activeDirectory | 
[**serverAdministratorsListByServer**](ServerAdministratorsApi.md#serverAdministratorsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/administrators | 



## serverAdministratorsCreateOrUpdate

> ServerAdministratorResource serverAdministratorsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, properties)



Creates or update active directory administrator on an existing server. The update action will overwrite the existing administrator.

### Example

```javascript
import MySqlManagementClient from 'my_sql_management_client';
let defaultClient = MySqlManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MySqlManagementClient.ServerAdministratorsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let properties = new MySqlManagementClient.ServerAdministratorResource(); // ServerAdministratorResource | The required parameters for creating or updating an AAD server administrator.
apiInstance.serverAdministratorsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, properties, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **properties** | [**ServerAdministratorResource**](ServerAdministratorResource.md)| The required parameters for creating or updating an AAD server administrator. | 

### Return type

[**ServerAdministratorResource**](ServerAdministratorResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serverAdministratorsDelete

> ServerAdministratorResource serverAdministratorsDelete(apiVersion, subscriptionId, resourceGroupName, serverName)



Deletes AAD Administrator.

### Example

```javascript
import MySqlManagementClient from 'my_sql_management_client';
let defaultClient = MySqlManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MySqlManagementClient.ServerAdministratorsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
apiInstance.serverAdministratorsDelete(apiVersion, subscriptionId, resourceGroupName, serverName, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 

### Return type

[**ServerAdministratorResource**](ServerAdministratorResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serverAdministratorsGet

> ServerAdministratorResource serverAdministratorsGet(apiVersion, subscriptionId, resourceGroupName, serverName)



Gets information about a AAD server administrator.

### Example

```javascript
import MySqlManagementClient from 'my_sql_management_client';
let defaultClient = MySqlManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MySqlManagementClient.ServerAdministratorsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
apiInstance.serverAdministratorsGet(apiVersion, subscriptionId, resourceGroupName, serverName, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 

### Return type

[**ServerAdministratorResource**](ServerAdministratorResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serverAdministratorsListByServer

> ServerAdministratorResourceListResult serverAdministratorsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName)



Returns a list of server Administrators.

### Example

```javascript
import MySqlManagementClient from 'my_sql_management_client';
let defaultClient = MySqlManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MySqlManagementClient.ServerAdministratorsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
apiInstance.serverAdministratorsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 

### Return type

[**ServerAdministratorResourceListResult**](ServerAdministratorResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

