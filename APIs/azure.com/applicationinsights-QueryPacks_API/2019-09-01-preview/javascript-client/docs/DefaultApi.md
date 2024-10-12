# AzureLogAnalyticsQueryPacks.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queryPacksCreateOrUpdate**](DefaultApi.md#queryPacksCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks/{queryPackName} | 
[**queryPacksDelete**](DefaultApi.md#queryPacksDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks/{queryPackName} | 
[**queryPacksGet**](DefaultApi.md#queryPacksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks/{queryPackName} | 
[**queryPacksList**](DefaultApi.md#queryPacksList) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/queryPacks | 
[**queryPacksListByResourceGroup**](DefaultApi.md#queryPacksListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks | 
[**queryPacksUpdateTags**](DefaultApi.md#queryPacksUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks/{queryPackName} | 



## queryPacksCreateOrUpdate

> LogAnalyticsQueryPack queryPacksCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, queryPackName, logAnalyticsQueryPackPayload)



Creates (or updates) a Log Analytics QueryPack. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation.

### Example

```javascript
import AzureLogAnalyticsQueryPacks from 'azure_log_analytics_query_packs';
let defaultClient = AzureLogAnalyticsQueryPacks.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalyticsQueryPacks.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let queryPackName = "queryPackName_example"; // String | The name of the Log Analytics QueryPack resource.
let logAnalyticsQueryPackPayload = new AzureLogAnalyticsQueryPacks.LogAnalyticsQueryPack(); // LogAnalyticsQueryPack | Properties that need to be specified to create or update a Log Analytics QueryPack.
apiInstance.queryPacksCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, queryPackName, logAnalyticsQueryPackPayload, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **queryPackName** | **String**| The name of the Log Analytics QueryPack resource. | 
 **logAnalyticsQueryPackPayload** | [**LogAnalyticsQueryPack**](LogAnalyticsQueryPack.md)| Properties that need to be specified to create or update a Log Analytics QueryPack. | 

### Return type

[**LogAnalyticsQueryPack**](LogAnalyticsQueryPack.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryPacksDelete

> queryPacksDelete(resourceGroupName, apiVersion, subscriptionId, queryPackName)



Deletes a Log Analytics QueryPack.

### Example

```javascript
import AzureLogAnalyticsQueryPacks from 'azure_log_analytics_query_packs';
let defaultClient = AzureLogAnalyticsQueryPacks.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalyticsQueryPacks.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let queryPackName = "queryPackName_example"; // String | The name of the Log Analytics QueryPack resource.
apiInstance.queryPacksDelete(resourceGroupName, apiVersion, subscriptionId, queryPackName, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **queryPackName** | **String**| The name of the Log Analytics QueryPack resource. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryPacksGet

> LogAnalyticsQueryPack queryPacksGet(resourceGroupName, apiVersion, subscriptionId, queryPackName)



Returns a Log Analytics QueryPack.

### Example

```javascript
import AzureLogAnalyticsQueryPacks from 'azure_log_analytics_query_packs';
let defaultClient = AzureLogAnalyticsQueryPacks.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalyticsQueryPacks.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let queryPackName = "queryPackName_example"; // String | The name of the Log Analytics QueryPack resource.
apiInstance.queryPacksGet(resourceGroupName, apiVersion, subscriptionId, queryPackName, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **queryPackName** | **String**| The name of the Log Analytics QueryPack resource. | 

### Return type

[**LogAnalyticsQueryPack**](LogAnalyticsQueryPack.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryPacksList

> LogAnalyticsQueryPackListResult queryPacksList(apiVersion, subscriptionId)



Gets a list of all Log Analytics QueryPacks within a subscription.

### Example

```javascript
import AzureLogAnalyticsQueryPacks from 'azure_log_analytics_query_packs';
let defaultClient = AzureLogAnalyticsQueryPacks.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalyticsQueryPacks.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.queryPacksList(apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**LogAnalyticsQueryPackListResult**](LogAnalyticsQueryPackListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryPacksListByResourceGroup

> LogAnalyticsQueryPackListResult queryPacksListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets a list of Log Analytics QueryPacks within a resource group.

### Example

```javascript
import AzureLogAnalyticsQueryPacks from 'azure_log_analytics_query_packs';
let defaultClient = AzureLogAnalyticsQueryPacks.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalyticsQueryPacks.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.queryPacksListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**LogAnalyticsQueryPackListResult**](LogAnalyticsQueryPackListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryPacksUpdateTags

> LogAnalyticsQueryPack queryPacksUpdateTags(resourceGroupName, apiVersion, subscriptionId, queryPackName, queryPackTags)



Updates an existing QueryPack&#39;s tags. To update other fields use the CreateOrUpdate method.

### Example

```javascript
import AzureLogAnalyticsQueryPacks from 'azure_log_analytics_query_packs';
let defaultClient = AzureLogAnalyticsQueryPacks.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalyticsQueryPacks.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let queryPackName = "queryPackName_example"; // String | The name of the Log Analytics QueryPack resource.
let queryPackTags = new AzureLogAnalyticsQueryPacks.TagsResource(); // TagsResource | Updated tag information to set into the QueryPack instance.
apiInstance.queryPacksUpdateTags(resourceGroupName, apiVersion, subscriptionId, queryPackName, queryPackTags, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **queryPackName** | **String**| The name of the Log Analytics QueryPack resource. | 
 **queryPackTags** | [**TagsResource**](TagsResource.md)| Updated tag information to set into the QueryPack instance. | 

### Return type

[**LogAnalyticsQueryPack**](LogAnalyticsQueryPack.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

