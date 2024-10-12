# OperationsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**operationsGet**](OperationsApi.md#operationsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.LabServices/locations/{locationName}/operations/{operationName} |  |


<a id="operationsGet"></a>
# **operationsGet**
> OperationResult operationsGet(subscriptionId, locationName, operationName, apiVersion)



Get operation

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
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OperationsApi apiInstance = new OperationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String locationName = "locationName_example"; // String | The name of the location.
    String operationName = "operationName_example"; // String | The name of the operation.
    String apiVersion = "2018-10-15"; // String | Client API version.
    try {
      OperationResult result = apiInstance.operationsGet(subscriptionId, locationName, operationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OperationsApi#operationsGet");
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
| **subscriptionId** | **String**| The subscription ID. | |
| **locationName** | **String**| The name of the location. | |
| **operationName** | **String**| The name of the operation. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-10-15] |

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

