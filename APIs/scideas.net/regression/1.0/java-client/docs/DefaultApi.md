# DefaultApi

All URIs are relative to *https://services.scideas.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**regressionApiPost**](DefaultApi.md#regressionApiPost) | **POST** /regression/api | Returns regression analysis. |


<a id="regressionApiPost"></a>
# **regressionApiPost**
> InlineResponse200 regressionApiPost(regressionApiBody)

Returns regression analysis.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://services.scideas.net");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    RegressionApiBody regressionApiBody = new RegressionApiBody(); // RegressionApiBody | 
    try {
      InlineResponse200 result = apiInstance.regressionApiPost(regressionApiBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#regressionApiPost");
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
| **regressionApiBody** | [**RegressionApiBody**](RegressionApiBody.md)|  | |

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A JSON array of data |  -  |

