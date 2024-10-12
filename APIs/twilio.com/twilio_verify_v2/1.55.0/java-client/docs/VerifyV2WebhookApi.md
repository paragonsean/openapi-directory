# VerifyV2WebhookApi

All URIs are relative to *https://verify.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWebhook**](VerifyV2WebhookApi.md#createWebhook) | **POST** /v2/Services/{ServiceSid}/Webhooks |  |
| [**deleteWebhook**](VerifyV2WebhookApi.md#deleteWebhook) | **DELETE** /v2/Services/{ServiceSid}/Webhooks/{Sid} |  |
| [**fetchWebhook**](VerifyV2WebhookApi.md#fetchWebhook) | **GET** /v2/Services/{ServiceSid}/Webhooks/{Sid} |  |
| [**listWebhook**](VerifyV2WebhookApi.md#listWebhook) | **GET** /v2/Services/{ServiceSid}/Webhooks |  |
| [**updateWebhook**](VerifyV2WebhookApi.md#updateWebhook) | **POST** /v2/Services/{ServiceSid}/Webhooks/{Sid} |  |


<a id="createWebhook"></a>
# **createWebhook**
> VerifyV2ServiceWebhook createWebhook(serviceSid, eventTypes, friendlyName, webhookUrl, status, version)



Create a new Webhook for the Service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2WebhookApi apiInstance = new VerifyV2WebhookApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Service.
    List<String> eventTypes = Arrays.asList(); // List<String> | The array of events that this Webhook is subscribed to. Possible event types: `*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied`
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the webhook. **This value should not contain PII.**
    String webhookUrl = "webhookUrl_example"; // String | The URL associated with this Webhook.
    WebhookEnumStatus status = WebhookEnumStatus.fromValue("enabled"); // WebhookEnumStatus | 
    WebhookEnumVersion version = WebhookEnumVersion.fromValue("v1"); // WebhookEnumVersion | 
    try {
      VerifyV2ServiceWebhook result = apiInstance.createWebhook(serviceSid, eventTypes, friendlyName, webhookUrl, status, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2WebhookApi#createWebhook");
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
| **serviceSid** | **String**| The unique SID identifier of the Service. | |
| **eventTypes** | [**List&lt;String&gt;**](String.md)| The array of events that this Webhook is subscribed to. Possible event types: &#x60;*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied&#x60; | |
| **friendlyName** | **String**| The string that you assigned to describe the webhook. **This value should not contain PII.** | |
| **webhookUrl** | **String**| The URL associated with this Webhook. | |
| **status** | **WebhookEnumStatus**|  | [optional] [enum: enabled, disabled] |
| **version** | **WebhookEnumVersion**|  | [optional] [enum: v1, v2] |

### Return type

[**VerifyV2ServiceWebhook**](VerifyV2ServiceWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteWebhook"></a>
# **deleteWebhook**
> deleteWebhook(serviceSid, sid)



Delete a specific Webhook.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2WebhookApi apiInstance = new VerifyV2WebhookApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Service.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Webhook resource to delete.
    try {
      apiInstance.deleteWebhook(serviceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2WebhookApi#deleteWebhook");
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
| **serviceSid** | **String**| The unique SID identifier of the Service. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Webhook resource to delete. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchWebhook"></a>
# **fetchWebhook**
> VerifyV2ServiceWebhook fetchWebhook(serviceSid, sid)



Fetch a specific Webhook.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2WebhookApi apiInstance = new VerifyV2WebhookApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Service.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Webhook resource to fetch.
    try {
      VerifyV2ServiceWebhook result = apiInstance.fetchWebhook(serviceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2WebhookApi#fetchWebhook");
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
| **serviceSid** | **String**| The unique SID identifier of the Service. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Webhook resource to fetch. | |

### Return type

[**VerifyV2ServiceWebhook**](VerifyV2ServiceWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listWebhook"></a>
# **listWebhook**
> ListWebhookResponse listWebhook(serviceSid, pageSize, page, pageToken)



Retrieve a list of all Webhooks for a Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2WebhookApi apiInstance = new VerifyV2WebhookApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Service.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListWebhookResponse result = apiInstance.listWebhook(serviceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2WebhookApi#listWebhook");
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
| **serviceSid** | **String**| The unique SID identifier of the Service. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListWebhookResponse**](ListWebhookResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateWebhook"></a>
# **updateWebhook**
> VerifyV2ServiceWebhook updateWebhook(serviceSid, sid, eventTypes, friendlyName, status, version, webhookUrl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerifyV2WebhookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://verify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VerifyV2WebhookApi apiInstance = new VerifyV2WebhookApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Service.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Webhook resource to update.
    List<String> eventTypes = Arrays.asList(); // List<String> | The array of events that this Webhook is subscribed to. Possible event types: `*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied`
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the webhook. **This value should not contain PII.**
    WebhookEnumStatus status = WebhookEnumStatus.fromValue("enabled"); // WebhookEnumStatus | 
    WebhookEnumVersion version = WebhookEnumVersion.fromValue("v1"); // WebhookEnumVersion | 
    String webhookUrl = "webhookUrl_example"; // String | The URL associated with this Webhook.
    try {
      VerifyV2ServiceWebhook result = apiInstance.updateWebhook(serviceSid, sid, eventTypes, friendlyName, status, version, webhookUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerifyV2WebhookApi#updateWebhook");
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
| **serviceSid** | **String**| The unique SID identifier of the Service. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Webhook resource to update. | |
| **eventTypes** | [**List&lt;String&gt;**](String.md)| The array of events that this Webhook is subscribed to. Possible event types: &#x60;*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied&#x60; | [optional] |
| **friendlyName** | **String**| The string that you assigned to describe the webhook. **This value should not contain PII.** | [optional] |
| **status** | **WebhookEnumStatus**|  | [optional] [enum: enabled, disabled] |
| **version** | **WebhookEnumVersion**|  | [optional] [enum: v1, v2] |
| **webhookUrl** | **String**| The URL associated with this Webhook. | [optional] |

### Return type

[**VerifyV2ServiceWebhook**](VerifyV2ServiceWebhook.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

