# StatusesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceSwitchPortsStatusesPackets_2**](StatusesApi.md#getDeviceSwitchPortsStatusesPackets_2) | **GET** /devices/{serial}/switch/ports/statuses/packets | Return the packet counters for all the ports of a switch |
| [**getDeviceSwitchPortsStatuses_2**](StatusesApi.md#getDeviceSwitchPortsStatuses_2) | **GET** /devices/{serial}/switch/ports/statuses | Return the status for all the ports of a switch |
| [**getOrganizationApplianceUplinkStatuses_2**](StatusesApi.md#getOrganizationApplianceUplinkStatuses_2) | **GET** /organizations/{organizationId}/appliance/uplink/statuses | List the uplink status of every Meraki MX and Z series appliances in the organization |
| [**getOrganizationApplianceVpnStatuses_2**](StatusesApi.md#getOrganizationApplianceVpnStatuses_2) | **GET** /organizations/{organizationId}/appliance/vpn/statuses | Show VPN status for networks in an organization |
| [**getOrganizationCameraOnboardingStatuses_2**](StatusesApi.md#getOrganizationCameraOnboardingStatuses_2) | **GET** /organizations/{organizationId}/camera/onboarding/statuses | Fetch onboarding status of cameras |
| [**getOrganizationCellularGatewayUplinkStatuses_2**](StatusesApi.md#getOrganizationCellularGatewayUplinkStatuses_2) | **GET** /organizations/{organizationId}/cellularGateway/uplink/statuses | List the uplink status of every Meraki MG cellular gateway in the organization |
| [**getOrganizationDevicesPowerModulesStatusesByDevice_3**](StatusesApi.md#getOrganizationDevicesPowerModulesStatusesByDevice_3) | **GET** /organizations/{organizationId}/devices/powerModules/statuses/byDevice | List the power status information for devices in an organization |
| [**getOrganizationDevicesStatusesOverview_2**](StatusesApi.md#getOrganizationDevicesStatusesOverview_2) | **GET** /organizations/{organizationId}/devices/statuses/overview | Return an overview of current device statuses |
| [**getOrganizationDevicesStatuses_2**](StatusesApi.md#getOrganizationDevicesStatuses_2) | **GET** /organizations/{organizationId}/devices/statuses | List the status of every Meraki device in the organization |
| [**getOrganizationUplinksStatuses_2**](StatusesApi.md#getOrganizationUplinksStatuses_2) | **GET** /organizations/{organizationId}/uplinks/statuses | List the uplink status of every Meraki MX, MG and Z series devices in the organization |
| [**getOrganizationWirelessDevicesEthernetStatuses_3**](StatusesApi.md#getOrganizationWirelessDevicesEthernetStatuses_3) | **GET** /organizations/{organizationId}/wireless/devices/ethernet/statuses | Endpoint to see power status for wireless devices |
| [**updateOrganizationCameraOnboardingStatuses_2**](StatusesApi.md#updateOrganizationCameraOnboardingStatuses_2) | **PUT** /organizations/{organizationId}/camera/onboarding/statuses | Notify that credential handoff to camera has completed |


<a id="getDeviceSwitchPortsStatusesPackets_2"></a>
# **getDeviceSwitchPortsStatusesPackets_2**
> List&lt;Object&gt; getDeviceSwitchPortsStatusesPackets_2(serial, t0, timespan)

Return the packet counters for all the ports of a switch

Return the packet counters for all the ports of a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StatusesApi apiInstance = new StatusesApi(defaultClient);
    String serial = "serial_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 1 day from today.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day.
    try {
      List<Object> result = apiInstance.getDeviceSwitchPortsStatusesPackets_2(serial, t0, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusesApi#getDeviceSwitchPortsStatusesPackets_2");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 1 day from today. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day. | [optional] |

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

<a id="getDeviceSwitchPortsStatuses_2"></a>
# **getDeviceSwitchPortsStatuses_2**
> List&lt;GetDeviceSwitchPortsStatuses200ResponseInner&gt; getDeviceSwitchPortsStatuses_2(serial, t0, timespan)

Return the status for all the ports of a switch

Return the status for all the ports of a switch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StatusesApi apiInstance = new StatusesApi(defaultClient);
    String serial = "serial_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    try {
      List<GetDeviceSwitchPortsStatuses200ResponseInner> result = apiInstance.getDeviceSwitchPortsStatuses_2(serial, t0, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusesApi#getDeviceSwitchPortsStatuses_2");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |

### Return type

[**List&lt;GetDeviceSwitchPortsStatuses200ResponseInner&gt;**](GetDeviceSwitchPortsStatuses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationApplianceUplinkStatuses_2"></a>
# **getOrganizationApplianceUplinkStatuses_2**
> List&lt;Object&gt; getOrganizationApplianceUplinkStatuses_2(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, iccids)

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
import org.openapitools.client.api.StatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StatusesApi apiInstance = new StatusesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | A list of network IDs. The returned devices will be filtered to only include these networks.
    List<String> serials = Arrays.asList(); // List<String> | A list of serial numbers. The returned devices will be filtered to only include these serials.
    List<String> iccids = Arrays.asList(); // List<String> | A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
    try {
      List<Object> result = apiInstance.getOrganizationApplianceUplinkStatuses_2(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, iccids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusesApi#getOrganizationApplianceUplinkStatuses_2");
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

<a id="getOrganizationApplianceVpnStatuses_2"></a>
# **getOrganizationApplianceVpnStatuses_2**
> List&lt;Object&gt; getOrganizationApplianceVpnStatuses_2(organizationId, perPage, startingAfter, endingBefore, networkIds)

Show VPN status for networks in an organization

Show VPN status for networks in an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StatusesApi apiInstance = new StatusesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 300. Default is 300.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456
    try {
      List<Object> result = apiInstance.getOrganizationApplianceVpnStatuses_2(organizationId, perPage, startingAfter, endingBefore, networkIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusesApi#getOrganizationApplianceVpnStatuses_2");
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
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 300. Default is 300. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]&#x3D;N_12345678&amp;networkIds[]&#x3D;L_3456 | [optional] |

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

<a id="getOrganizationCameraOnboardingStatuses_2"></a>
# **getOrganizationCameraOnboardingStatuses_2**
> List&lt;Object&gt; getOrganizationCameraOnboardingStatuses_2(organizationId, serials, networkIds)

Fetch onboarding status of cameras

Fetch onboarding status of cameras

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StatusesApi apiInstance = new StatusesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    List<String> serials = Arrays.asList(); // List<String> | A list of serial numbers. The returned cameras will be filtered to only include these serials.
    List<String> networkIds = Arrays.asList(); // List<String> | A list of network IDs. The returned cameras will be filtered to only include these networks.
    try {
      List<Object> result = apiInstance.getOrganizationCameraOnboardingStatuses_2(organizationId, serials, networkIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusesApi#getOrganizationCameraOnboardingStatuses_2");
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
| **serials** | [**List&lt;String&gt;**](String.md)| A list of serial numbers. The returned cameras will be filtered to only include these serials. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| A list of network IDs. The returned cameras will be filtered to only include these networks. | [optional] |

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

<a id="getOrganizationCellularGatewayUplinkStatuses_2"></a>
# **getOrganizationCellularGatewayUplinkStatuses_2**
> List&lt;GetOrganizationCellularGatewayUplinkStatuses200ResponseInner&gt; getOrganizationCellularGatewayUplinkStatuses_2(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, iccids)

List the uplink status of every Meraki MG cellular gateway in the organization

List the uplink status of every Meraki MG cellular gateway in the organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StatusesApi apiInstance = new StatusesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | A list of network IDs. The returned devices will be filtered to only include these networks.
    List<String> serials = Arrays.asList(); // List<String> | A list of serial numbers. The returned devices will be filtered to only include these serials.
    List<String> iccids = Arrays.asList(); // List<String> | A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
    try {
      List<GetOrganizationCellularGatewayUplinkStatuses200ResponseInner> result = apiInstance.getOrganizationCellularGatewayUplinkStatuses_2(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, iccids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusesApi#getOrganizationCellularGatewayUplinkStatuses_2");
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

[**List&lt;GetOrganizationCellularGatewayUplinkStatuses200ResponseInner&gt;**](GetOrganizationCellularGatewayUplinkStatuses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationDevicesPowerModulesStatusesByDevice_3"></a>
# **getOrganizationDevicesPowerModulesStatusesByDevice_3**
> List&lt;GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInner&gt; getOrganizationDevicesPowerModulesStatusesByDevice_3(organizationId, perPage, startingAfter, endingBefore, networkIds, productTypes, serials, tags, tagsFilterType)

List the power status information for devices in an organization

List the power status information for devices in an organization. The data returned by this endpoint is updated every 5 minutes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StatusesApi apiInstance = new StatusesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | Optional parameter to filter device availabilities by network ID. This filter uses multiple exact matches.
    List<String> productTypes = Arrays.asList(); // List<String> | Optional parameter to filter device availabilities by device product types. This filter uses multiple exact matches.
    List<String> serials = Arrays.asList(); // List<String> | Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
    List<String> tags = Arrays.asList(); // List<String> | An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches.
    String tagsFilterType = "withAllTags"; // String | An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
    try {
      List<GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInner> result = apiInstance.getOrganizationDevicesPowerModulesStatusesByDevice_3(organizationId, perPage, startingAfter, endingBefore, networkIds, productTypes, serials, tags, tagsFilterType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusesApi#getOrganizationDevicesPowerModulesStatusesByDevice_3");
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
| **networkIds** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter device availabilities by network ID. This filter uses multiple exact matches. | [optional] |
| **productTypes** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter device availabilities by device product types. This filter uses multiple exact matches. | [optional] |
| **serials** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches. | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below). This filter uses multiple exact matches. | [optional] |
| **tagsFilterType** | **String**| An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected. | [optional] [enum: withAllTags, withAnyTags] |

### Return type

[**List&lt;GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInner&gt;**](GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationDevicesStatusesOverview_2"></a>
# **getOrganizationDevicesStatusesOverview_2**
> GetOrganizationDevicesStatusesOverview200Response getOrganizationDevicesStatusesOverview_2(organizationId, productTypes, networkIds)

Return an overview of current device statuses

Return an overview of current device statuses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StatusesApi apiInstance = new StatusesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    List<String> productTypes = Arrays.asList(); // List<String> | An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
    List<String> networkIds = Arrays.asList(); // List<String> | An optional parameter to filter device statuses by network.
    try {
      GetOrganizationDevicesStatusesOverview200Response result = apiInstance.getOrganizationDevicesStatusesOverview_2(organizationId, productTypes, networkIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusesApi#getOrganizationDevicesStatusesOverview_2");
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
| **productTypes** | [**List&lt;String&gt;**](String.md)| An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor. | [optional] [enum: appliance, camera, cellularGateway, sensor, switch, systemsManager, wireless] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| An optional parameter to filter device statuses by network. | [optional] |

### Return type

[**GetOrganizationDevicesStatusesOverview200Response**](GetOrganizationDevicesStatusesOverview200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationDevicesStatuses_2"></a>
# **getOrganizationDevicesStatuses_2**
> GetOrganizationDevicesStatuses200Response getOrganizationDevicesStatuses_2(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, statuses, productTypes, models, tags, tagsFilterType)

List the status of every Meraki device in the organization

List the status of every Meraki device in the organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StatusesApi apiInstance = new StatusesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | Optional parameter to filter devices by network ids.
    List<String> serials = Arrays.asList(); // List<String> | Optional parameter to filter devices by serials.
    List<String> statuses = Arrays.asList(); // List<String> | Optional parameter to filter devices by statuses. Valid statuses are [\"online\", \"alerting\", \"offline\", \"dormant\"].
    List<String> productTypes = Arrays.asList(); // List<String> | An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
    List<String> models = Arrays.asList(); // List<String> | Optional parameter to filter devices by models.
    List<String> tags = Arrays.asList(); // List<String> | An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below).
    String tagsFilterType = "withAllTags"; // String | An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
    try {
      GetOrganizationDevicesStatuses200Response result = apiInstance.getOrganizationDevicesStatuses_2(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, statuses, productTypes, models, tags, tagsFilterType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusesApi#getOrganizationDevicesStatuses_2");
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
| **networkIds** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter devices by network ids. | [optional] |
| **serials** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter devices by serials. | [optional] |
| **statuses** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter devices by statuses. Valid statuses are [\&quot;online\&quot;, \&quot;alerting\&quot;, \&quot;offline\&quot;, \&quot;dormant\&quot;]. | [optional] [enum: alerting, dormant, offline, online] |
| **productTypes** | [**List&lt;String&gt;**](String.md)| An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor. | [optional] [enum: appliance, camera, cellularGateway, sensor, switch, systemsManager, wireless] |
| **models** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter devices by models. | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below). | [optional] |
| **tagsFilterType** | **String**| An optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected. | [optional] [enum: withAllTags, withAnyTags] |

### Return type

[**GetOrganizationDevicesStatuses200Response**](GetOrganizationDevicesStatuses200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationUplinksStatuses_2"></a>
# **getOrganizationUplinksStatuses_2**
> List&lt;GetOrganizationUplinksStatuses200ResponseInner&gt; getOrganizationUplinksStatuses_2(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, iccids)

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
import org.openapitools.client.api.StatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StatusesApi apiInstance = new StatusesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | A list of network IDs. The returned devices will be filtered to only include these networks.
    List<String> serials = Arrays.asList(); // List<String> | A list of serial numbers. The returned devices will be filtered to only include these serials.
    List<String> iccids = Arrays.asList(); // List<String> | A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
    try {
      List<GetOrganizationUplinksStatuses200ResponseInner> result = apiInstance.getOrganizationUplinksStatuses_2(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, iccids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusesApi#getOrganizationUplinksStatuses_2");
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

<a id="getOrganizationWirelessDevicesEthernetStatuses_3"></a>
# **getOrganizationWirelessDevicesEthernetStatuses_3**
> List&lt;GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner&gt; getOrganizationWirelessDevicesEthernetStatuses_3(organizationId, perPage, startingAfter, endingBefore, networkIds)

Endpoint to see power status for wireless devices

Endpoint to see power status for wireless devices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StatusesApi apiInstance = new StatusesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456
    try {
      List<GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner> result = apiInstance.getOrganizationWirelessDevicesEthernetStatuses_3(organizationId, perPage, startingAfter, endingBefore, networkIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusesApi#getOrganizationWirelessDevicesEthernetStatuses_3");
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
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]&#x3D;N_12345678&amp;networkIds[]&#x3D;L_3456 | [optional] |

### Return type

[**List&lt;GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner&gt;**](GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="updateOrganizationCameraOnboardingStatuses_2"></a>
# **updateOrganizationCameraOnboardingStatuses_2**
> Object updateOrganizationCameraOnboardingStatuses_2(organizationId, updateOrganizationCameraOnboardingStatusesRequest)

Notify that credential handoff to camera has completed

Notify that credential handoff to camera has completed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StatusesApi apiInstance = new StatusesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    UpdateOrganizationCameraOnboardingStatusesRequest updateOrganizationCameraOnboardingStatusesRequest = new UpdateOrganizationCameraOnboardingStatusesRequest(); // UpdateOrganizationCameraOnboardingStatusesRequest | 
    try {
      Object result = apiInstance.updateOrganizationCameraOnboardingStatuses_2(organizationId, updateOrganizationCameraOnboardingStatusesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusesApi#updateOrganizationCameraOnboardingStatuses_2");
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
| **updateOrganizationCameraOnboardingStatusesRequest** | [**UpdateOrganizationCameraOnboardingStatusesRequest**](UpdateOrganizationCameraOnboardingStatusesRequest.md)|  | [optional] |

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

