# NotifyV1BindingApi

All URIs are relative to *https://notify.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createBinding**](NotifyV1BindingApi.md#createBinding) | **POST** /v1/Services/{ServiceSid}/Bindings |  |
| [**deleteBinding**](NotifyV1BindingApi.md#deleteBinding) | **DELETE** /v1/Services/{ServiceSid}/Bindings/{Sid} |  |
| [**fetchBinding**](NotifyV1BindingApi.md#fetchBinding) | **GET** /v1/Services/{ServiceSid}/Bindings/{Sid} |  |
| [**listBinding**](NotifyV1BindingApi.md#listBinding) | **GET** /v1/Services/{ServiceSid}/Bindings |  |


<a id="createBinding"></a>
# **createBinding**
> NotifyV1ServiceBinding createBinding(serviceSid, address, bindingType, identity, credentialSid, endpoint, notificationProtocolVersion, tag)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotifyV1BindingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://notify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NotifyV1BindingApi apiInstance = new NotifyV1BindingApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to create the resource under.
    String address = "address_example"; // String | The channel-specific address. For APNS, the device token. For FCM and GCM, the registration token. For SMS, a phone number in E.164 format. For Facebook Messenger, the Messenger ID of the user or a phone number in E.164 format.
    BindingEnumBindingType bindingType = BindingEnumBindingType.fromValue("apn"); // BindingEnumBindingType | 
    String identity = "identity_example"; // String | The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/notify/api/service-resource). Up to 20 Bindings can be created for the same Identity in a given Service.
    String credentialSid = "credentialSid_example"; // String | The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) resource to be used to send notifications to this Binding. If present, this overrides the Credential specified in the Service resource. Applies to only `apn`, `fcm`, and `gcm` type Bindings.
    String endpoint = "endpoint_example"; // String | Deprecated.
    String notificationProtocolVersion = "notificationProtocolVersion_example"; // String | The protocol version to use to send the notification. This defaults to the value of `default_xxxx_notification_protocol_version` for the protocol in the [Service](https://www.twilio.com/docs/notify/api/service-resource). The current version is `\\\"3\\\"` for `apn`, `fcm`, and `gcm` type Bindings. The parameter is not applicable to `sms` and `facebook-messenger` type Bindings as the data format is fixed.
    List<String> tag = Arrays.asList(); // List<String> | A tag that can be used to select the Bindings to notify. Repeat this parameter to specify more than one tag, up to a total of 20 tags.
    try {
      NotifyV1ServiceBinding result = apiInstance.createBinding(serviceSid, address, bindingType, identity, credentialSid, endpoint, notificationProtocolVersion, tag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotifyV1BindingApi#createBinding");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to create the resource under. | |
| **address** | **String**| The channel-specific address. For APNS, the device token. For FCM and GCM, the registration token. For SMS, a phone number in E.164 format. For Facebook Messenger, the Messenger ID of the user or a phone number in E.164 format. | |
| **bindingType** | **BindingEnumBindingType**|  | [enum: apn, gcm, sms, fcm, facebook-messenger, alexa] |
| **identity** | **String**| The &#x60;identity&#x60; value that uniquely identifies the new resource&#39;s [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/notify/api/service-resource). Up to 20 Bindings can be created for the same Identity in a given Service. | |
| **credentialSid** | **String**| The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) resource to be used to send notifications to this Binding. If present, this overrides the Credential specified in the Service resource. Applies to only &#x60;apn&#x60;, &#x60;fcm&#x60;, and &#x60;gcm&#x60; type Bindings. | [optional] |
| **endpoint** | **String**| Deprecated. | [optional] |
| **notificationProtocolVersion** | **String**| The protocol version to use to send the notification. This defaults to the value of &#x60;default_xxxx_notification_protocol_version&#x60; for the protocol in the [Service](https://www.twilio.com/docs/notify/api/service-resource). The current version is &#x60;\\\&quot;3\\\&quot;&#x60; for &#x60;apn&#x60;, &#x60;fcm&#x60;, and &#x60;gcm&#x60; type Bindings. The parameter is not applicable to &#x60;sms&#x60; and &#x60;facebook-messenger&#x60; type Bindings as the data format is fixed. | [optional] |
| **tag** | [**List&lt;String&gt;**](String.md)| A tag that can be used to select the Bindings to notify. Repeat this parameter to specify more than one tag, up to a total of 20 tags. | [optional] |

### Return type

[**NotifyV1ServiceBinding**](NotifyV1ServiceBinding.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteBinding"></a>
# **deleteBinding**
> deleteBinding(serviceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotifyV1BindingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://notify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NotifyV1BindingApi apiInstance = new NotifyV1BindingApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to delete the resource from.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Binding resource to delete.
    try {
      apiInstance.deleteBinding(serviceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotifyV1BindingApi#deleteBinding");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to delete the resource from. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Binding resource to delete. | |

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

<a id="fetchBinding"></a>
# **fetchBinding**
> NotifyV1ServiceBinding fetchBinding(serviceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotifyV1BindingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://notify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NotifyV1BindingApi apiInstance = new NotifyV1BindingApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to fetch the resource from.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Binding resource to fetch.
    try {
      NotifyV1ServiceBinding result = apiInstance.fetchBinding(serviceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotifyV1BindingApi#fetchBinding");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to fetch the resource from. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Binding resource to fetch. | |

### Return type

[**NotifyV1ServiceBinding**](NotifyV1ServiceBinding.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listBinding"></a>
# **listBinding**
> ListBindingResponse listBinding(serviceSid, startDate, endDate, identity, tag, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NotifyV1BindingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://notify.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NotifyV1BindingApi apiInstance = new NotifyV1BindingApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to read the resource from.
    LocalDate startDate = LocalDate.now(); // LocalDate | Only include usage that has occurred on or after this date. Specify the date in GMT and format as `YYYY-MM-DD`.
    LocalDate endDate = LocalDate.now(); // LocalDate | Only include usage that occurred on or before this date. Specify the date in GMT and format as `YYYY-MM-DD`.
    List<String> identity = Arrays.asList(); // List<String> | The [User](https://www.twilio.com/docs/chat/rest/user-resource)'s `identity` value of the resources to read.
    List<String> tag = Arrays.asList(); // List<String> | Only list Bindings that have all of the specified Tags. The following implicit tags are available: `all`, `apn`, `fcm`, `gcm`, `sms`, `facebook-messenger`. Up to 5 tags are allowed.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListBindingResponse result = apiInstance.listBinding(serviceSid, startDate, endDate, identity, tag, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NotifyV1BindingApi#listBinding");
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
| **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) to read the resource from. | |
| **startDate** | **LocalDate**| Only include usage that has occurred on or after this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;. | [optional] |
| **endDate** | **LocalDate**| Only include usage that occurred on or before this date. Specify the date in GMT and format as &#x60;YYYY-MM-DD&#x60;. | [optional] |
| **identity** | [**List&lt;String&gt;**](String.md)| The [User](https://www.twilio.com/docs/chat/rest/user-resource)&#39;s &#x60;identity&#x60; value of the resources to read. | [optional] |
| **tag** | [**List&lt;String&gt;**](String.md)| Only list Bindings that have all of the specified Tags. The following implicit tags are available: &#x60;all&#x60;, &#x60;apn&#x60;, &#x60;fcm&#x60;, &#x60;gcm&#x60;, &#x60;sms&#x60;, &#x60;facebook-messenger&#x60;. Up to 5 tags are allowed. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListBindingResponse**](ListBindingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

