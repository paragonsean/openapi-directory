# RecommendationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**recommendationsDisableAllForWebApp**](RecommendationsApi.md#recommendationsDisableAllForWebApp) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/recommendations/disable | Disable all recommendations for an app. |
| [**recommendationsDisableRecommendationForSite**](RecommendationsApi.md#recommendationsDisableRecommendationForSite) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/recommendations/{name}/disable | Disables the specific rule for a web site permanently. |
| [**recommendationsDisableRecommendationForSubscription**](RecommendationsApi.md#recommendationsDisableRecommendationForSubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Web/recommendations/{name}/disable | Disables the specified rule so it will not apply to a subscription in the future. |
| [**recommendationsGetRuleDetailsByWebApp**](RecommendationsApi.md#recommendationsGetRuleDetailsByWebApp) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/recommendations/{name} | Get a recommendation rule for an app. |
| [**recommendationsList**](RecommendationsApi.md#recommendationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/recommendations | List all recommendations for a subscription. |
| [**recommendationsListHistoryForWebApp**](RecommendationsApi.md#recommendationsListHistoryForWebApp) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/recommendationHistory | Get past recommendations for an app, optionally specified by the time range. |
| [**recommendationsListRecommendedRulesForWebApp**](RecommendationsApi.md#recommendationsListRecommendedRulesForWebApp) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/recommendations | Get all recommendations for an app. |
| [**recommendationsResetAllFilters**](RecommendationsApi.md#recommendationsResetAllFilters) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Web/recommendations/reset | Reset all recommendation opt-out settings for a subscription. |
| [**recommendationsResetAllFiltersForWebApp**](RecommendationsApi.md#recommendationsResetAllFiltersForWebApp) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/recommendations/reset | Reset all recommendation opt-out settings for an app. |


<a id="recommendationsDisableAllForWebApp"></a>
# **recommendationsDisableAllForWebApp**
> recommendationsDisableAllForWebApp(resourceGroupName, siteName, subscriptionId, apiVersion)

Disable all recommendations for an app.

Disable all recommendations for an app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecommendationsApi apiInstance = new RecommendationsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Name of the app.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      apiInstance.recommendationsDisableAllForWebApp(resourceGroupName, siteName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendationsApi#recommendationsDisableAllForWebApp");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Name of the app. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="recommendationsDisableRecommendationForSite"></a>
# **recommendationsDisableRecommendationForSite**
> recommendationsDisableRecommendationForSite(resourceGroupName, siteName, name, subscriptionId, apiVersion)

Disables the specific rule for a web site permanently.

Disables the specific rule for a web site permanently.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecommendationsApi apiInstance = new RecommendationsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Site name
    String name = "name_example"; // String | Rule name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      apiInstance.recommendationsDisableRecommendationForSite(resourceGroupName, siteName, name, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendationsApi#recommendationsDisableRecommendationForSite");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Site name | |
| **name** | **String**| Rule name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully disabled recommendations. |  -  |

<a id="recommendationsDisableRecommendationForSubscription"></a>
# **recommendationsDisableRecommendationForSubscription**
> recommendationsDisableRecommendationForSubscription(name, subscriptionId, apiVersion)

Disables the specified rule so it will not apply to a subscription in the future.

Disables the specified rule so it will not apply to a subscription in the future.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecommendationsApi apiInstance = new RecommendationsApi(defaultClient);
    String name = "name_example"; // String | Rule name
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      apiInstance.recommendationsDisableRecommendationForSubscription(name, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendationsApi#recommendationsDisableRecommendationForSubscription");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| Rule name | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully disabled recommendations. |  -  |

<a id="recommendationsGetRuleDetailsByWebApp"></a>
# **recommendationsGetRuleDetailsByWebApp**
> RecommendationRule recommendationsGetRuleDetailsByWebApp(resourceGroupName, siteName, name, subscriptionId, apiVersion, updateSeen, recommendationId)

Get a recommendation rule for an app.

Get a recommendation rule for an app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecommendationsApi apiInstance = new RecommendationsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Name of the app.
    String name = "name_example"; // String | Name of the recommendation.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean updateSeen = true; // Boolean | Specify <code>true</code> to update the last-seen timestamp of the recommendation object.
    String recommendationId = "recommendationId_example"; // String | The GUID of the recommendation object if you query an expired one. You don't need to specify it to query an active entry.
    try {
      RecommendationRule result = apiInstance.recommendationsGetRuleDetailsByWebApp(resourceGroupName, siteName, name, subscriptionId, apiVersion, updateSeen, recommendationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendationsApi#recommendationsGetRuleDetailsByWebApp");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Name of the app. | |
| **name** | **String**| Name of the recommendation. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **updateSeen** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to update the last-seen timestamp of the recommendation object. | [optional] |
| **recommendationId** | **String**| The GUID of the recommendation object if you query an expired one. You don&#39;t need to specify it to query an active entry. | [optional] |

### Return type

[**RecommendationRule**](RecommendationRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recommendationsList"></a>
# **recommendationsList**
> RecommendationCollection recommendationsList(subscriptionId, apiVersion, featured, $filter)

List all recommendations for a subscription.

List all recommendations for a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecommendationsApi apiInstance = new RecommendationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean featured = true; // Boolean | Specify <code>true</code> to return only the most critical recommendations. The default is <code>false</code>, which returns all recommendations.
    String $filter = "$filter_example"; // String | Filter is specified by using OData syntax. Example: $filter=channels eq 'Api' or channel eq 'Notification' and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[PT1H|PT1M|P1D]
    try {
      RecommendationCollection result = apiInstance.recommendationsList(subscriptionId, apiVersion, featured, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendationsApi#recommendationsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **featured** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to return only the most critical recommendations. The default is &lt;code&gt;false&lt;/code&gt;, which returns all recommendations. | [optional] |
| **$filter** | **String**| Filter is specified by using OData syntax. Example: $filter&#x3D;channels eq &#39;Api&#39; or channel eq &#39;Notification&#39; and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[PT1H|PT1M|P1D] | [optional] |

### Return type

[**RecommendationCollection**](RecommendationCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recommendationsListHistoryForWebApp"></a>
# **recommendationsListHistoryForWebApp**
> RecommendationCollection recommendationsListHistoryForWebApp(resourceGroupName, siteName, subscriptionId, apiVersion, $filter)

Get past recommendations for an app, optionally specified by the time range.

Get past recommendations for an app, optionally specified by the time range.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecommendationsApi apiInstance = new RecommendationsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Name of the app.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    String $filter = "$filter_example"; // String | Filter is specified by using OData syntax. Example: $filter=channels eq 'Api' or channel eq 'Notification' and startTime eq '2014-01-01T00:00:00Z' and endTime eq '2014-12-31T23:59:59Z' and timeGrain eq duration'[PT1H|PT1M|P1D]
    try {
      RecommendationCollection result = apiInstance.recommendationsListHistoryForWebApp(resourceGroupName, siteName, subscriptionId, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendationsApi#recommendationsListHistoryForWebApp");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Name of the app. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **$filter** | **String**| Filter is specified by using OData syntax. Example: $filter&#x3D;channels eq &#39;Api&#39; or channel eq &#39;Notification&#39; and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[PT1H|PT1M|P1D] | [optional] |

### Return type

[**RecommendationCollection**](RecommendationCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recommendationsListRecommendedRulesForWebApp"></a>
# **recommendationsListRecommendedRulesForWebApp**
> RecommendationCollection recommendationsListRecommendedRulesForWebApp(resourceGroupName, siteName, subscriptionId, apiVersion, featured, $filter)

Get all recommendations for an app.

Get all recommendations for an app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecommendationsApi apiInstance = new RecommendationsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Name of the app.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean featured = true; // Boolean | Specify <code>true</code> to return only the most critical recommendations. The default is <code>false</code>, which returns all recommendations.
    String $filter = "$filter_example"; // String | Return only channels specified in the filter. Filter is specified by using OData syntax. Example: $filter=channels eq 'Api' or channel eq 'Notification'
    try {
      RecommendationCollection result = apiInstance.recommendationsListRecommendedRulesForWebApp(resourceGroupName, siteName, subscriptionId, apiVersion, featured, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendationsApi#recommendationsListRecommendedRulesForWebApp");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Name of the app. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **featured** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; to return only the most critical recommendations. The default is &lt;code&gt;false&lt;/code&gt;, which returns all recommendations. | [optional] |
| **$filter** | **String**| Return only channels specified in the filter. Filter is specified by using OData syntax. Example: $filter&#x3D;channels eq &#39;Api&#39; or channel eq &#39;Notification&#39; | [optional] |

### Return type

[**RecommendationCollection**](RecommendationCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recommendationsResetAllFilters"></a>
# **recommendationsResetAllFilters**
> recommendationsResetAllFilters(subscriptionId, apiVersion)

Reset all recommendation opt-out settings for a subscription.

Reset all recommendation opt-out settings for a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecommendationsApi apiInstance = new RecommendationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      apiInstance.recommendationsResetAllFilters(subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendationsApi#recommendationsResetAllFilters");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="recommendationsResetAllFiltersForWebApp"></a>
# **recommendationsResetAllFiltersForWebApp**
> recommendationsResetAllFiltersForWebApp(resourceGroupName, siteName, subscriptionId, apiVersion)

Reset all recommendation opt-out settings for an app.

Reset all recommendation opt-out settings for an app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    RecommendationsApi apiInstance = new RecommendationsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String siteName = "siteName_example"; // String | Name of the app.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      apiInstance.recommendationsResetAllFiltersForWebApp(resourceGroupName, siteName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendationsApi#recommendationsResetAllFiltersForWebApp");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **siteName** | **String**| Name of the app. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

