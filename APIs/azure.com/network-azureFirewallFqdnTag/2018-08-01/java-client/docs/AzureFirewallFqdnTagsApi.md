# AzureFirewallFqdnTagsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**azureFirewallFqdnTagsListAll**](AzureFirewallFqdnTagsApi.md#azureFirewallFqdnTagsListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/azureFirewallFqdnTags |  |


<a id="azureFirewallFqdnTagsListAll"></a>
# **azureFirewallFqdnTagsListAll**
> AzureFirewallFqdnTagListResult azureFirewallFqdnTagsListAll(apiVersion, subscriptionId)



Gets all the Azure Firewall FQDN Tags in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AzureFirewallFqdnTagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    AzureFirewallFqdnTagsApi apiInstance = new AzureFirewallFqdnTagsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      AzureFirewallFqdnTagListResult result = apiInstance.azureFirewallFqdnTagsListAll(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AzureFirewallFqdnTagsApi#azureFirewallFqdnTagsListAll");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**AzureFirewallFqdnTagListResult**](AzureFirewallFqdnTagListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. The operation returns a list of Azure Firewall FQDN Tag resources. |  -  |

