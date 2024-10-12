# NetworkgroupsApi

All URIs are relative to *https://api.clever-cloud.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkGroupExternalPeer_1**](NetworkgroupsApi.md#createNetworkGroupExternalPeer_1) | **POST** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/external-peers | Add external peer |
| [**createNetworkGroupMember_1**](NetworkgroupsApi.md#createNetworkGroupMember_1) | **POST** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members | Add member |
| [**createNetworkGroup_1**](NetworkgroupsApi.md#createNetworkGroup_1) | **POST** /v4/networkgroups/organisations/{ownerId}/networkgroups | Create Network Group |
| [**deleteNetworkGroupExternalPeer_1**](NetworkgroupsApi.md#deleteNetworkGroupExternalPeer_1) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/external-peers/{peerId} | Remove external peer |
| [**deleteNetworkGroupMember_1**](NetworkgroupsApi.md#deleteNetworkGroupMember_1) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members/{memberId} | Remove member |
| [**deleteNetworkGroupPeer_1**](NetworkgroupsApi.md#deleteNetworkGroupPeer_1) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId} | Remove peer |
| [**deleteNetworkGroup_1**](NetworkgroupsApi.md#deleteNetworkGroup_1) | **DELETE** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId} | Delete Network Group |
| [**getNetworkGroupMember_1**](NetworkgroupsApi.md#getNetworkGroupMember_1) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members/{memberId} | Get member |
| [**getNetworkGroupPeer_1**](NetworkgroupsApi.md#getNetworkGroupPeer_1) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId} | Get peer |
| [**getNetworkGroupStream_1**](NetworkgroupsApi.md#getNetworkGroupStream_1) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/stream | Network Group SSE |
| [**getNetworkGroupWireGuardConfigurationStream_1**](NetworkgroupsApi.md#getNetworkGroupWireGuardConfigurationStream_1) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId}/wireguard/configuration/stream | Get WireGuard® configuration |
| [**getNetworkGroupWireGuardConfiguration_1**](NetworkgroupsApi.md#getNetworkGroupWireGuardConfiguration_1) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers/{peerId}/wireguard/configuration | Get WireGuard® configuration |
| [**getNetworkGroup_1**](NetworkgroupsApi.md#getNetworkGroup_1) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId} | Get Network Group |
| [**listNetworkGroupMembers_1**](NetworkgroupsApi.md#listNetworkGroupMembers_1) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/members | List members |
| [**listNetworkGroupPeers_1**](NetworkgroupsApi.md#listNetworkGroupPeers_1) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups/{networkGroupId}/peers | List peers |
| [**listNetworkGroups_1**](NetworkgroupsApi.md#listNetworkGroups_1) | **GET** /v4/networkgroups/organisations/{ownerId}/networkgroups | List Network Groups |


<a id="createNetworkGroupExternalPeer_1"></a>
# **createNetworkGroupExternalPeer_1**
> Object createNetworkGroupExternalPeer_1(ownerId, networkGroupId, body)

Add external peer

Adds an external peer to a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkgroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    NetworkgroupsApi apiInstance = new NetworkgroupsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.createNetworkGroupExternalPeer_1(ownerId, networkGroupId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkgroupsApi#createNetworkGroupExternalPeer_1");
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
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain; charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="createNetworkGroupMember_1"></a>
# **createNetworkGroupMember_1**
> createNetworkGroupMember_1(ownerId, networkGroupId, schema2)

Add member

Adds a member to a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkgroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    NetworkgroupsApi apiInstance = new NetworkgroupsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Schema2 schema2 = new Schema2(); // Schema2 | 
    try {
      apiInstance.createNetworkGroupMember_1(ownerId, networkGroupId, schema2);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkgroupsApi#createNetworkGroupMember_1");
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
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **schema2** | [**Schema2**](Schema2.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** |  |  -  |
| **400** |  |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="createNetworkGroup_1"></a>
# **createNetworkGroup_1**
> Object createNetworkGroup_1(ownerId, body)

Create Network Group

Creates a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkgroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    NetworkgroupsApi apiInstance = new NetworkgroupsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.createNetworkGroup_1(ownerId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkgroupsApi#createNetworkGroup_1");
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
| **ownerId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain; charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **400** |  |  -  |
| **401** |  |  -  |
| **409** | Conflict |  -  |

<a id="deleteNetworkGroupExternalPeer_1"></a>
# **deleteNetworkGroupExternalPeer_1**
> deleteNetworkGroupExternalPeer_1(ownerId, networkGroupId, peerId, body)

Remove external peer

Removes an external peer from a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkgroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    NetworkgroupsApi apiInstance = new NetworkgroupsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String peerId = "peerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      apiInstance.deleteNetworkGroupExternalPeer_1(ownerId, networkGroupId, peerId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkgroupsApi#deleteNetworkGroupExternalPeer_1");
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
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **peerId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **401** |  |  -  |

<a id="deleteNetworkGroupMember_1"></a>
# **deleteNetworkGroupMember_1**
> deleteNetworkGroupMember_1(ownerId, networkGroupId, memberId, body)

Remove member

Removes a member from a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkgroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    NetworkgroupsApi apiInstance = new NetworkgroupsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String memberId = "memberId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      apiInstance.deleteNetworkGroupMember_1(ownerId, networkGroupId, memberId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkgroupsApi#deleteNetworkGroupMember_1");
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
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **memberId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **401** |  |  -  |

<a id="deleteNetworkGroupPeer_1"></a>
# **deleteNetworkGroupPeer_1**
> deleteNetworkGroupPeer_1(ownerId, networkGroupId, peerId, body)

Remove peer

Removes a peer from a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkgroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    NetworkgroupsApi apiInstance = new NetworkgroupsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String peerId = "peerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      apiInstance.deleteNetworkGroupPeer_1(ownerId, networkGroupId, peerId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkgroupsApi#deleteNetworkGroupPeer_1");
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
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **peerId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **401** |  |  -  |

<a id="deleteNetworkGroup_1"></a>
# **deleteNetworkGroup_1**
> deleteNetworkGroup_1(ownerId, networkGroupId, body)

Delete Network Group

Deletes a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkgroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    NetworkgroupsApi apiInstance = new NetworkgroupsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      apiInstance.deleteNetworkGroup_1(ownerId, networkGroupId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkgroupsApi#deleteNetworkGroup_1");
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
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="getNetworkGroupMember_1"></a>
# **getNetworkGroupMember_1**
> Schema1 getNetworkGroupMember_1(ownerId, networkGroupId, memberId, body)

Get member

Gets details of a Network Group member.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkgroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    NetworkgroupsApi apiInstance = new NetworkgroupsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String memberId = "memberId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Schema1 result = apiInstance.getNetworkGroupMember_1(ownerId, networkGroupId, memberId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkgroupsApi#getNetworkGroupMember_1");
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
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **memberId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

[**Schema1**](Schema1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="getNetworkGroupPeer_1"></a>
# **getNetworkGroupPeer_1**
> Object getNetworkGroupPeer_1(ownerId, networkGroupId, peerId, body)

Get peer

Gets details of a Network Group peer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkgroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    NetworkgroupsApi apiInstance = new NetworkgroupsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String peerId = "peerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.getNetworkGroupPeer_1(ownerId, networkGroupId, peerId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkgroupsApi#getNetworkGroupPeer_1");
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
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **peerId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="getNetworkGroupStream_1"></a>
# **getNetworkGroupStream_1**
> Object getNetworkGroupStream_1(ownerId, networkGroupId, body)

Network Group SSE

Retrieves the current Network Group details as a Server Sent Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkgroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    NetworkgroupsApi apiInstance = new NetworkgroupsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.getNetworkGroupStream_1(ownerId, networkGroupId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkgroupsApi#getNetworkGroupStream_1");
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
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="getNetworkGroupWireGuardConfigurationStream_1"></a>
# **getNetworkGroupWireGuardConfigurationStream_1**
> Object getNetworkGroupWireGuardConfigurationStream_1(ownerId, networkGroupId, peerId, body)

Get WireGuard® configuration

Gets the current WireGuard® tunnel configuration file for a Network Group peer as a Server Sent Event.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkgroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    NetworkgroupsApi apiInstance = new NetworkgroupsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String peerId = "peerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.getNetworkGroupWireGuardConfigurationStream_1(ownerId, networkGroupId, peerId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkgroupsApi#getNetworkGroupWireGuardConfigurationStream_1");
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
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **peerId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="getNetworkGroupWireGuardConfiguration_1"></a>
# **getNetworkGroupWireGuardConfiguration_1**
> Object getNetworkGroupWireGuardConfiguration_1(ownerId, networkGroupId, peerId, body)

Get WireGuard® configuration

Gets the current WireGuard® tunnel configuration file for a Network Group peer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkgroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    NetworkgroupsApi apiInstance = new NetworkgroupsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    String peerId = "peerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.getNetworkGroupWireGuardConfiguration_1(ownerId, networkGroupId, peerId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkgroupsApi#getNetworkGroupWireGuardConfiguration_1");
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
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **peerId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="getNetworkGroup_1"></a>
# **getNetworkGroup_1**
> Object getNetworkGroup_1(ownerId, networkGroupId, body)

Get Network Group

Gets details of a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkgroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    NetworkgroupsApi apiInstance = new NetworkgroupsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      Object result = apiInstance.getNetworkGroup_1(ownerId, networkGroupId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkgroupsApi#getNetworkGroup_1");
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
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="listNetworkGroupMembers_1"></a>
# **listNetworkGroupMembers_1**
> List&lt;Schema1&gt; listNetworkGroupMembers_1(ownerId, networkGroupId, body)

List members

Lists members in a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkgroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    NetworkgroupsApi apiInstance = new NetworkgroupsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      List<Schema1> result = apiInstance.listNetworkGroupMembers_1(ownerId, networkGroupId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkgroupsApi#listNetworkGroupMembers_1");
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
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

[**List&lt;Schema1&gt;**](Schema1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="listNetworkGroupPeers_1"></a>
# **listNetworkGroupPeers_1**
> List&lt;Object&gt; listNetworkGroupPeers_1(ownerId, networkGroupId, body)

List peers

Lists peers in a Network Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkgroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    NetworkgroupsApi apiInstance = new NetworkgroupsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    String networkGroupId = "networkGroupId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      List<Object> result = apiInstance.listNetworkGroupPeers_1(ownerId, networkGroupId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkgroupsApi#listNetworkGroupPeers_1");
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
| **ownerId** | **String**| Automatically added | |
| **networkGroupId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** |  |  -  |
| **404** |  |  -  |

<a id="listNetworkGroups_1"></a>
# **listNetworkGroups_1**
> List&lt;Object&gt; listNetworkGroups_1(ownerId, body)

List Network Groups

Lists Network Groups from an owner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworkgroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    NetworkgroupsApi apiInstance = new NetworkgroupsApi(defaultClient);
    String ownerId = "ownerId_example"; // String | Automatically added
    Object body = null; // Object | 
    try {
      List<Object> result = apiInstance.listNetworkGroups_1(ownerId, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworkgroupsApi#listNetworkGroups_1");
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
| **ownerId** | **String**| Automatically added | |
| **body** | **Object**|  | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** |  |  -  |

