# GetZippedScreenshotsApi

All URIs are relative to *https://api.lambdatest.com/screenshots/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**zippedScreenshots**](GetZippedScreenshotsApi.md#zippedScreenshots) | **GET** /{test_id}/zip | Fetch Zipped Screenshots |


<a id="zippedScreenshots"></a>
# **zippedScreenshots**
> ZippedScreenshotsSuccess zippedScreenshots(testId)

Fetch Zipped Screenshots

Fetch Zipped Screenshots

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GetZippedScreenshotsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lambdatest.com/screenshots/v1");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    GetZippedScreenshotsApi apiInstance = new GetZippedScreenshotsApi(defaultClient);
    String testId = "testId_example"; // String | Test ID that Zipped Screenshots you want to fetch
    try {
      ZippedScreenshotsSuccess result = apiInstance.zippedScreenshots(testId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GetZippedScreenshotsApi#zippedScreenshots");
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
| **testId** | **String**| Test ID that Zipped Screenshots you want to fetch | |

### Return type

[**ZippedScreenshotsSuccess**](ZippedScreenshotsSuccess.md)

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

