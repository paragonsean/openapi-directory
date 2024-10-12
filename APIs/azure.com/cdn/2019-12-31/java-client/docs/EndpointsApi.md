# EndpointsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**endpointsCreate**](EndpointsApi.md#endpointsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName} |  |
| [**endpointsDelete**](EndpointsApi.md#endpointsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName} |  |
| [**endpointsGet**](EndpointsApi.md#endpointsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName} |  |
| [**endpointsListByProfile**](EndpointsApi.md#endpointsListByProfile) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints |  |
| [**endpointsListResourceUsage**](EndpointsApi.md#endpointsListResourceUsage) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/checkResourceUsage |  |
| [**endpointsLoadContent**](EndpointsApi.md#endpointsLoadContent) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/load |  |
| [**endpointsPurgeContent**](EndpointsApi.md#endpointsPurgeContent) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/purge |  |
| [**endpointsStart**](EndpointsApi.md#endpointsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/start |  |
| [**endpointsStop**](EndpointsApi.md#endpointsStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/stop |  |
| [**endpointsUpdate**](EndpointsApi.md#endpointsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName} |  |
| [**endpointsValidateCustomDomain**](EndpointsApi.md#endpointsValidateCustomDomain) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/validateCustomDomain |  |


<a id="endpointsCreate"></a>
# **endpointsCreate**
> Endpoint endpointsCreate(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, endpoint)



Creates a new CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    Endpoint endpoint = new Endpoint(); // Endpoint | Endpoint properties
    try {
      Endpoint result = apiInstance.endpointsCreate(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, endpoint);
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |
| **endpoint** | [**Endpoint**](Endpoint.md)| Endpoint properties | |

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
| **200** | OK. The request has succeeded. |  -  |
| **201** | Created. The request has been fulfilled and a new endpoint has been created. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="endpointsDelete"></a>
# **endpointsDelete**
> endpointsDelete(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion)



Deletes an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    try {
      apiInstance.endpointsDelete(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#endpointsDelete");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |

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
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | No Content. The request has been accepted but the endpoint was not found. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="endpointsGet"></a>
# **endpointsGet**
> Endpoint endpointsGet(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion)



Gets an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    try {
      Endpoint result = apiInstance.endpointsGet(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion);
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |

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
| **200** | OK. The request has succeeded. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="endpointsListByProfile"></a>
# **endpointsListByProfile**
> EndpointListResult endpointsListByProfile(resourceGroupName, profileName, subscriptionId, apiVersion)



Lists existing CDN endpoints.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    try {
      EndpointListResult result = apiInstance.endpointsListByProfile(resourceGroupName, profileName, subscriptionId, apiVersion);
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |

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
| **200** | OK. The request has succeeded. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="endpointsListResourceUsage"></a>
# **endpointsListResourceUsage**
> ResourceUsageListResult endpointsListResourceUsage(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion)



Checks the quota and usage of geo filters and custom domains under the given endpoint.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    try {
      ResourceUsageListResult result = apiInstance.endpointsListResourceUsage(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EndpointsApi#endpointsListResourceUsage");
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |

### Return type

[**ResourceUsageListResult**](ResourceUsageListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="endpointsLoadContent"></a>
# **endpointsLoadContent**
> endpointsLoadContent(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, contentFilePaths)



Pre-loads a content to CDN. Available for Verizon Profiles.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    LoadParameters contentFilePaths = new LoadParameters(); // LoadParameters | The path to the content to be loaded. Path should be a full URL, e.g. ‘/pictures/city.png' which loads a single file 
    try {
      apiInstance.endpointsLoadContent(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, contentFilePaths);
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |
| **contentFilePaths** | [**LoadParameters**](LoadParameters.md)| The path to the content to be loaded. Path should be a full URL, e.g. ‘/pictures/city.png&#39; which loads a single file  | |

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
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="endpointsPurgeContent"></a>
# **endpointsPurgeContent**
> endpointsPurgeContent(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, contentFilePaths)



Removes a content from CDN.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    PurgeParameters contentFilePaths = new PurgeParameters(); // PurgeParameters | The path to the content to be purged. Path can be a full URL, e.g. '/pictures/city.png' which removes a single file, or a directory with a wildcard, e.g. '/pictures/_*' which removes all folders and files in the directory.
    try {
      apiInstance.endpointsPurgeContent(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, contentFilePaths);
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |
| **contentFilePaths** | [**PurgeParameters**](PurgeParameters.md)| The path to the content to be purged. Path can be a full URL, e.g. &#39;/pictures/city.png&#39; which removes a single file, or a directory with a wildcard, e.g. &#39;/pictures/_*&#39; which removes all folders and files in the directory. | |

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
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="endpointsStart"></a>
# **endpointsStart**
> Endpoint endpointsStart(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion)



Starts an existing CDN endpoint that is on a stopped state.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    try {
      Endpoint result = apiInstance.endpointsStart(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion);
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |

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
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="endpointsStop"></a>
# **endpointsStop**
> Endpoint endpointsStop(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion)



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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    try {
      Endpoint result = apiInstance.endpointsStop(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion);
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |

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
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="endpointsUpdate"></a>
# **endpointsUpdate**
> Endpoint endpointsUpdate(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, endpointUpdateProperties)



Updates an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile. Only tags can be updated after creating an endpoint. To update origins, use the Update Origin operation. To update origin groups, use the Update Origin group operation. To update custom domains, use the Update Custom Domain operation.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    EndpointUpdateParameters endpointUpdateProperties = new EndpointUpdateParameters(); // EndpointUpdateParameters | Endpoint update properties
    try {
      Endpoint result = apiInstance.endpointsUpdate(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, endpointUpdateProperties);
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |
| **endpointUpdateProperties** | [**EndpointUpdateParameters**](EndpointUpdateParameters.md)| Endpoint update properties | |

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
| **200** | OK. The request has succeeded. |  -  |
| **202** | Accepted and the operation will complete asynchronously |  -  |
| **0** | CDN error response describing why the operation failed |  -  |

<a id="endpointsValidateCustomDomain"></a>
# **endpointsValidateCustomDomain**
> ValidateCustomDomainOutput endpointsValidateCustomDomain(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, customDomainProperties)



Validates the custom domain mapping to ensure it maps to the correct CDN endpoint in DNS.

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
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
    String profileName = "profileName_example"; // String | Name of the CDN profile which is unique within the resource group.
    String endpointName = "endpointName_example"; // String | Name of the endpoint under the profile which is unique globally.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-04-02.
    ValidateCustomDomainInput customDomainProperties = new ValidateCustomDomainInput(); // ValidateCustomDomainInput | Custom domain to be validated.
    try {
      ValidateCustomDomainOutput result = apiInstance.endpointsValidateCustomDomain(resourceGroupName, profileName, endpointName, subscriptionId, apiVersion, customDomainProperties);
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
| **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | |
| **profileName** | **String**| Name of the CDN profile which is unique within the resource group. | |
| **endpointName** | **String**| Name of the endpoint under the profile which is unique globally. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-04-02. | |
| **customDomainProperties** | [**ValidateCustomDomainInput**](ValidateCustomDomainInput.md)| Custom domain to be validated. | |

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
| **200** | OK. The request has succeeded. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

