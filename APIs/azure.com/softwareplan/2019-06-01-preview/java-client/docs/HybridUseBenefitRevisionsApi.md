# HybridUseBenefitRevisionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**hybridUseBenefitRevisionList**](HybridUseBenefitRevisionsApi.md#hybridUseBenefitRevisionList) | **GET** /{scope}/providers/Microsoft.SoftwarePlan/hybridUseBenefits/{planId}/revisions |  |


<a id="hybridUseBenefitRevisionList"></a>
# **hybridUseBenefitRevisionList**
> HybridUseBenefitListResult hybridUseBenefitRevisionList(scope, planId, apiVersion)



Gets the version history of a hybrid use benefit

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HybridUseBenefitRevisionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    HybridUseBenefitRevisionsApi apiInstance = new HybridUseBenefitRevisionsApi(defaultClient);
    String scope = "scope_example"; // String | The scope at which the operation is performed. This is limited to Microsoft.Compute/virtualMachines and Microsoft.Compute/hostGroups/hosts for now
    String planId = "planId_example"; // String | This is a unique identifier for a plan. Should be a guid.
    String apiVersion = "apiVersion_example"; // String | The api-version to be used by the service
    try {
      HybridUseBenefitListResult result = apiInstance.hybridUseBenefitRevisionList(scope, planId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HybridUseBenefitRevisionsApi#hybridUseBenefitRevisionList");
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
| **planId** | **String**| This is a unique identifier for a plan. Should be a guid. | |
| **apiVersion** | **String**| The api-version to be used by the service | |

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
| **200** | OK - returns an array of plans ordered by revision |  -  |
| **0** | Error response describing why the operation failed. |  -  |

