# ArchiveApi

All URIs are relative to *http://api.nytimes.com/svc/archive/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**yearMonthJsonGet**](ArchiveApi.md#yearMonthJsonGet) | **GET** /{year}/{month}.json | Archive API |


<a id="yearMonthJsonGet"></a>
# **yearMonthJsonGet**
> YearMonthJsonGet200Response yearMonthJsonGet(year, month)

Archive API

The Archive API provides lists of NYT articles by month going back to 1851.  Simply pass in the year and month you want and it returns a JSON object with all articles for that month. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArchiveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.nytimes.com/svc/archive/v1");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    ArchiveApi apiInstance = new ArchiveApi(defaultClient);
    Integer year = 56; // Integer | The year (e.g. 2016).
    Integer month = 56; // Integer | The month number (e.g. 1 for January).
    try {
      YearMonthJsonGet200Response result = apiInstance.yearMonthJsonGet(year, month);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArchiveApi#yearMonthJsonGet");
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
| **year** | **Integer**| The year (e.g. 2016). | |
| **month** | **Integer**| The month number (e.g. 1 for January). | |

### Return type

[**YearMonthJsonGet200Response**](YearMonthJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The docs requested. |  -  |

