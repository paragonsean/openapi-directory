# WebSiteManagementClient.ManagedHostingEnvironmentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**managedHostingEnvironmentsCreateOrUpdateManagedHostingEnvironment**](ManagedHostingEnvironmentsApi.md#managedHostingEnvironmentsCreateOrUpdateManagedHostingEnvironment) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/managedHostingEnvironments/{name} | Create or update a managed hosting environment.
[**managedHostingEnvironmentsDeleteManagedHostingEnvironment**](ManagedHostingEnvironmentsApi.md#managedHostingEnvironmentsDeleteManagedHostingEnvironment) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/managedHostingEnvironments/{name} | Delete a managed hosting environment.
[**managedHostingEnvironmentsGetManagedHostingEnvironment**](ManagedHostingEnvironmentsApi.md#managedHostingEnvironmentsGetManagedHostingEnvironment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/managedHostingEnvironments/{name} | Get properties of a managed hosting environment.
[**managedHostingEnvironmentsGetManagedHostingEnvironmentOperation**](ManagedHostingEnvironmentsApi.md#managedHostingEnvironmentsGetManagedHostingEnvironmentOperation) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/managedHostingEnvironments/{name}/operations/{operationId} | Get status of an operation on a managed hosting environment.
[**managedHostingEnvironmentsGetManagedHostingEnvironmentServerFarms**](ManagedHostingEnvironmentsApi.md#managedHostingEnvironmentsGetManagedHostingEnvironmentServerFarms) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/managedHostingEnvironments/{name}/serverfarms | Get all serverfarms (App Service Plans) on the managed hosting environment.
[**managedHostingEnvironmentsGetManagedHostingEnvironmentSites**](ManagedHostingEnvironmentsApi.md#managedHostingEnvironmentsGetManagedHostingEnvironmentSites) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/managedHostingEnvironments/{name}/sites | Get all sites on the managed hosting environment.
[**managedHostingEnvironmentsGetManagedHostingEnvironmentVips**](ManagedHostingEnvironmentsApi.md#managedHostingEnvironmentsGetManagedHostingEnvironmentVips) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/managedHostingEnvironments/{name}/capacities/virtualip | Get list of ip addresses assigned to a managed hosting environment
[**managedHostingEnvironmentsGetManagedHostingEnvironmentWebHostingPlans**](ManagedHostingEnvironmentsApi.md#managedHostingEnvironmentsGetManagedHostingEnvironmentWebHostingPlans) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/managedHostingEnvironments/{name}/webhostingplans | Get all serverfarms (App Service Plans) on the managed hosting environment.
[**managedHostingEnvironmentsGetManagedHostingEnvironments**](ManagedHostingEnvironmentsApi.md#managedHostingEnvironmentsGetManagedHostingEnvironments) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/managedHostingEnvironments | Get all managed hosting environments in a resource group.



## managedHostingEnvironmentsCreateOrUpdateManagedHostingEnvironment

> HostingEnvironment managedHostingEnvironmentsCreateOrUpdateManagedHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, managedHostingEnvironmentEnvelope)

Create or update a managed hosting environment.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ManagedHostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of managed hosting environment
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let managedHostingEnvironmentEnvelope = new WebSiteManagementClient.HostingEnvironment(); // HostingEnvironment | Properties of managed hosting environment
apiInstance.managedHostingEnvironmentsCreateOrUpdateManagedHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, managedHostingEnvironmentEnvelope, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of managed hosting environment | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **managedHostingEnvironmentEnvelope** | [**HostingEnvironment**](HostingEnvironment.md)| Properties of managed hosting environment | 

### Return type

[**HostingEnvironment**](HostingEnvironment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## managedHostingEnvironmentsDeleteManagedHostingEnvironment

> Object managedHostingEnvironmentsDeleteManagedHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, opts)

Delete a managed hosting environment.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ManagedHostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of managed hosting environment
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'forceDelete': true // Boolean | Delete even if the managed hosting environment contains resources
};
apiInstance.managedHostingEnvironmentsDeleteManagedHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of managed hosting environment | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **forceDelete** | **Boolean**| Delete even if the managed hosting environment contains resources | [optional] 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## managedHostingEnvironmentsGetManagedHostingEnvironment

> ManagedHostingEnvironment managedHostingEnvironmentsGetManagedHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion)

Get properties of a managed hosting environment.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ManagedHostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of managed hosting environment
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.managedHostingEnvironmentsGetManagedHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of managed hosting environment | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ManagedHostingEnvironment**](ManagedHostingEnvironment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## managedHostingEnvironmentsGetManagedHostingEnvironmentOperation

> Object managedHostingEnvironmentsGetManagedHostingEnvironmentOperation(resourceGroupName, name, operationId, subscriptionId, apiVersion)

Get status of an operation on a managed hosting environment.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ManagedHostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of managed hosting environment
let operationId = "operationId_example"; // String | operation identifier GUID
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.managedHostingEnvironmentsGetManagedHostingEnvironmentOperation(resourceGroupName, name, operationId, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of managed hosting environment | 
 **operationId** | **String**| operation identifier GUID | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## managedHostingEnvironmentsGetManagedHostingEnvironmentServerFarms

> ServerFarmCollection managedHostingEnvironmentsGetManagedHostingEnvironmentServerFarms(resourceGroupName, name, subscriptionId, apiVersion)

Get all serverfarms (App Service Plans) on the managed hosting environment.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ManagedHostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of managed hosting environment
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.managedHostingEnvironmentsGetManagedHostingEnvironmentServerFarms(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of managed hosting environment | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ServerFarmCollection**](ServerFarmCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## managedHostingEnvironmentsGetManagedHostingEnvironmentSites

> SiteCollection managedHostingEnvironmentsGetManagedHostingEnvironmentSites(resourceGroupName, name, subscriptionId, apiVersion, opts)

Get all sites on the managed hosting environment.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ManagedHostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of managed hosting environment
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'propertiesToInclude': "propertiesToInclude_example" // String | Comma separated list of site properties to include
};
apiInstance.managedHostingEnvironmentsGetManagedHostingEnvironmentSites(resourceGroupName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of managed hosting environment | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **propertiesToInclude** | **String**| Comma separated list of site properties to include | [optional] 

### Return type

[**SiteCollection**](SiteCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## managedHostingEnvironmentsGetManagedHostingEnvironmentVips

> AddressResponse managedHostingEnvironmentsGetManagedHostingEnvironmentVips(resourceGroupName, name, subscriptionId, apiVersion)

Get list of ip addresses assigned to a managed hosting environment

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ManagedHostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of managed hosting environment
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.managedHostingEnvironmentsGetManagedHostingEnvironmentVips(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of managed hosting environment | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## managedHostingEnvironmentsGetManagedHostingEnvironmentWebHostingPlans

> ServerFarmCollection managedHostingEnvironmentsGetManagedHostingEnvironmentWebHostingPlans(resourceGroupName, name, subscriptionId, apiVersion)

Get all serverfarms (App Service Plans) on the managed hosting environment.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ManagedHostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let name = "name_example"; // String | Name of managed hosting environment
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.managedHostingEnvironmentsGetManagedHostingEnvironmentWebHostingPlans(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of resource group | 
 **name** | **String**| Name of managed hosting environment | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ServerFarmCollection**](ServerFarmCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## managedHostingEnvironmentsGetManagedHostingEnvironments

> HostingEnvironmentCollection managedHostingEnvironmentsGetManagedHostingEnvironments(resourceGroupName, subscriptionId, apiVersion)

Get all managed hosting environments in a resource group.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.ManagedHostingEnvironmentsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.managedHostingEnvironmentsGetManagedHostingEnvironments(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of resource group | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**HostingEnvironmentCollection**](HostingEnvironmentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

