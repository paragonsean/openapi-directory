# GetScreenshotsApi

All URIs are relative to *https://api.lambdatest.com/screenshots/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**screenshots**](GetScreenshotsApi.md#screenshots) | **GET** /{test_id} | Fetch specified screenshot details |


<a id="screenshots"></a>
# **screenshots**
> ScreenshotTestResponse screenshots(testId)

Fetch specified screenshot details

To fetch specified screenshot details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetScreenshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lambdatest.com/screenshots/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    GetScreenshotsApi apiInstance = new GetScreenshotsApi(defaultClient);
    String testId = "testId_example"; // String | Test ID that details you want to fetch
    try {
      ScreenshotTestResponse result = apiInstance.screenshots(testId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetScreenshotsApi#screenshots");
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
| **testId** | **String**| Test ID that details you want to fetch | |

### Return type

[**ScreenshotTestResponse**](ScreenshotTestResponse.md)

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
| **403** | Access denied. Auth error. |  -  |
| **404** | Resource not found |  -  |

