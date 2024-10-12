# FlexV1ChannelApi

All URIs are relative to *https://flex-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createChannel**](FlexV1ChannelApi.md#createChannel) | **POST** /v1/Channels |  |
| [**deleteChannel**](FlexV1ChannelApi.md#deleteChannel) | **DELETE** /v1/Channels/{Sid} |  |
| [**fetchChannel**](FlexV1ChannelApi.md#fetchChannel) | **GET** /v1/Channels/{Sid} |  |
| [**listChannel**](FlexV1ChannelApi.md#listChannel) | **GET** /v1/Channels |  |


<a id="createChannel"></a>
# **createChannel**
> FlexV1Channel createChannel(chatFriendlyName, chatUserFriendlyName, flexFlowSid, identity, chatUniqueName, longLived, preEngagementData, target, taskAttributes, taskSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1ChannelApi apiInstance = new FlexV1ChannelApi(defaultClient);
    String chatFriendlyName = "chatFriendlyName_example"; // String | The chat channel's friendly name.
    String chatUserFriendlyName = "chatUserFriendlyName_example"; // String | The chat participant's friendly name.
    String flexFlowSid = "flexFlowSid_example"; // String | The SID of the Flex Flow.
    String identity = "identity_example"; // String | The `identity` value that uniquely identifies the new resource's chat User.
    String chatUniqueName = "chatUniqueName_example"; // String | The chat channel's unique name.
    Boolean longLived = true; // Boolean | Whether to create the channel as long-lived.
    String preEngagementData = "preEngagementData_example"; // String | The pre-engagement data.
    String target = "target_example"; // String | The Target Contact Identity, for example the phone number of an SMS.
    String taskAttributes = "taskAttributes_example"; // String | The Task attributes to be added for the TaskRouter Task.
    String taskSid = "taskSid_example"; // String | The SID of the TaskRouter Task. Only valid when integration type is `task`. `null` for integration types `studio` & `external`
    try {
      FlexV1Channel result = apiInstance.createChannel(chatFriendlyName, chatUserFriendlyName, flexFlowSid, identity, chatUniqueName, longLived, preEngagementData, target, taskAttributes, taskSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1ChannelApi#createChannel");
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
| **chatFriendlyName** | **String**| The chat channel&#39;s friendly name. | |
| **chatUserFriendlyName** | **String**| The chat participant&#39;s friendly name. | |
| **flexFlowSid** | **String**| The SID of the Flex Flow. | |
| **identity** | **String**| The &#x60;identity&#x60; value that uniquely identifies the new resource&#39;s chat User. | |
| **chatUniqueName** | **String**| The chat channel&#39;s unique name. | [optional] |
| **longLived** | **Boolean**| Whether to create the channel as long-lived. | [optional] |
| **preEngagementData** | **String**| The pre-engagement data. | [optional] |
| **target** | **String**| The Target Contact Identity, for example the phone number of an SMS. | [optional] |
| **taskAttributes** | **String**| The Task attributes to be added for the TaskRouter Task. | [optional] |
| **taskSid** | **String**| The SID of the TaskRouter Task. Only valid when integration type is &#x60;task&#x60;. &#x60;null&#x60; for integration types &#x60;studio&#x60; &amp; &#x60;external&#x60; | [optional] |

### Return type

[**FlexV1Channel**](FlexV1Channel.md)

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
> deleteChannel(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1ChannelApi apiInstance = new FlexV1ChannelApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Flex chat channel resource to delete.
    try {
      apiInstance.deleteChannel(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1ChannelApi#deleteChannel");
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
| **sid** | **String**| The SID of the Flex chat channel resource to delete. | |

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
> FlexV1Channel fetchChannel(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1ChannelApi apiInstance = new FlexV1ChannelApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Flex chat channel resource to fetch.
    try {
      FlexV1Channel result = apiInstance.fetchChannel(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1ChannelApi#fetchChannel");
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
| **sid** | **String**| The SID of the Flex chat channel resource to fetch. | |

### Return type

[**FlexV1Channel**](FlexV1Channel.md)

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
> ListChannelResponse listChannel(pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1ChannelApi apiInstance = new FlexV1ChannelApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListChannelResponse result = apiInstance.listChannel(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1ChannelApi#listChannel");
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

