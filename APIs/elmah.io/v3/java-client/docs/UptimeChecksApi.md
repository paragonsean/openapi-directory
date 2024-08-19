# UptimeChecksApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**uptimeChecksGetAll**](UptimeChecksApi.md#uptimeChecksGetAll) | **GET** /v3/uptimechecks | Fetch a list of uptime checks. Currently in closed beta. Get in contact to get access to this endpoint. |


<a id="uptimeChecksGetAll"></a>
# **uptimeChecksGetAll**
> List&lt;UptimeCheck&gt; uptimeChecksGetAll()

Fetch a list of uptime checks. Currently in closed beta. Get in contact to get access to this endpoint.

Required permission: &#x60;uptimechecks_read&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UptimeChecksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    UptimeChecksApi apiInstance = new UptimeChecksApi(defaultClient);
    try {
      List<UptimeCheck> result = apiInstance.uptimeChecksGetAll();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UptimeChecksApi#uptimeChecksGetAll");
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

[**List&lt;UptimeCheck&gt;**](UptimeCheck.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request for uptime checks successful. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the uptime checks API but the trial expired. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

