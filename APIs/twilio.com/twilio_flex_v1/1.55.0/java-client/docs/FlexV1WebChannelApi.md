# FlexV1WebChannelApi

All URIs are relative to *https://flex-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWebChannel**](FlexV1WebChannelApi.md#createWebChannel) | **POST** /v1/WebChannels |  |
| [**deleteWebChannel**](FlexV1WebChannelApi.md#deleteWebChannel) | **DELETE** /v1/WebChannels/{Sid} |  |
| [**fetchWebChannel**](FlexV1WebChannelApi.md#fetchWebChannel) | **GET** /v1/WebChannels/{Sid} |  |
| [**listWebChannel**](FlexV1WebChannelApi.md#listWebChannel) | **GET** /v1/WebChannels |  |
| [**updateWebChannel**](FlexV1WebChannelApi.md#updateWebChannel) | **POST** /v1/WebChannels/{Sid} |  |


<a id="createWebChannel"></a>
# **createWebChannel**
> FlexV1WebChannel createWebChannel(chatFriendlyName, customerFriendlyName, flexFlowSid, identity, chatUniqueName, preEngagementData)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1WebChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1WebChannelApi apiInstance = new FlexV1WebChannelApi(defaultClient);
    String chatFriendlyName = "chatFriendlyName_example"; // String | The chat channel's friendly name.
    String customerFriendlyName = "customerFriendlyName_example"; // String | The chat participant's friendly name.
    String flexFlowSid = "flexFlowSid_example"; // String | The SID of the Flex Flow.
    String identity = "identity_example"; // String | The chat identity.
    String chatUniqueName = "chatUniqueName_example"; // String | The chat channel's unique name.
    String preEngagementData = "preEngagementData_example"; // String | The pre-engagement data.
    try {
      FlexV1WebChannel result = apiInstance.createWebChannel(chatFriendlyName, customerFriendlyName, flexFlowSid, identity, chatUniqueName, preEngagementData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1WebChannelApi#createWebChannel");
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
| **customerFriendlyName** | **String**| The chat participant&#39;s friendly name. | |
| **flexFlowSid** | **String**| The SID of the Flex Flow. | |
| **identity** | **String**| The chat identity. | |
| **chatUniqueName** | **String**| The chat channel&#39;s unique name. | [optional] |
| **preEngagementData** | **String**| The pre-engagement data. | [optional] |

### Return type

[**FlexV1WebChannel**](FlexV1WebChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteWebChannel"></a>
# **deleteWebChannel**
> deleteWebChannel(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1WebChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1WebChannelApi apiInstance = new FlexV1WebChannelApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the WebChannel resource to delete.
    try {
      apiInstance.deleteWebChannel(sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1WebChannelApi#deleteWebChannel");
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
| **sid** | **String**| The SID of the WebChannel resource to delete. | |

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

<a id="fetchWebChannel"></a>
# **fetchWebChannel**
> FlexV1WebChannel fetchWebChannel(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1WebChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1WebChannelApi apiInstance = new FlexV1WebChannelApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the WebChannel resource to fetch.
    try {
      FlexV1WebChannel result = apiInstance.fetchWebChannel(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1WebChannelApi#fetchWebChannel");
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
| **sid** | **String**| The SID of the WebChannel resource to fetch. | |

### Return type

[**FlexV1WebChannel**](FlexV1WebChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listWebChannel"></a>
# **listWebChannel**
> ListWebChannelResponse listWebChannel(pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1WebChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1WebChannelApi apiInstance = new FlexV1WebChannelApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListWebChannelResponse result = apiInstance.listWebChannel(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1WebChannelApi#listWebChannel");
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

[**ListWebChannelResponse**](ListWebChannelResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateWebChannel"></a>
# **updateWebChannel**
> FlexV1WebChannel updateWebChannel(sid, chatStatus, postEngagementData)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1WebChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1WebChannelApi apiInstance = new FlexV1WebChannelApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the WebChannel resource to update.
    WebChannelEnumChatStatus chatStatus = WebChannelEnumChatStatus.fromValue("inactive"); // WebChannelEnumChatStatus | 
    String postEngagementData = "postEngagementData_example"; // String | The post-engagement data.
    try {
      FlexV1WebChannel result = apiInstance.updateWebChannel(sid, chatStatus, postEngagementData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1WebChannelApi#updateWebChannel");
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
| **sid** | **String**| The SID of the WebChannel resource to update. | |
| **chatStatus** | **WebChannelEnumChatStatus**|  | [optional] [enum: inactive] |
| **postEngagementData** | **String**| The post-engagement data. | [optional] |

### Return type

[**FlexV1WebChannel**](FlexV1WebChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

