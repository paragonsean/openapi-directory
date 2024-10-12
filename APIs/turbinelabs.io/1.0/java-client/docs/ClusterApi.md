# ClusterApi

All URIs are relative to *https://api.turbinelabs.io/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clusterClusterKeyDelete**](ClusterApi.md#clusterClusterKeyDelete) | **DELETE** /cluster/{clusterKey} | delete cluster |
| [**clusterClusterKeyGet**](ClusterApi.md#clusterClusterKeyGet) | **GET** /cluster/{clusterKey} | get cluster |
| [**clusterClusterKeyInstancesInstanceIdentifierDelete**](ClusterApi.md#clusterClusterKeyInstancesInstanceIdentifierDelete) | **DELETE** /cluster/{clusterKey}/instances/{instanceIdentifier} | remove instance |
| [**clusterClusterKeyInstancesPost**](ClusterApi.md#clusterClusterKeyInstancesPost) | **POST** /cluster/{clusterKey}/instances | add instance |
| [**clusterClusterKeyPut**](ClusterApi.md#clusterClusterKeyPut) | **PUT** /cluster/{clusterKey} | modify cluster |
| [**clusterGet**](ClusterApi.md#clusterGet) | **GET** /cluster | get clusters |
| [**clusterPost**](ClusterApi.md#clusterPost) | **POST** /cluster | create cluster |


<a id="clusterClusterKeyDelete"></a>
# **clusterClusterKeyDelete**
> Object clusterClusterKeyDelete(clusterKey, checksum)

delete cluster

Delete an existing cluster

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String clusterKey = "7ef80556-60bb-46bd-4cec-f4e2533aa75c"; // String | the cluster key
    String checksum = "9cd24183-f848-48f8-6f55-0f07240700b9"; // String | the current checksum of the cluster to be deleted
    try {
      Object result = apiInstance.clusterClusterKeyDelete(clusterKey, checksum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#clusterClusterKeyDelete");
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
| **clusterKey** | **String**| the cluster key | |
| **checksum** | **String**| the current checksum of the cluster to be deleted | |

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | an empty result |  -  |
| **0** | Unexpected error |  -  |

<a id="clusterClusterKeyGet"></a>
# **clusterClusterKeyGet**
> ClusterResult clusterClusterKeyGet(clusterKey)

get cluster

Get details for an existing cluster

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String clusterKey = "7ef80556-60bb-46bd-4cec-f4e2533aa75c"; // String | the cluster key
    try {
      ClusterResult result = apiInstance.clusterClusterKeyGet(clusterKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#clusterClusterKeyGet");
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
| **clusterKey** | **String**| the cluster key | |

### Return type

[**ClusterResult**](ClusterResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a result containing a single cluster |  -  |
| **0** | Unexpected error |  -  |

<a id="clusterClusterKeyInstancesInstanceIdentifierDelete"></a>
# **clusterClusterKeyInstancesInstanceIdentifierDelete**
> Object clusterClusterKeyInstancesInstanceIdentifierDelete(checksum, clusterKey, instanceIdentifier)

remove instance

Remove an instance from a cluster

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String checksum = "9cd24183-f848-48f8-6f55-0f07240700b9"; // String | the current checksum of the instance to be deleted
    String clusterKey = "7ef80556-60bb-46bd-4cec-f4e2533aa75c"; // String | the cluster to remove an instance from
    String instanceIdentifier = "foo-1.useast.test.com:8080"; // String | the instance to remove, identified as <host>:<port>
    try {
      Object result = apiInstance.clusterClusterKeyInstancesInstanceIdentifierDelete(checksum, clusterKey, instanceIdentifier);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#clusterClusterKeyInstancesInstanceIdentifierDelete");
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
| **checksum** | **String**| the current checksum of the instance to be deleted | |
| **clusterKey** | **String**| the cluster to remove an instance from | |
| **instanceIdentifier** | **String**| the instance to remove, identified as &lt;host&gt;:&lt;port&gt; | |

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | an empty result |  -  |
| **0** | Unexpected error |  -  |

<a id="clusterClusterKeyInstancesPost"></a>
# **clusterClusterKeyInstancesPost**
> InstanceResult clusterClusterKeyInstancesPost(clusterKey, instance)

add instance

Add a new instance to a cluster

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String clusterKey = "1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c"; // String | the cluster to add the instance to
    Instance instance = new Instance(); // Instance | the instance to add
    try {
      InstanceResult result = apiInstance.clusterClusterKeyInstancesPost(clusterKey, instance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#clusterClusterKeyInstancesPost");
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
| **clusterKey** | **String**| the cluster to add the instance to | |
| **instance** | [**Instance**](Instance.md)| the instance to add | |

### Return type

[**InstanceResult**](InstanceResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the newly created instance |  -  |
| **0** | Unexpected error |  -  |

<a id="clusterClusterKeyPut"></a>
# **clusterClusterKeyPut**
> ClusterResult clusterClusterKeyPut(clusterKey, cluster)

modify cluster

Modify an existing cluster

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String clusterKey = "5074fe62-821e-4034-55bd-b9caa09af2a1"; // String | the cluster key
    Cluster cluster = new Cluster(); // Cluster | the cluster to modify
    try {
      ClusterResult result = apiInstance.clusterClusterKeyPut(clusterKey, cluster);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#clusterClusterKeyPut");
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
| **clusterKey** | **String**| the cluster key | |
| **cluster** | [**Cluster**](Cluster.md)| the cluster to modify | |

### Return type

[**ClusterResult**](ClusterResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A result containing the modified cluster |  -  |
| **0** | Unexpected error |  -  |

<a id="clusterGet"></a>
# **clusterGet**
> MultiClusterResult clusterGet(filters)

get clusters

Get a list of clusters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String filters = "filters_example"; // String | A JSON encoded array of ClusterFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ClusterFilter will be included. 
    try {
      MultiClusterResult result = apiInstance.clusterGet(filters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#clusterGet");
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
| **filters** | **String**| A JSON encoded array of ClusterFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ClusterFilter will be included.  | [optional] |

### Return type

[**MultiClusterResult**](MultiClusterResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a result containing a list of clusters |  -  |
| **0** | Unexpected error |  -  |

<a id="clusterPost"></a>
# **clusterPost**
> ClusterResult clusterPost(cluster)

create cluster

Create a new cluster

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    ClusterCreate cluster = new ClusterCreate(); // ClusterCreate | the cluster to create
    try {
      ClusterResult result = apiInstance.clusterPost(cluster);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#clusterPost");
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
| **cluster** | [**ClusterCreate**](ClusterCreate.md)| the cluster to create | |

### Return type

[**ClusterResult**](ClusterResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the newly created cluster |  -  |
| **0** | Unexpected error |  -  |

