# AzureSqlDatabase.TransparentDataEncryptionApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transparentDataEncryptionConfigurationsListByDatabase**](TransparentDataEncryptionApi.md#transparentDataEncryptionConfigurationsListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/transparentDataEncryption | 



## transparentDataEncryptionConfigurationsListByDatabase

> TransparentDataEncryptionListResult transparentDataEncryptionConfigurationsListByDatabase(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName)



Gets a list of a database&#39;s transparent data encryption configurations. There is only ever one element, named &#39;current&#39;, so GetTransparentDataEncryptionConfiguration should be used instead.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.TransparentDataEncryptionApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database for which the transparent data encryption applies.
apiInstance.transparentDataEncryptionConfigurationsListByDatabase(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, (error, data, response) => {
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

### Return type

[**TransparentDataEncryptionListResult**](TransparentDataEncryptionListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

