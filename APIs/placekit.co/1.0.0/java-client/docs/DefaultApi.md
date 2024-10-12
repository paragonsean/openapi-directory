# DefaultApi

All URIs are relative to *https://api.placekit.co*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reverse**](DefaultApi.md#reverse) | **POST** /reverse | Reverse geocoding |
| [**search**](DefaultApi.md#search) | **POST** /search | Search for addresses |


<a id="reverse"></a>
# **reverse**
> Results reverse(payload)

Reverse geocoding

Performs a reverse geocoding search.  It will return the closest results around &#x60;coordinates&#x60;.\\ If &#x60;coordinates&#x60; are not set, it will use the user&#39;s IP to approximate its coordinates but results will be less accurate (city level accuracy instead of street level accuracy). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.placekit.co");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    ReverseRequest payload = new ReverseRequest(); // ReverseRequest | Request parameters
    try {
      Results result = apiInstance.reverse(payload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#reverse");
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
| **payload** | [**ReverseRequest**](ReverseRequest.md)| Request parameters | [optional] |

### Return type

[**Results**](Results.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** |  |  -  |
| **403** |  |  -  |
| **404** |  |  -  |
| **412** |  |  -  |
| **422** |  |  -  |
| **429** |  |  -  |

<a id="search"></a>
# **search**
> Results search(payload)

Search for addresses

Performs a forward geocoding search.  It will return results around &#x60;coordinates&#x60; (if provided) and the best matching textual relevance.  **It is highly recommended** to set the &#x60;countries&#x60; parameter with the country you need results from for the best accuracy and revelance possible. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.placekit.co");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SearchRequest payload = new SearchRequest(); // SearchRequest | Request parameters
    try {
      Results result = apiInstance.search(payload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#search");
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
| **payload** | [**SearchRequest**](SearchRequest.md)| Request parameters | [optional] |

### Return type

[**Results**](Results.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** |  |  -  |
| **403** |  |  -  |
| **404** |  |  -  |
| **412** |  |  -  |
| **422** |  |  -  |
| **429** |  |  -  |

