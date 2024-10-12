# ChatV2ChannelApi

All URIs are relative to *https://chat.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createChannel**](ChatV2ChannelApi.md#createChannel) | **POST** /v2/Services/{ServiceSid}/Channels |  |
| [**deleteChannel**](ChatV2ChannelApi.md#deleteChannel) | **DELETE** /v2/Services/{ServiceSid}/Channels/{Sid} |  |
| [**fetchChannel**](ChatV2ChannelApi.md#fetchChannel) | **GET** /v2/Services/{ServiceSid}/Channels/{Sid} |  |
| [**listChannel**](ChatV2ChannelApi.md#listChannel) | **GET** /v2/Services/{ServiceSid}/Channels |  |
| [**updateChannel**](ChatV2ChannelApi.md#updateChannel) | **POST** /v2/Services/{ServiceSid}/Channels/{Sid} |  |


<a id="createChannel"></a>
# **createChannel**
> ChatV2ServiceChannel createChannel(serviceSid, xTwilioWebhookEnabled, attributes, createdBy, dateCreated, dateUpdated, friendlyName, type, uniqueName)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2ChannelApi apiInstance = new ChatV2ChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the Channel resource under.
    ChannelEnumWebhookEnabledType xTwilioWebhookEnabled = ChannelEnumWebhookEnabledType.fromValue("true"); // ChannelEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | A valid JSON string that contains application-specific data.
    String createdBy = "createdBy_example"; // String | The `identity` of the User that created the channel. Default is: `system`.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service.  Note that this should only be used in cases where a Channel is being recreated from a backup/separate source.
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated. The default value is `null`. Note that this parameter should only be used in cases where a Channel is being recreated from a backup/separate source  and where a Message was previously updated.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the new resource. It can be up to 64 characters long.
    ChannelEnumChannelType type = ChannelEnumChannelType.fromValue("public"); // ChannelEnumChannelType | 
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the Channel resource's `sid` in the URL. This value must be 64 characters or less in length and be unique within the Service.
    try {
      ChatV2ServiceChannel result = apiInstance.createChannel(serviceSid, xTwilioWebhookEnabled, attributes, createdBy, dateCreated, dateUpdated, friendlyName, type, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2ChannelApi#createChannel");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to create the Channel resource under. | |
| **xTwilioWebhookEnabled** | **ChannelEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| A valid JSON string that contains application-specific data. | [optional] |
| **createdBy** | **String**| The &#x60;identity&#x60; of the User that created the channel. Default is: &#x60;system&#x60;. | [optional] |
| **dateCreated** | **OffsetDateTime**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service.  Note that this should only be used in cases where a Channel is being recreated from a backup/separate source. | [optional] |
| **dateUpdated** | **OffsetDateTime**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated. The default value is &#x60;null&#x60;. Note that this parameter should only be used in cases where a Channel is being recreated from a backup/separate source  and where a Message was previously updated. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the new resource. It can be up to 64 characters long. | [optional] |
| **type** | **ChannelEnumChannelType**|  | [optional] [enum: public, private] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the Channel resource&#39;s &#x60;sid&#x60; in the URL. This value must be 64 characters or less in length and be unique within the Service. | [optional] |

### Return type

[**ChatV2ServiceChannel**](ChatV2ServiceChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteChannel"></a>
# **deleteChannel**
> deleteChannel(serviceSid, sid, xTwilioWebhookEnabled)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2ChannelApi apiInstance = new ChatV2ChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the resource from.
    String sid = "sid_example"; // String | The SID of the Channel resource to delete.  This value can be either the `sid` or the `unique_name` of the Channel resource to delete.
    ChannelEnumWebhookEnabledType xTwilioWebhookEnabled = ChannelEnumWebhookEnabledType.fromValue("true"); // ChannelEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    try {
      apiInstance.deleteChannel(serviceSid, sid, xTwilioWebhookEnabled);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2ChannelApi#deleteChannel");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to delete the resource from. | |
| **sid** | **String**| The SID of the Channel resource to delete.  This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the Channel resource to delete. | |
| **xTwilioWebhookEnabled** | **ChannelEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |

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

<a id="fetchChannel"></a>
# **fetchChannel**
> ChatV2ServiceChannel fetchChannel(serviceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2ChannelApi apiInstance = new ChatV2ChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the Channel resource from.
    String sid = "sid_example"; // String | The SID of the Channel resource to fetch. This value can be either the `sid` or the `unique_name` of the Channel resource to fetch.
    try {
      ChatV2ServiceChannel result = apiInstance.fetchChannel(serviceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2ChannelApi#fetchChannel");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to fetch the Channel resource from. | |
| **sid** | **String**| The SID of the Channel resource to fetch. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the Channel resource to fetch. | |

### Return type

[**ChatV2ServiceChannel**](ChatV2ServiceChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listChannel"></a>
# **listChannel**
> ListChannelResponse listChannel(serviceSid, type, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2ChannelApi apiInstance = new ChatV2ChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Channel resources from.
    List<ChannelEnumChannelType> type = Arrays.asList(); // List<ChannelEnumChannelType> | The visibility of the Channels to read. Can be: `public` or `private` and defaults to `public`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListChannelResponse result = apiInstance.listChannel(serviceSid, type, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2ChannelApi#listChannel");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Channel resources from. | |
| **type** | [**List&lt;ChannelEnumChannelType&gt;**](ChannelEnumChannelType.md)| The visibility of the Channels to read. Can be: &#x60;public&#x60; or &#x60;private&#x60; and defaults to &#x60;public&#x60;. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListChannelResponse**](ListChannelResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateChannel"></a>
# **updateChannel**
> ChatV2ServiceChannel updateChannel(serviceSid, sid, xTwilioWebhookEnabled, attributes, createdBy, dateCreated, dateUpdated, friendlyName, uniqueName)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChatV2ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ChatV2ChannelApi apiInstance = new ChatV2ChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the Channel resource in.
    String sid = "sid_example"; // String | The SID of the Channel resource to update. This value can be either the `sid` or the `unique_name` of the Channel resource to update.
    ChannelEnumWebhookEnabledType xTwilioWebhookEnabled = ChannelEnumWebhookEnabledType.fromValue("true"); // ChannelEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | A valid JSON string that contains application-specific data.
    String createdBy = "createdBy_example"; // String | The `identity` of the User that created the channel. Default is: `system`.
    OffsetDateTime dateCreated = OffsetDateTime.now(); // OffsetDateTime | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service.  Note that this should only be used in cases where a Channel is being recreated from a backup/separate source.
    OffsetDateTime dateUpdated = OffsetDateTime.now(); // OffsetDateTime | The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the resource. It can be up to 256 characters long.
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL. This value must be 256 characters or less in length and unique within the Service.
    try {
      ChatV2ServiceChannel result = apiInstance.updateChannel(serviceSid, sid, xTwilioWebhookEnabled, attributes, createdBy, dateCreated, dateUpdated, friendlyName, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChatV2ChannelApi#updateChannel");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the Channel resource in. | |
| **sid** | **String**| The SID of the Channel resource to update. This value can be either the &#x60;sid&#x60; or the &#x60;unique_name&#x60; of the Channel resource to update. | |
| **xTwilioWebhookEnabled** | **ChannelEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| A valid JSON string that contains application-specific data. | [optional] |
| **createdBy** | **String**| The &#x60;identity&#x60; of the User that created the channel. Default is: &#x60;system&#x60;. | [optional] |
| **dateCreated** | **OffsetDateTime**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service.  Note that this should only be used in cases where a Channel is being recreated from a backup/separate source. | [optional] |
| **dateUpdated** | **OffsetDateTime**| The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 256 characters long. | [optional] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource&#39;s &#x60;sid&#x60; in the URL. This value must be 256 characters or less in length and unique within the Service. | [optional] |

### Return type

[**ChatV2ServiceChannel**](ChatV2ServiceChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

