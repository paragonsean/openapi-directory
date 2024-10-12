# WebhookTestsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkWebhooksWebhookTest_2**](WebhookTestsApi.md#createNetworkWebhooksWebhookTest_2) | **POST** /networks/{networkId}/webhooks/webhookTests | Send a test webhook for a network |
| [**getNetworkWebhooksWebhookTest_2**](WebhookTestsApi.md#getNetworkWebhooksWebhookTest_2) | **GET** /networks/{networkId}/webhooks/webhookTests/{webhookTestId} | Return the status of a webhook test for a network |


<a id="createNetworkWebhooksWebhookTest_2"></a>
# **createNetworkWebhooksWebhookTest_2**
> CreateNetworkWebhooksWebhookTest201Response createNetworkWebhooksWebhookTest_2(networkId, createNetworkWebhooksWebhookTestRequest)

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
import org.openapitools.client.api.WebhookTestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WebhookTestsApi apiInstance = new WebhookTestsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkWebhooksWebhookTestRequest createNetworkWebhooksWebhookTestRequest = new CreateNetworkWebhooksWebhookTestRequest(); // CreateNetworkWebhooksWebhookTestRequest | 
    try {
      CreateNetworkWebhooksWebhookTest201Response result = apiInstance.createNetworkWebhooksWebhookTest_2(networkId, createNetworkWebhooksWebhookTestRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookTestsApi#createNetworkWebhooksWebhookTest_2");
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

<a id="getNetworkWebhooksWebhookTest_2"></a>
# **getNetworkWebhooksWebhookTest_2**
> CreateNetworkWebhooksWebhookTest201Response getNetworkWebhooksWebhookTest_2(networkId, webhookTestId)

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
import org.openapitools.client.api.WebhookTestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    WebhookTestsApi apiInstance = new WebhookTestsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String webhookTestId = "webhookTestId_example"; // String | 
    try {
      CreateNetworkWebhooksWebhookTest201Response result = apiInstance.getNetworkWebhooksWebhookTest_2(networkId, webhookTestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhookTestsApi#getNetworkWebhooksWebhookTest_2");
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

