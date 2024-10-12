# ProxyV1SessionApi

All URIs are relative to *https://proxy.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSession**](ProxyV1SessionApi.md#createSession) | **POST** /v1/Services/{ServiceSid}/Sessions |  |
| [**deleteSession**](ProxyV1SessionApi.md#deleteSession) | **DELETE** /v1/Services/{ServiceSid}/Sessions/{Sid} |  |
| [**fetchSession**](ProxyV1SessionApi.md#fetchSession) | **GET** /v1/Services/{ServiceSid}/Sessions/{Sid} |  |
| [**listSession**](ProxyV1SessionApi.md#listSession) | **GET** /v1/Services/{ServiceSid}/Sessions |  |
| [**updateSession**](ProxyV1SessionApi.md#updateSession) | **POST** /v1/Services/{ServiceSid}/Sessions/{Sid} |  |


<a id="createSession"></a>
# **createSession**
> ProxyV1ServiceSession createSession(serviceSid, dateExpiry, mode, participants, status, ttl, uniqueName)



Create a new Session

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1SessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1SessionApi apiInstance = new ProxyV1SessionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource.
    OffsetDateTime dateExpiry = OffsetDateTime.now(); // OffsetDateTime | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session should expire. If this is value is present, it overrides the `ttl` value.
    SessionEnumMode mode = SessionEnumMode.fromValue("message-only"); // SessionEnumMode | 
    List<Object> participants = Arrays.asList(null); // List<Object> | The Participant objects to include in the new session.
    SessionEnumStatus status = SessionEnumStatus.fromValue("open"); // SessionEnumStatus | 
    Integer ttl = 56; // Integer | The time, in seconds, when the session will expire. The time is measured from the last Session create or the Session's last Interaction.
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
    try {
      ProxyV1ServiceSession result = apiInstance.createSession(serviceSid, dateExpiry, mode, participants, status, ttl, uniqueName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1SessionApi#createSession");
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
| **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource. | |
| **dateExpiry** | **OffsetDateTime**| The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session should expire. If this is value is present, it overrides the &#x60;ttl&#x60; value. | [optional] |
| **mode** | **SessionEnumMode**|  | [optional] [enum: message-only, voice-only, voice-and-message] |
| **participants** | [**List&lt;Object&gt;**](Object.md)| The Participant objects to include in the new session. | [optional] |
| **status** | **SessionEnumStatus**|  | [optional] [enum: open, in-progress, closed, failed, unknown] |
| **ttl** | **Integer**| The time, in seconds, when the session will expire. The time is measured from the last Session create or the Session&#39;s last Interaction. | [optional] |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.** | [optional] |

### Return type

[**ProxyV1ServiceSession**](ProxyV1ServiceSession.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSession"></a>
# **deleteSession**
> deleteSession(serviceSid, sid)



Delete a specific Session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1SessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1SessionApi apiInstance = new ProxyV1SessionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Session resource to delete.
    try {
      apiInstance.deleteSession(serviceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1SessionApi#deleteSession");
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
| **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to delete. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Session resource to delete. | |

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

<a id="fetchSession"></a>
# **fetchSession**
> ProxyV1ServiceSession fetchSession(serviceSid, sid)



Fetch a specific Session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1SessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1SessionApi apiInstance = new ProxyV1SessionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Session resource to fetch.
    try {
      ProxyV1ServiceSession result = apiInstance.fetchSession(serviceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1SessionApi#fetchSession");
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
| **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Session resource to fetch. | |

### Return type

[**ProxyV1ServiceSession**](ProxyV1ServiceSession.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listSession"></a>
# **listSession**
> ListSessionResponse listSession(serviceSid, pageSize, page, pageToken)



Retrieve a list of all Sessions for the Service. A maximum of 100 records will be returned per page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1SessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1SessionApi apiInstance = new ProxyV1SessionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSessionResponse result = apiInstance.listSession(serviceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1SessionApi#listSession");
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
| **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSessionResponse**](ListSessionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSession"></a>
# **updateSession**
> ProxyV1ServiceSession updateSession(serviceSid, sid, dateExpiry, status, ttl)



Update a specific Session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1SessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1SessionApi apiInstance = new ProxyV1SessionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to update.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Session resource to update.
    OffsetDateTime dateExpiry = OffsetDateTime.now(); // OffsetDateTime | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session should expire. If this is value is present, it overrides the `ttl` value.
    SessionEnumStatus status = SessionEnumStatus.fromValue("open"); // SessionEnumStatus | 
    Integer ttl = 56; // Integer | The time, in seconds, when the session will expire. The time is measured from the last Session create or the Session's last Interaction.
    try {
      ProxyV1ServiceSession result = apiInstance.updateSession(serviceSid, sid, dateExpiry, status, ttl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1SessionApi#updateSession");
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
| **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to update. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Session resource to update. | |
| **dateExpiry** | **OffsetDateTime**| The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session should expire. If this is value is present, it overrides the &#x60;ttl&#x60; value. | [optional] |
| **status** | **SessionEnumStatus**|  | [optional] [enum: open, in-progress, closed, failed, unknown] |
| **ttl** | **Integer**| The time, in seconds, when the session will expire. The time is measured from the last Session create or the Session&#39;s last Interaction. | [optional] |

### Return type

[**ProxyV1ServiceSession**](ProxyV1ServiceSession.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

