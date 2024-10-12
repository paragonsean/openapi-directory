# AccessControlListsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkSwitchAccessControlLists_1**](AccessControlListsApi.md#getNetworkSwitchAccessControlLists_1) | **GET** /networks/{networkId}/switch/accessControlLists | Return the access control lists for a MS network |
| [**updateNetworkSwitchAccessControlLists_1**](AccessControlListsApi.md#updateNetworkSwitchAccessControlLists_1) | **PUT** /networks/{networkId}/switch/accessControlLists | Update the access control lists for a MS network |


<a id="getNetworkSwitchAccessControlLists_1"></a>
# **getNetworkSwitchAccessControlLists_1**
> GetNetworkSwitchAccessControlLists200Response getNetworkSwitchAccessControlLists_1(networkId)

Return the access control lists for a MS network

Return the access control lists for a MS network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessControlListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AccessControlListsApi apiInstance = new AccessControlListsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkSwitchAccessControlLists200Response result = apiInstance.getNetworkSwitchAccessControlLists_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessControlListsApi#getNetworkSwitchAccessControlLists_1");
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

[**GetNetworkSwitchAccessControlLists200Response**](GetNetworkSwitchAccessControlLists200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchAccessControlLists_1"></a>
# **updateNetworkSwitchAccessControlLists_1**
> GetNetworkSwitchAccessControlLists200Response updateNetworkSwitchAccessControlLists_1(networkId, updateNetworkSwitchAccessControlListsRequest)

Update the access control lists for a MS network

Update the access control lists for a MS network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccessControlListsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    AccessControlListsApi apiInstance = new AccessControlListsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchAccessControlListsRequest updateNetworkSwitchAccessControlListsRequest = new UpdateNetworkSwitchAccessControlListsRequest(); // UpdateNetworkSwitchAccessControlListsRequest | 
    try {
      GetNetworkSwitchAccessControlLists200Response result = apiInstance.updateNetworkSwitchAccessControlLists_1(networkId, updateNetworkSwitchAccessControlListsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccessControlListsApi#updateNetworkSwitchAccessControlLists_1");
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
| **updateNetworkSwitchAccessControlListsRequest** | [**UpdateNetworkSwitchAccessControlListsRequest**](UpdateNetworkSwitchAccessControlListsRequest.md)|  | |

### Return type

[**GetNetworkSwitchAccessControlLists200Response**](GetNetworkSwitchAccessControlLists200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

