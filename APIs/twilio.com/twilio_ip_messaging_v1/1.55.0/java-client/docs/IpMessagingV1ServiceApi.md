# IpMessagingV1ServiceApi

All URIs are relative to *https://ip-messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createService**](IpMessagingV1ServiceApi.md#createService) | **POST** /v1/Services |  |
| [**deleteService**](IpMessagingV1ServiceApi.md#deleteService) | **DELETE** /v1/Services/{Sid} |  |
| [**fetchService**](IpMessagingV1ServiceApi.md#fetchService) | **GET** /v1/Services/{Sid} |  |
| [**listService**](IpMessagingV1ServiceApi.md#listService) | **GET** /v1/Services |  |
| [**updateService**](IpMessagingV1ServiceApi.md#updateService) | **POST** /v1/Services/{Sid} |  |


<a id="createService"></a>
# **createService**
> IpMessagingV1Service createService(friendlyName)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1ServiceApi apiInstance = new IpMessagingV1ServiceApi(defaultClient);
    String friendlyName = "friendlyName_example"; // String | 
    try {
      IpMessagingV1Service result = apiInstance.createService(friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1ServiceApi#createService");
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
| **friendlyName** | **String**|  | |

### Return type

[**IpMessagingV1Service**](IpMessagingV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteService"></a>
# **deleteService**
> deleteService(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1ServiceApi apiInstance = new IpMessagingV1ServiceApi(defaultClient);
    String sid = "sid_example"; // String | 
    try {
      apiInstance.deleteService(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1ServiceApi#deleteService");
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
| **sid** | **String**|  | |

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

<a id="fetchService"></a>
# **fetchService**
> IpMessagingV1Service fetchService(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1ServiceApi apiInstance = new IpMessagingV1ServiceApi(defaultClient);
    String sid = "sid_example"; // String | 
    try {
      IpMessagingV1Service result = apiInstance.fetchService(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1ServiceApi#fetchService");
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
| **sid** | **String**|  | |

### Return type

[**IpMessagingV1Service**](IpMessagingV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listService"></a>
# **listService**
> ListServiceResponse listService(pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1ServiceApi apiInstance = new IpMessagingV1ServiceApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListServiceResponse result = apiInstance.listService(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1ServiceApi#listService");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListServiceResponse**](ListServiceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateService"></a>
# **updateService**
> IpMessagingV1Service updateService(sid, consumptionReportInterval, defaultChannelCreatorRoleSid, defaultChannelRoleSid, defaultServiceRoleSid, friendlyName, limitsChannelMembers, limitsUserChannels, notificationsAddedToChannelEnabled, notificationsAddedToChannelTemplate, notificationsInvitedToChannelEnabled, notificationsInvitedToChannelTemplate, notificationsNewMessageEnabled, notificationsNewMessageTemplate, notificationsRemovedFromChannelEnabled, notificationsRemovedFromChannelTemplate, postWebhookUrl, preWebhookUrl, reachabilityEnabled, readStatusEnabled, typingIndicatorTimeout, webhookFilters, webhookMethod, webhooksOnChannelAddMethod, webhooksOnChannelAddUrl, webhooksOnChannelAddedMethod, webhooksOnChannelAddedUrl, webhooksOnChannelDestroyMethod, webhooksOnChannelDestroyUrl, webhooksOnChannelDestroyedMethod, webhooksOnChannelDestroyedUrl, webhooksOnChannelUpdateMethod, webhooksOnChannelUpdateUrl, webhooksOnChannelUpdatedMethod, webhooksOnChannelUpdatedUrl, webhooksOnMemberAddMethod, webhooksOnMemberAddUrl, webhooksOnMemberAddedMethod, webhooksOnMemberAddedUrl, webhooksOnMemberRemoveMethod, webhooksOnMemberRemoveUrl, webhooksOnMemberRemovedMethod, webhooksOnMemberRemovedUrl, webhooksOnMessageRemoveMethod, webhooksOnMessageRemoveUrl, webhooksOnMessageRemovedMethod, webhooksOnMessageRemovedUrl, webhooksOnMessageSendMethod, webhooksOnMessageSendUrl, webhooksOnMessageSentMethod, webhooksOnMessageSentUrl, webhooksOnMessageUpdateMethod, webhooksOnMessageUpdateUrl, webhooksOnMessageUpdatedMethod, webhooksOnMessageUpdatedUrl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1ServiceApi apiInstance = new IpMessagingV1ServiceApi(defaultClient);
    String sid = "sid_example"; // String | 
    Integer consumptionReportInterval = 56; // Integer | 
    String defaultChannelCreatorRoleSid = "defaultChannelCreatorRoleSid_example"; // String | 
    String defaultChannelRoleSid = "defaultChannelRoleSid_example"; // String | 
    String defaultServiceRoleSid = "defaultServiceRoleSid_example"; // String | 
    String friendlyName = "friendlyName_example"; // String | 
    Integer limitsChannelMembers = 56; // Integer | 
    Integer limitsUserChannels = 56; // Integer | 
    Boolean notificationsAddedToChannelEnabled = true; // Boolean | 
    String notificationsAddedToChannelTemplate = "notificationsAddedToChannelTemplate_example"; // String | 
    Boolean notificationsInvitedToChannelEnabled = true; // Boolean | 
    String notificationsInvitedToChannelTemplate = "notificationsInvitedToChannelTemplate_example"; // String | 
    Boolean notificationsNewMessageEnabled = true; // Boolean | 
    String notificationsNewMessageTemplate = "notificationsNewMessageTemplate_example"; // String | 
    Boolean notificationsRemovedFromChannelEnabled = true; // Boolean | 
    String notificationsRemovedFromChannelTemplate = "notificationsRemovedFromChannelTemplate_example"; // String | 
    URI postWebhookUrl = new URI(); // URI | 
    URI preWebhookUrl = new URI(); // URI | 
    Boolean reachabilityEnabled = true; // Boolean | 
    Boolean readStatusEnabled = true; // Boolean | 
    Integer typingIndicatorTimeout = 56; // Integer | 
    List<String> webhookFilters = Arrays.asList(); // List<String> | 
    String webhookMethod = "HEAD"; // String | 
    String webhooksOnChannelAddMethod = "HEAD"; // String | 
    URI webhooksOnChannelAddUrl = new URI(); // URI | 
    String webhooksOnChannelAddedMethod = "HEAD"; // String | 
    URI webhooksOnChannelAddedUrl = new URI(); // URI | 
    String webhooksOnChannelDestroyMethod = "HEAD"; // String | 
    URI webhooksOnChannelDestroyUrl = new URI(); // URI | 
    String webhooksOnChannelDestroyedMethod = "HEAD"; // String | 
    URI webhooksOnChannelDestroyedUrl = new URI(); // URI | 
    String webhooksOnChannelUpdateMethod = "HEAD"; // String | 
    URI webhooksOnChannelUpdateUrl = new URI(); // URI | 
    String webhooksOnChannelUpdatedMethod = "HEAD"; // String | 
    URI webhooksOnChannelUpdatedUrl = new URI(); // URI | 
    String webhooksOnMemberAddMethod = "HEAD"; // String | 
    URI webhooksOnMemberAddUrl = new URI(); // URI | 
    String webhooksOnMemberAddedMethod = "HEAD"; // String | 
    URI webhooksOnMemberAddedUrl = new URI(); // URI | 
    String webhooksOnMemberRemoveMethod = "HEAD"; // String | 
    URI webhooksOnMemberRemoveUrl = new URI(); // URI | 
    String webhooksOnMemberRemovedMethod = "HEAD"; // String | 
    URI webhooksOnMemberRemovedUrl = new URI(); // URI | 
    String webhooksOnMessageRemoveMethod = "HEAD"; // String | 
    URI webhooksOnMessageRemoveUrl = new URI(); // URI | 
    String webhooksOnMessageRemovedMethod = "HEAD"; // String | 
    URI webhooksOnMessageRemovedUrl = new URI(); // URI | 
    String webhooksOnMessageSendMethod = "HEAD"; // String | 
    URI webhooksOnMessageSendUrl = new URI(); // URI | 
    String webhooksOnMessageSentMethod = "HEAD"; // String | 
    URI webhooksOnMessageSentUrl = new URI(); // URI | 
    String webhooksOnMessageUpdateMethod = "HEAD"; // String | 
    URI webhooksOnMessageUpdateUrl = new URI(); // URI | 
    String webhooksOnMessageUpdatedMethod = "HEAD"; // String | 
    URI webhooksOnMessageUpdatedUrl = new URI(); // URI | 
    try {
      IpMessagingV1Service result = apiInstance.updateService(sid, consumptionReportInterval, defaultChannelCreatorRoleSid, defaultChannelRoleSid, defaultServiceRoleSid, friendlyName, limitsChannelMembers, limitsUserChannels, notificationsAddedToChannelEnabled, notificationsAddedToChannelTemplate, notificationsInvitedToChannelEnabled, notificationsInvitedToChannelTemplate, notificationsNewMessageEnabled, notificationsNewMessageTemplate, notificationsRemovedFromChannelEnabled, notificationsRemovedFromChannelTemplate, postWebhookUrl, preWebhookUrl, reachabilityEnabled, readStatusEnabled, typingIndicatorTimeout, webhookFilters, webhookMethod, webhooksOnChannelAddMethod, webhooksOnChannelAddUrl, webhooksOnChannelAddedMethod, webhooksOnChannelAddedUrl, webhooksOnChannelDestroyMethod, webhooksOnChannelDestroyUrl, webhooksOnChannelDestroyedMethod, webhooksOnChannelDestroyedUrl, webhooksOnChannelUpdateMethod, webhooksOnChannelUpdateUrl, webhooksOnChannelUpdatedMethod, webhooksOnChannelUpdatedUrl, webhooksOnMemberAddMethod, webhooksOnMemberAddUrl, webhooksOnMemberAddedMethod, webhooksOnMemberAddedUrl, webhooksOnMemberRemoveMethod, webhooksOnMemberRemoveUrl, webhooksOnMemberRemovedMethod, webhooksOnMemberRemovedUrl, webhooksOnMessageRemoveMethod, webhooksOnMessageRemoveUrl, webhooksOnMessageRemovedMethod, webhooksOnMessageRemovedUrl, webhooksOnMessageSendMethod, webhooksOnMessageSendUrl, webhooksOnMessageSentMethod, webhooksOnMessageSentUrl, webhooksOnMessageUpdateMethod, webhooksOnMessageUpdateUrl, webhooksOnMessageUpdatedMethod, webhooksOnMessageUpdatedUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1ServiceApi#updateService");
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
| **sid** | **String**|  | |
| **consumptionReportInterval** | **Integer**|  | [optional] |
| **defaultChannelCreatorRoleSid** | **String**|  | [optional] |
| **defaultChannelRoleSid** | **String**|  | [optional] |
| **defaultServiceRoleSid** | **String**|  | [optional] |
| **friendlyName** | **String**|  | [optional] |
| **limitsChannelMembers** | **Integer**|  | [optional] |
| **limitsUserChannels** | **Integer**|  | [optional] |
| **notificationsAddedToChannelEnabled** | **Boolean**|  | [optional] |
| **notificationsAddedToChannelTemplate** | **String**|  | [optional] |
| **notificationsInvitedToChannelEnabled** | **Boolean**|  | [optional] |
| **notificationsInvitedToChannelTemplate** | **String**|  | [optional] |
| **notificationsNewMessageEnabled** | **Boolean**|  | [optional] |
| **notificationsNewMessageTemplate** | **String**|  | [optional] |
| **notificationsRemovedFromChannelEnabled** | **Boolean**|  | [optional] |
| **notificationsRemovedFromChannelTemplate** | **String**|  | [optional] |
| **postWebhookUrl** | **URI**|  | [optional] |
| **preWebhookUrl** | **URI**|  | [optional] |
| **reachabilityEnabled** | **Boolean**|  | [optional] |
| **readStatusEnabled** | **Boolean**|  | [optional] |
| **typingIndicatorTimeout** | **Integer**|  | [optional] |
| **webhookFilters** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **webhookMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnChannelAddMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnChannelAddUrl** | **URI**|  | [optional] |
| **webhooksOnChannelAddedMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnChannelAddedUrl** | **URI**|  | [optional] |
| **webhooksOnChannelDestroyMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnChannelDestroyUrl** | **URI**|  | [optional] |
| **webhooksOnChannelDestroyedMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnChannelDestroyedUrl** | **URI**|  | [optional] |
| **webhooksOnChannelUpdateMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnChannelUpdateUrl** | **URI**|  | [optional] |
| **webhooksOnChannelUpdatedMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnChannelUpdatedUrl** | **URI**|  | [optional] |
| **webhooksOnMemberAddMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMemberAddUrl** | **URI**|  | [optional] |
| **webhooksOnMemberAddedMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMemberAddedUrl** | **URI**|  | [optional] |
| **webhooksOnMemberRemoveMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMemberRemoveUrl** | **URI**|  | [optional] |
| **webhooksOnMemberRemovedMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMemberRemovedUrl** | **URI**|  | [optional] |
| **webhooksOnMessageRemoveMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMessageRemoveUrl** | **URI**|  | [optional] |
| **webhooksOnMessageRemovedMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMessageRemovedUrl** | **URI**|  | [optional] |
| **webhooksOnMessageSendMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMessageSendUrl** | **URI**|  | [optional] |
| **webhooksOnMessageSentMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMessageSentUrl** | **URI**|  | [optional] |
| **webhooksOnMessageUpdateMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMessageUpdateUrl** | **URI**|  | [optional] |
| **webhooksOnMessageUpdatedMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **webhooksOnMessageUpdatedUrl** | **URI**|  | [optional] |

### Return type

[**IpMessagingV1Service**](IpMessagingV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

