# ManagedHostingEnvironmentsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**managedHostingEnvironmentsCreateOrUpdateManagedHostingEnvironment**](ManagedHostingEnvironmentsApi.md#managedHostingEnvironmentsCreateOrUpdateManagedHostingEnvironment) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/managedHostingEnvironments/{name} | Create or update a managed hosting environment. |
| [**managedHostingEnvironmentsDeleteManagedHostingEnvironment**](ManagedHostingEnvironmentsApi.md#managedHostingEnvironmentsDeleteManagedHostingEnvironment) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/managedHostingEnvironments/{name} | Delete a managed hosting environment. |
| [**managedHostingEnvironmentsGetManagedHostingEnvironment**](ManagedHostingEnvironmentsApi.md#managedHostingEnvironmentsGetManagedHostingEnvironment) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/managedHostingEnvironments/{name} | Get properties of a managed hosting environment. |
| [**managedHostingEnvironmentsGetManagedHostingEnvironmentOperation**](ManagedHostingEnvironmentsApi.md#managedHostingEnvironmentsGetManagedHostingEnvironmentOperation) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/managedHostingEnvironments/{name}/operations/{operationId} | Get status of an operation on a managed hosting environment. |
| [**managedHostingEnvironmentsGetManagedHostingEnvironmentServerFarms**](ManagedHostingEnvironmentsApi.md#managedHostingEnvironmentsGetManagedHostingEnvironmentServerFarms) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/managedHostingEnvironments/{name}/serverfarms | Get all serverfarms (App Service Plans) on the managed hosting environment. |
| [**managedHostingEnvironmentsGetManagedHostingEnvironmentSites**](ManagedHostingEnvironmentsApi.md#managedHostingEnvironmentsGetManagedHostingEnvironmentSites) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/managedHostingEnvironments/{name}/sites | Get all sites on the managed hosting environment. |
| [**managedHostingEnvironmentsGetManagedHostingEnvironmentVips**](ManagedHostingEnvironmentsApi.md#managedHostingEnvironmentsGetManagedHostingEnvironmentVips) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/managedHostingEnvironments/{name}/capacities/virtualip | Get list of ip addresses assigned to a managed hosting environment |
| [**managedHostingEnvironmentsGetManagedHostingEnvironmentWebHostingPlans**](ManagedHostingEnvironmentsApi.md#managedHostingEnvironmentsGetManagedHostingEnvironmentWebHostingPlans) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/managedHostingEnvironments/{name}/webhostingplans | Get all serverfarms (App Service Plans) on the managed hosting environment. |
| [**managedHostingEnvironmentsGetManagedHostingEnvironments**](ManagedHostingEnvironmentsApi.md#managedHostingEnvironmentsGetManagedHostingEnvironments) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/managedHostingEnvironments | Get all managed hosting environments in a resource group. |


<a id="managedHostingEnvironmentsCreateOrUpdateManagedHostingEnvironment"></a>
# **managedHostingEnvironmentsCreateOrUpdateManagedHostingEnvironment**
> HostingEnvironment managedHostingEnvironmentsCreateOrUpdateManagedHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, managedHostingEnvironmentEnvelope)

Create or update a managed hosting environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedHostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedHostingEnvironmentsApi apiInstance = new ManagedHostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of managed hosting environment
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    HostingEnvironment managedHostingEnvironmentEnvelope = new HostingEnvironment(); // HostingEnvironment | Properties of managed hosting environment
    try {
      HostingEnvironment result = apiInstance.managedHostingEnvironmentsCreateOrUpdateManagedHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, managedHostingEnvironmentEnvelope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedHostingEnvironmentsApi#managedHostingEnvironmentsCreateOrUpdateManagedHostingEnvironment");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of managed hosting environment | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **managedHostingEnvironmentEnvelope** | [**HostingEnvironment**](HostingEnvironment.md)| Properties of managed hosting environment | |

### Return type

[**HostingEnvironment**](HostingEnvironment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Asynchronous operation in progress |  -  |
| **400** | Bad request |  -  |
| **404** | Not found |  -  |
| **409** | Conflict |  -  |

<a id="managedHostingEnvironmentsDeleteManagedHostingEnvironment"></a>
# **managedHostingEnvironmentsDeleteManagedHostingEnvironment**
> Object managedHostingEnvironmentsDeleteManagedHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, forceDelete)

Delete a managed hosting environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedHostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedHostingEnvironmentsApi apiInstance = new ManagedHostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of managed hosting environment
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    Boolean forceDelete = true; // Boolean | Delete even if the managed hosting environment contains resources
    try {
      Object result = apiInstance.managedHostingEnvironmentsDeleteManagedHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion, forceDelete);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedHostingEnvironmentsApi#managedHostingEnvironmentsDeleteManagedHostingEnvironment");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of managed hosting environment | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **forceDelete** | **Boolean**| Delete even if the managed hosting environment contains resources | [optional] |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Asynchronous operation in progress |  -  |
| **400** | Bad request |  -  |
| **404** | Not found |  -  |
| **409** | Conflict |  -  |

<a id="managedHostingEnvironmentsGetManagedHostingEnvironment"></a>
# **managedHostingEnvironmentsGetManagedHostingEnvironment**
> ManagedHostingEnvironment managedHostingEnvironmentsGetManagedHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion)

Get properties of a managed hosting environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedHostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedHostingEnvironmentsApi apiInstance = new ManagedHostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of managed hosting environment
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ManagedHostingEnvironment result = apiInstance.managedHostingEnvironmentsGetManagedHostingEnvironment(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedHostingEnvironmentsApi#managedHostingEnvironmentsGetManagedHostingEnvironment");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of managed hosting environment | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ManagedHostingEnvironment**](ManagedHostingEnvironment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="managedHostingEnvironmentsGetManagedHostingEnvironmentOperation"></a>
# **managedHostingEnvironmentsGetManagedHostingEnvironmentOperation**
> Object managedHostingEnvironmentsGetManagedHostingEnvironmentOperation(resourceGroupName, name, operationId, subscriptionId, apiVersion)

Get status of an operation on a managed hosting environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedHostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedHostingEnvironmentsApi apiInstance = new ManagedHostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of managed hosting environment
    String operationId = "operationId_example"; // String | operation identifier GUID
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      Object result = apiInstance.managedHostingEnvironmentsGetManagedHostingEnvironmentOperation(resourceGroupName, name, operationId, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedHostingEnvironmentsApi#managedHostingEnvironmentsGetManagedHostingEnvironmentOperation");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of managed hosting environment | |
| **operationId** | **String**| operation identifier GUID | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Operation completed successfully |  -  |
| **202** | Asynchronous operation in progress |  -  |
| **404** | Not found |  -  |
| **500** | Operation failed |  -  |

<a id="managedHostingEnvironmentsGetManagedHostingEnvironmentServerFarms"></a>
# **managedHostingEnvironmentsGetManagedHostingEnvironmentServerFarms**
> ServerFarmCollection managedHostingEnvironmentsGetManagedHostingEnvironmentServerFarms(resourceGroupName, name, subscriptionId, apiVersion)

Get all serverfarms (App Service Plans) on the managed hosting environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedHostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedHostingEnvironmentsApi apiInstance = new ManagedHostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of managed hosting environment
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ServerFarmCollection result = apiInstance.managedHostingEnvironmentsGetManagedHostingEnvironmentServerFarms(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedHostingEnvironmentsApi#managedHostingEnvironmentsGetManagedHostingEnvironmentServerFarms");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of managed hosting environment | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ServerFarmCollection**](ServerFarmCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="managedHostingEnvironmentsGetManagedHostingEnvironmentSites"></a>
# **managedHostingEnvironmentsGetManagedHostingEnvironmentSites**
> SiteCollection managedHostingEnvironmentsGetManagedHostingEnvironmentSites(resourceGroupName, name, subscriptionId, apiVersion, propertiesToInclude)

Get all sites on the managed hosting environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedHostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedHostingEnvironmentsApi apiInstance = new ManagedHostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of managed hosting environment
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    String propertiesToInclude = "propertiesToInclude_example"; // String | Comma separated list of site properties to include
    try {
      SiteCollection result = apiInstance.managedHostingEnvironmentsGetManagedHostingEnvironmentSites(resourceGroupName, name, subscriptionId, apiVersion, propertiesToInclude);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedHostingEnvironmentsApi#managedHostingEnvironmentsGetManagedHostingEnvironmentSites");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of managed hosting environment | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |
| **propertiesToInclude** | **String**| Comma separated list of site properties to include | [optional] |

### Return type

[**SiteCollection**](SiteCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="managedHostingEnvironmentsGetManagedHostingEnvironmentVips"></a>
# **managedHostingEnvironmentsGetManagedHostingEnvironmentVips**
> AddressResponse managedHostingEnvironmentsGetManagedHostingEnvironmentVips(resourceGroupName, name, subscriptionId, apiVersion)

Get list of ip addresses assigned to a managed hosting environment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedHostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedHostingEnvironmentsApi apiInstance = new ManagedHostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of managed hosting environment
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      AddressResponse result = apiInstance.managedHostingEnvironmentsGetManagedHostingEnvironmentVips(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedHostingEnvironmentsApi#managedHostingEnvironmentsGetManagedHostingEnvironmentVips");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of managed hosting environment | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**AddressResponse**](AddressResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="managedHostingEnvironmentsGetManagedHostingEnvironmentWebHostingPlans"></a>
# **managedHostingEnvironmentsGetManagedHostingEnvironmentWebHostingPlans**
> ServerFarmCollection managedHostingEnvironmentsGetManagedHostingEnvironmentWebHostingPlans(resourceGroupName, name, subscriptionId, apiVersion)

Get all serverfarms (App Service Plans) on the managed hosting environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedHostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedHostingEnvironmentsApi apiInstance = new ManagedHostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String name = "name_example"; // String | Name of managed hosting environment
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      ServerFarmCollection result = apiInstance.managedHostingEnvironmentsGetManagedHostingEnvironmentWebHostingPlans(resourceGroupName, name, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedHostingEnvironmentsApi#managedHostingEnvironmentsGetManagedHostingEnvironmentWebHostingPlans");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **name** | **String**| Name of managed hosting environment | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**ServerFarmCollection**](ServerFarmCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="managedHostingEnvironmentsGetManagedHostingEnvironments"></a>
# **managedHostingEnvironmentsGetManagedHostingEnvironments**
> HostingEnvironmentCollection managedHostingEnvironmentsGetManagedHostingEnvironments(resourceGroupName, subscriptionId, apiVersion)

Get all managed hosting environments in a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ManagedHostingEnvironmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ManagedHostingEnvironmentsApi apiInstance = new ManagedHostingEnvironmentsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of resource group
    String subscriptionId = "subscriptionId_example"; // String | Subscription Id
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      HostingEnvironmentCollection result = apiInstance.managedHostingEnvironmentsGetManagedHostingEnvironments(resourceGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ManagedHostingEnvironmentsApi#managedHostingEnvironmentsGetManagedHostingEnvironments");
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
| **resourceGroupName** | **String**| Name of resource group | |
| **subscriptionId** | **String**| Subscription Id | |
| **apiVersion** | **String**| API Version | |

### Return type

[**HostingEnvironmentCollection**](HostingEnvironmentCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

