# IpMessagingV2UserApi

All URIs are relative to *https://ip-messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createUser**](IpMessagingV2UserApi.md#createUser) | **POST** /v2/Services/{ServiceSid}/Users |  |
| [**deleteUser**](IpMessagingV2UserApi.md#deleteUser) | **DELETE** /v2/Services/{ServiceSid}/Users/{Sid} |  |
| [**fetchUser**](IpMessagingV2UserApi.md#fetchUser) | **GET** /v2/Services/{ServiceSid}/Users/{Sid} |  |
| [**listUser**](IpMessagingV2UserApi.md#listUser) | **GET** /v2/Services/{ServiceSid}/Users |  |
| [**updateUser**](IpMessagingV2UserApi.md#updateUser) | **POST** /v2/Services/{ServiceSid}/Users/{Sid} |  |


<a id="createUser"></a>
# **createUser**
> IpMessagingV2ServiceUser createUser(serviceSid, identity, xTwilioWebhookEnabled, attributes, friendlyName, roleSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2UserApi apiInstance = new IpMessagingV2UserApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String identity = "identity_example"; // String | 
    UserEnumWebhookEnabledType xTwilioWebhookEnabled = UserEnumWebhookEnabledType.fromValue("true"); // UserEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | 
    String friendlyName = "friendlyName_example"; // String | 
    String roleSid = "roleSid_example"; // String | 
    try {
      IpMessagingV2ServiceUser result = apiInstance.createUser(serviceSid, identity, xTwilioWebhookEnabled, attributes, friendlyName, roleSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2UserApi#createUser");
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
| **identity** | **String**|  | |
| **xTwilioWebhookEnabled** | **UserEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**|  | [optional] |
| **friendlyName** | **String**|  | [optional] |
| **roleSid** | **String**|  | [optional] |

### Return type

[**IpMessagingV2ServiceUser**](IpMessagingV2ServiceUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteUser"></a>
# **deleteUser**
> deleteUser(serviceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2UserApi apiInstance = new IpMessagingV2UserApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String sid = "sid_example"; // String | 
    try {
      apiInstance.deleteUser(serviceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2UserApi#deleteUser");
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

<a id="fetchUser"></a>
# **fetchUser**
> IpMessagingV2ServiceUser fetchUser(serviceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2UserApi apiInstance = new IpMessagingV2UserApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String sid = "sid_example"; // String | 
    try {
      IpMessagingV2ServiceUser result = apiInstance.fetchUser(serviceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2UserApi#fetchUser");
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

[**IpMessagingV2ServiceUser**](IpMessagingV2ServiceUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listUser"></a>
# **listUser**
> ListUserResponse listUser(serviceSid, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2UserApi apiInstance = new IpMessagingV2UserApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListUserResponse result = apiInstance.listUser(serviceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2UserApi#listUser");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListUserResponse**](ListUserResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateUser"></a>
# **updateUser**
> IpMessagingV2ServiceUser updateUser(serviceSid, sid, xTwilioWebhookEnabled, attributes, friendlyName, roleSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2UserApi apiInstance = new IpMessagingV2UserApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String sid = "sid_example"; // String | 
    UserEnumWebhookEnabledType xTwilioWebhookEnabled = UserEnumWebhookEnabledType.fromValue("true"); // UserEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | 
    String friendlyName = "friendlyName_example"; // String | 
    String roleSid = "roleSid_example"; // String | 
    try {
      IpMessagingV2ServiceUser result = apiInstance.updateUser(serviceSid, sid, xTwilioWebhookEnabled, attributes, friendlyName, roleSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2UserApi#updateUser");
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
| **xTwilioWebhookEnabled** | **UserEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**|  | [optional] |
| **friendlyName** | **String**|  | [optional] |
| **roleSid** | **String**|  | [optional] |

### Return type

[**IpMessagingV2ServiceUser**](IpMessagingV2ServiceUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

