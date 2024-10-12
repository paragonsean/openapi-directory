# ClusterVersionApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clusterVersionsGet**](ClusterVersionApi.md#clusterVersionsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/clusterVersions/{clusterVersion} | Gets information about a Service Fabric cluster code version available in the specified location. |
| [**clusterVersionsGetByEnvironment**](ClusterVersionApi.md#clusterVersionsGetByEnvironment) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/environments/{environment}/clusterVersions/{clusterVersion} | Gets information about a Service Fabric cluster code version available for the specified environment. |
| [**clusterVersionsList**](ClusterVersionApi.md#clusterVersionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/clusterVersions | Gets the list of Service Fabric cluster code versions available for the specified location. |
| [**clusterVersionsListByEnvironment**](ClusterVersionApi.md#clusterVersionsListByEnvironment) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/environments/{environment}/clusterVersions | Gets the list of Service Fabric cluster code versions available for the specified environment. |


<a id="clusterVersionsGet"></a>
# **clusterVersionsGet**
> ClusterCodeVersionsListResult clusterVersionsGet(location, apiVersion, subscriptionId, clusterVersion)

Gets information about a Service Fabric cluster code version available in the specified location.

Gets information about an available Service Fabric cluster code version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterVersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ClusterVersionApi apiInstance = new ClusterVersionApi(defaultClient);
    String location = "location_example"; // String | The location for the cluster code versions. This is different from cluster location.
    String apiVersion = "2019-03-01"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String clusterVersion = "clusterVersion_example"; // String | The cluster code version.
    try {
      ClusterCodeVersionsListResult result = apiInstance.clusterVersionsGet(location, apiVersion, subscriptionId, clusterVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterVersionApi#clusterVersionsGet");
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
| **location** | **String**| The location for the cluster code versions. This is different from cluster location. | |
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to 2019-03-01] [enum: 2019-03-01] |
| **subscriptionId** | **String**| The customer subscription identifier. | |
| **clusterVersion** | **String**| The cluster code version. | |

### Return type

[**ClusterCodeVersionsListResult**](ClusterCodeVersionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation completed successfully. |  -  |

<a id="clusterVersionsGetByEnvironment"></a>
# **clusterVersionsGetByEnvironment**
> ClusterCodeVersionsListResult clusterVersionsGetByEnvironment(location, environment, apiVersion, subscriptionId, clusterVersion)

Gets information about a Service Fabric cluster code version available for the specified environment.

Gets information about an available Service Fabric cluster code version by environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterVersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ClusterVersionApi apiInstance = new ClusterVersionApi(defaultClient);
    String location = "location_example"; // String | The location for the cluster code versions. This is different from cluster location.
    String environment = "Windows"; // String | The operating system of the cluster. The default means all.
    String apiVersion = "2019-03-01"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    String clusterVersion = "clusterVersion_example"; // String | The cluster code version.
    try {
      ClusterCodeVersionsListResult result = apiInstance.clusterVersionsGetByEnvironment(location, environment, apiVersion, subscriptionId, clusterVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterVersionApi#clusterVersionsGetByEnvironment");
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
| **location** | **String**| The location for the cluster code versions. This is different from cluster location. | |
| **environment** | **String**| The operating system of the cluster. The default means all. | [enum: Windows, Linux] |
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to 2019-03-01] [enum: 2019-03-01] |
| **subscriptionId** | **String**| The customer subscription identifier. | |
| **clusterVersion** | **String**| The cluster code version. | |

### Return type

[**ClusterCodeVersionsListResult**](ClusterCodeVersionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation completed successfully. |  -  |

<a id="clusterVersionsList"></a>
# **clusterVersionsList**
> ClusterCodeVersionsListResult clusterVersionsList(location, apiVersion, subscriptionId)

Gets the list of Service Fabric cluster code versions available for the specified location.

Gets all available code versions for Service Fabric cluster resources by location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterVersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ClusterVersionApi apiInstance = new ClusterVersionApi(defaultClient);
    String location = "location_example"; // String | The location for the cluster code versions. This is different from cluster location.
    String apiVersion = "2019-03-01"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    try {
      ClusterCodeVersionsListResult result = apiInstance.clusterVersionsList(location, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterVersionApi#clusterVersionsList");
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
| **location** | **String**| The location for the cluster code versions. This is different from cluster location. | |
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to 2019-03-01] [enum: 2019-03-01] |
| **subscriptionId** | **String**| The customer subscription identifier. | |

### Return type

[**ClusterCodeVersionsListResult**](ClusterCodeVersionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation completed successfully. |  -  |

<a id="clusterVersionsListByEnvironment"></a>
# **clusterVersionsListByEnvironment**
> ClusterCodeVersionsListResult clusterVersionsListByEnvironment(location, environment, apiVersion, subscriptionId)

Gets the list of Service Fabric cluster code versions available for the specified environment.

Gets all available code versions for Service Fabric cluster resources by environment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterVersionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ClusterVersionApi apiInstance = new ClusterVersionApi(defaultClient);
    String location = "location_example"; // String | The location for the cluster code versions. This is different from cluster location.
    String environment = "Windows"; // String | The operating system of the cluster. The default means all.
    String apiVersion = "2019-03-01"; // String | The version of the Service Fabric resource provider API. This is a required parameter and it's value must be \"2019-03-01\" for this specification.
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier.
    try {
      ClusterCodeVersionsListResult result = apiInstance.clusterVersionsListByEnvironment(location, environment, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterVersionApi#clusterVersionsListByEnvironment");
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
| **location** | **String**| The location for the cluster code versions. This is different from cluster location. | |
| **environment** | **String**| The operating system of the cluster. The default means all. | [enum: Windows, Linux] |
| **apiVersion** | **String**| The version of the Service Fabric resource provider API. This is a required parameter and it&#39;s value must be \&quot;2019-03-01\&quot; for this specification. | [default to 2019-03-01] [enum: 2019-03-01] |
| **subscriptionId** | **String**| The customer subscription identifier. | |

### Return type

[**ClusterCodeVersionsListResult**](ClusterCodeVersionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The operation completed successfully. |  -  |

