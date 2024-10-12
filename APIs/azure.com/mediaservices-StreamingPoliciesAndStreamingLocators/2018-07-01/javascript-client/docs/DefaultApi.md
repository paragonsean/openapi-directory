# AzureMediaServices.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**streamingLocatorsCreate**](DefaultApi.md#streamingLocatorsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingLocators/{streamingLocatorName} | Create a Streaming Locator
[**streamingLocatorsDelete**](DefaultApi.md#streamingLocatorsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingLocators/{streamingLocatorName} | Delete a Streaming Locator
[**streamingLocatorsGet**](DefaultApi.md#streamingLocatorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingLocators/{streamingLocatorName} | Get a Streaming Locator
[**streamingLocatorsList**](DefaultApi.md#streamingLocatorsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingLocators | List Streaming Locators
[**streamingLocatorsListContentKeys**](DefaultApi.md#streamingLocatorsListContentKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingLocators/{streamingLocatorName}/listContentKeys | List Content Keys
[**streamingLocatorsListPaths**](DefaultApi.md#streamingLocatorsListPaths) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingLocators/{streamingLocatorName}/listPaths | List Paths
[**streamingPoliciesCreate**](DefaultApi.md#streamingPoliciesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingPolicies/{streamingPolicyName} | Create a Streaming Policy
[**streamingPoliciesDelete**](DefaultApi.md#streamingPoliciesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingPolicies/{streamingPolicyName} | Delete a Streaming Policy
[**streamingPoliciesGet**](DefaultApi.md#streamingPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingPolicies/{streamingPolicyName} | Get a Streaming Policy
[**streamingPoliciesList**](DefaultApi.md#streamingPoliciesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/streamingPolicies | List Streaming Policies



## streamingLocatorsCreate

> StreamingLocator streamingLocatorsCreate(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion, parameters)

Create a Streaming Locator

Create a Streaming Locator in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let streamingLocatorName = "streamingLocatorName_example"; // String | The Streaming Locator name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.StreamingLocator(); // StreamingLocator | The request parameters
apiInstance.streamingLocatorsCreate(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion, parameters, (error, data, response) => {
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
 **streamingLocatorName** | **String**| The Streaming Locator name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**StreamingLocator**](StreamingLocator.md)| The request parameters | 

### Return type

[**StreamingLocator**](StreamingLocator.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## streamingLocatorsDelete

> streamingLocatorsDelete(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion)

Delete a Streaming Locator

Deletes a Streaming Locator in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let streamingLocatorName = "streamingLocatorName_example"; // String | The Streaming Locator name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.streamingLocatorsDelete(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion, (error, data, response) => {
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
 **streamingLocatorName** | **String**| The Streaming Locator name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## streamingLocatorsGet

> StreamingLocator streamingLocatorsGet(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion)

Get a Streaming Locator

Get the details of a Streaming Locator in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let streamingLocatorName = "streamingLocatorName_example"; // String | The Streaming Locator name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.streamingLocatorsGet(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion, (error, data, response) => {
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
 **streamingLocatorName** | **String**| The Streaming Locator name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**StreamingLocator**](StreamingLocator.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## streamingLocatorsList

> StreamingLocatorCollection streamingLocatorsList(subscriptionId, resourceGroupName, accountName, apiVersion, opts)

List Streaming Locators

Lists the Streaming Locators in the account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | Restricts the set of items returned.
  'top': 56, // Number | Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
  'orderby': "orderby_example" // String | Specifies the key by which the result collection should be ordered.
};
apiInstance.streamingLocatorsList(subscriptionId, resourceGroupName, accountName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| Restricts the set of items returned. | [optional] 
 **top** | **Number**| Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n. | [optional] 
 **orderby** | **String**| Specifies the key by which the result collection should be ordered. | [optional] 

### Return type

[**StreamingLocatorCollection**](StreamingLocatorCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## streamingLocatorsListContentKeys

> ListContentKeysResponse streamingLocatorsListContentKeys(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion)

List Content Keys

List Content Keys used by this Streaming Locator

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let streamingLocatorName = "streamingLocatorName_example"; // String | The Streaming Locator name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.streamingLocatorsListContentKeys(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion, (error, data, response) => {
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
 **streamingLocatorName** | **String**| The Streaming Locator name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**ListContentKeysResponse**](ListContentKeysResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## streamingLocatorsListPaths

> ListPathsResponse streamingLocatorsListPaths(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion)

List Paths

List Paths supported by this Streaming Locator

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let streamingLocatorName = "streamingLocatorName_example"; // String | The Streaming Locator name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.streamingLocatorsListPaths(subscriptionId, resourceGroupName, accountName, streamingLocatorName, apiVersion, (error, data, response) => {
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
 **streamingLocatorName** | **String**| The Streaming Locator name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**ListPathsResponse**](ListPathsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## streamingPoliciesCreate

> StreamingPolicy streamingPoliciesCreate(subscriptionId, resourceGroupName, accountName, streamingPolicyName, apiVersion, parameters)

Create a Streaming Policy

Create a Streaming Policy in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let streamingPolicyName = "streamingPolicyName_example"; // String | The Streaming Policy name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.StreamingPolicy(); // StreamingPolicy | The request parameters
apiInstance.streamingPoliciesCreate(subscriptionId, resourceGroupName, accountName, streamingPolicyName, apiVersion, parameters, (error, data, response) => {
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
 **streamingPolicyName** | **String**| The Streaming Policy name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**StreamingPolicy**](StreamingPolicy.md)| The request parameters | 

### Return type

[**StreamingPolicy**](StreamingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## streamingPoliciesDelete

> streamingPoliciesDelete(subscriptionId, resourceGroupName, accountName, streamingPolicyName, apiVersion)

Delete a Streaming Policy

Deletes a Streaming Policy in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let streamingPolicyName = "streamingPolicyName_example"; // String | The Streaming Policy name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.streamingPoliciesDelete(subscriptionId, resourceGroupName, accountName, streamingPolicyName, apiVersion, (error, data, response) => {
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
 **streamingPolicyName** | **String**| The Streaming Policy name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## streamingPoliciesGet

> StreamingPolicy streamingPoliciesGet(subscriptionId, resourceGroupName, accountName, streamingPolicyName, apiVersion)

Get a Streaming Policy

Get the details of a Streaming Policy in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let streamingPolicyName = "streamingPolicyName_example"; // String | The Streaming Policy name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.streamingPoliciesGet(subscriptionId, resourceGroupName, accountName, streamingPolicyName, apiVersion, (error, data, response) => {
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
 **streamingPolicyName** | **String**| The Streaming Policy name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**StreamingPolicy**](StreamingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## streamingPoliciesList

> StreamingPolicyCollection streamingPoliciesList(subscriptionId, resourceGroupName, accountName, apiVersion, opts)

List Streaming Policies

Lists the Streaming Policies in the account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | Restricts the set of items returned.
  'top': 56, // Number | Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
  'orderby': "orderby_example" // String | Specifies the key by which the result collection should be ordered.
};
apiInstance.streamingPoliciesList(subscriptionId, resourceGroupName, accountName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| Restricts the set of items returned. | [optional] 
 **top** | **Number**| Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n. | [optional] 
 **orderby** | **String**| Specifies the key by which the result collection should be ordered. | [optional] 

### Return type

[**StreamingPolicyCollection**](StreamingPolicyCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

