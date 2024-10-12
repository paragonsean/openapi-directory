# PolicySetApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**policySetEvaluatePolicies**](PolicySetApi.md#policySetEvaluatePolicies) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevTestLab/labs/{labName}/policysets/{name}/evaluatePolicies |  |


<a id="policySetEvaluatePolicies"></a>
# **policySetEvaluatePolicies**
> EvaluatePoliciesResponse policySetEvaluatePolicies(subscriptionId, resourceGroupName, labName, name, apiVersion, evaluatePoliciesRequest)



Evaluates Lab Policy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PolicySetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PolicySetApi apiInstance = new PolicySetApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String labName = "labName_example"; // String | The name of the lab.
    String name = "name_example"; // String | The name of the policy set.
    String apiVersion = "2015-05-21-preview"; // String | Client API version.
    EvaluatePoliciesRequest evaluatePoliciesRequest = new EvaluatePoliciesRequest(); // EvaluatePoliciesRequest | 
    try {
      EvaluatePoliciesResponse result = apiInstance.policySetEvaluatePolicies(subscriptionId, resourceGroupName, labName, name, apiVersion, evaluatePoliciesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PolicySetApi#policySetEvaluatePolicies");
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
| **apiVersion** | **String**| Client API version. | [default to 2015-05-21-preview] |
| **evaluatePoliciesRequest** | [**EvaluatePoliciesRequest**](EvaluatePoliciesRequest.md)|  | |

### Return type

[**EvaluatePoliciesResponse**](EvaluatePoliciesResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | BadRequest |  -  |

