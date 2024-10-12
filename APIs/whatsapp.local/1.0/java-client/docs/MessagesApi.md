# MessagesApi

All URIs are relative to *http://whatsapp.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**markMessageAsRead**](MessagesApi.md#markMessageAsRead) | **PUT** /messages/{MessageID} | Mark-Message-As-Read |
| [**sendMessage**](MessagesApi.md#sendMessage) | **POST** /messages | Send-Message |


<a id="markMessageAsRead"></a>
# **markMessageAsRead**
> markMessageAsRead(messageID, markMessageAsReadRequestBody)

Mark-Message-As-Read

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://whatsapp.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    String messageID = "messageID_example"; // String | Message ID from Webhook
    MarkMessageAsReadRequestBody markMessageAsReadRequestBody = new MarkMessageAsReadRequestBody(); // MarkMessageAsReadRequestBody | 
    try {
      apiInstance.markMessageAsRead(messageID, markMessageAsReadRequestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#markMessageAsRead");
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
| **messageID** | **String**| Message ID from Webhook | |
| **markMessageAsReadRequestBody** | [**MarkMessageAsReadRequestBody**](MarkMessageAsReadRequestBody.md)|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="sendMessage"></a>
# **sendMessage**
> MessageResponse sendMessage(sendMessageRequestBody)

Send-Message

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://whatsapp.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    MessagesApi apiInstance = new MessagesApi(defaultClient);
    SendMessageRequestBody sendMessageRequestBody = new SendMessageRequestBody(); // SendMessageRequestBody | 
    try {
      MessageResponse result = apiInstance.sendMessage(sendMessageRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagesApi#sendMessage");
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
| **sendMessageRequestBody** | [**SendMessageRequestBody**](SendMessageRequestBody.md)|  | |

### Return type

[**MessageResponse**](MessageResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

