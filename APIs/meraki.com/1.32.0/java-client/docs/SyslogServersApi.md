# SyslogServersApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkSyslogServers_1**](SyslogServersApi.md#getNetworkSyslogServers_1) | **GET** /networks/{networkId}/syslogServers | List the syslog servers for a network |
| [**updateNetworkSyslogServers_1**](SyslogServersApi.md#updateNetworkSyslogServers_1) | **PUT** /networks/{networkId}/syslogServers | Update the syslog servers for a network |


<a id="getNetworkSyslogServers_1"></a>
# **getNetworkSyslogServers_1**
> GetNetworkSyslogServers200Response getNetworkSyslogServers_1(networkId)

List the syslog servers for a network

List the syslog servers for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyslogServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SyslogServersApi apiInstance = new SyslogServersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkSyslogServers200Response result = apiInstance.getNetworkSyslogServers_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyslogServersApi#getNetworkSyslogServers_1");
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

[**GetNetworkSyslogServers200Response**](GetNetworkSyslogServers200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSyslogServers_1"></a>
# **updateNetworkSyslogServers_1**
> GetNetworkSyslogServers200Response updateNetworkSyslogServers_1(networkId, updateNetworkSyslogServersRequest)

Update the syslog servers for a network

Update the syslog servers for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SyslogServersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SyslogServersApi apiInstance = new SyslogServersApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSyslogServersRequest updateNetworkSyslogServersRequest = new UpdateNetworkSyslogServersRequest(); // UpdateNetworkSyslogServersRequest | 
    try {
      GetNetworkSyslogServers200Response result = apiInstance.updateNetworkSyslogServers_1(networkId, updateNetworkSyslogServersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SyslogServersApi#updateNetworkSyslogServers_1");
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
| **updateNetworkSyslogServersRequest** | [**UpdateNetworkSyslogServersRequest**](UpdateNetworkSyslogServersRequest.md)|  | |

### Return type

[**GetNetworkSyslogServers200Response**](GetNetworkSyslogServers200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

