# ApplicationInsightsManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**proactiveDetectionConfigurationsGet**](DefaultApi.md#proactiveDetectionConfigurationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/ProactiveDetectionConfigs/{ConfigurationId} | 
[**proactiveDetectionConfigurationsList**](DefaultApi.md#proactiveDetectionConfigurationsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/ProactiveDetectionConfigs | 
[**proactiveDetectionConfigurationsUpdate**](DefaultApi.md#proactiveDetectionConfigurationsUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/ProactiveDetectionConfigs/{ConfigurationId} | 



## proactiveDetectionConfigurationsGet

> ApplicationInsightsComponentProactiveDetectionConfiguration proactiveDetectionConfigurationsGet(resourceGroupName, apiVersion, subscriptionId, resourceName, configurationId)



Get the ProactiveDetection configuration for this configuration id.

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
let resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
let configurationId = "configurationId_example"; // String | The ProactiveDetection configuration ID. This is unique within a Application Insights component.
apiInstance.proactiveDetectionConfigurationsGet(resourceGroupName, apiVersion, subscriptionId, resourceName, configurationId, (error, data, response) => {
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
 **resourceName** | **String**| The name of the Application Insights component resource. | 
 **configurationId** | **String**| The ProactiveDetection configuration ID. This is unique within a Application Insights component. | 

### Return type

[**ApplicationInsightsComponentProactiveDetectionConfiguration**](ApplicationInsightsComponentProactiveDetectionConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proactiveDetectionConfigurationsList

> [ApplicationInsightsComponentProactiveDetectionConfiguration] proactiveDetectionConfigurationsList(resourceGroupName, apiVersion, subscriptionId, resourceName)



Gets a list of ProactiveDetection configurations of an Application Insights component.

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
let resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
apiInstance.proactiveDetectionConfigurationsList(resourceGroupName, apiVersion, subscriptionId, resourceName, (error, data, response) => {
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
 **resourceName** | **String**| The name of the Application Insights component resource. | 

### Return type

[**[ApplicationInsightsComponentProactiveDetectionConfiguration]**](ApplicationInsightsComponentProactiveDetectionConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proactiveDetectionConfigurationsUpdate

> ApplicationInsightsComponentProactiveDetectionConfiguration proactiveDetectionConfigurationsUpdate(resourceGroupName, apiVersion, subscriptionId, resourceName, configurationId, proactiveDetectionProperties)



Update the ProactiveDetection configuration for this configuration id.

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
let resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
let configurationId = "configurationId_example"; // String | The ProactiveDetection configuration ID. This is unique within a Application Insights component.
let proactiveDetectionProperties = new ApplicationInsightsManagementClient.ApplicationInsightsComponentProactiveDetectionConfiguration(); // ApplicationInsightsComponentProactiveDetectionConfiguration | Properties that need to be specified to update the ProactiveDetection configuration.
apiInstance.proactiveDetectionConfigurationsUpdate(resourceGroupName, apiVersion, subscriptionId, resourceName, configurationId, proactiveDetectionProperties, (error, data, response) => {
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
 **resourceName** | **String**| The name of the Application Insights component resource. | 
 **configurationId** | **String**| The ProactiveDetection configuration ID. This is unique within a Application Insights component. | 
 **proactiveDetectionProperties** | [**ApplicationInsightsComponentProactiveDetectionConfiguration**](ApplicationInsightsComponentProactiveDetectionConfiguration.md)| Properties that need to be specified to update the ProactiveDetection configuration. | 

### Return type

[**ApplicationInsightsComponentProactiveDetectionConfiguration**](ApplicationInsightsComponentProactiveDetectionConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

