# Mx11NatRulesApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkOneToOneNatRules**](Mx11NatRulesApi.md#getNetworkOneToOneNatRules) | **GET** /networks/{networkId}/oneToOneNatRules | Return the 1:1 NAT mapping rules for an MX network |
| [**updateNetworkOneToOneNatRules**](Mx11NatRulesApi.md#updateNetworkOneToOneNatRules) | **PUT** /networks/{networkId}/oneToOneNatRules | Set the 1:1 NAT mapping rules for an MX network |


<a id="getNetworkOneToOneNatRules"></a>
# **getNetworkOneToOneNatRules**
> Object getNetworkOneToOneNatRules(networkId)

Return the 1:1 NAT mapping rules for an MX network

Return the 1:1 NAT mapping rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Mx11NatRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    Mx11NatRulesApi apiInstance = new Mx11NatRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkOneToOneNatRules(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Mx11NatRulesApi#getNetworkOneToOneNatRules");
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

<a id="updateNetworkOneToOneNatRules"></a>
# **updateNetworkOneToOneNatRules**
> Object updateNetworkOneToOneNatRules(networkId, updateNetworkOneToOneNatRulesRequest)

Set the 1:1 NAT mapping rules for an MX network

Set the 1:1 NAT mapping rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Mx11NatRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    Mx11NatRulesApi apiInstance = new Mx11NatRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkOneToOneNatRulesRequest updateNetworkOneToOneNatRulesRequest = new UpdateNetworkOneToOneNatRulesRequest(); // UpdateNetworkOneToOneNatRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkOneToOneNatRules(networkId, updateNetworkOneToOneNatRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Mx11NatRulesApi#updateNetworkOneToOneNatRules");
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
| **updateNetworkOneToOneNatRulesRequest** | [**UpdateNetworkOneToOneNatRulesRequest**](UpdateNetworkOneToOneNatRulesRequest.md)|  | |

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

