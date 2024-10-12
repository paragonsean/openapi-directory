# WebhookApi

All URIs are relative to *https://api.api2cart.com/v1.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**webhookCount**](WebhookApi.md#webhookCount) | **GET** /webhook.count.json |  |
| [**webhookCreate**](WebhookApi.md#webhookCreate) | **POST** /webhook.create.json |  |
| [**webhookDelete**](WebhookApi.md#webhookDelete) | **DELETE** /webhook.delete.json |  |
| [**webhookEvents**](WebhookApi.md#webhookEvents) | **GET** /webhook.events.json |  |
| [**webhookList**](WebhookApi.md#webhookList) | **GET** /webhook.list.json |  |
| [**webhookUpdate**](WebhookApi.md#webhookUpdate) | **PUT** /webhook.update.json |  |


<a id="webhookCount"></a>
# **webhookCount**
> WebhookCount200Response webhookCount(entity, action, active)



Count registered webhooks on the store.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    WebhookApi apiInstance = new WebhookApi(defaultClient);
    String entity = "entity_example"; // String | The entity you want to filter webhooks by (e.g. order or product)
    String action = "action_example"; // String | The action you want to filter webhooks by (e.g. order or product)
    Boolean active = true; // Boolean | The webhook status you want to filter webhooks by
    try {
      WebhookCount200Response result = apiInstance.webhookCount(entity, action, active);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookApi#webhookCount");
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
| **entity** | **String**| The entity you want to filter webhooks by (e.g. order or product) | [optional] |
| **action** | **String**| The action you want to filter webhooks by (e.g. order or product) | [optional] |
| **active** | **Boolean**| The webhook status you want to filter webhooks by | [optional] |

### Return type

[**WebhookCount200Response**](WebhookCount200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="webhookCreate"></a>
# **webhookCreate**
> AttributeAdd200Response webhookCreate(entity, action, paramCallback, label, fields, active, storeId)



Create webhook on the store and subscribe to it.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    WebhookApi apiInstance = new WebhookApi(defaultClient);
    String entity = "entity_example"; // String | Specify the entity that you want to enable webhooks for (e.g product, order, customer, category)
    String action = "action_example"; // String | Specify what action (event) will trigger the webhook (e.g add, delete, or update)
    String paramCallback = "paramCallback_example"; // String | Callback url that returns shipping rates. It should be able to accept POST requests with json data.
    String label = "label_example"; // String | The name you give to the webhook
    String fields = "force_all"; // String | Fields the webhook should send
    Boolean active = true; // Boolean | Webhook status
    String storeId = "storeId_example"; // String | Defines store id where the webhook should be assigned
    try {
      AttributeAdd200Response result = apiInstance.webhookCreate(entity, action, paramCallback, label, fields, active, storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookApi#webhookCreate");
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
| **entity** | **String**| Specify the entity that you want to enable webhooks for (e.g product, order, customer, category) | |
| **action** | **String**| Specify what action (event) will trigger the webhook (e.g add, delete, or update) | |
| **paramCallback** | **String**| Callback url that returns shipping rates. It should be able to accept POST requests with json data. | [optional] |
| **label** | **String**| The name you give to the webhook | [optional] |
| **fields** | **String**| Fields the webhook should send | [optional] [default to force_all] |
| **active** | **Boolean**| Webhook status | [optional] [default to true] |
| **storeId** | **String**| Defines store id where the webhook should be assigned | [optional] |

### Return type

[**AttributeAdd200Response**](AttributeAdd200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="webhookDelete"></a>
# **webhookDelete**
> AttributeDelete200Response webhookDelete(id)



Delete registered webhook on the store.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    WebhookApi apiInstance = new WebhookApi(defaultClient);
    String id = "id_example"; // String | Webhook id
    try {
      AttributeDelete200Response result = apiInstance.webhookDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookApi#webhookDelete");
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
| **id** | **String**| Webhook id | |

### Return type

[**AttributeDelete200Response**](AttributeDelete200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="webhookEvents"></a>
# **webhookEvents**
> WebhookEvents200Response webhookEvents()



List all Webhooks that are available on this store.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    WebhookApi apiInstance = new WebhookApi(defaultClient);
    try {
      WebhookEvents200Response result = apiInstance.webhookEvents();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookApi#webhookEvents");
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

[**WebhookEvents200Response**](WebhookEvents200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="webhookList"></a>
# **webhookList**
> WebhookList200Response webhookList(params, start, count, entity, action, active, ids)



List registered webhook on the store.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    WebhookApi apiInstance = new WebhookApi(defaultClient);
    String params = "id,entity,action,callback"; // String | Set this parameter in order to choose which entity fields you want to retrieve
    Integer start = 0; // Integer | This parameter sets the number from which you want to get entities
    Integer count = 10; // Integer | This parameter sets the entity amount that has to be retrieved. Max allowed count=250
    String entity = "entity_example"; // String | The entity you want to filter webhooks by (e.g. order or product)
    String action = "action_example"; // String | The action you want to filter webhooks by (e.g. add, update, or delete)
    Boolean active = true; // Boolean | The webhook status you want to filter webhooks by
    String ids = "ids_example"; // String | List of сomma-separated webhook ids
    try {
      WebhookList200Response result = apiInstance.webhookList(params, start, count, entity, action, active, ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookApi#webhookList");
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
| **params** | **String**| Set this parameter in order to choose which entity fields you want to retrieve | [optional] [default to id,entity,action,callback] |
| **start** | **Integer**| This parameter sets the number from which you want to get entities | [optional] [default to 0] |
| **count** | **Integer**| This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250 | [optional] [default to 10] |
| **entity** | **String**| The entity you want to filter webhooks by (e.g. order or product) | [optional] |
| **action** | **String**| The action you want to filter webhooks by (e.g. add, update, or delete) | [optional] |
| **active** | **Boolean**| The webhook status you want to filter webhooks by | [optional] |
| **ids** | **String**| List of сomma-separated webhook ids | [optional] |

### Return type

[**WebhookList200Response**](WebhookList200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="webhookUpdate"></a>
# **webhookUpdate**
> ProductImageUpdate200Response webhookUpdate(id, paramCallback, label, fields, active)



Update Webhooks parameters.

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
    defaultClient.setBasePath("https://api.api2cart.com/v1.1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: store_key
    ApiKeyAuth store_key = (ApiKeyAuth) defaultClient.getAuthentication("store_key");
    store_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //store_key.setApiKeyPrefix("Token");

    WebhookApi apiInstance = new WebhookApi(defaultClient);
    String id = "id_example"; // String | Webhook id
    String paramCallback = "paramCallback_example"; // String | Callback url that returns shipping rates. It should be able to accept POST requests with json data.
    String label = "label_example"; // String | The name you give to the webhook
    String fields = "fields_example"; // String | Fields the webhook should send
    Boolean active = true; // Boolean | Webhook status
    try {
      ProductImageUpdate200Response result = apiInstance.webhookUpdate(id, paramCallback, label, fields, active);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookApi#webhookUpdate");
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
| **id** | **String**| Webhook id | |
| **paramCallback** | **String**| Callback url that returns shipping rates. It should be able to accept POST requests with json data. | [optional] |
| **label** | **String**| The name you give to the webhook | [optional] |
| **fields** | **String**| Fields the webhook should send | [optional] |
| **active** | **Boolean**| Webhook status | [optional] |

### Return type

[**ProductImageUpdate200Response**](ProductImageUpdate200Response.md)

### Authorization

[api_key](../README.md#api_key), [store_key](../README.md#store_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

