# AzureDigitalTwinsManagementClient.DigitalTwinsInstanceApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**digitalTwinsCreateOrUpdate**](DigitalTwinsInstanceApi.md#digitalTwinsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resourceName} | 
[**digitalTwinsDelete**](DigitalTwinsInstanceApi.md#digitalTwinsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resourceName} | 
[**digitalTwinsGet**](DigitalTwinsInstanceApi.md#digitalTwinsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resourceName} | 
[**digitalTwinsList**](DigitalTwinsInstanceApi.md#digitalTwinsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DigitalTwins/digitalTwinsInstances | 
[**digitalTwinsListByResourceGroup**](DigitalTwinsInstanceApi.md#digitalTwinsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances | 
[**digitalTwinsUpdate**](DigitalTwinsInstanceApi.md#digitalTwinsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DigitalTwins/digitalTwinsInstances/{resourceName} | 



## digitalTwinsCreateOrUpdate

> DigitalTwinsDescription digitalTwinsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, digitalTwinsCreate)



Create or update the metadata of a DigitalTwinsInstance. The usual pattern to modify a property is to retrieve the DigitalTwinsInstance and security metadata, and then combine them with the modified values in a new body to update the DigitalTwinsInstance.

### Example

```javascript
import AzureDigitalTwinsManagementClient from 'azure_digital_twins_management_client';
let defaultClient = AzureDigitalTwinsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDigitalTwinsManagementClient.DigitalTwinsInstanceApi();
let apiVersion = "apiVersion_example"; // String | Version of the DigitalTwinsInstance Management API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
let resourceName = "resourceName_example"; // String | The name of the DigitalTwinsInstance.
let digitalTwinsCreate = new AzureDigitalTwinsManagementClient.DigitalTwinsDescription(); // DigitalTwinsDescription | The DigitalTwinsInstance and security metadata.
apiInstance.digitalTwinsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, digitalTwinsCreate, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the DigitalTwinsInstance. | 
 **resourceName** | **String**| The name of the DigitalTwinsInstance. | 
 **digitalTwinsCreate** | [**DigitalTwinsDescription**](DigitalTwinsDescription.md)| The DigitalTwinsInstance and security metadata. | 

### Return type

[**DigitalTwinsDescription**](DigitalTwinsDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## digitalTwinsDelete

> digitalTwinsDelete(apiVersion, subscriptionId, resourceGroupName, resourceName)



Delete a DigitalTwinsInstance.

### Example

```javascript
import AzureDigitalTwinsManagementClient from 'azure_digital_twins_management_client';
let defaultClient = AzureDigitalTwinsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDigitalTwinsManagementClient.DigitalTwinsInstanceApi();
let apiVersion = "apiVersion_example"; // String | Version of the DigitalTwinsInstance Management API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
let resourceName = "resourceName_example"; // String | The name of the DigitalTwinsInstance.
apiInstance.digitalTwinsDelete(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the DigitalTwinsInstance. | 
 **resourceName** | **String**| The name of the DigitalTwinsInstance. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## digitalTwinsGet

> DigitalTwinsDescription digitalTwinsGet(apiVersion, subscriptionId, resourceGroupName, resourceName)



Get DigitalTwinsInstances resource.

### Example

```javascript
import AzureDigitalTwinsManagementClient from 'azure_digital_twins_management_client';
let defaultClient = AzureDigitalTwinsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDigitalTwinsManagementClient.DigitalTwinsInstanceApi();
let apiVersion = "apiVersion_example"; // String | Version of the DigitalTwinsInstance Management API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
let resourceName = "resourceName_example"; // String | The name of the DigitalTwinsInstance.
apiInstance.digitalTwinsGet(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the DigitalTwinsInstance. | 
 **resourceName** | **String**| The name of the DigitalTwinsInstance. | 

### Return type

[**DigitalTwinsDescription**](DigitalTwinsDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## digitalTwinsList

> DigitalTwinsDescriptionListResult digitalTwinsList(apiVersion, subscriptionId)



Get all the DigitalTwinsInstances in a subscription.

### Example

```javascript
import AzureDigitalTwinsManagementClient from 'azure_digital_twins_management_client';
let defaultClient = AzureDigitalTwinsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDigitalTwinsManagementClient.DigitalTwinsInstanceApi();
let apiVersion = "apiVersion_example"; // String | Version of the DigitalTwinsInstance Management API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
apiInstance.digitalTwinsList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | 
 **subscriptionId** | **String**| The subscription identifier. | 

### Return type

[**DigitalTwinsDescriptionListResult**](DigitalTwinsDescriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## digitalTwinsListByResourceGroup

> DigitalTwinsDescriptionListResult digitalTwinsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)



Get all the DigitalTwinsInstances in a resource group.

### Example

```javascript
import AzureDigitalTwinsManagementClient from 'azure_digital_twins_management_client';
let defaultClient = AzureDigitalTwinsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDigitalTwinsManagementClient.DigitalTwinsInstanceApi();
let apiVersion = "apiVersion_example"; // String | Version of the DigitalTwinsInstance Management API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
apiInstance.digitalTwinsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the DigitalTwinsInstance. | 

### Return type

[**DigitalTwinsDescriptionListResult**](DigitalTwinsDescriptionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## digitalTwinsUpdate

> DigitalTwinsDescription digitalTwinsUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, digitalTwinsPatchDescription)



Update metadata of DigitalTwinsInstance.

### Example

```javascript
import AzureDigitalTwinsManagementClient from 'azure_digital_twins_management_client';
let defaultClient = AzureDigitalTwinsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDigitalTwinsManagementClient.DigitalTwinsInstanceApi();
let apiVersion = "apiVersion_example"; // String | Version of the DigitalTwinsInstance Management API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the DigitalTwinsInstance.
let resourceName = "resourceName_example"; // String | The name of the DigitalTwinsInstance.
let digitalTwinsPatchDescription = new AzureDigitalTwinsManagementClient.DigitalTwinsPatchDescription(); // DigitalTwinsPatchDescription | The DigitalTwinsInstance and security metadata.
apiInstance.digitalTwinsUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, digitalTwinsPatchDescription, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the DigitalTwinsInstance Management API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the DigitalTwinsInstance. | 
 **resourceName** | **String**| The name of the DigitalTwinsInstance. | 
 **digitalTwinsPatchDescription** | [**DigitalTwinsPatchDescription**](DigitalTwinsPatchDescription.md)| The DigitalTwinsInstance and security metadata. | 

### Return type

[**DigitalTwinsDescription**](DigitalTwinsDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

