# ConnectionGatewaysApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**connectionGatewayInstallationsGet**](ConnectionGatewaysApi.md#connectionGatewayInstallationsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/connectionGatewayInstallations/{gatewayId} | Gets an installed gateway that the user is an admin of |
| [**connectionGatewayInstallationsList**](ConnectionGatewaysApi.md#connectionGatewayInstallationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/connectionGatewayInstallations | Gets a list of installed gateways that the user is an admin of |
| [**connectionGatewaysCreateOrUpdate**](ConnectionGatewaysApi.md#connectionGatewaysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connectionGateways/{connectionGatewayName} | Replaces a specific gateway |
| [**connectionGatewaysDelete**](ConnectionGatewaysApi.md#connectionGatewaysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connectionGateways/{connectionGatewayName} | Deletes a specific gateway |
| [**connectionGatewaysGet**](ConnectionGatewaysApi.md#connectionGatewaysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connectionGateways/{connectionGatewayName} | Gets a specific gateway |
| [**connectionGatewaysList**](ConnectionGatewaysApi.md#connectionGatewaysList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/connectionGateways | Lists all of the connection gateways |
| [**connectionGatewaysListByResourceGroup**](ConnectionGatewaysApi.md#connectionGatewaysListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connectionGateways | Lists all of the connection gateways |
| [**connectionGatewaysUpdate**](ConnectionGatewaysApi.md#connectionGatewaysUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connectionGateways/{connectionGatewayName} | Updates a specific gateway |


<a id="connectionGatewayInstallationsGet"></a>
# **connectionGatewayInstallationsGet**
> ConnectionGatewayInstallationDefinition connectionGatewayInstallationsGet(subscriptionId, location, gatewayId, apiVersion)

Gets an installed gateway that the user is an admin of

Get a specific installed gateway that the user is an admin of, in a specific subscription and at a certain location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionGatewaysApi apiInstance = new ConnectionGatewaysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String location = "location_example"; // String | The location
    String gatewayId = "gatewayId_example"; // String | Gateway ID
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ConnectionGatewayInstallationDefinition result = apiInstance.connectionGatewayInstallationsGet(subscriptionId, location, gatewayId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionGatewaysApi#connectionGatewayInstallationsGet");
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
| **subscriptionId** | **String**| Subscription Id | |
| **location** | **String**| The location | |
| **gatewayId** | **String**| Gateway ID | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ConnectionGatewayInstallationDefinition**](ConnectionGatewayInstallationDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The gateway installation |  -  |

<a id="connectionGatewayInstallationsList"></a>
# **connectionGatewayInstallationsList**
> ConnectionGatewayInstallationDefinitionCollection connectionGatewayInstallationsList(subscriptionId, location, apiVersion)

Gets a list of installed gateways that the user is an admin of

Gets a list of installed gateways that the user is an admin of, in a specific subscription and at a certain location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionGatewaysApi apiInstance = new ConnectionGatewaysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String location = "location_example"; // String | The location
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ConnectionGatewayInstallationDefinitionCollection result = apiInstance.connectionGatewayInstallationsList(subscriptionId, location, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionGatewaysApi#connectionGatewayInstallationsList");
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
| **subscriptionId** | **String**| Subscription Id | |
| **location** | **String**| The location | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ConnectionGatewayInstallationDefinitionCollection**](ConnectionGatewayInstallationDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The gateway installations |  -  |

<a id="connectionGatewaysCreateOrUpdate"></a>
# **connectionGatewaysCreateOrUpdate**
> ConnectionGatewayDefinition connectionGatewaysCreateOrUpdate(subscriptionId, resourceGroupName, connectionGatewayName, apiVersion, connectionGateway)

Replaces a specific gateway

Creates or updates a specific gateway for under a subscription and in a specific resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionGatewaysApi apiInstance = new ConnectionGatewaysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String connectionGatewayName = "connectionGatewayName_example"; // String | The connection gateway name
    String apiVersion = "apiVersion_example"; // String | API Version
    ConnectionGatewayDefinition connectionGateway = new ConnectionGatewayDefinition(); // ConnectionGatewayDefinition | The connection gateway
    try {
      ConnectionGatewayDefinition result = apiInstance.connectionGatewaysCreateOrUpdate(subscriptionId, resourceGroupName, connectionGatewayName, apiVersion, connectionGateway);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionGatewaysApi#connectionGatewaysCreateOrUpdate");
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
| **subscriptionId** | **String**| Subscription Id | |
| **resourceGroupName** | **String**| The resource group | |
| **connectionGatewayName** | **String**| The connection gateway name | |
| **apiVersion** | **String**| API Version | |
| **connectionGateway** | [**ConnectionGatewayDefinition**](ConnectionGatewayDefinition.md)| The connection gateway | |

### Return type

[**ConnectionGatewayDefinition**](ConnectionGatewayDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated gateway definition |  -  |
| **201** | The newly created gateway definition |  -  |

<a id="connectionGatewaysDelete"></a>
# **connectionGatewaysDelete**
> connectionGatewaysDelete(subscriptionId, resourceGroupName, connectionGatewayName, apiVersion)

Deletes a specific gateway

Deletes a specific gateway for under a subscription and in a specific resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionGatewaysApi apiInstance = new ConnectionGatewaysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String connectionGatewayName = "connectionGatewayName_example"; // String | The connection gateway name
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      apiInstance.connectionGatewaysDelete(subscriptionId, resourceGroupName, connectionGatewayName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionGatewaysApi#connectionGatewaysDelete");
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
| **subscriptionId** | **String**| Subscription Id | |
| **resourceGroupName** | **String**| The resource group | |
| **connectionGatewayName** | **String**| The connection gateway name | |
| **apiVersion** | **String**| API Version | |

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
| **200** | Successfully deleted the connection gateway |  -  |
| **204** | No connection gateway to delete |  -  |

<a id="connectionGatewaysGet"></a>
# **connectionGatewaysGet**
> ConnectionGatewayDefinition connectionGatewaysGet(subscriptionId, resourceGroupName, connectionGatewayName, apiVersion)

Gets a specific gateway

Gets a specific gateway under a subscription and in a specific resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionGatewaysApi apiInstance = new ConnectionGatewaysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String connectionGatewayName = "connectionGatewayName_example"; // String | The connection gateway name
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ConnectionGatewayDefinition result = apiInstance.connectionGatewaysGet(subscriptionId, resourceGroupName, connectionGatewayName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionGatewaysApi#connectionGatewaysGet");
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
| **subscriptionId** | **String**| Subscription Id | |
| **resourceGroupName** | **String**| The resource group | |
| **connectionGatewayName** | **String**| The connection gateway name | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ConnectionGatewayDefinition**](ConnectionGatewayDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The gateway definition |  -  |

<a id="connectionGatewaysList"></a>
# **connectionGatewaysList**
> ConnectionGatewayDefinitionCollection connectionGatewaysList(subscriptionId, apiVersion)

Lists all of the connection gateways

Gets a list of gateways under a subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionGatewaysApi apiInstance = new ConnectionGatewaysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ConnectionGatewayDefinitionCollection result = apiInstance.connectionGatewaysList(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionGatewaysApi#connectionGatewaysList");
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
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ConnectionGatewayDefinitionCollection**](ConnectionGatewayDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The gateway definitions |  -  |

<a id="connectionGatewaysListByResourceGroup"></a>
# **connectionGatewaysListByResourceGroup**
> ConnectionGatewayDefinitionCollection connectionGatewaysListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)

Lists all of the connection gateways

Gets a list of gateways under a subscription and in a specific resource group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionGatewaysApi apiInstance = new ConnectionGatewaysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ConnectionGatewayDefinitionCollection result = apiInstance.connectionGatewaysListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionGatewaysApi#connectionGatewaysListByResourceGroup");
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
| **subscriptionId** | **String**| Subscription Id | |
| **resourceGroupName** | **String**| The resource group | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ConnectionGatewayDefinitionCollection**](ConnectionGatewayDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The gateway definitions |  -  |

<a id="connectionGatewaysUpdate"></a>
# **connectionGatewaysUpdate**
> ConnectionGatewayDefinition connectionGatewaysUpdate(subscriptionId, resourceGroupName, connectionGatewayName, apiVersion, connectionGateway)

Updates a specific gateway

Updates a connection gateway&#39;s tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionGatewaysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionGatewaysApi apiInstance = new ConnectionGatewaysApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String connectionGatewayName = "connectionGatewayName_example"; // String | The connection gateway name
    String apiVersion = "apiVersion_example"; // String | API Version
    ConnectionGatewayDefinition connectionGateway = new ConnectionGatewayDefinition(); // ConnectionGatewayDefinition | The connection gateway
    try {
      ConnectionGatewayDefinition result = apiInstance.connectionGatewaysUpdate(subscriptionId, resourceGroupName, connectionGatewayName, apiVersion, connectionGateway);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionGatewaysApi#connectionGatewaysUpdate");
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
| **subscriptionId** | **String**| Subscription Id | |
| **resourceGroupName** | **String**| The resource group | |
| **connectionGatewayName** | **String**| The connection gateway name | |
| **apiVersion** | **String**| API Version | |
| **connectionGateway** | [**ConnectionGatewayDefinition**](ConnectionGatewayDefinition.md)| The connection gateway | |

### Return type

[**ConnectionGatewayDefinition**](ConnectionGatewayDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The gateway definition |  -  |

