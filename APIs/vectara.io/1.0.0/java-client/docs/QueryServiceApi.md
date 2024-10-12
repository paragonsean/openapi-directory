# QueryServiceApi

All URIs are relative to *https://api.vectara.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**query**](QueryServiceApi.md#query) | **POST** /v1/query |  |
| [**streamQuery**](QueryServiceApi.md#streamQuery) | **POST** /v1/stream-query |  |


<a id="query"></a>
# **query**
> ServingBatchQueryResponse query(customerId, servingBatchQueryRequest)



Query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vectara.io");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oAuth
    OAuth oAuth = (OAuth) defaultClient.getAuthentication("oAuth");
    oAuth.setAccessToken("YOUR ACCESS TOKEN");

    QueryServiceApi apiInstance = new QueryServiceApi(defaultClient);
    Integer customerId = 56; // Integer | The Customer ID to use for the request.
    ServingBatchQueryRequest servingBatchQueryRequest = new ServingBatchQueryRequest(); // ServingBatchQueryRequest | 
    try {
      ServingBatchQueryResponse result = apiInstance.query(customerId, servingBatchQueryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryServiceApi#query");
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
| **customerId** | **Integer**| The Customer ID to use for the request. | |
| **servingBatchQueryRequest** | [**ServingBatchQueryRequest**](ServingBatchQueryRequest.md)|  | |

### Return type

[**ServingBatchQueryResponse**](ServingBatchQueryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a id="streamQuery"></a>
# **streamQuery**
> StreamResultOfServingResponseSet streamQuery(customerId, servingBatchQueryRequest)



Stream Query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vectara.io");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oAuth
    OAuth oAuth = (OAuth) defaultClient.getAuthentication("oAuth");
    oAuth.setAccessToken("YOUR ACCESS TOKEN");

    QueryServiceApi apiInstance = new QueryServiceApi(defaultClient);
    Integer customerId = 56; // Integer | The Customer ID to use for the request.
    ServingBatchQueryRequest servingBatchQueryRequest = new ServingBatchQueryRequest(); // ServingBatchQueryRequest | 
    try {
      StreamResultOfServingResponseSet result = apiInstance.streamQuery(customerId, servingBatchQueryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryServiceApi#streamQuery");
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
| **customerId** | **Integer**| The Customer ID to use for the request. | |
| **servingBatchQueryRequest** | [**ServingBatchQueryRequest**](ServingBatchQueryRequest.md)|  | |

### Return type

[**StreamResultOfServingResponseSet**](StreamResultOfServingResponseSet.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response.(streaming responses) |  -  |
| **0** | An unexpected error response. |  -  |

