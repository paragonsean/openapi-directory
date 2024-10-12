# AuthorApi

All URIs are relative to *https://api.isbndb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authorNameGet**](AuthorApi.md#authorNameGet) | **GET** /author/{name} | Gets author details |
| [**authorsQueryGet**](AuthorApi.md#authorsQueryGet) | **GET** /authors/{query} | Search authors |


<a id="authorNameGet"></a>
# **authorNameGet**
> Author authorNameGet(name, page, pageSize)

Gets author details

Returns the name and a list of books by the author.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.isbndb.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AuthorApi apiInstance = new AuthorApi(defaultClient);
    String name = "name_example"; // String | The name of an author in the Author's database
    String page = "page_example"; // String | The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them
    String pageSize = "pageSize_example"; // String | How many items should be returned per page, maximum of 1,000
    try {
      Author result = apiInstance.authorNameGet(name, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorApi#authorNameGet");
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
| **name** | **String**| The name of an author in the Author&#39;s database | |
| **page** | **String**| The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them | [optional] |
| **pageSize** | **String**| How many items should be returned per page, maximum of 1,000 | [optional] |

### Return type

[**Author**](Author.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The author name was found in the database |  * Access-Control-Allow-Origin - CORS Header to allow different origin responses <br>  |
| **404** | Author not found |  -  |

<a id="authorsQueryGet"></a>
# **authorsQueryGet**
> AuthorQueryResults authorsQueryGet(query, pageSize, page)

Search authors

This returns a list of authors whos name matches the given query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.isbndb.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    AuthorApi apiInstance = new AuthorApi(defaultClient);
    String query = "query_example"; // String | A string to search for in the Author’s database
    String pageSize = "pageSize_example"; // String | How many items should be returned per page, maximum of 1,000
    String page = "page_example"; // String | The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them
    try {
      AuthorQueryResults result = apiInstance.authorsQueryGet(query, pageSize, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorApi#authorsQueryGet");
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
| **query** | **String**| A string to search for in the Author’s database | |
| **pageSize** | **String**| How many items should be returned per page, maximum of 1,000 | [optional] |
| **page** | **String**| The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them | [optional] |

### Return type

[**AuthorQueryResults**](AuthorQueryResults.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The query string found results in the author&#39;s database |  * Access-Control-Allow-Origin - CORS Header to allow different origin responses <br>  |
| **404** | There are no results in the author&#39;s database for the given query |  -  |

