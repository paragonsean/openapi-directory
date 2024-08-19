# CdnManagementClient.EndpointsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpointsCreate**](EndpointsApi.md#endpointsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName} | 
[**endpointsDelete**](EndpointsApi.md#endpointsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName} | 
[**endpointsGet**](EndpointsApi.md#endpointsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName} | 
[**endpointsListByProfile**](EndpointsApi.md#endpointsListByProfile) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints | 
[**endpointsListResourceUsage**](EndpointsApi.md#endpointsListResourceUsage) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/checkResourceUsage | 
[**endpointsLoadContent**](EndpointsApi.md#endpointsLoadContent) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/load | 
[**endpointsPurgeContent**](EndpointsApi.md#endpointsPurgeContent) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/purge | 
[**endpointsStart**](EndpointsApi.md#endpointsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/start | 
[**endpointsStop**](EndpointsApi.md#endpointsStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/stop | 
[**endpointsUpdate**](EndpointsApi.md#endpointsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName} | 
[**endpointsValidateCustomDomain**](EndpointsApi.md#endpointsValidateCustomDomain) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/validateCustomDomain | 



## endpointsCreate

> Endpoint endpointsCreate(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, endpoint)



Creates a new CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.EndpointsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
let endpoint = new CdnManagementClient.Endpoint(); // Endpoint | Endpoint properties
apiInstance.endpointsCreate(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, endpoint, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | 
 **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 
 **endpoint** | [**Endpoint**](Endpoint.md)| Endpoint properties | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## endpointsDelete

> endpointsDelete(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion)



Deletes an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.EndpointsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.endpointsDelete(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | 
 **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## endpointsGet

> Endpoint endpointsGet(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion)



Gets an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.EndpointsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.endpointsGet(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | 
 **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## endpointsListByProfile

> EndpointListResult endpointsListByProfile(resourceGroupName, profileName, subscriptionId, apiVersion)



Lists existing CDN endpoints.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.EndpointsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.endpointsListByProfile(resourceGroupName, profileName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 

### Return type

[**EndpointListResult**](EndpointListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## endpointsListResourceUsage

> ResourceUsageListResult endpointsListResourceUsage(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion)



Checks the quota and usage of geo filters and custom domains under the given endpoint.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.EndpointsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.endpointsListResourceUsage(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | 
 **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 

### Return type

[**ResourceUsageListResult**](ResourceUsageListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## endpointsLoadContent

> endpointsLoadContent(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, contentFilePaths)



Pre-loads a content to CDN. Available for Verizon Profiles.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.EndpointsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
let contentFilePaths = new CdnManagementClient.LoadParameters(); // LoadParameters | The path to the content to be loaded. Path should be a full URL, e.g. ‘/pictures/city.png' which loads a single file 
apiInstance.endpointsLoadContent(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, contentFilePaths, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | 
 **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 
 **contentFilePaths** | [**LoadParameters**](LoadParameters.md)| The path to the content to be loaded. Path should be a full URL, e.g. ‘/pictures/city.png&#39; which loads a single file  | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## endpointsPurgeContent

> endpointsPurgeContent(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, contentFilePaths)



Removes a content from CDN.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.EndpointsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
let contentFilePaths = new CdnManagementClient.PurgeParameters(); // PurgeParameters | The path to the content to be purged. Path can be a full URL, e.g. '/pictures/city.png' which removes a single file, or a directory with a wildcard, e.g. '/pictures/_*' which removes all folders and files in the directory.
apiInstance.endpointsPurgeContent(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, contentFilePaths, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | 
 **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 
 **contentFilePaths** | [**PurgeParameters**](PurgeParameters.md)| The path to the content to be purged. Path can be a full URL, e.g. &#39;/pictures/city.png&#39; which removes a single file, or a directory with a wildcard, e.g. &#39;/pictures/_*&#39; which removes all folders and files in the directory. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## endpointsStart

> Endpoint endpointsStart(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion)



Starts an existing CDN endpoint that is on a stopped state.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.EndpointsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.endpointsStart(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | 
 **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## endpointsStop

> Endpoint endpointsStop(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion)



Stops an existing running CDN endpoint.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.EndpointsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.endpointsStop(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | 
 **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## endpointsUpdate

> Endpoint endpointsUpdate(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, endpointUpdateProperties)



Updates an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile. Only tags can be updated after creating an endpoint. To update origins, use the Update Origin operation. To update origin groups, use the Update Origin group operation. To update custom domains, use the Update Custom Domain operation.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.EndpointsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
let endpointUpdateProperties = new CdnManagementClient.EndpointUpdateParameters(); // EndpointUpdateParameters | Endpoint update properties
apiInstance.endpointsUpdate(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, endpointUpdateProperties, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | 
 **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 
 **endpointUpdateProperties** | [**EndpointUpdateParameters**](EndpointUpdateParameters.md)| Endpoint update properties | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## endpointsValidateCustomDomain

> ValidateCustomDomainOutput endpointsValidateCustomDomain(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, customDomainProperties)



Validates the custom domain mapping to ensure it maps to the correct CDN endpoint in DNS.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.EndpointsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
let customDomainProperties = new CdnManagementClient.ValidateCustomDomainInput(); // ValidateCustomDomainInput | Custom domain to be validated.
apiInstance.endpointsValidateCustomDomain(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, customDomainProperties, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | 
 **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 
 **customDomainProperties** | [**ValidateCustomDomainInput**](ValidateCustomDomainInput.md)| Custom domain to be validated. | 

### Return type

[**ValidateCustomDomainOutput**](ValidateCustomDomainOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

