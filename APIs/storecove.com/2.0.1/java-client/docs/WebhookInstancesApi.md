# WebhookInstancesApi

All URIs are relative to *https://api.storecove.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteWebhookInstance**](WebhookInstancesApi.md#deleteWebhookInstance) | **DELETE** /webhook_instances/{guid} | DELETE a WebhookInstance |
| [**getWebhookInstances**](WebhookInstancesApi.md#getWebhookInstances) | **GET** /webhook_instances/ | GET a WebhookInstance |


<a id="deleteWebhookInstance"></a>
# **deleteWebhookInstance**
> deleteWebhookInstance(guid)

DELETE a WebhookInstance

DELETE a specific WebhookInstance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhookInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    WebhookInstancesApi apiInstance = new WebhookInstancesApi(defaultClient);
    UUID guid = UUID.randomUUID(); // UUID | WebhookInstance guid
    try {
      apiInstance.deleteWebhookInstance(guid);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookInstancesApi#deleteWebhookInstance");
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
| **guid** | **UUID**| WebhookInstance guid | |

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getWebhookInstances"></a>
# **getWebhookInstances**
> WebhookInstance getWebhookInstances()

GET a WebhookInstance

GET a WebhookInstance from the queue. After processing it successfully, DELETE it and GET the next one. When a 204 is received, the queue is empty and the polling process can sleep for a while.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhookInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.storecove.com/api/v2");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    WebhookInstancesApi apiInstance = new WebhookInstancesApi(defaultClient);
    try {
      WebhookInstance result = apiInstance.getWebhookInstances();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookInstancesApi#getWebhookInstances");
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

[**WebhookInstance**](WebhookInstance.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **204** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

