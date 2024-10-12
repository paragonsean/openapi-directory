# IpMessagingV1ChannelApi

All URIs are relative to *https://ip-messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createChannel**](IpMessagingV1ChannelApi.md#createChannel) | **POST** /v1/Services/{ServiceSid}/Channels |  |
| [**deleteChannel**](IpMessagingV1ChannelApi.md#deleteChannel) | **DELETE** /v1/Services/{ServiceSid}/Channels/{Sid} |  |
| [**fetchChannel**](IpMessagingV1ChannelApi.md#fetchChannel) | **GET** /v1/Services/{ServiceSid}/Channels/{Sid} |  |
| [**listChannel**](IpMessagingV1ChannelApi.md#listChannel) | **GET** /v1/Services/{ServiceSid}/Channels |  |
| [**updateChannel**](IpMessagingV1ChannelApi.md#updateChannel) | **POST** /v1/Services/{ServiceSid}/Channels/{Sid} |  |


<a id="createChannel"></a>
# **createChannel**
> IpMessagingV1ServiceChannel createChannel(serviceSid, attributes, friendlyName, type, uniqueName)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1ChannelApi apiInstance = new IpMessagingV1ChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String attributes = "attributes_example"; // String | 
    String friendlyName = "friendlyName_example"; // String | 
    ChannelEnumChannelType type = ChannelEnumChannelType.fromValue("public"); // ChannelEnumChannelType | 
    String uniqueName = "uniqueName_example"; // String | 
    try {
      IpMessagingV1ServiceChannel result = apiInstance.createChannel(serviceSid, attributes, friendlyName, type, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1ChannelApi#createChannel");
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
| **attributes** | **String**|  | [optional] |
| **friendlyName** | **String**|  | [optional] |
| **type** | **ChannelEnumChannelType**|  | [optional] [enum: public, private] |
| **uniqueName** | **String**|  | [optional] |

### Return type

[**IpMessagingV1ServiceChannel**](IpMessagingV1ServiceChannel.md)

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
> deleteChannel(serviceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1ChannelApi apiInstance = new IpMessagingV1ChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String sid = "sid_example"; // String | 
    try {
      apiInstance.deleteChannel(serviceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1ChannelApi#deleteChannel");
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

<a id="fetchChannel"></a>
# **fetchChannel**
> IpMessagingV1ServiceChannel fetchChannel(serviceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1ChannelApi apiInstance = new IpMessagingV1ChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String sid = "sid_example"; // String | 
    try {
      IpMessagingV1ServiceChannel result = apiInstance.fetchChannel(serviceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1ChannelApi#fetchChannel");
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
| **sid** | **String**|  | |

### Return type

[**IpMessagingV1ServiceChannel**](IpMessagingV1ServiceChannel.md)

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
import org.openapitools.client.api.IpMessagingV1ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1ChannelApi apiInstance = new IpMessagingV1ChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    List<ChannelEnumChannelType> type = Arrays.asList(); // List<ChannelEnumChannelType> | 
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListChannelResponse result = apiInstance.listChannel(serviceSid, type, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1ChannelApi#listChannel");
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
| **type** | [**List&lt;ChannelEnumChannelType&gt;**](ChannelEnumChannelType.md)|  | [optional] |
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
> IpMessagingV1ServiceChannel updateChannel(serviceSid, sid, attributes, friendlyName, uniqueName)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV1ChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV1ChannelApi apiInstance = new IpMessagingV1ChannelApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String sid = "sid_example"; // String | 
    String attributes = "attributes_example"; // String | 
    String friendlyName = "friendlyName_example"; // String | 
    String uniqueName = "uniqueName_example"; // String | 
    try {
      IpMessagingV1ServiceChannel result = apiInstance.updateChannel(serviceSid, sid, attributes, friendlyName, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV1ChannelApi#updateChannel");
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
| **sid** | **String**|  | |
| **attributes** | **String**|  | [optional] |
| **friendlyName** | **String**|  | [optional] |
| **uniqueName** | **String**|  | [optional] |

### Return type

[**IpMessagingV1ServiceChannel**](IpMessagingV1ServiceChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

