# WebhooksApi

All URIs are relative to *https://api.snyk.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAWebhook**](WebhooksApi.md#createAWebhook) | **POST** /org/{orgId}/webhooks | Create a webhook |
| [**deleteAWebhook**](WebhooksApi.md#deleteAWebhook) | **DELETE** /org/{orgId}/webhooks/{webhookId} | Delete a webhook |
| [**listWebhooks**](WebhooksApi.md#listWebhooks) | **GET** /org/{orgId}/webhooks | List webhooks |
| [**pingAWebhook**](WebhooksApi.md#pingAWebhook) | **POST** /org/{orgId}/webhooks/{webhookId}/ping | Ping a webhook |
| [**retrieveAWebhook**](WebhooksApi.md#retrieveAWebhook) | **GET** /org/{orgId}/webhooks/{webhookId} | Retrieve a webhook |


<a id="createAWebhook"></a>
# **createAWebhook**
> createAWebhook(orgId, createAWebhookRequest)

Create a webhook



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to list projects for. The `API_KEY` must have access to this organization.
    CreateAWebhookRequest createAWebhookRequest = new CreateAWebhookRequest(); // CreateAWebhookRequest | 
    try {
      apiInstance.createAWebhook(orgId, createAWebhookRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#createAWebhook");
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
| **orgId** | **String**| The organization ID to list projects for. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **createAWebhookRequest** | [**CreateAWebhookRequest**](CreateAWebhookRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="deleteAWebhook"></a>
# **deleteAWebhook**
> deleteAWebhook(orgId, webhookId)

Delete a webhook



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String orgId = "orgId_example"; // String | Automatically added
    String webhookId = "webhookId_example"; // String | Automatically added
    try {
      apiInstance.deleteAWebhook(orgId, webhookId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#deleteAWebhook");
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
| **orgId** | **String**| Automatically added | |
| **webhookId** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listWebhooks"></a>
# **listWebhooks**
> listWebhooks(orgId)

List webhooks



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to list projects for. The `API_KEY` must have access to this organization.
    try {
      apiInstance.listWebhooks(orgId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#listWebhooks");
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
| **orgId** | **String**| The organization ID to list projects for. The &#x60;API_KEY&#x60; must have access to this organization. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="pingAWebhook"></a>
# **pingAWebhook**
> pingAWebhook(orgId, webhookId)

Ping a webhook



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID the project belongs to. The `API_KEY` must have access to this organization.
    String webhookId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The webhook ID.
    try {
      apiInstance.pingAWebhook(orgId, webhookId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#pingAWebhook");
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
| **orgId** | **String**| The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **webhookId** | **String**| The webhook ID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="retrieveAWebhook"></a>
# **retrieveAWebhook**
> retrieveAWebhook(orgId, webhookId)

Retrieve a webhook



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID the project belongs to. The `API_KEY` must have access to this organization.
    String webhookId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The webhook ID.
    try {
      apiInstance.retrieveAWebhook(orgId, webhookId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#retrieveAWebhook");
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
| **orgId** | **String**| The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **webhookId** | **String**| The webhook ID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

