# ReturnsIdLabelsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rmaTrackManagementV1GetShippingLabelPdfGet**](ReturnsIdLabelsApi.md#rmaTrackManagementV1GetShippingLabelPdfGet) | **GET** /V1/returns/{id}/labels | returns/{id}/labels |


<a id="rmaTrackManagementV1GetShippingLabelPdfGet"></a>
# **rmaTrackManagementV1GetShippingLabelPdfGet**
> String rmaTrackManagementV1GetShippingLabelPdfGet(id)

returns/{id}/labels

Get shipping label int the PDF format

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReturnsIdLabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ReturnsIdLabelsApi apiInstance = new ReturnsIdLabelsApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      String result = apiInstance.rmaTrackManagementV1GetShippingLabelPdfGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReturnsIdLabelsApi#rmaTrackManagementV1GetShippingLabelPdfGet");
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
| **id** | **Integer**|  | |

### Return type

**String**

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

