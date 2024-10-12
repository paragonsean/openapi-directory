# ApplicationResourceApi

All URIs are relative to *http://azure.local:19080*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createApplicationResource**](ApplicationResourceApi.md#createApplicationResource) | **PUT** /Resources/Applications/{applicationResourceName} | Creates or updates an application resource. |
| [**deleteApplicationResource**](ApplicationResourceApi.md#deleteApplicationResource) | **DELETE** /Resources/Applications/{applicationResourceName} | Deletes the specified application. |
| [**getApplicationResource**](ApplicationResourceApi.md#getApplicationResource) | **GET** /Resources/Applications/{applicationResourceName} | Gets the application with the given name. |
| [**getReplica**](ApplicationResourceApi.md#getReplica) | **GET** /Resources/Applications/{applicationResourceName}/Services/{serviceResourceName}/Replicas/{replicaName} | Gets a specific replica of a given service in an application resource. |
| [**getReplicas**](ApplicationResourceApi.md#getReplicas) | **GET** /Resources/Applications/{applicationResourceName}/Services/{serviceResourceName}/replicas | Gets replicas of a given service in an application resource. |
| [**getService**](ApplicationResourceApi.md#getService) | **GET** /Resources/Applications/{applicationResourceName}/Services/{serviceResourceName} | Gets the description of the specified service in an application resource. |
| [**getServices**](ApplicationResourceApi.md#getServices) | **GET** /Resources/Applications/{applicationResourceName}/Services | Gets all the services in the application resource. |


<a id="createApplicationResource"></a>
# **createApplicationResource**
> createApplicationResource(apiVersion, applicationResourceName, applicationResourceDescription)

Creates or updates an application resource.

Creates an application with the specified name and description. If an application with the same name already exists, then its description are updated to the one indicated in this request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ApplicationResourceApi apiInstance = new ApplicationResourceApi(defaultClient);
    String apiVersion = "6.3-preview"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
    String applicationResourceName = "applicationResourceName_example"; // String | Service Fabric application resource name.
    ApplicationResourceDescription applicationResourceDescription = new ApplicationResourceDescription(); // ApplicationResourceDescription | Description for creating an application resource.
    try {
      apiInstance.createApplicationResource(apiVersion, applicationResourceName, applicationResourceDescription);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationResourceApi#createApplicationResource");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to 6.3-preview] [enum: 6.3-preview] |
| **applicationResourceName** | **String**| Service Fabric application resource name. | |
| **applicationResourceDescription** | [**ApplicationResourceDescription**](ApplicationResourceDescription.md)| Description for creating an application resource. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **202** | Accepted |  -  |
| **0** | Error |  -  |

<a id="deleteApplicationResource"></a>
# **deleteApplicationResource**
> deleteApplicationResource(apiVersion, applicationResourceName)

Deletes the specified application.

Deletes the application identified by the name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ApplicationResourceApi apiInstance = new ApplicationResourceApi(defaultClient);
    String apiVersion = "6.3-preview"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
    String applicationResourceName = "applicationResourceName_example"; // String | Service Fabric application resource name.
    try {
      apiInstance.deleteApplicationResource(apiVersion, applicationResourceName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationResourceApi#deleteApplicationResource");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to 6.3-preview] [enum: 6.3-preview] |
| **applicationResourceName** | **String**| Service Fabric application resource name. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |
| **204** | No Content - the specified application was not found. |  -  |
| **0** | Error |  -  |

<a id="getApplicationResource"></a>
# **getApplicationResource**
> ApplicationResourceDescription getApplicationResource(apiVersion, applicationResourceName)

Gets the application with the given name.

Gets the application with the given name. This includes the information about the application&#39;s services and other runtime information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ApplicationResourceApi apiInstance = new ApplicationResourceApi(defaultClient);
    String apiVersion = "6.3-preview"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
    String applicationResourceName = "applicationResourceName_example"; // String | Service Fabric application resource name.
    try {
      ApplicationResourceDescription result = apiInstance.getApplicationResource(apiVersion, applicationResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationResourceApi#getApplicationResource");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to 6.3-preview] [enum: 6.3-preview] |
| **applicationResourceName** | **String**| Service Fabric application resource name. | |

### Return type

[**ApplicationResourceDescription**](ApplicationResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error |  -  |

<a id="getReplica"></a>
# **getReplica**
> ServiceResourceReplicaDescription getReplica(apiVersion, applicationResourceName, serviceResourceName, replicaName)

Gets a specific replica of a given service in an application resource.

Gets the information about the specified replica of a given service of an application. The information includes the runtime properties of the replica instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ApplicationResourceApi apiInstance = new ApplicationResourceApi(defaultClient);
    String apiVersion = "6.3-preview"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
    String applicationResourceName = "applicationResourceName_example"; // String | Service Fabric application resource name.
    String serviceResourceName = "serviceResourceName_example"; // String | Service Fabric service resource name.
    String replicaName = "replicaName_example"; // String | Service Fabric replica name.
    try {
      ServiceResourceReplicaDescription result = apiInstance.getReplica(apiVersion, applicationResourceName, serviceResourceName, replicaName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationResourceApi#getReplica");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to 6.3-preview] [enum: 6.3-preview] |
| **applicationResourceName** | **String**| Service Fabric application resource name. | |
| **serviceResourceName** | **String**| Service Fabric service resource name. | |
| **replicaName** | **String**| Service Fabric replica name. | |

### Return type

[**ServiceResourceReplicaDescription**](ServiceResourceReplicaDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getReplicas"></a>
# **getReplicas**
> PagedServiceResourceReplicaDescriptionList getReplicas(apiVersion, applicationResourceName, serviceResourceName)

Gets replicas of a given service in an application resource.

Gets the information about all replicas of a given service of an application. The information includes the runtime properties of the replica instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ApplicationResourceApi apiInstance = new ApplicationResourceApi(defaultClient);
    String apiVersion = "6.3-preview"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
    String applicationResourceName = "applicationResourceName_example"; // String | Service Fabric application resource name.
    String serviceResourceName = "serviceResourceName_example"; // String | Service Fabric service resource name.
    try {
      PagedServiceResourceReplicaDescriptionList result = apiInstance.getReplicas(apiVersion, applicationResourceName, serviceResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationResourceApi#getReplicas");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to 6.3-preview] [enum: 6.3-preview] |
| **applicationResourceName** | **String**| Service Fabric application resource name. | |
| **serviceResourceName** | **String**| Service Fabric service resource name. | |

### Return type

[**PagedServiceResourceReplicaDescriptionList**](PagedServiceResourceReplicaDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getService"></a>
# **getService**
> ServiceResourceDescription getService(apiVersion, applicationResourceName, serviceResourceName)

Gets the description of the specified service in an application resource.

Gets the description of the service resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ApplicationResourceApi apiInstance = new ApplicationResourceApi(defaultClient);
    String apiVersion = "6.3-preview"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
    String applicationResourceName = "applicationResourceName_example"; // String | Service Fabric application resource name.
    String serviceResourceName = "serviceResourceName_example"; // String | Service Fabric service resource name.
    try {
      ServiceResourceDescription result = apiInstance.getService(apiVersion, applicationResourceName, serviceResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationResourceApi#getService");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to 6.3-preview] [enum: 6.3-preview] |
| **applicationResourceName** | **String**| Service Fabric application resource name. | |
| **serviceResourceName** | **String**| Service Fabric service resource name. | |

### Return type

[**ServiceResourceDescription**](ServiceResourceDescription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getServices"></a>
# **getServices**
> PagedServiceResourceDescriptionList getServices(apiVersion, applicationResourceName)

Gets all the services in the application resource.

The operation returns the service descriptions of all the services in the application resource. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationResourceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure.local:19080");

    ApplicationResourceApi apiInstance = new ApplicationResourceApi(defaultClient);
    String apiVersion = "6.3-preview"; // String | The version of the API. This parameter is required and its value must be '6.3-preview'.
    String applicationResourceName = "applicationResourceName_example"; // String | Service Fabric application resource name.
    try {
      PagedServiceResourceDescriptionList result = apiInstance.getServices(apiVersion, applicationResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationResourceApi#getServices");
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
| **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#39;6.3-preview&#39;. | [default to 6.3-preview] [enum: 6.3-preview] |
| **applicationResourceName** | **String**| Service Fabric application resource name. | |

### Return type

[**PagedServiceResourceDescriptionList**](PagedServiceResourceDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

