# MetricDefinitionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metricDefinitionsList**](MetricDefinitionsApi.md#metricDefinitionsList) | **GET** /{resourceUri}/providers/microsoft.insights/metricDefinitions |  |


<a id="metricDefinitionsList"></a>
# **metricDefinitionsList**
> MetricDefinitionCollection metricDefinitionsList(resourceUri, apiVersion, $filter)



Lists the metric definitions for the resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricDefinitionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    MetricDefinitionsApi apiInstance = new MetricDefinitionsApi(defaultClient);
    String resourceUri = "resourceUri_example"; // String | The identifier of the resource.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String $filter = "$filter_example"; // String | Reduces the set of data collected by retrieving particular metric definitions from all the definitions available for the resource.<br>For example, to get just the definition for the 'CPU percentage' counter: $filter=name.value eq '\\Processor(_Total)\\% Processor Time'.<br>Multiple metrics can be retrieved by joining together *'name eq <value>'* clauses separated by *or* logical operators.<br>**NOTE**: No other syntax is allowed.
    try {
      MetricDefinitionCollection result = apiInstance.metricDefinitionsList(resourceUri, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricDefinitionsApi#metricDefinitionsList");
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
| **$filter** | **String**| Reduces the set of data collected by retrieving particular metric definitions from all the definitions available for the resource.&lt;br&gt;For example, to get just the definition for the &#39;CPU percentage&#39; counter: $filter&#x3D;name.value eq &#39;\\Processor(_Total)\\% Processor Time&#39;.&lt;br&gt;Multiple metrics can be retrieved by joining together *&#39;name eq &lt;value&gt;&#39;* clauses separated by *or* logical operators.&lt;br&gt;**NOTE**: No other syntax is allowed. | [optional] |

### Return type

[**MetricDefinitionCollection**](MetricDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request to get the list of metric definitions |  -  |
| **0** | Error response describing why the operation failed. |  -  |

