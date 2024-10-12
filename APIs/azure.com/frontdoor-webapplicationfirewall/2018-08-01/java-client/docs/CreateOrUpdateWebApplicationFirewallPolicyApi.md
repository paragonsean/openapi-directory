# CreateOrUpdateWebApplicationFirewallPolicyApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**policiesCreateOrUpdate**](CreateOrUpdateWebApplicationFirewallPolicyApi.md#policiesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallPolicies/{policyName} |  |


<a id="policiesCreateOrUpdate"></a>
# **policiesCreateOrUpdate**
> WebApplicationFirewallPolicy policiesCreateOrUpdate(resourceGroupName, policyName, subscriptionId, apiVersion, parameters)



Creates or update policy with specified rule set name within a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreateOrUpdateWebApplicationFirewallPolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CreateOrUpdateWebApplicationFirewallPolicyApi apiInstance = new CreateOrUpdateWebApplicationFirewallPolicyApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String policyName = "policyName_example"; // String | The name of the resource group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    WebApplicationFirewallPolicy parameters = new WebApplicationFirewallPolicy(); // WebApplicationFirewallPolicy | Policy to be created.
    try {
      WebApplicationFirewallPolicy result = apiInstance.policiesCreateOrUpdate(resourceGroupName, policyName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreateOrUpdateWebApplicationFirewallPolicyApi#policiesCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **policyName** | **String**| The name of the resource group. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |
| **parameters** | [**WebApplicationFirewallPolicy**](WebApplicationFirewallPolicy.md)| Policy to be created. | |

### Return type

[**WebApplicationFirewallPolicy**](WebApplicationFirewallPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **201** | Created. The request has been fulfilled and a new protection policy has been created. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

