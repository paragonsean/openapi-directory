# DiscoveryApi

All URIs are relative to *https://hub.docker.com/api/publisher/analytics/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNamespace**](DiscoveryApi.md#getNamespace) | **GET** /namespaces/{namespace} | Get namespace |
| [**getNamespaces**](DiscoveryApi.md#getNamespaces) | **GET** / | Get namespaces and repos |


<a id="getNamespace"></a>
# **getNamespace**
> NamespaceMetadata getNamespace(namespace)

Get namespace

Gets metadata associated with specified namespace, including extra repos associated with the namespace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com/api/publisher/analytics/v1");
    
    // Configure HTTP bearer authorization: HubAuth
    HttpBearerAuth HubAuth = (HttpBearerAuth) defaultClient.getAuthentication("HubAuth");
    HubAuth.setBearerToken("BEARER TOKEN");

    DiscoveryApi apiInstance = new DiscoveryApi(defaultClient);
    String namespace = "namespace_example"; // String | Namespace to fetch data for
    try {
      NamespaceMetadata result = apiInstance.getNamespace(namespace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryApi#getNamespace");
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
| **namespace** | **String**| Namespace to fetch data for | |

### Return type

[**NamespaceMetadata**](NamespaceMetadata.md)

### Authorization

[HubAuth](../README.md#HubAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getNamespaces"></a>
# **getNamespaces**
> NamespaceData getNamespaces()

Get namespaces and repos

Gets a list of your namespaces and repos which have data available

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiscoveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com/api/publisher/analytics/v1");
    
    // Configure HTTP bearer authorization: HubAuth
    HttpBearerAuth HubAuth = (HttpBearerAuth) defaultClient.getAuthentication("HubAuth");
    HubAuth.setBearerToken("BEARER TOKEN");

    DiscoveryApi apiInstance = new DiscoveryApi(defaultClient);
    try {
      NamespaceData result = apiInstance.getNamespaces();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiscoveryApi#getNamespaces");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NamespaceData**](NamespaceData.md)

### Authorization

[HubAuth](../README.md#HubAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

