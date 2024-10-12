# PublisherApi

All URIs are relative to *https://api.isbndb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**publisherNameGet**](PublisherApi.md#publisherNameGet) | **GET** /publisher/{name} | Gets publisher details |
| [**publishersQueryGet**](PublisherApi.md#publishersQueryGet) | **GET** /publishers/{query} | Search publishers |


<a id="publisherNameGet"></a>
# **publisherNameGet**
> Publisher publisherNameGet(name, page, pageSize)

Gets publisher details

Returns details and a list of books by the publisher.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublisherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.isbndb.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    PublisherApi apiInstance = new PublisherApi(defaultClient);
    String name = "name_example"; // String | The name of a publisher in the Publisher's database
    String page = "page_example"; // String | The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them
    String pageSize = "pageSize_example"; // String | How many items should be returned per page, maximum of 1,000
    try {
      Publisher result = apiInstance.publisherNameGet(name, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublisherApi#publisherNameGet");
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
| **name** | **String**| The name of a publisher in the Publisher&#39;s database | |
| **page** | **String**| The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them | [optional] |
| **pageSize** | **String**| How many items should be returned per page, maximum of 1,000 | [optional] |

### Return type

[**Publisher**](Publisher.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The publisher name was found in the database |  * Access-Control-Allow-Origin - CORS Header to allow different origin responses <br>  |
| **404** | Publisher not found |  -  |

<a id="publishersQueryGet"></a>
# **publishersQueryGet**
> publishersQueryGet(query, pageSize, page)

Search publishers

This returns a list of publishers that match the given query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublisherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.isbndb.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    PublisherApi apiInstance = new PublisherApi(defaultClient);
    String query = "query_example"; // String | A string to search for in the Publisher’s database
    String pageSize = "pageSize_example"; // String | How many items should be returned per page, maximum of 1,000
    String page = "page_example"; // String | The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them
    try {
      apiInstance.publishersQueryGet(query, pageSize, page);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublisherApi#publishersQueryGet");
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
| **query** | **String**| A string to search for in the Publisher’s database | |
| **pageSize** | **String**| How many items should be returned per page, maximum of 1,000 | [optional] |
| **page** | **String**| The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The query string found results in the publisher&#39;s database |  * Access-Control-Allow-Origin - CORS Header to allow different origin responses <br>  |
| **404** | There are no results in the publisher&#39;s database for the given query |  -  |

