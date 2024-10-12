# OauthApi

All URIs are relative to *http://api.thenounproject.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getApiQuotaStatus**](OauthApi.md#getApiQuotaStatus) | **GET** /oauth/usage | Get api quota status |


<a id="getApiQuotaStatus"></a>
# **getApiQuotaStatus**
> getApiQuotaStatus()

Get api quota status

Returns current oauth usage and limits

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.thenounproject.com");

    OauthApi apiInstance = new OauthApi(defaultClient);
    try {
      apiInstance.getApiQuotaStatus();
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthApi#getApiQuotaStatus");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

