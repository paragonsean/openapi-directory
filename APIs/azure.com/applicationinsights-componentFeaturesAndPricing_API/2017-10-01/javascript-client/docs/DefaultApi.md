# ApplicationInsightsManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**componentCurrentPricingPlanCreateAndUpdate**](DefaultApi.md#componentCurrentPricingPlanCreateAndUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/pricingPlans/current | 
[**componentCurrentPricingPlanGet**](DefaultApi.md#componentCurrentPricingPlanGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/pricingPlans/current | 
[**componentCurrentPricingPlanUpdate**](DefaultApi.md#componentCurrentPricingPlanUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/pricingPlans/current | 



## componentCurrentPricingPlanCreateAndUpdate

> ApplicationInsightsComponentPricingPlan componentCurrentPricingPlanCreateAndUpdate(resourceGroupName, apiVersion, subscriptionId, resourceName, pricingPlanProperties)



Replace current pricing plan for an Application Insights component.

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
let pricingPlanProperties = new ApplicationInsightsManagementClient.ApplicationInsightsComponentPricingPlan(); // ApplicationInsightsComponentPricingPlan | Properties that need to be specified to update current pricing plan for an Application Insights component.
apiInstance.componentCurrentPricingPlanCreateAndUpdate(resourceGroupName, apiVersion, subscriptionId, resourceName, pricingPlanProperties, (error, data, response) => {
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
 **pricingPlanProperties** | [**ApplicationInsightsComponentPricingPlan**](ApplicationInsightsComponentPricingPlan.md)| Properties that need to be specified to update current pricing plan for an Application Insights component. | 

### Return type

[**ApplicationInsightsComponentPricingPlan**](ApplicationInsightsComponentPricingPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## componentCurrentPricingPlanGet

> ApplicationInsightsComponentPricingPlan componentCurrentPricingPlanGet(resourceGroupName, apiVersion, subscriptionId, resourceName)



Returns the current pricing plan setting for an Application Insights component.

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
apiInstance.componentCurrentPricingPlanGet(resourceGroupName, apiVersion, subscriptionId, resourceName, (error, data, response) => {
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

[**ApplicationInsightsComponentPricingPlan**](ApplicationInsightsComponentPricingPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## componentCurrentPricingPlanUpdate

> ApplicationInsightsComponentPricingPlan componentCurrentPricingPlanUpdate(resourceGroupName, apiVersion, subscriptionId, resourceName, pricingPlanProperties)



Update current pricing plan for an Application Insights component.

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
let pricingPlanProperties = new ApplicationInsightsManagementClient.ApplicationInsightsComponentPricingPlan(); // ApplicationInsightsComponentPricingPlan | Properties that need to be specified to update current pricing plan for an Application Insights component.
apiInstance.componentCurrentPricingPlanUpdate(resourceGroupName, apiVersion, subscriptionId, resourceName, pricingPlanProperties, (error, data, response) => {
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
 **pricingPlanProperties** | [**ApplicationInsightsComponentPricingPlan**](ApplicationInsightsComponentPricingPlan.md)| Properties that need to be specified to update current pricing plan for an Application Insights component. | 

### Return type

[**ApplicationInsightsComponentPricingPlan**](ApplicationInsightsComponentPricingPlan.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

