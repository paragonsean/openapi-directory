# ApplicationInsightsManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**componentAvailableFeaturesGet**](DefaultApi.md#componentAvailableFeaturesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/getavailablebillingfeatures | 
[**componentCurrentBillingFeaturesGet**](DefaultApi.md#componentCurrentBillingFeaturesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/currentbillingfeatures | 
[**componentCurrentBillingFeaturesUpdate**](DefaultApi.md#componentCurrentBillingFeaturesUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/currentbillingfeatures | 
[**componentFeatureCapabilitiesGet**](DefaultApi.md#componentFeatureCapabilitiesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/featurecapabilities | 
[**componentQuotaStatusGet**](DefaultApi.md#componentQuotaStatusGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/quotastatus | 



## componentAvailableFeaturesGet

> ApplicationInsightsComponentAvailableFeatures componentAvailableFeaturesGet(resourceGroupName, apiVersion, subscriptionId, resourceName)



Returns all available features of the application insights component.

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
apiInstance.componentAvailableFeaturesGet(resourceGroupName, apiVersion, subscriptionId, resourceName, (error, data, response) => {
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

[**ApplicationInsightsComponentAvailableFeatures**](ApplicationInsightsComponentAvailableFeatures.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## componentCurrentBillingFeaturesGet

> ApplicationInsightsComponentBillingFeatures componentCurrentBillingFeaturesGet(resourceGroupName, apiVersion, subscriptionId, resourceName)



Returns current billing features for an Application Insights component.

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
apiInstance.componentCurrentBillingFeaturesGet(resourceGroupName, apiVersion, subscriptionId, resourceName, (error, data, response) => {
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

[**ApplicationInsightsComponentBillingFeatures**](ApplicationInsightsComponentBillingFeatures.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## componentCurrentBillingFeaturesUpdate

> ApplicationInsightsComponentBillingFeatures componentCurrentBillingFeaturesUpdate(resourceGroupName, apiVersion, subscriptionId, resourceName, billingFeaturesProperties)



Update current billing features for an Application Insights component.

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
let billingFeaturesProperties = new ApplicationInsightsManagementClient.ApplicationInsightsComponentBillingFeatures(); // ApplicationInsightsComponentBillingFeatures | Properties that need to be specified to update billing features for an Application Insights component.
apiInstance.componentCurrentBillingFeaturesUpdate(resourceGroupName, apiVersion, subscriptionId, resourceName, billingFeaturesProperties, (error, data, response) => {
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
 **billingFeaturesProperties** | [**ApplicationInsightsComponentBillingFeatures**](ApplicationInsightsComponentBillingFeatures.md)| Properties that need to be specified to update billing features for an Application Insights component. | 

### Return type

[**ApplicationInsightsComponentBillingFeatures**](ApplicationInsightsComponentBillingFeatures.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## componentFeatureCapabilitiesGet

> ApplicationInsightsComponentFeatureCapabilities componentFeatureCapabilitiesGet(resourceGroupName, apiVersion, subscriptionId, resourceName)



Returns feature capabilities of the application insights component.

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
apiInstance.componentFeatureCapabilitiesGet(resourceGroupName, apiVersion, subscriptionId, resourceName, (error, data, response) => {
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

[**ApplicationInsightsComponentFeatureCapabilities**](ApplicationInsightsComponentFeatureCapabilities.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## componentQuotaStatusGet

> ApplicationInsightsComponentQuotaStatus componentQuotaStatusGet(resourceGroupName, apiVersion, subscriptionId, resourceName)



Returns daily data volume cap (quota) status for an Application Insights component.

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
apiInstance.componentQuotaStatusGet(resourceGroupName, apiVersion, subscriptionId, resourceName, (error, data, response) => {
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

[**ApplicationInsightsComponentQuotaStatus**](ApplicationInsightsComponentQuotaStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

