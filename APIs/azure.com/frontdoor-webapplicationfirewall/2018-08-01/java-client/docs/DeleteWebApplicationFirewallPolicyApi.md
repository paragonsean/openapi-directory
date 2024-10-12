# DeleteWebApplicationFirewallPolicyApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**policiesDelete**](DeleteWebApplicationFirewallPolicyApi.md#policiesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallPolicies/{policyName} |  |


<a id="policiesDelete"></a>
# **policiesDelete**
> policiesDelete(resourceGroupName, policyName, subscriptionId, apiVersion)



Deletes Policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeleteWebApplicationFirewallPolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DeleteWebApplicationFirewallPolicyApi apiInstance = new DeleteWebApplicationFirewallPolicyApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String policyName = "policyName_example"; // String | The name of the resource group.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      apiInstance.policiesDelete(resourceGroupName, policyName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeleteWebApplicationFirewallPolicyApi#policiesDelete");
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

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete successful. |  -  |
| **202** | Accepted. The request has been accepted for processing and the operation will complete asynchronously. |  -  |
| **204** | No Content. The request has been accepted but the policy was not found. |  -  |

