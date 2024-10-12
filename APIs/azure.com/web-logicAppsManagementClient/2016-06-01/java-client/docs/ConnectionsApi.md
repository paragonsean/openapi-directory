# ConnectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**connectionsConfirmConsentCode**](ConnectionsApi.md#connectionsConfirmConsentCode) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName}/confirmConsentCode | Confirms the consent code for a connection |
| [**connectionsCreateOrUpdate**](ConnectionsApi.md#connectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName} | Replace an existing connection |
| [**connectionsDelete**](ConnectionsApi.md#connectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName} | Delete an existing connection |
| [**connectionsGet**](ConnectionsApi.md#connectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName} | Get a connection |
| [**connectionsList**](ConnectionsApi.md#connectionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections | Get all connections |
| [**connectionsListConsentLinks**](ConnectionsApi.md#connectionsListConsentLinks) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName}/listConsentLinks | Lists consent links for a connection |
| [**connectionsUpdate**](ConnectionsApi.md#connectionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName} | Update an existing connection |


<a id="connectionsConfirmConsentCode"></a>
# **connectionsConfirmConsentCode**
> ConfirmConsentCodeDefinition connectionsConfirmConsentCode(subscriptionId, resourceGroupName, connectionName, apiVersion, confirmConsentCode)

Confirms the consent code for a connection

Confirms consent code of a connection

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
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String connectionName = "connectionName_example"; // String | Connection name
    String apiVersion = "apiVersion_example"; // String | API Version
    ConfirmConsentCodeDefinition confirmConsentCode = new ConfirmConsentCodeDefinition(); // ConfirmConsentCodeDefinition | The consent code confirmation
    try {
      ConfirmConsentCodeDefinition result = apiInstance.connectionsConfirmConsentCode(subscriptionId, resourceGroupName, connectionName, apiVersion, confirmConsentCode);
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
| **resourceGroupName** | **String**| The resource group | |
| **connectionName** | **String**| Connection name | |
| **apiVersion** | **String**| API Version | |
| **confirmConsentCode** | [**ConfirmConsentCodeDefinition**](ConfirmConsentCodeDefinition.md)| The consent code confirmation | |

### Return type

[**ConfirmConsentCodeDefinition**](ConfirmConsentCodeDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Confirmation of the consent code |  -  |

<a id="connectionsCreateOrUpdate"></a>
# **connectionsCreateOrUpdate**
> ApiConnectionDefinition connectionsCreateOrUpdate(subscriptionId, resourceGroupName, connectionName, apiVersion, connection)

Replace an existing connection

Creates or updates a connection

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
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String connectionName = "connectionName_example"; // String | Connection name
    String apiVersion = "apiVersion_example"; // String | API Version
    ApiConnectionDefinition connection = new ApiConnectionDefinition(); // ApiConnectionDefinition | The connection
    try {
      ApiConnectionDefinition result = apiInstance.connectionsCreateOrUpdate(subscriptionId, resourceGroupName, connectionName, apiVersion, connection);
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
| **resourceGroupName** | **String**| The resource group | |
| **connectionName** | **String**| Connection name | |
| **apiVersion** | **String**| API Version | |
| **connection** | [**ApiConnectionDefinition**](ApiConnectionDefinition.md)| The connection | |

### Return type

[**ApiConnectionDefinition**](ApiConnectionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | New API connection created |  -  |
| **201** | Already existing API connection updated |  -  |

<a id="connectionsDelete"></a>
# **connectionsDelete**
> connectionsDelete(subscriptionId, resourceGroupName, connectionName, apiVersion)

Delete an existing connection

Deletes a connection

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
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String connectionName = "connectionName_example"; // String | Connection name
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
| **resourceGroupName** | **String**| The resource group | |
| **connectionName** | **String**| Connection name | |
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
| **200** | Successfully deleted the connection |  -  |
| **204** | No connection to delete |  -  |

<a id="connectionsGet"></a>
# **connectionsGet**
> ApiConnectionDefinition connectionsGet(subscriptionId, resourceGroupName, connectionName, apiVersion)

Get a connection

Get a specific connection

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
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String connectionName = "connectionName_example"; // String | Connection name
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ApiConnectionDefinition result = apiInstance.connectionsGet(subscriptionId, resourceGroupName, connectionName, apiVersion);
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
| **resourceGroupName** | **String**| The resource group | |
| **connectionName** | **String**| Connection name | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ApiConnectionDefinition**](ApiConnectionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An API connection |  -  |

<a id="connectionsList"></a>
# **connectionsList**
> ApiConnectionDefinitionCollection connectionsList(subscriptionId, resourceGroupName, apiVersion, $top, $filter)

Get all connections

Gets a list of connections

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
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String apiVersion = "apiVersion_example"; // String | API Version
    Integer $top = 56; // Integer | The number of items to be included in the result
    String $filter = "$filter_example"; // String | The filter to apply on the operation
    try {
      ApiConnectionDefinitionCollection result = apiInstance.connectionsList(subscriptionId, resourceGroupName, apiVersion, $top, $filter);
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
| **subscriptionId** | **String**| Subscription Id | |
| **resourceGroupName** | **String**| The resource group | |
| **apiVersion** | **String**| API Version | |
| **$top** | **Integer**| The number of items to be included in the result | [optional] |
| **$filter** | **String**| The filter to apply on the operation | [optional] |

### Return type

[**ApiConnectionDefinitionCollection**](ApiConnectionDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of API connection |  -  |

<a id="connectionsListConsentLinks"></a>
# **connectionsListConsentLinks**
> ConsentLinkCollection connectionsListConsentLinks(subscriptionId, resourceGroupName, connectionName, apiVersion, listConsentLink)

Lists consent links for a connection

Lists the consent links of a connection

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
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String connectionName = "connectionName_example"; // String | Connection name
    String apiVersion = "apiVersion_example"; // String | API Version
    ListConsentLinksDefinition listConsentLink = new ListConsentLinksDefinition(); // ListConsentLinksDefinition | The consent links
    try {
      ConsentLinkCollection result = apiInstance.connectionsListConsentLinks(subscriptionId, resourceGroupName, connectionName, apiVersion, listConsentLink);
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
| **resourceGroupName** | **String**| The resource group | |
| **connectionName** | **String**| Connection name | |
| **apiVersion** | **String**| API Version | |
| **listConsentLink** | [**ListConsentLinksDefinition**](ListConsentLinksDefinition.md)| The consent links | |

### Return type

[**ConsentLinkCollection**](ConsentLinkCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of the consent links |  -  |

<a id="connectionsUpdate"></a>
# **connectionsUpdate**
> ApiConnectionDefinition connectionsUpdate(subscriptionId, resourceGroupName, connectionName, apiVersion, connection)

Update an existing connection

Updates a connection&#39;s tags

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
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group
    String connectionName = "connectionName_example"; // String | Connection name
    String apiVersion = "apiVersion_example"; // String | API Version
    ApiConnectionDefinition connection = new ApiConnectionDefinition(); // ApiConnectionDefinition | The connection
    try {
      ApiConnectionDefinition result = apiInstance.connectionsUpdate(subscriptionId, resourceGroupName, connectionName, apiVersion, connection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionsApi#connectionsUpdate");
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
| **connectionName** | **String**| Connection name | |
| **apiVersion** | **String**| API Version | |
| **connection** | [**ApiConnectionDefinition**](ApiConnectionDefinition.md)| The connection | |

### Return type

[**ApiConnectionDefinition**](ApiConnectionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | API connection updated |  -  |

