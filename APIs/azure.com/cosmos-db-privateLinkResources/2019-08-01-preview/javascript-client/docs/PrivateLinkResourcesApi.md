# CosmosDb.PrivateLinkResourcesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateLinkResourcesGet**](PrivateLinkResourcesApi.md#privateLinkResourcesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/privateLinkResources/{groupName} | 
[**privateLinkResourcesListByDatabaseAccount**](PrivateLinkResourcesApi.md#privateLinkResourcesListByDatabaseAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/privateLinkResources | 



## privateLinkResourcesGet

> PrivateLinkResource privateLinkResourcesGet(subscriptionId, resourceGroupName, apiVersion, accountName, groupName)



Gets the private link resources that need to be created for a Cosmos DB account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.PrivateLinkResourcesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let groupName = "groupName_example"; // String | The name of the private link resource.
apiInstance.privateLinkResourcesGet(subscriptionId, resourceGroupName, apiVersion, accountName, groupName, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **accountName** | **String**| Cosmos DB database account name. | 
 **groupName** | **String**| The name of the private link resource. | 

### Return type

[**PrivateLinkResource**](PrivateLinkResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateLinkResourcesListByDatabaseAccount

> PrivateLinkResourceListResult privateLinkResourcesListByDatabaseAccount(subscriptionId, resourceGroupName, apiVersion, accountName)



Gets the private link resources that need to be created for a Cosmos DB account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.PrivateLinkResourcesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure resource group.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-08-01.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
apiInstance.privateLinkResourcesListByDatabaseAccount(subscriptionId, resourceGroupName, apiVersion, accountName, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID. | 
 **resourceGroupName** | **String**| Name of an Azure resource group. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-08-01. | 
 **accountName** | **String**| Cosmos DB database account name. | 

### Return type

[**PrivateLinkResourceListResult**](PrivateLinkResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

