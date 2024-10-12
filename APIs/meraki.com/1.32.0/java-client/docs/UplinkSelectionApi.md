# UplinkSelectionApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkApplianceTrafficShapingUplinkSelection_2**](UplinkSelectionApi.md#getNetworkApplianceTrafficShapingUplinkSelection_2) | **GET** /networks/{networkId}/appliance/trafficShaping/uplinkSelection | Show uplink selection settings for an MX network |
| [**updateNetworkApplianceTrafficShapingUplinkSelection_2**](UplinkSelectionApi.md#updateNetworkApplianceTrafficShapingUplinkSelection_2) | **PUT** /networks/{networkId}/appliance/trafficShaping/uplinkSelection | Update uplink selection settings for an MX network |


<a id="getNetworkApplianceTrafficShapingUplinkSelection_2"></a>
# **getNetworkApplianceTrafficShapingUplinkSelection_2**
> GetNetworkApplianceTrafficShapingUplinkSelection200Response getNetworkApplianceTrafficShapingUplinkSelection_2(networkId)

Show uplink selection settings for an MX network

Show uplink selection settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UplinkSelectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UplinkSelectionApi apiInstance = new UplinkSelectionApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkApplianceTrafficShapingUplinkSelection200Response result = apiInstance.getNetworkApplianceTrafficShapingUplinkSelection_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UplinkSelectionApi#getNetworkApplianceTrafficShapingUplinkSelection_2");
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
| **networkId** | **String**|  | |

### Return type

[**GetNetworkApplianceTrafficShapingUplinkSelection200Response**](GetNetworkApplianceTrafficShapingUplinkSelection200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceTrafficShapingUplinkSelection_2"></a>
# **updateNetworkApplianceTrafficShapingUplinkSelection_2**
> GetNetworkApplianceTrafficShapingUplinkSelection200Response updateNetworkApplianceTrafficShapingUplinkSelection_2(networkId, updateNetworkApplianceTrafficShapingUplinkSelectionRequest)

Update uplink selection settings for an MX network

Update uplink selection settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UplinkSelectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UplinkSelectionApi apiInstance = new UplinkSelectionApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest updateNetworkApplianceTrafficShapingUplinkSelectionRequest = new UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest(); // UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest | 
    try {
      GetNetworkApplianceTrafficShapingUplinkSelection200Response result = apiInstance.updateNetworkApplianceTrafficShapingUplinkSelection_2(networkId, updateNetworkApplianceTrafficShapingUplinkSelectionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UplinkSelectionApi#updateNetworkApplianceTrafficShapingUplinkSelection_2");
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
| **networkId** | **String**|  | |
| **updateNetworkApplianceTrafficShapingUplinkSelectionRequest** | [**UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest**](UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest.md)|  | [optional] |

### Return type

[**GetNetworkApplianceTrafficShapingUplinkSelection200Response**](GetNetworkApplianceTrafficShapingUplinkSelection200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

