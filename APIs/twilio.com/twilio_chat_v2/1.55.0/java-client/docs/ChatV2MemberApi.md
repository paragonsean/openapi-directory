# ChatV2MemberApi

All URIs are relative to *https://chat.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createMember**](ChatV2MemberApi.md#createMember) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Members |  |
| [**deleteMember**](ChatV2MemberApi.md#deleteMember) | **DELETE** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Members/{Sid} |  |
| [**fetchMember**](ChatV2MemberApi.md#fetchMember) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Members/{Sid} |  |
| [**listMember**](ChatV2MemberApi.md#listMember) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Members |  |
| [**updateMember**](ChatV2MemberApi.md#updateMember) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Members/{Sid} |  |


<a id="createMember"></a>
# **createMember**
> ChatV2ServiceChannelMember createMember(serviceSid, channelSid, identity, xTwilioWebhookEnabled, attributes, dateCreated, dateUpdated, lastConsumedMessageIndex, lastConsumptionTimestamp, roleSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2MemberApi apiInstance = new ChatV2MemberApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the Member resource under.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the new Member resource belongs to. This value can be the Channel resource's `sid` or `unique_name`.
    String identity = "identity_example"; // String | The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/chat/rest/service-resource). See [access tokens](https://www.twilio.com/docs/chat/create-tokens) for more info.
    MemberEnumWebhookEnabledType xTwilioWebhookEnabled = MemberEnumWebhookEnabledType.fromValue("true"); // MemberEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | A valid JSON string that contains application-specific data.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service.  Note that this parameter should only be used when a Member is being recreated from a backup/separate source.
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated. The default value is `null`. Note that this parameter should only be used when a Member is being recreated from a backup/separate source and where a Member was previously updated.
    Integer lastConsumedMessageIndex = 56; // Integer | The index of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) in the [Channel](https://www.twilio.com/docs/chat/channels) that the Member has read. This parameter should only be used when recreating a Member from a backup/separate source.
    OffsetDateTime lastConsumptionTimestamp = OffsetDateTime.now(); // OffsetDateTime | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) read event for the Member within the [Channel](https://www.twilio.com/docs/chat/channels).
    String roleSid = "roleSid_example"; // String | The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) to assign to the member. The default roles are those specified on the [Service](https://www.twilio.com/docs/chat/rest/service-resource).
    try {
      ChatV2ServiceChannelMember result = apiInstance.createMember(serviceSid, channelSid, identity, xTwilioWebhookEnabled, attributes, dateCreated, dateUpdated, lastConsumedMessageIndex, lastConsumptionTimestamp, roleSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2MemberApi#createMember");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the Member resource under. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the new Member resource belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
| **identity** | **String**| The &#x60;identity&#x60; value that uniquely identifies the new resource&#39;s [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/chat/rest/service-resource). See [access tokens](https://www.twilio.com/docs/chat/create-tokens) for more info. | |
| **xTwilioWebhookEnabled** | **MemberEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| A valid JSON string that contains application-specific data. | [optional] |
| **dateCreated** | **OffsetDateTime**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service.  Note that this parameter should only be used when a Member is being recreated from a backup/separate source. | [optional] |
| **dateUpdated** | **OffsetDateTime**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated. The default value is &#x60;null&#x60;. Note that this parameter should only be used when a Member is being recreated from a backup/separate source and where a Member was previously updated. | [optional] |
| **lastConsumedMessageIndex** | **Integer**| The index of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) in the [Channel](https://www.twilio.com/docs/chat/channels) that the Member has read. This parameter should only be used when recreating a Member from a backup/separate source. | [optional] |
| **lastConsumptionTimestamp** | **OffsetDateTime**| The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) read event for the Member within the [Channel](https://www.twilio.com/docs/chat/channels). | [optional] |
| **roleSid** | **String**| The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) to assign to the member. The default roles are those specified on the [Service](https://www.twilio.com/docs/chat/rest/service-resource). | [optional] |

### Return type

[**ChatV2ServiceChannelMember**](ChatV2ServiceChannelMember.md)

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
import org.openapitools.client.api.ChatV2MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2MemberApi apiInstance = new ChatV2MemberApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the Member resource from.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Member resource to delete belongs to. This value can be the Channel resource's `sid` or `unique_name`.
    String sid = "sid_example"; // String | The SID of the Member resource to delete. This value can be either the Member's `sid` or its `identity` value.
    MemberEnumWebhookEnabledType xTwilioWebhookEnabled = MemberEnumWebhookEnabledType.fromValue("true"); // MemberEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    try {
      apiInstance.deleteMember(serviceSid, channelSid, sid, xTwilioWebhookEnabled);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2MemberApi#deleteMember");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the Member resource from. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Member resource to delete belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
| **sid** | **String**| The SID of the Member resource to delete. This value can be either the Member&#39;s &#x60;sid&#x60; or its &#x60;identity&#x60; value. | |
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
> ChatV2ServiceChannelMember fetchMember(serviceSid, channelSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2MemberApi apiInstance = new ChatV2MemberApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the Member resource from.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Member resource to fetch belongs to. This value can be the Channel resource's `sid` or `unique_name`.
    String sid = "sid_example"; // String | The SID of the Member resource to fetch. This value can be either the Member's `sid` or its `identity` value.
    try {
      ChatV2ServiceChannelMember result = apiInstance.fetchMember(serviceSid, channelSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2MemberApi#fetchMember");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the Member resource from. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Member resource to fetch belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
| **sid** | **String**| The SID of the Member resource to fetch. This value can be either the Member&#39;s &#x60;sid&#x60; or its &#x60;identity&#x60; value. | |

### Return type

[**ChatV2ServiceChannelMember**](ChatV2ServiceChannelMember.md)

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
import org.openapitools.client.api.ChatV2MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2MemberApi apiInstance = new ChatV2MemberApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Member resources from.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Member resources to read belong to. This value can be the Channel resource's `sid` or `unique_name`.
    List<String> identity = Arrays.asList(); // List<String> | The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s `identity` value of the Member resources to read. See [access tokens](https://www.twilio.com/docs/chat/create-tokens) for more details.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListMemberResponse result = apiInstance.listMember(serviceSid, channelSid, identity, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2MemberApi#listMember");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Member resources from. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Member resources to read belong to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
| **identity** | [**List&lt;String&gt;**](String.md)| The [User](https://www.twilio.com/docs/chat/rest/user-resource)&#39;s &#x60;identity&#x60; value of the Member resources to read. See [access tokens](https://www.twilio.com/docs/chat/create-tokens) for more details. | [optional] |
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
> ChatV2ServiceChannelMember updateMember(serviceSid, channelSid, sid, xTwilioWebhookEnabled, attributes, dateCreated, dateUpdated, lastConsumedMessageIndex, lastConsumptionTimestamp, roleSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2MemberApi apiInstance = new ChatV2MemberApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the Member resource in.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Member resource to update belongs to. This value can be the Channel resource's `sid` or `unique_name`.
    String sid = "sid_example"; // String | The SID of the Member resource to update. This value can be either the Member's `sid` or its `identity` value.
    MemberEnumWebhookEnabledType xTwilioWebhookEnabled = MemberEnumWebhookEnabledType.fromValue("true"); // MemberEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | A valid JSON string that contains application-specific data.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service.  Note that this parameter should only be used when a Member is being recreated from a backup/separate source.
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated.
    Integer lastConsumedMessageIndex = 56; // Integer | The index of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) that the Member has read within the [Channel](https://www.twilio.com/docs/chat/channels).
    OffsetDateTime lastConsumptionTimestamp = OffsetDateTime.now(); // OffsetDateTime | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) read event for the Member within the [Channel](https://www.twilio.com/docs/chat/channels).
    String roleSid = "roleSid_example"; // String | The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) to assign to the member. The default roles are those specified on the [Service](https://www.twilio.com/docs/chat/rest/service-resource).
    try {
      ChatV2ServiceChannelMember result = apiInstance.updateMember(serviceSid, channelSid, sid, xTwilioWebhookEnabled, attributes, dateCreated, dateUpdated, lastConsumedMessageIndex, lastConsumptionTimestamp, roleSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2MemberApi#updateMember");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the Member resource in. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Member resource to update belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
| **sid** | **String**| The SID of the Member resource to update. This value can be either the Member&#39;s &#x60;sid&#x60; or its &#x60;identity&#x60; value. | |
| **xTwilioWebhookEnabled** | **MemberEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| A valid JSON string that contains application-specific data. | [optional] |
| **dateCreated** | **OffsetDateTime**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service.  Note that this parameter should only be used when a Member is being recreated from a backup/separate source. | [optional] |
| **dateUpdated** | **OffsetDateTime**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated. | [optional] |
| **lastConsumedMessageIndex** | **Integer**| The index of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) that the Member has read within the [Channel](https://www.twilio.com/docs/chat/channels). | [optional] |
| **lastConsumptionTimestamp** | **OffsetDateTime**| The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) timestamp of the last [Message](https://www.twilio.com/docs/chat/rest/message-resource) read event for the Member within the [Channel](https://www.twilio.com/docs/chat/channels). | [optional] |
| **roleSid** | **String**| The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) to assign to the member. The default roles are those specified on the [Service](https://www.twilio.com/docs/chat/rest/service-resource). | [optional] |

### Return type

[**ChatV2ServiceChannelMember**](ChatV2ServiceChannelMember.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

