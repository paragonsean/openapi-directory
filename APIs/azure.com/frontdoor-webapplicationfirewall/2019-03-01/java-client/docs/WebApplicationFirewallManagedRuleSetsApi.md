# WebApplicationFirewallManagedRuleSetsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**managedRuleSetsList**](WebApplicationFirewallManagedRuleSetsApi.md#managedRuleSetsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/FrontDoorWebApplicationFirewallManagedRuleSets |  |


<a id="managedRuleSetsList"></a>
# **managedRuleSetsList**
> ManagedRuleSetDefinitionList managedRuleSetsList(subscriptionId, apiVersion)



Lists all available managed rule sets.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebApplicationFirewallManagedRuleSetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    WebApplicationFirewallManagedRuleSetsApi apiInstance = new WebApplicationFirewallManagedRuleSetsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API version.
    try {
      ManagedRuleSetDefinitionList result = apiInstance.managedRuleSetsList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebApplicationFirewallManagedRuleSetsApi#managedRuleSetsList");
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
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API version. | |

### Return type

[**ManagedRuleSetDefinitionList**](ManagedRuleSetDefinitionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The operation returns a list of all available web application firewall managed rule sets. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

