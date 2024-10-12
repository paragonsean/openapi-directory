# CinemaDetailApi

All URIs are relative to *https://etmdb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cinemaDetailSearchRead**](CinemaDetailApi.md#cinemaDetailSearchRead) | **GET** /api/v1/cinema-detail/search/{cinema_name} | Return cinema details search result |


<a id="cinemaDetailSearchRead"></a>
# **cinemaDetailSearchRead**
> cinemaDetailSearchRead(cinemaName)

Return cinema details search result

Return cinema details search result  ### Response Class (Status 200)  * __{cinema_name}__: Used as a key word to search cinemas,  For more details on how cinemas are listed [see here][ref]. [ref]: https://etmdb.com/en/cinema-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CinemaDetailApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    CinemaDetailApi apiInstance = new CinemaDetailApi(defaultClient);
    String cinemaName = "cinemaName_example"; // String | 
    try {
      apiInstance.cinemaDetailSearchRead(cinemaName);
    } catch (ApiException e) {
      System.err.println("Exception when calling CinemaDetailApi#cinemaDetailSearchRead");
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
| **cinemaName** | **String**|  | |

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

