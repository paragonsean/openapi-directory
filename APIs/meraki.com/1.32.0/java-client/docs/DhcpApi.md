# DhcpApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceApplianceDhcpSubnets_1**](DhcpApi.md#getDeviceApplianceDhcpSubnets_1) | **GET** /devices/{serial}/appliance/dhcp/subnets | Return the DHCP subnet information for an appliance |
| [**getDeviceSwitchRoutingInterfaceDhcp_3**](DhcpApi.md#getDeviceSwitchRoutingInterfaceDhcp_3) | **GET** /devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp | Return a layer 3 interface DHCP configuration for a switch |
| [**getNetworkCellularGatewayDhcp_1**](DhcpApi.md#getNetworkCellularGatewayDhcp_1) | **GET** /networks/{networkId}/cellularGateway/dhcp | List common DHCP settings of MGs |
| [**getNetworkSwitchDhcpV4ServersSeen_1**](DhcpApi.md#getNetworkSwitchDhcpV4ServersSeen_1) | **GET** /networks/{networkId}/switch/dhcp/v4/servers/seen | Return the network&#39;s DHCPv4 servers seen within the selected timeframe (default 1 day) |
| [**getNetworkSwitchStackRoutingInterfaceDhcp_4**](DhcpApi.md#getNetworkSwitchStackRoutingInterfaceDhcp_4) | **GET** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp | Return a layer 3 interface DHCP configuration for a switch stack |
| [**updateDeviceSwitchRoutingInterfaceDhcp_3**](DhcpApi.md#updateDeviceSwitchRoutingInterfaceDhcp_3) | **PUT** /devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp | Update a layer 3 interface DHCP configuration for a switch |
| [**updateNetworkCellularGatewayDhcp_1**](DhcpApi.md#updateNetworkCellularGatewayDhcp_1) | **PUT** /networks/{networkId}/cellularGateway/dhcp | Update common DHCP settings of MGs |
| [**updateNetworkSwitchStackRoutingInterfaceDhcp_4**](DhcpApi.md#updateNetworkSwitchStackRoutingInterfaceDhcp_4) | **PUT** /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp | Update a layer 3 interface DHCP configuration for a switch stack |


<a id="getDeviceApplianceDhcpSubnets_1"></a>
# **getDeviceApplianceDhcpSubnets_1**
> List&lt;Object&gt; getDeviceApplianceDhcpSubnets_1(serial)

Return the DHCP subnet information for an appliance

Return the DHCP subnet information for an appliance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DhcpApi apiInstance = new DhcpApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      List<Object> result = apiInstance.getDeviceApplianceDhcpSubnets_1(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpApi#getDeviceApplianceDhcpSubnets_1");
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
| **serial** | **String**|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceSwitchRoutingInterfaceDhcp_3"></a>
# **getDeviceSwitchRoutingInterfaceDhcp_3**
> Object getDeviceSwitchRoutingInterfaceDhcp_3(serial, interfaceId)

Return a layer 3 interface DHCP configuration for a switch

Return a layer 3 interface DHCP configuration for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DhcpApi apiInstance = new DhcpApi(defaultClient);
    String serial = "serial_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      Object result = apiInstance.getDeviceSwitchRoutingInterfaceDhcp_3(serial, interfaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpApi#getDeviceSwitchRoutingInterfaceDhcp_3");
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
| **serial** | **String**|  | |
| **interfaceId** | **String**|  | |

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

<a id="getNetworkCellularGatewayDhcp_1"></a>
# **getNetworkCellularGatewayDhcp_1**
> GetNetworkCellularGatewayDhcp200Response getNetworkCellularGatewayDhcp_1(networkId)

List common DHCP settings of MGs

List common DHCP settings of MGs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DhcpApi apiInstance = new DhcpApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkCellularGatewayDhcp200Response result = apiInstance.getNetworkCellularGatewayDhcp_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpApi#getNetworkCellularGatewayDhcp_1");
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

[**GetNetworkCellularGatewayDhcp200Response**](GetNetworkCellularGatewayDhcp200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSwitchDhcpV4ServersSeen_1"></a>
# **getNetworkSwitchDhcpV4ServersSeen_1**
> List&lt;GetNetworkSwitchDhcpV4ServersSeen200ResponseInner&gt; getNetworkSwitchDhcpV4ServersSeen_1(networkId, t0, timespan, perPage, startingAfter, endingBefore)

Return the network&#39;s DHCPv4 servers seen within the selected timeframe (default 1 day)

Return the network&#39;s DHCPv4 servers seen within the selected timeframe (default 1 day)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DhcpApi apiInstance = new DhcpApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<GetNetworkSwitchDhcpV4ServersSeen200ResponseInner> result = apiInstance.getNetworkSwitchDhcpV4ServersSeen_1(networkId, t0, timespan, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpApi#getNetworkSwitchDhcpV4ServersSeen_1");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

### Return type

[**List&lt;GetNetworkSwitchDhcpV4ServersSeen200ResponseInner&gt;**](GetNetworkSwitchDhcpV4ServersSeen200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkSwitchStackRoutingInterfaceDhcp_4"></a>
# **getNetworkSwitchStackRoutingInterfaceDhcp_4**
> Object getNetworkSwitchStackRoutingInterfaceDhcp_4(networkId, switchStackId, interfaceId)

Return a layer 3 interface DHCP configuration for a switch stack

Return a layer 3 interface DHCP configuration for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DhcpApi apiInstance = new DhcpApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSwitchStackRoutingInterfaceDhcp_4(networkId, switchStackId, interfaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpApi#getNetworkSwitchStackRoutingInterfaceDhcp_4");
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
| **switchStackId** | **String**|  | |
| **interfaceId** | **String**|  | |

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

<a id="updateDeviceSwitchRoutingInterfaceDhcp_3"></a>
# **updateDeviceSwitchRoutingInterfaceDhcp_3**
> Object updateDeviceSwitchRoutingInterfaceDhcp_3(serial, interfaceId, updateDeviceSwitchRoutingInterfaceDhcpRequest)

Update a layer 3 interface DHCP configuration for a switch

Update a layer 3 interface DHCP configuration for a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DhcpApi apiInstance = new DhcpApi(defaultClient);
    String serial = "serial_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    UpdateDeviceSwitchRoutingInterfaceDhcpRequest updateDeviceSwitchRoutingInterfaceDhcpRequest = new UpdateDeviceSwitchRoutingInterfaceDhcpRequest(); // UpdateDeviceSwitchRoutingInterfaceDhcpRequest | 
    try {
      Object result = apiInstance.updateDeviceSwitchRoutingInterfaceDhcp_3(serial, interfaceId, updateDeviceSwitchRoutingInterfaceDhcpRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpApi#updateDeviceSwitchRoutingInterfaceDhcp_3");
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
| **serial** | **String**|  | |
| **interfaceId** | **String**|  | |
| **updateDeviceSwitchRoutingInterfaceDhcpRequest** | [**UpdateDeviceSwitchRoutingInterfaceDhcpRequest**](UpdateDeviceSwitchRoutingInterfaceDhcpRequest.md)|  | [optional] |

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

<a id="updateNetworkCellularGatewayDhcp_1"></a>
# **updateNetworkCellularGatewayDhcp_1**
> GetNetworkCellularGatewayDhcp200Response updateNetworkCellularGatewayDhcp_1(networkId, updateNetworkCellularGatewayDhcpRequest)

Update common DHCP settings of MGs

Update common DHCP settings of MGs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DhcpApi apiInstance = new DhcpApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkCellularGatewayDhcpRequest updateNetworkCellularGatewayDhcpRequest = new UpdateNetworkCellularGatewayDhcpRequest(); // UpdateNetworkCellularGatewayDhcpRequest | 
    try {
      GetNetworkCellularGatewayDhcp200Response result = apiInstance.updateNetworkCellularGatewayDhcp_1(networkId, updateNetworkCellularGatewayDhcpRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpApi#updateNetworkCellularGatewayDhcp_1");
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
| **updateNetworkCellularGatewayDhcpRequest** | [**UpdateNetworkCellularGatewayDhcpRequest**](UpdateNetworkCellularGatewayDhcpRequest.md)|  | [optional] |

### Return type

[**GetNetworkCellularGatewayDhcp200Response**](GetNetworkCellularGatewayDhcp200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkSwitchStackRoutingInterfaceDhcp_4"></a>
# **updateNetworkSwitchStackRoutingInterfaceDhcp_4**
> Object updateNetworkSwitchStackRoutingInterfaceDhcp_4(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceDhcpRequest)

Update a layer 3 interface DHCP configuration for a switch stack

Update a layer 3 interface DHCP configuration for a switch stack

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DhcpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DhcpApi apiInstance = new DhcpApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String switchStackId = "switchStackId_example"; // String | 
    String interfaceId = "interfaceId_example"; // String | 
    UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest updateNetworkSwitchStackRoutingInterfaceDhcpRequest = new UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest(); // UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchStackRoutingInterfaceDhcp_4(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceDhcpRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DhcpApi#updateNetworkSwitchStackRoutingInterfaceDhcp_4");
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
| **switchStackId** | **String**|  | |
| **interfaceId** | **String**|  | |
| **updateNetworkSwitchStackRoutingInterfaceDhcpRequest** | [**UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest**](UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest.md)|  | [optional] |

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

