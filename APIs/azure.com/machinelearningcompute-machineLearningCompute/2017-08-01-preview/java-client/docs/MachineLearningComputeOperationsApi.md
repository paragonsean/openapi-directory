# MachineLearningComputeOperationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**machineLearningComputeListAvailableOperations**](MachineLearningComputeOperationsApi.md#machineLearningComputeListAvailableOperations) | **GET** /providers/Microsoft.MachineLearningCompute/operations |  |


<a id="machineLearningComputeListAvailableOperations"></a>
# **machineLearningComputeListAvailableOperations**
> AvailableOperations machineLearningComputeListAvailableOperations(apiVersion)



Gets all available operations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MachineLearningComputeOperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    MachineLearningComputeOperationsApi apiInstance = new MachineLearningComputeOperationsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
    try {
      AvailableOperations result = apiInstance.machineLearningComputeListAvailableOperations(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MachineLearningComputeOperationsApi#machineLearningComputeListAvailableOperations");
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
| **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | |

### Return type

[**AvailableOperations**](AvailableOperations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

