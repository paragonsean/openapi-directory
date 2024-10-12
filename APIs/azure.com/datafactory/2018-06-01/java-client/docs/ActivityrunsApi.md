# ActivityrunsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activityRunsQueryByPipelineRun**](ActivityrunsApi.md#activityRunsQueryByPipelineRun) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/pipelineruns/{runId}/queryActivityruns |  |


<a id="activityRunsQueryByPipelineRun"></a>
# **activityRunsQueryByPipelineRun**
> ActivityRunsQueryResponse activityRunsQueryByPipelineRun(subscriptionId, resourceGroupName, factoryName, runId, apiVersion, filterParameters)



Query activity runs based on input filter conditions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityrunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ActivityrunsApi apiInstance = new ActivityrunsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String runId = "runId_example"; // String | The pipeline run identifier.
    String apiVersion = "apiVersion_example"; // String | The API version.
    RunFilterParameters filterParameters = new RunFilterParameters(); // RunFilterParameters | Parameters to filter the activity runs.
    try {
      ActivityRunsQueryResponse result = apiInstance.activityRunsQueryByPipelineRun(subscriptionId, resourceGroupName, factoryName, runId, apiVersion, filterParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityrunsApi#activityRunsQueryByPipelineRun");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **runId** | **String**| The pipeline run identifier. | |
| **apiVersion** | **String**| The API version. | |
| **filterParameters** | [**RunFilterParameters**](RunFilterParameters.md)| Parameters to filter the activity runs. | |

### Return type

[**ActivityRunsQueryResponse**](ActivityRunsQueryResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

