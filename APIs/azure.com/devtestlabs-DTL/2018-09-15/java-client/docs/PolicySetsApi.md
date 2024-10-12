# PolicySetsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**policySetsEvaluatePolicies**](PolicySetsApi.md#policySetsEvaluatePolicies) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/policysets/{name}/evaluatePolicies |  |


<a id="policySetsEvaluatePolicies"></a>
# **policySetsEvaluatePolicies**
> EvaluatePoliciesResponse policySetsEvaluatePolicies(subscriptionId, resourceGroupName, labName, name, apiVersion, evaluatePoliciesRequest)



Evaluates lab policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicySetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PolicySetsApi apiInstance = new PolicySetsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the policy set.
    String apiVersion = "2018-09-15"; // String | Client API version.
    EvaluatePoliciesRequest evaluatePoliciesRequest = new EvaluatePoliciesRequest(); // EvaluatePoliciesRequest | Request body for evaluating a policy set.
    try {
      EvaluatePoliciesResponse result = apiInstance.policySetsEvaluatePolicies(subscriptionId, resourceGroupName, labName, name, apiVersion, evaluatePoliciesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicySetsApi#policySetsEvaluatePolicies");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **labName** | **String**| The name of the lab. | |
| **name** | **String**| The name of the policy set. | |
| **apiVersion** | **String**| Client API version. | [default to 2018-09-15] |
| **evaluatePoliciesRequest** | [**EvaluatePoliciesRequest**](EvaluatePoliciesRequest.md)| Request body for evaluating a policy set. | |

### Return type

[**EvaluatePoliciesResponse**](EvaluatePoliciesResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

