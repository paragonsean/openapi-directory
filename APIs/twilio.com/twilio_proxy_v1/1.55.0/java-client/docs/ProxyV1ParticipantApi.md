# ProxyV1ParticipantApi

All URIs are relative to *https://proxy.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createParticipant**](ProxyV1ParticipantApi.md#createParticipant) | **POST** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants |  |
| [**deleteParticipant**](ProxyV1ParticipantApi.md#deleteParticipant) | **DELETE** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{Sid} |  |
| [**fetchParticipant**](ProxyV1ParticipantApi.md#fetchParticipant) | **GET** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{Sid} |  |
| [**listParticipant**](ProxyV1ParticipantApi.md#listParticipant) | **GET** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants |  |


<a id="createParticipant"></a>
# **createParticipant**
> ProxyV1ServiceSessionParticipant createParticipant(serviceSid, sessionSid, identifier, friendlyName, proxyIdentifier, proxyIdentifierSid)



Add a new Participant to the Session

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1ParticipantApi apiInstance = new ProxyV1ParticipantApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource.
    String sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) resource.
    String identifier = "identifier_example"; // String | The phone number of the Participant.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the participant. This value must be 255 characters or fewer. **This value should not have PII.**
    String proxyIdentifier = "proxyIdentifier_example"; // String | The proxy phone number to use for the Participant. If not specified, Proxy will select a number from the pool.
    String proxyIdentifierSid = "proxyIdentifierSid_example"; // String | The SID of the Proxy Identifier to assign to the Participant.
    try {
      ProxyV1ServiceSessionParticipant result = apiInstance.createParticipant(serviceSid, sessionSid, identifier, friendlyName, proxyIdentifier, proxyIdentifierSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1ParticipantApi#createParticipant");
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
| **sessionSid** | **String**| The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) resource. | |
| **identifier** | **String**| The phone number of the Participant. | |
| **friendlyName** | **String**| The string that you assigned to describe the participant. This value must be 255 characters or fewer. **This value should not have PII.** | [optional] |
| **proxyIdentifier** | **String**| The proxy phone number to use for the Participant. If not specified, Proxy will select a number from the pool. | [optional] |
| **proxyIdentifierSid** | **String**| The SID of the Proxy Identifier to assign to the Participant. | [optional] |

### Return type

[**ProxyV1ServiceSessionParticipant**](ProxyV1ServiceSessionParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteParticipant"></a>
# **deleteParticipant**
> deleteParticipant(serviceSid, sessionSid, sid)



Delete a specific Participant. This is a soft-delete. The participant remains associated with the session and cannot be re-added. Participants are only permanently deleted when the [Session](https://www.twilio.com/docs/proxy/api/session) is deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1ParticipantApi apiInstance = new ProxyV1ParticipantApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to delete.
    String sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Participant resource to delete.
    try {
      apiInstance.deleteParticipant(serviceSid, sessionSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1ParticipantApi#deleteParticipant");
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
| **sessionSid** | **String**| The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to delete. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Participant resource to delete. | |

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

<a id="fetchParticipant"></a>
# **fetchParticipant**
> ProxyV1ServiceSessionParticipant fetchParticipant(serviceSid, sessionSid, sid)



Fetch a specific Participant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1ParticipantApi apiInstance = new ProxyV1ParticipantApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to fetch.
    String sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Participant resource to fetch.
    try {
      ProxyV1ServiceSessionParticipant result = apiInstance.fetchParticipant(serviceSid, sessionSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1ParticipantApi#fetchParticipant");
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
| **sessionSid** | **String**| The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Participant resource to fetch. | |

### Return type

[**ProxyV1ServiceSessionParticipant**](ProxyV1ServiceSessionParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listParticipant"></a>
# **listParticipant**
> ListParticipantResponse listParticipant(serviceSid, sessionSid, pageSize, page, pageToken)



Retrieve a list of all Participants in a Session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1ParticipantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1ParticipantApi apiInstance = new ProxyV1ParticipantApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resources to read.
    String sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListParticipantResponse result = apiInstance.listParticipant(serviceSid, sessionSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1ParticipantApi#listParticipant");
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
| **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resources to read. | |
| **sessionSid** | **String**| The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resources to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListParticipantResponse**](ListParticipantResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

