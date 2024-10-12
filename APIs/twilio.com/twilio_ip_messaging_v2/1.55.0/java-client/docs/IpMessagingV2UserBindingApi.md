# IpMessagingV2UserBindingApi

All URIs are relative to *https://ip-messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteUserBinding**](IpMessagingV2UserBindingApi.md#deleteUserBinding) | **DELETE** /v2/Services/{ServiceSid}/Users/{UserSid}/Bindings/{Sid} |  |
| [**fetchUserBinding**](IpMessagingV2UserBindingApi.md#fetchUserBinding) | **GET** /v2/Services/{ServiceSid}/Users/{UserSid}/Bindings/{Sid} |  |
| [**listUserBinding**](IpMessagingV2UserBindingApi.md#listUserBinding) | **GET** /v2/Services/{ServiceSid}/Users/{UserSid}/Bindings |  |


<a id="deleteUserBinding"></a>
# **deleteUserBinding**
> deleteUserBinding(serviceSid, userSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2UserBindingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2UserBindingApi apiInstance = new IpMessagingV2UserBindingApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String userSid = "userSid_example"; // String | 
    String sid = "sid_example"; // String | 
    try {
      apiInstance.deleteUserBinding(serviceSid, userSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2UserBindingApi#deleteUserBinding");
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

<a id="fetchUserBinding"></a>
# **fetchUserBinding**
> IpMessagingV2ServiceUserUserBinding fetchUserBinding(serviceSid, userSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2UserBindingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2UserBindingApi apiInstance = new IpMessagingV2UserBindingApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String userSid = "userSid_example"; // String | 
    String sid = "sid_example"; // String | 
    try {
      IpMessagingV2ServiceUserUserBinding result = apiInstance.fetchUserBinding(serviceSid, userSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2UserBindingApi#fetchUserBinding");
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
| **sid** | **String**|  | |

### Return type

[**IpMessagingV2ServiceUserUserBinding**](IpMessagingV2ServiceUserUserBinding.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listUserBinding"></a>
# **listUserBinding**
> ListUserBindingResponse listUserBinding(serviceSid, userSid, bindingType, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IpMessagingV2UserBindingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ip-messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    IpMessagingV2UserBindingApi apiInstance = new IpMessagingV2UserBindingApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | 
    String userSid = "userSid_example"; // String | 
    List<UserBindingEnumBindingType> bindingType = Arrays.asList(); // List<UserBindingEnumBindingType> | 
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListUserBindingResponse result = apiInstance.listUserBinding(serviceSid, userSid, bindingType, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IpMessagingV2UserBindingApi#listUserBinding");
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
| **bindingType** | [**List&lt;UserBindingEnumBindingType&gt;**](UserBindingEnumBindingType.md)|  | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListUserBindingResponse**](ListUserBindingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

