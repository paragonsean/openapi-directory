# WebhooksApi

All URIs are relative to *https://api.test.enode.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postWebhooksFirehoseTest**](WebhooksApi.md#postWebhooksFirehoseTest) | **POST** /webhooks/firehose/test | Test Firehose Webhook |
| [**putWebhooksFirehose**](WebhooksApi.md#putWebhooksFirehose) | **PUT** /webhooks/firehose | Update Firehose Webhook |


<a id="postWebhooksFirehoseTest"></a>
# **postWebhooksFirehoseTest**
> String postWebhooksFirehoseTest()

Test Firehose Webhook

Trigger a test payload to be sent to your configured Firehose Webhook url.

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
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: ClientAccessToken
    OAuth ClientAccessToken = (OAuth) defaultClient.getAuthentication("ClientAccessToken");
    ClientAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    try {
      String result = apiInstance.postWebhooksFirehoseTest();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#postWebhooksFirehoseTest");
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

**String**

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Successful |  -  |

<a id="putWebhooksFirehose"></a>
# **putWebhooksFirehose**
> putWebhooksFirehose(putWebhooksFirehoseRequest)

Update Firehose Webhook

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
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: ClientAccessToken
    OAuth ClientAccessToken = (OAuth) defaultClient.getAuthentication("ClientAccessToken");
    ClientAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    PutWebhooksFirehoseRequest putWebhooksFirehoseRequest = new PutWebhooksFirehoseRequest(); // PutWebhooksFirehoseRequest | 
    try {
      apiInstance.putWebhooksFirehose(putWebhooksFirehoseRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#putWebhooksFirehose");
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
| **putWebhooksFirehoseRequest** | [**PutWebhooksFirehoseRequest**](PutWebhooksFirehoseRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[ClientAccessToken](../README.md#ClientAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

