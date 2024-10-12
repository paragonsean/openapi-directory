# ApplicationInsightsManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**favoritesAdd**](DefaultApi.md#favoritesAdd) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteId} | 
[**favoritesDelete**](DefaultApi.md#favoritesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteId} | 
[**favoritesGet**](DefaultApi.md#favoritesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteId} | 
[**favoritesList**](DefaultApi.md#favoritesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites | 
[**favoritesUpdate**](DefaultApi.md#favoritesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteId} | 



## favoritesAdd

> ApplicationInsightsComponentFavorite favoritesAdd(resourceGroupName, apiVersion, subscriptionId, resourceName, favoriteId, favoriteProperties)



Adds a new favorites to an Application Insights component.

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
let favoriteId = "favoriteId_example"; // String | The Id of a specific favorite defined in the Application Insights component
let favoriteProperties = new ApplicationInsightsManagementClient.ApplicationInsightsComponentFavorite(); // ApplicationInsightsComponentFavorite | Properties that need to be specified to create a new favorite and add it to an Application Insights component.
apiInstance.favoritesAdd(resourceGroupName, apiVersion, subscriptionId, resourceName, favoriteId, favoriteProperties, (error, data, response) => {
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
 **favoriteId** | **String**| The Id of a specific favorite defined in the Application Insights component | 
 **favoriteProperties** | [**ApplicationInsightsComponentFavorite**](ApplicationInsightsComponentFavorite.md)| Properties that need to be specified to create a new favorite and add it to an Application Insights component. | 

### Return type

[**ApplicationInsightsComponentFavorite**](ApplicationInsightsComponentFavorite.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## favoritesDelete

> favoritesDelete(resourceGroupName, apiVersion, subscriptionId, resourceName, favoriteId)



Remove a favorite that is associated to an Application Insights component.

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
let favoriteId = "favoriteId_example"; // String | The Id of a specific favorite defined in the Application Insights component
apiInstance.favoritesDelete(resourceGroupName, apiVersion, subscriptionId, resourceName, favoriteId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceName** | **String**| The name of the Application Insights component resource. | 
 **favoriteId** | **String**| The Id of a specific favorite defined in the Application Insights component | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## favoritesGet

> ApplicationInsightsComponentFavorite favoritesGet(resourceGroupName, apiVersion, subscriptionId, resourceName, favoriteId)



Get a single favorite by its FavoriteId, defined within an Application Insights component.

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
let favoriteId = "favoriteId_example"; // String | The Id of a specific favorite defined in the Application Insights component
apiInstance.favoritesGet(resourceGroupName, apiVersion, subscriptionId, resourceName, favoriteId, (error, data, response) => {
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
 **favoriteId** | **String**| The Id of a specific favorite defined in the Application Insights component | 

### Return type

[**ApplicationInsightsComponentFavorite**](ApplicationInsightsComponentFavorite.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## favoritesList

> [ApplicationInsightsComponentFavorite] favoritesList(resourceGroupName, apiVersion, subscriptionId, resourceName, opts)



Gets a list of favorites defined within an Application Insights component.

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
let opts = {
  'favoriteType': "'shared'", // String | The type of favorite. Value can be either shared or user.
  'sourceType': "sourceType_example", // String | Source type of favorite to return. When left out, the source type defaults to 'other' (not present in this enum).
  'canFetchContent': true, // Boolean | Flag indicating whether or not to return the full content for each applicable favorite. If false, only return summary content for favorites.
  'tags': ["null"] // [String] | Tags that must be present on each favorite returned.
};
apiInstance.favoritesList(resourceGroupName, apiVersion, subscriptionId, resourceName, opts, (error, data, response) => {
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
 **favoriteType** | **String**| The type of favorite. Value can be either shared or user. | [optional] [default to &#39;shared&#39;]
 **sourceType** | **String**| Source type of favorite to return. When left out, the source type defaults to &#39;other&#39; (not present in this enum). | [optional] 
 **canFetchContent** | **Boolean**| Flag indicating whether or not to return the full content for each applicable favorite. If false, only return summary content for favorites. | [optional] 
 **tags** | [**[String]**](String.md)| Tags that must be present on each favorite returned. | [optional] 

### Return type

[**[ApplicationInsightsComponentFavorite]**](ApplicationInsightsComponentFavorite.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## favoritesUpdate

> ApplicationInsightsComponentFavorite favoritesUpdate(resourceGroupName, apiVersion, subscriptionId, resourceName, favoriteId, favoriteProperties)



Updates a favorite that has already been added to an Application Insights component.

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
let favoriteId = "favoriteId_example"; // String | The Id of a specific favorite defined in the Application Insights component
let favoriteProperties = new ApplicationInsightsManagementClient.ApplicationInsightsComponentFavorite(); // ApplicationInsightsComponentFavorite | Properties that need to be specified to update the existing favorite.
apiInstance.favoritesUpdate(resourceGroupName, apiVersion, subscriptionId, resourceName, favoriteId, favoriteProperties, (error, data, response) => {
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
 **favoriteId** | **String**| The Id of a specific favorite defined in the Application Insights component | 
 **favoriteProperties** | [**ApplicationInsightsComponentFavorite**](ApplicationInsightsComponentFavorite.md)| Properties that need to be specified to update the existing favorite. | 

### Return type

[**ApplicationInsightsComponentFavorite**](ApplicationInsightsComponentFavorite.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

