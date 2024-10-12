# ConnectionStatsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceWirelessConnectionStats_1**](ConnectionStatsApi.md#getDeviceWirelessConnectionStats_1) | **GET** /devices/{serial}/wireless/connectionStats | Aggregated connectivity info for a given AP on this network |
| [**getNetworkWirelessClientConnectionStats_2**](ConnectionStatsApi.md#getNetworkWirelessClientConnectionStats_2) | **GET** /networks/{networkId}/wireless/clients/{clientId}/connectionStats | Aggregated connectivity info for a given client on this network |
| [**getNetworkWirelessClientsConnectionStats_2**](ConnectionStatsApi.md#getNetworkWirelessClientsConnectionStats_2) | **GET** /networks/{networkId}/wireless/clients/connectionStats | Aggregated connectivity info for this network, grouped by clients |
| [**getNetworkWirelessConnectionStats_1**](ConnectionStatsApi.md#getNetworkWirelessConnectionStats_1) | **GET** /networks/{networkId}/wireless/connectionStats | Aggregated connectivity info for this network |
| [**getNetworkWirelessDevicesConnectionStats_2**](ConnectionStatsApi.md#getNetworkWirelessDevicesConnectionStats_2) | **GET** /networks/{networkId}/wireless/devices/connectionStats | Aggregated connectivity info for this network, grouped by node |


<a id="getDeviceWirelessConnectionStats_1"></a>
# **getDeviceWirelessConnectionStats_1**
> GetDeviceWirelessConnectionStats200Response getDeviceWirelessConnectionStats_1(serial, t0, t1, timespan, band, ssid, vlan, apTag)

Aggregated connectivity info for a given AP on this network

Aggregated connectivity info for a given AP on this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionStatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ConnectionStatsApi apiInstance = new ConnectionStatsApi(defaultClient);
    String serial = "serial_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    try {
      GetDeviceWirelessConnectionStats200Response result = apiInstance.getDeviceWirelessConnectionStats_1(serial, t0, t1, timespan, band, ssid, vlan, apTag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionStatsApi#getDeviceWirelessConnectionStats_1");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID | [optional] |
| **vlan** | **Integer**| Filter results by VLAN | [optional] |
| **apTag** | **String**| Filter results by AP Tag | [optional] |

### Return type

[**GetDeviceWirelessConnectionStats200Response**](GetDeviceWirelessConnectionStats200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessClientConnectionStats_2"></a>
# **getNetworkWirelessClientConnectionStats_2**
> Object getNetworkWirelessClientConnectionStats_2(networkId, clientId, t0, t1, timespan, band, ssid, vlan, apTag)

Aggregated connectivity info for a given client on this network

Aggregated connectivity info for a given client on this network. Clients are identified by their MAC.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionStatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ConnectionStatsApi apiInstance = new ConnectionStatsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String clientId = "clientId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    try {
      Object result = apiInstance.getNetworkWirelessClientConnectionStats_2(networkId, clientId, t0, t1, timespan, band, ssid, vlan, apTag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionStatsApi#getNetworkWirelessClientConnectionStats_2");
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
| **clientId** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID | [optional] |
| **vlan** | **Integer**| Filter results by VLAN | [optional] |
| **apTag** | **String**| Filter results by AP Tag | [optional] |

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

<a id="getNetworkWirelessClientsConnectionStats_2"></a>
# **getNetworkWirelessClientsConnectionStats_2**
> List&lt;Object&gt; getNetworkWirelessClientsConnectionStats_2(networkId, t0, t1, timespan, band, ssid, vlan, apTag)

Aggregated connectivity info for this network, grouped by clients

Aggregated connectivity info for this network, grouped by clients

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionStatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ConnectionStatsApi apiInstance = new ConnectionStatsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    try {
      List<Object> result = apiInstance.getNetworkWirelessClientsConnectionStats_2(networkId, t0, t1, timespan, band, ssid, vlan, apTag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionStatsApi#getNetworkWirelessClientsConnectionStats_2");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID | [optional] |
| **vlan** | **Integer**| Filter results by VLAN | [optional] |
| **apTag** | **String**| Filter results by AP Tag | [optional] |

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

<a id="getNetworkWirelessConnectionStats_1"></a>
# **getNetworkWirelessConnectionStats_1**
> GetNetworkWirelessConnectionStats200Response getNetworkWirelessConnectionStats_1(networkId, t0, t1, timespan, band, ssid, vlan, apTag)

Aggregated connectivity info for this network

Aggregated connectivity info for this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionStatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ConnectionStatsApi apiInstance = new ConnectionStatsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    try {
      GetNetworkWirelessConnectionStats200Response result = apiInstance.getNetworkWirelessConnectionStats_1(networkId, t0, t1, timespan, band, ssid, vlan, apTag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionStatsApi#getNetworkWirelessConnectionStats_1");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID | [optional] |
| **vlan** | **Integer**| Filter results by VLAN | [optional] |
| **apTag** | **String**| Filter results by AP Tag | [optional] |

### Return type

[**GetNetworkWirelessConnectionStats200Response**](GetNetworkWirelessConnectionStats200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWirelessDevicesConnectionStats_2"></a>
# **getNetworkWirelessDevicesConnectionStats_2**
> List&lt;GetDeviceWirelessConnectionStats200Response&gt; getNetworkWirelessDevicesConnectionStats_2(networkId, t0, t1, timespan, band, ssid, vlan, apTag)

Aggregated connectivity info for this network, grouped by node

Aggregated connectivity info for this network, grouped by node

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionStatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ConnectionStatsApi apiInstance = new ConnectionStatsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    try {
      List<GetDeviceWirelessConnectionStats200Response> result = apiInstance.getNetworkWirelessDevicesConnectionStats_2(networkId, t0, t1, timespan, band, ssid, vlan, apTag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionStatsApi#getNetworkWirelessDevicesConnectionStats_2");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 180 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. | [optional] |
| **band** | **String**| Filter results by band (either &#39;2.4&#39;, &#39;5&#39; or &#39;6&#39;). Note that data prior to February 2020 will not have band information. | [optional] [enum: 2.4, 5, 6] |
| **ssid** | **Integer**| Filter results by SSID | [optional] |
| **vlan** | **Integer**| Filter results by VLAN | [optional] |
| **apTag** | **String**| Filter results by AP Tag | [optional] |

### Return type

[**List&lt;GetDeviceWirelessConnectionStats200Response&gt;**](GetDeviceWirelessConnectionStats200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

