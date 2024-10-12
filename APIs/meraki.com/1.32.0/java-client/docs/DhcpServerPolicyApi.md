# DhcpServerPolicyApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1**](DhcpServerPolicyApi.md#createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1) | **POST** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers | Add a server to be trusted by Dynamic ARP Inspection on this network |
| [**deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1**](DhcpServerPolicyApi.md#deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1) | **DELETE** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trustedServerId} | Remove a server from being trusted by Dynamic ARP Inspection on this network |
| [**getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_1**](DhcpServerPolicyApi.md#getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_1) | **GET** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers | Return the list of servers trusted by Dynamic ARP Inspection on this network |
| [**getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice_1**](DhcpServerPolicyApi.md#getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice_1) | **GET** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/warnings/byDevice | Return the devices that have a Dynamic ARP Inspection warning and their warnings |
| [**getNetworkSwitchDhcpServerPolicy_1**](DhcpServerPolicyApi.md#getNetworkSwitchDhcpServerPolicy_1) | **GET** /networks/{networkId}/switch/dhcpServerPolicy | Return the DHCP server settings |
| [**updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1**](DhcpServerPolicyApi.md#updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1) | **PUT** /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trustedServerId} | Update a server that is trusted by Dynamic ARP Inspection on this network |
| [**updateNetworkSwitchDhcpServerPolicy_1**](DhcpServerPolicyApi.md#updateNetworkSwitchDhcpServerPolicy_1) | **PUT** /networks/{networkId}/switch/dhcpServerPolicy | Update the DHCP server settings |


<a id="createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1"></a>
# **createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1**
> GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1(networkId, createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest)

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
import org.openapitools.client.api.DhcpServerPolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DhcpServerPolicyApi apiInstance = new DhcpServerPolicyApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest = new CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest(); // CreateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest | 
    try {
      GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner result = apiInstance.createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1(networkId, createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpServerPolicyApi#createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1");
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

<a id="deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1"></a>
# **deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1**
> deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1(networkId, trustedServerId)

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
import org.openapitools.client.api.DhcpServerPolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DhcpServerPolicyApi apiInstance = new DhcpServerPolicyApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String trustedServerId = "trustedServerId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1(networkId, trustedServerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpServerPolicyApi#deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1");
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

<a id="getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_1"></a>
# **getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_1**
> List&lt;GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner&gt; getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_1(networkId, perPage, startingAfter, endingBefore)

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
import org.openapitools.client.api.DhcpServerPolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DhcpServerPolicyApi apiInstance = new DhcpServerPolicyApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner> result = apiInstance.getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_1(networkId, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpServerPolicyApi#getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers_1");
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

<a id="getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice_1"></a>
# **getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice_1**
> List&lt;GetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice200ResponseInner&gt; getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice_1(networkId, perPage, startingAfter, endingBefore)

Return the devices that have a Dynamic ARP Inspection warning and their warnings

Return the devices that have a Dynamic ARP Inspection warning and their warnings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpServerPolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DhcpServerPolicyApi apiInstance = new DhcpServerPolicyApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<GetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice200ResponseInner> result = apiInstance.getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice_1(networkId, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpServerPolicyApi#getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice_1");
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

[**List&lt;GetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice200ResponseInner&gt;**](GetNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkSwitchDhcpServerPolicy_1"></a>
# **getNetworkSwitchDhcpServerPolicy_1**
> Object getNetworkSwitchDhcpServerPolicy_1(networkId)

Return the DHCP server settings

Return the DHCP server settings. Blocked/allowed servers are only applied when default policy is allow/block, respectively

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpServerPolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DhcpServerPolicyApi apiInstance = new DhcpServerPolicyApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchDhcpServerPolicy_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpServerPolicyApi#getNetworkSwitchDhcpServerPolicy_1");
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

<a id="updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1"></a>
# **updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1**
> GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1(networkId, trustedServerId, updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest)

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
import org.openapitools.client.api.DhcpServerPolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DhcpServerPolicyApi apiInstance = new DhcpServerPolicyApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String trustedServerId = "trustedServerId_example"; // String | 
    UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest = new UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest(); // UpdateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest | 
    try {
      GetNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers200ResponseInner result = apiInstance.updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1(networkId, trustedServerId, updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpServerPolicyApi#updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer_1");
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

<a id="updateNetworkSwitchDhcpServerPolicy_1"></a>
# **updateNetworkSwitchDhcpServerPolicy_1**
> Object updateNetworkSwitchDhcpServerPolicy_1(networkId, updateNetworkSwitchDhcpServerPolicyRequest)

Update the DHCP server settings

Update the DHCP server settings. Blocked/allowed servers are only applied when default policy is allow/block, respectively

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpServerPolicyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DhcpServerPolicyApi apiInstance = new DhcpServerPolicyApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSwitchDhcpServerPolicyRequest updateNetworkSwitchDhcpServerPolicyRequest = new UpdateNetworkSwitchDhcpServerPolicyRequest(); // UpdateNetworkSwitchDhcpServerPolicyRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchDhcpServerPolicy_1(networkId, updateNetworkSwitchDhcpServerPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpServerPolicyApi#updateNetworkSwitchDhcpServerPolicy_1");
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
| **updateNetworkSwitchDhcpServerPolicyRequest** | [**UpdateNetworkSwitchDhcpServerPolicyRequest**](UpdateNetworkSwitchDhcpServerPolicyRequest.md)|  | [optional] |

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

