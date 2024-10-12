# MonitorApi

All URIs are relative to *https://api.snyk.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**monitorDepGraph**](MonitorApi.md#monitorDepGraph) | **POST** /monitor/dep-graph | Monitor Dep Graph |


<a id="monitorDepGraph"></a>
# **monitorDepGraph**
> monitorDepGraph(org, monitorDepGraphRequest)

Monitor Dep Graph

Use this endpoint to monitor a [DepGraph data object](https://github.com/snyk/dep-graph#depgraphdata).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonitorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    MonitorApi apiInstance = new MonitorApi(defaultClient);
    String org = "9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7"; // String | The organization to test the package with. See \"The Snyk organization for a request\" above.
    MonitorDepGraphRequest monitorDepGraphRequest = new MonitorDepGraphRequest(); // MonitorDepGraphRequest | 
    try {
      apiInstance.monitorDepGraph(org, monitorDepGraphRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorApi#monitorDepGraph");
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
| **org** | **String**| The organization to test the package with. See \&quot;The Snyk organization for a request\&quot; above. | [optional] |
| **monitorDepGraphRequest** | [**MonitorDepGraphRequest**](MonitorDepGraphRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

