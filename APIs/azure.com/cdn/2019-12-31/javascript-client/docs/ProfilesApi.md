# CdnManagementClient.ProfilesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profilesCreate**](ProfilesApi.md#profilesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName} | 
[**profilesDelete**](ProfilesApi.md#profilesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName} | 
[**profilesGenerateSsoUri**](ProfilesApi.md#profilesGenerateSsoUri) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/generateSsoUri | 
[**profilesGet**](ProfilesApi.md#profilesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName} | 
[**profilesList**](ProfilesApi.md#profilesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Cdn/profiles | 
[**profilesListByResourceGroup**](ProfilesApi.md#profilesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles | 
[**profilesListResourceUsage**](ProfilesApi.md#profilesListResourceUsage) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/checkResourceUsage | 
[**profilesListSupportedOptimizationTypes**](ProfilesApi.md#profilesListSupportedOptimizationTypes) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/getSupportedOptimizationTypes | 
[**profilesUpdate**](ProfilesApi.md#profilesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName} | 



## profilesCreate

> Profile profilesCreate(resourceGroupName, profileName, subscriptionId, apiVersion, profile)



Creates a new CDN profile with a profile name under the specified subscription and resource group.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.ProfilesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
let profile = new CdnManagementClient.Profile(); // Profile | Profile properties needed to create a new profile.
apiInstance.profilesCreate(resourceGroupName, profileName, subscriptionId, apiVersion, profile, (error, data, response) => {
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
 **profile** | [**Profile**](Profile.md)| Profile properties needed to create a new profile. | 

### Return type

[**Profile**](Profile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## profilesDelete

> profilesDelete(resourceGroupName, profileName, subscriptionId, apiVersion)



Deletes an existing CDN profile with the specified parameters. Deleting a profile will result in the deletion of all of the sub-resources including endpoints, origins and custom domains.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.ProfilesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.profilesDelete(resourceGroupName, profileName, subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesGenerateSsoUri

> SsoUri profilesGenerateSsoUri(resourceGroupName, profileName, subscriptionId, apiVersion)



Generates a dynamic SSO URI used to sign in to the CDN supplemental portal. Supplemental portal is used to configure advanced feature capabilities that are not yet available in the Azure portal, such as core reports in a standard profile; rules engine, advanced HTTP reports, and real-time stats and alerts in a premium profile. The SSO URI changes approximately every 10 minutes.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.ProfilesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.profilesGenerateSsoUri(resourceGroupName, profileName, subscriptionId, apiVersion, (error, data, response) => {
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

[**SsoUri**](SsoUri.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesGet

> Profile profilesGet(resourceGroupName, profileName, subscriptionId, apiVersion)



Gets a CDN profile with the specified profile name under the specified subscription and resource group.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.ProfilesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.profilesGet(resourceGroupName, profileName, subscriptionId, apiVersion, (error, data, response) => {
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

[**Profile**](Profile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesList

> ProfileListResult profilesList(subscriptionId, apiVersion)



Lists all of the CDN profiles within an Azure subscription.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.ProfilesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.profilesList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 

### Return type

[**ProfileListResult**](ProfileListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesListByResourceGroup

> ProfileListResult profilesListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



Lists all of the CDN profiles within a resource group.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.ProfilesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.profilesListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 

### Return type

[**ProfileListResult**](ProfileListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesListResourceUsage

> ResourceUsageListResult profilesListResourceUsage(resourceGroupName, profileName, subscriptionId, apiVersion)



Checks the quota and actual usage of endpoints under the given CDN profile.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.ProfilesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.profilesListResourceUsage(resourceGroupName, profileName, subscriptionId, apiVersion, (error, data, response) => {
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

[**ResourceUsageListResult**](ResourceUsageListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesListSupportedOptimizationTypes

> SupportedOptimizationTypesListResult profilesListSupportedOptimizationTypes(resourceGroupName, profileName, subscriptionId, apiVersion)



Gets the supported optimization types for the current profile. A user can create an endpoint with an optimization type from the listed values.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.ProfilesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.profilesListSupportedOptimizationTypes(resourceGroupName, profileName, subscriptionId, apiVersion, (error, data, response) => {
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

[**SupportedOptimizationTypesListResult**](SupportedOptimizationTypesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## profilesUpdate

> Profile profilesUpdate(resourceGroupName, profileName, subscriptionId, apiVersion, profileUpdateParameters)



Updates an existing CDN profile with the specified profile name under the specified subscription and resource group.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.ProfilesApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
let profileUpdateParameters = new CdnManagementClient.ProfileUpdateParameters(); // ProfileUpdateParameters | Profile properties needed to update an existing profile.
apiInstance.profilesUpdate(resourceGroupName, profileName, subscriptionId, apiVersion, profileUpdateParameters, (error, data, response) => {
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
 **profileUpdateParameters** | [**ProfileUpdateParameters**](ProfileUpdateParameters.md)| Profile properties needed to update an existing profile. | 

### Return type

[**Profile**](Profile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

