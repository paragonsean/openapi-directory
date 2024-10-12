# NamespacesApi

All URIs are relative to *https://control.ably.net/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appsAppIdNamespacesGet**](NamespacesApi.md#appsAppIdNamespacesGet) | **GET** /apps/{app_id}/namespaces | Lists namespaces |
| [**appsAppIdNamespacesNamespaceIdDelete**](NamespacesApi.md#appsAppIdNamespacesNamespaceIdDelete) | **DELETE** /apps/{app_id}/namespaces/{namespace_id} | Deletes a namespace |
| [**appsAppIdNamespacesNamespaceIdPatch**](NamespacesApi.md#appsAppIdNamespacesNamespaceIdPatch) | **PATCH** /apps/{app_id}/namespaces/{namespace_id} | Updates a namespace |
| [**appsAppIdNamespacesPost**](NamespacesApi.md#appsAppIdNamespacesPost) | **POST** /apps/{app_id}/namespaces | Creates a namespace |


<a id="appsAppIdNamespacesGet"></a>
# **appsAppIdNamespacesGet**
> List&lt;NamespaceResponse&gt; appsAppIdNamespacesGet(appId)

Lists namespaces

List the namespaces for the specified application ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String appId = "appId_example"; // String | The application ID.
    try {
      List<NamespaceResponse> result = apiInstance.appsAppIdNamespacesGet(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#appsAppIdNamespacesGet");
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
| **appId** | **String**| The application ID. | |

### Return type

[**List&lt;NamespaceResponse&gt;**](NamespaceResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Namespace list |  -  |
| **401** | Authentication failed |  -  |
| **404** | App not found |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

<a id="appsAppIdNamespacesNamespaceIdDelete"></a>
# **appsAppIdNamespacesNamespaceIdDelete**
> appsAppIdNamespacesNamespaceIdDelete(appId, namespaceId)

Deletes a namespace

Deletes the namespace with the specified ID, for the specified application ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String appId = "appId_example"; // String | The application ID.
    String namespaceId = "namespaceId_example"; // String | The namespace ID.
    try {
      apiInstance.appsAppIdNamespacesNamespaceIdDelete(appId, namespaceId);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#appsAppIdNamespacesNamespaceIdDelete");
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
| **appId** | **String**| The application ID. | |
| **namespaceId** | **String**| The namespace ID. | |

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Namespace deleted |  -  |
| **401** | Authentication failed |  -  |
| **404** | Not found |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

<a id="appsAppIdNamespacesNamespaceIdPatch"></a>
# **appsAppIdNamespacesNamespaceIdPatch**
> NamespaceResponse appsAppIdNamespacesNamespaceIdPatch(appId, namespaceId, namespacePatch)

Updates a namespace

Updates the namespace with the specified ID, for the application with the specified application ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String appId = "appId_example"; // String | The application ID.
    String namespaceId = "namespaceId_example"; // String | The namespace ID.
    NamespacePatch namespacePatch = new NamespacePatch(); // NamespacePatch | 
    try {
      NamespaceResponse result = apiInstance.appsAppIdNamespacesNamespaceIdPatch(appId, namespaceId, namespacePatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#appsAppIdNamespacesNamespaceIdPatch");
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
| **appId** | **String**| The application ID. | |
| **namespaceId** | **String**| The namespace ID. | |
| **namespacePatch** | [**NamespacePatch**](NamespacePatch.md)|  | [optional] |

### Return type

[**NamespaceResponse**](NamespaceResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Namespace updated |  -  |
| **400** | Bad request |  -  |
| **401** | Authentication failed |  -  |
| **404** | Not found |  -  |
| **500** | Internal server error |  -  |
| **504** | Gateway timeout |  -  |

<a id="appsAppIdNamespacesPost"></a>
# **appsAppIdNamespacesPost**
> NamespaceResponse appsAppIdNamespacesPost(appId, namespacePost)

Creates a namespace

Creates a namespace for the specified application ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://control.ably.net/v1");
    
    // Configure HTTP bearer authorization: bearer_auth
    HttpBearerAuth bearer_auth = (HttpBearerAuth) defaultClient.getAuthentication("bearer_auth");
    bearer_auth.setBearerToken("BEARER TOKEN");

    NamespacesApi apiInstance = new NamespacesApi(defaultClient);
    String appId = "appId_example"; // String | The application ID.
    NamespacePost namespacePost = new NamespacePost(); // NamespacePost | 
    try {
      NamespaceResponse result = apiInstance.appsAppIdNamespacesPost(appId, namespacePost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespacesApi#appsAppIdNamespacesPost");
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
| **appId** | **String**| The application ID. | |
| **namespacePost** | [**NamespacePost**](NamespacePost.md)|  | [optional] |

### Return type

[**NamespaceResponse**](NamespaceResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Namespace created |  -  |
| **400** | Bad request |  -  |
| **401** | Authentication failed |  -  |
| **404** | App not found |  -  |
| **422** | Invalid request |  -  |
| **500** | Internal server error |  -  |

