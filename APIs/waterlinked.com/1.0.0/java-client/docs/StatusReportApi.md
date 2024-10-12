# StatusReportApi

All URIs are relative to *http://demo.waterlinked.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**statusReportGet**](StatusReportApi.md#statusReportGet) | **GET** /api/v1/status_report/ | Get status_report |


<a id="statusReportGet"></a>
# **statusReportGet**
> List&lt;WlStatusGroup&gt; statusReportGet()

Get status_report

Get list of status reports from all status groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusReportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    StatusReportApi apiInstance = new StatusReportApi(defaultClient);
    try {
      List<WlStatusGroup> result = apiInstance.statusReportGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusReportApi#statusReportGet");
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

[**List&lt;WlStatusGroup&gt;**](WlStatusGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.wl.status.group+json; type=collection

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

