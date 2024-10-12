# RepositoriesApi

All URIs are relative to *https://hub.docker.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2NamespacesNamespaceRepositoriesRepositoryTagsGet**](RepositoriesApi.md#v2NamespacesNamespaceRepositoriesRepositoryTagsGet) | **GET** /v2/namespaces/{namespace}/repositories/{repository}/tags | List repository tags |
| [**v2NamespacesNamespaceRepositoriesRepositoryTagsHead**](RepositoriesApi.md#v2NamespacesNamespaceRepositoriesRepositoryTagsHead) | **HEAD** /v2/namespaces/{namespace}/repositories/{repository}/tags | Check repository tags |
| [**v2NamespacesNamespaceRepositoriesRepositoryTagsTagGet**](RepositoriesApi.md#v2NamespacesNamespaceRepositoriesRepositoryTagsTagGet) | **GET** /v2/namespaces/{namespace}/repositories/{repository}/tags/{tag} | Read repository tag |
| [**v2NamespacesNamespaceRepositoriesRepositoryTagsTagHead**](RepositoriesApi.md#v2NamespacesNamespaceRepositoriesRepositoryTagsTagHead) | **HEAD** /v2/namespaces/{namespace}/repositories/{repository}/tags/{tag} | Check repository tag |


<a id="v2NamespacesNamespaceRepositoriesRepositoryTagsGet"></a>
# **v2NamespacesNamespaceRepositoriesRepositoryTagsGet**
> PaginatedTags v2NamespacesNamespaceRepositoriesRepositoryTagsGet(namespace, repository, page, pageSize)

List repository tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String namespace = "namespace_example"; // String | 
    String repository = "repository_example"; // String | 
    Integer page = 56; // Integer | Page number to get. Defaults to 1.
    Integer pageSize = 56; // Integer | Number of items to get per page. Defaults to 10. Max of 100.
    try {
      PaginatedTags result = apiInstance.v2NamespacesNamespaceRepositoriesRepositoryTagsGet(namespace, repository, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#v2NamespacesNamespaceRepositoriesRepositoryTagsGet");
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
| **namespace** | **String**|  | |
| **repository** | **String**|  | |
| **page** | **Integer**| Page number to get. Defaults to 1. | [optional] |
| **pageSize** | **Integer**| Number of items to get per page. Defaults to 10. Max of 100. | [optional] |

### Return type

[**PaginatedTags**](PaginatedTags.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | list repository tags |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="v2NamespacesNamespaceRepositoriesRepositoryTagsHead"></a>
# **v2NamespacesNamespaceRepositoriesRepositoryTagsHead**
> v2NamespacesNamespaceRepositoriesRepositoryTagsHead(namespace, repository)

Check repository tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String namespace = "namespace_example"; // String | 
    String repository = "repository_example"; // String | 
    try {
      apiInstance.v2NamespacesNamespaceRepositoriesRepositoryTagsHead(namespace, repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#v2NamespacesNamespaceRepositoriesRepositoryTagsHead");
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
| **namespace** | **String**|  | |
| **repository** | **String**|  | |

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
| **200** | Repository contains tags |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="v2NamespacesNamespaceRepositoriesRepositoryTagsTagGet"></a>
# **v2NamespacesNamespaceRepositoriesRepositoryTagsTagGet**
> Tag v2NamespacesNamespaceRepositoriesRepositoryTagsTagGet(namespace, repository, tag)

Read repository tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String namespace = "namespace_example"; // String | 
    String repository = "repository_example"; // String | 
    String tag = "tag_example"; // String | 
    try {
      Tag result = apiInstance.v2NamespacesNamespaceRepositoriesRepositoryTagsTagGet(namespace, repository, tag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#v2NamespacesNamespaceRepositoriesRepositoryTagsTagGet");
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
| **namespace** | **String**|  | |
| **repository** | **String**|  | |
| **tag** | **String**|  | |

### Return type

[**Tag**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | repository tag |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="v2NamespacesNamespaceRepositoriesRepositoryTagsTagHead"></a>
# **v2NamespacesNamespaceRepositoriesRepositoryTagsTagHead**
> v2NamespacesNamespaceRepositoriesRepositoryTagsTagHead(namespace, repository, tag)

Check repository tag

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://hub.docker.com");

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String namespace = "namespace_example"; // String | 
    String repository = "repository_example"; // String | 
    String tag = "tag_example"; // String | 
    try {
      apiInstance.v2NamespacesNamespaceRepositoriesRepositoryTagsTagHead(namespace, repository, tag);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#v2NamespacesNamespaceRepositoriesRepositoryTagsTagHead");
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
| **namespace** | **String**|  | |
| **repository** | **String**|  | |
| **tag** | **String**|  | |

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
| **200** | Repository tag exists |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

