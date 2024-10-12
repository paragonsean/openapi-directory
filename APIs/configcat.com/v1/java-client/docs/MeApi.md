# MeApi

All URIs are relative to *https://api.configcat.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMe**](MeApi.md#getMe) | **GET** /v1/me | Get authenticated user details |


<a id="getMe"></a>
# **getMe**
> MeModel getMe()

Get authenticated user details



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.configcat.com");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    MeApi apiInstance = new MeApi(defaultClient);
    try {
      MeModel result = apiInstance.getMe();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MeApi#getMe");
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

[**MeModel**](MeModel.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized. In case of the Public Management API credentials are invalid. |  -  |
| **429** | Too many requests. In case of the request rate exceeds the rate limits. |  -  |

