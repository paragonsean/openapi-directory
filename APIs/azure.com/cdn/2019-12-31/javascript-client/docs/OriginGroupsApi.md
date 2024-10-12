# CdnManagementClient.OriginGroupsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**originGroupsCreate**](OriginGroupsApi.md#originGroupsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/originGroups/{originGroupName} | 
[**originGroupsDelete**](OriginGroupsApi.md#originGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/originGroups/{originGroupName} | 
[**originGroupsGet**](OriginGroupsApi.md#originGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/originGroups/{originGroupName} | 
[**originGroupsListByEndpoint**](OriginGroupsApi.md#originGroupsListByEndpoint) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/originGroups | 
[**originGroupsUpdate**](OriginGroupsApi.md#originGroupsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/originGroups/{originGroupName} | 



## originGroupsCreate

> OriginGroup originGroupsCreate(resourceGroupName, profileName, endpointName, originGroupName, subscriptionId, apiVersion, originGroup)



Creates a new origin group within the specified endpoint.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.OriginGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let originGroupName = "originGroupName_example"; // String | Name of the origin group which is unique within the endpoint.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
let originGroup = new CdnManagementClient.OriginGroup(); // OriginGroup | Origin group properties
apiInstance.originGroupsCreate(resourceGroupName, profileName, endpointName, originGroupName, subscriptionId, apiVersion, originGroup, (error, data, response) => {
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
 **originGroupName** | **String**| Name of the origin group which is unique within the endpoint. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 
 **originGroup** | [**OriginGroup**](OriginGroup.md)| Origin group properties | 

### Return type

[**OriginGroup**](OriginGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## originGroupsDelete

> originGroupsDelete(resourceGroupName, profileName, endpointName, originGroupName, subscriptionId, apiVersion)



Deletes an existing origin group within an endpoint.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.OriginGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let originGroupName = "originGroupName_example"; // String | Name of the origin group which is unique within the endpoint.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.originGroupsDelete(resourceGroupName, profileName, endpointName, originGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **originGroupName** | **String**| Name of the origin group which is unique within the endpoint. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## originGroupsGet

> OriginGroup originGroupsGet(resourceGroupName, profileName, endpointName, originGroupName, subscriptionId, apiVersion)



Gets an existing origin group within an endpoint.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.OriginGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let originGroupName = "originGroupName_example"; // String | Name of the origin group which is unique within the endpoint.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.originGroupsGet(resourceGroupName, profileName, endpointName, originGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **originGroupName** | **String**| Name of the origin group which is unique within the endpoint. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 

### Return type

[**OriginGroup**](OriginGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## originGroupsListByEndpoint

> OriginGroupListResult originGroupsListByEndpoint(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion)



Lists all of the existing origin groups within an endpoint.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.OriginGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.originGroupsListByEndpoint(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, (error, data, response) => {
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

[**OriginGroupListResult**](OriginGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## originGroupsUpdate

> OriginGroup originGroupsUpdate(resourceGroupName, profileName, endpointName, originGroupName, subscriptionId, apiVersion, originGroupUpdateProperties)



Updates an existing origin group within an endpoint.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.OriginGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let originGroupName = "originGroupName_example"; // String | Name of the origin group which is unique within the endpoint.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
let originGroupUpdateProperties = new CdnManagementClient.OriginGroupUpdateParameters(); // OriginGroupUpdateParameters | Origin group properties
apiInstance.originGroupsUpdate(resourceGroupName, profileName, endpointName, originGroupName, subscriptionId, apiVersion, originGroupUpdateProperties, (error, data, response) => {
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
 **originGroupName** | **String**| Name of the origin group which is unique within the endpoint. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 
 **originGroupUpdateProperties** | [**OriginGroupUpdateParameters**](OriginGroupUpdateParameters.md)| Origin group properties | 

### Return type

[**OriginGroup**](OriginGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

