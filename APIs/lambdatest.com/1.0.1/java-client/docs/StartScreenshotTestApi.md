# StartScreenshotTestApi

All URIs are relative to *https://api.lambdatest.com/screenshots/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**startScreenshotTest**](StartScreenshotTestApi.md#startScreenshotTest) | **POST** / | Start Screenshot Test |


<a id="startScreenshotTest"></a>
# **startScreenshotTest**
> StartScreenshotSuccess startScreenshotTest(screenshotPayload)

Start Screenshot Test

Start Screenshot Test

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StartScreenshotTestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lambdatest.com/screenshots/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    StartScreenshotTestApi apiInstance = new StartScreenshotTestApi(defaultClient);
    ScreenshotPayload screenshotPayload = new ScreenshotPayload(); // ScreenshotPayload | start screenshot test payload.
    try {
      StartScreenshotSuccess result = apiInstance.startScreenshotTest(screenshotPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StartScreenshotTestApi#startScreenshotTest");
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
| **screenshotPayload** | [**ScreenshotPayload**](ScreenshotPayload.md)| start screenshot test payload. | |

### Return type

[**StartScreenshotSuccess**](StartScreenshotSuccess.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad Request |  -  |
| **401** | Access denied. Auth error. |  -  |
| **403** | Access denied. Auth error. |  -  |

