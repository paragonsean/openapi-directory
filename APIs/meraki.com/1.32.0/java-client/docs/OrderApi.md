# OrderApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkSwitchQosRulesOrder_2**](OrderApi.md#getNetworkSwitchQosRulesOrder_2) | **GET** /networks/{networkId}/switch/qosRules/order | Return the quality of service rule IDs by order in which they will be processed by the switch |
| [**updateNetworkSwitchQosRulesOrder_2**](OrderApi.md#updateNetworkSwitchQosRulesOrder_2) | **PUT** /networks/{networkId}/switch/qosRules/order | Update the order in which the rules should be processed by the switch |


<a id="getNetworkSwitchQosRulesOrder_2"></a>
# **getNetworkSwitchQosRulesOrder_2**
> Object getNetworkSwitchQosRulesOrder_2(networkId)

Return the quality of service rule IDs by order in which they will be processed by the switch

Return the quality of service rule IDs by order in which they will be processed by the switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchQosRulesOrder_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#getNetworkSwitchQosRulesOrder_2");
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

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchQosRulesOrder_2"></a>
# **updateNetworkSwitchQosRulesOrder_2**
> Object updateNetworkSwitchQosRulesOrder_2(networkId, updateNetworkSwitchQosRulesOrderRequest)

Update the order in which the rules should be processed by the switch

Update the order in which the rules should be processed by the switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OrderApi apiInstance = new OrderApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchQosRulesOrderRequest updateNetworkSwitchQosRulesOrderRequest = new UpdateNetworkSwitchQosRulesOrderRequest(); // UpdateNetworkSwitchQosRulesOrderRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchQosRulesOrder_2(networkId, updateNetworkSwitchQosRulesOrderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrderApi#updateNetworkSwitchQosRulesOrder_2");
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
| **updateNetworkSwitchQosRulesOrderRequest** | [**UpdateNetworkSwitchQosRulesOrderRequest**](UpdateNetworkSwitchQosRulesOrderRequest.md)|  | |

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

