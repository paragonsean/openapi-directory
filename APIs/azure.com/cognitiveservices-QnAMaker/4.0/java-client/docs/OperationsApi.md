# OperationsApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**operationsGetDetails**](OperationsApi.md#operationsGetDetails) | **GET** /operations/{operationId} | Gets details of a specific long running operation. |


<a id="operationsGetDetails"></a>
# **operationsGetDetails**
> Operation operationsGetDetails(operationId)

Gets details of a specific long running operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OperationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    OperationsApi apiInstance = new OperationsApi(defaultClient);
    String operationId = "operationId_example"; // String | Operation id.
    try {
      Operation result = apiInstance.operationsGetDetails(operationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationsApi#operationsGetDetails");
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
| **operationId** | **String**| Operation id. | |

### Return type

[**Operation**](Operation.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of the long running operation. |  * RetryAfter - Indicates how long the client should wait before sending a follow up request. The header will be present only if the operation is running or has not started yet. <br>  |
| **0** | Error response. |  -  |

