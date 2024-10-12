# BlockchainMemberOperationResultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**blockchainMemberOperationResultsGet**](BlockchainMemberOperationResultApi.md#blockchainMemberOperationResultsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Blockchain/locations/{locationName}/blockchainMemberOperationResults/{operationId} |  |


<a id="blockchainMemberOperationResultsGet"></a>
# **blockchainMemberOperationResultsGet**
> OperationResult blockchainMemberOperationResultsGet(locationName, operationId, apiVersion, subscriptionId)



Get Async operation result.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BlockchainMemberOperationResultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    BlockchainMemberOperationResultApi apiInstance = new BlockchainMemberOperationResultApi(defaultClient);
    String locationName = "locationName_example"; // String | Location name.
    String operationId = "operationId_example"; // String | Operation Id.
    String apiVersion = "2018-06-01-preview"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    try {
      OperationResult result = apiInstance.blockchainMemberOperationResultsGet(locationName, operationId, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BlockchainMemberOperationResultApi#blockchainMemberOperationResultsGet");
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
| **locationName** | **String**| Location name. | |
| **operationId** | **String**| Operation Id. | |
| **apiVersion** | **String**| Client API Version. | [enum: 2018-06-01-preview] |
| **subscriptionId** | **String**| Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call. | |

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
| **200** | Success |  -  |
| **204** | Success |  -  |

