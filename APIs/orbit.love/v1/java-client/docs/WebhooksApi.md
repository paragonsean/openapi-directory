# WebhooksApi

All URIs are relative to *https://app.orbit.love/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workspaceSlugWebhooksGet**](WebhooksApi.md#workspaceSlugWebhooksGet) | **GET** /{workspace_slug}/webhooks | List webhooks in a workspace |
| [**workspaceSlugWebhooksIdDelete**](WebhooksApi.md#workspaceSlugWebhooksIdDelete) | **DELETE** /{workspace_slug}/webhooks/{id} | Delete a webhook |
| [**workspaceSlugWebhooksIdGet**](WebhooksApi.md#workspaceSlugWebhooksIdGet) | **GET** /{workspace_slug}/webhooks/{id} | Get a webhook |
| [**workspaceSlugWebhooksIdPut**](WebhooksApi.md#workspaceSlugWebhooksIdPut) | **PUT** /{workspace_slug}/webhooks/{id} | Update a webhook |
| [**workspaceSlugWebhooksPost**](WebhooksApi.md#workspaceSlugWebhooksPost) | **POST** /{workspace_slug}/webhooks | Create a webhook |


<a id="workspaceSlugWebhooksGet"></a>
# **workspaceSlugWebhooksGet**
> workspaceSlugWebhooksGet(workspaceSlug)

List webhooks in a workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    try {
      apiInstance.workspaceSlugWebhooksGet(workspaceSlug);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#workspaceSlugWebhooksGet");
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
| **workspaceSlug** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="workspaceSlugWebhooksIdDelete"></a>
# **workspaceSlugWebhooksIdDelete**
> workspaceSlugWebhooksIdDelete(workspaceSlug, id)

Delete a webhook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.workspaceSlugWebhooksIdDelete(workspaceSlug, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#workspaceSlugWebhooksIdDelete");
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
| **workspaceSlug** | **String**|  | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | webhook deleted |  -  |
| **403** | forbidden |  -  |

<a id="workspaceSlugWebhooksIdGet"></a>
# **workspaceSlugWebhooksIdGet**
> workspaceSlugWebhooksIdGet(workspaceSlug, id)

Get a webhook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.workspaceSlugWebhooksIdGet(workspaceSlug, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#workspaceSlugWebhooksIdGet");
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
| **workspaceSlug** | **String**|  | |
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="workspaceSlugWebhooksIdPut"></a>
# **workspaceSlugWebhooksIdPut**
> workspaceSlugWebhooksIdPut(workspaceSlug, id, webhookSubscription)

Update a webhook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    String id = "id_example"; // String | 
    WebhookSubscription webhookSubscription = new WebhookSubscription(); // WebhookSubscription | 
    try {
      apiInstance.workspaceSlugWebhooksIdPut(workspaceSlug, id, webhookSubscription);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#workspaceSlugWebhooksIdPut");
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
| **workspaceSlug** | **String**|  | |
| **id** | **String**|  | |
| **webhookSubscription** | [**WebhookSubscription**](WebhookSubscription.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | webhook updated |  -  |
| **403** | forbidden |  -  |

<a id="workspaceSlugWebhooksPost"></a>
# **workspaceSlugWebhooksPost**
> workspaceSlugWebhooksPost(workspaceSlug, webhookSubscription)

Create a webhook

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    WebhookSubscription webhookSubscription = new WebhookSubscription(); // WebhookSubscription | 
    try {
      apiInstance.workspaceSlugWebhooksPost(workspaceSlug, webhookSubscription);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#workspaceSlugWebhooksPost");
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
| **workspaceSlug** | **String**|  | |
| **webhookSubscription** | [**WebhookSubscription**](WebhookSubscription.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | webhook created |  -  |
| **403** | forbidden |  -  |

