# ApplicationTypeApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applicationTypesCreate**](ApplicationTypeApi.md#applicationTypesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applicationTypes/{applicationTypeName} | Creates or updates a Service Fabric application type name resource. |
| [**applicationTypesDelete**](ApplicationTypeApi.md#applicationTypesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applicationTypes/{applicationTypeName} | Deletes a Service Fabric application type name resource. |
| [**applicationTypesGet**](ApplicationTypeApi.md#applicationTypesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applicationTypes/{applicationTypeName} | Gets a Service Fabric application type name resource. |
| [**applicationTypesList**](ApplicationTypeApi.md#applicationTypesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applicationTypes | Gets the list of application type name resources created in the specified Service Fabric cluster resource. |


<a id="applicationTypesCreate"></a>
# **applicationTypesCreate**
> ApplicationTypeResource applicationTypesCreate(subscriptionId, resourceGroupName, clusterName, applicationTypeName, apiVersion, parameters)

Creates or updates a Service Fabric application type name resource.

Create or update a Service Fabric application type name resource with the specified name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationTypeApi apiInstance = new ApplicationTypeApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster resource.
    String applicationTypeName = "applicationTypeName_example"; // String | The name of the application type name resource.
    String apiVersion = "2019-06-01-preview"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-06-01-preview\" for this specification.
    ApplicationTypeResource parameters = new ApplicationTypeResource(); // ApplicationTypeResource | The application type name resource.
    try {
      ApplicationTypeResource result = apiInstance.applicationTypesCreate(subscriptionId, resourceGroupName, clusterName, applicationTypeName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationTypeApi#applicationTypesCreate");
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
| **applicationTypeName** | **String**| The name of the application type name resource. | |
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-06-01-preview\&quot; for this specification. | [default to 2019-06-01-preview] [enum: 2019-06-01-preview] |
| **parameters** | [**ApplicationTypeResource**](ApplicationTypeResource.md)| The application type name resource. | |

### Return type

[**ApplicationTypeResource**](ApplicationTypeResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation completed successfully. |  -  |
| **0** | The detailed error response. |  -  |

<a id="applicationTypesDelete"></a>
# **applicationTypesDelete**
> applicationTypesDelete(subscriptionId, resourceGroupName, clusterName, applicationTypeName, apiVersion)

Deletes a Service Fabric application type name resource.

Delete a Service Fabric application type name resource with the specified name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationTypeApi apiInstance = new ApplicationTypeApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster resource.
    String applicationTypeName = "applicationTypeName_example"; // String | The name of the application type name resource.
    String apiVersion = "2019-06-01-preview"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-06-01-preview\" for this specification.
    try {
      apiInstance.applicationTypesDelete(subscriptionId, resourceGroupName, clusterName, applicationTypeName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationTypeApi#applicationTypesDelete");
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
| **applicationTypeName** | **String**| The name of the application type name resource. | |
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-06-01-preview\&quot; for this specification. | [default to 2019-06-01-preview] [enum: 2019-06-01-preview] |

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

<a id="applicationTypesGet"></a>
# **applicationTypesGet**
> ApplicationTypeResource applicationTypesGet(subscriptionId, resourceGroupName, clusterName, applicationTypeName, apiVersion)

Gets a Service Fabric application type name resource.

Get a Service Fabric application type name resource created or in the process of being created in the Service Fabric cluster resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationTypeApi apiInstance = new ApplicationTypeApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster resource.
    String applicationTypeName = "applicationTypeName_example"; // String | The name of the application type name resource.
    String apiVersion = "2019-06-01-preview"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-06-01-preview\" for this specification.
    try {
      ApplicationTypeResource result = apiInstance.applicationTypesGet(subscriptionId, resourceGroupName, clusterName, applicationTypeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationTypeApi#applicationTypesGet");
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
| **applicationTypeName** | **String**| The name of the application type name resource. | |
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-06-01-preview\&quot; for this specification. | [default to 2019-06-01-preview] [enum: 2019-06-01-preview] |

### Return type

[**ApplicationTypeResource**](ApplicationTypeResource.md)

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

<a id="applicationTypesList"></a>
# **applicationTypesList**
> ApplicationTypeResourceList applicationTypesList(subscriptionId, resourceGroupName, clusterName, apiVersion)

Gets the list of application type name resources created in the specified Service Fabric cluster resource.

Gets all application type name resources created or in the process of being created in the Service Fabric cluster resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationTypeApi apiInstance = new ApplicationTypeApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster resource.
    String apiVersion = "2019-06-01-preview"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-06-01-preview\" for this specification.
    try {
      ApplicationTypeResourceList result = apiInstance.applicationTypesList(subscriptionId, resourceGroupName, clusterName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationTypeApi#applicationTypesList");
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
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-06-01-preview\&quot; for this specification. | [default to 2019-06-01-preview] [enum: 2019-06-01-preview] |

### Return type

[**ApplicationTypeResourceList**](ApplicationTypeResourceList.md)

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

