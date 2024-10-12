# VirtualMachineSizesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualMachineSizesList**](VirtualMachineSizesApi.md#virtualMachineSizesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearningServices/locations/{location}/vmSizes |  |


<a id="virtualMachineSizesList"></a>
# **virtualMachineSizesList**
> VirtualMachineSizeListResult virtualMachineSizesList(location, apiVersion, subscriptionId)



Returns supported VM Sizes in a location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualMachineSizesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualMachineSizesApi apiInstance = new VirtualMachineSizesApi(defaultClient);
    String location = "location_example"; // String | The location upon which virtual-machine-sizes is queried.
    String apiVersion = "apiVersion_example"; // String | Version of Azure Machine Learning resource provider API.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription identifier.
    try {
      VirtualMachineSizeListResult result = apiInstance.virtualMachineSizesList(location, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualMachineSizesApi#virtualMachineSizesList");
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
| **location** | **String**| The location upon which virtual-machine-sizes is queried. | |
| **apiVersion** | **String**| Version of Azure Machine Learning resource provider API. | |
| **subscriptionId** | **String**| Azure subscription identifier. | |

### Return type

[**VirtualMachineSizeListResult**](VirtualMachineSizeListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

