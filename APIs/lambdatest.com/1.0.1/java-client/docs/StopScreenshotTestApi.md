# StopScreenshotTestApi

All URIs are relative to *https://api.lambdatest.com/screenshots/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**stopScreenshotsTest**](StopScreenshotTestApi.md#stopScreenshotsTest) | **PUT** /stop/{test_id} | Stop specified screenshot test |


<a id="stopScreenshotsTest"></a>
# **stopScreenshotsTest**
> StopScreenshotSuccess stopScreenshotsTest(testId)

Stop specified screenshot test

Stop specified screenshot test

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopScreenshotTestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lambdatest.com/screenshots/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    StopScreenshotTestApi apiInstance = new StopScreenshotTestApi(defaultClient);
    String testId = "testId_example"; // String | Test ID that details you want to stop
    try {
      StopScreenshotSuccess result = apiInstance.stopScreenshotsTest(testId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopScreenshotTestApi#stopScreenshotsTest");
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
| **testId** | **String**| Test ID that details you want to stop | |

### Return type

[**StopScreenshotSuccess**](StopScreenshotSuccess.md)

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

