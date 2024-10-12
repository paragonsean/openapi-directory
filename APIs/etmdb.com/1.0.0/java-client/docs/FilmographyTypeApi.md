# FilmographyTypeApi

All URIs are relative to *https://etmdb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**filmographyTypeSearchRead**](FilmographyTypeApi.md#filmographyTypeSearchRead) | **GET** /api/v1/filmography-type/search/{filmography_description} | Return filmography type search result |


<a id="filmographyTypeSearchRead"></a>
# **filmographyTypeSearchRead**
> filmographyTypeSearchRead(filmographyDescription)

Return filmography type search result

Return filmography type search result  ### Response Class (Status 200)  * __{filmography_description}__: Used as a key word to search filmography types  For more details on how filmography types are listed [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FilmographyTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    FilmographyTypeApi apiInstance = new FilmographyTypeApi(defaultClient);
    String filmographyDescription = "filmographyDescription_example"; // String | 
    try {
      apiInstance.filmographyTypeSearchRead(filmographyDescription);
    } catch (ApiException e) {
      System.err.println("Exception when calling FilmographyTypeApi#filmographyTypeSearchRead");
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
| **filmographyDescription** | **String**|  | |

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

