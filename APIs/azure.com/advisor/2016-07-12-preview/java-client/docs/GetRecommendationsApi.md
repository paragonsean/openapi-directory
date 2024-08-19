# GetRecommendationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**recommendationsGet**](GetRecommendationsApi.md#recommendationsGet) | **GET** /{resourceUri}/providers/Microsoft.Advisor/recommendations/{recommendationId} |  |
| [**recommendationsList**](GetRecommendationsApi.md#recommendationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Advisor/recommendations |  |


<a id="recommendationsGet"></a>
# **recommendationsGet**
> ResourceRecommendationBase recommendationsGet(resourceUri, recommendationId, apiVersion)



Obtains details of a cached recommendation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetRecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetRecommendationsApi apiInstance = new GetRecommendationsApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies.
    String recommendationId = "recommendationId_example"; // String | The recommendation ID.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    try {
      ResourceRecommendationBase result = apiInstance.recommendationsGet(resourceUri, recommendationId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetRecommendationsApi#recommendationsGet");
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
| **resourceUri** | **String**| The fully qualified Azure Resource Manager identifier of the resource to which the recommendation applies. | |
| **recommendationId** | **String**| The recommendation ID. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |

### Return type

[**ResourceRecommendationBase**](ResourceRecommendationBase.md)

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
> ResourceRecommendationBaseListResult recommendationsList(subscriptionId, apiVersion, $filter, $top, $skipToken)



Obtains cached recommendations for a subscription. The recommendations are generated or computed by invoking generateRecommendations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetRecommendationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    GetRecommendationsApi apiInstance = new GetRecommendationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
    String apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
    String $filter = "$filter_example"; // String | The filter to apply to the recommendations.
    Integer $top = 56; // Integer | The number of recommendations per page if a paged version of this API is being used.
    String $skipToken = "$skipToken_example"; // String | The page-continuation token to use with a paged version of this API.
    try {
      ResourceRecommendationBaseListResult result = apiInstance.recommendationsList(subscriptionId, apiVersion, $filter, $top, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetRecommendationsApi#recommendationsList");
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
| **subscriptionId** | **String**| The Azure subscription ID. | |
| **apiVersion** | **String**| The version of the API to be used with the client request. | |
| **$filter** | **String**| The filter to apply to the recommendations. | [optional] |
| **$top** | **Integer**| The number of recommendations per page if a paged version of this API is being used. | [optional] |
| **$skipToken** | **String**| The page-continuation token to use with a paged version of this API. | [optional] |

### Return type

[**ResourceRecommendationBaseListResult**](ResourceRecommendationBaseListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |

