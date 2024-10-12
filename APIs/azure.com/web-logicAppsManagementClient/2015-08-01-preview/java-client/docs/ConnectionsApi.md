# ConnectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**connectionsConfirmConsentCode**](ConnectionsApi.md#connectionsConfirmConsentCode) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName}/confirmConsentCode |  |
| [**connectionsCreateOrUpdate**](ConnectionsApi.md#connectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName} |  |
| [**connectionsDelete**](ConnectionsApi.md#connectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName} |  |
| [**connectionsGet**](ConnectionsApi.md#connectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName} |  |
| [**connectionsList**](ConnectionsApi.md#connectionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections | Get Connections |
| [**connectionsListConnectionKeys**](ConnectionsApi.md#connectionsListConnectionKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName}/listConnectionKeys |  |
| [**connectionsListConsentLinks**](ConnectionsApi.md#connectionsListConsentLinks) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName}/listConsentLinks |  |


<a id="connectionsConfirmConsentCode"></a>
# **connectionsConfirmConsentCode**
> Connection connectionsConfirmConsentCode(subscriptionId, resourceGroupName, connectionName, apiVersion, content)



Confirms consent code of a connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionsApi apiInstance = new ConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String connectionName = "connectionName_example"; // String | The connection name.
    String apiVersion = "apiVersion_example"; // String | API Version
    ConfirmConsentCodeInput content = new ConfirmConsentCodeInput(); // ConfirmConsentCodeInput | The content.
    try {
      Connection result = apiInstance.connectionsConfirmConsentCode(subscriptionId, resourceGroupName, connectionName, apiVersion, content);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionsApi#connectionsConfirmConsentCode");
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
| **resourceGroupName** | **String**| The resource group name. | |
| **connectionName** | **String**| The connection name. | |
| **apiVersion** | **String**| API Version | |
| **content** | [**ConfirmConsentCodeInput**](ConfirmConsentCodeInput.md)| The content. | |

### Return type

[**Connection**](Connection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="connectionsCreateOrUpdate"></a>
# **connectionsCreateOrUpdate**
> Connection connectionsCreateOrUpdate(subscriptionId, resourceGroupName, connectionName, apiVersion, connection)



Creates or updates a connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionsApi apiInstance = new ConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String connectionName = "connectionName_example"; // String | The connection name.
    String apiVersion = "apiVersion_example"; // String | API Version
    Connection connection = new Connection(); // Connection | The connection.
    try {
      Connection result = apiInstance.connectionsCreateOrUpdate(subscriptionId, resourceGroupName, connectionName, apiVersion, connection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionsApi#connectionsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The resource group name. | |
| **connectionName** | **String**| The connection name. | |
| **apiVersion** | **String**| API Version | |
| **connection** | [**Connection**](Connection.md)| The connection. | |

### Return type

[**Connection**](Connection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |

<a id="connectionsDelete"></a>
# **connectionsDelete**
> connectionsDelete(subscriptionId, resourceGroupName, connectionName, apiVersion)



Deletes a connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionsApi apiInstance = new ConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String connectionName = "connectionName_example"; // String | The connection name.
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      apiInstance.connectionsDelete(subscriptionId, resourceGroupName, connectionName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionsApi#connectionsDelete");
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
| **resourceGroupName** | **String**| The resource group name. | |
| **connectionName** | **String**| The connection name. | |
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
| **200** | OK |  -  |
| **204** | No Content |  -  |

<a id="connectionsGet"></a>
# **connectionsGet**
> Connection connectionsGet(subscriptionId, resourceGroupName, connectionName, apiVersion)



Gets a connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionsApi apiInstance = new ConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String connectionName = "connectionName_example"; // String | The connection name.
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Connection result = apiInstance.connectionsGet(subscriptionId, resourceGroupName, connectionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionsApi#connectionsGet");
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
| **resourceGroupName** | **String**| The resource group name. | |
| **connectionName** | **String**| The connection name. | |
| **apiVersion** | **String**| API Version | |

### Return type

[**Connection**](Connection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="connectionsList"></a>
# **connectionsList**
> ConnectionCollection connectionsList(resourceGroupName, subscriptionId, apiVersion, $top, $filter)

Get Connections

Gets a list of connections.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionsApi apiInstance = new ConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Integer $top = 56; // Integer | The number of items to be included in the result.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    try {
      ConnectionCollection result = apiInstance.connectionsList(resourceGroupName, subscriptionId, apiVersion, $top, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionsApi#connectionsList");
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
| **resourceGroupName** | **String**| Resource Group Name | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **$top** | **Integer**| The number of items to be included in the result. | [optional] |
| **$filter** | **String**| The filter to apply on the operation. | [optional] |

### Return type

[**ConnectionCollection**](ConnectionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="connectionsListConnectionKeys"></a>
# **connectionsListConnectionKeys**
> ConnectionSecrets connectionsListConnectionKeys(subscriptionId, resourceGroupName, connectionName, apiVersion, content)



Lists connection keys.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionsApi apiInstance = new ConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String connectionName = "connectionName_example"; // String | The connection name.
    String apiVersion = "apiVersion_example"; // String | API Version
    ListConnectionKeysInput content = new ListConnectionKeysInput(); // ListConnectionKeysInput | The content.
    try {
      ConnectionSecrets result = apiInstance.connectionsListConnectionKeys(subscriptionId, resourceGroupName, connectionName, apiVersion, content);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionsApi#connectionsListConnectionKeys");
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
| **resourceGroupName** | **String**| The resource group name. | |
| **connectionName** | **String**| The connection name. | |
| **apiVersion** | **String**| API Version | |
| **content** | [**ListConnectionKeysInput**](ListConnectionKeysInput.md)| The content. | |

### Return type

[**ConnectionSecrets**](ConnectionSecrets.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="connectionsListConsentLinks"></a>
# **connectionsListConsentLinks**
> ConsentLinkPayload connectionsListConsentLinks(subscriptionId, resourceGroupName, connectionName, apiVersion, content)



Lists consent links of a connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ConnectionsApi apiInstance = new ConnectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String connectionName = "connectionName_example"; // String | The connection name.
    String apiVersion = "apiVersion_example"; // String | API Version
    ConsentLinkInput content = new ConsentLinkInput(); // ConsentLinkInput | The content.
    try {
      ConsentLinkPayload result = apiInstance.connectionsListConsentLinks(subscriptionId, resourceGroupName, connectionName, apiVersion, content);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionsApi#connectionsListConsentLinks");
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
| **resourceGroupName** | **String**| The resource group name. | |
| **connectionName** | **String**| The connection name. | |
| **apiVersion** | **String**| API Version | |
| **content** | [**ConsentLinkInput**](ConsentLinkInput.md)| The content. | |

### Return type

[**ConsentLinkPayload**](ConsentLinkPayload.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

