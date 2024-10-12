# ApplicationInsightsManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webTestsCreateOrUpdate**](DefaultApi.md#webTestsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/webtests/{webTestName} | 
[**webTestsDelete**](DefaultApi.md#webTestsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/webtests/{webTestName} | 
[**webTestsGet**](DefaultApi.md#webTestsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/webtests/{webTestName} | 
[**webTestsList**](DefaultApi.md#webTestsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Insights/webtests | 
[**webTestsListByComponent**](DefaultApi.md#webTestsListByComponent) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{componentName}/webtests | 
[**webTestsListByResourceGroup**](DefaultApi.md#webTestsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/webtests | 
[**webTestsUpdateTags**](DefaultApi.md#webTestsUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/webtests/{webTestName} | 



## webTestsCreateOrUpdate

> WebTest webTestsCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, webTestName, webTestDefinition)



Creates or updates an Application Insights web test definition.

### Example

```javascript
import ApplicationInsightsManagementClient from 'application_insights_management_client';
let defaultClient = ApplicationInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsManagementClient.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let webTestName = "webTestName_example"; // String | The name of the Application Insights webtest resource.
let webTestDefinition = new ApplicationInsightsManagementClient.WebTest(); // WebTest | Properties that need to be specified to create or update an Application Insights web test definition.
apiInstance.webTestsCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, webTestName, webTestDefinition, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **webTestName** | **String**| The name of the Application Insights webtest resource. | 
 **webTestDefinition** | [**WebTest**](WebTest.md)| Properties that need to be specified to create or update an Application Insights web test definition. | 

### Return type

[**WebTest**](WebTest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webTestsDelete

> webTestsDelete(subscriptionId, resourceGroupName, webTestName, apiVersion)



Deletes an Application Insights web test.

### Example

```javascript
import ApplicationInsightsManagementClient from 'application_insights_management_client';
let defaultClient = ApplicationInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let webTestName = "webTestName_example"; // String | The name of the Application Insights webtest resource.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.webTestsDelete(subscriptionId, resourceGroupName, webTestName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **webTestName** | **String**| The name of the Application Insights webtest resource. | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webTestsGet

> WebTest webTestsGet(resourceGroupName, apiVersion, subscriptionId, webTestName)



Get a specific Application Insights web test definition.

### Example

```javascript
import ApplicationInsightsManagementClient from 'application_insights_management_client';
let defaultClient = ApplicationInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsManagementClient.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let webTestName = "webTestName_example"; // String | The name of the Application Insights webtest resource.
apiInstance.webTestsGet(resourceGroupName, apiVersion, subscriptionId, webTestName, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **webTestName** | **String**| The name of the Application Insights webtest resource. | 

### Return type

[**WebTest**](WebTest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webTestsList

> WebTestListResult webTestsList(apiVersion, subscriptionId)



Get all Application Insights web test alerts definitions within a subscription.

### Example

```javascript
import ApplicationInsightsManagementClient from 'application_insights_management_client';
let defaultClient = ApplicationInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsManagementClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.webTestsList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**WebTestListResult**](WebTestListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webTestsListByComponent

> WebTestListResult webTestsListByComponent(componentName, resourceGroupName, apiVersion, subscriptionId)



Get all Application Insights web tests defined for the specified component.

### Example

```javascript
import ApplicationInsightsManagementClient from 'application_insights_management_client';
let defaultClient = ApplicationInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsManagementClient.DefaultApi();
let componentName = "componentName_example"; // String | The name of the Application Insights component resource.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.webTestsListByComponent(componentName, resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **componentName** | **String**| The name of the Application Insights component resource. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**WebTestListResult**](WebTestListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webTestsListByResourceGroup

> WebTestListResult webTestsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Get all Application Insights web tests defined within a specified resource group.

### Example

```javascript
import ApplicationInsightsManagementClient from 'application_insights_management_client';
let defaultClient = ApplicationInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsManagementClient.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.webTestsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**WebTestListResult**](WebTestListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webTestsUpdateTags

> WebTest webTestsUpdateTags(resourceGroupName, apiVersion, subscriptionId, webTestName, webTestTags)



Creates or updates an Application Insights web test definition.

### Example

```javascript
import ApplicationInsightsManagementClient from 'application_insights_management_client';
let defaultClient = ApplicationInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationInsightsManagementClient.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let webTestName = "webTestName_example"; // String | The name of the Application Insights webtest resource.
let webTestTags = new ApplicationInsightsManagementClient.TagsResource(); // TagsResource | Updated tag information to set into the web test instance.
apiInstance.webTestsUpdateTags(resourceGroupName, apiVersion, subscriptionId, webTestName, webTestTags, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **webTestName** | **String**| The name of the Application Insights webtest resource. | 
 **webTestTags** | [**TagsResource**](TagsResource.md)| Updated tag information to set into the web test instance. | 

### Return type

[**WebTest**](WebTest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

