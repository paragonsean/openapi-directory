# RetrieveApi

All URIs are relative to *https://test.api.amadeus.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gETActivity**](RetrieveApi.md#gETActivity) | **GET** /shopping/activities/{activityId} | Retrieve one activity by its id |


<a id="gETActivity"></a>
# **gETActivity**
> SuccessfulSearch1 gETActivity(activityId)

Retrieve one activity by its id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RetrieveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://test.api.amadeus.com/v1");

    RetrieveApi apiInstance = new RetrieveApi(defaultClient);
    String activityId = "activityId_example"; // String | 
    try {
      SuccessfulSearch1 result = apiInstance.gETActivity(activityId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RetrieveApi#gETActivity");
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
| **activityId** | **String**|  | |

### Return type

[**SuccessfulSearch1**](SuccessfulSearch1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.amadeus+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Operation |  -  |
| **400** | Code   | Title -------|---------------- 572    | INVALID OPTION        |  -  |
| **404** | Not Found |  -  |
| **0** | Unexpected Error |  -  |

