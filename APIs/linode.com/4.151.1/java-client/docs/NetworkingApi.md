# NetworkingApi

All URIs are relative to *https://api.linode.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**allocateIP**](NetworkingApi.md#allocateIP) | **POST** /networking/ips | IP Address Allocate |
| [**assignIPs**](NetworkingApi.md#assignIPs) | **POST** /networking/ips/assign | IP Addresses Assign |
| [**assignIPv4s**](NetworkingApi.md#assignIPv4s) | **POST** /networking/ipv4/assign | Linodes Assign IPv4s |
| [**createFirewallDevice**](NetworkingApi.md#createFirewallDevice) | **POST** /networking/firewalls/{firewallId}/devices | Firewall Device Create |
| [**createFirewalls**](NetworkingApi.md#createFirewalls) | **POST** /networking/firewalls | Firewall Create |
| [**deleteFirewall**](NetworkingApi.md#deleteFirewall) | **DELETE** /networking/firewalls/{firewallId} | Firewall Delete |
| [**deleteFirewallDevice**](NetworkingApi.md#deleteFirewallDevice) | **DELETE** /networking/firewalls/{firewallId}/devices/{deviceId} | Firewall Device Delete |
| [**deleteIPv6Range**](NetworkingApi.md#deleteIPv6Range) | **DELETE** /networking/ipv6/ranges/{range} | IPv6 Range Delete |
| [**getFirewall**](NetworkingApi.md#getFirewall) | **GET** /networking/firewalls/{firewallId} | Firewall View |
| [**getFirewallDevice**](NetworkingApi.md#getFirewallDevice) | **GET** /networking/firewalls/{firewallId}/devices/{deviceId} | Firewall Device View |
| [**getFirewallDevices**](NetworkingApi.md#getFirewallDevices) | **GET** /networking/firewalls/{firewallId}/devices | Firewall Devices List |
| [**getFirewallRules**](NetworkingApi.md#getFirewallRules) | **GET** /networking/firewalls/{firewallId}/rules | Firewall Rules List |
| [**getFirewalls**](NetworkingApi.md#getFirewalls) | **GET** /networking/firewalls | Firewalls List |
| [**getIP**](NetworkingApi.md#getIP) | **GET** /networking/ips/{address} | IP Address View |
| [**getIPs**](NetworkingApi.md#getIPs) | **GET** /networking/ips | IP Addresses List |
| [**getIPv6Pools**](NetworkingApi.md#getIPv6Pools) | **GET** /networking/ipv6/pools | IPv6 Pools List |
| [**getIPv6Range**](NetworkingApi.md#getIPv6Range) | **GET** /networking/ipv6/ranges/{range} | IPv6 Range View |
| [**getIPv6Ranges**](NetworkingApi.md#getIPv6Ranges) | **GET** /networking/ipv6/ranges | IPv6 Ranges List |
| [**getVLANs**](NetworkingApi.md#getVLANs) | **GET** /networking/vlans | VLANs List |
| [**postIPv6Range**](NetworkingApi.md#postIPv6Range) | **POST** /networking/ipv6/ranges | IPv6 Range Create |
| [**shareIPs**](NetworkingApi.md#shareIPs) | **POST** /networking/ips/share | IP Addresses Share |
| [**shareIPv4s**](NetworkingApi.md#shareIPv4s) | **POST** /networking/ipv4/share | IPv4 Sharing Configure |
| [**updateFirewall**](NetworkingApi.md#updateFirewall) | **PUT** /networking/firewalls/{firewallId} | Firewall Update |
| [**updateFirewallRules**](NetworkingApi.md#updateFirewallRules) | **PUT** /networking/firewalls/{firewallId}/rules | Firewall Rules Update |
| [**updateIP**](NetworkingApi.md#updateIP) | **PUT** /networking/ips/{address} | IP Address RDNS Update |


<a id="allocateIP"></a>
# **allocateIP**
> IPAddress allocateIP(allocateIPRequest)

IP Address Allocate

Allocates a new IPv4 Address on your Account. The Linode must be configured to support additional addresses - please [open a support ticket](/docs/api/support/#support-ticket-open) requesting additional addresses before attempting allocation. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    AllocateIPRequest allocateIPRequest = new AllocateIPRequest(); // AllocateIPRequest | Information about the address you are creating.
    try {
      IPAddress result = apiInstance.allocateIP(allocateIPRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#allocateIP");
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
| **allocateIPRequest** | [**AllocateIPRequest**](AllocateIPRequest.md)| Information about the address you are creating. | |

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | IP Address allocated successfully. |  -  |
| **0** | Error |  -  |

<a id="assignIPs"></a>
# **assignIPs**
> Object assignIPs(ipAddressesAssignRequest)

IP Addresses Assign

Assign multiple IPv4 addresses and/or IPv6 ranges to multiple Linodes in one Region. This allows swapping, shuffling, or otherwise reorganizing IPs to your Linodes.  The following restrictions apply: * All Linodes involved must have at least one public IPv4 address after assignment. * Linodes may have no more than one assigned private IPv4 address. * Linodes may have no more than one assigned IPv6 range.  [Open a Support Ticket](/docs/api/support/#support-ticket-open) to request additional IPv4 addresses or IPv6 ranges beyond standard account limits.  **Note**: Removing an IP address that has been set as a Managed Linode&#39;s &#x60;ssh.ip&#x60; causes the Managed Linode&#39;s SSH access settings to reset to their default values. To view and configure Managed Linode SSH settings, use the following commands: * **Linode&#39;s Managed Settings View** ([GET /managed/linode-settings/{linodeId}](/docs/api/managed/#linodes-managed-settings-view)) * **Linode&#39;s Managed Settings Update** ([PUT /managed/linode-settings/{linodeId}](/docs/api/managed/#linodes-managed-settings-update)) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    IPAddressesAssignRequest ipAddressesAssignRequest = new IPAddressesAssignRequest(); // IPAddressesAssignRequest | Information about what IPv4 address or IPv6 range to assign, and to which Linode. 
    try {
      Object result = apiInstance.assignIPs(ipAddressesAssignRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#assignIPs");
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
| **ipAddressesAssignRequest** | [**IPAddressesAssignRequest**](IPAddressesAssignRequest.md)| Information about what IPv4 address or IPv6 range to assign, and to which Linode.  | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All assignments completed successfully. |  -  |
| **0** | Error |  -  |

<a id="assignIPv4s"></a>
# **assignIPv4s**
> Object assignIPv4s(ipAddressesAssignRequest)

Linodes Assign IPv4s

This command is equivalent to **IP Addresses Assign** ([POST /networking/ips/assign](#ip-addresses-assign)).  Assign multiple IPv4 addresses and/or IPv6 ranges to multiple Linodes in one Region. This allows swapping, shuffling, or otherwise reorganizing IPs to your Linodes.  The following restrictions apply: * All Linodes involved must have at least one public IPv4 address after assignment. * Linodes may have no more than one assigned private IPv4 address. * Linodes may have no more than one assigned IPv6 range.  [Open a Support Ticket](/docs/api/support/#support-ticket-open) to request additional IPv4 addresses or IPv6 ranges beyond standard account limits.  **Note**: Removing an IP address that has been set as a Managed Linode&#39;s &#x60;ssh.ip&#x60; causes the Managed Linode&#39;s SSH access settings to reset to their default values. To view and configure Managed Linode SSH settings, use the following commands: * **Linode&#39;s Managed Settings View** ([GET /managed/linode-settings/{linodeId}](/docs/api/managed/#linodes-managed-settings-view)) * **Linode&#39;s Managed Settings Update** ([PUT /managed/linode-settings/{linodeId}](/docs/api/managed/#linodes-managed-settings-update)) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    IPAddressesAssignRequest ipAddressesAssignRequest = new IPAddressesAssignRequest(); // IPAddressesAssignRequest | Information about what IPv4 address to assign, and to which Linode. 
    try {
      Object result = apiInstance.assignIPv4s(ipAddressesAssignRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#assignIPv4s");
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
| **ipAddressesAssignRequest** | [**IPAddressesAssignRequest**](IPAddressesAssignRequest.md)| Information about what IPv4 address to assign, and to which Linode.  | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All assignments completed successfully. |  -  |
| **0** | Error |  -  |

<a id="createFirewallDevice"></a>
# **createFirewallDevice**
> FirewallDevices createFirewallDevice(firewallId, UNKNOWN_BASE_TYPE)

Firewall Device Create

Creates a Firewall Device, which assigns a Firewall to a service (referred to as the Device&#39;s &#x60;entity&#x60;) and applies the Firewall&#39;s Rules to the device.  * Currently, only Devices with an entity of type &#x60;linode&#x60; are accepted.  * A Firewall can be assigned to multiple Linode instances at a time.  * A Linode instance can have one active, assigned Firewall at a time. Additional disabled Firewalls can be assigned to a service, but they cannot be enabled if another active Firewall is already assigned to the same service.  * A &#x60;firewall_device_add&#x60; Event is generated when the Firewall Device is added successfully. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    Integer firewallId = 56; // Integer | ID of the Firewall to access. 
    UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE = new HashMap(); // UNKNOWN_BASE_TYPE | 
    try {
      FirewallDevices result = apiInstance.createFirewallDevice(firewallId, UNKNOWN_BASE_TYPE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#createFirewallDevice");
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
| **firewallId** | **Integer**| ID of the Firewall to access.  | |
| **UNKNOWN_BASE_TYPE** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | [optional] |

### Return type

[**FirewallDevices**](FirewallDevices.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns information about the created Firewall Device. |  -  |
| **0** | Error |  -  |

<a id="createFirewalls"></a>
# **createFirewalls**
> Firewall createFirewalls(createFirewallsRequest)

Firewall Create

Creates a Firewall to filter network traffic.  * Use the &#x60;rules&#x60; property to create inbound and outbound access rules.  * Use the &#x60;devices&#x60; property to assign the Firewall to a service and apply its Rules to the device. Requires &#x60;read_write&#x60; [User&#39;s Grants](/docs/api/account/#users-grants-view) to the device. Currently, Firewalls can only be assigned to Linode instances.  * A Firewall can be assigned to multiple Linode instances at a time.  * A Linode instance can have one active, assigned Firewall at a time. Additional disabled Firewalls can be assigned to a service, but they cannot be enabled if another active Firewall is already assigned to the same service.  * A &#x60;firewall_create&#x60; Event is generated when this endpoint returns successfully. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    CreateFirewallsRequest createFirewallsRequest = new CreateFirewallsRequest(); // CreateFirewallsRequest | Creates a Firewall object that can be applied to a Linode service to filter the service's network traffic.
    try {
      Firewall result = apiInstance.createFirewalls(createFirewallsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#createFirewalls");
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
| **createFirewallsRequest** | [**CreateFirewallsRequest**](CreateFirewallsRequest.md)| Creates a Firewall object that can be applied to a Linode service to filter the service&#39;s network traffic. | [optional] |

### Return type

[**Firewall**](Firewall.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns information about the created Firewall. |  -  |
| **0** | Error |  -  |

<a id="deleteFirewall"></a>
# **deleteFirewall**
> Object deleteFirewall(firewallId)

Firewall Delete

Delete a Firewall resource by its ID. This will remove all of the Firewall&#39;s Rules from any Linode services that the Firewall was assigned to.  A &#x60;firewall_delete&#x60; Event is generated when this endpoint returns successfully. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    Integer firewallId = 56; // Integer | ID of the Firewall to access. 
    try {
      Object result = apiInstance.deleteFirewall(firewallId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#deleteFirewall");
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
| **firewallId** | **Integer**| ID of the Firewall to access.  | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete Successful. |  -  |
| **0** | Error |  -  |

<a id="deleteFirewallDevice"></a>
# **deleteFirewallDevice**
> Object deleteFirewallDevice(firewallId, deviceId)

Firewall Device Delete

Removes a Firewall Device, which removes a Firewall from the Linode service it was assigned to by the Device. This will remove all of the Firewall&#39;s Rules from the Linode service. If any other Firewalls have been assigned to the Linode service, then those Rules will remain in effect.  A &#x60;firewall_device_remove&#x60; Event is generated when the Firewall Device is removed successfully. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    Integer firewallId = 56; // Integer | ID of the Firewall to access. 
    Integer deviceId = 56; // Integer | ID of the Firewall Device to access. 
    try {
      Object result = apiInstance.deleteFirewallDevice(firewallId, deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#deleteFirewallDevice");
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
| **firewallId** | **Integer**| ID of the Firewall to access.  | |
| **deviceId** | **Integer**| ID of the Firewall Device to access.  | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete Successful. |  -  |
| **0** | Error |  -  |

<a id="deleteIPv6Range"></a>
# **deleteIPv6Range**
> Object deleteIPv6Range(range)

IPv6 Range Delete

Removes this IPv6 range from your account and disconnects the range from any assigned Linodes.  **Note:** Shared IPv6 ranges cannot be deleted at this time. Please contact Customer Support for assistance. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    String range = "range_example"; // String | The IPv6 range to access. Corresponds to the `range` property of objects returned from the IPv6 Ranges List ([GET /networking/ipv6/ranges](/docs/api/networking/#ipv6-ranges-list)) command.  **Note**: Omit the prefix length of the IPv6 range. 
    try {
      Object result = apiInstance.deleteIPv6Range(range);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#deleteIPv6Range");
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
| **range** | **String**| The IPv6 range to access. Corresponds to the &#x60;range&#x60; property of objects returned from the IPv6 Ranges List ([GET /networking/ipv6/ranges](/docs/api/networking/#ipv6-ranges-list)) command.  **Note**: Omit the prefix length of the IPv6 range.  | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | IPv6 Range deleted. |  -  |
| **0** | Error |  -  |

<a id="getFirewall"></a>
# **getFirewall**
> Firewall getFirewall(firewallId)

Firewall View

Get a specific Firewall resource by its ID. The Firewall&#39;s Devices will not be returned in the response. Instead, use the [List Firewall Devices](/docs/api/networking/#firewall-devices-list) endpoint to review them. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    Integer firewallId = 56; // Integer | ID of the Firewall to access. 
    try {
      Firewall result = apiInstance.getFirewall(firewallId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#getFirewall");
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
| **firewallId** | **Integer**| ID of the Firewall to access.  | |

### Return type

[**Firewall**](Firewall.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns information about this Firewall. |  -  |
| **0** | Error |  -  |

<a id="getFirewallDevice"></a>
# **getFirewallDevice**
> FirewallDevices getFirewallDevice(firewallId, deviceId)

Firewall Device View

Returns information for a Firewall Device, which assigns a Firewall to a Linode service (referred to as the Device&#39;s &#x60;entity&#x60;). Currently, only Devices with an entity of type &#x60;linode&#x60; are accepted. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    Integer firewallId = 56; // Integer | ID of the Firewall to access. 
    Integer deviceId = 56; // Integer | ID of the Firewall Device to access. 
    try {
      FirewallDevices result = apiInstance.getFirewallDevice(firewallId, deviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#getFirewallDevice");
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
| **firewallId** | **Integer**| ID of the Firewall to access.  | |
| **deviceId** | **Integer**| ID of the Firewall Device to access.  | |

### Return type

[**FirewallDevices**](FirewallDevices.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested Firewall Device. |  -  |
| **0** | Error |  -  |

<a id="getFirewallDevices"></a>
# **getFirewallDevices**
> GetFirewallDevices200Response getFirewallDevices(firewallId, page, pageSize)

Firewall Devices List

Returns a paginated list of a Firewall&#39;s Devices. A Firewall Device assigns a Firewall to a Linode service (referred to as the Device&#39;s &#x60;entity&#x60;). Currently, only Devices with an entity of type &#x60;linode&#x60; are accepted. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    Integer firewallId = 56; // Integer | ID of the Firewall to access. 
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetFirewallDevices200Response result = apiInstance.getFirewallDevices(firewallId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#getFirewallDevices");
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
| **firewallId** | **Integer**| ID of the Firewall to access.  | |
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetFirewallDevices200Response**](GetFirewallDevices200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of Firewall Devices |  -  |
| **0** | Error |  -  |

<a id="getFirewallRules"></a>
# **getFirewallRules**
> FirewallRules getFirewallRules(firewallId)

Firewall Rules List

Returns the inbound and outbound Rules for a Firewall. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    Integer firewallId = 56; // Integer | ID of the Firewall to access. 
    try {
      FirewallRules result = apiInstance.getFirewallRules(firewallId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#getFirewallRules");
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
| **firewallId** | **Integer**| ID of the Firewall to access.  | |

### Return type

[**FirewallRules**](FirewallRules.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested Firewall Rules. |  -  |
| **0** | Error |  -  |

<a id="getFirewalls"></a>
# **getFirewalls**
> GetLinodeFirewalls200Response getFirewalls(page, pageSize)

Firewalls List

Returns a paginated list of accessible Firewalls. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetLinodeFirewalls200Response result = apiInstance.getFirewalls(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#getFirewalls");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetLinodeFirewalls200Response**](GetLinodeFirewalls200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of Firewalls. |  -  |
| **0** | Error |  -  |

<a id="getIP"></a>
# **getIP**
> IPAddress getIP(address)

IP Address View

Returns information about a single IP Address on your Account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    String address = "address_example"; // String | The address to operate on.
    try {
      IPAddress result = apiInstance.getIP(address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#getIP");
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
| **address** | **String**| The address to operate on. | |

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The requested IP Address. |  -  |
| **0** | Error |  -  |

<a id="getIPs"></a>
# **getIPs**
> GetIPs200Response getIPs()

IP Addresses List

Returns a paginated list of IP Addresses on your Account, excluding private addresses. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    try {
      GetIPs200Response result = apiInstance.getIPs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#getIPs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetIPs200Response**](GetIPs200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of IP Addresses. |  -  |
| **0** | Error |  -  |

<a id="getIPv6Pools"></a>
# **getIPv6Pools**
> GetIPv6Pools200Response getIPv6Pools(page, pageSize)

IPv6 Pools List

Displays the IPv6 pools on your Account. A pool of IPv6 addresses are routed to all of your Linodes in a single [Region](/docs/api/regions/#regions-list). Any Linode on your Account may bring up any address in this pool at any time, with no external configuration required. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetIPv6Pools200Response result = apiInstance.getIPv6Pools(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#getIPv6Pools");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetIPv6Pools200Response**](GetIPv6Pools200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The IPv6 pools on your Account. |  -  |
| **0** | Error |  -  |

<a id="getIPv6Range"></a>
# **getIPv6Range**
> IPv6RangeBGP getIPv6Range(range)

IPv6 Range View

View IPv6 range information. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    String range = "range_example"; // String | The IPv6 range to access. Corresponds to the `range` property of objects returned from the IPv6 Ranges List ([GET /networking/ipv6/ranges](/docs/api/networking/#ipv6-ranges-list)) command.  **Note**: Omit the prefix length of the IPv6 range. 
    try {
      IPv6RangeBGP result = apiInstance.getIPv6Range(range);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#getIPv6Range");
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
| **range** | **String**| The IPv6 range to access. Corresponds to the &#x60;range&#x60; property of objects returned from the IPv6 Ranges List ([GET /networking/ipv6/ranges](/docs/api/networking/#ipv6-ranges-list)) command.  **Note**: Omit the prefix length of the IPv6 range.  | |

### Return type

[**IPv6RangeBGP**](IPv6RangeBGP.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns IPv6 range information. |  -  |
| **0** | Error |  -  |

<a id="getIPv6Ranges"></a>
# **getIPv6Ranges**
> GetIPv6Ranges200Response getIPv6Ranges(page, pageSize)

IPv6 Ranges List

Displays the IPv6 ranges on your Account.     * An IPv6 range is a &#x60;/64&#x60; or &#x60;/54&#x60; block of IPv6 addresses routed to a single Linode in a given [Region](/docs/api/regions/#regions-list).    * Your Linode is responsible for routing individual addresses in the range, or handling traffic for all the addresses in the range.    * Access the IPv6 Range Create ([POST /networking/ipv6/ranges](/docs/api/networking/#ipv6-range-create)) endpoint to add a &#x60;/64&#x60; or &#x60;/56&#x60; block of IPv6 addresses to your account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetIPv6Ranges200Response result = apiInstance.getIPv6Ranges(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#getIPv6Ranges");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetIPv6Ranges200Response**](GetIPv6Ranges200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The IPv6 ranges on your Account. |  -  |
| **0** | Error |  -  |

<a id="getVLANs"></a>
# **getVLANs**
> GetVLANs200Response getVLANs(page, pageSize)

VLANs List

Returns a list of all Virtual Local Area Networks (VLANs) on your Account. VLANs provide a mechanism for secure communication between two or more Linodes that are assigned to the same VLAN and are both within the same Layer 2 broadcast domain.  VLANs are created and attached to Linodes by using the &#x60;interfaces&#x60; property for the following endpoints:  - Linode Create ([POST /linode/instances](/docs/api/linode-instances/#linode-create)) - Configuration Profile Create ([POST /linode/instances/{linodeId}/configs](/docs/api/linode-instances/#configuration-profile-create)) - Configuration Profile Update ([PUT /linode/instances/{linodeId}/configs/{configId}](/docs/api/linode-instances/#configuration-profile-update))  There are several ways to detach a VLAN from a Linode:  - [Update](/docs/api/linode-instances/#configuration-profile-update) the active Configuration Profile to remove the VLAN interface, then [reboot](/docs/api/linode-instances/#linode-reboot) the Linode. - [Create](/docs/api/linode-instances/#configuration-profile-create) a new Configuration Profile without the VLAN interface, then [reboot](/docs/api/linode-instances/#linode-reboot) the Linode into the new Configuration Profile. - [Delete](/docs/api/linode-instances/#linode-delete) the Linode.  **Note:** Only Next Generation Network (NGN) data centers support VLANs. Use the Regions ([/regions](/docs/api/regions/)) endpoint to view the capabilities of data center regions. If a VLAN is attached to your Linode and you attempt to migrate or clone it to a non-NGN data center, the migration or cloning will not initiate. If a Linode cannot be migrated because of an incompatibility, you will be prompted to select a different data center or contact support.  **Note:** See the [VLANs Overview](/docs/products/networking/vlans/#technical-specifications) to view additional specifications and limitations. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetVLANs200Response result = apiInstance.getVLANs(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#getVLANs");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetVLANs200Response**](GetVLANs200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The VLANs available on this Account. |  -  |
| **0** | Error |  -  |

<a id="postIPv6Range"></a>
# **postIPv6Range**
> PostIPv6Range200Response postIPv6Range(postIPv6RangeRequest)

IPv6 Range Create

Creates an IPv6 Range and assigns it based on the provided Linode or route target IPv6 SLAAC address. See the &#x60;ipv6&#x60; property when accessing the Linode View ([GET /linode/instances/{linodeId}](/docs/api/linode-instances/#linode-view)) endpoint to view a Linode&#39;s IPv6 SLAAC address.   * Either &#x60;linode_id&#x60; or &#x60;route_target&#x60; is required in a request.   * &#x60;linode_id&#x60; and &#x60;route_target&#x60; are mutually exclusive. Submitting values for both properties in a request results in an error.   * Upon a successful request, an IPv6 range is created in the [Region](/docs/api/regions/#regions-list) that corresponds to the provided &#x60;linode_id&#x60; or &#x60;route_target&#x60;.   * Your Linode is responsible for routing individual addresses in the range, or handling traffic for all the addresses in the range.   * Access the IP Addresses Assign ([POST /networking/ips/assign](/docs/api/networking/#ip-addresses-assign)) endpoint to re-assign IPv6 Ranges to your Linodes.  **Note**: The following restrictions apply:   * A Linode can only have one IPv6 range targeting its SLAAC address.   * An account can only have one IPv6 range in each [Region](/docs/api/regions/#regions-list).   * [Open a Support Ticket](/docs/api/support/#support-ticket-open) to request expansion of these restrictions. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    PostIPv6RangeRequest postIPv6RangeRequest = new PostIPv6RangeRequest(); // PostIPv6RangeRequest | Information about the IPv6 range to create. 
    try {
      PostIPv6Range200Response result = apiInstance.postIPv6Range(postIPv6RangeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#postIPv6Range");
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
| **postIPv6RangeRequest** | [**PostIPv6RangeRequest**](PostIPv6RangeRequest.md)| Information about the IPv6 range to create.  | |

### Return type

[**PostIPv6Range200Response**](PostIPv6Range200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | IPv6 range created successfully. |  -  |
| **0** | Error |  -  |

<a id="shareIPs"></a>
# **shareIPs**
> Object shareIPs(ipAddressesShareRequest)

IP Addresses Share

Configure shared IPs.  IP sharing allows IP address reassignment (also referred to as IP failover) from one Linode to another if the primary Linode becomes unresponsive. This means that requests to the primary Linode&#39;s IP address can be automatically rerouted to secondary Linodes at the configured shared IP addresses.  IP failover requires configuration of a failover service (such as [Keepalived](/docs/guides/ip-failover-keepalived)) within the internal system of the primary Linode. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    IPAddressesShareRequest ipAddressesShareRequest = new IPAddressesShareRequest(); // IPAddressesShareRequest | Information about what IPs to share with which Linode.
    try {
      Object result = apiInstance.shareIPs(ipAddressesShareRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#shareIPs");
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
| **ipAddressesShareRequest** | [**IPAddressesShareRequest**](IPAddressesShareRequest.md)| Information about what IPs to share with which Linode. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | IP Address sharing successful. |  -  |
| **0** | Error |  -  |

<a id="shareIPv4s"></a>
# **shareIPv4s**
> Object shareIPv4s(ipAddressesShareRequest)

IPv4 Sharing Configure

This command is equivalent to **IP Addresses Share** ([POST /networking/ips/share](#ip-addresses-share)).  Configure shared IPs.  IP sharing allows IP address reassignment (also referred to as IP failover) from one Linode to another if the primary Linode becomes unresponsive. This means that requests to the primary Linode&#39;s IP address can be automatically rerouted to secondary Linodes at the configured shared IP addresses.  IP failover requires configuration of a failover service (such as [Keepalived](/docs/guides/ip-failover-keepalived)) within the internal system of the primary Linode. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    IPAddressesShareRequest ipAddressesShareRequest = new IPAddressesShareRequest(); // IPAddressesShareRequest | Information about what IPs to share with which Linode.
    try {
      Object result = apiInstance.shareIPv4s(ipAddressesShareRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#shareIPv4s");
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
| **ipAddressesShareRequest** | [**IPAddressesShareRequest**](IPAddressesShareRequest.md)| Information about what IPs to share with which Linode. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Sharing configured successfully. |  -  |
| **0** | Error |  -  |

<a id="updateFirewall"></a>
# **updateFirewall**
> Firewall updateFirewall(firewallId, updateFirewallRequest)

Firewall Update

Updates information for a Firewall. Some parts of a Firewall&#39;s configuration cannot be manipulated by this endpoint:  - A Firewall&#39;s Devices cannot be set with this endpoint. Instead, use the [Create Firewall Device](/docs/api/networking/#firewall-device-create) and [Delete Firewall Device](/docs/api/networking/#firewall-device-delete) endpoints to assign and remove this Firewall from Linode services.  - A Firewall&#39;s Rules cannot be changed with this endpoint. Instead, use the [Update Firewall Rules](/docs/api/networking/#firewall-rules-update) endpoint to update your Rules.  - A Firewall&#39;s status can be set to &#x60;enabled&#x60; or &#x60;disabled&#x60; by this endpoint, but it cannot be set to &#x60;deleted&#x60;. Instead, use the [Delete Firewall](/docs/api/networking/#firewall-delete) endpoint to delete a Firewall.  If a Firewall&#39;s status is changed with this endpoint, a corresponding &#x60;firewall_enable&#x60; or &#x60;firewall_disable&#x60; Event will be generated. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    Integer firewallId = 56; // Integer | ID of the Firewall to access. 
    UpdateFirewallRequest updateFirewallRequest = new UpdateFirewallRequest(); // UpdateFirewallRequest | The Firewall information to update.
    try {
      Firewall result = apiInstance.updateFirewall(firewallId, updateFirewallRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#updateFirewall");
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
| **firewallId** | **Integer**| ID of the Firewall to access.  | |
| **updateFirewallRequest** | [**UpdateFirewallRequest**](UpdateFirewallRequest.md)| The Firewall information to update. | [optional] |

### Return type

[**Firewall**](Firewall.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Firewall updated successfully. |  -  |
| **0** | Error |  -  |

<a id="updateFirewallRules"></a>
# **updateFirewallRules**
> FirewallRules updateFirewallRules(firewallId, updateFirewallRulesRequest)

Firewall Rules Update

Updates the inbound and outbound Rules for a Firewall.  **Note:** This command replaces all of a Firewall&#39;s &#x60;inbound&#x60; and/or &#x60;outbound&#x60; rulesets with the values specified in your request. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    Integer firewallId = 56; // Integer | ID of the Firewall to access. 
    UpdateFirewallRulesRequest updateFirewallRulesRequest = new UpdateFirewallRulesRequest(); // UpdateFirewallRulesRequest | The Firewall Rules information to update.
    try {
      FirewallRules result = apiInstance.updateFirewallRules(firewallId, updateFirewallRulesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#updateFirewallRules");
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
| **firewallId** | **Integer**| ID of the Firewall to access.  | |
| **updateFirewallRulesRequest** | [**UpdateFirewallRulesRequest**](UpdateFirewallRulesRequest.md)| The Firewall Rules information to update. | [optional] |

### Return type

[**FirewallRules**](FirewallRules.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Firewall Rules updated successfully. |  -  |
| **0** | Error |  -  |

<a id="updateIP"></a>
# **updateIP**
> IPAddress updateIP(address, updateIPRequest)

IP Address RDNS Update

Sets RDNS on an IP Address. Forward DNS must already be set up for reverse DNS to be applied. If you set the RDNS to &#x60;null&#x60; for public IPv4 addresses, it will be reset to the default _ip.linodeusercontent.com_ RDNS value. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    NetworkingApi apiInstance = new NetworkingApi(defaultClient);
    String address = "address_example"; // String | The address to operate on.
    UpdateIPRequest updateIPRequest = new UpdateIPRequest(); // UpdateIPRequest | The information to update.
    try {
      IPAddress result = apiInstance.updateIP(address, updateIPRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkingApi#updateIP");
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
| **address** | **String**| The address to operate on. | |
| **updateIPRequest** | [**UpdateIPRequest**](UpdateIPRequest.md)| The information to update. | |

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | RDNS set successfully |  -  |
| **0** | Error |  -  |

