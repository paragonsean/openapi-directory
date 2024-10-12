# MeApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2MeJsonGet**](MeApi.md#v2MeJsonGet) | **GET** /v2/me.json | Fetch current user |


<a id="v2MeJsonGet"></a>
# **v2MeJsonGet**
> User v2MeJsonGet()

Fetch current user

Authenticated user information. This endpoint does not accept any parameters as it is represents your authenticated user. The \&quot;Users\&quot; resource provides user information for other users on the team. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.salesloft.com");

    MeApi apiInstance = new MeApi(defaultClient);
    try {
      User result = apiInstance.v2MeJsonGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#v2MeJsonGet");
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

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

