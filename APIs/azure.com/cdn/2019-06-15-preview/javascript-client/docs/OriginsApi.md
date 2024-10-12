# CdnManagementClient.OriginsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**originsGet**](OriginsApi.md#originsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/origins/{originName} | 
[**originsListByEndpoint**](OriginsApi.md#originsListByEndpoint) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/origins | 
[**originsUpdate**](OriginsApi.md#originsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/origins/{originName} | 



## originsGet

> Origin originsGet(resourceGroupName, profileName, endpointName, originName, subscriptionId, apiVersion)



Gets an existing origin within an endpoint.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.OriginsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let originName = "originName_example"; // String | Name of the origin which is unique within the endpoint.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.originsGet(resourceGroupName, profileName, endpointName, originName, subscriptionId, apiVersion, (error, data, response) => {
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
 **originName** | **String**| Name of the origin which is unique within the endpoint. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 

### Return type

[**Origin**](Origin.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## originsListByEndpoint

> OriginListResult originsListByEndpoint(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion)



Lists all of the existing origins within an endpoint.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.OriginsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.originsListByEndpoint(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, (error, data, response) => {
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

[**OriginListResult**](OriginListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## originsUpdate

> Origin originsUpdate(resourceGroupName, profileName, endpointName, originName, subscriptionId, apiVersion, originUpdateProperties)



Updates an existing origin within an endpoint.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.OriginsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let originName = "originName_example"; // String | Name of the origin which is unique within the endpoint.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
let originUpdateProperties = new CdnManagementClient.OriginUpdateParameters(); // OriginUpdateParameters | Origin properties
apiInstance.originsUpdate(resourceGroupName, profileName, endpointName, originName, subscriptionId, apiVersion, originUpdateProperties, (error, data, response) => {
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
 **originName** | **String**| Name of the origin which is unique within the endpoint. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 
 **originUpdateProperties** | [**OriginUpdateParameters**](OriginUpdateParameters.md)| Origin properties | 

### Return type

[**Origin**](Origin.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

