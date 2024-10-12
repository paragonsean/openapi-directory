# ChatV2InviteApi

All URIs are relative to *https://chat.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInvite**](ChatV2InviteApi.md#createInvite) | **POST** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Invites |  |
| [**deleteInvite**](ChatV2InviteApi.md#deleteInvite) | **DELETE** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Invites/{Sid} |  |
| [**fetchInvite**](ChatV2InviteApi.md#fetchInvite) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Invites/{Sid} |  |
| [**listInvite**](ChatV2InviteApi.md#listInvite) | **GET** /v2/Services/{ServiceSid}/Channels/{ChannelSid}/Invites |  |


<a id="createInvite"></a>
# **createInvite**
> ChatV2ServiceChannelInvite createInvite(serviceSid, channelSid, identity, roleSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2InviteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2InviteApi apiInstance = new ChatV2InviteApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the Invite resource under.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the new Invite resource belongs to. This value can be the Channel resource's `sid` or `unique_name`.
    String identity = "identity_example"; // String | The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/chat/rest/service-resource). See [access tokens](https://www.twilio.com/docs/chat/create-tokens) for more info.
    String roleSid = "roleSid_example"; // String | The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) assigned to the new member.
    try {
      ChatV2ServiceChannelInvite result = apiInstance.createInvite(serviceSid, channelSid, identity, roleSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2InviteApi#createInvite");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the Invite resource under. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the new Invite resource belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
| **identity** | **String**| The &#x60;identity&#x60; value that uniquely identifies the new resource&#39;s [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/chat/rest/service-resource). See [access tokens](https://www.twilio.com/docs/chat/create-tokens) for more info. | |
| **roleSid** | **String**| The SID of the [Role](https://www.twilio.com/docs/chat/rest/role-resource) assigned to the new member. | [optional] |

### Return type

[**ChatV2ServiceChannelInvite**](ChatV2ServiceChannelInvite.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteInvite"></a>
# **deleteInvite**
> deleteInvite(serviceSid, channelSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2InviteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2InviteApi apiInstance = new ChatV2InviteApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the Invite resource from.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Invite resource to delete belongs to. This value can be the Channel resource's `sid` or `unique_name`.
    String sid = "sid_example"; // String | The SID of the Invite resource to delete.
    try {
      apiInstance.deleteInvite(serviceSid, channelSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2InviteApi#deleteInvite");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the Invite resource from. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Invite resource to delete belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
| **sid** | **String**| The SID of the Invite resource to delete. | |

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

<a id="fetchInvite"></a>
# **fetchInvite**
> ChatV2ServiceChannelInvite fetchInvite(serviceSid, channelSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2InviteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2InviteApi apiInstance = new ChatV2InviteApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the Invite resource from.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Invite resource to fetch belongs to. This value can be the Channel resource's `sid` or `unique_name`.
    String sid = "sid_example"; // String | The SID of the Invite resource to fetch.
    try {
      ChatV2ServiceChannelInvite result = apiInstance.fetchInvite(serviceSid, channelSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2InviteApi#fetchInvite");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the Invite resource from. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Invite resource to fetch belongs to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
| **sid** | **String**| The SID of the Invite resource to fetch. | |

### Return type

[**ChatV2ServiceChannelInvite**](ChatV2ServiceChannelInvite.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listInvite"></a>
# **listInvite**
> ListInviteResponse listInvite(serviceSid, channelSid, identity, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2InviteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2InviteApi apiInstance = new ChatV2InviteApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Invite resources from.
    String channelSid = "channelSid_example"; // String | The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Invite resources to read belong to. This value can be the Channel resource's `sid` or `unique_name`.
    List<String> identity = Arrays.asList(); // List<String> | The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s `identity` value of the resources to read. See [access tokens](https://www.twilio.com/docs/chat/create-tokens) for more details.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListInviteResponse result = apiInstance.listInvite(serviceSid, channelSid, identity, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2InviteApi#listInvite");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Invite resources from. | |
| **channelSid** | **String**| The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Invite resources to read belong to. This value can be the Channel resource&#39;s &#x60;sid&#x60; or &#x60;unique_name&#x60;. | |
| **identity** | [**List&lt;String&gt;**](String.md)| The [User](https://www.twilio.com/docs/chat/rest/user-resource)&#39;s &#x60;identity&#x60; value of the resources to read. See [access tokens](https://www.twilio.com/docs/chat/create-tokens) for more details. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListInviteResponse**](ListInviteResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

