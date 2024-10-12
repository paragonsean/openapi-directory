# WebhooksApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkWebhooksHttpServer_1**](WebhooksApi.md#createNetworkWebhooksHttpServer_1) | **POST** /networks/{networkId}/webhooks/httpServers | Add an HTTP server to a network |
| [**createNetworkWebhooksPayloadTemplate_1**](WebhooksApi.md#createNetworkWebhooksPayloadTemplate_1) | **POST** /networks/{networkId}/webhooks/payloadTemplates | Create a webhook payload template for a network |
| [**createNetworkWebhooksWebhookTest_1**](WebhooksApi.md#createNetworkWebhooksWebhookTest_1) | **POST** /networks/{networkId}/webhooks/webhookTests | Send a test webhook for a network |
| [**deleteNetworkWebhooksHttpServer_1**](WebhooksApi.md#deleteNetworkWebhooksHttpServer_1) | **DELETE** /networks/{networkId}/webhooks/httpServers/{httpServerId} | Delete an HTTP server from a network |
| [**deleteNetworkWebhooksPayloadTemplate_1**](WebhooksApi.md#deleteNetworkWebhooksPayloadTemplate_1) | **DELETE** /networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId} | Destroy a webhook payload template for a network |
| [**getNetworkWebhooksHttpServer_1**](WebhooksApi.md#getNetworkWebhooksHttpServer_1) | **GET** /networks/{networkId}/webhooks/httpServers/{httpServerId} | Return an HTTP server for a network |
| [**getNetworkWebhooksHttpServers_1**](WebhooksApi.md#getNetworkWebhooksHttpServers_1) | **GET** /networks/{networkId}/webhooks/httpServers | List the HTTP servers for a network |
| [**getNetworkWebhooksPayloadTemplate_1**](WebhooksApi.md#getNetworkWebhooksPayloadTemplate_1) | **GET** /networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId} | Get the webhook payload template for a network |
| [**getNetworkWebhooksPayloadTemplates_1**](WebhooksApi.md#getNetworkWebhooksPayloadTemplates_1) | **GET** /networks/{networkId}/webhooks/payloadTemplates | List the webhook payload templates for a network |
| [**getNetworkWebhooksWebhookTest_1**](WebhooksApi.md#getNetworkWebhooksWebhookTest_1) | **GET** /networks/{networkId}/webhooks/webhookTests/{webhookTestId} | Return the status of a webhook test for a network |
| [**getOrganizationWebhooksAlertTypes_1**](WebhooksApi.md#getOrganizationWebhooksAlertTypes_1) | **GET** /organizations/{organizationId}/webhooks/alertTypes | Return a list of alert types to be used with managing webhook alerts |
| [**getOrganizationWebhooksLogs_1**](WebhooksApi.md#getOrganizationWebhooksLogs_1) | **GET** /organizations/{organizationId}/webhooks/logs | Return the log of webhook POSTs sent |
| [**updateNetworkWebhooksHttpServer_1**](WebhooksApi.md#updateNetworkWebhooksHttpServer_1) | **PUT** /networks/{networkId}/webhooks/httpServers/{httpServerId} | Update an HTTP server |
| [**updateNetworkWebhooksPayloadTemplate_1**](WebhooksApi.md#updateNetworkWebhooksPayloadTemplate_1) | **PUT** /networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId} | Update a webhook payload template for a network |


<a id="createNetworkWebhooksHttpServer_1"></a>
# **createNetworkWebhooksHttpServer_1**
> GetNetworkWebhooksHttpServers200ResponseInner createNetworkWebhooksHttpServer_1(networkId, createNetworkWebhooksHttpServerRequest)

Add an HTTP server to a network

Add an HTTP server to a network

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkWebhooksHttpServerRequest createNetworkWebhooksHttpServerRequest = new CreateNetworkWebhooksHttpServerRequest(); // CreateNetworkWebhooksHttpServerRequest | 
    try {
      GetNetworkWebhooksHttpServers200ResponseInner result = apiInstance.createNetworkWebhooksHttpServer_1(networkId, createNetworkWebhooksHttpServerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#createNetworkWebhooksHttpServer_1");
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
| **networkId** | **String**|  | |
| **createNetworkWebhooksHttpServerRequest** | [**CreateNetworkWebhooksHttpServerRequest**](CreateNetworkWebhooksHttpServerRequest.md)|  | |

### Return type

[**GetNetworkWebhooksHttpServers200ResponseInner**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkWebhooksPayloadTemplate_1"></a>
# **createNetworkWebhooksPayloadTemplate_1**
> GetNetworkWebhooksPayloadTemplates200ResponseInner createNetworkWebhooksPayloadTemplate_1(networkId, createNetworkWebhooksPayloadTemplateRequest)

Create a webhook payload template for a network

Create a webhook payload template for a network

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkWebhooksPayloadTemplateRequest createNetworkWebhooksPayloadTemplateRequest = new CreateNetworkWebhooksPayloadTemplateRequest(); // CreateNetworkWebhooksPayloadTemplateRequest | 
    try {
      GetNetworkWebhooksPayloadTemplates200ResponseInner result = apiInstance.createNetworkWebhooksPayloadTemplate_1(networkId, createNetworkWebhooksPayloadTemplateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#createNetworkWebhooksPayloadTemplate_1");
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
| **networkId** | **String**|  | |
| **createNetworkWebhooksPayloadTemplateRequest** | [**CreateNetworkWebhooksPayloadTemplateRequest**](CreateNetworkWebhooksPayloadTemplateRequest.md)|  | |

### Return type

[**GetNetworkWebhooksPayloadTemplates200ResponseInner**](GetNetworkWebhooksPayloadTemplates200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createNetworkWebhooksWebhookTest_1"></a>
# **createNetworkWebhooksWebhookTest_1**
> CreateNetworkWebhooksWebhookTest201Response createNetworkWebhooksWebhookTest_1(networkId, createNetworkWebhooksWebhookTestRequest)

Send a test webhook for a network

Send a test webhook for a network

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkWebhooksWebhookTestRequest createNetworkWebhooksWebhookTestRequest = new CreateNetworkWebhooksWebhookTestRequest(); // CreateNetworkWebhooksWebhookTestRequest | 
    try {
      CreateNetworkWebhooksWebhookTest201Response result = apiInstance.createNetworkWebhooksWebhookTest_1(networkId, createNetworkWebhooksWebhookTestRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#createNetworkWebhooksWebhookTest_1");
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
| **networkId** | **String**|  | |
| **createNetworkWebhooksWebhookTestRequest** | [**CreateNetworkWebhooksWebhookTestRequest**](CreateNetworkWebhooksWebhookTestRequest.md)|  | |

### Return type

[**CreateNetworkWebhooksWebhookTest201Response**](CreateNetworkWebhooksWebhookTest201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteNetworkWebhooksHttpServer_1"></a>
# **deleteNetworkWebhooksHttpServer_1**
> deleteNetworkWebhooksHttpServer_1(networkId, httpServerId)

Delete an HTTP server from a network

Delete an HTTP server from a network

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String httpServerId = "httpServerId_example"; // String | 
    try {
      apiInstance.deleteNetworkWebhooksHttpServer_1(networkId, httpServerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#deleteNetworkWebhooksHttpServer_1");
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
| **networkId** | **String**|  | |
| **httpServerId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="deleteNetworkWebhooksPayloadTemplate_1"></a>
# **deleteNetworkWebhooksPayloadTemplate_1**
> deleteNetworkWebhooksPayloadTemplate_1(networkId, payloadTemplateId)

Destroy a webhook payload template for a network

Destroy a webhook payload template for a network. Does not work for included templates (&#39;wpt_00001&#39;, &#39;wpt_00002&#39;, &#39;wpt_00003&#39;, &#39;wpt_00004&#39;, &#39;wpt_00005&#39; or &#39;wpt_00006&#39;)

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String payloadTemplateId = "payloadTemplateId_example"; // String | 
    try {
      apiInstance.deleteNetworkWebhooksPayloadTemplate_1(networkId, payloadTemplateId);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#deleteNetworkWebhooksPayloadTemplate_1");
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
| **networkId** | **String**|  | |
| **payloadTemplateId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="getNetworkWebhooksHttpServer_1"></a>
# **getNetworkWebhooksHttpServer_1**
> GetNetworkWebhooksHttpServers200ResponseInner getNetworkWebhooksHttpServer_1(networkId, httpServerId)

Return an HTTP server for a network

Return an HTTP server for a network

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String httpServerId = "httpServerId_example"; // String | 
    try {
      GetNetworkWebhooksHttpServers200ResponseInner result = apiInstance.getNetworkWebhooksHttpServer_1(networkId, httpServerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#getNetworkWebhooksHttpServer_1");
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
| **networkId** | **String**|  | |
| **httpServerId** | **String**|  | |

### Return type

[**GetNetworkWebhooksHttpServers200ResponseInner**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWebhooksHttpServers_1"></a>
# **getNetworkWebhooksHttpServers_1**
> List&lt;GetNetworkWebhooksHttpServers200ResponseInner&gt; getNetworkWebhooksHttpServers_1(networkId)

List the HTTP servers for a network

List the HTTP servers for a network

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkWebhooksHttpServers200ResponseInner> result = apiInstance.getNetworkWebhooksHttpServers_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#getNetworkWebhooksHttpServers_1");
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
| **networkId** | **String**|  | |

### Return type

[**List&lt;GetNetworkWebhooksHttpServers200ResponseInner&gt;**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWebhooksPayloadTemplate_1"></a>
# **getNetworkWebhooksPayloadTemplate_1**
> GetNetworkWebhooksPayloadTemplates200ResponseInner getNetworkWebhooksPayloadTemplate_1(networkId, payloadTemplateId)

Get the webhook payload template for a network

Get the webhook payload template for a network

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String payloadTemplateId = "payloadTemplateId_example"; // String | 
    try {
      GetNetworkWebhooksPayloadTemplates200ResponseInner result = apiInstance.getNetworkWebhooksPayloadTemplate_1(networkId, payloadTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#getNetworkWebhooksPayloadTemplate_1");
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
| **networkId** | **String**|  | |
| **payloadTemplateId** | **String**|  | |

### Return type

[**GetNetworkWebhooksPayloadTemplates200ResponseInner**](GetNetworkWebhooksPayloadTemplates200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWebhooksPayloadTemplates_1"></a>
# **getNetworkWebhooksPayloadTemplates_1**
> List&lt;GetNetworkWebhooksPayloadTemplates200ResponseInner&gt; getNetworkWebhooksPayloadTemplates_1(networkId)

List the webhook payload templates for a network

List the webhook payload templates for a network

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkWebhooksPayloadTemplates200ResponseInner> result = apiInstance.getNetworkWebhooksPayloadTemplates_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#getNetworkWebhooksPayloadTemplates_1");
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
| **networkId** | **String**|  | |

### Return type

[**List&lt;GetNetworkWebhooksPayloadTemplates200ResponseInner&gt;**](GetNetworkWebhooksPayloadTemplates200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkWebhooksWebhookTest_1"></a>
# **getNetworkWebhooksWebhookTest_1**
> CreateNetworkWebhooksWebhookTest201Response getNetworkWebhooksWebhookTest_1(networkId, webhookTestId)

Return the status of a webhook test for a network

Return the status of a webhook test for a network

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String webhookTestId = "webhookTestId_example"; // String | 
    try {
      CreateNetworkWebhooksWebhookTest201Response result = apiInstance.getNetworkWebhooksWebhookTest_1(networkId, webhookTestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#getNetworkWebhooksWebhookTest_1");
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
| **networkId** | **String**|  | |
| **webhookTestId** | **String**|  | |

### Return type

[**CreateNetworkWebhooksWebhookTest201Response**](CreateNetworkWebhooksWebhookTest201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationWebhooksAlertTypes_1"></a>
# **getOrganizationWebhooksAlertTypes_1**
> List&lt;Object&gt; getOrganizationWebhooksAlertTypes_1(organizationId, productType)

Return a list of alert types to be used with managing webhook alerts

Return a list of alert types to be used with managing webhook alerts

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String productType = "appliance"; // String | Filter sample alerts to a specific product type
    try {
      List<Object> result = apiInstance.getOrganizationWebhooksAlertTypes_1(organizationId, productType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#getOrganizationWebhooksAlertTypes_1");
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
| **organizationId** | **String**|  | |
| **productType** | **String**| Filter sample alerts to a specific product type | [optional] [enum: appliance, camera, cellularGateway, health, platform, sensor, sm, switch, wireless] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationWebhooksLogs_1"></a>
# **getOrganizationWebhooksLogs_1**
> List&lt;GetOrganizationWebhooksLogs200ResponseInner&gt; getOrganizationWebhooksLogs_1(organizationId, t0, t1, timespan, perPage, startingAfter, endingBefore, url)

Return the log of webhook POSTs sent

Return the log of webhook POSTs sent

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 90 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String url = "url_example"; // String | The URL the webhook was sent to
    try {
      List<GetOrganizationWebhooksLogs200ResponseInner> result = apiInstance.getOrganizationWebhooksLogs_1(organizationId, t0, t1, timespan, perPage, startingAfter, endingBefore, url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#getOrganizationWebhooksLogs_1");
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
| **organizationId** | **String**|  | |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 90 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **url** | **String**| The URL the webhook was sent to | [optional] |

### Return type

[**List&lt;GetOrganizationWebhooksLogs200ResponseInner&gt;**](GetOrganizationWebhooksLogs200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="updateNetworkWebhooksHttpServer_1"></a>
# **updateNetworkWebhooksHttpServer_1**
> GetNetworkWebhooksHttpServers200ResponseInner updateNetworkWebhooksHttpServer_1(networkId, httpServerId, updateNetworkWebhooksHttpServerRequest)

Update an HTTP server

Update an HTTP server. To change a URL, create a new HTTP server.

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String httpServerId = "httpServerId_example"; // String | 
    UpdateNetworkWebhooksHttpServerRequest updateNetworkWebhooksHttpServerRequest = new UpdateNetworkWebhooksHttpServerRequest(); // UpdateNetworkWebhooksHttpServerRequest | 
    try {
      GetNetworkWebhooksHttpServers200ResponseInner result = apiInstance.updateNetworkWebhooksHttpServer_1(networkId, httpServerId, updateNetworkWebhooksHttpServerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#updateNetworkWebhooksHttpServer_1");
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
| **networkId** | **String**|  | |
| **httpServerId** | **String**|  | |
| **updateNetworkWebhooksHttpServerRequest** | [**UpdateNetworkWebhooksHttpServerRequest**](UpdateNetworkWebhooksHttpServerRequest.md)|  | [optional] |

### Return type

[**GetNetworkWebhooksHttpServers200ResponseInner**](GetNetworkWebhooksHttpServers200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkWebhooksPayloadTemplate_1"></a>
# **updateNetworkWebhooksPayloadTemplate_1**
> GetNetworkWebhooksPayloadTemplates200ResponseInner updateNetworkWebhooksPayloadTemplate_1(networkId, payloadTemplateId, updateNetworkWebhooksPayloadTemplateRequest)

Update a webhook payload template for a network

Update a webhook payload template for a network

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
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String payloadTemplateId = "payloadTemplateId_example"; // String | 
    UpdateNetworkWebhooksPayloadTemplateRequest updateNetworkWebhooksPayloadTemplateRequest = new UpdateNetworkWebhooksPayloadTemplateRequest(); // UpdateNetworkWebhooksPayloadTemplateRequest | 
    try {
      GetNetworkWebhooksPayloadTemplates200ResponseInner result = apiInstance.updateNetworkWebhooksPayloadTemplate_1(networkId, payloadTemplateId, updateNetworkWebhooksPayloadTemplateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#updateNetworkWebhooksPayloadTemplate_1");
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
| **networkId** | **String**|  | |
| **payloadTemplateId** | **String**|  | |
| **updateNetworkWebhooksPayloadTemplateRequest** | [**UpdateNetworkWebhooksPayloadTemplateRequest**](UpdateNetworkWebhooksPayloadTemplateRequest.md)|  | [optional] |

### Return type

[**GetNetworkWebhooksPayloadTemplates200ResponseInner**](GetNetworkWebhooksPayloadTemplates200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

