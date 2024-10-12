# CyclesApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiRnsPubCyclesCycleIdGet**](CyclesApi.md#apiRnsPubCyclesCycleIdGet) | **GET** /api/rns/pub/cycles/{cycleId} | Get cycle details |
| [**apiRnsPubCyclesCycleIdRetryPost**](CyclesApi.md#apiRnsPubCyclesCycleIdRetryPost) | **POST** /api/rns/pub/cycles/{cycleId}/retry | Retry cycle |
| [**apiRnsPubCyclesGet**](CyclesApi.md#apiRnsPubCyclesGet) | **GET** /api/rns/pub/cycles | List cycles |


<a id="apiRnsPubCyclesCycleIdGet"></a>
# **apiRnsPubCyclesCycleIdGet**
> SubscriptionCycleResponse apiRnsPubCyclesCycleIdGet(cycleId, contentType, accept)

Get cycle details

Retrieve a specific cycle by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CyclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    CyclesApi apiInstance = new CyclesApi(defaultClient);
    String cycleId = "cycleId_example"; // String | ID from the desired cycle.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      SubscriptionCycleResponse result = apiInstance.apiRnsPubCyclesCycleIdGet(cycleId, contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CyclesApi#apiRnsPubCyclesCycleIdGet");
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
| **cycleId** | **String**| ID from the desired cycle. | |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |

### Return type

[**SubscriptionCycleResponse**](SubscriptionCycleResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiRnsPubCyclesCycleIdRetryPost"></a>
# **apiRnsPubCyclesCycleIdRetryPost**
> apiRnsPubCyclesCycleIdRetryPost(cycleId, contentType, accept)

Retry cycle

Every subscription order has an execution count called cycle, which determines the position of an order counting from when the shopper subscribed. This endpoint reruns a cycle that is currently in error state.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CyclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    CyclesApi apiInstance = new CyclesApi(defaultClient);
    String cycleId = "cycleId_example"; // String | Id from the cycle that will be retried
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      apiInstance.apiRnsPubCyclesCycleIdRetryPost(cycleId, contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling CyclesApi#apiRnsPubCyclesCycleIdRetryPost");
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
| **cycleId** | **String**| Id from the cycle that will be retried | |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiRnsPubCyclesGet"></a>
# **apiRnsPubCyclesGet**
> List&lt;SubscriptionCycleResponse&gt; apiRnsPubCyclesGet(contentType, accept, beginDate, endDate, subscriptionId, customerEmail, status, page, size)

List cycles

List cycles filtering by some arguments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CyclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    CyclesApi apiInstance = new CyclesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String beginDate = "beginDate_example"; // String | Lower limit for the date of creation of the cycle
    String endDate = "endDate_example"; // String | Upper limit for the date of creation of the cycle
    String subscriptionId = "subscriptionId_example"; // String | Id from the subscription that generated the cycle
    String customerEmail = "customerEmail_example"; // String | Customer that owns the subscription. Defaults to the current logged user
    String status = "status_example"; // String | Current cycle status
    Integer page = 1; // Integer | Page used for pagination
    Integer size = 15; // Integer | Page size used for pagination
    try {
      List<SubscriptionCycleResponse> result = apiInstance.apiRnsPubCyclesGet(contentType, accept, beginDate, endDate, subscriptionId, customerEmail, status, page, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CyclesApi#apiRnsPubCyclesGet");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **beginDate** | **String**| Lower limit for the date of creation of the cycle | [optional] |
| **endDate** | **String**| Upper limit for the date of creation of the cycle | [optional] |
| **subscriptionId** | **String**| Id from the subscription that generated the cycle | [optional] |
| **customerEmail** | **String**| Customer that owns the subscription. Defaults to the current logged user | [optional] |
| **status** | **String**| Current cycle status | [optional] |
| **page** | **Integer**| Page used for pagination | [optional] [default to 1] |
| **size** | **Integer**| Page size used for pagination | [optional] [default to 15] |

### Return type

[**List&lt;SubscriptionCycleResponse&gt;**](SubscriptionCycleResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

