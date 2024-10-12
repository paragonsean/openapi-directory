# PublicIpAddressesApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**publicIPAddressesList**](PublicIpAddressesApi.md#publicIPAddressesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network.Admin/adminPublicIpAddresses |  |


<a id="publicIPAddressesList"></a>
# **publicIPAddressesList**
> PublicIpAddressList publicIPAddressesList(subscriptionId, apiVersion, $filter, $orderBy, $top, $skip, $inlineCount)



List of public ip addresses.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublicIpAddressesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    PublicIpAddressesApi apiInstance = new PublicIpAddressesApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "2015-06-15"; // String | Client API Version.
    String $filter = "$filter_example"; // String | OData filter parameter.
    String $orderBy = "$orderBy_example"; // String | OData orderBy parameter.
    String $top = "$top_example"; // String | OData top parameter.
    String $skip = "$skip_example"; // String | OData skip parameter.
    String $inlineCount = "$inlineCount_example"; // String | OData inline count parameter.
    try {
      PublicIpAddressList result = apiInstance.publicIPAddressesList(subscriptionId, apiVersion, $filter, $orderBy, $top, $skip, $inlineCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublicIpAddressesApi#publicIPAddressesList");
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

[**PublicIpAddressList**](PublicIpAddressList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

