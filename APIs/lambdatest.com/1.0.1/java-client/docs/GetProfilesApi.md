# GetProfilesApi

All URIs are relative to *https://api.lambdatest.com/screenshots/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**profiles**](GetProfilesApi.md#profiles) | **GET** /profiles | Fetch login profiles |


<a id="profiles"></a>
# **profiles**
> Profiles profiles()

Fetch login profiles

Fetch login profiles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lambdatest.com/screenshots/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    GetProfilesApi apiInstance = new GetProfilesApi(defaultClient);
    try {
      Profiles result = apiInstance.profiles();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetProfilesApi#profiles");
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

[**Profiles**](Profiles.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **401** | Access denied. Auth error. |  -  |

