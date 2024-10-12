# IpMessagingV2UserChannelApi

All URIs are relative to *https://ip-messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteUserChannel**](IpMessagingV2UserChannelApi.md#deleteUserChannel) | **DELETE** /v2/Services/{ServiceSid}/Users/{UserSid}/Channels/{ChannelSid} |  |
| [**fetchUserChannel**](IpMessagingV2UserChannelApi.md#fetchUserChannel) | **GET** /v2/Services/{ServiceSid}/Users/{UserSid}/Channels/{ChannelSid} |  |
| [**listUserChannel**](IpMessagingV2UserChannelApi.md#listUserChannel) | **GET** /v2/Services/{ServiceSid}/Users/{UserSid}/Channels |  |
| [**updateUserChannel**](IpMessagingV2UserChannelApi.md#updateUserChannel) | **POST** /v2/Services/{ServiceSid}/Users/{UserSid}/Channels/{ChannelSid} |  |


<a id="deleteUserChannel"></a>
# **deleteUserChannel**
> deleteUserChannel(serviceSid, userSid, channelSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2UserChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2UserChannelApi apiInstance = new IpMessagingV2UserChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String userSid = "userSid_example"; // String | 
    String channelSid = "channelSid_example"; // String | 
    try {
      apiInstance.deleteUserChannel(serviceSid, userSid, channelSid);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2UserChannelApi#deleteUserChannel");
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
| **serviceSid** | **String**|  | |
| **userSid** | **String**|  | |
| **channelSid** | **String**|  | |

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

<a id="fetchUserChannel"></a>
# **fetchUserChannel**
> IpMessagingV2ServiceUserUserChannel fetchUserChannel(serviceSid, userSid, channelSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2UserChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2UserChannelApi apiInstance = new IpMessagingV2UserChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String userSid = "userSid_example"; // String | 
    String channelSid = "channelSid_example"; // String | 
    try {
      IpMessagingV2ServiceUserUserChannel result = apiInstance.fetchUserChannel(serviceSid, userSid, channelSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2UserChannelApi#fetchUserChannel");
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
| **serviceSid** | **String**|  | |
| **userSid** | **String**|  | |
| **channelSid** | **String**|  | |

### Return type

[**IpMessagingV2ServiceUserUserChannel**](IpMessagingV2ServiceUserUserChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listUserChannel"></a>
# **listUserChannel**
> ListUserChannelResponse listUserChannel(serviceSid, userSid, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2UserChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2UserChannelApi apiInstance = new IpMessagingV2UserChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String userSid = "userSid_example"; // String | 
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListUserChannelResponse result = apiInstance.listUserChannel(serviceSid, userSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2UserChannelApi#listUserChannel");
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
| **serviceSid** | **String**|  | |
| **userSid** | **String**|  | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListUserChannelResponse**](ListUserChannelResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateUserChannel"></a>
# **updateUserChannel**
> IpMessagingV2ServiceUserUserChannel updateUserChannel(serviceSid, userSid, channelSid, lastConsumedMessageIndex, lastConsumptionTimestamp, notificationLevel)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2UserChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2UserChannelApi apiInstance = new IpMessagingV2UserChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String userSid = "userSid_example"; // String | 
    String channelSid = "channelSid_example"; // String | 
    Integer lastConsumedMessageIndex = 56; // Integer | 
    OffsetDateTime lastConsumptionTimestamp = OffsetDateTime.now(); // OffsetDateTime | 
    UserChannelEnumNotificationLevel notificationLevel = UserChannelEnumNotificationLevel.fromValue("default"); // UserChannelEnumNotificationLevel | 
    try {
      IpMessagingV2ServiceUserUserChannel result = apiInstance.updateUserChannel(serviceSid, userSid, channelSid, lastConsumedMessageIndex, lastConsumptionTimestamp, notificationLevel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2UserChannelApi#updateUserChannel");
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
| **serviceSid** | **String**|  | |
| **userSid** | **String**|  | |
| **channelSid** | **String**|  | |
| **lastConsumedMessageIndex** | **Integer**|  | [optional] |
| **lastConsumptionTimestamp** | **OffsetDateTime**|  | [optional] |
| **notificationLevel** | **UserChannelEnumNotificationLevel**|  | [optional] [enum: default, muted] |

### Return type

[**IpMessagingV2ServiceUserUserChannel**](IpMessagingV2ServiceUserUserChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

