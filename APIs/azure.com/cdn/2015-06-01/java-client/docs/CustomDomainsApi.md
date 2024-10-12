# CustomDomainsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customDomainsCreate**](CustomDomainsApi.md#customDomainsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains/{customDomainName} | Creates a new CDN custom domain within an endpoint. |
| [**customDomainsDeleteIfExists**](CustomDomainsApi.md#customDomainsDeleteIfExists) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains/{customDomainName} | Deletes an existing CDN custom domain within an endpoint. |
| [**customDomainsGet**](CustomDomainsApi.md#customDomainsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains/{customDomainName} | Gets an existing CDN custom domain within an endpoint. |
| [**customDomainsListByEndpoint**](CustomDomainsApi.md#customDomainsListByEndpoint) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains | Lists the existing CDN custom domains within an endpoint. |
| [**customDomainsUpdate**](CustomDomainsApi.md#customDomainsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cdn/profiles/{profileName}/endpoints/{endpointName}/customDomains/{customDomainName} | Updates an existing CDN custom domain within an endpoint. |


<a id="customDomainsCreate"></a>
# **customDomainsCreate**
> CustomDomain customDomainsCreate(customDomainName, endpointName, profileName, resourceGroupName, subscriptionId, apiVersion, customDomainProperties)

Creates a new CDN custom domain within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomDomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomDomainsApi apiInstance = new CustomDomainsApi(defaultClient);
    String customDomainName = "customDomainName_example"; // String | Name of the custom domain within an endpoint.
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    CustomDomainParameters customDomainProperties = new CustomDomainParameters(); // CustomDomainParameters | Custom domain properties required for creation.
    try {
      CustomDomain result = apiInstance.customDomainsCreate(customDomainName, endpointName, profileName, resourceGroupName, subscriptionId, apiVersion, customDomainProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomDomainsApi#customDomainsCreate");
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
| **customDomainName** | **String**| Name of the custom domain within an endpoint. | |
| **endpointName** | **String**| Name of the endpoint within the CDN profile. | |
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |
| **customDomainProperties** | [**CustomDomainParameters**](CustomDomainParameters.md)| Custom domain properties required for creation. | |

### Return type

[**CustomDomain**](CustomDomain.md)

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

<a id="customDomainsDeleteIfExists"></a>
# **customDomainsDeleteIfExists**
> customDomainsDeleteIfExists(customDomainName, endpointName, profileName, resourceGroupName, subscriptionId, apiVersion)

Deletes an existing CDN custom domain within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomDomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomDomainsApi apiInstance = new CustomDomainsApi(defaultClient);
    String customDomainName = "customDomainName_example"; // String | Name of the custom domain within an endpoint.
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      apiInstance.customDomainsDeleteIfExists(customDomainName, endpointName, profileName, resourceGroupName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomDomainsApi#customDomainsDeleteIfExists");
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
| **customDomainName** | **String**| Name of the custom domain within an endpoint. | |
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
| **200** | OK |  -  |
| **202** | Accepted and the operation will complete asynchronously. |  -  |
| **204** | No Content |  -  |
| **0** | CDN error response describing why the operation failed. |  -  |

<a id="customDomainsGet"></a>
# **customDomainsGet**
> CustomDomain customDomainsGet(customDomainName, endpointName, profileName, resourceGroupName, subscriptionId, apiVersion)

Gets an existing CDN custom domain within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomDomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomDomainsApi apiInstance = new CustomDomainsApi(defaultClient);
    String customDomainName = "customDomainName_example"; // String | Name of the custom domain within an endpoint.
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      CustomDomain result = apiInstance.customDomainsGet(customDomainName, endpointName, profileName, resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomDomainsApi#customDomainsGet");
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
| **customDomainName** | **String**| Name of the custom domain within an endpoint. | |
| **endpointName** | **String**| Name of the endpoint within the CDN profile. | |
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |

### Return type

[**CustomDomain**](CustomDomain.md)

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

<a id="customDomainsListByEndpoint"></a>
# **customDomainsListByEndpoint**
> CustomDomainListResult customDomainsListByEndpoint(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion)

Lists the existing CDN custom domains within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomDomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomDomainsApi apiInstance = new CustomDomainsApi(defaultClient);
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    try {
      CustomDomainListResult result = apiInstance.customDomainsListByEndpoint(endpointName, profileName, resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomDomainsApi#customDomainsListByEndpoint");
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

[**CustomDomainListResult**](CustomDomainListResult.md)

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

<a id="customDomainsUpdate"></a>
# **customDomainsUpdate**
> ErrorResponse customDomainsUpdate(customDomainName, endpointName, profileName, resourceGroupName, subscriptionId, apiVersion, customDomainProperties)

Updates an existing CDN custom domain within an endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomDomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomDomainsApi apiInstance = new CustomDomainsApi(defaultClient);
    String customDomainName = "customDomainName_example"; // String | Name of the custom domain within an endpoint.
    String endpointName = "endpointName_example"; // String | Name of the endpoint within the CDN profile.
    String profileName = "profileName_example"; // String | Name of the CDN profile within the resource group.
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group within the Azure subscription.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2015-06-01
    CustomDomainParameters customDomainProperties = new CustomDomainParameters(); // CustomDomainParameters | Custom domain properties to update.
    try {
      ErrorResponse result = apiInstance.customDomainsUpdate(customDomainName, endpointName, profileName, resourceGroupName, subscriptionId, apiVersion, customDomainProperties);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomDomainsApi#customDomainsUpdate");
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
| **customDomainName** | **String**| Name of the custom domain within an endpoint. | |
| **endpointName** | **String**| Name of the endpoint within the CDN profile. | |
| **profileName** | **String**| Name of the CDN profile within the resource group. | |
| **resourceGroupName** | **String**| Name of the resource group within the Azure subscription. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2015-06-01 | |
| **customDomainProperties** | [**CustomDomainParameters**](CustomDomainParameters.md)| Custom domain properties to update. | |

### Return type

[**ErrorResponse**](ErrorResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | CDN error response describing why the operation failed. |  -  |

