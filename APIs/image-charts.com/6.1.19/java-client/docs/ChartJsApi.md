# ChartJsApi

All URIs are relative to *https://image-charts.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getChartjs280**](ChartJsApi.md#getChartjs280) | **GET** /chart.js/2.8.0 | Chart.js as image API |


<a id="getChartjs280"></a>
# **getChartjs280**
> String getChartjs280(c, chart, width, height, backgroundColor, bkg, encoding, icac, ichm, icretina)

Chart.js as image API

Image-charts

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartJsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://image-charts.com");

    ChartJsApi apiInstance = new ChartJsApi(defaultClient);
    String c = "c_example"; // String | Javascript/JSON definition of the chart. Use a Chart.js configuration object.
    String chart = "chart_example"; // String | Javascript/JSON definition of the chart. Use a Chart.js configuration object.
    Integer width = 500; // Integer | Width of the chart
    Integer height = 300; // Integer | Height of the chart
    String backgroundColor = "backgroundColor_example"; // String | Background of the chart canvas. Accepts rgb (rgb(255,255,120)), colors (red), and url-encoded hex values (%23ff00ff). Abbreviated as \"bkg\"
    String bkg = "bkg_example"; // String | Background of the chart canvas. Accepts rgb (rgb(255,255,120)), colors (red), and url-encoded hex values (%23ff00ff). Abbreviated as \"bkg\"
    String encoding = "url"; // String | Encoding of your \"chart\" parameter. Accepted values are url and base64.
    String icac = "icac_example"; // String | image-charts enterprise `account_id`
    String ichm = "ichm_example"; // String | HMAC-SHA256 signature required to activate paid features
    String icretina = "0"; // String | retina mode
    try {
      String result = apiInstance.getChartjs280(c, chart, width, height, backgroundColor, bkg, encoding, icac, ichm, icretina);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartJsApi#getChartjs280");
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
| **c** | **String**| Javascript/JSON definition of the chart. Use a Chart.js configuration object. | [optional] |
| **chart** | **String**| Javascript/JSON definition of the chart. Use a Chart.js configuration object. | [optional] |
| **width** | **Integer**| Width of the chart | [optional] [default to 500] |
| **height** | **Integer**| Height of the chart | [optional] [default to 300] |
| **backgroundColor** | **String**| Background of the chart canvas. Accepts rgb (rgb(255,255,120)), colors (red), and url-encoded hex values (%23ff00ff). Abbreviated as \&quot;bkg\&quot; | [optional] |
| **bkg** | **String**| Background of the chart canvas. Accepts rgb (rgb(255,255,120)), colors (red), and url-encoded hex values (%23ff00ff). Abbreviated as \&quot;bkg\&quot; | [optional] |
| **encoding** | **String**| Encoding of your \&quot;chart\&quot; parameter. Accepted values are url and base64. | [optional] [default to url] [enum: url, base64] |
| **icac** | **String**| image-charts enterprise &#x60;account_id&#x60; | [optional] |
| **ichm** | **String**| HMAC-SHA256 signature required to activate paid features | [optional] |
| **icretina** | **String**| retina mode | [optional] [enum: 0, 1] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/png, application/gif, image/svg+xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Successful |  -  |

