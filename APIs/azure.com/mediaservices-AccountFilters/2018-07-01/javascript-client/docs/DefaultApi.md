# AzureMediaServices.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountFiltersCreateOrUpdate**](DefaultApi.md#accountFiltersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/accountFilters/{filterName} | Create or update an Account Filter
[**accountFiltersDelete**](DefaultApi.md#accountFiltersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/accountFilters/{filterName} | Delete an Account Filter.
[**accountFiltersGet**](DefaultApi.md#accountFiltersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/accountFilters/{filterName} | Get an Account Filter.
[**accountFiltersList**](DefaultApi.md#accountFiltersList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/accountFilters | List Account Filters
[**accountFiltersUpdate**](DefaultApi.md#accountFiltersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/accountFilters/{filterName} | Update an Account Filter



## accountFiltersCreateOrUpdate

> AccountFilter accountFiltersCreateOrUpdate(subscriptionId, resourceGroupName, accountName, filterName, apiVersion, parameters)

Create or update an Account Filter

Creates or updates an Account Filter in the Media Services account.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let filterName = "filterName_example"; // String | The Account Filter name
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.AccountFilter(); // AccountFilter | The request parameters
apiInstance.accountFiltersCreateOrUpdate(subscriptionId, resourceGroupName, accountName, filterName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **filterName** | **String**| The Account Filter name | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**AccountFilter**](AccountFilter.md)| The request parameters | 

### Return type

[**AccountFilter**](AccountFilter.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountFiltersDelete

> accountFiltersDelete(subscriptionId, resourceGroupName, accountName, filterName, apiVersion)

Delete an Account Filter.

Deletes an Account Filter in the Media Services account.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let filterName = "filterName_example"; // String | The Account Filter name
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.accountFiltersDelete(subscriptionId, resourceGroupName, accountName, filterName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **filterName** | **String**| The Account Filter name | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountFiltersGet

> AccountFilter accountFiltersGet(subscriptionId, resourceGroupName, accountName, filterName, apiVersion)

Get an Account Filter.

Get the details of an Account Filter in the Media Services account.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let filterName = "filterName_example"; // String | The Account Filter name
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.accountFiltersGet(subscriptionId, resourceGroupName, accountName, filterName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **filterName** | **String**| The Account Filter name | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**AccountFilter**](AccountFilter.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountFiltersList

> AccountFilterCollection accountFiltersList(subscriptionId, resourceGroupName, accountName, apiVersion)

List Account Filters

List Account Filters in the Media Services account.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.accountFiltersList(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**AccountFilterCollection**](AccountFilterCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountFiltersUpdate

> AccountFilter accountFiltersUpdate(subscriptionId, resourceGroupName, accountName, filterName, apiVersion, parameters)

Update an Account Filter

Updates an existing Account Filter in the Media Services account.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let filterName = "filterName_example"; // String | The Account Filter name
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.AccountFilter(); // AccountFilter | The request parameters
apiInstance.accountFiltersUpdate(subscriptionId, resourceGroupName, accountName, filterName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **filterName** | **String**| The Account Filter name | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**AccountFilter**](AccountFilter.md)| The request parameters | 

### Return type

[**AccountFilter**](AccountFilter.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

