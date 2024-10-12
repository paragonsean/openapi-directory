# BookApi

All URIs are relative to *https://api.isbndb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bookIsbnGet**](BookApi.md#bookIsbnGet) | **GET** /book/{isbn} | Gets book details |
| [**booksQueryGet**](BookApi.md#booksQueryGet) | **GET** /books/{query} | Search books |


<a id="bookIsbnGet"></a>
# **bookIsbnGet**
> Book bookIsbnGet(isbn)

Gets book details

Returns the book details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.isbndb.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    BookApi apiInstance = new BookApi(defaultClient);
    String isbn = "isbn_example"; // String | an ISBN 10 or ISBN 13 in the Books database
    try {
      Book result = apiInstance.bookIsbnGet(isbn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookApi#bookIsbnGet");
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
| **isbn** | **String**| an ISBN 10 or ISBN 13 in the Books database | |

### Return type

[**Book**](Book.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The book ISBN was found in the database |  * Access-Control-Allow-Origin - CORS Header to allow different origin responses <br>  |
| **404** | Book not found |  -  |

<a id="booksQueryGet"></a>
# **booksQueryGet**
> booksQueryGet(query, page, author, pageSize)

Search books

This returns a list of books that match the query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.isbndb.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    BookApi apiInstance = new BookApi(defaultClient);
    String query = "query_example"; // String | A string to search for in the Book’s database
    String page = "page_example"; // String | The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them
    String author = "author_example"; // String | Filters the query results by author
    String pageSize = "pageSize_example"; // String | How many items should be returned per page, maximum of 1,000
    try {
      apiInstance.booksQueryGet(query, page, author, pageSize);
    } catch (ApiException e) {
      System.err.println("Exception when calling BookApi#booksQueryGet");
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
| **query** | **String**| A string to search for in the Book’s database | |
| **page** | **String**| The number of page to retrieve, please note the API will not return more than 10,000 results no matter how you paginate them | [optional] |
| **author** | **String**| Filters the query results by author | [optional] |
| **pageSize** | **String**| How many items should be returned per page, maximum of 1,000 | [optional] |

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
| **200** | The query string found results in the books&#39;s database |  * Access-Control-Allow-Origin - CORS Header to allow different origin responses <br>  |
| **404** | There are no results in the book&#39;s database for the given query |  -  |

