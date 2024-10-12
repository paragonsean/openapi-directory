# AzureSqlDatabase.ServerCommunicationLinksApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serverCommunicationLinksCreateOrUpdate**](ServerCommunicationLinksApi.md#serverCommunicationLinksCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/communicationLinks/{communicationLinkName} | 
[**serverCommunicationLinksDelete**](ServerCommunicationLinksApi.md#serverCommunicationLinksDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/communicationLinks/{communicationLinkName} | 
[**serverCommunicationLinksGet**](ServerCommunicationLinksApi.md#serverCommunicationLinksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/communicationLinks/{communicationLinkName} | 
[**serverCommunicationLinksListByServer**](ServerCommunicationLinksApi.md#serverCommunicationLinksListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/communicationLinks | 



## serverCommunicationLinksCreateOrUpdate

> ServerCommunicationLink serverCommunicationLinksCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, communicationLinkName, parameters)



Creates a server communication link.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.ServerCommunicationLinksApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let communicationLinkName = "communicationLinkName_example"; // String | The name of the server communication link.
let parameters = new AzureSqlDatabase.ServerCommunicationLink(); // ServerCommunicationLink | The required parameters for creating a server communication link.
apiInstance.serverCommunicationLinksCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, communicationLinkName, parameters, (error, data, response) => {
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
 **communicationLinkName** | **String**| The name of the server communication link. | 
 **parameters** | [**ServerCommunicationLink**](ServerCommunicationLink.md)| The required parameters for creating a server communication link. | 

### Return type

[**ServerCommunicationLink**](ServerCommunicationLink.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serverCommunicationLinksDelete

> serverCommunicationLinksDelete(apiVersion, subscriptionId, resourceGroupName, serverName, communicationLinkName)



Deletes a server communication link.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.ServerCommunicationLinksApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let communicationLinkName = "communicationLinkName_example"; // String | The name of the server communication link.
apiInstance.serverCommunicationLinksDelete(apiVersion, subscriptionId, resourceGroupName, serverName, communicationLinkName, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **communicationLinkName** | **String**| The name of the server communication link. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## serverCommunicationLinksGet

> ServerCommunicationLink serverCommunicationLinksGet(apiVersion, subscriptionId, resourceGroupName, serverName, communicationLinkName)



Returns a server communication link.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.ServerCommunicationLinksApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let communicationLinkName = "communicationLinkName_example"; // String | The name of the server communication link.
apiInstance.serverCommunicationLinksGet(apiVersion, subscriptionId, resourceGroupName, serverName, communicationLinkName, (error, data, response) => {
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
 **communicationLinkName** | **String**| The name of the server communication link. | 

### Return type

[**ServerCommunicationLink**](ServerCommunicationLink.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serverCommunicationLinksListByServer

> ServerCommunicationLinkListResult serverCommunicationLinksListByServer(apiVersion, subscriptionId, resourceGroupName, serverName)



Gets a list of server communication links.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.ServerCommunicationLinksApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
apiInstance.serverCommunicationLinksListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, (error, data, response) => {
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

[**ServerCommunicationLinkListResult**](ServerCommunicationLinkListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

