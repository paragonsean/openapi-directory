# ClusterVersionApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clusterVersionsGet**](ClusterVersionApi.md#clusterVersionsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/environments/{environment}/clusterVersions/{clusterVersion} |  |
| [**clusterVersionsList**](ClusterVersionApi.md#clusterVersionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/clusterVersions |  |
| [**clusterVersionsListByEnvironment**](ClusterVersionApi.md#clusterVersionsListByEnvironment) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceFabric/locations/{location}/environments/{environment}/clusterVersions |  |


<a id="clusterVersionsGet"></a>
# **clusterVersionsGet**
> ClusterCodeVersionsResult clusterVersionsGet(location, environment, apiVersion, subscriptionId, clusterVersion)



Get cluster code versions by environment and version

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
    String location = "location_example"; // String | The location for the cluster code versions, this is different from cluster location
    String environment = "Windows"; // String | Cluster operating system, the default means all
    String apiVersion = "apiVersion_example"; // String | The version of the ServiceFabric resource provider api
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
    String clusterVersion = "clusterVersion_example"; // String | The cluster code version
    try {
      ClusterCodeVersionsResult result = apiInstance.clusterVersionsGet(location, environment, apiVersion, subscriptionId, clusterVersion);
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
| **location** | **String**| The location for the cluster code versions, this is different from cluster location | |
| **environment** | **String**| Cluster operating system, the default means all | [enum: Windows, Linux] |
| **apiVersion** | **String**| The version of the ServiceFabric resource provider api | |
| **subscriptionId** | **String**| The customer subscription identifier | |
| **clusterVersion** | **String**| The cluster code version | |

### Return type

[**ClusterCodeVersionsResult**](ClusterCodeVersionsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - Get cluster code versions successfully |  -  |

<a id="clusterVersionsList"></a>
# **clusterVersionsList**
> ClusterCodeVersionsListResult clusterVersionsList(location, apiVersion, subscriptionId)



List cluster code versions by location

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
    String location = "location_example"; // String | The location for the cluster code versions, this is different from cluster location
    String apiVersion = "apiVersion_example"; // String | The version of the ServiceFabric resource provider api
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
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
| **location** | **String**| The location for the cluster code versions, this is different from cluster location | |
| **apiVersion** | **String**| The version of the ServiceFabric resource provider api | |
| **subscriptionId** | **String**| The customer subscription identifier | |

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
| **200** | OK - List cluster code versions successfully |  -  |

<a id="clusterVersionsListByEnvironment"></a>
# **clusterVersionsListByEnvironment**
> ClusterCodeVersionsListResult clusterVersionsListByEnvironment(location, environment, apiVersion, subscriptionId)



List cluster code versions by environment

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
    String location = "location_example"; // String | The location for the cluster code versions, this is different from cluster location
    String environment = "Windows"; // String | Cluster operating system, the default means all
    String apiVersion = "apiVersion_example"; // String | The version of the ServiceFabric resource provider api
    String subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
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
| **location** | **String**| The location for the cluster code versions, this is different from cluster location | |
| **environment** | **String**| Cluster operating system, the default means all | [enum: Windows, Linux] |
| **apiVersion** | **String**| The version of the ServiceFabric resource provider api | |
| **subscriptionId** | **String**| The customer subscription identifier | |

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
| **200** | OK - List cluster code versions successfully |  -  |

