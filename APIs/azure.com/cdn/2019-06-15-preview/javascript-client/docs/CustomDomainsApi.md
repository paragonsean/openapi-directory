# CdnManagementClient.CustomDomainsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customDomainsCreate**](CustomDomainsApi.md#customDomainsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains/{customDomainName} | 
[**customDomainsDelete**](CustomDomainsApi.md#customDomainsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains/{customDomainName} | 
[**customDomainsDisableCustomHttps**](CustomDomainsApi.md#customDomainsDisableCustomHttps) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains/{customDomainName}/disableCustomHttps | 
[**customDomainsEnableCustomHttps**](CustomDomainsApi.md#customDomainsEnableCustomHttps) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains/{customDomainName}/enableCustomHttps | 
[**customDomainsGet**](CustomDomainsApi.md#customDomainsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains/{customDomainName} | 
[**customDomainsListByEndpoint**](CustomDomainsApi.md#customDomainsListByEndpoint) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains | 



## customDomainsCreate

> CustomDomain customDomainsCreate(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion, customDomainProperties)



Creates a new custom domain within an endpoint.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.CustomDomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let customDomainName = "customDomainName_example"; // String | Name of the custom domain within an endpoint.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
let customDomainProperties = new CdnManagementClient.CustomDomainParameters(); // CustomDomainParameters | Properties required to create a new custom domain.
apiInstance.customDomainsCreate(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion, customDomainProperties, (error, data, response) => {
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
 **customDomainName** | **String**| Name of the custom domain within an endpoint. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 
 **customDomainProperties** | [**CustomDomainParameters**](CustomDomainParameters.md)| Properties required to create a new custom domain. | 

### Return type

[**CustomDomain**](CustomDomain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customDomainsDelete

> customDomainsDelete(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion)



Deletes an existing custom domain within an endpoint.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.CustomDomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let customDomainName = "customDomainName_example"; // String | Name of the custom domain within an endpoint.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.customDomainsDelete(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion, (error, data, response) => {
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
 **customDomainName** | **String**| Name of the custom domain within an endpoint. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customDomainsDisableCustomHttps

> customDomainsDisableCustomHttps(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion)



Disable https delivery of the custom domain.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.CustomDomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let customDomainName = "customDomainName_example"; // String | Name of the custom domain within an endpoint.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.customDomainsDisableCustomHttps(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion, (error, data, response) => {
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
 **customDomainName** | **String**| Name of the custom domain within an endpoint. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customDomainsEnableCustomHttps

> customDomainsEnableCustomHttps(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion, opts)



Enable https delivery of the custom domain.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.CustomDomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let customDomainName = "customDomainName_example"; // String | Name of the custom domain within an endpoint.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
let opts = {
  'customDomainHttpsParameters': new CdnManagementClient.CustomDomainHttpsParameters() // CustomDomainHttpsParameters | The configuration specifying how to enable HTTPS for the custom domain - using CDN managed certificate or user's own certificate. If not specified, enabling ssl uses CDN managed certificate by default.
};
apiInstance.customDomainsEnableCustomHttps(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **customDomainName** | **String**| Name of the custom domain within an endpoint. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 
 **customDomainHttpsParameters** | [**CustomDomainHttpsParameters**](CustomDomainHttpsParameters.md)| The configuration specifying how to enable HTTPS for the custom domain - using CDN managed certificate or user&#39;s own certificate. If not specified, enabling ssl uses CDN managed certificate by default. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customDomainsGet

> CustomDomain customDomainsGet(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion)



Gets an existing custom domain within an endpoint.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.CustomDomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let customDomainName = "customDomainName_example"; // String | Name of the custom domain within an endpoint.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.customDomainsGet(resourceGroupName, profileName, endpointName, customDomainName, subscriptionId, apiVersion, (error, data, response) => {
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
 **customDomainName** | **String**| Name of the custom domain within an endpoint. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | 

### Return type

[**CustomDomain**](CustomDomain.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customDomainsListByEndpoint

> CustomDomainListResult customDomainsListByEndpoint(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion)



Lists all of the existing custom domains within an endpoint.

### Example

```javascript
import CdnManagementClient from 'cdn_management_client';
let defaultClient = CdnManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CdnManagementClient.CustomDomainsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
let endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
apiInstance.customDomainsListByEndpoint(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, (error, data, response) => {
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

[**CustomDomainListResult**](CustomDomainListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

