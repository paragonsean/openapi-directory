# WarningsApi

All URIs are relative to *http://demo.waterlinked.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**warningsGet**](WarningsApi.md#warningsGet) | **GET** /api/v1/warnings/ | Get warnings |


<a id="warningsGet"></a>
# **warningsGet**
> List&lt;WlWarning&gt; warningsGet()

Get warnings

[DEPRECATED] Get current list of messages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WarningsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    WarningsApi apiInstance = new WarningsApi(defaultClient);
    try {
      List<WlWarning> result = apiInstance.warningsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WarningsApi#warningsGet");
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

[**List&lt;WlWarning&gt;**](WlWarning.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.waterlinked.operation_response+json, application/vnd.wl.warning+json; type=collection

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **500** | Internal Server Error |  -  |

