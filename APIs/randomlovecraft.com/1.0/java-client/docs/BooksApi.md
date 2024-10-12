# BooksApi

All URIs are relative to *https://randomlovecraft.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBooks**](BooksApi.md#getBooks) | **GET** /books | List all books |


<a id="getBooks"></a>
# **getBooks**
> GetBooks200Response getBooks()

List all books



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://randomlovecraft.com/api");

    BooksApi apiInstance = new BooksApi(defaultClient);
    try {
      GetBooks200Response result = apiInstance.getBooks();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BooksApi#getBooks");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBooks200Response**](GetBooks200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

