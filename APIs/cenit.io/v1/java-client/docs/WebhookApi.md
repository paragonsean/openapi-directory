# WebhookApi

All URIs are relative to *https://cenit.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**setupWebhookGet**](WebhookApi.md#setupWebhookGet) | **GET** /setup/webhook/ | Returns a list of webhooks |
| [**setupWebhookIdDelete**](WebhookApi.md#setupWebhookIdDelete) | **DELETE** /setup/webhook/{id} | Delete a webhook |
| [**setupWebhookIdGet**](WebhookApi.md#setupWebhookIdGet) | **GET** /setup/webhook/{id} | Retrieve an existing webhook |
| [**setupWebhookPost**](WebhookApi.md#setupWebhookPost) | **POST** /setup/webhook/ | Create or update a webhook |


<a id="setupWebhookGet"></a>
# **setupWebhookGet**
> List&lt;Webhook&gt; setupWebhookGet()

Returns a list of webhooks

Returns a list of webhooks you&#39;ve previously created. The webhooks are returned in sorted order, with the most recent webhook appearing first.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cenit.io/api/v1");
    
    // Configure API key authorization: X-User-Access-Key
    ApiKeyAuth X-User-Access-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Key");
    X-User-Access-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-User-Access-Token
    ApiKeyAuth X-User-Access-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Token");
    X-User-Access-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Token.setApiKeyPrefix("Token");

    WebhookApi apiInstance = new WebhookApi(defaultClient);
    try {
      List<Webhook> result = apiInstance.setupWebhookGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookApi#setupWebhookGet");
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

[**List&lt;Webhook&gt;**](Webhook.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="setupWebhookIdDelete"></a>
# **setupWebhookIdDelete**
> setupWebhookIdDelete(id)

Delete a webhook

Deletes the specified webhook.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cenit.io/api/v1");
    
    // Configure API key authorization: X-User-Access-Key
    ApiKeyAuth X-User-Access-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Key");
    X-User-Access-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-User-Access-Token
    ApiKeyAuth X-User-Access-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Token");
    X-User-Access-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Token.setApiKeyPrefix("Token");

    WebhookApi apiInstance = new WebhookApi(defaultClient);
    String id = "id_example"; // String | Webhook ID.
    try {
      apiInstance.setupWebhookIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookApi#setupWebhookIdDelete");
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
| **id** | **String**| Webhook ID. | |

### Return type

null (empty response body)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Item not found |  -  |

<a id="setupWebhookIdGet"></a>
# **setupWebhookIdGet**
> Webhook setupWebhookIdGet(id)

Retrieve an existing webhook

Retrieves the details of an existing webhook. You need only supply the unique webhook identifier that was returned upon webhook creation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cenit.io/api/v1");
    
    // Configure API key authorization: X-User-Access-Key
    ApiKeyAuth X-User-Access-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Key");
    X-User-Access-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-User-Access-Token
    ApiKeyAuth X-User-Access-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Token");
    X-User-Access-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Token.setApiKeyPrefix("Token");

    WebhookApi apiInstance = new WebhookApi(defaultClient);
    String id = "id_example"; // String | Webhook ID.
    try {
      Webhook result = apiInstance.setupWebhookIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookApi#setupWebhookIdGet");
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
| **id** | **String**| Webhook ID. | |

### Return type

[**Webhook**](Webhook.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Item not found. |  -  |

<a id="setupWebhookPost"></a>
# **setupWebhookPost**
> Webhook setupWebhookPost()

Create or update a webhook

Creates or updates the specified webhook. Any parameters not provided will be left unchanged.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cenit.io/api/v1");
    
    // Configure API key authorization: X-User-Access-Key
    ApiKeyAuth X-User-Access-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Key");
    X-User-Access-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-User-Access-Token
    ApiKeyAuth X-User-Access-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Token");
    X-User-Access-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Token.setApiKeyPrefix("Token");

    WebhookApi apiInstance = new WebhookApi(defaultClient);
    try {
      Webhook result = apiInstance.setupWebhookPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookApi#setupWebhookPost");
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

[**Webhook**](Webhook.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

