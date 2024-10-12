# NetworksApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bindNetwork**](NetworksApi.md#bindNetwork) | **POST** /networks/{networkId}/bind | Bind a network to a template. |
| [**combineOrganizationNetworks**](NetworksApi.md#combineOrganizationNetworks) | **POST** /organizations/{organizationId}/networks/combine | Combine multiple networks into a single network |
| [**createOrganizationNetwork**](NetworksApi.md#createOrganizationNetwork) | **POST** /organizations/{organizationId}/networks | Create a network |
| [**deleteNetwork**](NetworksApi.md#deleteNetwork) | **DELETE** /networks/{networkId} | Delete a network |
| [**getNetwork**](NetworksApi.md#getNetwork) | **GET** /networks/{networkId} | Return a network |
| [**getNetworkAirMarshal**](NetworksApi.md#getNetworkAirMarshal) | **GET** /networks/{networkId}/airMarshal | List Air Marshal scan results from a network |
| [**getNetworkSiteToSiteVpn**](NetworksApi.md#getNetworkSiteToSiteVpn) | **GET** /networks/{networkId}/siteToSiteVpn | Return the site-to-site VPN settings of a network |
| [**getNetworkTraffic**](NetworksApi.md#getNetworkTraffic) | **GET** /networks/{networkId}/traffic | Return the traffic analysis data for this network |
| [**getOrganizationNetworks**](NetworksApi.md#getOrganizationNetworks) | **GET** /organizations/{organizationId}/networks | List the networks in an organization |
| [**splitNetwork**](NetworksApi.md#splitNetwork) | **POST** /networks/{networkId}/split | Split a combined network into individual networks for each type of device |
| [**unbindNetwork**](NetworksApi.md#unbindNetwork) | **POST** /networks/{networkId}/unbind | Unbind a network from a template. |
| [**updateNetwork**](NetworksApi.md#updateNetwork) | **PUT** /networks/{networkId} | Update a network |
| [**updateNetworkSiteToSiteVpn**](NetworksApi.md#updateNetworkSiteToSiteVpn) | **PUT** /networks/{networkId}/siteToSiteVpn | Update the site-to-site VPN settings of a network |


<a id="bindNetwork"></a>
# **bindNetwork**
> bindNetwork(networkId, bindNetworkRequest)

Bind a network to a template.

Bind a network to a template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    BindNetworkRequest bindNetworkRequest = new BindNetworkRequest(); // BindNetworkRequest | 
    try {
      apiInstance.bindNetwork(networkId, bindNetworkRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#bindNetwork");
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
| **bindNetworkRequest** | [**BindNetworkRequest**](BindNetworkRequest.md)|  | |

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

<a id="combineOrganizationNetworks"></a>
# **combineOrganizationNetworks**
> Object combineOrganizationNetworks(organizationId, combineOrganizationNetworksRequest)

Combine multiple networks into a single network

Combine multiple networks into a single network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CombineOrganizationNetworksRequest combineOrganizationNetworksRequest = new CombineOrganizationNetworksRequest(); // CombineOrganizationNetworksRequest | 
    try {
      Object result = apiInstance.combineOrganizationNetworks(organizationId, combineOrganizationNetworksRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#combineOrganizationNetworks");
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
| **combineOrganizationNetworksRequest** | [**CombineOrganizationNetworksRequest**](CombineOrganizationNetworksRequest.md)|  | |

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

<a id="createOrganizationNetwork"></a>
# **createOrganizationNetwork**
> Object createOrganizationNetwork(organizationId, createOrganizationNetworkRequest)

Create a network

Create a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationNetworkRequest createOrganizationNetworkRequest = new CreateOrganizationNetworkRequest(); // CreateOrganizationNetworkRequest | 
    try {
      Object result = apiInstance.createOrganizationNetwork(organizationId, createOrganizationNetworkRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#createOrganizationNetwork");
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
| **createOrganizationNetworkRequest** | [**CreateOrganizationNetworkRequest**](CreateOrganizationNetworkRequest.md)|  | |

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
| **201** | Successful operation |  -  |

<a id="deleteNetwork"></a>
# **deleteNetwork**
> deleteNetwork(networkId)

Delete a network

Delete a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      apiInstance.deleteNetwork(networkId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#deleteNetwork");
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

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="getNetwork"></a>
# **getNetwork**
> Object getNetwork(networkId)

Return a network

Return a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetwork(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetwork");
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

<a id="getNetworkAirMarshal"></a>
# **getNetworkAirMarshal**
> List&lt;Object&gt; getNetworkAirMarshal(networkId, t0, timespan)

List Air Marshal scan results from a network

List Air Marshal scan results from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    try {
      List<Object> result = apiInstance.getNetworkAirMarshal(networkId, t0, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkAirMarshal");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] |

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

<a id="getNetworkSiteToSiteVpn"></a>
# **getNetworkSiteToSiteVpn**
> Object getNetworkSiteToSiteVpn(networkId)

Return the site-to-site VPN settings of a network

Return the site-to-site VPN settings of a network. Only valid for MX networks.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkSiteToSiteVpn(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkSiteToSiteVpn");
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

<a id="getNetworkTraffic"></a>
# **getNetworkTraffic**
> List&lt;Object&gt; getNetworkTraffic(networkId, t0, timespan, deviceType)

Return the traffic analysis data for this network

Return the traffic analysis data for this network. Traffic analysis with hostname visibility must be enabled on the network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days.
    String deviceType = "appliance"; // String | Filter the data by device type: 'combined', 'wireless', 'switch' or 'appliance'. Defaults to 'combined'. When using 'combined', for each rule the data will come from the device type with the most usage.
    try {
      List<Object> result = apiInstance.getNetworkTraffic(networkId, t0, timespan, deviceType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getNetworkTraffic");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 30 days from today. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days. | [optional] |
| **deviceType** | **String**| Filter the data by device type: &#39;combined&#39;, &#39;wireless&#39;, &#39;switch&#39; or &#39;appliance&#39;. Defaults to &#39;combined&#39;. When using &#39;combined&#39;, for each rule the data will come from the device type with the most usage. | [optional] [enum: appliance, combined, switch, wireless] |

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

<a id="getOrganizationNetworks"></a>
# **getOrganizationNetworks**
> List&lt;Object&gt; getOrganizationNetworks(organizationId, configTemplateId)

List the networks in an organization

List the networks in an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String configTemplateId = "configTemplateId_example"; // String | An optional parameter that is the ID of a config template. Will return all networks bound to that template.
    try {
      List<Object> result = apiInstance.getOrganizationNetworks(organizationId, configTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#getOrganizationNetworks");
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
| **configTemplateId** | **String**| An optional parameter that is the ID of a config template. Will return all networks bound to that template. | [optional] |

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

<a id="splitNetwork"></a>
# **splitNetwork**
> Object splitNetwork(networkId)

Split a combined network into individual networks for each type of device

Split a combined network into individual networks for each type of device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.splitNetwork(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#splitNetwork");
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

<a id="unbindNetwork"></a>
# **unbindNetwork**
> unbindNetwork(networkId)

Unbind a network from a template.

Unbind a network from a template.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      apiInstance.unbindNetwork(networkId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#unbindNetwork");
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

<a id="updateNetwork"></a>
# **updateNetwork**
> Object updateNetwork(networkId, updateNetworkRequest)

Update a network

Update a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkRequest updateNetworkRequest = new UpdateNetworkRequest(); // UpdateNetworkRequest | 
    try {
      Object result = apiInstance.updateNetwork(networkId, updateNetworkRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetwork");
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
| **updateNetworkRequest** | [**UpdateNetworkRequest**](UpdateNetworkRequest.md)|  | [optional] |

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

<a id="updateNetworkSiteToSiteVpn"></a>
# **updateNetworkSiteToSiteVpn**
> Object updateNetworkSiteToSiteVpn(networkId, updateNetworkSiteToSiteVpnRequest)

Update the site-to-site VPN settings of a network

Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NetworksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    NetworksApi apiInstance = new NetworksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkSiteToSiteVpnRequest updateNetworkSiteToSiteVpnRequest = new UpdateNetworkSiteToSiteVpnRequest(); // UpdateNetworkSiteToSiteVpnRequest | 
    try {
      Object result = apiInstance.updateNetworkSiteToSiteVpn(networkId, updateNetworkSiteToSiteVpnRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NetworksApi#updateNetworkSiteToSiteVpn");
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
| **updateNetworkSiteToSiteVpnRequest** | [**UpdateNetworkSiteToSiteVpnRequest**](UpdateNetworkSiteToSiteVpnRequest.md)|  | |

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

