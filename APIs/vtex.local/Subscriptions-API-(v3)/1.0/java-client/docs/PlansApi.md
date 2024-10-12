# PlansApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiRnsPvtPlansGet**](PlansApi.md#apiRnsPvtPlansGet) | **GET** /api/rns/pvt/plans | List plans |
| [**apiRnsPvtPlansIdGet**](PlansApi.md#apiRnsPvtPlansIdGet) | **GET** /api/rns/pvt/plans/{id} | Get plan details |


<a id="apiRnsPvtPlansGet"></a>
# **apiRnsPvtPlansGet**
> List&lt;StorePlan&gt; apiRnsPvtPlansGet(contentType, accept, periodicity, interval, page, size)

List plans

List plans filtering by some arguments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlansApi;

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

    PlansApi apiInstance = new PlansApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String periodicity = "periodicity_example"; // String | Filter plans by available periodicity
    String interval = "interval_example"; // String | Filter plans by available interval
    Integer page = 1; // Integer | Page used for pagination
    Integer size = 15; // Integer | Page size used for pagination
    try {
      List<StorePlan> result = apiInstance.apiRnsPvtPlansGet(contentType, accept, periodicity, interval, page, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlansApi#apiRnsPvtPlansGet");
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
| **periodicity** | **String**| Filter plans by available periodicity | [optional] |
| **interval** | **String**| Filter plans by available interval | [optional] |
| **page** | **Integer**| Page used for pagination | [optional] [default to 1] |
| **size** | **Integer**| Page size used for pagination | [optional] [default to 15] |

### Return type

[**List&lt;StorePlan&gt;**](StorePlan.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Requested plans |  -  |

<a id="apiRnsPvtPlansIdGet"></a>
# **apiRnsPvtPlansIdGet**
> StorePlan apiRnsPvtPlansIdGet(id, contentType, accept)

Get plan details

This endpoint retrieves a specific plan by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlansApi;

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

    PlansApi apiInstance = new PlansApi(defaultClient);
    String id = "id_example"; // String | Id from the desired plan
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      StorePlan result = apiInstance.apiRnsPvtPlansIdGet(id, contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlansApi#apiRnsPvtPlansIdGet");
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
| **id** | **String**| Id from the desired plan | |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |

### Return type

[**StorePlan**](StorePlan.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Requested plan |  -  |

