# BaselineApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**baselinesList**](BaselineApi.md#baselinesList) | **GET** /{resourceUri}/providers/microsoft.insights/metricBaselines |  |


<a id="baselinesList"></a>
# **baselinesList**
> MetricBaselinesResponse baselinesList(resourceUri, apiVersion, metricnames, metricnamespace, timespan, interval, aggregation, sensitivities, $filter, resultType)



**Lists the metric baseline values for a resource**.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BaselineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BaselineApi apiInstance = new BaselineApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The identifier of the resource.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String metricnames = "metricnames_example"; // String | The names of the metrics (comma separated) to retrieve.
    String metricnamespace = "metricnamespace_example"; // String | Metric namespace to query metric definitions for.
    String timespan = "timespan_example"; // String | The timespan of the query. It is a string with the following format 'startDateTime_ISO/endDateTime_ISO'.
    String interval = "interval_example"; // String | The interval (i.e. timegrain) of the query.
    String aggregation = "aggregation_example"; // String | The list of aggregation types (comma separated) to retrieve.
    String sensitivities = "sensitivities_example"; // String | The list of sensitivities (comma separated) to retrieve.
    String $filter = "$filter_example"; // String | The **$filter** is used to reduce the set of metric data returned.<br>Example:<br>Metric contains metadata A, B and C.<br>- Return all time series of C where A = a1 and B = b1 or b2<br>**$filter=A eq ‘a1’ and B eq ‘b1’ or B eq ‘b2’ and C eq ‘*’**<br>- Invalid variant:<br>**$filter=A eq ‘a1’ and B eq ‘b1’ and C eq ‘*’ or B = ‘b2’**<br>This is invalid because the logical or operator cannot separate two different metadata names.<br>- Return all time series where A = a1, B = b1 and C = c1:<br>**$filter=A eq ‘a1’ and B eq ‘b1’ and C eq ‘c1’**<br>- Return all time series where A = a1<br>**$filter=A eq ‘a1’ and B eq ‘*’ and C eq ‘*’**.
    String resultType = "Data"; // String | Allows retrieving only metadata of the baseline. On data request all information is retrieved.
    try {
      MetricBaselinesResponse result = apiInstance.baselinesList(resourceUri, apiVersion, metricnames, metricnamespace, timespan, interval, aggregation, sensitivities, $filter, resultType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BaselineApi#baselinesList");
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
| **metricnames** | **String**| The names of the metrics (comma separated) to retrieve. | [optional] |
| **metricnamespace** | **String**| Metric namespace to query metric definitions for. | [optional] |
| **timespan** | **String**| The timespan of the query. It is a string with the following format &#39;startDateTime_ISO/endDateTime_ISO&#39;. | [optional] |
| **interval** | **String**| The interval (i.e. timegrain) of the query. | [optional] |
| **aggregation** | **String**| The list of aggregation types (comma separated) to retrieve. | [optional] |
| **sensitivities** | **String**| The list of sensitivities (comma separated) to retrieve. | [optional] |
| **$filter** | **String**| The **$filter** is used to reduce the set of metric data returned.&lt;br&gt;Example:&lt;br&gt;Metric contains metadata A, B and C.&lt;br&gt;- Return all time series of C where A &#x3D; a1 and B &#x3D; b1 or b2&lt;br&gt;**$filter&#x3D;A eq ‘a1’ and B eq ‘b1’ or B eq ‘b2’ and C eq ‘*’**&lt;br&gt;- Invalid variant:&lt;br&gt;**$filter&#x3D;A eq ‘a1’ and B eq ‘b1’ and C eq ‘*’ or B &#x3D; ‘b2’**&lt;br&gt;This is invalid because the logical or operator cannot separate two different metadata names.&lt;br&gt;- Return all time series where A &#x3D; a1, B &#x3D; b1 and C &#x3D; c1:&lt;br&gt;**$filter&#x3D;A eq ‘a1’ and B eq ‘b1’ and C eq ‘c1’**&lt;br&gt;- Return all time series where A &#x3D; a1&lt;br&gt;**$filter&#x3D;A eq ‘a1’ and B eq ‘*’ and C eq ‘*’**. | [optional] |
| **resultType** | **String**| Allows retrieving only metadata of the baseline. On data request all information is retrieved. | [optional] [enum: Data, Metadata] |

### Return type

[**MetricBaselinesResponse**](MetricBaselinesResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to get the list of metric baseline values. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

