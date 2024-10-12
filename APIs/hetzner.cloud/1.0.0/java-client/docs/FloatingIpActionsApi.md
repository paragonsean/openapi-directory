# FloatingIpActionsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**floatingIpsIdActionsActionIdGet**](FloatingIpActionsApi.md#floatingIpsIdActionsActionIdGet) | **GET** /floating_ips/{id}/actions/{action_id} | Get an Action for a Floating IP |
| [**floatingIpsIdActionsAssignPost**](FloatingIpActionsApi.md#floatingIpsIdActionsAssignPost) | **POST** /floating_ips/{id}/actions/assign | Assign a Floating IP to a Server |
| [**floatingIpsIdActionsChangeDnsPtrPost**](FloatingIpActionsApi.md#floatingIpsIdActionsChangeDnsPtrPost) | **POST** /floating_ips/{id}/actions/change_dns_ptr | Change reverse DNS entry for a Floating IP |
| [**floatingIpsIdActionsChangeProtectionPost**](FloatingIpActionsApi.md#floatingIpsIdActionsChangeProtectionPost) | **POST** /floating_ips/{id}/actions/change_protection | Change Floating IP Protection |
| [**floatingIpsIdActionsGet**](FloatingIpActionsApi.md#floatingIpsIdActionsGet) | **GET** /floating_ips/{id}/actions | Get all Actions for a Floating IP |
| [**floatingIpsIdActionsUnassignPost**](FloatingIpActionsApi.md#floatingIpsIdActionsUnassignPost) | **POST** /floating_ips/{id}/actions/unassign | Unassign a Floating IP |


<a id="floatingIpsIdActionsActionIdGet"></a>
# **floatingIpsIdActionsActionIdGet**
> ActionResponse floatingIpsIdActionsActionIdGet(id, actionId)

Get an Action for a Floating IP

Returns a specific Action object for a Floating IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FloatingIpActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FloatingIpActionsApi apiInstance = new FloatingIpActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Floating IP
    Integer actionId = 56; // Integer | ID of the Action
    try {
      ActionResponse result = apiInstance.floatingIpsIdActionsActionIdGet(id, actionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FloatingIpActionsApi#floatingIpsIdActionsActionIdGet");
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
| **id** | **Integer**| ID of the Floating IP | |
| **actionId** | **Integer**| ID of the Action | |

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
| **200** | The &#x60;action&#x60; key in the reply has this structure |  -  |

<a id="floatingIpsIdActionsAssignPost"></a>
# **floatingIpsIdActionsAssignPost**
> ActionResponse floatingIpsIdActionsAssignPost(id, assignFloatingIPRequest)

Assign a Floating IP to a Server

Assigns a Floating IP to a Server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FloatingIpActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FloatingIpActionsApi apiInstance = new FloatingIpActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Floating IP
    AssignFloatingIPRequest assignFloatingIPRequest = new AssignFloatingIPRequest(); // AssignFloatingIPRequest | 
    try {
      ActionResponse result = apiInstance.floatingIpsIdActionsAssignPost(id, assignFloatingIPRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FloatingIpActionsApi#floatingIpsIdActionsAssignPost");
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
| **id** | **Integer**| ID of the Floating IP | |
| **assignFloatingIPRequest** | [**AssignFloatingIPRequest**](AssignFloatingIPRequest.md)|  | [optional] |

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
| **201** | The &#x60;action&#x60; key contains the &#x60;assign&#x60; Action |  -  |

<a id="floatingIpsIdActionsChangeDnsPtrPost"></a>
# **floatingIpsIdActionsChangeDnsPtrPost**
> ActionResponse floatingIpsIdActionsChangeDnsPtrPost(id, changeDNSPTRRequest)

Change reverse DNS entry for a Floating IP

Changes the hostname that will appear when getting the hostname belonging to this Floating IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FloatingIpActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FloatingIpActionsApi apiInstance = new FloatingIpActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Floating IP
    ChangeDNSPTRRequest changeDNSPTRRequest = new ChangeDNSPTRRequest(); // ChangeDNSPTRRequest | Select the IP address for which to change the DNS entry by passing `ip`. For a Floating IP of type `ipv4` this must exactly match the IP address of the Floating IP. For a Floating IP of type `ipv6` this must be a single IP within the IPv6 /64 range that belongs to this Floating IP. You can add up to 100 IPv6 reverse DNS entries.  The target hostname is set by passing `dns_ptr`. 
    try {
      ActionResponse result = apiInstance.floatingIpsIdActionsChangeDnsPtrPost(id, changeDNSPTRRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FloatingIpActionsApi#floatingIpsIdActionsChangeDnsPtrPost");
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
| **id** | **Integer**| ID of the Floating IP | |
| **changeDNSPTRRequest** | [**ChangeDNSPTRRequest**](ChangeDNSPTRRequest.md)| Select the IP address for which to change the DNS entry by passing &#x60;ip&#x60;. For a Floating IP of type &#x60;ipv4&#x60; this must exactly match the IP address of the Floating IP. For a Floating IP of type &#x60;ipv6&#x60; this must be a single IP within the IPv6 /64 range that belongs to this Floating IP. You can add up to 100 IPv6 reverse DNS entries.  The target hostname is set by passing &#x60;dns_ptr&#x60;.  | [optional] |

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

<a id="floatingIpsIdActionsChangeProtectionPost"></a>
# **floatingIpsIdActionsChangeProtectionPost**
> ActionResponse floatingIpsIdActionsChangeProtectionPost(id, changeProtectionRequest)

Change Floating IP Protection

Changes the protection configuration of the Floating IP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FloatingIpActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FloatingIpActionsApi apiInstance = new FloatingIpActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Floating IP
    ChangeProtectionRequest changeProtectionRequest = new ChangeProtectionRequest(); // ChangeProtectionRequest | 
    try {
      ActionResponse result = apiInstance.floatingIpsIdActionsChangeProtectionPost(id, changeProtectionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FloatingIpActionsApi#floatingIpsIdActionsChangeProtectionPost");
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
| **id** | **Integer**| ID of the Floating IP | |
| **changeProtectionRequest** | [**ChangeProtectionRequest**](ChangeProtectionRequest.md)|  | [optional] |

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

<a id="floatingIpsIdActionsGet"></a>
# **floatingIpsIdActionsGet**
> FloatingIpsIdActionsGet200Response floatingIpsIdActionsGet(id, sort, status)

Get all Actions for a Floating IP

Returns all Action objects for a Floating IP. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FloatingIpActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FloatingIpActionsApi apiInstance = new FloatingIpActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Floating IP
    String sort = "id"; // String | Can be used multiple times.
    String status = "running"; // String | Can be used multiple times, the response will contain only Actions with specified statuses
    try {
      FloatingIpsIdActionsGet200Response result = apiInstance.floatingIpsIdActionsGet(id, sort, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FloatingIpActionsApi#floatingIpsIdActionsGet");
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
| **id** | **Integer**| ID of the Floating IP | |
| **sort** | **String**| Can be used multiple times. | [optional] [enum: id, id:asc, id:desc, command, command:asc, command:desc, status, status:asc, status:desc, progress, progress:asc, progress:desc, started, started:asc, started:desc, finished, finished:asc, finished:desc] |
| **status** | **String**| Can be used multiple times, the response will contain only Actions with specified statuses | [optional] [enum: running, success, error] |

### Return type

[**FloatingIpsIdActionsGet200Response**](FloatingIpsIdActionsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;actions&#x60; key contains a list of Actions |  -  |

<a id="floatingIpsIdActionsUnassignPost"></a>
# **floatingIpsIdActionsUnassignPost**
> ActionResponse floatingIpsIdActionsUnassignPost(id)

Unassign a Floating IP

Unassigns a Floating IP, resulting in it being unreachable. You may assign it to a Server again at a later time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FloatingIpActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    FloatingIpActionsApi apiInstance = new FloatingIpActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Floating IP
    try {
      ActionResponse result = apiInstance.floatingIpsIdActionsUnassignPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FloatingIpActionsApi#floatingIpsIdActionsUnassignPost");
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
| **id** | **Integer**| ID of the Floating IP | |

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
| **201** | The &#x60;action&#x60; key contains the &#x60;unassign&#x60; Action |  -  |

