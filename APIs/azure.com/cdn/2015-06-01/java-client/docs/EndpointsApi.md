# EndpointsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**endpointsCreate**](EndpointsApi.md#endpointsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName} | Creates a new CDN endpoint with the specified parameters. |
| [**endpointsDeleteIfExists**](EndpointsApi.md#endpointsDeleteIfExists) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName} | Deletes an existing CDN endpoint with the specified parameters. |
| [**endpointsGet**](EndpointsApi.md#endpointsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName} | Gets an existing CDN endpoint with the specified parameters. |
| [**endpointsListByProfile**](EndpointsApi.md#endpointsListByProfile) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints | Lists existing CDN endpoints within a profile. |
| [**endpointsLoadContent**](EndpointsApi.md#endpointsLoadContent) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/load | Forcibly pre-loads CDN endpoint content. |
| [**endpointsPurgeContent**](EndpointsApi.md#endpointsPurgeContent) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/purge | Forcibly purges CDN endpoint content. |
| [**endpointsStart**](EndpointsApi.md#endpointsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/start | Starts an existing stopped CDN endpoint. |
| [**endpointsStop**](EndpointsApi.md#endpointsStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/stop | Stops an existing running CDN endpoint. |
| [**endpointsUpdate**](EndpointsApi.md#endpointsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName} | Updates an existing CDN endpoint with the specified parameters. Only tags and OriginHostHeader can be updated after creating an endpoint. To update origins, use the Update Origin operation. To update custom domains, use the Update Custom Domain operation. |
| [**endpointsValidateCustomDomain**](EndpointsApi.md#endpointsValidateCustomDomain) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/validateCustomDomain | Validates a custom domain mapping to ensure it maps to the correct CNAME in DNS. |


<a id="endpointsCreate"></a>
# **endpointsCreate**
> Endpoint endpointsCreate(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion, endpointProperties)

Creates a new CDN endpoint with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    EndpointCreateParameters endpointProperties = new EndpointCreateParameters(); // EndpointCreateParameters | Endpoint properties
    try {
      Endpoint result = apiInstance.endpointsCreate(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion, endpointProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#endpointsCreate");
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
| **endpointName** | **String**| Name of the endpoint within the CDN profile. | |
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |
| **endpointProperties** | [**EndpointCreateParameters**](EndpointCreateParameters.md)| Endpoint properties | |

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="endpointsDeleteIfExists"></a>
# **endpointsDeleteIfExists**
> endpointsDeleteIfExists(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion)

Deletes an existing CDN endpoint with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      apiInstance.endpointsDeleteIfExists(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#endpointsDeleteIfExists");
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
| **endpointName** | **String**| Name of the endpoint within the CDN profile. | |
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |
| **204** | No Content |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="endpointsGet"></a>
# **endpointsGet**
> Endpoint endpointsGet(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion)

Gets an existing CDN endpoint with the specified parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      Endpoint result = apiInstance.endpointsGet(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#endpointsGet");
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
| **endpointName** | **String**| Name of the endpoint within the CDN profile. | |
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="endpointsListByProfile"></a>
# **endpointsListByProfile**
> EndpointListResult endpointsListByProfile(profileName, resourceGroupName, subscriptionId, apiVersion)

Lists existing CDN endpoints within a profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      EndpointListResult result = apiInstance.endpointsListByProfile(profileName, resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#endpointsListByProfile");
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
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |

### Return type

[**EndpointListResult**](EndpointListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="endpointsLoadContent"></a>
# **endpointsLoadContent**
> endpointsLoadContent(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion, contentFilePaths)

Forcibly pre-loads CDN endpoint content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    LoadParameters contentFilePaths = new LoadParameters(); // LoadParameters | The path to the content to be loaded. Path should describe a file.
    try {
      apiInstance.endpointsLoadContent(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion, contentFilePaths);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#endpointsLoadContent");
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
| **endpointName** | **String**| Name of the endpoint within the CDN profile. | |
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |
| **contentFilePaths** | [**LoadParameters**](LoadParameters.md)| The path to the content to be loaded. Path should describe a file. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="endpointsPurgeContent"></a>
# **endpointsPurgeContent**
> endpointsPurgeContent(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion, contentFilePaths)

Forcibly purges CDN endpoint content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    PurgeParameters contentFilePaths = new PurgeParameters(); // PurgeParameters | The path to the content to be purged. Path can describe a file or directory.
    try {
      apiInstance.endpointsPurgeContent(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion, contentFilePaths);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#endpointsPurgeContent");
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
| **endpointName** | **String**| Name of the endpoint within the CDN profile. | |
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |
| **contentFilePaths** | [**PurgeParameters**](PurgeParameters.md)| The path to the content to be purged. Path can describe a file or directory. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="endpointsStart"></a>
# **endpointsStart**
> Endpoint endpointsStart(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion)

Starts an existing stopped CDN endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      Endpoint result = apiInstance.endpointsStart(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#endpointsStart");
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
| **endpointName** | **String**| Name of the endpoint within the CDN profile. | |
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="endpointsStop"></a>
# **endpointsStop**
> Endpoint endpointsStop(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion)

Stops an existing running CDN endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      Endpoint result = apiInstance.endpointsStop(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#endpointsStop");
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
| **endpointName** | **String**| Name of the endpoint within the CDN profile. | |
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="endpointsUpdate"></a>
# **endpointsUpdate**
> Endpoint endpointsUpdate(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion, endpointProperties)

Updates an existing CDN endpoint with the specified parameters. Only tags and OriginHostHeader can be updated after creating an endpoint. To update origins, use the Update Origin operation. To update custom domains, use the Update Custom Domain operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    EndpointUpdateParameters endpointProperties = new EndpointUpdateParameters(); // EndpointUpdateParameters | Endpoint properties
    try {
      Endpoint result = apiInstance.endpointsUpdate(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion, endpointProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#endpointsUpdate");
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
| **endpointName** | **String**| Name of the endpoint within the CDN profile. | |
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |
| **endpointProperties** | [**EndpointUpdateParameters**](EndpointUpdateParameters.md)| Endpoint properties | |

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted and  the operation will complete asynchronously |  -  |
| **0** | CDN error response describing why the operation failed |  -  |

<a id="endpointsValidateCustomDomain"></a>
# **endpointsValidateCustomDomain**
> ValidateCustomDomainOutput endpointsValidateCustomDomain(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion, customDomainProperties)

Validates a custom domain mapping to ensure it maps to the correct CNAME in DNS.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    EndpointsApi apiInstance = new EndpointsApi(defaultClient);
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    ValidateCustomDomainInput customDomainProperties = new ValidateCustomDomainInput(); // ValidateCustomDomainInput | Custom domain to validate.
    try {
      ValidateCustomDomainOutput result = apiInstance.endpointsValidateCustomDomain(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion, customDomainProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#endpointsValidateCustomDomain");
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
| **endpointName** | **String**| Name of the endpoint within the CDN profile. | |
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |
| **customDomainProperties** | [**ValidateCustomDomainInput**](ValidateCustomDomainInput.md)| Custom domain to validate. | |

### Return type

[**ValidateCustomDomainOutput**](ValidateCustomDomainOutput.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

