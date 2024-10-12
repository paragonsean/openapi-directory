# MetricsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metricsList**](MetricsApi.md#metricsList) | **GET** /{resourceUri}/providers/microsoft.insights/metrics |  |


<a id="metricsList"></a>
# **metricsList**
> MetricCollection metricsList(resourceUri, apiVersion, $filter)



Lists the metric values for a resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The identifier of the resource.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | Reduces the set of data collected.<br>The filter is optional. If present it must contain a list of metric names to retrieve of the form: *(name.value eq 'metricName' [or name.value eq 'metricName' or ...])*. Optionally, the filter can contain conditions for the following attributes *aggregationType*, *startTime*, *endTime*, and *timeGrain* of the form *attributeName operator value*. Where operator is one of *ne*, *eq*, *gt*, *lt*.<br>Several conditions can be combined with parentheses and logical operators, e.g: *and*, *or*.<br>Some example filter expressions are:<br>- $filter=(name.value eq 'RunsSucceeded') and aggregationType eq 'Total' and startTime eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq duration'PT1M',<br>- $filter=(name.value eq 'RunsSucceeded') and (aggregationType eq 'Total' or aggregationType eq 'Average') and startTime eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq duration'PT1H',<br>- $filter=(name.value eq 'ActionsCompleted' or name.value eq 'RunsSucceeded') and (aggregationType eq 'Total' or aggregationType eq 'Average') and startTime eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq duration'PT1M'.<br><br>**NOTE**: When a metrics query comes in with multiple metrics, but with no aggregation types defined, the service will pick the Primary aggregation type of the first metrics to be used as the default aggregation type for all the metrics.
    try {
      MetricCollection result = apiInstance.metricsList(resourceUri, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#metricsList");
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
| **resourceUri** | **String**| The identifier of the resource. | |
| **apiVersion** | **String**| Client Api Version. | |
| **$filter** | **String**| Reduces the set of data collected.&lt;br&gt;The filter is optional. If present it must contain a list of metric names to retrieve of the form: *(name.value eq &#39;metricName&#39; [or name.value eq &#39;metricName&#39; or ...])*. Optionally, the filter can contain conditions for the following attributes *aggregationType*, *startTime*, *endTime*, and *timeGrain* of the form *attributeName operator value*. Where operator is one of *ne*, *eq*, *gt*, *lt*.&lt;br&gt;Several conditions can be combined with parentheses and logical operators, e.g: *and*, *or*.&lt;br&gt;Some example filter expressions are:&lt;br&gt;- $filter&#x3D;(name.value eq &#39;RunsSucceeded&#39;) and aggregationType eq &#39;Total&#39; and startTime eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq duration&#39;PT1M&#39;,&lt;br&gt;- $filter&#x3D;(name.value eq &#39;RunsSucceeded&#39;) and (aggregationType eq &#39;Total&#39; or aggregationType eq &#39;Average&#39;) and startTime eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq duration&#39;PT1H&#39;,&lt;br&gt;- $filter&#x3D;(name.value eq &#39;ActionsCompleted&#39; or name.value eq &#39;RunsSucceeded&#39;) and (aggregationType eq &#39;Total&#39; or aggregationType eq &#39;Average&#39;) and startTime eq 2016-02-20 and endTime eq 2016-02-21 and timeGrain eq duration&#39;PT1M&#39;.&lt;br&gt;&lt;br&gt;**NOTE**: When a metrics query comes in with multiple metrics, but with no aggregation types defined, the service will pick the Primary aggregation type of the first metrics to be used as the default aggregation type for all the metrics. | [optional] |

### Return type

[**MetricCollection**](MetricCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to get the list of metric values |  -  |
| **0** | Error response describing why the operation failed. |  -  |

