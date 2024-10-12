# VirtualNetworksApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualNetworksList**](VirtualNetworksApi.md#virtualNetworksList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network.Admin/adminVirtualNetworks |  |


<a id="virtualNetworksList"></a>
# **virtualNetworksList**
> VirtualNetworksList virtualNetworksList(subscriptionId, apiVersion, $filter, $orderBy, $top, $skip, $inlineCount)



Get a list of all virtual networks.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworksApi apiInstance = new VirtualNetworksApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "2015-06-15"; // String | Client API Version.
    String $filter = "$filter_example"; // String | OData filter parameter.
    String $orderBy = "$orderBy_example"; // String | OData orderBy parameter.
    String $top = "$top_example"; // String | OData top parameter.
    String $skip = "$skip_example"; // String | OData skip parameter.
    String $inlineCount = "$inlineCount_example"; // String | OData inline count parameter.
    try {
      VirtualNetworksList result = apiInstance.virtualNetworksList(subscriptionId, apiVersion, $filter, $orderBy, $top, $skip, $inlineCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworksApi#virtualNetworksList");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | [default to 2015-06-15] |
| **$filter** | **String**| OData filter parameter. | [optional] |
| **$orderBy** | **String**| OData orderBy parameter. | [optional] |
| **$top** | **String**| OData top parameter. | [optional] |
| **$skip** | **String**| OData skip parameter. | [optional] |
| **$inlineCount** | **String**| OData inline count parameter. | [optional] |

### Return type

[**VirtualNetworksList**](VirtualNetworksList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

