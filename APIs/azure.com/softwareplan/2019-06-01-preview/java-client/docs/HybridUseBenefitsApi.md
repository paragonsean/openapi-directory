# HybridUseBenefitsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**hybridUseBenefitList**](HybridUseBenefitsApi.md#hybridUseBenefitList) | **GET** /{scope}/providers/Microsoft.SoftwarePlan/hybridUseBenefits |  |


<a id="hybridUseBenefitList"></a>
# **hybridUseBenefitList**
> HybridUseBenefitListResult hybridUseBenefitList(scope, apiVersion, $filter)



Get all hybrid use benefits associated with an ARM resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridUseBenefitsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridUseBenefitsApi apiInstance = new HybridUseBenefitsApi(defaultClient);
    String scope = "scope_example"; // String | The scope at which the operation is performed. This is limited to Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts for now
    String apiVersion = "apiVersion_example"; // String | The api-version to be used by the service
    String $filter = "$filter_example"; // String | Supports applying filter on the type of SKU
    try {
      HybridUseBenefitListResult result = apiInstance.hybridUseBenefitList(scope, apiVersion, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridUseBenefitsApi#hybridUseBenefitList");
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
| **scope** | **String**| The scope at which the operation is performed. This is limited to Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts for now | |
| **apiVersion** | **String**| The api-version to be used by the service | |
| **$filter** | **String**| Supports applying filter on the type of SKU | [optional] |

### Return type

[**HybridUseBenefitListResult**](HybridUseBenefitListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - returns an array of plans at that scope |  -  |
| **0** | Error response describing why the operation failed. |  -  |

