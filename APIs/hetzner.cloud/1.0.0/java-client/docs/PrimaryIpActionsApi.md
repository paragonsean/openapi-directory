# PrimaryIpActionsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**primaryIpsIdActionsAssignPost**](PrimaryIpActionsApi.md#primaryIpsIdActionsAssignPost) | **POST** /primary_ips/{id}/actions/assign | Assign a Primary IP to a resource |
| [**primaryIpsIdActionsChangeDnsPtrPost**](PrimaryIpActionsApi.md#primaryIpsIdActionsChangeDnsPtrPost) | **POST** /primary_ips/{id}/actions/change_dns_ptr | Change reverse DNS entry for a Primary IP |
| [**primaryIpsIdActionsChangeProtectionPost**](PrimaryIpActionsApi.md#primaryIpsIdActionsChangeProtectionPost) | **POST** /primary_ips/{id}/actions/change_protection | Change Primary IP Protection |
| [**primaryIpsIdActionsUnassignPost**](PrimaryIpActionsApi.md#primaryIpsIdActionsUnassignPost) | **POST** /primary_ips/{id}/actions/unassign | Unassign a Primary IP from a resource |


<a id="primaryIpsIdActionsAssignPost"></a>
# **primaryIpsIdActionsAssignPost**
> ActionResponse primaryIpsIdActionsAssignPost(id, assignPrimaryIPRequest)

Assign a Primary IP to a resource

Assigns a Primary IP to a Server.  A Server can only have one Primary IP of type &#x60;ipv4&#x60; and one of type &#x60;ipv6&#x60; assigned. If you need more IPs use Floating IPs.  The Server must be powered off (status &#x60;off&#x60;) in order for this operation to succeed.  #### Call specific error codes  | Code                          | Description                                                   | |------------------------------ |-------------------------------------------------------------- | | &#x60;server_not_stopped&#x60;          | The server is running, but needs to be powered off            | | &#x60;primary_ip_already_assigned&#x60; | Primary ip is already assigned to a different server          | | &#x60;server_has_ipv4&#x60;             | The server already has an ipv4 address                        | | &#x60;server_has_ipv6&#x60;             | The server already has an ipv6 address                        | 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrimaryIpActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    PrimaryIpActionsApi apiInstance = new PrimaryIpActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Primary IP
    AssignPrimaryIPRequest assignPrimaryIPRequest = new AssignPrimaryIPRequest(); // AssignPrimaryIPRequest | 
    try {
      ActionResponse result = apiInstance.primaryIpsIdActionsAssignPost(id, assignPrimaryIPRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrimaryIpActionsApi#primaryIpsIdActionsAssignPost");
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
| **id** | **Integer**| ID of the Primary IP | |
| **assignPrimaryIPRequest** | [**AssignPrimaryIPRequest**](AssignPrimaryIPRequest.md)|  | [optional] |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key in the reply contains an Action object with this structure |  -  |

<a id="primaryIpsIdActionsChangeDnsPtrPost"></a>
# **primaryIpsIdActionsChangeDnsPtrPost**
> ActionResponse primaryIpsIdActionsChangeDnsPtrPost(id, changeDNSPTRRequest)

Change reverse DNS entry for a Primary IP

Changes the hostname that will appear when getting the hostname belonging to this Primary IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrimaryIpActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    PrimaryIpActionsApi apiInstance = new PrimaryIpActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Primary IP
    ChangeDNSPTRRequest changeDNSPTRRequest = new ChangeDNSPTRRequest(); // ChangeDNSPTRRequest | Select the IP address for which to change the DNS entry by passing `ip`. For a Primary IP of type `ipv4` this must exactly match the IP address of the Primary IP. For a Primary IP of type `ipv6` this must be a single IP within the IPv6 /64 range that belongs to this Primary IP. You can add up to 100 IPv6 reverse DNS entries.  The target hostname is set by passing `dns_ptr`. 
    try {
      ActionResponse result = apiInstance.primaryIpsIdActionsChangeDnsPtrPost(id, changeDNSPTRRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrimaryIpActionsApi#primaryIpsIdActionsChangeDnsPtrPost");
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
| **id** | **Integer**| ID of the Primary IP | |
| **changeDNSPTRRequest** | [**ChangeDNSPTRRequest**](ChangeDNSPTRRequest.md)| Select the IP address for which to change the DNS entry by passing &#x60;ip&#x60;. For a Primary IP of type &#x60;ipv4&#x60; this must exactly match the IP address of the Primary IP. For a Primary IP of type &#x60;ipv6&#x60; this must be a single IP within the IPv6 /64 range that belongs to this Primary IP. You can add up to 100 IPv6 reverse DNS entries.  The target hostname is set by passing &#x60;dns_ptr&#x60;.  | [optional] |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the &#x60;change_dns_ptr&#x60; Action |  -  |

<a id="primaryIpsIdActionsChangeProtectionPost"></a>
# **primaryIpsIdActionsChangeProtectionPost**
> ActionResponse primaryIpsIdActionsChangeProtectionPost(id, changeProtectionRequest2)

Change Primary IP Protection

Changes the protection configuration of a Primary IP.  A Primary IP can only be delete protected if its &#x60;auto_delete&#x60; property is set to &#x60;false&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrimaryIpActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    PrimaryIpActionsApi apiInstance = new PrimaryIpActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Primary IP
    ChangeProtectionRequest2 changeProtectionRequest2 = new ChangeProtectionRequest2(); // ChangeProtectionRequest2 | 
    try {
      ActionResponse result = apiInstance.primaryIpsIdActionsChangeProtectionPost(id, changeProtectionRequest2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrimaryIpActionsApi#primaryIpsIdActionsChangeProtectionPost");
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
| **id** | **Integer**| ID of the Primary IP | |
| **changeProtectionRequest2** | [**ChangeProtectionRequest2**](ChangeProtectionRequest2.md)|  | [optional] |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key contains the &#x60;change_protection&#x60; Action |  -  |

<a id="primaryIpsIdActionsUnassignPost"></a>
# **primaryIpsIdActionsUnassignPost**
> ActionResponse primaryIpsIdActionsUnassignPost(id)

Unassign a Primary IP from a resource

Unassigns a Primary IP from a Server.  The Server must be powered off (status &#x60;off&#x60;) in order for this operation to succeed.  Note that only Servers that have at least one network interface (public or private) attached can be powered on.  #### Call specific error codes  | Code                              | Description                                                   | |---------------------------------- |-------------------------------------------------------------- | | &#x60;server_not_stopped&#x60;              | The server is running, but needs to be powered off            | | &#x60;server_is_load_balancer_target&#x60;  | The server ipv4 address is a loadbalancer target              | 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrimaryIpActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    PrimaryIpActionsApi apiInstance = new PrimaryIpActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Primary IP
    try {
      ActionResponse result = apiInstance.primaryIpsIdActionsUnassignPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrimaryIpActionsApi#primaryIpsIdActionsUnassignPost");
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
| **id** | **Integer**| ID of the Primary IP | |

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The &#x60;action&#x60; key in the reply contains an Action object with this structure |  -  |

