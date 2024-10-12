# WorkspaceSkusApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listSkus**](WorkspaceSkusApi.md#listSkus) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearningServices/workspaces/skus |  |


<a id="listSkus"></a>
# **listSkus**
> SkuListResult listSkus(apiVersion, subscriptionId)



Lists all skus with associated features

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceSkusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WorkspaceSkusApi apiInstance = new WorkspaceSkusApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    try {
      SkuListResult result = apiInstance.listSkus(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceSkusApi#listSkus");
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
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **subscriptionId** | **String**| Azure subscription identifier. | |

### Return type

[**SkuListResult**](SkuListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; the request was well-formed and received properly. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

