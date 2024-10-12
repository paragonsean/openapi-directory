# ShowtimeApi

All URIs are relative to *https://etmdb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**showtimeSearchallRead**](ShowtimeApi.md#showtimeSearchallRead) | **GET** /api/v1/showtime/searchall/{param} | Return showtime search result |


<a id="showtimeSearchallRead"></a>
# **showtimeSearchallRead**
> showtimeSearchallRead(param)

Return showtime search result

Return showtime search result  ### Response Class (Status 200) __{param}__ argument can be * show time or * day of the week [Mon&#x3D;1, Tue&#x3D;2, Wed&#x3D;3, Thu&#x3D;4, Fri&#x3D;5, Sat&#x3D;6, Sun&#x3D;7]  For more details about showtime, check each cinema from the cinema list [see here][ref]. [ref]: https://etmdb.com/en/movie-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShowtimeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    ShowtimeApi apiInstance = new ShowtimeApi(defaultClient);
    String param = "param_example"; // String | 
    try {
      apiInstance.showtimeSearchallRead(param);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShowtimeApi#showtimeSearchallRead");
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
| **param** | **String**|  | |

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

