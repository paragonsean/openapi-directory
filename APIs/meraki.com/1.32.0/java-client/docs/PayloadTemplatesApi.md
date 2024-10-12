# PayloadTemplatesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkWebhooksPayloadTemplate_2**](PayloadTemplatesApi.md#createNetworkWebhooksPayloadTemplate_2) | **POST** /networks/{networkId}/webhooks/payloadTemplates | Create a webhook payload template for a network |
| [**deleteNetworkWebhooksPayloadTemplate_2**](PayloadTemplatesApi.md#deleteNetworkWebhooksPayloadTemplate_2) | **DELETE** /networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId} | Destroy a webhook payload template for a network |
| [**getNetworkWebhooksPayloadTemplate_2**](PayloadTemplatesApi.md#getNetworkWebhooksPayloadTemplate_2) | **GET** /networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId} | Get the webhook payload template for a network |
| [**getNetworkWebhooksPayloadTemplates_2**](PayloadTemplatesApi.md#getNetworkWebhooksPayloadTemplates_2) | **GET** /networks/{networkId}/webhooks/payloadTemplates | List the webhook payload templates for a network |
| [**updateNetworkWebhooksPayloadTemplate_2**](PayloadTemplatesApi.md#updateNetworkWebhooksPayloadTemplate_2) | **PUT** /networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId} | Update a webhook payload template for a network |


<a id="createNetworkWebhooksPayloadTemplate_2"></a>
# **createNetworkWebhooksPayloadTemplate_2**
> GetNetworkWebhooksPayloadTemplates200ResponseInner createNetworkWebhooksPayloadTemplate_2(networkId, createNetworkWebhooksPayloadTemplateRequest)

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
import org.openapitools.client.api.PayloadTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PayloadTemplatesApi apiInstance = new PayloadTemplatesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkWebhooksPayloadTemplateRequest createNetworkWebhooksPayloadTemplateRequest = new CreateNetworkWebhooksPayloadTemplateRequest(); // CreateNetworkWebhooksPayloadTemplateRequest | 
    try {
      GetNetworkWebhooksPayloadTemplates200ResponseInner result = apiInstance.createNetworkWebhooksPayloadTemplate_2(networkId, createNetworkWebhooksPayloadTemplateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayloadTemplatesApi#createNetworkWebhooksPayloadTemplate_2");
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

<a id="deleteNetworkWebhooksPayloadTemplate_2"></a>
# **deleteNetworkWebhooksPayloadTemplate_2**
> deleteNetworkWebhooksPayloadTemplate_2(networkId, payloadTemplateId)

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
import org.openapitools.client.api.PayloadTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PayloadTemplatesApi apiInstance = new PayloadTemplatesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String payloadTemplateId = "payloadTemplateId_example"; // String | 
    try {
      apiInstance.deleteNetworkWebhooksPayloadTemplate_2(networkId, payloadTemplateId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayloadTemplatesApi#deleteNetworkWebhooksPayloadTemplate_2");
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

<a id="getNetworkWebhooksPayloadTemplate_2"></a>
# **getNetworkWebhooksPayloadTemplate_2**
> GetNetworkWebhooksPayloadTemplates200ResponseInner getNetworkWebhooksPayloadTemplate_2(networkId, payloadTemplateId)

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
import org.openapitools.client.api.PayloadTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PayloadTemplatesApi apiInstance = new PayloadTemplatesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String payloadTemplateId = "payloadTemplateId_example"; // String | 
    try {
      GetNetworkWebhooksPayloadTemplates200ResponseInner result = apiInstance.getNetworkWebhooksPayloadTemplate_2(networkId, payloadTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayloadTemplatesApi#getNetworkWebhooksPayloadTemplate_2");
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

<a id="getNetworkWebhooksPayloadTemplates_2"></a>
# **getNetworkWebhooksPayloadTemplates_2**
> List&lt;GetNetworkWebhooksPayloadTemplates200ResponseInner&gt; getNetworkWebhooksPayloadTemplates_2(networkId)

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
import org.openapitools.client.api.PayloadTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PayloadTemplatesApi apiInstance = new PayloadTemplatesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkWebhooksPayloadTemplates200ResponseInner> result = apiInstance.getNetworkWebhooksPayloadTemplates_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayloadTemplatesApi#getNetworkWebhooksPayloadTemplates_2");
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

<a id="updateNetworkWebhooksPayloadTemplate_2"></a>
# **updateNetworkWebhooksPayloadTemplate_2**
> GetNetworkWebhooksPayloadTemplates200ResponseInner updateNetworkWebhooksPayloadTemplate_2(networkId, payloadTemplateId, updateNetworkWebhooksPayloadTemplateRequest)

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
import org.openapitools.client.api.PayloadTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PayloadTemplatesApi apiInstance = new PayloadTemplatesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String payloadTemplateId = "payloadTemplateId_example"; // String | 
    UpdateNetworkWebhooksPayloadTemplateRequest updateNetworkWebhooksPayloadTemplateRequest = new UpdateNetworkWebhooksPayloadTemplateRequest(); // UpdateNetworkWebhooksPayloadTemplateRequest | 
    try {
      GetNetworkWebhooksPayloadTemplates200ResponseInner result = apiInstance.updateNetworkWebhooksPayloadTemplate_2(networkId, payloadTemplateId, updateNetworkWebhooksPayloadTemplateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayloadTemplatesApi#updateNetworkWebhooksPayloadTemplate_2");
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

