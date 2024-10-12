# ApplicationInsightsManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyticsItemsDelete**](DefaultApi.md#analyticsItemsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item | 
[**analyticsItemsGet**](DefaultApi.md#analyticsItemsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item | 
[**analyticsItemsList**](DefaultApi.md#analyticsItemsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath} | 
[**analyticsItemsPut**](DefaultApi.md#analyticsItemsPut) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/{scopePath}/item | 



## analyticsItemsDelete

> analyticsItemsDelete(subscriptionId, resourceGroupName, resourceName, scopePath, apiVersion, opts)



Deletes a specific Analytics Items defined within an Application Insights component.

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
let resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
let scopePath = "scopePath_example"; // String | Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'id': "id_example", // String | The Id of a specific item defined in the Application Insights component
  'name': "name_example" // String | The name of a specific item defined in the Application Insights component
};
apiInstance.analyticsItemsDelete(subscriptionId, resourceGroupName, resourceName, scopePath, apiVersion, opts, (error, data, response) => {
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
 **resourceName** | **String**| The name of the Application Insights component resource. | 
 **scopePath** | **String**| Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **id** | **String**| The Id of a specific item defined in the Application Insights component | [optional] 
 **name** | **String**| The name of a specific item defined in the Application Insights component | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## analyticsItemsGet

> ApplicationInsightsComponentAnalyticsItem analyticsItemsGet(subscriptionId, resourceGroupName, resourceName, scopePath, apiVersion, opts)



Gets a specific Analytics Items defined within an Application Insights component.

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
let resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
let scopePath = "scopePath_example"; // String | Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'id': "id_example", // String | The Id of a specific item defined in the Application Insights component
  'name': "name_example" // String | The name of a specific item defined in the Application Insights component
};
apiInstance.analyticsItemsGet(subscriptionId, resourceGroupName, resourceName, scopePath, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **resourceName** | **String**| The name of the Application Insights component resource. | 
 **scopePath** | **String**| Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **id** | **String**| The Id of a specific item defined in the Application Insights component | [optional] 
 **name** | **String**| The name of a specific item defined in the Application Insights component | [optional] 

### Return type

[**ApplicationInsightsComponentAnalyticsItem**](ApplicationInsightsComponentAnalyticsItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsItemsList

> [ApplicationInsightsComponentAnalyticsItem] analyticsItemsList(subscriptionId, resourceGroupName, resourceName, scopePath, apiVersion, opts)



Gets a list of Analytics Items defined within an Application Insights component.

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
let resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
let scopePath = "scopePath_example"; // String | Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'scope': "'shared'", // String | Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
  'type': "'none'", // String | Enum indicating the type of the Analytics item.
  'includeContent': true // Boolean | Flag indicating whether or not to return the content of each applicable item. If false, only return the item information.
};
apiInstance.analyticsItemsList(subscriptionId, resourceGroupName, resourceName, scopePath, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **resourceName** | **String**| The name of the Application Insights component resource. | 
 **scopePath** | **String**| Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **scope** | **String**| Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component. | [optional] [default to &#39;shared&#39;]
 **type** | **String**| Enum indicating the type of the Analytics item. | [optional] [default to &#39;none&#39;]
 **includeContent** | **Boolean**| Flag indicating whether or not to return the content of each applicable item. If false, only return the item information. | [optional] 

### Return type

[**[ApplicationInsightsComponentAnalyticsItem]**](ApplicationInsightsComponentAnalyticsItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## analyticsItemsPut

> ApplicationInsightsComponentAnalyticsItem analyticsItemsPut(subscriptionId, resourceGroupName, resourceName, scopePath, apiVersion, itemProperties, opts)



Adds or Updates a specific Analytics Item within an Application Insights component.

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
let resourceName = "resourceName_example"; // String | The name of the Application Insights component resource.
let scopePath = "scopePath_example"; // String | Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let itemProperties = new ApplicationInsightsManagementClient.ApplicationInsightsComponentAnalyticsItem(); // ApplicationInsightsComponentAnalyticsItem | Properties that need to be specified to create a new item and add it to an Application Insights component.
let opts = {
  'overrideItem': true // Boolean | Flag indicating whether or not to force save an item. This allows overriding an item if it already exists.
};
apiInstance.analyticsItemsPut(subscriptionId, resourceGroupName, resourceName, scopePath, apiVersion, itemProperties, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **resourceName** | **String**| The name of the Application Insights component resource. | 
 **scopePath** | **String**| Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **itemProperties** | [**ApplicationInsightsComponentAnalyticsItem**](ApplicationInsightsComponentAnalyticsItem.md)| Properties that need to be specified to create a new item and add it to an Application Insights component. | 
 **overrideItem** | **Boolean**| Flag indicating whether or not to force save an item. This allows overriding an item if it already exists. | [optional] 

### Return type

[**ApplicationInsightsComponentAnalyticsItem**](ApplicationInsightsComponentAnalyticsItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

