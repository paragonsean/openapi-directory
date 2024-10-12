# RecommendationsApiClient.RecommendationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recommendationsDisableAllForHostingEnvironment**](RecommendationsApi.md#recommendationsDisableAllForHostingEnvironment) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{hostingEnvironmentName}/recommendations/disable | Disable all recommendations for an app.
[**recommendationsDisableAllForWebApp**](RecommendationsApi.md#recommendationsDisableAllForWebApp) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/recommendations/disable | Disable all recommendations for an app.
[**recommendationsDisableRecommendationForHostingEnvironment**](RecommendationsApi.md#recommendationsDisableRecommendationForHostingEnvironment) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{hostingEnvironmentName}/recommendations/{name}/disable | Disables the specific rule for a web site permanently.
[**recommendationsDisableRecommendationForSite**](RecommendationsApi.md#recommendationsDisableRecommendationForSite) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/recommendations/{name}/disable | Disables the specific rule for a web site permanently.
[**recommendationsDisableRecommendationForSubscription**](RecommendationsApi.md#recommendationsDisableRecommendationForSubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Web/recommendations/{name}/disable | Disables the specified rule so it will not apply to a subscription in the future.
[**recommendationsGetRuleDetailsByHostingEnvironment**](RecommendationsApi.md#recommendationsGetRuleDetailsByHostingEnvironment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{hostingEnvironmentName}/recommendations/{name} | Get a recommendation rule for an app.
[**recommendationsGetRuleDetailsByWebApp**](RecommendationsApi.md#recommendationsGetRuleDetailsByWebApp) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/recommendations/{name} | Get a recommendation rule for an app.
[**recommendationsList**](RecommendationsApi.md#recommendationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/recommendations | List all recommendations for a subscription.
[**recommendationsListHistoryForHostingEnvironment**](RecommendationsApi.md#recommendationsListHistoryForHostingEnvironment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{hostingEnvironmentName}/recommendationHistory | Get past recommendations for an app, optionally specified by the time range.
[**recommendationsListHistoryForWebApp**](RecommendationsApi.md#recommendationsListHistoryForWebApp) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/recommendationHistory | Get past recommendations for an app, optionally specified by the time range.
[**recommendationsListRecommendedRulesForHostingEnvironment**](RecommendationsApi.md#recommendationsListRecommendedRulesForHostingEnvironment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{hostingEnvironmentName}/recommendations | Get all recommendations for an app.
[**recommendationsListRecommendedRulesForWebApp**](RecommendationsApi.md#recommendationsListRecommendedRulesForWebApp) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/recommendations | Get all recommendations for an app.
[**recommendationsResetAllFilters**](RecommendationsApi.md#recommendationsResetAllFilters) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Web/recommendations/reset | Reset all recommendation opt-out settings for a subscription.
[**recommendationsResetAllFiltersForHostingEnvironment**](RecommendationsApi.md#recommendationsResetAllFiltersForHostingEnvironment) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{hostingEnvironmentName}/recommendations/reset | Reset all recommendation opt-out settings for an app.
[**recommendationsResetAllFiltersForWebApp**](RecommendationsApi.md#recommendationsResetAllFiltersForWebApp) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/recommendations/reset | Reset all recommendation opt-out settings for an app.



## recommendationsDisableAllForHostingEnvironment

> recommendationsDisableAllForHostingEnvironment(resourceGroupName, environmentName, hostingEnvironmentName, subscriptionId, apiVersion)

Disable all recommendations for an app.

Description for Disable all recommendations for an app.

### Example

```javascript
import RecommendationsApiClient from 'recommendations_api_client';
let defaultClient = RecommendationsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecommendationsApiClient.RecommendationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let environmentName = "environmentName_example"; // String | Name of the app.
let hostingEnvironmentName = "hostingEnvironmentName_example"; // String | 
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.recommendationsDisableAllForHostingEnvironment(resourceGroupName, environmentName, hostingEnvironmentName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **environmentName** | **String**| Name of the app. | 
 **hostingEnvironmentName** | **String**|  | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendationsDisableAllForWebApp

> recommendationsDisableAllForWebApp(resourceGroupName, siteName, subscriptionId, apiVersion)

Disable all recommendations for an app.

Description for Disable all recommendations for an app.

### Example

```javascript
import RecommendationsApiClient from 'recommendations_api_client';
let defaultClient = RecommendationsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecommendationsApiClient.RecommendationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.recommendationsDisableAllForWebApp(resourceGroupName, siteName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendationsDisableRecommendationForHostingEnvironment

> recommendationsDisableRecommendationForHostingEnvironment(resourceGroupName, environmentName, name, hostingEnvironmentName, subscriptionId, apiVersion)

Disables the specific rule for a web site permanently.

Description for Disables the specific rule for a web site permanently.

### Example

```javascript
import RecommendationsApiClient from 'recommendations_api_client';
let defaultClient = RecommendationsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecommendationsApiClient.RecommendationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let environmentName = "environmentName_example"; // String | Site name
let name = "name_example"; // String | Rule name
let hostingEnvironmentName = "hostingEnvironmentName_example"; // String | 
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.recommendationsDisableRecommendationForHostingEnvironment(resourceGroupName, environmentName, name, hostingEnvironmentName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **environmentName** | **String**| Site name | 
 **name** | **String**| Rule name | 
 **hostingEnvironmentName** | **String**|  | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendationsDisableRecommendationForSite

> recommendationsDisableRecommendationForSite(resourceGroupName, siteName, name, subscriptionId, apiVersion)

Disables the specific rule for a web site permanently.

Description for Disables the specific rule for a web site permanently.

### Example

```javascript
import RecommendationsApiClient from 'recommendations_api_client';
let defaultClient = RecommendationsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecommendationsApiClient.RecommendationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site name
let name = "name_example"; // String | Rule name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.recommendationsDisableRecommendationForSite(resourceGroupName, siteName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site name | 
 **name** | **String**| Rule name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendationsDisableRecommendationForSubscription

> recommendationsDisableRecommendationForSubscription(name, subscriptionId, apiVersion)

Disables the specified rule so it will not apply to a subscription in the future.

Description for Disables the specified rule so it will not apply to a subscription in the future.

### Example

```javascript
import RecommendationsApiClient from 'recommendations_api_client';
let defaultClient = RecommendationsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecommendationsApiClient.RecommendationsApi();
let name = "name_example"; // String | Rule name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.recommendationsDisableRecommendationForSubscription(name, subscriptionId, apiVersion, (error, data, response) => {
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
 **name** | **String**| Rule name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendationsGetRuleDetailsByHostingEnvironment

> RecommendationRule recommendationsGetRuleDetailsByHostingEnvironment(resourceGroupName, hostingEnvironmentName, name, subscriptionId, apiVersion, opts)

Get a recommendation rule for an app.

Description for Get a recommendation rule for an app.

### Example

```javascript
import RecommendationsApiClient from 'recommendations_api_client';
let defaultClient = RecommendationsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecommendationsApiClient.RecommendationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let hostingEnvironmentName = "hostingEnvironmentName_example"; // String | Name of the hosting environment.
let name = "name_example"; // String | Name of the recommendation.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'updateSeen': true, // Boolean | Specify <code>true</code> to update the last-seen timestamp of the recommendation object.
  'recommendationId': "recommendationId_example" // String | The GUID of the recommendation object if you query an expired one. You don't need to specify it to query an active entry.
};
apiInstance.recommendationsGetRuleDetailsByHostingEnvironment(resourceGroupName, hostingEnvironmentName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **hostingEnvironmentName** | **String**| Name of the hosting environment. | 
 **name** | **String**| Name of the recommendation. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **updateSeen** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to update the last-seen timestamp of the recommendation object. | [optional] 
 **recommendationId** | **String**| The GUID of the recommendation object if you query an expired one. You don&#39;t need to specify it to query an active entry. | [optional] 

### Return type

[**RecommendationRule**](RecommendationRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendationsGetRuleDetailsByWebApp

> RecommendationRule recommendationsGetRuleDetailsByWebApp(resourceGroupName, siteName, name, subscriptionId, apiVersion, opts)

Get a recommendation rule for an app.

Description for Get a recommendation rule for an app.

### Example

```javascript
import RecommendationsApiClient from 'recommendations_api_client';
let defaultClient = RecommendationsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecommendationsApiClient.RecommendationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Name of the app.
let name = "name_example"; // String | Name of the recommendation.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'updateSeen': true, // Boolean | Specify <code>true</code> to update the last-seen timestamp of the recommendation object.
  'recommendationId': "recommendationId_example" // String | The GUID of the recommendation object if you query an expired one. You don't need to specify it to query an active entry.
};
apiInstance.recommendationsGetRuleDetailsByWebApp(resourceGroupName, siteName, name, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Name of the app. | 
 **name** | **String**| Name of the recommendation. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **updateSeen** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to update the last-seen timestamp of the recommendation object. | [optional] 
 **recommendationId** | **String**| The GUID of the recommendation object if you query an expired one. You don&#39;t need to specify it to query an active entry. | [optional] 

### Return type

[**RecommendationRule**](RecommendationRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendationsList

> RecommendationCollection recommendationsList(subscriptionId, apiVersion, opts)

List all recommendations for a subscription.

Description for List all recommendations for a subscription.

### Example

```javascript
import RecommendationsApiClient from 'recommendations_api_client';
let defaultClient = RecommendationsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecommendationsApiClient.RecommendationsApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'featured': true, // Boolean | Specify <code>true</code> to return only the most critical recommendations. The default is <code>false</code>, which returns all recommendations.
  'filter': "filter_example" // String | Filter is specified by using OData syntax. Example: $filter=channel eq 'Api' or channel eq 'Notification' and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration'[PT1H|PT1M|P1D]
};
apiInstance.recommendationsList(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **featured** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to return only the most critical recommendations. The default is &lt;code&gt;false&lt;/code&gt;, which returns all recommendations. | [optional] 
 **filter** | **String**| Filter is specified by using OData syntax. Example: $filter&#x3D;channel eq &#39;Api&#39; or channel eq &#39;Notification&#39; and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[PT1H|PT1M|P1D] | [optional] 

### Return type

[**RecommendationCollection**](RecommendationCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendationsListHistoryForHostingEnvironment

> RecommendationCollection recommendationsListHistoryForHostingEnvironment(resourceGroupName, hostingEnvironmentName, subscriptionId, apiVersion, opts)

Get past recommendations for an app, optionally specified by the time range.

Description for Get past recommendations for an app, optionally specified by the time range.

### Example

```javascript
import RecommendationsApiClient from 'recommendations_api_client';
let defaultClient = RecommendationsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecommendationsApiClient.RecommendationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let hostingEnvironmentName = "hostingEnvironmentName_example"; // String | Name of the hosting environment.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'expiredOnly': true, // Boolean | Specify <code>false</code> to return all recommendations. The default is <code>true</code>, which returns only expired recommendations.
  'filter': "filter_example" // String | Filter is specified by using OData syntax. Example: $filter=channel eq 'Api' or channel eq 'Notification' and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration'[PT1H|PT1M|P1D]
};
apiInstance.recommendationsListHistoryForHostingEnvironment(resourceGroupName, hostingEnvironmentName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **hostingEnvironmentName** | **String**| Name of the hosting environment. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **expiredOnly** | **Boolean**| Specify &lt;code&gt;false&lt;/code&gt; to return all recommendations. The default is &lt;code&gt;true&lt;/code&gt;, which returns only expired recommendations. | [optional] 
 **filter** | **String**| Filter is specified by using OData syntax. Example: $filter&#x3D;channel eq &#39;Api&#39; or channel eq &#39;Notification&#39; and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[PT1H|PT1M|P1D] | [optional] 

### Return type

[**RecommendationCollection**](RecommendationCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendationsListHistoryForWebApp

> RecommendationCollection recommendationsListHistoryForWebApp(resourceGroupName, siteName, subscriptionId, apiVersion, opts)

Get past recommendations for an app, optionally specified by the time range.

Description for Get past recommendations for an app, optionally specified by the time range.

### Example

```javascript
import RecommendationsApiClient from 'recommendations_api_client';
let defaultClient = RecommendationsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecommendationsApiClient.RecommendationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'expiredOnly': true, // Boolean | Specify <code>false</code> to return all recommendations. The default is <code>true</code>, which returns only expired recommendations.
  'filter': "filter_example" // String | Filter is specified by using OData syntax. Example: $filter=channel eq 'Api' or channel eq 'Notification' and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration'[PT1H|PT1M|P1D]
};
apiInstance.recommendationsListHistoryForWebApp(resourceGroupName, siteName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **expiredOnly** | **Boolean**| Specify &lt;code&gt;false&lt;/code&gt; to return all recommendations. The default is &lt;code&gt;true&lt;/code&gt;, which returns only expired recommendations. | [optional] 
 **filter** | **String**| Filter is specified by using OData syntax. Example: $filter&#x3D;channel eq &#39;Api&#39; or channel eq &#39;Notification&#39; and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[PT1H|PT1M|P1D] | [optional] 

### Return type

[**RecommendationCollection**](RecommendationCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendationsListRecommendedRulesForHostingEnvironment

> RecommendationCollection recommendationsListRecommendedRulesForHostingEnvironment(resourceGroupName, hostingEnvironmentName, subscriptionId, apiVersion, opts)

Get all recommendations for an app.

Description for Get all recommendations for an app.

### Example

```javascript
import RecommendationsApiClient from 'recommendations_api_client';
let defaultClient = RecommendationsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecommendationsApiClient.RecommendationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let hostingEnvironmentName = "hostingEnvironmentName_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'featured': true, // Boolean | Specify <code>true</code> to return only the most critical recommendations. The default is <code>false</code>, which returns all recommendations.
  'filter': "filter_example" // String | Return only channels specified in the filter. Filter is specified by using OData syntax. Example: $filter=channel eq 'Api' or channel eq 'Notification'
};
apiInstance.recommendationsListRecommendedRulesForHostingEnvironment(resourceGroupName, hostingEnvironmentName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **hostingEnvironmentName** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **featured** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to return only the most critical recommendations. The default is &lt;code&gt;false&lt;/code&gt;, which returns all recommendations. | [optional] 
 **filter** | **String**| Return only channels specified in the filter. Filter is specified by using OData syntax. Example: $filter&#x3D;channel eq &#39;Api&#39; or channel eq &#39;Notification&#39; | [optional] 

### Return type

[**RecommendationCollection**](RecommendationCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendationsListRecommendedRulesForWebApp

> RecommendationCollection recommendationsListRecommendedRulesForWebApp(resourceGroupName, siteName, subscriptionId, apiVersion, opts)

Get all recommendations for an app.

Description for Get all recommendations for an app.

### Example

```javascript
import RecommendationsApiClient from 'recommendations_api_client';
let defaultClient = RecommendationsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecommendationsApiClient.RecommendationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'featured': true, // Boolean | Specify <code>true</code> to return only the most critical recommendations. The default is <code>false</code>, which returns all recommendations.
  'filter': "filter_example" // String | Return only channels specified in the filter. Filter is specified by using OData syntax. Example: $filter=channel eq 'Api' or channel eq 'Notification'
};
apiInstance.recommendationsListRecommendedRulesForWebApp(resourceGroupName, siteName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **featured** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to return only the most critical recommendations. The default is &lt;code&gt;false&lt;/code&gt;, which returns all recommendations. | [optional] 
 **filter** | **String**| Return only channels specified in the filter. Filter is specified by using OData syntax. Example: $filter&#x3D;channel eq &#39;Api&#39; or channel eq &#39;Notification&#39; | [optional] 

### Return type

[**RecommendationCollection**](RecommendationCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendationsResetAllFilters

> recommendationsResetAllFilters(subscriptionId, apiVersion)

Reset all recommendation opt-out settings for a subscription.

Description for Reset all recommendation opt-out settings for a subscription.

### Example

```javascript
import RecommendationsApiClient from 'recommendations_api_client';
let defaultClient = RecommendationsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecommendationsApiClient.RecommendationsApi();
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.recommendationsResetAllFilters(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendationsResetAllFiltersForHostingEnvironment

> recommendationsResetAllFiltersForHostingEnvironment(resourceGroupName, environmentName, hostingEnvironmentName, subscriptionId, apiVersion)

Reset all recommendation opt-out settings for an app.

Description for Reset all recommendation opt-out settings for an app.

### Example

```javascript
import RecommendationsApiClient from 'recommendations_api_client';
let defaultClient = RecommendationsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecommendationsApiClient.RecommendationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let environmentName = "environmentName_example"; // String | Name of the app.
let hostingEnvironmentName = "hostingEnvironmentName_example"; // String | 
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.recommendationsResetAllFiltersForHostingEnvironment(resourceGroupName, environmentName, hostingEnvironmentName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **environmentName** | **String**| Name of the app. | 
 **hostingEnvironmentName** | **String**|  | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendationsResetAllFiltersForWebApp

> recommendationsResetAllFiltersForWebApp(resourceGroupName, siteName, subscriptionId, apiVersion)

Reset all recommendation opt-out settings for an app.

Description for Reset all recommendation opt-out settings for an app.

### Example

```javascript
import RecommendationsApiClient from 'recommendations_api_client';
let defaultClient = RecommendationsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecommendationsApiClient.RecommendationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Name of the app.
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.recommendationsResetAllFiltersForWebApp(resourceGroupName, siteName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Name of the app. | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

