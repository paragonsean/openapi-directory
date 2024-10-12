# ApplicationTypeVersionApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applicationTypeVersionsCreateOrUpdate**](ApplicationTypeVersionApi.md#applicationTypeVersionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applicationTypes/{applicationTypeName}/versions/{version} | Creates or updates a Service Fabric application type version resource. |
| [**applicationTypeVersionsDelete**](ApplicationTypeVersionApi.md#applicationTypeVersionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applicationTypes/{applicationTypeName}/versions/{version} | Deletes a Service Fabric application type version resource. |
| [**applicationTypeVersionsGet**](ApplicationTypeVersionApi.md#applicationTypeVersionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applicationTypes/{applicationTypeName}/versions/{version} | Gets a Service Fabric application type version resource. |
| [**applicationTypeVersionsList**](ApplicationTypeVersionApi.md#applicationTypeVersionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName}/applicationTypes/{applicationTypeName}/versions | Gets the list of application type version resources created in the specified Service Fabric application type name resource. |


<a id="applicationTypeVersionsCreateOrUpdate"></a>
# **applicationTypeVersionsCreateOrUpdate**
> ApplicationTypeVersionResource applicationTypeVersionsCreateOrUpdate(subscriptionId, resourceGroupName, clusterName, applicationTypeName, version, apiVersion, parameters)

Creates or updates a Service Fabric application type version resource.

Create or update a Service Fabric application type version resource with the specified name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationTypeVersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationTypeVersionApi apiInstance = new ApplicationTypeVersionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster resource.
    String applicationTypeName = "applicationTypeName_example"; // String | The name of the application type name resource.
    String version = "version_example"; // String | The application type version.
    String apiVersion = "2019-03-01"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
    ApplicationTypeVersionResource parameters = new ApplicationTypeVersionResource(); // ApplicationTypeVersionResource | The application type version resource.
    try {
      ApplicationTypeVersionResource result = apiInstance.applicationTypeVersionsCreateOrUpdate(subscriptionId, resourceGroupName, clusterName, applicationTypeName, version, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationTypeVersionApi#applicationTypeVersionsCreateOrUpdate");
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
| **version** | **String**| The application type version. | |
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to 2019-03-01] [enum: 2019-03-01] |
| **parameters** | [**ApplicationTypeVersionResource**](ApplicationTypeVersionResource.md)| The application type version resource. | |

### Return type

[**ApplicationTypeVersionResource**](ApplicationTypeVersionResource.md)

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

<a id="applicationTypeVersionsDelete"></a>
# **applicationTypeVersionsDelete**
> applicationTypeVersionsDelete(subscriptionId, resourceGroupName, clusterName, applicationTypeName, version, apiVersion)

Deletes a Service Fabric application type version resource.

Delete a Service Fabric application type version resource with the specified name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationTypeVersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationTypeVersionApi apiInstance = new ApplicationTypeVersionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster resource.
    String applicationTypeName = "applicationTypeName_example"; // String | The name of the application type name resource.
    String version = "version_example"; // String | The application type version.
    String apiVersion = "2019-03-01"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
    try {
      apiInstance.applicationTypeVersionsDelete(subscriptionId, resourceGroupName, clusterName, applicationTypeName, version, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationTypeVersionApi#applicationTypeVersionsDelete");
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
| **version** | **String**| The application type version. | |
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to 2019-03-01] [enum: 2019-03-01] |

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

<a id="applicationTypeVersionsGet"></a>
# **applicationTypeVersionsGet**
> ApplicationTypeVersionResource applicationTypeVersionsGet(subscriptionId, resourceGroupName, clusterName, applicationTypeName, version, apiVersion)

Gets a Service Fabric application type version resource.

Get a Service Fabric application type version resource created or in the process of being created in the Service Fabric application type name resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationTypeVersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationTypeVersionApi apiInstance = new ApplicationTypeVersionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster resource.
    String applicationTypeName = "applicationTypeName_example"; // String | The name of the application type name resource.
    String version = "version_example"; // String | The application type version.
    String apiVersion = "2019-03-01"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
    try {
      ApplicationTypeVersionResource result = apiInstance.applicationTypeVersionsGet(subscriptionId, resourceGroupName, clusterName, applicationTypeName, version, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationTypeVersionApi#applicationTypeVersionsGet");
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
| **version** | **String**| The application type version. | |
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to 2019-03-01] [enum: 2019-03-01] |

### Return type

[**ApplicationTypeVersionResource**](ApplicationTypeVersionResource.md)

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

<a id="applicationTypeVersionsList"></a>
# **applicationTypeVersionsList**
> ApplicationTypeVersionResourceList applicationTypeVersionsList(subscriptionId, resourceGroupName, clusterName, applicationTypeName, apiVersion)

Gets the list of application type version resources created in the specified Service Fabric application type name resource.

Gets all application type version resources created or in the process of being created in the Service Fabric application type name resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationTypeVersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ApplicationTypeVersionApi apiInstance = new ApplicationTypeVersionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String clusterName = "clusterName_example"; // String | The name of the cluster resource.
    String applicationTypeName = "applicationTypeName_example"; // String | The name of the application type name resource.
    String apiVersion = "2019-03-01"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
    try {
      ApplicationTypeVersionResourceList result = apiInstance.applicationTypeVersionsList(subscriptionId, resourceGroupName, clusterName, applicationTypeName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationTypeVersionApi#applicationTypeVersionsList");
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
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to 2019-03-01] [enum: 2019-03-01] |

### Return type

[**ApplicationTypeVersionResourceList**](ApplicationTypeVersionResourceList.md)

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

