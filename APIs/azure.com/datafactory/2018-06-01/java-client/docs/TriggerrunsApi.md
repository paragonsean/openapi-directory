# TriggerrunsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**triggerRunsQueryByFactory**](TriggerrunsApi.md#triggerRunsQueryByFactory) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/queryTriggerRuns |  |
| [**triggerRunsRerun**](TriggerrunsApi.md#triggerRunsRerun) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/triggers/{triggerName}/triggerRuns/{runId}/rerun |  |


<a id="triggerRunsQueryByFactory"></a>
# **triggerRunsQueryByFactory**
> TriggerRunsQueryResponse triggerRunsQueryByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion, filterParameters)



Query trigger runs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggerrunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggerrunsApi apiInstance = new TriggerrunsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    RunFilterParameters filterParameters = new RunFilterParameters(); // RunFilterParameters | Parameters to filter the pipeline run.
    try {
      TriggerRunsQueryResponse result = apiInstance.triggerRunsQueryByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion, filterParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggerrunsApi#triggerRunsQueryByFactory");
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
| **apiVersion** | **String**| The API version. | |
| **filterParameters** | [**RunFilterParameters**](RunFilterParameters.md)| Parameters to filter the pipeline run. | |

### Return type

[**TriggerRunsQueryResponse**](TriggerRunsQueryResponse.md)

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

<a id="triggerRunsRerun"></a>
# **triggerRunsRerun**
> triggerRunsRerun(subscriptionId, resourceGroupName, factoryName, triggerName, runId, apiVersion)



Rerun single trigger instance by runId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggerrunsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggerrunsApi apiInstance = new TriggerrunsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String triggerName = "triggerName_example"; // String | The trigger name.
    String runId = "runId_example"; // String | The pipeline run identifier.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.triggerRunsRerun(subscriptionId, resourceGroupName, factoryName, triggerName, runId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggerrunsApi#triggerRunsRerun");
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
| **triggerName** | **String**| The trigger name. | |
| **runId** | **String**| The pipeline run identifier. | |
| **apiVersion** | **String**| The API version. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TriggerRun has been restarted. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

