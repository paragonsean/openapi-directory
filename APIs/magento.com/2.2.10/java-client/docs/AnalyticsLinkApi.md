# AnalyticsLinkApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**analyticsLinkProviderV1GetGet**](AnalyticsLinkApi.md#analyticsLinkProviderV1GetGet) | **GET** /V1/analytics/link | analytics/link |


<a id="analyticsLinkProviderV1GetGet"></a>
# **analyticsLinkProviderV1GetGet**
> AnalyticsDataLinkInterface analyticsLinkProviderV1GetGet()

analytics/link



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsLinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    AnalyticsLinkApi apiInstance = new AnalyticsLinkApi(defaultClient);
    try {
      AnalyticsDataLinkInterface result = apiInstance.analyticsLinkProviderV1GetGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsLinkApi#analyticsLinkProviderV1GetGet");
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

[**AnalyticsDataLinkInterface**](AnalyticsDataLinkInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

