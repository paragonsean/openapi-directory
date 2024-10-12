# TimeZonesApi

All URIs are relative to *https://api.pocketsmith.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**timeZonesGet**](TimeZonesApi.md#timeZonesGet) | **GET** /time_zones | List time zones |


<a id="timeZonesGet"></a>
# **timeZonesGet**
> List&lt;TimeZone&gt; timeZonesGet()

List time zones

Lists time zones.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TimeZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    TimeZonesApi apiInstance = new TimeZonesApi(defaultClient);
    try {
      List<TimeZone> result = apiInstance.timeZonesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TimeZonesApi#timeZonesGet");
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

[**List&lt;TimeZone&gt;**](TimeZone.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

