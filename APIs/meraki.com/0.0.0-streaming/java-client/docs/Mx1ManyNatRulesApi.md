# Mx1ManyNatRulesApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkOneToManyNatRules**](Mx1ManyNatRulesApi.md#getNetworkOneToManyNatRules) | **GET** /networks/{networkId}/oneToManyNatRules | Return the 1:Many NAT mapping rules for an MX network |
| [**updateNetworkOneToManyNatRules**](Mx1ManyNatRulesApi.md#updateNetworkOneToManyNatRules) | **PUT** /networks/{networkId}/oneToManyNatRules | Set the 1:Many NAT mapping rules for an MX network |


<a id="getNetworkOneToManyNatRules"></a>
# **getNetworkOneToManyNatRules**
> Object getNetworkOneToManyNatRules(networkId)

Return the 1:Many NAT mapping rules for an MX network

Return the 1:Many NAT mapping rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Mx1ManyNatRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    Mx1ManyNatRulesApi apiInstance = new Mx1ManyNatRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkOneToManyNatRules(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Mx1ManyNatRulesApi#getNetworkOneToManyNatRules");
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

<a id="updateNetworkOneToManyNatRules"></a>
# **updateNetworkOneToManyNatRules**
> Object updateNetworkOneToManyNatRules(networkId, updateNetworkOneToManyNatRulesRequest)

Set the 1:Many NAT mapping rules for an MX network

Set the 1:Many NAT mapping rules for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Mx1ManyNatRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    Mx1ManyNatRulesApi apiInstance = new Mx1ManyNatRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkOneToManyNatRulesRequest updateNetworkOneToManyNatRulesRequest = new UpdateNetworkOneToManyNatRulesRequest(); // UpdateNetworkOneToManyNatRulesRequest | 
    try {
      Object result = apiInstance.updateNetworkOneToManyNatRules(networkId, updateNetworkOneToManyNatRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Mx1ManyNatRulesApi#updateNetworkOneToManyNatRules");
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
| **updateNetworkOneToManyNatRulesRequest** | [**UpdateNetworkOneToManyNatRulesRequest**](UpdateNetworkOneToManyNatRulesRequest.md)|  | |

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

