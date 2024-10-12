# NetworkActionsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**networksIdActionsActionIdGet**](NetworkActionsApi.md#networksIdActionsActionIdGet) | **GET** /networks/{id}/actions/{action_id} | Get an Action for a Network |
| [**networksIdActionsAddRoutePost**](NetworkActionsApi.md#networksIdActionsAddRoutePost) | **POST** /networks/{id}/actions/add_route | Add a route to a Network |
| [**networksIdActionsAddSubnetPost**](NetworkActionsApi.md#networksIdActionsAddSubnetPost) | **POST** /networks/{id}/actions/add_subnet | Add a subnet to a Network |
| [**networksIdActionsChangeIpRangePost**](NetworkActionsApi.md#networksIdActionsChangeIpRangePost) | **POST** /networks/{id}/actions/change_ip_range | Change IP range of a Network |
| [**networksIdActionsChangeProtectionPost**](NetworkActionsApi.md#networksIdActionsChangeProtectionPost) | **POST** /networks/{id}/actions/change_protection | Change Network Protection |
| [**networksIdActionsDeleteRoutePost**](NetworkActionsApi.md#networksIdActionsDeleteRoutePost) | **POST** /networks/{id}/actions/delete_route | Delete a route from a Network |
| [**networksIdActionsDeleteSubnetPost**](NetworkActionsApi.md#networksIdActionsDeleteSubnetPost) | **POST** /networks/{id}/actions/delete_subnet | Delete a subnet from a Network |
| [**networksIdActionsGet**](NetworkActionsApi.md#networksIdActionsGet) | **GET** /networks/{id}/actions | Get all Actions for a Network |


<a id="networksIdActionsActionIdGet"></a>
# **networksIdActionsActionIdGet**
> ActionResponse networksIdActionsActionIdGet(id, actionId)

Get an Action for a Network

Returns a specific Action for a Network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    NetworkActionsApi apiInstance = new NetworkActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Network
    Integer actionId = 56; // Integer | ID of the Action
    try {
      ActionResponse result = apiInstance.networksIdActionsActionIdGet(id, actionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkActionsApi#networksIdActionsActionIdGet");
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
| **id** | **Integer**| ID of the Network | |
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
| **200** | The &#x60;action&#x60; key contains the Network Action |  -  |

<a id="networksIdActionsAddRoutePost"></a>
# **networksIdActionsAddRoutePost**
> ActionResponse networksIdActionsAddRoutePost(id, addDeleteRouteRequest)

Add a route to a Network

Adds a route entry to a Network.  Note: if the Network object changes during the request, the response will be a “conflict” error. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    NetworkActionsApi apiInstance = new NetworkActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Network
    AddDeleteRouteRequest addDeleteRouteRequest = new AddDeleteRouteRequest(); // AddDeleteRouteRequest | 
    try {
      ActionResponse result = apiInstance.networksIdActionsAddRoutePost(id, addDeleteRouteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkActionsApi#networksIdActionsAddRoutePost");
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
| **id** | **Integer**| ID of the Network | |
| **addDeleteRouteRequest** | [**AddDeleteRouteRequest**](AddDeleteRouteRequest.md)|  | [optional] |

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
| **201** | The &#x60;action&#x60; key contains the &#x60;add_route&#x60; Action |  -  |

<a id="networksIdActionsAddSubnetPost"></a>
# **networksIdActionsAddSubnetPost**
> ActionResponse networksIdActionsAddSubnetPost(id, addSubnetRequest)

Add a subnet to a Network

Adds a new subnet object to the Network. If you do not specify an &#x60;ip_range&#x60; for the subnet we will automatically pick the first available /24 range for you if possible.  Note: if the parent Network object changes during the request, the response will be a “conflict” error. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    NetworkActionsApi apiInstance = new NetworkActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Network
    AddSubnetRequest addSubnetRequest = new AddSubnetRequest(); // AddSubnetRequest | 
    try {
      ActionResponse result = apiInstance.networksIdActionsAddSubnetPost(id, addSubnetRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkActionsApi#networksIdActionsAddSubnetPost");
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
| **id** | **Integer**| ID of the Network | |
| **addSubnetRequest** | [**AddSubnetRequest**](AddSubnetRequest.md)|  | [optional] |

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
| **201** | The &#x60;action&#x60; key contains the &#x60;add_subnet&#x60; Action |  -  |

<a id="networksIdActionsChangeIpRangePost"></a>
# **networksIdActionsChangeIpRangePost**
> ActionResponse networksIdActionsChangeIpRangePost(id, changeIPRangeRequest)

Change IP range of a Network

Changes the IP range of a Network. IP ranges can only be extended and never shrunk. You can only add IPs at the end of an existing IP range. This means that the IP part of your existing range must stay the same and you can only change its netmask.  For example if you have a range &#x60;10.0.0.0/16&#x60; you want to extend then your new range must also start with the IP &#x60;10.0.0.0&#x60;. Your CIDR netmask &#x60;/16&#x60; may change to a number that is smaller than &#x60;16&#x60; thereby increasing the IP range. So valid entries would be &#x60;10.0.0.0/15&#x60;, &#x60;10.0.0.0/14&#x60;, &#x60;10.0.0.0/13&#x60; and so on.  After changing the IP range you will have to adjust the routes on your connected Servers by either rebooting them or manually changing the routes to your private Network interface.  Note: if the Network object changes during the request, the response will be a “conflict” error. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    NetworkActionsApi apiInstance = new NetworkActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Network
    ChangeIPRangeRequest changeIPRangeRequest = new ChangeIPRangeRequest(); // ChangeIPRangeRequest | 
    try {
      ActionResponse result = apiInstance.networksIdActionsChangeIpRangePost(id, changeIPRangeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkActionsApi#networksIdActionsChangeIpRangePost");
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
| **id** | **Integer**| ID of the Network | |
| **changeIPRangeRequest** | [**ChangeIPRangeRequest**](ChangeIPRangeRequest.md)|  | [optional] |

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
| **201** | The &#x60;action&#x60; key contains the &#x60;change_ip_range&#x60; Action |  -  |

<a id="networksIdActionsChangeProtectionPost"></a>
# **networksIdActionsChangeProtectionPost**
> ActionResponse networksIdActionsChangeProtectionPost(id, changeProtectionRequest1)

Change Network Protection

Changes the protection configuration of a Network.  Note: if the Network object changes during the request, the response will be a “conflict” error. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    NetworkActionsApi apiInstance = new NetworkActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Network
    ChangeProtectionRequest1 changeProtectionRequest1 = new ChangeProtectionRequest1(); // ChangeProtectionRequest1 | 
    try {
      ActionResponse result = apiInstance.networksIdActionsChangeProtectionPost(id, changeProtectionRequest1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkActionsApi#networksIdActionsChangeProtectionPost");
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
| **id** | **Integer**| ID of the Network | |
| **changeProtectionRequest1** | [**ChangeProtectionRequest1**](ChangeProtectionRequest1.md)|  | [optional] |

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

<a id="networksIdActionsDeleteRoutePost"></a>
# **networksIdActionsDeleteRoutePost**
> ActionResponse networksIdActionsDeleteRoutePost(id, addDeleteRouteRequest)

Delete a route from a Network

Delete a route entry from a Network.  Note: if the Network object changes during the request, the response will be a “conflict” error. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    NetworkActionsApi apiInstance = new NetworkActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Network
    AddDeleteRouteRequest addDeleteRouteRequest = new AddDeleteRouteRequest(); // AddDeleteRouteRequest | 
    try {
      ActionResponse result = apiInstance.networksIdActionsDeleteRoutePost(id, addDeleteRouteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkActionsApi#networksIdActionsDeleteRoutePost");
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
| **id** | **Integer**| ID of the Network | |
| **addDeleteRouteRequest** | [**AddDeleteRouteRequest**](AddDeleteRouteRequest.md)|  | [optional] |

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
| **201** | The &#x60;action&#x60; key contains the &#x60;delete_route&#x60; Action |  -  |

<a id="networksIdActionsDeleteSubnetPost"></a>
# **networksIdActionsDeleteSubnetPost**
> ActionResponse networksIdActionsDeleteSubnetPost(id, deleteSubnetRequest)

Delete a subnet from a Network

Deletes a single subnet entry from a Network. You cannot delete subnets which still have Servers attached. If you have Servers attached you first need to detach all Servers that use IPs from this subnet before you can delete the subnet.  Note: if the Network object changes during the request, the response will be a “conflict” error. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    NetworkActionsApi apiInstance = new NetworkActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Network
    DeleteSubnetRequest deleteSubnetRequest = new DeleteSubnetRequest(); // DeleteSubnetRequest | 
    try {
      ActionResponse result = apiInstance.networksIdActionsDeleteSubnetPost(id, deleteSubnetRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkActionsApi#networksIdActionsDeleteSubnetPost");
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
| **id** | **Integer**| ID of the Network | |
| **deleteSubnetRequest** | [**DeleteSubnetRequest**](DeleteSubnetRequest.md)|  | [optional] |

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
| **201** | The &#x60;action&#x60; key contains the &#x60;delete_subnet&#x60; Action |  -  |

<a id="networksIdActionsGet"></a>
# **networksIdActionsGet**
> ActionsResponse networksIdActionsGet(id, sort, status)

Get all Actions for a Network

Returns all Action objects for a Network. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.hetzner.cloud/v1");

    NetworkActionsApi apiInstance = new NetworkActionsApi(defaultClient);
    Integer id = 56; // Integer | ID of the Network
    String sort = "id"; // String | Can be used multiple times.
    String status = "running"; // String | Can be used multiple times, the response will contain only Actions with specified statuses
    try {
      ActionsResponse result = apiInstance.networksIdActionsGet(id, sort, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkActionsApi#networksIdActionsGet");
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
| **id** | **Integer**| ID of the Network | |
| **sort** | **String**| Can be used multiple times. | [optional] [enum: id, id:asc, id:desc, command, command:asc, command:desc, status, status:asc, status:desc, progress, progress:asc, progress:desc, started, started:asc, started:desc, finished, finished:asc, finished:desc] |
| **status** | **String**| Can be used multiple times, the response will contain only Actions with specified statuses | [optional] [enum: running, success, error] |

### Return type

[**ActionsResponse**](ActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The &#x60;actions&#x60; key contains a list of Actions |  -  |

