# UplinkBandwidthApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkApplianceTrafficShapingUplinkBandwidth_2**](UplinkBandwidthApi.md#getNetworkApplianceTrafficShapingUplinkBandwidth_2) | **GET** /networks/{networkId}/appliance/trafficShaping/uplinkBandwidth | Returns the uplink bandwidth limits for your MX network |
| [**updateNetworkApplianceTrafficShapingUplinkBandwidth_2**](UplinkBandwidthApi.md#updateNetworkApplianceTrafficShapingUplinkBandwidth_2) | **PUT** /networks/{networkId}/appliance/trafficShaping/uplinkBandwidth | Updates the uplink bandwidth settings for your MX network. |


<a id="getNetworkApplianceTrafficShapingUplinkBandwidth_2"></a>
# **getNetworkApplianceTrafficShapingUplinkBandwidth_2**
> GetNetworkApplianceTrafficShapingUplinkBandwidth200Response getNetworkApplianceTrafficShapingUplinkBandwidth_2(networkId)

Returns the uplink bandwidth limits for your MX network

Returns the uplink bandwidth limits for your MX network. This may not reflect the affected device&#39;s hardware capabilities.  For more information on your device&#39;s hardware capabilities, please consult our MX Family Datasheet - [https://meraki.cisco.com/product-collateral/mx-family-datasheet/?file]

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UplinkBandwidthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UplinkBandwidthApi apiInstance = new UplinkBandwidthApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkApplianceTrafficShapingUplinkBandwidth200Response result = apiInstance.getNetworkApplianceTrafficShapingUplinkBandwidth_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UplinkBandwidthApi#getNetworkApplianceTrafficShapingUplinkBandwidth_2");
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

[**GetNetworkApplianceTrafficShapingUplinkBandwidth200Response**](GetNetworkApplianceTrafficShapingUplinkBandwidth200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceTrafficShapingUplinkBandwidth_2"></a>
# **updateNetworkApplianceTrafficShapingUplinkBandwidth_2**
> Object updateNetworkApplianceTrafficShapingUplinkBandwidth_2(networkId, updateNetworkApplianceTrafficShapingUplinkBandwidthRequest)

Updates the uplink bandwidth settings for your MX network.

Updates the uplink bandwidth settings for your MX network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UplinkBandwidthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UplinkBandwidthApi apiInstance = new UplinkBandwidthApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest updateNetworkApplianceTrafficShapingUplinkBandwidthRequest = new UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest(); // UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceTrafficShapingUplinkBandwidth_2(networkId, updateNetworkApplianceTrafficShapingUplinkBandwidthRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UplinkBandwidthApi#updateNetworkApplianceTrafficShapingUplinkBandwidth_2");
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
| **updateNetworkApplianceTrafficShapingUplinkBandwidthRequest** | [**UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest**](UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

