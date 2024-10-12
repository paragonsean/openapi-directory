# UplinksApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceApplianceUplinksSettings_1**](UplinksApi.md#getDeviceApplianceUplinksSettings_1) | **GET** /devices/{serial}/appliance/uplinks/settings | Return the uplink settings for an MX appliance |
| [**getDeviceLossAndLatencyHistory_1**](UplinksApi.md#getDeviceLossAndLatencyHistory_1) | **GET** /devices/{serial}/lossAndLatencyHistory | Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device. |
| [**getNetworkApplianceUplinksUsageHistory_1**](UplinksApi.md#getNetworkApplianceUplinksUsageHistory_1) | **GET** /networks/{networkId}/appliance/uplinks/usageHistory | Get the sent and received bytes for each uplink of a network. |
| [**getOrganizationApplianceUplinkStatuses_1**](UplinksApi.md#getOrganizationApplianceUplinkStatuses_1) | **GET** /organizations/{organizationId}/appliance/uplink/statuses | List the uplink status of every Meraki MX and Z series appliances in the organization |
| [**getOrganizationDevicesUplinksAddressesByDevice_2**](UplinksApi.md#getOrganizationDevicesUplinksAddressesByDevice_2) | **GET** /organizations/{organizationId}/devices/uplinks/addresses/byDevice | List the current uplink addresses for devices in an organization. |
| [**getOrganizationDevicesUplinksLossAndLatency_2**](UplinksApi.md#getOrganizationDevicesUplinksLossAndLatency_2) | **GET** /organizations/{organizationId}/devices/uplinksLossAndLatency | Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago |
| [**getOrganizationUplinksStatuses_1**](UplinksApi.md#getOrganizationUplinksStatuses_1) | **GET** /organizations/{organizationId}/uplinks/statuses | List the uplink status of every Meraki MX, MG and Z series devices in the organization |
| [**updateDeviceApplianceUplinksSettings_1**](UplinksApi.md#updateDeviceApplianceUplinksSettings_1) | **PUT** /devices/{serial}/appliance/uplinks/settings | Update the uplink settings for an MX appliance |


<a id="getDeviceApplianceUplinksSettings_1"></a>
# **getDeviceApplianceUplinksSettings_1**
> GetDeviceApplianceUplinksSettings200Response getDeviceApplianceUplinksSettings_1(serial)

Return the uplink settings for an MX appliance

Return the uplink settings for an MX appliance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UplinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UplinksApi apiInstance = new UplinksApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      GetDeviceApplianceUplinksSettings200Response result = apiInstance.getDeviceApplianceUplinksSettings_1(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UplinksApi#getDeviceApplianceUplinksSettings_1");
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

[**GetDeviceApplianceUplinksSettings200Response**](GetDeviceApplianceUplinksSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceLossAndLatencyHistory_1"></a>
# **getDeviceLossAndLatencyHistory_1**
> List&lt;Object&gt; getDeviceLossAndLatencyHistory_1(serial, ip, t0, t1, timespan, resolution, uplink)

Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.

Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UplinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UplinksApi apiInstance = new UplinksApi(defaultClient);
    String serial = "serial_example"; // String | 
    String ip = "ip_example"; // String | The destination IP used to obtain the requested stats. This is required.
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    Integer resolution = 56; // Integer | The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60.
    String uplink = "cellular"; // String | The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, cellular. The default is wan1.
    try {
      List<Object> result = apiInstance.getDeviceLossAndLatencyHistory_1(serial, ip, t0, t1, timespan, resolution, uplink);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UplinksApi#getDeviceLossAndLatencyHistory_1");
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
| **ip** | **String**| The destination IP used to obtain the requested stats. This is required. | |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 60 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |
| **resolution** | **Integer**| The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60. | [optional] |
| **uplink** | **String**| The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, cellular. The default is wan1. | [optional] [enum: cellular, wan1, wan2] |

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

<a id="getNetworkApplianceUplinksUsageHistory_1"></a>
# **getNetworkApplianceUplinksUsageHistory_1**
> List&lt;Object&gt; getNetworkApplianceUplinksUsageHistory_1(networkId, t0, t1, timespan, resolution)

Get the sent and received bytes for each uplink of a network.

Get the sent and received bytes for each uplink of a network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UplinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UplinksApi apiInstance = new UplinksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 10 minutes.
    Integer resolution = 56; // Integer | The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 600, 1800, 3600, 86400. The default is 60.
    try {
      List<Object> result = apiInstance.getNetworkApplianceUplinksUsageHistory_1(networkId, t0, t1, timespan, resolution);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UplinksApi#getNetworkApplianceUplinksUsageHistory_1");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 365 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 10 minutes. | [optional] |
| **resolution** | **Integer**| The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 600, 1800, 3600, 86400. The default is 60. | [optional] |

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

<a id="getOrganizationApplianceUplinkStatuses_1"></a>
# **getOrganizationApplianceUplinkStatuses_1**
> List&lt;Object&gt; getOrganizationApplianceUplinkStatuses_1(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, iccids)

List the uplink status of every Meraki MX and Z series appliances in the organization

List the uplink status of every Meraki MX and Z series appliances in the organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UplinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UplinksApi apiInstance = new UplinksApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | A list of network IDs. The returned devices will be filtered to only include these networks.
    List<String> serials = Arrays.asList(); // List<String> | A list of serial numbers. The returned devices will be filtered to only include these serials.
    List<String> iccids = Arrays.asList(); // List<String> | A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
    try {
      List<Object> result = apiInstance.getOrganizationApplianceUplinkStatuses_1(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, iccids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UplinksApi#getOrganizationApplianceUplinkStatuses_1");
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
| **organizationId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| A list of network IDs. The returned devices will be filtered to only include these networks. | [optional] |
| **serials** | [**List&lt;String&gt;**](String.md)| A list of serial numbers. The returned devices will be filtered to only include these serials. | [optional] |
| **iccids** | [**List&lt;String&gt;**](String.md)| A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs. | [optional] |

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
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationDevicesUplinksAddressesByDevice_2"></a>
# **getOrganizationDevicesUplinksAddressesByDevice_2**
> List&lt;GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner&gt; getOrganizationDevicesUplinksAddressesByDevice_2(organizationId, perPage, startingAfter, endingBefore, networkIds, productTypes, serials, tags, tagsFilterType)

List the current uplink addresses for devices in an organization.

List the current uplink addresses for devices in an organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UplinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UplinksApi apiInstance = new UplinksApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | Optional parameter to filter device uplinks by network ID. This filter uses multiple exact matches.
    List<String> productTypes = Arrays.asList(); // List<String> | Optional parameter to filter device uplinks by device product types. This filter uses multiple exact matches.
    List<String> serials = Arrays.asList(); // List<String> | Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
    List<String> tags = Arrays.asList(); // List<String> | An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches.
    String tagsFilterType = "withAllTags"; // String | An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
    try {
      List<GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner> result = apiInstance.getOrganizationDevicesUplinksAddressesByDevice_2(organizationId, perPage, startingAfter, endingBefore, networkIds, productTypes, serials, tags, tagsFilterType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UplinksApi#getOrganizationDevicesUplinksAddressesByDevice_2");
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
| **organizationId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter device uplinks by network ID. This filter uses multiple exact matches. | [optional] |
| **productTypes** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter device uplinks by device product types. This filter uses multiple exact matches. | [optional] |
| **serials** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches. | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below). This filter uses multiple exact matches. | [optional] |
| **tagsFilterType** | **String**| An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected. | [optional] [enum: withAllTags, withAnyTags] |

### Return type

[**List&lt;GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner&gt;**](GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationDevicesUplinksLossAndLatency_2"></a>
# **getOrganizationDevicesUplinksLossAndLatency_2**
> List&lt;GetOrganizationDevicesUplinksLossAndLatency200ResponseInner&gt; getOrganizationDevicesUplinksLossAndLatency_2(organizationId, t0, t1, timespan, uplink, ip)

Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago

Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UplinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UplinksApi apiInstance = new UplinksApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes.
    String uplink = "cellular"; // String | Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks.
    String ip = "ip_example"; // String | Optional filter for a specific destination IP. Default will return all destination IPs.
    try {
      List<GetOrganizationDevicesUplinksLossAndLatency200ResponseInner> result = apiInstance.getOrganizationDevicesUplinksLossAndLatency_2(organizationId, t0, t1, timespan, uplink, ip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UplinksApi#getOrganizationDevicesUplinksLossAndLatency_2");
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
| **organizationId** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 60 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes. | [optional] |
| **uplink** | **String**| Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks. | [optional] [enum: cellular, wan1, wan2] |
| **ip** | **String**| Optional filter for a specific destination IP. Default will return all destination IPs. | [optional] |

### Return type

[**List&lt;GetOrganizationDevicesUplinksLossAndLatency200ResponseInner&gt;**](GetOrganizationDevicesUplinksLossAndLatency200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationUplinksStatuses_1"></a>
# **getOrganizationUplinksStatuses_1**
> List&lt;GetOrganizationUplinksStatuses200ResponseInner&gt; getOrganizationUplinksStatuses_1(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, iccids)

List the uplink status of every Meraki MX, MG and Z series devices in the organization

List the uplink status of every Meraki MX, MG and Z series devices in the organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UplinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UplinksApi apiInstance = new UplinksApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | A list of network IDs. The returned devices will be filtered to only include these networks.
    List<String> serials = Arrays.asList(); // List<String> | A list of serial numbers. The returned devices will be filtered to only include these serials.
    List<String> iccids = Arrays.asList(); // List<String> | A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
    try {
      List<GetOrganizationUplinksStatuses200ResponseInner> result = apiInstance.getOrganizationUplinksStatuses_1(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, iccids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UplinksApi#getOrganizationUplinksStatuses_1");
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
| **organizationId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| A list of network IDs. The returned devices will be filtered to only include these networks. | [optional] |
| **serials** | [**List&lt;String&gt;**](String.md)| A list of serial numbers. The returned devices will be filtered to only include these serials. | [optional] |
| **iccids** | [**List&lt;String&gt;**](String.md)| A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs. | [optional] |

### Return type

[**List&lt;GetOrganizationUplinksStatuses200ResponseInner&gt;**](GetOrganizationUplinksStatuses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="updateDeviceApplianceUplinksSettings_1"></a>
# **updateDeviceApplianceUplinksSettings_1**
> GetDeviceApplianceUplinksSettings200Response updateDeviceApplianceUplinksSettings_1(serial, updateDeviceApplianceUplinksSettingsRequest)

Update the uplink settings for an MX appliance

Update the uplink settings for an MX appliance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UplinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    UplinksApi apiInstance = new UplinksApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceApplianceUplinksSettingsRequest updateDeviceApplianceUplinksSettingsRequest = new UpdateDeviceApplianceUplinksSettingsRequest(); // UpdateDeviceApplianceUplinksSettingsRequest | 
    try {
      GetDeviceApplianceUplinksSettings200Response result = apiInstance.updateDeviceApplianceUplinksSettings_1(serial, updateDeviceApplianceUplinksSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UplinksApi#updateDeviceApplianceUplinksSettings_1");
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
| **updateDeviceApplianceUplinksSettingsRequest** | [**UpdateDeviceApplianceUplinksSettingsRequest**](UpdateDeviceApplianceUplinksSettingsRequest.md)|  | |

### Return type

[**GetDeviceApplianceUplinksSettings200Response**](GetDeviceApplianceUplinksSettings200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

