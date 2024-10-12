# AzureLogAnalyticsQueryPacks.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queriesDelete**](DefaultApi.md#queriesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks/{queryPackName}/queries/{queryId} | 
[**queriesGet**](DefaultApi.md#queriesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks/{queryPackName}/queries/{queryId} | 
[**queriesList**](DefaultApi.md#queriesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks/{queryPackName}/queries | 
[**queriesPut**](DefaultApi.md#queriesPut) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks/{queryPackName}/queries/{queryId} | 
[**queriesSearch**](DefaultApi.md#queriesSearch) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/queryPacks/{queryPackName}/queries/search | 



## queriesDelete

> queriesDelete(subscriptionId, resourceGroupName, queryPackName, queryId, apiVersion)



Deletes a specific Query defined within an Log Analytics QueryPack.

### Example

```javascript
import AzureLogAnalyticsQueryPacks from 'azure_log_analytics_query_packs';
let defaultClient = AzureLogAnalyticsQueryPacks.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalyticsQueryPacks.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let queryPackName = "queryPackName_example"; // String | The name of the Log Analytics QueryPack resource.
let queryId = "queryId_example"; // String | The id of a specific query defined in the Log Analytics QueryPack
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.queriesDelete(subscriptionId, resourceGroupName, queryPackName, queryId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **queryPackName** | **String**| The name of the Log Analytics QueryPack resource. | 
 **queryId** | **String**| The id of a specific query defined in the Log Analytics QueryPack | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queriesGet

> LogAnalyticsQueryPackQuery queriesGet(subscriptionId, resourceGroupName, queryPackName, queryId, apiVersion)



Gets a specific Log Analytics Query defined within a Log Analytics QueryPack.

### Example

```javascript
import AzureLogAnalyticsQueryPacks from 'azure_log_analytics_query_packs';
let defaultClient = AzureLogAnalyticsQueryPacks.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalyticsQueryPacks.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let queryPackName = "queryPackName_example"; // String | The name of the Log Analytics QueryPack resource.
let queryId = "queryId_example"; // String | The id of a specific query defined in the Log Analytics QueryPack
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.queriesGet(subscriptionId, resourceGroupName, queryPackName, queryId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **queryPackName** | **String**| The name of the Log Analytics QueryPack resource. | 
 **queryId** | **String**| The id of a specific query defined in the Log Analytics QueryPack | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**LogAnalyticsQueryPackQuery**](LogAnalyticsQueryPackQuery.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queriesList

> LogAnalyticsQueryPackQueryListResult queriesList(subscriptionId, resourceGroupName, queryPackName, apiVersion, opts)



Gets a list of Queries defined within a Log Analytics QueryPack.

### Example

```javascript
import AzureLogAnalyticsQueryPacks from 'azure_log_analytics_query_packs';
let defaultClient = AzureLogAnalyticsQueryPacks.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalyticsQueryPacks.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let queryPackName = "queryPackName_example"; // String | The name of the Log Analytics QueryPack resource.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'top': 56, // Number | Maximum items returned in page.
  'includeBody': true, // Boolean | Flag indicating whether or not to return the body of each applicable query. If false, only return the query information.
  'skipToken': "skipToken_example" // String | Base64 encoded token used to fetch the next page of items. Default is null.
};
apiInstance.queriesList(subscriptionId, resourceGroupName, queryPackName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **queryPackName** | **String**| The name of the Log Analytics QueryPack resource. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **top** | **Number**| Maximum items returned in page. | [optional] 
 **includeBody** | **Boolean**| Flag indicating whether or not to return the body of each applicable query. If false, only return the query information. | [optional] 
 **skipToken** | **String**| Base64 encoded token used to fetch the next page of items. Default is null. | [optional] 

### Return type

[**LogAnalyticsQueryPackQueryListResult**](LogAnalyticsQueryPackQueryListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queriesPut

> LogAnalyticsQueryPackQuery queriesPut(subscriptionId, resourceGroupName, queryPackName, queryId, apiVersion, queryPayload)



Adds or Updates a specific Query within a Log Analytics QueryPack.

### Example

```javascript
import AzureLogAnalyticsQueryPacks from 'azure_log_analytics_query_packs';
let defaultClient = AzureLogAnalyticsQueryPacks.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalyticsQueryPacks.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let queryPackName = "queryPackName_example"; // String | The name of the Log Analytics QueryPack resource.
let queryId = "queryId_example"; // String | The id of a specific query defined in the Log Analytics QueryPack
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let queryPayload = new AzureLogAnalyticsQueryPacks.LogAnalyticsQueryPackQuery(); // LogAnalyticsQueryPackQuery | Properties that need to be specified to create a new query and add it to a Log Analytics QueryPack.
apiInstance.queriesPut(subscriptionId, resourceGroupName, queryPackName, queryId, apiVersion, queryPayload, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **queryPackName** | **String**| The name of the Log Analytics QueryPack resource. | 
 **queryId** | **String**| The id of a specific query defined in the Log Analytics QueryPack | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **queryPayload** | [**LogAnalyticsQueryPackQuery**](LogAnalyticsQueryPackQuery.md)| Properties that need to be specified to create a new query and add it to a Log Analytics QueryPack. | 

### Return type

[**LogAnalyticsQueryPackQuery**](LogAnalyticsQueryPackQuery.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queriesSearch

> LogAnalyticsQueryPackQueryListResult queriesSearch(subscriptionId, resourceGroupName, queryPackName, apiVersion, querySearchProperties, opts)



Search a list of Queries defined within a Log Analytics QueryPack according to given search properties.

### Example

```javascript
import AzureLogAnalyticsQueryPacks from 'azure_log_analytics_query_packs';
let defaultClient = AzureLogAnalyticsQueryPacks.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureLogAnalyticsQueryPacks.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let queryPackName = "queryPackName_example"; // String | The name of the Log Analytics QueryPack resource.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let querySearchProperties = new AzureLogAnalyticsQueryPacks.LogAnalyticsQueryPackQuerySearchProperties(); // LogAnalyticsQueryPackQuerySearchProperties | Properties by which to search queries in the given Log Analytics QueryPack.
let opts = {
  'top': 56, // Number | Maximum items returned in page.
  'includeBody': true, // Boolean | Flag indicating whether or not to return the body of each applicable query. If false, only return the query information.
  'skipToken': "skipToken_example" // String | Base64 encoded token used to fetch the next page of items. Default is null.
};
apiInstance.queriesSearch(subscriptionId, resourceGroupName, queryPackName, apiVersion, querySearchProperties, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **queryPackName** | **String**| The name of the Log Analytics QueryPack resource. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **querySearchProperties** | [**LogAnalyticsQueryPackQuerySearchProperties**](LogAnalyticsQueryPackQuerySearchProperties.md)| Properties by which to search queries in the given Log Analytics QueryPack. | 
 **top** | **Number**| Maximum items returned in page. | [optional] 
 **includeBody** | **Boolean**| Flag indicating whether or not to return the body of each applicable query. If false, only return the query information. | [optional] 
 **skipToken** | **String**| Base64 encoded token used to fetch the next page of items. Default is null. | [optional] 

### Return type

[**LogAnalyticsQueryPackQueryListResult**](LogAnalyticsQueryPackQueryListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

