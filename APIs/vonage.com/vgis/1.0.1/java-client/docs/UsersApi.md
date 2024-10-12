# UsersApi

All URIs are relative to *https://api.vonage.com/t/vbc.prod/vis/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getUser**](UsersApi.md#getUser) | **GET** /self | User info |


<a id="getUser"></a>
# **getUser**
> User getUser()

User info

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/vis/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      User result = apiInstance.getUser();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUser");
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request: The client should not repeat the request without modifications |  -  |
| **401** | Unauthorized: Invalid access token |  -  |
| **403** | Forbidden: The user has no rights to access the resource(s) |  -  |
| **408** | Timeout: The client may repeat the request without modifications |  -  |
| **422** | Validation Error |  -  |
| **500** | Internal Server Error |  -  |
| **502** | Bad Gateway |  -  |

