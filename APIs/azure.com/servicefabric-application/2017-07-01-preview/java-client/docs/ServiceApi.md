# ServiceApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**servicesCreate**](ServiceApi.md#servicesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName}/services/{serviceName} | Creates or updates a Service Fabric service resource. |
| [**servicesDelete**](ServiceApi.md#servicesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName}/services/{serviceName} | Deletes a Service Fabric service resource. |
| [**servicesGet**](ServiceApi.md#servicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName}/services/{serviceName} | Gets a Service Fabric service resource. |
| [**servicesList**](ServiceApi.md#servicesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName}/services | Gets the list of service resources created in the specified Service Fabric application resource. |
| [**servicesUpdate**](ServiceApi.md#servicesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName}/services/{serviceName} | Updates a Service Fabric service resource. |


<a id="servicesCreate"></a>
# **servicesCreate**
> ServiceResource servicesCreate(subscriptionId, resourceGroupName, clusterName, applicationName, serviceName, apiVersion, parameters)

Creates or updates a Service Fabric service resource.

Create or update a Service Fabric service resource with the specified name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceApi apiInstance = new ServiceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster resource.
    String applicationName = "applicationName_example"; // String | The name of the application resource.
    String serviceName = "serviceName_example"; // String | The name of the service resource in the format of {applicationName}~{serviceName}.
    String apiVersion = "2017-07-01-preview"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2017-07-01-preview\" for this specification.
    ServiceResource parameters = new ServiceResource(); // ServiceResource | The service resource.
    try {
      ServiceResource result = apiInstance.servicesCreate(subscriptionId, resourceGroupName, clusterName, applicationName, serviceName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceApi#servicesCreate");
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
| **subscriptionId** | **String**| The customer subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **clusterName** | **String**| The name of the cluster resource. | |
| **applicationName** | **String**| The name of the application resource. | |
| **serviceName** | **String**| The name of the service resource in the format of {applicationName}~{serviceName}. | |
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2017-07-01-preview\&quot; for this specification. | [default to 2017-07-01-preview] [enum: 2017-07-01-preview] |
| **parameters** | [**ServiceResource**](ServiceResource.md)| The service resource. | |

### Return type

[**ServiceResource**](ServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The request was accepted and the operation will complete asynchronously. |  -  |
| **0** | The detailed error response. |  -  |

<a id="servicesDelete"></a>
# **servicesDelete**
> servicesDelete(subscriptionId, resourceGroupName, clusterName, applicationName, serviceName, apiVersion)

Deletes a Service Fabric service resource.

Delete a Service Fabric service resource with the specified name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceApi apiInstance = new ServiceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster resource.
    String applicationName = "applicationName_example"; // String | The name of the application resource.
    String serviceName = "serviceName_example"; // String | The name of the service resource in the format of {applicationName}~{serviceName}.
    String apiVersion = "2017-07-01-preview"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2017-07-01-preview\" for this specification.
    try {
      apiInstance.servicesDelete(subscriptionId, resourceGroupName, clusterName, applicationName, serviceName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceApi#servicesDelete");
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
| **subscriptionId** | **String**| The customer subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **clusterName** | **String**| The name of the cluster resource. | |
| **applicationName** | **String**| The name of the application resource. | |
| **serviceName** | **String**| The name of the service resource in the format of {applicationName}~{serviceName}. | |
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2017-07-01-preview\&quot; for this specification. | [default to 2017-07-01-preview] [enum: 2017-07-01-preview] |

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
| **202** | The request was accepted and the operation will complete asynchronously. |  -  |
| **204** | The resource was not found. |  -  |
| **0** | The detailed error response. |  -  |

<a id="servicesGet"></a>
# **servicesGet**
> ServiceResource servicesGet(subscriptionId, resourceGroupName, clusterName, applicationName, serviceName, apiVersion)

Gets a Service Fabric service resource.

Get a Service Fabric service resource created or in the process of being created in the Service Fabric application resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceApi apiInstance = new ServiceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster resource.
    String applicationName = "applicationName_example"; // String | The name of the application resource.
    String serviceName = "serviceName_example"; // String | The name of the service resource in the format of {applicationName}~{serviceName}.
    String apiVersion = "2017-07-01-preview"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2017-07-01-preview\" for this specification.
    try {
      ServiceResource result = apiInstance.servicesGet(subscriptionId, resourceGroupName, clusterName, applicationName, serviceName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceApi#servicesGet");
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
| **subscriptionId** | **String**| The customer subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **clusterName** | **String**| The name of the cluster resource. | |
| **applicationName** | **String**| The name of the application resource. | |
| **serviceName** | **String**| The name of the service resource in the format of {applicationName}~{serviceName}. | |
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2017-07-01-preview\&quot; for this specification. | [default to 2017-07-01-preview] [enum: 2017-07-01-preview] |

### Return type

[**ServiceResource**](ServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation completed successfully. |  -  |
| **0** | The detailed error response. |  -  |

<a id="servicesList"></a>
# **servicesList**
> ServiceResourceList servicesList(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion)

Gets the list of service resources created in the specified Service Fabric application resource.

Gets all service resources created or in the process of being created in the Service Fabric application resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceApi apiInstance = new ServiceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster resource.
    String applicationName = "applicationName_example"; // String | The name of the application resource.
    String apiVersion = "2017-07-01-preview"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2017-07-01-preview\" for this specification.
    try {
      ServiceResourceList result = apiInstance.servicesList(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceApi#servicesList");
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
| **subscriptionId** | **String**| The customer subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **clusterName** | **String**| The name of the cluster resource. | |
| **applicationName** | **String**| The name of the application resource. | |
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2017-07-01-preview\&quot; for this specification. | [default to 2017-07-01-preview] [enum: 2017-07-01-preview] |

### Return type

[**ServiceResourceList**](ServiceResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation completed successfully. |  -  |
| **0** | The detailed error response. |  -  |

<a id="servicesUpdate"></a>
# **servicesUpdate**
> ServiceResource servicesUpdate(subscriptionId, resourceGroupName, clusterName, applicationName, serviceName, apiVersion, parameters)

Updates a Service Fabric service resource.

Update a Service Fabric service resource with the specified name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ServiceApi apiInstance = new ServiceApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster resource.
    String applicationName = "applicationName_example"; // String | The name of the application resource.
    String serviceName = "serviceName_example"; // String | The name of the service resource in the format of {applicationName}~{serviceName}.
    String apiVersion = "2017-07-01-preview"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2017-07-01-preview\" for this specification.
    ServiceResourceUpdate parameters = new ServiceResourceUpdate(); // ServiceResourceUpdate | The service resource for patch operations.
    try {
      ServiceResource result = apiInstance.servicesUpdate(subscriptionId, resourceGroupName, clusterName, applicationName, serviceName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceApi#servicesUpdate");
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
| **subscriptionId** | **String**| The customer subscription identifier. | |
| **resourceGroupName** | **String**| The name of the resource group. | |
| **clusterName** | **String**| The name of the cluster resource. | |
| **applicationName** | **String**| The name of the application resource. | |
| **serviceName** | **String**| The name of the service resource in the format of {applicationName}~{serviceName}. | |
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2017-07-01-preview\&quot; for this specification. | [default to 2017-07-01-preview] [enum: 2017-07-01-preview] |
| **parameters** | [**ServiceResourceUpdate**](ServiceResourceUpdate.md)| The service resource for patch operations. | |

### Return type

[**ServiceResource**](ServiceResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The request was accepted and the operation will complete asynchronously. |  -  |
| **0** | The detailed error response. |  -  |

