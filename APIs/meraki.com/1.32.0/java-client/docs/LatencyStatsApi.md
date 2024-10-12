# LatencyStatsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceWirelessLatencyStats_1**](LatencyStatsApi.md#getDeviceWirelessLatencyStats_1) | **GET** /devices/{serial}/wireless/latencyStats | Aggregated latency info for a given AP on this network |
| [**getNetworkWirelessClientLatencyStats_2**](LatencyStatsApi.md#getNetworkWirelessClientLatencyStats_2) | **GET** /networks/{networkId}/wireless/clients/{clientId}/latencyStats | Aggregated latency info for a given client on this network |
| [**getNetworkWirelessClientsLatencyStats_2**](LatencyStatsApi.md#getNetworkWirelessClientsLatencyStats_2) | **GET** /networks/{networkId}/wireless/clients/latencyStats | Aggregated latency info for this network, grouped by clients |
| [**getNetworkWirelessDevicesLatencyStats_2**](LatencyStatsApi.md#getNetworkWirelessDevicesLatencyStats_2) | **GET** /networks/{networkId}/wireless/devices/latencyStats | Aggregated latency info for this network, grouped by node |
| [**getNetworkWirelessLatencyStats_1**](LatencyStatsApi.md#getNetworkWirelessLatencyStats_1) | **GET** /networks/{networkId}/wireless/latencyStats | Aggregated latency info for this network |


<a id="getDeviceWirelessLatencyStats_1"></a>
# **getDeviceWirelessLatencyStats_1**
> Object getDeviceWirelessLatencyStats_1(serial, t0, t1, timespan, band, ssid, vlan, apTag, fields)

Aggregated latency info for a given AP on this network

Aggregated latency info for a given AP on this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LatencyStatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LatencyStatsApi apiInstance = new LatencyStatsApi(defaultClient);
    String serial = "serial_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    String fields = "fields_example"; // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
    try {
      Object result = apiInstance.getDeviceWirelessLatencyStats_1(serial, t0, t1, timespan, band, ssid, vlan, apTag, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LatencyStatsApi#getDeviceWirelessLatencyStats_1");
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
| **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] |

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

<a id="getNetworkWirelessClientLatencyStats_2"></a>
# **getNetworkWirelessClientLatencyStats_2**
> Object getNetworkWirelessClientLatencyStats_2(networkId, clientId, t0, t1, timespan, band, ssid, vlan, apTag, fields)

Aggregated latency info for a given client on this network

Aggregated latency info for a given client on this network. Clients are identified by their MAC.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LatencyStatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LatencyStatsApi apiInstance = new LatencyStatsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String clientId = "clientId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    String fields = "fields_example"; // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
    try {
      Object result = apiInstance.getNetworkWirelessClientLatencyStats_2(networkId, clientId, t0, t1, timespan, band, ssid, vlan, apTag, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LatencyStatsApi#getNetworkWirelessClientLatencyStats_2");
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
| **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] |

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

<a id="getNetworkWirelessClientsLatencyStats_2"></a>
# **getNetworkWirelessClientsLatencyStats_2**
> List&lt;Object&gt; getNetworkWirelessClientsLatencyStats_2(networkId, t0, t1, timespan, band, ssid, vlan, apTag, fields)

Aggregated latency info for this network, grouped by clients

Aggregated latency info for this network, grouped by clients

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LatencyStatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LatencyStatsApi apiInstance = new LatencyStatsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    String fields = "fields_example"; // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
    try {
      List<Object> result = apiInstance.getNetworkWirelessClientsLatencyStats_2(networkId, t0, t1, timespan, band, ssid, vlan, apTag, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LatencyStatsApi#getNetworkWirelessClientsLatencyStats_2");
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
| **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] |

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

<a id="getNetworkWirelessDevicesLatencyStats_2"></a>
# **getNetworkWirelessDevicesLatencyStats_2**
> List&lt;Object&gt; getNetworkWirelessDevicesLatencyStats_2(networkId, t0, t1, timespan, band, ssid, vlan, apTag, fields)

Aggregated latency info for this network, grouped by node

Aggregated latency info for this network, grouped by node

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LatencyStatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LatencyStatsApi apiInstance = new LatencyStatsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    String fields = "fields_example"; // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
    try {
      List<Object> result = apiInstance.getNetworkWirelessDevicesLatencyStats_2(networkId, t0, t1, timespan, band, ssid, vlan, apTag, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LatencyStatsApi#getNetworkWirelessDevicesLatencyStats_2");
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
| **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] |

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

<a id="getNetworkWirelessLatencyStats_1"></a>
# **getNetworkWirelessLatencyStats_1**
> Object getNetworkWirelessLatencyStats_1(networkId, t0, t1, timespan, band, ssid, vlan, apTag, fields)

Aggregated latency info for this network

Aggregated latency info for this network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LatencyStatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LatencyStatsApi apiInstance = new LatencyStatsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    String fields = "fields_example"; // String | Partial selection: If present, this call will return only the selected fields of [\"rawDistribution\", \"avg\"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
    try {
      Object result = apiInstance.getNetworkWirelessLatencyStats_1(networkId, t0, t1, timespan, band, ssid, vlan, apTag, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LatencyStatsApi#getNetworkWirelessLatencyStats_1");
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
| **fields** | **String**| Partial selection: If present, this call will return only the selected fields of [\&quot;rawDistribution\&quot;, \&quot;avg\&quot;]. All fields will be returned by default. Selected fields must be entered as a comma separated string. | [optional] |

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

