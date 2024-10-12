# MetricsApi

All URIs are relative to *https://monitoring.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**metricsCreate**](MetricsApi.md#metricsCreate) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProvider}/{resourceTypeName}/{resourceName}/metrics |  |


<a id="metricsCreate"></a>
# **metricsCreate**
> AzureMetricsResult metricsCreate(contentType, contentLength, authorization, subscriptionId, resourceGroupName, resourceProvider, resourceTypeName, resourceName, body)



**Post the metric values for a resource**.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://monitoring.azure.com");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    String contentType = "contentType_example"; // String | Supports application/json and application/x-ndjson
    Integer contentLength = 56; // Integer | Content length of the payload
    String authorization = "authorization_example"; // String | Authorization token issue for issued for audience \"https:\\\\monitoring.azure.com\\\"
    String subscriptionId = "subscriptionId_example"; // String | The azure subscription id
    String resourceGroupName = "resourceGroupName_example"; // String | The ARM resource group name
    String resourceProvider = "resourceProvider_example"; // String | The ARM resource provider name
    String resourceTypeName = "resourceTypeName_example"; // String | The ARM resource type name
    String resourceName = "resourceName_example"; // String | The ARM resource name
    AzureMetricsDocument body = new AzureMetricsDocument(); // AzureMetricsDocument | The Azure metrics document json payload
    try {
      AzureMetricsResult result = apiInstance.metricsCreate(contentType, contentLength, authorization, subscriptionId, resourceGroupName, resourceProvider, resourceTypeName, resourceName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#metricsCreate");
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
| **contentType** | **String**| Supports application/json and application/x-ndjson | |
| **contentLength** | **Integer**| Content length of the payload | |
| **authorization** | **String**| Authorization token issue for issued for audience \&quot;https:\\\\monitoring.azure.com\\\&quot; | |
| **subscriptionId** | **String**| The azure subscription id | |
| **resourceGroupName** | **String**| The ARM resource group name | |
| **resourceProvider** | **String**| The ARM resource provider name | |
| **resourceTypeName** | **String**| The ARM resource type name | |
| **resourceName** | **String**| The ARM resource name | |
| **body** | [**AzureMetricsDocument**](AzureMetricsDocument.md)| The Azure metrics document json payload | |

### Return type

[**AzureMetricsResult**](AzureMetricsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The azure metrics publish succeeded |  -  |
| **0** | An unexpected error from the server. See response object for the reason |  -  |

