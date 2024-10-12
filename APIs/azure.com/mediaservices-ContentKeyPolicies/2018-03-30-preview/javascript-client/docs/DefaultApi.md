# AzureMediaServices.DefaultApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contentKeyPoliciesCreateOrUpdate**](DefaultApi.md#contentKeyPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName} | Create or update an Content Key Policy
[**contentKeyPoliciesDelete**](DefaultApi.md#contentKeyPoliciesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName} | Delete a Content Key Policy
[**contentKeyPoliciesGet**](DefaultApi.md#contentKeyPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName} | Get a Content Key Policy
[**contentKeyPoliciesGetPolicyPropertiesWithSecrets**](DefaultApi.md#contentKeyPoliciesGetPolicyPropertiesWithSecrets) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName}/getPolicyPropertiesWithSecrets | Get a Content Key Policy with secrets
[**contentKeyPoliciesList**](DefaultApi.md#contentKeyPoliciesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies | List Content Key Policies
[**contentKeyPoliciesUpdate**](DefaultApi.md#contentKeyPoliciesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/contentKeyPolicies/{contentKeyPolicyName} | Update a Content Key Policy



## contentKeyPoliciesCreateOrUpdate

> ContentKeyPolicy contentKeyPoliciesCreateOrUpdate(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion, parameters)

Create or update an Content Key Policy

Create or update a Content Key Policy in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let contentKeyPolicyName = "contentKeyPolicyName_example"; // String | The Content Key Policy name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.ContentKeyPolicy(); // ContentKeyPolicy | The request parameters
apiInstance.contentKeyPoliciesCreateOrUpdate(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion, parameters, (error, data, response) => {
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
 **contentKeyPolicyName** | **String**| The Content Key Policy name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**ContentKeyPolicy**](ContentKeyPolicy.md)| The request parameters | 

### Return type

[**ContentKeyPolicy**](ContentKeyPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## contentKeyPoliciesDelete

> contentKeyPoliciesDelete(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion)

Delete a Content Key Policy

Deletes a Content Key Policy in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let contentKeyPolicyName = "contentKeyPolicyName_example"; // String | The Content Key Policy name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.contentKeyPoliciesDelete(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion, (error, data, response) => {
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
 **contentKeyPolicyName** | **String**| The Content Key Policy name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contentKeyPoliciesGet

> ContentKeyPolicy contentKeyPoliciesGet(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion)

Get a Content Key Policy

Get the details of a Content Key Policy in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let contentKeyPolicyName = "contentKeyPolicyName_example"; // String | The Content Key Policy name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.contentKeyPoliciesGet(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion, (error, data, response) => {
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
 **contentKeyPolicyName** | **String**| The Content Key Policy name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**ContentKeyPolicy**](ContentKeyPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contentKeyPoliciesGetPolicyPropertiesWithSecrets

> ContentKeyPolicyProperties contentKeyPoliciesGetPolicyPropertiesWithSecrets(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion)

Get a Content Key Policy with secrets

Get a Content Key Policy including secret values

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let contentKeyPolicyName = "contentKeyPolicyName_example"; // String | The Content Key Policy name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.contentKeyPoliciesGetPolicyPropertiesWithSecrets(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion, (error, data, response) => {
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
 **contentKeyPolicyName** | **String**| The Content Key Policy name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**ContentKeyPolicyProperties**](ContentKeyPolicyProperties.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contentKeyPoliciesList

> ContentKeyPolicyCollection contentKeyPoliciesList(subscriptionId, resourceGroupName, accountName, apiVersion, opts)

List Content Key Policies

Lists the Content Key Policies in the account

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
apiInstance.contentKeyPoliciesList(subscriptionId, resourceGroupName, accountName, apiVersion, opts, (error, data, response) => {
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

[**ContentKeyPolicyCollection**](ContentKeyPolicyCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## contentKeyPoliciesUpdate

> ContentKeyPolicy contentKeyPoliciesUpdate(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion, parameters)

Update a Content Key Policy

Updates an existing Content Key Policy in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let contentKeyPolicyName = "contentKeyPolicyName_example"; // String | The Content Key Policy name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.ContentKeyPolicy(); // ContentKeyPolicy | The request parameters
apiInstance.contentKeyPoliciesUpdate(subscriptionId, resourceGroupName, accountName, contentKeyPolicyName, apiVersion, parameters, (error, data, response) => {
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
 **contentKeyPolicyName** | **String**| The Content Key Policy name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**ContentKeyPolicy**](ContentKeyPolicy.md)| The request parameters | 

### Return type

[**ContentKeyPolicy**](ContentKeyPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

