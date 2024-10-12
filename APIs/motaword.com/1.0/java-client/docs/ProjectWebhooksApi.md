# ProjectWebhooksApi

All URIs are relative to *https://api.motaword.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteProjectWebhook**](ProjectWebhooksApi.md#deleteProjectWebhook) | **DELETE** /projects/{id}/webhooks | Delete project webhooks |
| [**getProjectWebhooks**](ProjectWebhooksApi.md#getProjectWebhooks) | **GET** /projects/{id}/webhooks | View project webhooks |
| [**postProjectWebhook**](ProjectWebhooksApi.md#postProjectWebhook) | **POST** /projects/{id}/webhooks | Update project webhook |
| [**updateProjectWebhook**](ProjectWebhooksApi.md#updateProjectWebhook) | **PUT** /projects/{id}/webhooks | Update project webhook |


<a id="deleteProjectWebhook"></a>
# **deleteProjectWebhook**
> OperationStatus deleteProjectWebhook(id)

Delete project webhooks

Delete project webhooks. Projects currently support registering only 1 webhook. This endpoint deletes the previously registered webhook.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectWebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ProjectWebhooksApi apiInstance = new ProjectWebhooksApi(defaultClient);
    Long id = 74L; // Long | Project ID
    try {
      OperationStatus result = apiInstance.deleteProjectWebhook(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectWebhooksApi#deleteProjectWebhook");
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
| **id** | **Long**| Project ID | |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project webhook deleted successfully |  -  |
| **404** | ProjectNotFound |  -  |

<a id="getProjectWebhooks"></a>
# **getProjectWebhooks**
> Project getProjectWebhooks(id)

View project webhooks

This endpoint returns Project entity which contains &#x60;callback_url&#x60; field for webhook URL. Currently projects can have only 1 webhook registered.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectWebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ProjectWebhooksApi apiInstance = new ProjectWebhooksApi(defaultClient);
    Long id = 74L; // Long | Project ID
    try {
      Project result = apiInstance.getProjectWebhooks(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectWebhooksApi#getProjectWebhooks");
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
| **id** | **Long**| Project ID | |

### Return type

[**Project**](Project.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project model |  -  |
| **404** | ProjectNotFound |  -  |

<a id="postProjectWebhook"></a>
# **postProjectWebhook**
> Project postProjectWebhook(id, webhook)

Update project webhook

Update project webhook URL

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectWebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ProjectWebhooksApi apiInstance = new ProjectWebhooksApi(defaultClient);
    Long id = 74L; // Long | Project ID
    Webhook webhook = new Webhook(); // Webhook | 
    try {
      Project result = apiInstance.postProjectWebhook(id, webhook);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectWebhooksApi#postProjectWebhook");
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
| **id** | **Long**| Project ID | |
| **webhook** | [**Webhook**](Webhook.md)|  | [optional] |

### Return type

[**Project**](Project.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated project |  -  |
| **404** | ProjectNotFound |  -  |

<a id="updateProjectWebhook"></a>
# **updateProjectWebhook**
> Project updateProjectWebhook(id, webhook)

Update project webhook

Update project webhook URL

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectWebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    ProjectWebhooksApi apiInstance = new ProjectWebhooksApi(defaultClient);
    Long id = 74L; // Long | Project ID
    Webhook webhook = new Webhook(); // Webhook | 
    try {
      Project result = apiInstance.updateProjectWebhook(id, webhook);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectWebhooksApi#updateProjectWebhook");
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
| **id** | **Long**| Project ID | |
| **webhook** | [**Webhook**](Webhook.md)|  | [optional] |

### Return type

[**Project**](Project.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated project |  -  |
| **404** | ProjectNotFound |  -  |

