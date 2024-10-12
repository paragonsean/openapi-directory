# TrustedServersApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3**](TrustedServersApi.md#createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3) | **POST** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers | Add a server to be trusted by Dynamic ARP Inspection on this network |
| [**deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3**](TrustedServersApi.md#deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3) | **DELETE** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trustedServerId} | Remove a server from being trusted by Dynamic ARP Inspection on this network |
| [**getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_3**](TrustedServersApi.md#getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_3) | **GET** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers | Return the list of servers trusted by Dynamic ARP Inspection on this network |
| [**updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3**](TrustedServersApi.md#updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3) | **PUT** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trustedServerId} | Update a server that is trusted by Dynamic ARP Inspection on this network |


<a id="createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3"></a>
# **createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3**
> GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3(networkId, createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest)

Add a server to be trusted by Dynamic ARP Inspection on this network

Add a server to be trusted by Dynamic ARP Inspection on this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrustedServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrustedServersApi apiInstance = new TrustedServersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest = new CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest(); // CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest | 
    try {
      GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner result = apiInstance.createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3(networkId, createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrustedServersApi#createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3");
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
| **createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest** | [**CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest**](CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest.md)|  | |

### Return type

[**GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner**](GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3"></a>
# **deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3**
> deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3(networkId, trustedServerId)

Remove a server from being trusted by Dynamic ARP Inspection on this network

Remove a server from being trusted by Dynamic ARP Inspection on this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrustedServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrustedServersApi apiInstance = new TrustedServersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String trustedServerId = "trustedServerId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3(networkId, trustedServerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrustedServersApi#deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3");
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
| **trustedServerId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_3"></a>
# **getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_3**
> List&lt;GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner&gt; getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_3(networkId, perPage, startingAfter, endingBefore)

Return the list of servers trusted by Dynamic ARP Inspection on this network

Return the list of servers trusted by Dynamic ARP Inspection on this network. These are also known as whitelisted snoop entries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrustedServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrustedServersApi apiInstance = new TrustedServersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner> result = apiInstance.getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_3(networkId, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrustedServersApi#getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_3");
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
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

### Return type

[**List&lt;GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner&gt;**](GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3"></a>
# **updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3**
> GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3(networkId, trustedServerId, updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest)

Update a server that is trusted by Dynamic ARP Inspection on this network

Update a server that is trusted by Dynamic ARP Inspection on this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrustedServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    TrustedServersApi apiInstance = new TrustedServersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String trustedServerId = "trustedServerId_example"; // String | 
    UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest = new UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest(); // UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest | 
    try {
      GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner result = apiInstance.updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3(networkId, trustedServerId, updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrustedServersApi#updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_3");
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
| **trustedServerId** | **String**|  | |
| **updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest** | [**UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest**](UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest.md)|  | [optional] |

### Return type

[**GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner**](GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

