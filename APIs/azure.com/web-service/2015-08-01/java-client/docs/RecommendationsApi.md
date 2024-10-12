# RecommendationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**recommendationsGetRecommendationBySubscription**](RecommendationsApi.md#recommendationsGetRecommendationBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/recommendations | Gets a list of recommendations associated with the specified subscription. |
| [**recommendationsGetRecommendationHistoryForSite**](RecommendationsApi.md#recommendationsGetRecommendationHistoryForSite) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/recommendationHistory | Gets the list of past recommendations optionally specified by the time range. |
| [**recommendationsGetRecommendedRulesForSite**](RecommendationsApi.md#recommendationsGetRecommendedRulesForSite) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/recommendations | Gets a list of recommendations associated with the specified web site. |
| [**recommendationsGetRuleDetailsBySiteName**](RecommendationsApi.md#recommendationsGetRuleDetailsBySiteName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/recommendations/{name} | Gets the detailed properties of the recommendation object for the specified web site. |


<a id="recommendationsGetRecommendationBySubscription"></a>
# **recommendationsGetRecommendationBySubscription**
> List&lt;Recommendation&gt; recommendationsGetRecommendationBySubscription(subscriptionId, apiVersion, featured, $filter)

Gets a list of recommendations associated with the specified subscription.

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
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean featured = true; // Boolean | If set, this API returns only the most critical recommendation among the others. Otherwise this API returns all recommendations available
    String $filter = "$filter_example"; // String | Return only channels specified in the filter. Filter is specified by using OData syntax. Example: $filter=channels eq 'Api' or channel eq 'Notification'
    try {
      List<Recommendation> result = apiInstance.recommendationsGetRecommendationBySubscription(subscriptionId, apiVersion, featured, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendationsApi#recommendationsGetRecommendationBySubscription");
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
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **featured** | **Boolean**| If set, this API returns only the most critical recommendation among the others. Otherwise this API returns all recommendations available | [optional] |
| **$filter** | **String**| Return only channels specified in the filter. Filter is specified by using OData syntax. Example: $filter&#x3D;channels eq &#39;Api&#39; or channel eq &#39;Notification&#39; | [optional] |

### Return type

[**List&lt;Recommendation&gt;**](Recommendation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recommendationsGetRecommendationHistoryForSite"></a>
# **recommendationsGetRecommendationHistoryForSite**
> List&lt;Recommendation&gt; recommendationsGetRecommendationHistoryForSite(resourceGroupName, siteName, subscriptionId, apiVersion, startTime, endTime)

Gets the list of past recommendations optionally specified by the time range.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name
    String siteName = "siteName_example"; // String | Site name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    String startTime = "startTime_example"; // String | The start time of a time range to query, e.g. $filter=startTime eq '2015-01-01T00:00:00Z' and endTime eq '2015-01-02T00:00:00Z'
    String endTime = "endTime_example"; // String | The end time of a time range to query, e.g. $filter=startTime eq '2015-01-01T00:00:00Z' and endTime eq '2015-01-02T00:00:00Z'
    try {
      List<Recommendation> result = apiInstance.recommendationsGetRecommendationHistoryForSite(resourceGroupName, siteName, subscriptionId, apiVersion, startTime, endTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendationsApi#recommendationsGetRecommendationHistoryForSite");
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
| **resourceGroupName** | **String**| Resource group name | |
| **siteName** | **String**| Site name | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **startTime** | **String**| The start time of a time range to query, e.g. $filter&#x3D;startTime eq &#39;2015-01-01T00:00:00Z&#39; and endTime eq &#39;2015-01-02T00:00:00Z&#39; | [optional] |
| **endTime** | **String**| The end time of a time range to query, e.g. $filter&#x3D;startTime eq &#39;2015-01-01T00:00:00Z&#39; and endTime eq &#39;2015-01-02T00:00:00Z&#39; | [optional] |

### Return type

[**List&lt;Recommendation&gt;**](Recommendation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recommendationsGetRecommendedRulesForSite"></a>
# **recommendationsGetRecommendedRulesForSite**
> List&lt;Recommendation&gt; recommendationsGetRecommendedRulesForSite(resourceGroupName, siteName, subscriptionId, apiVersion, featured, siteSku, numSlots)

Gets a list of recommendations associated with the specified web site.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name
    String siteName = "siteName_example"; // String | Site name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean featured = true; // Boolean | If set, this API returns only the most critical recommendation among the others. Otherwise this API returns all recommendations available
    String siteSku = "siteSku_example"; // String | The name of site SKU.
    Integer numSlots = 56; // Integer | The number of site slots associated to the site
    try {
      List<Recommendation> result = apiInstance.recommendationsGetRecommendedRulesForSite(resourceGroupName, siteName, subscriptionId, apiVersion, featured, siteSku, numSlots);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendationsApi#recommendationsGetRecommendedRulesForSite");
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
| **resourceGroupName** | **String**| Resource group name | |
| **siteName** | **String**| Site name | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **featured** | **Boolean**| If set, this API returns only the most critical recommendation among the others. Otherwise this API returns all recommendations available | [optional] |
| **siteSku** | **String**| The name of site SKU. | [optional] |
| **numSlots** | **Integer**| The number of site slots associated to the site | [optional] |

### Return type

[**List&lt;Recommendation&gt;**](Recommendation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recommendationsGetRuleDetailsBySiteName"></a>
# **recommendationsGetRuleDetailsBySiteName**
> RecommendationRule recommendationsGetRuleDetailsBySiteName(resourceGroupName, siteName, name, subscriptionId, apiVersion)

Gets the detailed properties of the recommendation object for the specified web site.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group name
    String siteName = "siteName_example"; // String | Site name
    String name = "name_example"; // String | Recommendation rule name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      RecommendationRule result = apiInstance.recommendationsGetRuleDetailsBySiteName(resourceGroupName, siteName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecommendationsApi#recommendationsGetRuleDetailsBySiteName");
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
| **resourceGroupName** | **String**| Resource group name | |
| **siteName** | **String**| Site name | |
| **name** | **String**| Recommendation rule name | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**RecommendationRule**](RecommendationRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

