# GenreTypeApi

All URIs are relative to *https://etmdb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**genreTypeSearchRead**](GenreTypeApi.md#genreTypeSearchRead) | **GET** /api/v1/genre-type/search/{genre_description} | Return genre type search result |


<a id="genreTypeSearchRead"></a>
# **genreTypeSearchRead**
> genreTypeSearchRead(genreDescription)

Return genre type search result

Return genre type search result  ### Response Class (Status 200)  * __{genre_description}__: Used as a key word to search genre types  For more details on how genre types are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GenreTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    GenreTypeApi apiInstance = new GenreTypeApi(defaultClient);
    String genreDescription = "genreDescription_example"; // String | 
    try {
      apiInstance.genreTypeSearchRead(genreDescription);
    } catch (ApiException e) {
      System.err.println("Exception when calling GenreTypeApi#genreTypeSearchRead");
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
| **genreDescription** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

