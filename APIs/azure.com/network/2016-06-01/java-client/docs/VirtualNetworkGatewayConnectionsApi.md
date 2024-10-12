# VirtualNetworkGatewayConnectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualNetworkGatewayConnectionsCreateOrUpdate**](VirtualNetworkGatewayConnectionsApi.md#virtualNetworkGatewayConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName} |  |
| [**virtualNetworkGatewayConnectionsDelete**](VirtualNetworkGatewayConnectionsApi.md#virtualNetworkGatewayConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName} |  |
| [**virtualNetworkGatewayConnectionsGet**](VirtualNetworkGatewayConnectionsApi.md#virtualNetworkGatewayConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName} |  |
| [**virtualNetworkGatewayConnectionsGetSharedKey**](VirtualNetworkGatewayConnectionsApi.md#virtualNetworkGatewayConnectionsGetSharedKey) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey |  |
| [**virtualNetworkGatewayConnectionsList**](VirtualNetworkGatewayConnectionsApi.md#virtualNetworkGatewayConnectionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections |  |
| [**virtualNetworkGatewayConnectionsResetSharedKey**](VirtualNetworkGatewayConnectionsApi.md#virtualNetworkGatewayConnectionsResetSharedKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey/reset |  |
| [**virtualNetworkGatewayConnectionsSetSharedKey**](VirtualNetworkGatewayConnectionsApi.md#virtualNetworkGatewayConnectionsSetSharedKey) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/connections/{virtualNetworkGatewayConnectionName}/sharedkey |  |


<a id="virtualNetworkGatewayConnectionsCreateOrUpdate"></a>
# **virtualNetworkGatewayConnectionsCreateOrUpdate**
> VirtualNetworkGatewayConnection virtualNetworkGatewayConnectionsCreateOrUpdate(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters)



The Put VirtualNetworkGatewayConnection operation creates/updates a virtual network gateway connection in the specified resource group through Network resource provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkGatewayConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkGatewayConnectionsApi apiInstance = new VirtualNetworkGatewayConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualNetworkGatewayConnectionName = "virtualNetworkGatewayConnectionName_example"; // String | The name of the virtual network gateway connection.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VirtualNetworkGatewayConnection parameters = new VirtualNetworkGatewayConnection(); // VirtualNetworkGatewayConnection | Parameters supplied to the Begin Create or update Virtual Network Gateway connection operation through Network resource provider.
    try {
      VirtualNetworkGatewayConnection result = apiInstance.virtualNetworkGatewayConnectionsCreateOrUpdate(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewayConnectionsApi#virtualNetworkGatewayConnectionsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **virtualNetworkGatewayConnectionName** | **String**| The name of the virtual network gateway connection. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**VirtualNetworkGatewayConnection**](VirtualNetworkGatewayConnection.md)| Parameters supplied to the Begin Create or update Virtual Network Gateway connection operation through Network resource provider. | |

### Return type

[**VirtualNetworkGatewayConnection**](VirtualNetworkGatewayConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **201** |  |  -  |

<a id="virtualNetworkGatewayConnectionsDelete"></a>
# **virtualNetworkGatewayConnectionsDelete**
> virtualNetworkGatewayConnectionsDelete(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId)



The Delete VirtualNetworkGatewayConnection operation deletes the specified virtual network Gateway connection through Network resource provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkGatewayConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkGatewayConnectionsApi apiInstance = new VirtualNetworkGatewayConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualNetworkGatewayConnectionName = "virtualNetworkGatewayConnectionName_example"; // String | The name of the virtual network gateway connection.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.virtualNetworkGatewayConnectionsDelete(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewayConnectionsApi#virtualNetworkGatewayConnectionsDelete");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **virtualNetworkGatewayConnectionName** | **String**| The name of the virtual network gateway connection. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **202** |  |  -  |
| **204** |  |  -  |

<a id="virtualNetworkGatewayConnectionsGet"></a>
# **virtualNetworkGatewayConnectionsGet**
> VirtualNetworkGatewayConnection virtualNetworkGatewayConnectionsGet(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId)



The Get VirtualNetworkGatewayConnection operation retrieves information about the specified virtual network gateway connection through Network resource provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkGatewayConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkGatewayConnectionsApi apiInstance = new VirtualNetworkGatewayConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualNetworkGatewayConnectionName = "virtualNetworkGatewayConnectionName_example"; // String | The name of the virtual network gateway connection.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VirtualNetworkGatewayConnection result = apiInstance.virtualNetworkGatewayConnectionsGet(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewayConnectionsApi#virtualNetworkGatewayConnectionsGet");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **virtualNetworkGatewayConnectionName** | **String**| The name of the virtual network gateway connection. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**VirtualNetworkGatewayConnection**](VirtualNetworkGatewayConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualNetworkGatewayConnectionsGetSharedKey"></a>
# **virtualNetworkGatewayConnectionsGetSharedKey**
> ConnectionSharedKeyResult virtualNetworkGatewayConnectionsGetSharedKey(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId)



The Get VirtualNetworkGatewayConnectionSharedKey operation retrieves information about the specified virtual network gateway connection shared key through Network resource provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkGatewayConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkGatewayConnectionsApi apiInstance = new VirtualNetworkGatewayConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualNetworkGatewayConnectionName = "virtualNetworkGatewayConnectionName_example"; // String | The virtual network gateway connection shared key name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      ConnectionSharedKeyResult result = apiInstance.virtualNetworkGatewayConnectionsGetSharedKey(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewayConnectionsApi#virtualNetworkGatewayConnectionsGetSharedKey");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **virtualNetworkGatewayConnectionName** | **String**| The virtual network gateway connection shared key name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**ConnectionSharedKeyResult**](ConnectionSharedKeyResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualNetworkGatewayConnectionsList"></a>
# **virtualNetworkGatewayConnectionsList**
> VirtualNetworkGatewayConnectionListResult virtualNetworkGatewayConnectionsList(resourceGroupName, apiVersion, subscriptionId)



The List VirtualNetworkGatewayConnections operation retrieves all the virtual network gateways connections created.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkGatewayConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkGatewayConnectionsApi apiInstance = new VirtualNetworkGatewayConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VirtualNetworkGatewayConnectionListResult result = apiInstance.virtualNetworkGatewayConnectionsList(resourceGroupName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewayConnectionsApi#virtualNetworkGatewayConnectionsList");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**VirtualNetworkGatewayConnectionListResult**](VirtualNetworkGatewayConnectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="virtualNetworkGatewayConnectionsResetSharedKey"></a>
# **virtualNetworkGatewayConnectionsResetSharedKey**
> ConnectionResetSharedKey virtualNetworkGatewayConnectionsResetSharedKey(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters)



The VirtualNetworkGatewayConnectionResetSharedKey operation resets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkGatewayConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkGatewayConnectionsApi apiInstance = new VirtualNetworkGatewayConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualNetworkGatewayConnectionName = "virtualNetworkGatewayConnectionName_example"; // String | The virtual network gateway connection reset shared key Name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ConnectionResetSharedKey parameters = new ConnectionResetSharedKey(); // ConnectionResetSharedKey | Parameters supplied to the Begin Reset Virtual Network Gateway connection shared key operation through Network resource provider.
    try {
      ConnectionResetSharedKey result = apiInstance.virtualNetworkGatewayConnectionsResetSharedKey(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewayConnectionsApi#virtualNetworkGatewayConnectionsResetSharedKey");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **virtualNetworkGatewayConnectionName** | **String**| The virtual network gateway connection reset shared key Name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ConnectionResetSharedKey**](ConnectionResetSharedKey.md)| Parameters supplied to the Begin Reset Virtual Network Gateway connection shared key operation through Network resource provider. | |

### Return type

[**ConnectionResetSharedKey**](ConnectionResetSharedKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **202** |  |  -  |

<a id="virtualNetworkGatewayConnectionsSetSharedKey"></a>
# **virtualNetworkGatewayConnectionsSetSharedKey**
> ConnectionSharedKey virtualNetworkGatewayConnectionsSetSharedKey(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters)



The Put VirtualNetworkGatewayConnectionSharedKey operation sets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkGatewayConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    VirtualNetworkGatewayConnectionsApi apiInstance = new VirtualNetworkGatewayConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String virtualNetworkGatewayConnectionName = "virtualNetworkGatewayConnectionName_example"; // String | The virtual network gateway connection name.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    ConnectionSharedKey parameters = new ConnectionSharedKey(); // ConnectionSharedKey | Parameters supplied to the Begin Set Virtual Network Gateway connection Shared key operation throughNetwork resource provider.
    try {
      ConnectionSharedKey result = apiInstance.virtualNetworkGatewayConnectionsSetSharedKey(resourceGroupName, virtualNetworkGatewayConnectionName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkGatewayConnectionsApi#virtualNetworkGatewayConnectionsSetSharedKey");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **virtualNetworkGatewayConnectionName** | **String**| The virtual network gateway connection name. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**ConnectionSharedKey**](ConnectionSharedKey.md)| Parameters supplied to the Begin Set Virtual Network Gateway connection Shared key operation throughNetwork resource provider. | |

### Return type

[**ConnectionSharedKey**](ConnectionSharedKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **201** |  |  -  |

