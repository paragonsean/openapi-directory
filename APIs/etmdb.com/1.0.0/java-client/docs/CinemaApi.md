# CinemaApi

All URIs are relative to *https://etmdb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cinemaSearchRead**](CinemaApi.md#cinemaSearchRead) | **GET** /api/v1/cinema/search/{id} | Return cinema search result |


<a id="cinemaSearchRead"></a>
# **cinemaSearchRead**
> cinemaSearchRead(id)

Return cinema search result

Return cinema search result  ### Response Class (Status 200)  * __{id}__: Used as a key to search cinemas,  For more details on how cinemas are listed [see here][ref]. [ref]: https://etmdb.com/en/cinema-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CinemaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    CinemaApi apiInstance = new CinemaApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.cinemaSearchRead(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CinemaApi#cinemaSearchRead");
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
| **id** | **String**|  | |

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

