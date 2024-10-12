# InfoApi

All URIs are relative to *https://api.infermedica.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDatabaseInfo**](InfoApi.md#getDatabaseInfo) | **GET** /info | Get database information |


<a id="getDatabaseInfo"></a>
# **getDatabaseInfo**
> InfoPublic getDatabaseInfo(ageValue, ageUnit)

Get database information

Returns information about data used by diagnostic engine.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    InfoApi apiInstance = new InfoApi(defaultClient);
    Integer ageValue = 18; // Integer | age value
    String ageUnit = "year"; // String | unit in which age value was provided
    try {
      InfoPublic result = apiInstance.getDatabaseInfo(ageValue, ageUnit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoApi#getDatabaseInfo");
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
| **ageValue** | **Integer**| age value | [optional] |
| **ageUnit** | **String**| unit in which age value was provided | [optional] [default to year] [enum: year, month] |

### Return type

[**InfoPublic**](InfoPublic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

