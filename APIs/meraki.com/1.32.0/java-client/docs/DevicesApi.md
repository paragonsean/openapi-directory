# DevicesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**blinkDeviceLeds**](DevicesApi.md#blinkDeviceLeds) | **POST** /devices/{serial}/blinkLeds | Blink the LEDs on a device |
| [**checkinNetworkSmDevices_1**](DevicesApi.md#checkinNetworkSmDevices_1) | **POST** /networks/{networkId}/sm/devices/checkin | Force check-in a set of devices |
| [**claimNetworkDevices_1**](DevicesApi.md#claimNetworkDevices_1) | **POST** /networks/{networkId}/devices/claim | Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed) |
| [**cloneOrganizationSwitchDevices_1**](DevicesApi.md#cloneOrganizationSwitchDevices_1) | **POST** /organizations/{organizationId}/switch/devices/clone | Clone port-level and some switch-level configuration settings from a source switch to one or more target switches |
| [**createDeviceLiveToolsPing**](DevicesApi.md#createDeviceLiveToolsPing) | **POST** /devices/{serial}/liveTools/ping | Enqueue a job to ping a target host from the device |
| [**createDeviceLiveToolsPingDevice**](DevicesApi.md#createDeviceLiveToolsPingDevice) | **POST** /devices/{serial}/liveTools/pingDevice | Enqueue a job to check connectivity status to the device |
| [**getDevice**](DevicesApi.md#getDevice) | **GET** /devices/{serial} | Return a single device |
| [**getDeviceCellularSims**](DevicesApi.md#getDeviceCellularSims) | **GET** /devices/{serial}/cellular/sims | Return the SIM and APN configurations for a cellular device. |
| [**getDeviceClients**](DevicesApi.md#getDeviceClients) | **GET** /devices/{serial}/clients | List the clients of a device, up to a maximum of a month ago |
| [**getDeviceLiveToolsPing**](DevicesApi.md#getDeviceLiveToolsPing) | **GET** /devices/{serial}/liveTools/ping/{id} | Return a ping job |
| [**getDeviceLiveToolsPingDevice**](DevicesApi.md#getDeviceLiveToolsPingDevice) | **GET** /devices/{serial}/liveTools/pingDevice/{id} | Return a ping device job |
| [**getDeviceLldpCdp**](DevicesApi.md#getDeviceLldpCdp) | **GET** /devices/{serial}/lldpCdp | List LLDP and CDP information for a device |
| [**getDeviceLossAndLatencyHistory**](DevicesApi.md#getDeviceLossAndLatencyHistory) | **GET** /devices/{serial}/lossAndLatencyHistory | Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device. |
| [**getDeviceManagementInterface**](DevicesApi.md#getDeviceManagementInterface) | **GET** /devices/{serial}/managementInterface | Return the management interface settings for a device |
| [**getNetworkDevices_1**](DevicesApi.md#getNetworkDevices_1) | **GET** /networks/{networkId}/devices | List the devices in a network |
| [**getNetworkSmDeviceCellularUsageHistory_1**](DevicesApi.md#getNetworkSmDeviceCellularUsageHistory_1) | **GET** /networks/{networkId}/sm/devices/{deviceId}/cellularUsageHistory | Return the client&#39;s daily cellular data usage history |
| [**getNetworkSmDeviceCerts_1**](DevicesApi.md#getNetworkSmDeviceCerts_1) | **GET** /networks/{networkId}/sm/devices/{deviceId}/certs | List the certs on a device |
| [**getNetworkSmDeviceConnectivity_1**](DevicesApi.md#getNetworkSmDeviceConnectivity_1) | **GET** /networks/{networkId}/sm/devices/{deviceId}/connectivity | Returns historical connectivity data (whether a device is regularly checking in to Dashboard). |
| [**getNetworkSmDeviceDesktopLogs_1**](DevicesApi.md#getNetworkSmDeviceDesktopLogs_1) | **GET** /networks/{networkId}/sm/devices/{deviceId}/desktopLogs | Return historical records of various Systems Manager network connection details for desktop devices. |
| [**getNetworkSmDeviceDeviceCommandLogs_1**](DevicesApi.md#getNetworkSmDeviceDeviceCommandLogs_1) | **GET** /networks/{networkId}/sm/devices/{deviceId}/deviceCommandLogs | Return historical records of commands sent to Systems Manager devices |
| [**getNetworkSmDeviceDeviceProfiles_1**](DevicesApi.md#getNetworkSmDeviceDeviceProfiles_1) | **GET** /networks/{networkId}/sm/devices/{deviceId}/deviceProfiles | Get the installed profiles associated with a device |
| [**getNetworkSmDeviceNetworkAdapters_1**](DevicesApi.md#getNetworkSmDeviceNetworkAdapters_1) | **GET** /networks/{networkId}/sm/devices/{deviceId}/networkAdapters | List the network adapters of a device |
| [**getNetworkSmDevicePerformanceHistory_1**](DevicesApi.md#getNetworkSmDevicePerformanceHistory_1) | **GET** /networks/{networkId}/sm/devices/{deviceId}/performanceHistory | Return historical records of various Systems Manager client metrics for desktop devices. |
| [**getNetworkSmDeviceRestrictions_1**](DevicesApi.md#getNetworkSmDeviceRestrictions_1) | **GET** /networks/{networkId}/sm/devices/{deviceId}/restrictions | List the restrictions on a device |
| [**getNetworkSmDeviceSecurityCenters_1**](DevicesApi.md#getNetworkSmDeviceSecurityCenters_1) | **GET** /networks/{networkId}/sm/devices/{deviceId}/securityCenters | List the security centers on a device |
| [**getNetworkSmDeviceSoftwares_1**](DevicesApi.md#getNetworkSmDeviceSoftwares_1) | **GET** /networks/{networkId}/sm/devices/{deviceId}/softwares | Get a list of softwares associated with a device |
| [**getNetworkSmDeviceWlanLists_1**](DevicesApi.md#getNetworkSmDeviceWlanLists_1) | **GET** /networks/{networkId}/sm/devices/{deviceId}/wlanLists | List the saved SSID names on a device |
| [**getNetworkSmDevices_1**](DevicesApi.md#getNetworkSmDevices_1) | **GET** /networks/{networkId}/sm/devices | List the devices enrolled in an SM network with various specified fields and filters |
| [**getNetworkWirelessDevicesConnectionStats_1**](DevicesApi.md#getNetworkWirelessDevicesConnectionStats_1) | **GET** /networks/{networkId}/wireless/devices/connectionStats | Aggregated connectivity info for this network, grouped by node |
| [**getNetworkWirelessDevicesLatencyStats_1**](DevicesApi.md#getNetworkWirelessDevicesLatencyStats_1) | **GET** /networks/{networkId}/wireless/devices/latencyStats | Aggregated latency info for this network, grouped by node |
| [**getOrganizationDevicesAvailabilities_1**](DevicesApi.md#getOrganizationDevicesAvailabilities_1) | **GET** /organizations/{organizationId}/devices/availabilities | List the availability information for devices in an organization |
| [**getOrganizationDevicesPowerModulesStatusesByDevice_1**](DevicesApi.md#getOrganizationDevicesPowerModulesStatusesByDevice_1) | **GET** /organizations/{organizationId}/devices/powerModules/statuses/byDevice | List the power status information for devices in an organization |
| [**getOrganizationDevicesStatusesOverview_1**](DevicesApi.md#getOrganizationDevicesStatusesOverview_1) | **GET** /organizations/{organizationId}/devices/statuses/overview | Return an overview of current device statuses |
| [**getOrganizationDevicesStatuses_1**](DevicesApi.md#getOrganizationDevicesStatuses_1) | **GET** /organizations/{organizationId}/devices/statuses | List the status of every Meraki device in the organization |
| [**getOrganizationDevicesUplinksAddressesByDevice_1**](DevicesApi.md#getOrganizationDevicesUplinksAddressesByDevice_1) | **GET** /organizations/{organizationId}/devices/uplinks/addresses/byDevice | List the current uplink addresses for devices in an organization. |
| [**getOrganizationDevicesUplinksLossAndLatency_1**](DevicesApi.md#getOrganizationDevicesUplinksLossAndLatency_1) | **GET** /organizations/{organizationId}/devices/uplinksLossAndLatency | Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago |
| [**getOrganizationDevices_1**](DevicesApi.md#getOrganizationDevices_1) | **GET** /organizations/{organizationId}/devices | List the devices in an organization |
| [**getOrganizationInventoryDevice_2**](DevicesApi.md#getOrganizationInventoryDevice_2) | **GET** /organizations/{organizationId}/inventory/devices/{serial} | Return a single device from the inventory of an organization |
| [**getOrganizationInventoryDevices_2**](DevicesApi.md#getOrganizationInventoryDevices_2) | **GET** /organizations/{organizationId}/inventory/devices | Return the device inventory for an organization |
| [**getOrganizationSummaryTopDevicesByUsage_3**](DevicesApi.md#getOrganizationSummaryTopDevicesByUsage_3) | **GET** /organizations/{organizationId}/summary/top/devices/byUsage | Return metrics for organization&#39;s top 10 devices sorted by data usage over given time range |
| [**getOrganizationSummaryTopDevicesModelsByUsage_3**](DevicesApi.md#getOrganizationSummaryTopDevicesModelsByUsage_3) | **GET** /organizations/{organizationId}/summary/top/devices/models/byUsage | Return metrics for organization&#39;s top 10 device models sorted by data usage over given time range |
| [**getOrganizationWirelessDevicesEthernetStatuses_1**](DevicesApi.md#getOrganizationWirelessDevicesEthernetStatuses_1) | **GET** /organizations/{organizationId}/wireless/devices/ethernet/statuses | Endpoint to see power status for wireless devices |
| [**lockNetworkSmDevices_1**](DevicesApi.md#lockNetworkSmDevices_1) | **POST** /networks/{networkId}/sm/devices/lock | Lock a set of devices |
| [**modifyNetworkSmDevicesTags_1**](DevicesApi.md#modifyNetworkSmDevicesTags_1) | **POST** /networks/{networkId}/sm/devices/modifyTags | Add, delete, or update the tags of a set of devices |
| [**moveNetworkSmDevices_1**](DevicesApi.md#moveNetworkSmDevices_1) | **POST** /networks/{networkId}/sm/devices/move | Move a set of devices to a new network |
| [**rebootDevice**](DevicesApi.md#rebootDevice) | **POST** /devices/{serial}/reboot | Reboot a device |
| [**refreshNetworkSmDeviceDetails_1**](DevicesApi.md#refreshNetworkSmDeviceDetails_1) | **POST** /networks/{networkId}/sm/devices/{deviceId}/refreshDetails | Refresh the details of a device |
| [**removeNetworkDevices_1**](DevicesApi.md#removeNetworkDevices_1) | **POST** /networks/{networkId}/devices/remove | Remove a single device |
| [**unenrollNetworkSmDevice_1**](DevicesApi.md#unenrollNetworkSmDevice_1) | **POST** /networks/{networkId}/sm/devices/{deviceId}/unenroll | Unenroll a device |
| [**updateDevice**](DevicesApi.md#updateDevice) | **PUT** /devices/{serial} | Update the attributes of a device |
| [**updateDeviceCellularSims**](DevicesApi.md#updateDeviceCellularSims) | **PUT** /devices/{serial}/cellular/sims | Updates the SIM and APN configurations for a cellular device. |
| [**updateDeviceManagementInterface**](DevicesApi.md#updateDeviceManagementInterface) | **PUT** /devices/{serial}/managementInterface | Update the management interface settings for a device |
| [**updateNetworkSmDevicesFields_1**](DevicesApi.md#updateNetworkSmDevicesFields_1) | **PUT** /networks/{networkId}/sm/devices/fields | Modify the fields of a device |
| [**vmxNetworkDevicesClaim_1**](DevicesApi.md#vmxNetworkDevicesClaim_1) | **POST** /networks/{networkId}/devices/claim/vmx | Claim a vMX into a network |
| [**wipeNetworkSmDevices_1**](DevicesApi.md#wipeNetworkSmDevices_1) | **POST** /networks/{networkId}/sm/devices/wipe | Wipe a device |


<a id="blinkDeviceLeds"></a>
# **blinkDeviceLeds**
> Object blinkDeviceLeds(serial, blinkDeviceLedsRequest)

Blink the LEDs on a device

Blink the LEDs on a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String serial = "serial_example"; // String | 
    BlinkDeviceLedsRequest blinkDeviceLedsRequest = new BlinkDeviceLedsRequest(); // BlinkDeviceLedsRequest | 
    try {
      Object result = apiInstance.blinkDeviceLeds(serial, blinkDeviceLedsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#blinkDeviceLeds");
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
| **blinkDeviceLedsRequest** | [**BlinkDeviceLedsRequest**](BlinkDeviceLedsRequest.md)|  | [optional] |

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
| **202** | Successful operation |  -  |

<a id="checkinNetworkSmDevices_1"></a>
# **checkinNetworkSmDevices_1**
> CheckinNetworkSmDevices200Response checkinNetworkSmDevices_1(networkId, checkinNetworkSmDevicesRequest)

Force check-in a set of devices

Force check-in a set of devices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CheckinNetworkSmDevicesRequest checkinNetworkSmDevicesRequest = new CheckinNetworkSmDevicesRequest(); // CheckinNetworkSmDevicesRequest | 
    try {
      CheckinNetworkSmDevices200Response result = apiInstance.checkinNetworkSmDevices_1(networkId, checkinNetworkSmDevicesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#checkinNetworkSmDevices_1");
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
| **checkinNetworkSmDevicesRequest** | [**CheckinNetworkSmDevicesRequest**](CheckinNetworkSmDevicesRequest.md)|  | [optional] |

### Return type

[**CheckinNetworkSmDevices200Response**](CheckinNetworkSmDevices200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="claimNetworkDevices_1"></a>
# **claimNetworkDevices_1**
> claimNetworkDevices_1(networkId, claimNetworkDevicesRequest)

Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed)

Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    ClaimNetworkDevicesRequest claimNetworkDevicesRequest = new ClaimNetworkDevicesRequest(); // ClaimNetworkDevicesRequest | 
    try {
      apiInstance.claimNetworkDevices_1(networkId, claimNetworkDevicesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#claimNetworkDevices_1");
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
| **claimNetworkDevicesRequest** | [**ClaimNetworkDevicesRequest**](ClaimNetworkDevicesRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="cloneOrganizationSwitchDevices_1"></a>
# **cloneOrganizationSwitchDevices_1**
> Object cloneOrganizationSwitchDevices_1(organizationId, cloneOrganizationSwitchDevicesRequest)

Clone port-level and some switch-level configuration settings from a source switch to one or more target switches

Clone port-level and some switch-level configuration settings from a source switch to one or more target switches. Cloned settings include: Aggregation Groups, Power Settings, Multicast Settings, MTU Configuration, STP Bridge priority, Port Mirroring

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CloneOrganizationSwitchDevicesRequest cloneOrganizationSwitchDevicesRequest = new CloneOrganizationSwitchDevicesRequest(); // CloneOrganizationSwitchDevicesRequest | 
    try {
      Object result = apiInstance.cloneOrganizationSwitchDevices_1(organizationId, cloneOrganizationSwitchDevicesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#cloneOrganizationSwitchDevices_1");
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
| **cloneOrganizationSwitchDevicesRequest** | [**CloneOrganizationSwitchDevicesRequest**](CloneOrganizationSwitchDevicesRequest.md)|  | |

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

<a id="createDeviceLiveToolsPing"></a>
# **createDeviceLiveToolsPing**
> CreateDeviceLiveToolsPing201Response createDeviceLiveToolsPing(serial, createDeviceLiveToolsPingRequest)

Enqueue a job to ping a target host from the device

Enqueue a job to ping a target host from the device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String serial = "serial_example"; // String | 
    CreateDeviceLiveToolsPingRequest createDeviceLiveToolsPingRequest = new CreateDeviceLiveToolsPingRequest(); // CreateDeviceLiveToolsPingRequest | 
    try {
      CreateDeviceLiveToolsPing201Response result = apiInstance.createDeviceLiveToolsPing(serial, createDeviceLiveToolsPingRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#createDeviceLiveToolsPing");
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
| **createDeviceLiveToolsPingRequest** | [**CreateDeviceLiveToolsPingRequest**](CreateDeviceLiveToolsPingRequest.md)|  | |

### Return type

[**CreateDeviceLiveToolsPing201Response**](CreateDeviceLiveToolsPing201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createDeviceLiveToolsPingDevice"></a>
# **createDeviceLiveToolsPingDevice**
> CreateDeviceLiveToolsPing201Response createDeviceLiveToolsPingDevice(serial, createDeviceLiveToolsPingDeviceRequest)

Enqueue a job to check connectivity status to the device

Enqueue a job to check connectivity status to the device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String serial = "serial_example"; // String | 
    CreateDeviceLiveToolsPingDeviceRequest createDeviceLiveToolsPingDeviceRequest = new CreateDeviceLiveToolsPingDeviceRequest(); // CreateDeviceLiveToolsPingDeviceRequest | 
    try {
      CreateDeviceLiveToolsPing201Response result = apiInstance.createDeviceLiveToolsPingDevice(serial, createDeviceLiveToolsPingDeviceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#createDeviceLiveToolsPingDevice");
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
| **createDeviceLiveToolsPingDeviceRequest** | [**CreateDeviceLiveToolsPingDeviceRequest**](CreateDeviceLiveToolsPingDeviceRequest.md)|  | [optional] |

### Return type

[**CreateDeviceLiveToolsPing201Response**](CreateDeviceLiveToolsPing201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="getDevice"></a>
# **getDevice**
> Object getDevice(serial)

Return a single device

Return a single device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDevice(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getDevice");
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

<a id="getDeviceCellularSims"></a>
# **getDeviceCellularSims**
> Object getDeviceCellularSims(serial)

Return the SIM and APN configurations for a cellular device.

Return the SIM and APN configurations for a cellular device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceCellularSims(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getDeviceCellularSims");
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

<a id="getDeviceClients"></a>
# **getDeviceClients**
> List&lt;Object&gt; getDeviceClients(serial, t0, timespan)

List the clients of a device, up to a maximum of a month ago

List the clients of a device, up to a maximum of a month ago. The usage of each client is returned in kilobytes. If the device is a switch, the switchport is returned; otherwise the switchport field is null.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String serial = "serial_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    try {
      List<Object> result = apiInstance.getDeviceClients(serial, t0, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getDeviceClients");
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

<a id="getDeviceLiveToolsPing"></a>
# **getDeviceLiveToolsPing**
> GetDeviceLiveToolsPing200Response getDeviceLiveToolsPing(serial, id)

Return a ping job

Return a ping job. Latency unit in response is in milliseconds. Size is in bytes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String serial = "serial_example"; // String | 
    String id = "id_example"; // String | 
    try {
      GetDeviceLiveToolsPing200Response result = apiInstance.getDeviceLiveToolsPing(serial, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getDeviceLiveToolsPing");
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
| **id** | **String**|  | |

### Return type

[**GetDeviceLiveToolsPing200Response**](GetDeviceLiveToolsPing200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceLiveToolsPingDevice"></a>
# **getDeviceLiveToolsPingDevice**
> GetDeviceLiveToolsPing200Response getDeviceLiveToolsPingDevice(serial, id)

Return a ping device job

Return a ping device job. Latency unit in response is in milliseconds. Size is in bytes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String serial = "serial_example"; // String | 
    String id = "id_example"; // String | 
    try {
      GetDeviceLiveToolsPing200Response result = apiInstance.getDeviceLiveToolsPingDevice(serial, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getDeviceLiveToolsPingDevice");
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
| **id** | **String**|  | |

### Return type

[**GetDeviceLiveToolsPing200Response**](GetDeviceLiveToolsPing200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getDeviceLldpCdp"></a>
# **getDeviceLldpCdp**
> Object getDeviceLldpCdp(serial)

List LLDP and CDP information for a device

List LLDP and CDP information for a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceLldpCdp(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getDeviceLldpCdp");
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

<a id="getDeviceLossAndLatencyHistory"></a>
# **getDeviceLossAndLatencyHistory**
> List&lt;Object&gt; getDeviceLossAndLatencyHistory(serial, ip, t0, t1, timespan, resolution, uplink)

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
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String serial = "serial_example"; // String | 
    String ip = "ip_example"; // String | The destination IP used to obtain the requested stats. This is required.
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    Integer resolution = 56; // Integer | The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60.
    String uplink = "cellular"; // String | The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, cellular. The default is wan1.
    try {
      List<Object> result = apiInstance.getDeviceLossAndLatencyHistory(serial, ip, t0, t1, timespan, resolution, uplink);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getDeviceLossAndLatencyHistory");
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

<a id="getDeviceManagementInterface"></a>
# **getDeviceManagementInterface**
> Object getDeviceManagementInterface(serial)

Return the management interface settings for a device

Return the management interface settings for a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.getDeviceManagementInterface(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getDeviceManagementInterface");
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

<a id="getNetworkDevices_1"></a>
# **getNetworkDevices_1**
> List&lt;Object&gt; getNetworkDevices_1(networkId)

List the devices in a network

List the devices in a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkDevices_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getNetworkDevices_1");
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

<a id="getNetworkSmDeviceCellularUsageHistory_1"></a>
# **getNetworkSmDeviceCellularUsageHistory_1**
> List&lt;GetNetworkSmDeviceCellularUsageHistory200ResponseInner&gt; getNetworkSmDeviceCellularUsageHistory_1(networkId, deviceId)

Return the client&#39;s daily cellular data usage history

Return the client&#39;s daily cellular data usage history. Usage data is in kilobytes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    try {
      List<GetNetworkSmDeviceCellularUsageHistory200ResponseInner> result = apiInstance.getNetworkSmDeviceCellularUsageHistory_1(networkId, deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getNetworkSmDeviceCellularUsageHistory_1");
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
| **deviceId** | **String**|  | |

### Return type

[**List&lt;GetNetworkSmDeviceCellularUsageHistory200ResponseInner&gt;**](GetNetworkSmDeviceCellularUsageHistory200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSmDeviceCerts_1"></a>
# **getNetworkSmDeviceCerts_1**
> List&lt;GetNetworkSmDeviceCerts200ResponseInner&gt; getNetworkSmDeviceCerts_1(networkId, deviceId)

List the certs on a device

List the certs on a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    try {
      List<GetNetworkSmDeviceCerts200ResponseInner> result = apiInstance.getNetworkSmDeviceCerts_1(networkId, deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getNetworkSmDeviceCerts_1");
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
| **deviceId** | **String**|  | |

### Return type

[**List&lt;GetNetworkSmDeviceCerts200ResponseInner&gt;**](GetNetworkSmDeviceCerts200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSmDeviceConnectivity_1"></a>
# **getNetworkSmDeviceConnectivity_1**
> List&lt;GetNetworkSmDeviceConnectivity200ResponseInner&gt; getNetworkSmDeviceConnectivity_1(networkId, deviceId, perPage, startingAfter, endingBefore)

Returns historical connectivity data (whether a device is regularly checking in to Dashboard).

Returns historical connectivity data (whether a device is regularly checking in to Dashboard).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<GetNetworkSmDeviceConnectivity200ResponseInner> result = apiInstance.getNetworkSmDeviceConnectivity_1(networkId, deviceId, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getNetworkSmDeviceConnectivity_1");
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
| **deviceId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

### Return type

[**List&lt;GetNetworkSmDeviceConnectivity200ResponseInner&gt;**](GetNetworkSmDeviceConnectivity200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkSmDeviceDesktopLogs_1"></a>
# **getNetworkSmDeviceDesktopLogs_1**
> List&lt;GetNetworkSmDeviceDesktopLogs200ResponseInner&gt; getNetworkSmDeviceDesktopLogs_1(networkId, deviceId, perPage, startingAfter, endingBefore)

Return historical records of various Systems Manager network connection details for desktop devices.

Return historical records of various Systems Manager network connection details for desktop devices.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<GetNetworkSmDeviceDesktopLogs200ResponseInner> result = apiInstance.getNetworkSmDeviceDesktopLogs_1(networkId, deviceId, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getNetworkSmDeviceDesktopLogs_1");
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
| **deviceId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

### Return type

[**List&lt;GetNetworkSmDeviceDesktopLogs200ResponseInner&gt;**](GetNetworkSmDeviceDesktopLogs200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkSmDeviceDeviceCommandLogs_1"></a>
# **getNetworkSmDeviceDeviceCommandLogs_1**
> List&lt;GetNetworkSmDeviceDeviceCommandLogs200ResponseInner&gt; getNetworkSmDeviceDeviceCommandLogs_1(networkId, deviceId, perPage, startingAfter, endingBefore)

Return historical records of commands sent to Systems Manager devices

Return historical records of commands sent to Systems Manager devices. Note that this will include the name of the Dashboard user who initiated the command if it was generated by a Dashboard admin rather than the automatic behavior of the system; you may wish to filter this out of any reports.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<GetNetworkSmDeviceDeviceCommandLogs200ResponseInner> result = apiInstance.getNetworkSmDeviceDeviceCommandLogs_1(networkId, deviceId, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getNetworkSmDeviceDeviceCommandLogs_1");
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
| **deviceId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

### Return type

[**List&lt;GetNetworkSmDeviceDeviceCommandLogs200ResponseInner&gt;**](GetNetworkSmDeviceDeviceCommandLogs200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkSmDeviceDeviceProfiles_1"></a>
# **getNetworkSmDeviceDeviceProfiles_1**
> List&lt;GetNetworkSmDeviceDeviceProfiles200ResponseInner&gt; getNetworkSmDeviceDeviceProfiles_1(networkId, deviceId)

Get the installed profiles associated with a device

Get the installed profiles associated with a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    try {
      List<GetNetworkSmDeviceDeviceProfiles200ResponseInner> result = apiInstance.getNetworkSmDeviceDeviceProfiles_1(networkId, deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getNetworkSmDeviceDeviceProfiles_1");
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
| **deviceId** | **String**|  | |

### Return type

[**List&lt;GetNetworkSmDeviceDeviceProfiles200ResponseInner&gt;**](GetNetworkSmDeviceDeviceProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSmDeviceNetworkAdapters_1"></a>
# **getNetworkSmDeviceNetworkAdapters_1**
> List&lt;GetNetworkSmDeviceNetworkAdapters200ResponseInner&gt; getNetworkSmDeviceNetworkAdapters_1(networkId, deviceId)

List the network adapters of a device

List the network adapters of a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    try {
      List<GetNetworkSmDeviceNetworkAdapters200ResponseInner> result = apiInstance.getNetworkSmDeviceNetworkAdapters_1(networkId, deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getNetworkSmDeviceNetworkAdapters_1");
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
| **deviceId** | **String**|  | |

### Return type

[**List&lt;GetNetworkSmDeviceNetworkAdapters200ResponseInner&gt;**](GetNetworkSmDeviceNetworkAdapters200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSmDevicePerformanceHistory_1"></a>
# **getNetworkSmDevicePerformanceHistory_1**
> List&lt;GetNetworkSmDevicePerformanceHistory200ResponseInner&gt; getNetworkSmDevicePerformanceHistory_1(networkId, deviceId, perPage, startingAfter, endingBefore)

Return historical records of various Systems Manager client metrics for desktop devices.

Return historical records of various Systems Manager client metrics for desktop devices.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<GetNetworkSmDevicePerformanceHistory200ResponseInner> result = apiInstance.getNetworkSmDevicePerformanceHistory_1(networkId, deviceId, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getNetworkSmDevicePerformanceHistory_1");
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
| **deviceId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

### Return type

[**List&lt;GetNetworkSmDevicePerformanceHistory200ResponseInner&gt;**](GetNetworkSmDevicePerformanceHistory200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkSmDeviceRestrictions_1"></a>
# **getNetworkSmDeviceRestrictions_1**
> List&lt;Object&gt; getNetworkSmDeviceRestrictions_1(networkId, deviceId)

List the restrictions on a device

List the restrictions on a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkSmDeviceRestrictions_1(networkId, deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getNetworkSmDeviceRestrictions_1");
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
| **deviceId** | **String**|  | |

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

<a id="getNetworkSmDeviceSecurityCenters_1"></a>
# **getNetworkSmDeviceSecurityCenters_1**
> List&lt;GetNetworkSmDeviceSecurityCenters200ResponseInner&gt; getNetworkSmDeviceSecurityCenters_1(networkId, deviceId)

List the security centers on a device

List the security centers on a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    try {
      List<GetNetworkSmDeviceSecurityCenters200ResponseInner> result = apiInstance.getNetworkSmDeviceSecurityCenters_1(networkId, deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getNetworkSmDeviceSecurityCenters_1");
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
| **deviceId** | **String**|  | |

### Return type

[**List&lt;GetNetworkSmDeviceSecurityCenters200ResponseInner&gt;**](GetNetworkSmDeviceSecurityCenters200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSmDeviceSoftwares_1"></a>
# **getNetworkSmDeviceSoftwares_1**
> List&lt;GetNetworkSmDeviceSoftwares200ResponseInner&gt; getNetworkSmDeviceSoftwares_1(networkId, deviceId)

Get a list of softwares associated with a device

Get a list of softwares associated with a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    try {
      List<GetNetworkSmDeviceSoftwares200ResponseInner> result = apiInstance.getNetworkSmDeviceSoftwares_1(networkId, deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getNetworkSmDeviceSoftwares_1");
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
| **deviceId** | **String**|  | |

### Return type

[**List&lt;GetNetworkSmDeviceSoftwares200ResponseInner&gt;**](GetNetworkSmDeviceSoftwares200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSmDeviceWlanLists_1"></a>
# **getNetworkSmDeviceWlanLists_1**
> List&lt;GetNetworkSmDeviceWlanLists200ResponseInner&gt; getNetworkSmDeviceWlanLists_1(networkId, deviceId)

List the saved SSID names on a device

List the saved SSID names on a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    try {
      List<GetNetworkSmDeviceWlanLists200ResponseInner> result = apiInstance.getNetworkSmDeviceWlanLists_1(networkId, deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getNetworkSmDeviceWlanLists_1");
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
| **deviceId** | **String**|  | |

### Return type

[**List&lt;GetNetworkSmDeviceWlanLists200ResponseInner&gt;**](GetNetworkSmDeviceWlanLists200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSmDevices_1"></a>
# **getNetworkSmDevices_1**
> List&lt;GetNetworkSmDevices200ResponseInner&gt; getNetworkSmDevices_1(networkId, fields, wifiMacs, serials, ids, scope, perPage, startingAfter, endingBefore)

List the devices enrolled in an SM network with various specified fields and filters

List the devices enrolled in an SM network with various specified fields and filters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    List<String> fields = Arrays.asList(); // List<String> | Additional fields that will be displayed for each device.     The default fields are: id, name, tags, ssid, wifiMac, osName, systemModel, uuid, and serialNumber. The additional fields are: ip,     systemType, availableDeviceCapacity, kioskAppName, biosVersion, lastConnected, missingAppsCount, userSuppliedAddress, location, lastUser,     ownerEmail, ownerUsername, osBuild, publicIp, phoneNumber, diskInfoJson, deviceCapacity, isManaged, hadMdm, isSupervised, meid, imei, iccid,     simCarrierNetwork, cellularDataUsed, isHotspotEnabled, createdAt, batteryEstCharge, quarantined, avName, avRunning, asName, fwName,     isRooted, loginRequired, screenLockEnabled, screenLockDelay, autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent, diskEncryptionEnabled,     hardwareEncryptionCaps, passCodeLock, usesHardwareKeystore, androidSecurityPatchVersion, and url.
    List<String> wifiMacs = Arrays.asList(); // List<String> | Filter devices by wifi mac(s).
    List<String> serials = Arrays.asList(); // List<String> | Filter devices by serial(s).
    List<String> ids = Arrays.asList(); // List<String> | Filter devices by id(s).
    List<String> scope = Arrays.asList(); // List<String> | Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags.
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<GetNetworkSmDevices200ResponseInner> result = apiInstance.getNetworkSmDevices_1(networkId, fields, wifiMacs, serials, ids, scope, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getNetworkSmDevices_1");
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
| **fields** | [**List&lt;String&gt;**](String.md)| Additional fields that will be displayed for each device.     The default fields are: id, name, tags, ssid, wifiMac, osName, systemModel, uuid, and serialNumber. The additional fields are: ip,     systemType, availableDeviceCapacity, kioskAppName, biosVersion, lastConnected, missingAppsCount, userSuppliedAddress, location, lastUser,     ownerEmail, ownerUsername, osBuild, publicIp, phoneNumber, diskInfoJson, deviceCapacity, isManaged, hadMdm, isSupervised, meid, imei, iccid,     simCarrierNetwork, cellularDataUsed, isHotspotEnabled, createdAt, batteryEstCharge, quarantined, avName, avRunning, asName, fwName,     isRooted, loginRequired, screenLockEnabled, screenLockDelay, autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent, diskEncryptionEnabled,     hardwareEncryptionCaps, passCodeLock, usesHardwareKeystore, androidSecurityPatchVersion, and url. | [optional] |
| **wifiMacs** | [**List&lt;String&gt;**](String.md)| Filter devices by wifi mac(s). | [optional] |
| **serials** | [**List&lt;String&gt;**](String.md)| Filter devices by serial(s). | [optional] |
| **ids** | [**List&lt;String&gt;**](String.md)| Filter devices by id(s). | [optional] |
| **scope** | [**List&lt;String&gt;**](String.md)| Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags. | [optional] |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

### Return type

[**List&lt;GetNetworkSmDevices200ResponseInner&gt;**](GetNetworkSmDevices200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getNetworkWirelessDevicesConnectionStats_1"></a>
# **getNetworkWirelessDevicesConnectionStats_1**
> List&lt;GetDeviceWirelessConnectionStats200Response&gt; getNetworkWirelessDevicesConnectionStats_1(networkId, t0, t1, timespan, band, ssid, vlan, apTag)

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
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
    String band = "2.4"; // String | Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
    Integer ssid = 56; // Integer | Filter results by SSID
    Integer vlan = 56; // Integer | Filter results by VLAN
    String apTag = "apTag_example"; // String | Filter results by AP Tag
    try {
      List<GetDeviceWirelessConnectionStats200Response> result = apiInstance.getNetworkWirelessDevicesConnectionStats_1(networkId, t0, t1, timespan, band, ssid, vlan, apTag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getNetworkWirelessDevicesConnectionStats_1");
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

<a id="getNetworkWirelessDevicesLatencyStats_1"></a>
# **getNetworkWirelessDevicesLatencyStats_1**
> List&lt;Object&gt; getNetworkWirelessDevicesLatencyStats_1(networkId, t0, t1, timespan, band, ssid, vlan, apTag, fields)

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
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
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
      List<Object> result = apiInstance.getNetworkWirelessDevicesLatencyStats_1(networkId, t0, t1, timespan, band, ssid, vlan, apTag, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getNetworkWirelessDevicesLatencyStats_1");
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

<a id="getOrganizationDevicesAvailabilities_1"></a>
# **getOrganizationDevicesAvailabilities_1**
> List&lt;GetOrganizationDevicesAvailabilities200ResponseInner&gt; getOrganizationDevicesAvailabilities_1(organizationId, perPage, startingAfter, endingBefore, networkIds, productTypes, serials, tags, tagsFilterType)

List the availability information for devices in an organization

List the availability information for devices in an organization. The data returned by this endpoint is updated every 5 minutes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
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
      List<GetOrganizationDevicesAvailabilities200ResponseInner> result = apiInstance.getOrganizationDevicesAvailabilities_1(organizationId, perPage, startingAfter, endingBefore, networkIds, productTypes, serials, tags, tagsFilterType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getOrganizationDevicesAvailabilities_1");
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

[**List&lt;GetOrganizationDevicesAvailabilities200ResponseInner&gt;**](GetOrganizationDevicesAvailabilities200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationDevicesPowerModulesStatusesByDevice_1"></a>
# **getOrganizationDevicesPowerModulesStatusesByDevice_1**
> List&lt;GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInner&gt; getOrganizationDevicesPowerModulesStatusesByDevice_1(organizationId, perPage, startingAfter, endingBefore, networkIds, productTypes, serials, tags, tagsFilterType)

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
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
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
      List<GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInner> result = apiInstance.getOrganizationDevicesPowerModulesStatusesByDevice_1(organizationId, perPage, startingAfter, endingBefore, networkIds, productTypes, serials, tags, tagsFilterType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getOrganizationDevicesPowerModulesStatusesByDevice_1");
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

<a id="getOrganizationDevicesStatusesOverview_1"></a>
# **getOrganizationDevicesStatusesOverview_1**
> GetOrganizationDevicesStatusesOverview200Response getOrganizationDevicesStatusesOverview_1(organizationId, productTypes, networkIds)

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
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    List<String> productTypes = Arrays.asList(); // List<String> | An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
    List<String> networkIds = Arrays.asList(); // List<String> | An optional parameter to filter device statuses by network.
    try {
      GetOrganizationDevicesStatusesOverview200Response result = apiInstance.getOrganizationDevicesStatusesOverview_1(organizationId, productTypes, networkIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getOrganizationDevicesStatusesOverview_1");
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

<a id="getOrganizationDevicesStatuses_1"></a>
# **getOrganizationDevicesStatuses_1**
> GetOrganizationDevicesStatuses200Response getOrganizationDevicesStatuses_1(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, statuses, productTypes, models, tags, tagsFilterType)

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
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
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
      GetOrganizationDevicesStatuses200Response result = apiInstance.getOrganizationDevicesStatuses_1(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, statuses, productTypes, models, tags, tagsFilterType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getOrganizationDevicesStatuses_1");
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

<a id="getOrganizationDevicesUplinksAddressesByDevice_1"></a>
# **getOrganizationDevicesUplinksAddressesByDevice_1**
> List&lt;GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner&gt; getOrganizationDevicesUplinksAddressesByDevice_1(organizationId, perPage, startingAfter, endingBefore, networkIds, productTypes, serials, tags, tagsFilterType)

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
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
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
      List<GetOrganizationDevicesUplinksAddressesByDevice200ResponseInner> result = apiInstance.getOrganizationDevicesUplinksAddressesByDevice_1(organizationId, perPage, startingAfter, endingBefore, networkIds, productTypes, serials, tags, tagsFilterType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getOrganizationDevicesUplinksAddressesByDevice_1");
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

<a id="getOrganizationDevicesUplinksLossAndLatency_1"></a>
# **getOrganizationDevicesUplinksLossAndLatency_1**
> List&lt;GetOrganizationDevicesUplinksLossAndLatency200ResponseInner&gt; getOrganizationDevicesUplinksLossAndLatency_1(organizationId, t0, t1, timespan, uplink, ip)

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
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes.
    String uplink = "cellular"; // String | Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks.
    String ip = "ip_example"; // String | Optional filter for a specific destination IP. Default will return all destination IPs.
    try {
      List<GetOrganizationDevicesUplinksLossAndLatency200ResponseInner> result = apiInstance.getOrganizationDevicesUplinksLossAndLatency_1(organizationId, t0, t1, timespan, uplink, ip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getOrganizationDevicesUplinksLossAndLatency_1");
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

<a id="getOrganizationDevices_1"></a>
# **getOrganizationDevices_1**
> List&lt;GetOrganizationDevices200ResponseInner&gt; getOrganizationDevices_1(organizationId, perPage, startingAfter, endingBefore, configurationUpdatedAfter, networkIds, productTypes, tags, tagsFilterType, name, mac, serial, model, macs, serials, sensorMetrics, sensorAlertProfileIds, models)

List the devices in an organization

List the devices in an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String configurationUpdatedAfter = "configurationUpdatedAfter_example"; // String | Filter results by whether or not the device's configuration has been updated after the given timestamp
    List<String> networkIds = Arrays.asList(); // List<String> | Optional parameter to filter devices by network.
    List<String> productTypes = Arrays.asList(); // List<String> | Optional parameter to filter devices by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
    List<String> tags = Arrays.asList(); // List<String> | Optional parameter to filter devices by tags.
    String tagsFilterType = "withAllTags"; // String | Optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
    String name = "name_example"; // String | Optional parameter to filter devices by name. All returned devices will have a name that contains the search term or is an exact match.
    String mac = "mac_example"; // String | Optional parameter to filter devices by MAC address. All returned devices will have a MAC address that contains the search term or is an exact match.
    String serial = "serial_example"; // String | Optional parameter to filter devices by serial number. All returned devices will have a serial number that contains the search term or is an exact match.
    String model = "model_example"; // String | Optional parameter to filter devices by model. All returned devices will have a model that contains the search term or is an exact match.
    List<String> macs = Arrays.asList(); // List<String> | Optional parameter to filter devices by one or more MAC addresses. All returned devices will have a MAC address that is an exact match.
    List<String> serials = Arrays.asList(); // List<String> | Optional parameter to filter devices by one or more serial numbers. All returned devices will have a serial number that is an exact match.
    List<String> sensorMetrics = Arrays.asList(); // List<String> | Optional parameter to filter devices by the metrics that they provide. Only applies to sensor devices.
    List<String> sensorAlertProfileIds = Arrays.asList(); // List<String> | Optional parameter to filter devices by the alert profiles that are bound to them. Only applies to sensor devices.
    List<String> models = Arrays.asList(); // List<String> | Optional parameter to filter devices by one or more models. All returned devices will have a model that is an exact match.
    try {
      List<GetOrganizationDevices200ResponseInner> result = apiInstance.getOrganizationDevices_1(organizationId, perPage, startingAfter, endingBefore, configurationUpdatedAfter, networkIds, productTypes, tags, tagsFilterType, name, mac, serial, model, macs, serials, sensorMetrics, sensorAlertProfileIds, models);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getOrganizationDevices_1");
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
| **configurationUpdatedAfter** | **String**| Filter results by whether or not the device&#39;s configuration has been updated after the given timestamp | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter devices by network. | [optional] |
| **productTypes** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter devices by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor. | [optional] [enum: appliance, camera, cellularGateway, sensor, switch, systemsManager, wireless] |
| **tags** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter devices by tags. | [optional] |
| **tagsFilterType** | **String**| Optional parameter of value &#39;withAnyTags&#39; or &#39;withAllTags&#39; to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, &#39;withAnyTags&#39; will be selected. | [optional] [enum: withAllTags, withAnyTags] |
| **name** | **String**| Optional parameter to filter devices by name. All returned devices will have a name that contains the search term or is an exact match. | [optional] |
| **mac** | **String**| Optional parameter to filter devices by MAC address. All returned devices will have a MAC address that contains the search term or is an exact match. | [optional] |
| **serial** | **String**| Optional parameter to filter devices by serial number. All returned devices will have a serial number that contains the search term or is an exact match. | [optional] |
| **model** | **String**| Optional parameter to filter devices by model. All returned devices will have a model that contains the search term or is an exact match. | [optional] |
| **macs** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter devices by one or more MAC addresses. All returned devices will have a MAC address that is an exact match. | [optional] |
| **serials** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter devices by one or more serial numbers. All returned devices will have a serial number that is an exact match. | [optional] |
| **sensorMetrics** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter devices by the metrics that they provide. Only applies to sensor devices. | [optional] |
| **sensorAlertProfileIds** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter devices by the alert profiles that are bound to them. Only applies to sensor devices. | [optional] |
| **models** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter devices by one or more models. All returned devices will have a model that is an exact match. | [optional] |

### Return type

[**List&lt;GetOrganizationDevices200ResponseInner&gt;**](GetOrganizationDevices200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationInventoryDevice_2"></a>
# **getOrganizationInventoryDevice_2**
> GetOrganizationInventoryDevices200ResponseInner getOrganizationInventoryDevice_2(organizationId, serial)

Return a single device from the inventory of an organization

Return a single device from the inventory of an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String serial = "serial_example"; // String | 
    try {
      GetOrganizationInventoryDevices200ResponseInner result = apiInstance.getOrganizationInventoryDevice_2(organizationId, serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getOrganizationInventoryDevice_2");
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
| **serial** | **String**|  | |

### Return type

[**GetOrganizationInventoryDevices200ResponseInner**](GetOrganizationInventoryDevices200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationInventoryDevices_2"></a>
# **getOrganizationInventoryDevices_2**
> List&lt;GetOrganizationInventoryDevices200ResponseInner&gt; getOrganizationInventoryDevices_2(organizationId, perPage, startingAfter, endingBefore, usedState, search, macs, networkIds, serials, models, orderNumbers, tags, tagsFilterType, productTypes)

Return the device inventory for an organization

Return the device inventory for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String usedState = "unused"; // String | Filter results by used or unused inventory. Accepted values are 'used' or 'unused'.
    String search = "search_example"; // String | Search for devices in inventory based on serial number, mac address, or model.
    List<String> macs = Arrays.asList(); // List<String> | Search for devices in inventory based on mac addresses.
    List<String> networkIds = Arrays.asList(); // List<String> | Search for devices in inventory based on network ids.
    List<String> serials = Arrays.asList(); // List<String> | Search for devices in inventory based on serials.
    List<String> models = Arrays.asList(); // List<String> | Search for devices in inventory based on model.
    List<String> orderNumbers = Arrays.asList(); // List<String> | Search for devices in inventory based on order numbers.
    List<String> tags = Arrays.asList(); // List<String> | Filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below).
    String tagsFilterType = "withAllTags"; // String | To use with 'tags' parameter, to filter devices which contain ANY or ALL given tags. Accepted values are 'withAnyTags' or 'withAllTags', default is 'withAnyTags'.
    List<String> productTypes = Arrays.asList(); // List<String> | Filter devices by product type. Accepted values are appliance, camera, cellularGateway, sensor, switch, systemsManager, and wireless.
    try {
      List<GetOrganizationInventoryDevices200ResponseInner> result = apiInstance.getOrganizationInventoryDevices_2(organizationId, perPage, startingAfter, endingBefore, usedState, search, macs, networkIds, serials, models, orderNumbers, tags, tagsFilterType, productTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getOrganizationInventoryDevices_2");
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
| **usedState** | **String**| Filter results by used or unused inventory. Accepted values are &#39;used&#39; or &#39;unused&#39;. | [optional] [enum: unused, used] |
| **search** | **String**| Search for devices in inventory based on serial number, mac address, or model. | [optional] |
| **macs** | [**List&lt;String&gt;**](String.md)| Search for devices in inventory based on mac addresses. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| Search for devices in inventory based on network ids. | [optional] |
| **serials** | [**List&lt;String&gt;**](String.md)| Search for devices in inventory based on serials. | [optional] |
| **models** | [**List&lt;String&gt;**](String.md)| Search for devices in inventory based on model. | [optional] |
| **orderNumbers** | [**List&lt;String&gt;**](String.md)| Search for devices in inventory based on order numbers. | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| Filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below). | [optional] |
| **tagsFilterType** | **String**| To use with &#39;tags&#39; parameter, to filter devices which contain ANY or ALL given tags. Accepted values are &#39;withAnyTags&#39; or &#39;withAllTags&#39;, default is &#39;withAnyTags&#39;. | [optional] [enum: withAllTags, withAnyTags] |
| **productTypes** | [**List&lt;String&gt;**](String.md)| Filter devices by product type. Accepted values are appliance, camera, cellularGateway, sensor, switch, systemsManager, and wireless. | [optional] [enum: appliance, camera, cellularGateway, sensor, switch, systemsManager, wireless] |

### Return type

[**List&lt;GetOrganizationInventoryDevices200ResponseInner&gt;**](GetOrganizationInventoryDevices200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationSummaryTopDevicesByUsage_3"></a>
# **getOrganizationSummaryTopDevicesByUsage_3**
> List&lt;GetOrganizationSummaryTopDevicesByUsage200ResponseInner&gt; getOrganizationSummaryTopDevicesByUsage_3(organizationId, t0, t1, timespan)

Return metrics for organization&#39;s top 10 devices sorted by data usage over given time range

Return metrics for organization&#39;s top 10 devices sorted by data usage over given time range. Default unit is megabytes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    try {
      List<GetOrganizationSummaryTopDevicesByUsage200ResponseInner> result = apiInstance.getOrganizationSummaryTopDevicesByUsage_3(organizationId, t0, t1, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getOrganizationSummaryTopDevicesByUsage_3");
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
| **t0** | **String**| The beginning of the timespan for the data. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |

### Return type

[**List&lt;GetOrganizationSummaryTopDevicesByUsage200ResponseInner&gt;**](GetOrganizationSummaryTopDevicesByUsage200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationSummaryTopDevicesModelsByUsage_3"></a>
# **getOrganizationSummaryTopDevicesModelsByUsage_3**
> List&lt;GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInner&gt; getOrganizationSummaryTopDevicesModelsByUsage_3(organizationId, t0, t1, timespan)

Return metrics for organization&#39;s top 10 device models sorted by data usage over given time range

Return metrics for organization&#39;s top 10 device models sorted by data usage over given time range. Default unit is megabytes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    try {
      List<GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInner> result = apiInstance.getOrganizationSummaryTopDevicesModelsByUsage_3(organizationId, t0, t1, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getOrganizationSummaryTopDevicesModelsByUsage_3");
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
| **t0** | **String**| The beginning of the timespan for the data. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |

### Return type

[**List&lt;GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInner&gt;**](GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationWirelessDevicesEthernetStatuses_1"></a>
# **getOrganizationWirelessDevicesEthernetStatuses_1**
> List&lt;GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner&gt; getOrganizationWirelessDevicesEthernetStatuses_1(organizationId, perPage, startingAfter, endingBefore, networkIds)

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
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456
    try {
      List<GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner> result = apiInstance.getOrganizationWirelessDevicesEthernetStatuses_1(organizationId, perPage, startingAfter, endingBefore, networkIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#getOrganizationWirelessDevicesEthernetStatuses_1");
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

<a id="lockNetworkSmDevices_1"></a>
# **lockNetworkSmDevices_1**
> CheckinNetworkSmDevices200Response lockNetworkSmDevices_1(networkId, lockNetworkSmDevicesRequest)

Lock a set of devices

Lock a set of devices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    LockNetworkSmDevicesRequest lockNetworkSmDevicesRequest = new LockNetworkSmDevicesRequest(); // LockNetworkSmDevicesRequest | 
    try {
      CheckinNetworkSmDevices200Response result = apiInstance.lockNetworkSmDevices_1(networkId, lockNetworkSmDevicesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#lockNetworkSmDevices_1");
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
| **lockNetworkSmDevicesRequest** | [**LockNetworkSmDevicesRequest**](LockNetworkSmDevicesRequest.md)|  | [optional] |

### Return type

[**CheckinNetworkSmDevices200Response**](CheckinNetworkSmDevices200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="modifyNetworkSmDevicesTags_1"></a>
# **modifyNetworkSmDevicesTags_1**
> List&lt;ModifyNetworkSmDevicesTags200ResponseInner&gt; modifyNetworkSmDevicesTags_1(networkId, modifyNetworkSmDevicesTagsRequest)

Add, delete, or update the tags of a set of devices

Add, delete, or update the tags of a set of devices

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    ModifyNetworkSmDevicesTagsRequest modifyNetworkSmDevicesTagsRequest = new ModifyNetworkSmDevicesTagsRequest(); // ModifyNetworkSmDevicesTagsRequest | 
    try {
      List<ModifyNetworkSmDevicesTags200ResponseInner> result = apiInstance.modifyNetworkSmDevicesTags_1(networkId, modifyNetworkSmDevicesTagsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#modifyNetworkSmDevicesTags_1");
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
| **modifyNetworkSmDevicesTagsRequest** | [**ModifyNetworkSmDevicesTagsRequest**](ModifyNetworkSmDevicesTagsRequest.md)|  | |

### Return type

[**List&lt;ModifyNetworkSmDevicesTags200ResponseInner&gt;**](ModifyNetworkSmDevicesTags200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="moveNetworkSmDevices_1"></a>
# **moveNetworkSmDevices_1**
> MoveNetworkSmDevices200Response moveNetworkSmDevices_1(networkId, moveNetworkSmDevicesRequest)

Move a set of devices to a new network

Move a set of devices to a new network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    MoveNetworkSmDevicesRequest moveNetworkSmDevicesRequest = new MoveNetworkSmDevicesRequest(); // MoveNetworkSmDevicesRequest | 
    try {
      MoveNetworkSmDevices200Response result = apiInstance.moveNetworkSmDevices_1(networkId, moveNetworkSmDevicesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#moveNetworkSmDevices_1");
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
| **moveNetworkSmDevicesRequest** | [**MoveNetworkSmDevicesRequest**](MoveNetworkSmDevicesRequest.md)|  | |

### Return type

[**MoveNetworkSmDevices200Response**](MoveNetworkSmDevices200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="rebootDevice"></a>
# **rebootDevice**
> Object rebootDevice(serial)

Reboot a device

Reboot a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      Object result = apiInstance.rebootDevice(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#rebootDevice");
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

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successful operation |  -  |

<a id="refreshNetworkSmDeviceDetails_1"></a>
# **refreshNetworkSmDeviceDetails_1**
> refreshNetworkSmDeviceDetails_1(networkId, deviceId)

Refresh the details of a device

Refresh the details of a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    try {
      apiInstance.refreshNetworkSmDeviceDetails_1(networkId, deviceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#refreshNetworkSmDeviceDetails_1");
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
| **deviceId** | **String**|  | |

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
| **200** | Successful operation |  -  |

<a id="removeNetworkDevices_1"></a>
# **removeNetworkDevices_1**
> removeNetworkDevices_1(networkId, removeNetworkDevicesRequest)

Remove a single device

Remove a single device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    RemoveNetworkDevicesRequest removeNetworkDevicesRequest = new RemoveNetworkDevicesRequest(); // RemoveNetworkDevicesRequest | 
    try {
      apiInstance.removeNetworkDevices_1(networkId, removeNetworkDevicesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#removeNetworkDevices_1");
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
| **removeNetworkDevicesRequest** | [**RemoveNetworkDevicesRequest**](RemoveNetworkDevicesRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="unenrollNetworkSmDevice_1"></a>
# **unenrollNetworkSmDevice_1**
> Object unenrollNetworkSmDevice_1(networkId, deviceId)

Unenroll a device

Unenroll a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String deviceId = "deviceId_example"; // String | 
    try {
      Object result = apiInstance.unenrollNetworkSmDevice_1(networkId, deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#unenrollNetworkSmDevice_1");
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
| **deviceId** | **String**|  | |

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

<a id="updateDevice"></a>
# **updateDevice**
> Object updateDevice(serial, updateDeviceRequest)

Update the attributes of a device

Update the attributes of a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceRequest updateDeviceRequest = new UpdateDeviceRequest(); // UpdateDeviceRequest | 
    try {
      Object result = apiInstance.updateDevice(serial, updateDeviceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#updateDevice");
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
| **updateDeviceRequest** | [**UpdateDeviceRequest**](UpdateDeviceRequest.md)|  | [optional] |

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

<a id="updateDeviceCellularSims"></a>
# **updateDeviceCellularSims**
> Object updateDeviceCellularSims(serial, updateDeviceCellularSimsRequest)

Updates the SIM and APN configurations for a cellular device.

Updates the SIM and APN configurations for a cellular device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceCellularSimsRequest updateDeviceCellularSimsRequest = new UpdateDeviceCellularSimsRequest(); // UpdateDeviceCellularSimsRequest | 
    try {
      Object result = apiInstance.updateDeviceCellularSims(serial, updateDeviceCellularSimsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#updateDeviceCellularSims");
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
| **updateDeviceCellularSimsRequest** | [**UpdateDeviceCellularSimsRequest**](UpdateDeviceCellularSimsRequest.md)|  | [optional] |

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

<a id="updateDeviceManagementInterface"></a>
# **updateDeviceManagementInterface**
> Object updateDeviceManagementInterface(serial, updateDeviceManagementInterfaceRequest)

Update the management interface settings for a device

Update the management interface settings for a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceManagementInterfaceRequest updateDeviceManagementInterfaceRequest = new UpdateDeviceManagementInterfaceRequest(); // UpdateDeviceManagementInterfaceRequest | 
    try {
      Object result = apiInstance.updateDeviceManagementInterface(serial, updateDeviceManagementInterfaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#updateDeviceManagementInterface");
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
| **updateDeviceManagementInterfaceRequest** | [**UpdateDeviceManagementInterfaceRequest**](UpdateDeviceManagementInterfaceRequest.md)|  | [optional] |

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

<a id="updateNetworkSmDevicesFields_1"></a>
# **updateNetworkSmDevicesFields_1**
> List&lt;UpdateNetworkSmDevicesFields200ResponseInner&gt; updateNetworkSmDevicesFields_1(networkId, updateNetworkSmDevicesFieldsRequest)

Modify the fields of a device

Modify the fields of a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSmDevicesFieldsRequest updateNetworkSmDevicesFieldsRequest = new UpdateNetworkSmDevicesFieldsRequest(); // UpdateNetworkSmDevicesFieldsRequest | 
    try {
      List<UpdateNetworkSmDevicesFields200ResponseInner> result = apiInstance.updateNetworkSmDevicesFields_1(networkId, updateNetworkSmDevicesFieldsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#updateNetworkSmDevicesFields_1");
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
| **updateNetworkSmDevicesFieldsRequest** | [**UpdateNetworkSmDevicesFieldsRequest**](UpdateNetworkSmDevicesFieldsRequest.md)|  | |

### Return type

[**List&lt;UpdateNetworkSmDevicesFields200ResponseInner&gt;**](UpdateNetworkSmDevicesFields200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="vmxNetworkDevicesClaim_1"></a>
# **vmxNetworkDevicesClaim_1**
> Object vmxNetworkDevicesClaim_1(networkId, vmxNetworkDevicesClaimRequest)

Claim a vMX into a network

Claim a vMX into a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    VmxNetworkDevicesClaimRequest vmxNetworkDevicesClaimRequest = new VmxNetworkDevicesClaimRequest(); // VmxNetworkDevicesClaimRequest | 
    try {
      Object result = apiInstance.vmxNetworkDevicesClaim_1(networkId, vmxNetworkDevicesClaimRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#vmxNetworkDevicesClaim_1");
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
| **vmxNetworkDevicesClaimRequest** | [**VmxNetworkDevicesClaimRequest**](VmxNetworkDevicesClaimRequest.md)|  | |

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

<a id="wipeNetworkSmDevices_1"></a>
# **wipeNetworkSmDevices_1**
> WipeNetworkSmDevices200Response wipeNetworkSmDevices_1(networkId, wipeNetworkSmDevicesRequest)

Wipe a device

Wipe a device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    WipeNetworkSmDevicesRequest wipeNetworkSmDevicesRequest = new WipeNetworkSmDevicesRequest(); // WipeNetworkSmDevicesRequest | 
    try {
      WipeNetworkSmDevices200Response result = apiInstance.wipeNetworkSmDevices_1(networkId, wipeNetworkSmDevicesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#wipeNetworkSmDevices_1");
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
| **wipeNetworkSmDevicesRequest** | [**WipeNetworkSmDevicesRequest**](WipeNetworkSmDevicesRequest.md)|  | [optional] |

### Return type

[**WipeNetworkSmDevices200Response**](WipeNetworkSmDevices200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

