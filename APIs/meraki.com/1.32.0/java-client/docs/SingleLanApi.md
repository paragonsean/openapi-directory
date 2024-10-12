# SingleLanApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkApplianceSingleLan_1**](SingleLanApi.md#getNetworkApplianceSingleLan_1) | **GET** /networks/{networkId}/appliance/singleLan | Return single LAN configuration |
| [**updateNetworkApplianceSingleLan_1**](SingleLanApi.md#updateNetworkApplianceSingleLan_1) | **PUT** /networks/{networkId}/appliance/singleLan | Update single LAN configuration |


<a id="getNetworkApplianceSingleLan_1"></a>
# **getNetworkApplianceSingleLan_1**
> GetNetworkApplianceSingleLan200Response getNetworkApplianceSingleLan_1(networkId)

Return single LAN configuration

Return single LAN configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleLanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SingleLanApi apiInstance = new SingleLanApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkApplianceSingleLan200Response result = apiInstance.getNetworkApplianceSingleLan_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleLanApi#getNetworkApplianceSingleLan_1");
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

[**GetNetworkApplianceSingleLan200Response**](GetNetworkApplianceSingleLan200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkApplianceSingleLan_1"></a>
# **updateNetworkApplianceSingleLan_1**
> GetNetworkApplianceSingleLan200Response updateNetworkApplianceSingleLan_1(networkId, updateNetworkApplianceSingleLanRequest)

Update single LAN configuration

Update single LAN configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SingleLanApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SingleLanApi apiInstance = new SingleLanApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceSingleLanRequest updateNetworkApplianceSingleLanRequest = new UpdateNetworkApplianceSingleLanRequest(); // UpdateNetworkApplianceSingleLanRequest | 
    try {
      GetNetworkApplianceSingleLan200Response result = apiInstance.updateNetworkApplianceSingleLan_1(networkId, updateNetworkApplianceSingleLanRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SingleLanApi#updateNetworkApplianceSingleLan_1");
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
| **updateNetworkApplianceSingleLanRequest** | [**UpdateNetworkApplianceSingleLanRequest**](UpdateNetworkApplianceSingleLanRequest.md)|  | [optional] |

### Return type

[**GetNetworkApplianceSingleLan200Response**](GetNetworkApplianceSingleLan200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

