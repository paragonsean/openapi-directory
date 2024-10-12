# IpMessagingV2ServiceApi

All URIs are relative to *https://ip-messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createService**](IpMessagingV2ServiceApi.md#createService) | **POST** /v2/Services |  |
| [**deleteService**](IpMessagingV2ServiceApi.md#deleteService) | **DELETE** /v2/Services/{Sid} |  |
| [**fetchService**](IpMessagingV2ServiceApi.md#fetchService) | **GET** /v2/Services/{Sid} |  |
| [**listService**](IpMessagingV2ServiceApi.md#listService) | **GET** /v2/Services |  |
| [**updateService**](IpMessagingV2ServiceApi.md#updateService) | **POST** /v2/Services/{Sid} |  |


<a id="createService"></a>
# **createService**
> IpMessagingV2Service createService(friendlyName)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2ServiceApi apiInstance = new IpMessagingV2ServiceApi(defaultClient);
    String friendlyName = "friendlyName_example"; // String | 
    try {
      IpMessagingV2Service result = apiInstance.createService(friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2ServiceApi#createService");
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

[**IpMessagingV2Service**](IpMessagingV2Service.md)

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
import org.openapitools.client.api.IpMessagingV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2ServiceApi apiInstance = new IpMessagingV2ServiceApi(defaultClient);
    String sid = "sid_example"; // String | 
    try {
      apiInstance.deleteService(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2ServiceApi#deleteService");
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
> IpMessagingV2Service fetchService(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2ServiceApi apiInstance = new IpMessagingV2ServiceApi(defaultClient);
    String sid = "sid_example"; // String | 
    try {
      IpMessagingV2Service result = apiInstance.fetchService(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2ServiceApi#fetchService");
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

[**IpMessagingV2Service**](IpMessagingV2Service.md)

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
import org.openapitools.client.api.IpMessagingV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2ServiceApi apiInstance = new IpMessagingV2ServiceApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListServiceResponse result = apiInstance.listService(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2ServiceApi#listService");
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
> IpMessagingV2Service updateService(sid, consumptionReportInterval, defaultChannelCreatorRoleSid, defaultChannelRoleSid, defaultServiceRoleSid, friendlyName, limitsChannelMembers, limitsUserChannels, mediaCompatibilityMessage, notificationsAddedToChannelEnabled, notificationsAddedToChannelSound, notificationsAddedToChannelTemplate, notificationsInvitedToChannelEnabled, notificationsInvitedToChannelSound, notificationsInvitedToChannelTemplate, notificationsLogEnabled, notificationsNewMessageBadgeCountEnabled, notificationsNewMessageEnabled, notificationsNewMessageSound, notificationsNewMessageTemplate, notificationsRemovedFromChannelEnabled, notificationsRemovedFromChannelSound, notificationsRemovedFromChannelTemplate, postWebhookRetryCount, postWebhookUrl, preWebhookRetryCount, preWebhookUrl, reachabilityEnabled, readStatusEnabled, typingIndicatorTimeout, webhookFilters, webhookMethod)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2ServiceApi apiInstance = new IpMessagingV2ServiceApi(defaultClient);
    String sid = "sid_example"; // String | 
    Integer consumptionReportInterval = 56; // Integer | 
    String defaultChannelCreatorRoleSid = "defaultChannelCreatorRoleSid_example"; // String | 
    String defaultChannelRoleSid = "defaultChannelRoleSid_example"; // String | 
    String defaultServiceRoleSid = "defaultServiceRoleSid_example"; // String | 
    String friendlyName = "friendlyName_example"; // String | 
    Integer limitsChannelMembers = 56; // Integer | 
    Integer limitsUserChannels = 56; // Integer | 
    String mediaCompatibilityMessage = "mediaCompatibilityMessage_example"; // String | 
    Boolean notificationsAddedToChannelEnabled = true; // Boolean | 
    String notificationsAddedToChannelSound = "notificationsAddedToChannelSound_example"; // String | 
    String notificationsAddedToChannelTemplate = "notificationsAddedToChannelTemplate_example"; // String | 
    Boolean notificationsInvitedToChannelEnabled = true; // Boolean | 
    String notificationsInvitedToChannelSound = "notificationsInvitedToChannelSound_example"; // String | 
    String notificationsInvitedToChannelTemplate = "notificationsInvitedToChannelTemplate_example"; // String | 
    Boolean notificationsLogEnabled = true; // Boolean | 
    Boolean notificationsNewMessageBadgeCountEnabled = true; // Boolean | 
    Boolean notificationsNewMessageEnabled = true; // Boolean | 
    String notificationsNewMessageSound = "notificationsNewMessageSound_example"; // String | 
    String notificationsNewMessageTemplate = "notificationsNewMessageTemplate_example"; // String | 
    Boolean notificationsRemovedFromChannelEnabled = true; // Boolean | 
    String notificationsRemovedFromChannelSound = "notificationsRemovedFromChannelSound_example"; // String | 
    String notificationsRemovedFromChannelTemplate = "notificationsRemovedFromChannelTemplate_example"; // String | 
    Integer postWebhookRetryCount = 56; // Integer | 
    URI postWebhookUrl = new URI(); // URI | 
    Integer preWebhookRetryCount = 56; // Integer | 
    URI preWebhookUrl = new URI(); // URI | 
    Boolean reachabilityEnabled = true; // Boolean | 
    Boolean readStatusEnabled = true; // Boolean | 
    Integer typingIndicatorTimeout = 56; // Integer | 
    List<String> webhookFilters = Arrays.asList(); // List<String> | 
    String webhookMethod = "HEAD"; // String | 
    try {
      IpMessagingV2Service result = apiInstance.updateService(sid, consumptionReportInterval, defaultChannelCreatorRoleSid, defaultChannelRoleSid, defaultServiceRoleSid, friendlyName, limitsChannelMembers, limitsUserChannels, mediaCompatibilityMessage, notificationsAddedToChannelEnabled, notificationsAddedToChannelSound, notificationsAddedToChannelTemplate, notificationsInvitedToChannelEnabled, notificationsInvitedToChannelSound, notificationsInvitedToChannelTemplate, notificationsLogEnabled, notificationsNewMessageBadgeCountEnabled, notificationsNewMessageEnabled, notificationsNewMessageSound, notificationsNewMessageTemplate, notificationsRemovedFromChannelEnabled, notificationsRemovedFromChannelSound, notificationsRemovedFromChannelTemplate, postWebhookRetryCount, postWebhookUrl, preWebhookRetryCount, preWebhookUrl, reachabilityEnabled, readStatusEnabled, typingIndicatorTimeout, webhookFilters, webhookMethod);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2ServiceApi#updateService");
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
| **mediaCompatibilityMessage** | **String**|  | [optional] |
| **notificationsAddedToChannelEnabled** | **Boolean**|  | [optional] |
| **notificationsAddedToChannelSound** | **String**|  | [optional] |
| **notificationsAddedToChannelTemplate** | **String**|  | [optional] |
| **notificationsInvitedToChannelEnabled** | **Boolean**|  | [optional] |
| **notificationsInvitedToChannelSound** | **String**|  | [optional] |
| **notificationsInvitedToChannelTemplate** | **String**|  | [optional] |
| **notificationsLogEnabled** | **Boolean**|  | [optional] |
| **notificationsNewMessageBadgeCountEnabled** | **Boolean**|  | [optional] |
| **notificationsNewMessageEnabled** | **Boolean**|  | [optional] |
| **notificationsNewMessageSound** | **String**|  | [optional] |
| **notificationsNewMessageTemplate** | **String**|  | [optional] |
| **notificationsRemovedFromChannelEnabled** | **Boolean**|  | [optional] |
| **notificationsRemovedFromChannelSound** | **String**|  | [optional] |
| **notificationsRemovedFromChannelTemplate** | **String**|  | [optional] |
| **postWebhookRetryCount** | **Integer**|  | [optional] |
| **postWebhookUrl** | **URI**|  | [optional] |
| **preWebhookRetryCount** | **Integer**|  | [optional] |
| **preWebhookUrl** | **URI**|  | [optional] |
| **reachabilityEnabled** | **Boolean**|  | [optional] |
| **readStatusEnabled** | **Boolean**|  | [optional] |
| **typingIndicatorTimeout** | **Integer**|  | [optional] |
| **webhookFilters** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **webhookMethod** | **String**|  | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |

### Return type

[**IpMessagingV2Service**](IpMessagingV2Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

