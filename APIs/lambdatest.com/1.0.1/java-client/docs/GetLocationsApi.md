# GetLocationsApi

All URIs are relative to *https://api.lambdatest.com/screenshots/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**locations**](GetLocationsApi.md#locations) | **GET** /locations | Fetch Locations |


<a id="locations"></a>
# **locations**
> Locations locations()

Fetch Locations

Fetch list of available Geolocations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetLocationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lambdatest.com/screenshots/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    GetLocationsApi apiInstance = new GetLocationsApi(defaultClient);
    try {
      Locations result = apiInstance.locations();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetLocationsApi#locations");
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

[**Locations**](Locations.md)

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

