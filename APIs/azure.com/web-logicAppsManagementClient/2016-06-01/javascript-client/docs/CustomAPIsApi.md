# LogicAppsManagementClient.CustomAPIsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customApisCreateOrUpdate**](CustomAPIsApi.md#customApisCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/customApis/{apiName} | Replaces an existing custom API
[**customApisDelete**](CustomAPIsApi.md#customApisDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/customApis/{apiName} | Delete a custom API
[**customApisExtractApiDefinitionFromWsdl**](CustomAPIsApi.md#customApisExtractApiDefinitionFromWsdl) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/extractApiDefinitionFromWsdl | Returns API definition from WSDL
[**customApisGet**](CustomAPIsApi.md#customApisGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/customApis/{apiName} | Get a custom API
[**customApisList**](CustomAPIsApi.md#customApisList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/customApis | List of custom APIs
[**customApisListByResourceGroup**](CustomAPIsApi.md#customApisListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/customApis | List of custom APIs
[**customApisListWsdlInterfaces**](CustomAPIsApi.md#customApisListWsdlInterfaces) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/listWsdlInterfaces | Lists WSDL interfaces
[**customApisMove**](CustomAPIsApi.md#customApisMove) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/customApis/{apiName}/move | Moves the custom API
[**customApisUpdate**](CustomAPIsApi.md#customApisUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/customApis/{apiName} | Update an existing custom API



## customApisCreateOrUpdate

> CustomApiDefinition customApisCreateOrUpdate(subscriptionId, resourceGroupName, apiName, apiVersion, customApi)

Replaces an existing custom API

Creates or updates an existing custom API

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.CustomAPIsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let apiName = "apiName_example"; // String | API name
let apiVersion = "apiVersion_example"; // String | API Version
let customApi = new LogicAppsManagementClient.CustomApiDefinition(); // CustomApiDefinition | The custom API
apiInstance.customApisCreateOrUpdate(subscriptionId, resourceGroupName, apiName, apiVersion, customApi, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **resourceGroupName** | **String**| The resource group | 
 **apiName** | **String**| API name | 
 **apiVersion** | **String**| API Version | 
 **customApi** | [**CustomApiDefinition**](CustomApiDefinition.md)| The custom API | 

### Return type

[**CustomApiDefinition**](CustomApiDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customApisDelete

> customApisDelete(subscriptionId, resourceGroupName, apiName, apiVersion)

Delete a custom API

Deletes a custom API from the resource group

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.CustomAPIsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let apiName = "apiName_example"; // String | API name
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.customApisDelete(subscriptionId, resourceGroupName, apiName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **resourceGroupName** | **String**| The resource group | 
 **apiName** | **String**| API name | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## customApisExtractApiDefinitionFromWsdl

> Object customApisExtractApiDefinitionFromWsdl(subscriptionId, location, apiVersion, wsdlDefinition)

Returns API definition from WSDL

Parses the specified WSDL and extracts the API definition

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.CustomAPIsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let location = "location_example"; // String | The location
let apiVersion = "apiVersion_example"; // String | API Version
let wsdlDefinition = new LogicAppsManagementClient.WsdlDefinition(); // WsdlDefinition | WSDL definition
apiInstance.customApisExtractApiDefinitionFromWsdl(subscriptionId, location, apiVersion, wsdlDefinition, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **location** | **String**| The location | 
 **apiVersion** | **String**| API Version | 
 **wsdlDefinition** | [**WsdlDefinition**](WsdlDefinition.md)| WSDL definition | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customApisGet

> CustomApiDefinition customApisGet(subscriptionId, resourceGroupName, apiName, apiVersion)

Get a custom API

Gets a custom API by name for a specific subscription and resource group

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.CustomAPIsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let apiName = "apiName_example"; // String | API name
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.customApisGet(subscriptionId, resourceGroupName, apiName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **resourceGroupName** | **String**| The resource group | 
 **apiName** | **String**| API name | 
 **apiVersion** | **String**| API Version | 

### Return type

[**CustomApiDefinition**](CustomApiDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customApisList

> CustomApiDefinitionCollection customApisList(subscriptionId, apiVersion, opts)

List of custom APIs

Gets a list of all custom APIs for a subscription id

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.CustomAPIsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'top': 56, // Number | The number of items to be included in the result
  'skiptoken': "skiptoken_example" // String | Skip Token
};
apiInstance.customApisList(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **top** | **Number**| The number of items to be included in the result | [optional] 
 **skiptoken** | **String**| Skip Token | [optional] 

### Return type

[**CustomApiDefinitionCollection**](CustomApiDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customApisListByResourceGroup

> CustomApiDefinitionCollection customApisListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)

List of custom APIs

Gets a list of all custom APIs in a subscription for a specific resource group

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.CustomAPIsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'top': 56, // Number | The number of items to be included in the result
  'skiptoken': "skiptoken_example" // String | Skip Token
};
apiInstance.customApisListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **resourceGroupName** | **String**| The resource group | 
 **apiVersion** | **String**| API Version | 
 **top** | **Number**| The number of items to be included in the result | [optional] 
 **skiptoken** | **String**| Skip Token | [optional] 

### Return type

[**CustomApiDefinitionCollection**](CustomApiDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customApisListWsdlInterfaces

> WsdlServiceCollection customApisListWsdlInterfaces(subscriptionId, location, apiVersion, wsdlDefinition)

Lists WSDL interfaces

This returns the list of interfaces in the WSDL

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.CustomAPIsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let location = "location_example"; // String | The location
let apiVersion = "apiVersion_example"; // String | API Version
let wsdlDefinition = new LogicAppsManagementClient.WsdlDefinition(); // WsdlDefinition | WSDL definition
apiInstance.customApisListWsdlInterfaces(subscriptionId, location, apiVersion, wsdlDefinition, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **location** | **String**| The location | 
 **apiVersion** | **String**| API Version | 
 **wsdlDefinition** | [**WsdlDefinition**](WsdlDefinition.md)| WSDL definition | 

### Return type

[**WsdlServiceCollection**](WsdlServiceCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customApisMove

> customApisMove(subscriptionId, resourceGroupName, apiName, apiVersion, customApiReference)

Moves the custom API

Moves a specific custom API

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.CustomAPIsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let apiName = "apiName_example"; // String | API name
let apiVersion = "apiVersion_example"; // String | API Version
let customApiReference = new LogicAppsManagementClient.CustomApiReference(); // CustomApiReference | The custom API reference
apiInstance.customApisMove(subscriptionId, resourceGroupName, apiName, apiVersion, customApiReference, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **resourceGroupName** | **String**| The resource group | 
 **apiName** | **String**| API name | 
 **apiVersion** | **String**| API Version | 
 **customApiReference** | [**CustomApiReference**](CustomApiReference.md)| The custom API reference | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## customApisUpdate

> CustomApiDefinition customApisUpdate(subscriptionId, resourceGroupName, apiName, apiVersion, customApi)

Update an existing custom API

Updates an existing custom API&#39;s tags

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.CustomAPIsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let apiName = "apiName_example"; // String | API name
let apiVersion = "apiVersion_example"; // String | API Version
let customApi = new LogicAppsManagementClient.CustomApiDefinition(); // CustomApiDefinition | The custom API
apiInstance.customApisUpdate(subscriptionId, resourceGroupName, apiName, apiVersion, customApi, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **resourceGroupName** | **String**| The resource group | 
 **apiName** | **String**| API name | 
 **apiVersion** | **String**| API Version | 
 **customApi** | [**CustomApiDefinition**](CustomApiDefinition.md)| The custom API | 

### Return type

[**CustomApiDefinition**](CustomApiDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

