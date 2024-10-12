# Class10UserUserIdApi

All URIs are relative to */rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resource10UserUserIdGetUserGET**](Class10UserUserIdApi.md#resource10UserUserIdGetUserGET) | **GET** /1.0/user/{userId} | Get a user by userId. |


<a id="resource10UserUserIdGetUserGET"></a>
# **resource10UserUserIdGetUserGET**
> JsonUser resource10UserUserIdGetUserGET(userId)

Get a user by userId.

Get a user by userId. (deprecated)  Note: This endpoint always returns a result, even if the user doesn&#39;t exist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class10UserUserIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/rest");

    Class10UserUserIdApi apiInstance = new Class10UserUserIdApi(defaultClient);
    String userId = "userId_example"; // String | the user's userId
    try {
      JsonUser result = apiInstance.resource10UserUserIdGetUserGET(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class10UserUserIdApi#resource10UserUserIdGetUserGET");
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
| **userId** | **String**| the user&#39;s userId | |

### Return type

[**JsonUser**](JsonUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

