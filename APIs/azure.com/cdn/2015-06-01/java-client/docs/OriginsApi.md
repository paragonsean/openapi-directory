# OriginsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**originsCreate**](OriginsApi.md#originsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/origins/{originName} | Creates a new CDN origin within an endpoint. |
| [**originsDeleteIfExists**](OriginsApi.md#originsDeleteIfExists) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/origins/{originName} | Deletes an existing CDN origin within an endpoint. |
| [**originsGet**](OriginsApi.md#originsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/origins/{originName} | Gets an existing CDN origin within an endpoint. |
| [**originsListByEndpoint**](OriginsApi.md#originsListByEndpoint) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/origins | Lists the existing CDN origins within an endpoint. |
| [**originsUpdate**](OriginsApi.md#originsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/origins/{originName} | Updates an existing CDN origin within an endpoint. |


<a id="originsCreate"></a>
# **originsCreate**
> Origin originsCreate(originName, endpointName, profileName, resourceGroupName, subscriptionId, apiVersion, originProperties)

Creates a new CDN origin within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OriginsApi apiInstance = new OriginsApi(defaultClient);
    String originName = "originName_example"; // String | Name of the origin, an arbitrary value but it needs to be unique under endpoint
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    OriginParameters originProperties = new OriginParameters(); // OriginParameters | Origin properties
    try {
      Origin result = apiInstance.originsCreate(originName, endpointName, profileName, resourceGroupName, subscriptionId, apiVersion, originProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginsApi#originsCreate");
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
| **originName** | **String**| Name of the origin, an arbitrary value but it needs to be unique under endpoint | |
| **endpointName** | **String**| Name of the endpoint within the CDN profile. | |
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |
| **originProperties** | [**OriginParameters**](OriginParameters.md)| Origin properties | |

### Return type

[**Origin**](Origin.md)

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

<a id="originsDeleteIfExists"></a>
# **originsDeleteIfExists**
> Origin originsDeleteIfExists(originName, endpointName, profileName, resourceGroupName, subscriptionId, apiVersion)

Deletes an existing CDN origin within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OriginsApi apiInstance = new OriginsApi(defaultClient);
    String originName = "originName_example"; // String | Name of the origin. Must be unique within endpoint.
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      Origin result = apiInstance.originsDeleteIfExists(originName, endpointName, profileName, resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginsApi#originsDeleteIfExists");
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
| **originName** | **String**| Name of the origin. Must be unique within endpoint. | |
| **endpointName** | **String**| Name of the endpoint within the CDN profile. | |
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |

### Return type

[**Origin**](Origin.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | No Content |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="originsGet"></a>
# **originsGet**
> Origin originsGet(originName, endpointName, profileName, resourceGroupName, subscriptionId, apiVersion)

Gets an existing CDN origin within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OriginsApi apiInstance = new OriginsApi(defaultClient);
    String originName = "originName_example"; // String | Name of the origin, an arbitrary value but it needs to be unique under endpoint
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      Origin result = apiInstance.originsGet(originName, endpointName, profileName, resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginsApi#originsGet");
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
| **originName** | **String**| Name of the origin, an arbitrary value but it needs to be unique under endpoint | |
| **endpointName** | **String**| Name of the endpoint within the CDN profile. | |
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |

### Return type

[**Origin**](Origin.md)

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

<a id="originsListByEndpoint"></a>
# **originsListByEndpoint**
> OriginListResult originsListByEndpoint(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion)

Lists the existing CDN origins within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OriginsApi apiInstance = new OriginsApi(defaultClient);
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      OriginListResult result = apiInstance.originsListByEndpoint(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginsApi#originsListByEndpoint");
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

[**OriginListResult**](OriginListResult.md)

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

<a id="originsUpdate"></a>
# **originsUpdate**
> Origin originsUpdate(originName, endpointName, profileName, resourceGroupName, subscriptionId, apiVersion, originProperties)

Updates an existing CDN origin within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OriginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OriginsApi apiInstance = new OriginsApi(defaultClient);
    String originName = "originName_example"; // String | Name of the origin. Must be unique within endpoint.
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    OriginParameters originProperties = new OriginParameters(); // OriginParameters | Origin properties
    try {
      Origin result = apiInstance.originsUpdate(originName, endpointName, profileName, resourceGroupName, subscriptionId, apiVersion, originProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OriginsApi#originsUpdate");
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
| **originName** | **String**| Name of the origin. Must be unique within endpoint. | |
| **endpointName** | **String**| Name of the endpoint within the CDN profile. | |
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |
| **originProperties** | [**OriginParameters**](OriginParameters.md)| Origin properties | |

### Return type

[**Origin**](Origin.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

