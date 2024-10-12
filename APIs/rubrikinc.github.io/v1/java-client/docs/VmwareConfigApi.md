# VmwareConfigApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPreferredCdpNetworkProtocol**](VmwareConfigApi.md#getPreferredCdpNetworkProtocol) | **GET** /vmware/config/cdp/get_preferred_cdp_network_protocol | Returns the current preference of CDM between IPv4 and IPv6 for CDP data transfer |
| [**getVmwareRecoveryNetworks**](VmwareConfigApi.md#getVmwareRecoveryNetworks) | **GET** /vmware/config/recovery/networks | Get all the VMware recovery networks for a compute resource ID |
| [**setPreferredCdpNetworkProtocol**](VmwareConfigApi.md#setPreferredCdpNetworkProtocol) | **PATCH** /vmware/config/cdp/set_preferred_cdp_network_protocol | Set the current preference of CDM between IPv4 and IPv6 for CDP data transfer |


<a id="getPreferredCdpNetworkProtocol"></a>
# **getPreferredCdpNetworkProtocol**
> PreferredCdpNetworkProtocolObject getPreferredCdpNetworkProtocol()

Returns the current preference of CDM between IPv4 and IPv6 for CDP data transfer

Returns the current preference of CDM between IPv4 and IPv6 for CDP data transfer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VmwareConfigApi apiInstance = new VmwareConfigApi(defaultClient);
    try {
      PreferredCdpNetworkProtocolObject result = apiInstance.getPreferredCdpNetworkProtocol();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareConfigApi#getPreferredCdpNetworkProtocol");
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

[**PreferredCdpNetworkProtocolObject**](PreferredCdpNetworkProtocolObject.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The preferred network protocol to use for transferring CDP data. |  -  |

<a id="getVmwareRecoveryNetworks"></a>
# **getVmwareRecoveryNetworks**
> VmwareNetworkCollection getVmwareRecoveryNetworks(computeResourceId, computeResourceType)

Get all the VMware recovery networks for a compute resource ID

Get all the networks for snapshot recovery for the specified compute resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VmwareConfigApi apiInstance = new VmwareConfigApi(defaultClient);
    String computeResourceId = "computeResourceId_example"; // String | Get VMware recovery networks for the compute resource ID.
    String computeResourceType = "ComputeCluster"; // String | The type of the compute resource.
    try {
      VmwareNetworkCollection result = apiInstance.getVmwareRecoveryNetworks(computeResourceId, computeResourceType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareConfigApi#getVmwareRecoveryNetworks");
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
| **computeResourceId** | **String**| Get VMware recovery networks for the compute resource ID. | |
| **computeResourceType** | **String**| The type of the compute resource. | [enum: ComputeCluster, Host, ResourcePool] |

### Return type

[**VmwareNetworkCollection**](VmwareNetworkCollection.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All the VMware networks for the compute resource. |  -  |

<a id="setPreferredCdpNetworkProtocol"></a>
# **setPreferredCdpNetworkProtocol**
> PreferredCdpNetworkProtocolObject setPreferredCdpNetworkProtocol(body)

Set the current preference of CDM between IPv4 and IPv6 for CDP data transfer

Set the current preference of CDM between IPv4 and IPv6 for CDP data transfer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VmwareConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    VmwareConfigApi apiInstance = new VmwareConfigApi(defaultClient);
    String body = "body_example"; // String | The preferred network protocol to use for transferring CDP data.
    try {
      PreferredCdpNetworkProtocolObject result = apiInstance.setPreferredCdpNetworkProtocol(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VmwareConfigApi#setPreferredCdpNetworkProtocol");
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
| **body** | **String**| The preferred network protocol to use for transferring CDP data. | |

### Return type

[**PreferredCdpNetworkProtocolObject**](PreferredCdpNetworkProtocolObject.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated preferred network protocol to transfer CDP data over. |  -  |

