# AzureSqlDatabase.TransparentDataEncryptionApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transparentDataEncryptionActivitiesListByConfiguration**](TransparentDataEncryptionApi.md#transparentDataEncryptionActivitiesListByConfiguration) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/transparentDataEncryption/{transparentDataEncryptionName}/operationResults | 
[**transparentDataEncryptionsCreateOrUpdate**](TransparentDataEncryptionApi.md#transparentDataEncryptionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/transparentDataEncryption/{transparentDataEncryptionName} | 
[**transparentDataEncryptionsGet**](TransparentDataEncryptionApi.md#transparentDataEncryptionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/transparentDataEncryption/{transparentDataEncryptionName} | 



## transparentDataEncryptionActivitiesListByConfiguration

> TransparentDataEncryptionActivityListResult transparentDataEncryptionActivitiesListByConfiguration(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, transparentDataEncryptionName)



Returns a database&#39;s transparent data encryption operation result.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.TransparentDataEncryptionApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database for which the transparent data encryption applies.
let transparentDataEncryptionName = "transparentDataEncryptionName_example"; // String | The name of the transparent data encryption configuration.
apiInstance.transparentDataEncryptionActivitiesListByConfiguration(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, transparentDataEncryptionName, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database for which the transparent data encryption applies. | 
 **transparentDataEncryptionName** | **String**| The name of the transparent data encryption configuration. | 

### Return type

[**TransparentDataEncryptionActivityListResult**](TransparentDataEncryptionActivityListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transparentDataEncryptionsCreateOrUpdate

> TransparentDataEncryption transparentDataEncryptionsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, transparentDataEncryptionName, parameters)



Creates or updates a database&#39;s transparent data encryption configuration.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.TransparentDataEncryptionApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database for which setting the transparent data encryption applies.
let transparentDataEncryptionName = "transparentDataEncryptionName_example"; // String | The name of the transparent data encryption configuration.
let parameters = new AzureSqlDatabase.TransparentDataEncryption(); // TransparentDataEncryption | The required parameters for creating or updating transparent data encryption.
apiInstance.transparentDataEncryptionsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, transparentDataEncryptionName, parameters, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database for which setting the transparent data encryption applies. | 
 **transparentDataEncryptionName** | **String**| The name of the transparent data encryption configuration. | 
 **parameters** | [**TransparentDataEncryption**](TransparentDataEncryption.md)| The required parameters for creating or updating transparent data encryption. | 

### Return type

[**TransparentDataEncryption**](TransparentDataEncryption.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## transparentDataEncryptionsGet

> TransparentDataEncryption transparentDataEncryptionsGet(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, transparentDataEncryptionName)



Gets a database&#39;s transparent data encryption configuration.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.TransparentDataEncryptionApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database for which the transparent data encryption applies.
let transparentDataEncryptionName = "transparentDataEncryptionName_example"; // String | The name of the transparent data encryption configuration.
apiInstance.transparentDataEncryptionsGet(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, transparentDataEncryptionName, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database for which the transparent data encryption applies. | 
 **transparentDataEncryptionName** | **String**| The name of the transparent data encryption configuration. | 

### Return type

[**TransparentDataEncryption**](TransparentDataEncryption.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

