# WebSiteManagementClient.RecommendationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recommendationsGetRecommendationBySubscription**](RecommendationsApi.md#recommendationsGetRecommendationBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/recommendations | Gets a list of recommendations associated with the specified subscription.
[**recommendationsGetRecommendationHistoryForSite**](RecommendationsApi.md#recommendationsGetRecommendationHistoryForSite) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/recommendationHistory | Gets the list of past recommendations optionally specified by the time range.
[**recommendationsGetRecommendedRulesForSite**](RecommendationsApi.md#recommendationsGetRecommendedRulesForSite) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/recommendations | Gets a list of recommendations associated with the specified web site.
[**recommendationsGetRuleDetailsBySiteName**](RecommendationsApi.md#recommendationsGetRuleDetailsBySiteName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/recommendations/{name} | Gets the detailed properties of the recommendation object for the specified web site.



## recommendationsGetRecommendationBySubscription

> [Recommendation] recommendationsGetRecommendationBySubscription(subscriptionId, apiVersion, opts)

Gets a list of recommendations associated with the specified subscription.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.RecommendationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'featured': true, // Boolean | If set, this API returns only the most critical recommendation among the others. Otherwise this API returns all recommendations available
  'filter': "filter_example" // String | Return only channels specified in the filter. Filter is specified by using OData syntax. Example: $filter=channels eq 'Api' or channel eq 'Notification'
};
apiInstance.recommendationsGetRecommendationBySubscription(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **featured** | **Boolean**| If set, this API returns only the most critical recommendation among the others. Otherwise this API returns all recommendations available | [optional] 
 **filter** | **String**| Return only channels specified in the filter. Filter is specified by using OData syntax. Example: $filter&#x3D;channels eq &#39;Api&#39; or channel eq &#39;Notification&#39; | [optional] 

### Return type

[**[Recommendation]**](Recommendation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## recommendationsGetRecommendationHistoryForSite

> [Recommendation] recommendationsGetRecommendationHistoryForSite(resourceGroupName, siteName, subscriptionId, apiVersion, opts)

Gets the list of past recommendations optionally specified by the time range.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.RecommendationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name
let siteName = "siteName_example"; // String | Site name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'startTime': "startTime_example", // String | The start time of a time range to query, e.g. $filter=startTime eq '2015-01-01T00:00:00Z' and endTime eq '2015-01-02T00:00:00Z'
  'endTime': "endTime_example" // String | The end time of a time range to query, e.g. $filter=startTime eq '2015-01-01T00:00:00Z' and endTime eq '2015-01-02T00:00:00Z'
};
apiInstance.recommendationsGetRecommendationHistoryForSite(resourceGroupName, siteName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Resource group name | 
 **siteName** | **String**| Site name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **startTime** | **String**| The start time of a time range to query, e.g. $filter&#x3D;startTime eq &#39;2015-01-01T00:00:00Z&#39; and endTime eq &#39;2015-01-02T00:00:00Z&#39; | [optional] 
 **endTime** | **String**| The end time of a time range to query, e.g. $filter&#x3D;startTime eq &#39;2015-01-01T00:00:00Z&#39; and endTime eq &#39;2015-01-02T00:00:00Z&#39; | [optional] 

### Return type

[**[Recommendation]**](Recommendation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## recommendationsGetRecommendedRulesForSite

> [Recommendation] recommendationsGetRecommendedRulesForSite(resourceGroupName, siteName, subscriptionId, apiVersion, opts)

Gets a list of recommendations associated with the specified web site.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.RecommendationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name
let siteName = "siteName_example"; // String | Site name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'featured': true, // Boolean | If set, this API returns only the most critical recommendation among the others. Otherwise this API returns all recommendations available
  'siteSku': "siteSku_example", // String | The name of site SKU.
  'numSlots': 56 // Number | The number of site slots associated to the site
};
apiInstance.recommendationsGetRecommendedRulesForSite(resourceGroupName, siteName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Resource group name | 
 **siteName** | **String**| Site name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **featured** | **Boolean**| If set, this API returns only the most critical recommendation among the others. Otherwise this API returns all recommendations available | [optional] 
 **siteSku** | **String**| The name of site SKU. | [optional] 
 **numSlots** | **Number**| The number of site slots associated to the site | [optional] 

### Return type

[**[Recommendation]**](Recommendation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## recommendationsGetRuleDetailsBySiteName

> RecommendationRule recommendationsGetRuleDetailsBySiteName(resourceGroupName, siteName, name, subscriptionId, apiVersion)

Gets the detailed properties of the recommendation object for the specified web site.

### Example

```javascript
import WebSiteManagementClient from 'web_site_management_client';
let defaultClient = WebSiteManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new WebSiteManagementClient.RecommendationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name
let siteName = "siteName_example"; // String | Site name
let name = "name_example"; // String | Recommendation rule name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.recommendationsGetRuleDetailsBySiteName(resourceGroupName, siteName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Resource group name | 
 **siteName** | **String**| Site name | 
 **name** | **String**| Recommendation rule name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**RecommendationRule**](RecommendationRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

