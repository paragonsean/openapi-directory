# ApplicationApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applicationsCreate**](ApplicationApi.md#applicationsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName} | Creates or updates a Service Fabric application resource. |
| [**applicationsDelete**](ApplicationApi.md#applicationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName} | Deletes a Service Fabric application resource. |
| [**applicationsGet**](ApplicationApi.md#applicationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName} | Gets a Service Fabric application resource. |
| [**applicationsList**](ApplicationApi.md#applicationsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications | Gets the list of application resources created in the specified Service Fabric cluster resource. |
| [**applicationsUpdate**](ApplicationApi.md#applicationsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applications/{applicationName} | Updates a Service Fabric application resource. |


<a id="applicationsCreate"></a>
# **applicationsCreate**
> ApplicationResource applicationsCreate(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion, parameters)

Creates or updates a Service Fabric application resource.

Create or update a Service Fabric application resource with the specified name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster resource.
    String applicationName = "applicationName_example"; // String | The name of the application resource.
    String apiVersion = "2019-03-01-preview"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01-preview\" for this specification.
    ApplicationResource parameters = new ApplicationResource(); // ApplicationResource | The application resource.
    try {
      ApplicationResource result = apiInstance.applicationsCreate(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationsCreate");
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
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01-preview\&quot; for this specification. | [default to 2019-03-01-preview] [enum: 2019-03-01-preview] |
| **parameters** | [**ApplicationResource**](ApplicationResource.md)| The application resource. | |

### Return type

[**ApplicationResource**](ApplicationResource.md)

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

<a id="applicationsDelete"></a>
# **applicationsDelete**
> applicationsDelete(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion)

Deletes a Service Fabric application resource.

Delete a Service Fabric application resource with the specified name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster resource.
    String applicationName = "applicationName_example"; // String | The name of the application resource.
    String apiVersion = "2019-03-01-preview"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01-preview\" for this specification.
    try {
      apiInstance.applicationsDelete(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationsDelete");
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
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01-preview\&quot; for this specification. | [default to 2019-03-01-preview] [enum: 2019-03-01-preview] |

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

<a id="applicationsGet"></a>
# **applicationsGet**
> ApplicationResource applicationsGet(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion)

Gets a Service Fabric application resource.

Get a Service Fabric application resource created or in the process of being created in the Service Fabric cluster resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster resource.
    String applicationName = "applicationName_example"; // String | The name of the application resource.
    String apiVersion = "2019-03-01-preview"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01-preview\" for this specification.
    try {
      ApplicationResource result = apiInstance.applicationsGet(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationsGet");
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
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01-preview\&quot; for this specification. | [default to 2019-03-01-preview] [enum: 2019-03-01-preview] |

### Return type

[**ApplicationResource**](ApplicationResource.md)

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

<a id="applicationsList"></a>
# **applicationsList**
> ApplicationResourceList applicationsList(subscriptionId, resourceGroupName, clusterName, apiVersion)

Gets the list of application resources created in the specified Service Fabric cluster resource.

Gets all application resources created or in the process of being created in the Service Fabric cluster resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster resource.
    String apiVersion = "2019-03-01-preview"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01-preview\" for this specification.
    try {
      ApplicationResourceList result = apiInstance.applicationsList(subscriptionId, resourceGroupName, clusterName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationsList");
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
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01-preview\&quot; for this specification. | [default to 2019-03-01-preview] [enum: 2019-03-01-preview] |

### Return type

[**ApplicationResourceList**](ApplicationResourceList.md)

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

<a id="applicationsUpdate"></a>
# **applicationsUpdate**
> ApplicationResource applicationsUpdate(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion, parameters)

Updates a Service Fabric application resource.

Update a Service Fabric application resource with the specified name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster resource.
    String applicationName = "applicationName_example"; // String | The name of the application resource.
    String apiVersion = "2019-03-01-preview"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01-preview\" for this specification.
    ApplicationResourceUpdate parameters = new ApplicationResourceUpdate(); // ApplicationResourceUpdate | The application resource for patch operations.
    try {
      ApplicationResource result = apiInstance.applicationsUpdate(subscriptionId, resourceGroupName, clusterName, applicationName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationsUpdate");
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
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01-preview\&quot; for this specification. | [default to 2019-03-01-preview] [enum: 2019-03-01-preview] |
| **parameters** | [**ApplicationResourceUpdate**](ApplicationResourceUpdate.md)| The application resource for patch operations. | |

### Return type

[**ApplicationResource**](ApplicationResource.md)

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

