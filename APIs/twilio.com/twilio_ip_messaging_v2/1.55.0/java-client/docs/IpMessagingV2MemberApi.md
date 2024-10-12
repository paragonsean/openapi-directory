# IpMessagingV2MemberApi

All URIs are relative to *https://ip-messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createMember**](IpMessagingV2MemberApi.md#createMember) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Members |  |
| [**deleteMember**](IpMessagingV2MemberApi.md#deleteMember) | **DELETE** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Members/{Sid} |  |
| [**fetchMember**](IpMessagingV2MemberApi.md#fetchMember) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Members/{Sid} |  |
| [**listMember**](IpMessagingV2MemberApi.md#listMember) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Members |  |
| [**updateMember**](IpMessagingV2MemberApi.md#updateMember) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Members/{Sid} |  |


<a id="createMember"></a>
# **createMember**
> IpMessagingV2ServiceChannelMember createMember(serviceSid, channelSid, identity, xTwilioWebhookEnabled, attributes, dateCreated, dateUpdated, lastConsumedMessageIndex, lastConsumptionTimestamp, roleSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2MemberApi apiInstance = new IpMessagingV2MemberApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String channelSid = "channelSid_example"; // String | 
    String identity = "identity_example"; // String | 
    MemberEnumWebhookEnabledType xTwilioWebhookEnabled = MemberEnumWebhookEnabledType.fromValue("true"); // MemberEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | 
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | 
    Integer lastConsumedMessageIndex = 56; // Integer | 
    OffsetDateTime lastConsumptionTimestamp = OffsetDateTime.now(); // OffsetDateTime | 
    String roleSid = "roleSid_example"; // String | 
    try {
      IpMessagingV2ServiceChannelMember result = apiInstance.createMember(serviceSid, channelSid, identity, xTwilioWebhookEnabled, attributes, dateCreated, dateUpdated, lastConsumedMessageIndex, lastConsumptionTimestamp, roleSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2MemberApi#createMember");
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
| **channelSid** | **String**|  | |
| **identity** | **String**|  | |
| **xTwilioWebhookEnabled** | **MemberEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**|  | [optional] |
| **dateCreated** | **OffsetDateTime**|  | [optional] |
| **dateUpdated** | **OffsetDateTime**|  | [optional] |
| **lastConsumedMessageIndex** | **Integer**|  | [optional] |
| **lastConsumptionTimestamp** | **OffsetDateTime**|  | [optional] |
| **roleSid** | **String**|  | [optional] |

### Return type

[**IpMessagingV2ServiceChannelMember**](IpMessagingV2ServiceChannelMember.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteMember"></a>
# **deleteMember**
> deleteMember(serviceSid, channelSid, sid, xTwilioWebhookEnabled)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2MemberApi apiInstance = new IpMessagingV2MemberApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String channelSid = "channelSid_example"; // String | 
    String sid = "sid_example"; // String | 
    MemberEnumWebhookEnabledType xTwilioWebhookEnabled = MemberEnumWebhookEnabledType.fromValue("true"); // MemberEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    try {
      apiInstance.deleteMember(serviceSid, channelSid, sid, xTwilioWebhookEnabled);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2MemberApi#deleteMember");
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
| **channelSid** | **String**|  | |
| **sid** | **String**|  | |
| **xTwilioWebhookEnabled** | **MemberEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |

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

<a id="fetchMember"></a>
# **fetchMember**
> IpMessagingV2ServiceChannelMember fetchMember(serviceSid, channelSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2MemberApi apiInstance = new IpMessagingV2MemberApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String channelSid = "channelSid_example"; // String | 
    String sid = "sid_example"; // String | 
    try {
      IpMessagingV2ServiceChannelMember result = apiInstance.fetchMember(serviceSid, channelSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2MemberApi#fetchMember");
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
| **channelSid** | **String**|  | |
| **sid** | **String**|  | |

### Return type

[**IpMessagingV2ServiceChannelMember**](IpMessagingV2ServiceChannelMember.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listMember"></a>
# **listMember**
> ListMemberResponse listMember(serviceSid, channelSid, identity, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2MemberApi apiInstance = new IpMessagingV2MemberApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String channelSid = "channelSid_example"; // String | 
    List<String> identity = Arrays.asList(); // List<String> | 
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListMemberResponse result = apiInstance.listMember(serviceSid, channelSid, identity, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2MemberApi#listMember");
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
| **channelSid** | **String**|  | |
| **identity** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListMemberResponse**](ListMemberResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateMember"></a>
# **updateMember**
> IpMessagingV2ServiceChannelMember updateMember(serviceSid, channelSid, sid, xTwilioWebhookEnabled, attributes, dateCreated, dateUpdated, lastConsumedMessageIndex, lastConsumptionTimestamp, roleSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2MemberApi apiInstance = new IpMessagingV2MemberApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String channelSid = "channelSid_example"; // String | 
    String sid = "sid_example"; // String | 
    MemberEnumWebhookEnabledType xTwilioWebhookEnabled = MemberEnumWebhookEnabledType.fromValue("true"); // MemberEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | 
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | 
    Integer lastConsumedMessageIndex = 56; // Integer | 
    OffsetDateTime lastConsumptionTimestamp = OffsetDateTime.now(); // OffsetDateTime | 
    String roleSid = "roleSid_example"; // String | 
    try {
      IpMessagingV2ServiceChannelMember result = apiInstance.updateMember(serviceSid, channelSid, sid, xTwilioWebhookEnabled, attributes, dateCreated, dateUpdated, lastConsumedMessageIndex, lastConsumptionTimestamp, roleSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2MemberApi#updateMember");
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
| **channelSid** | **String**|  | |
| **sid** | **String**|  | |
| **xTwilioWebhookEnabled** | **MemberEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**|  | [optional] |
| **dateCreated** | **OffsetDateTime**|  | [optional] |
| **dateUpdated** | **OffsetDateTime**|  | [optional] |
| **lastConsumedMessageIndex** | **Integer**|  | [optional] |
| **lastConsumptionTimestamp** | **OffsetDateTime**|  | [optional] |
| **roleSid** | **String**|  | [optional] |

### Return type

[**IpMessagingV2ServiceChannelMember**](IpMessagingV2ServiceChannelMember.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

