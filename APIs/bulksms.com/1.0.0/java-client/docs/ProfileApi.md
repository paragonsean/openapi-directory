# ProfileApi

All URIs are relative to *https://api.bulksms.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**profileGet**](ProfileApi.md#profileGet) | **GET** /profile | Get profile |


<a id="profileGet"></a>
# **profileGet**
> Profile profileGet()

Get profile

Returns information about your user profile

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bulksms.com/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ProfileApi apiInstance = new ProfileApi(defaultClient);
    try {
      Profile result = apiInstance.profileGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileApi#profileGet");
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

[**Profile**](Profile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A Profile object |  -  |

