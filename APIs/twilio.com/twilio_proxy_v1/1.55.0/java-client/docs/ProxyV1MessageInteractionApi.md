# ProxyV1MessageInteractionApi

All URIs are relative to *https://proxy.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createMessageInteraction**](ProxyV1MessageInteractionApi.md#createMessageInteraction) | **POST** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{ParticipantSid}/MessageInteractions |  |
| [**fetchMessageInteraction**](ProxyV1MessageInteractionApi.md#fetchMessageInteraction) | **GET** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{ParticipantSid}/MessageInteractions/{Sid} |  |
| [**listMessageInteraction**](ProxyV1MessageInteractionApi.md#listMessageInteraction) | **GET** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{ParticipantSid}/MessageInteractions |  |


<a id="createMessageInteraction"></a>
# **createMessageInteraction**
> ProxyV1ServiceSessionParticipantMessageInteraction createMessageInteraction(serviceSid, sessionSid, participantSid, body, mediaUrl)



Create a new message Interaction to send directly from your system to one [Participant](https://www.twilio.com/docs/proxy/api/participant).  The &#x60;inbound&#x60; properties for the Interaction will always be empty.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1MessageInteractionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1MessageInteractionApi apiInstance = new ProxyV1MessageInteractionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource.
    String sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) resource.
    String participantSid = "participantSid_example"; // String | The SID of the [Participant](https://www.twilio.com/docs/proxy/api/participant) resource.
    String body = "body_example"; // String | The message to send to the participant
    List<URI> mediaUrl = Arrays.asList(); // List<URI> | Reserved. Not currently supported.
    try {
      ProxyV1ServiceSessionParticipantMessageInteraction result = apiInstance.createMessageInteraction(serviceSid, sessionSid, participantSid, body, mediaUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1MessageInteractionApi#createMessageInteraction");
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
| **participantSid** | **String**| The SID of the [Participant](https://www.twilio.com/docs/proxy/api/participant) resource. | |
| **body** | **String**| The message to send to the participant | [optional] |
| **mediaUrl** | [**List&lt;URI&gt;**](URI.md)| Reserved. Not currently supported. | [optional] |

### Return type

[**ProxyV1ServiceSessionParticipantMessageInteraction**](ProxyV1ServiceSessionParticipantMessageInteraction.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchMessageInteraction"></a>
# **fetchMessageInteraction**
> ProxyV1ServiceSessionParticipantMessageInteraction fetchMessageInteraction(serviceSid, sessionSid, participantSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1MessageInteractionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1MessageInteractionApi apiInstance = new ProxyV1MessageInteractionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to fetch.
    String sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to fetch.
    String participantSid = "participantSid_example"; // String | The SID of the [Participant](https://www.twilio.com/docs/proxy/api/participant) resource.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the MessageInteraction resource to fetch.
    try {
      ProxyV1ServiceSessionParticipantMessageInteraction result = apiInstance.fetchMessageInteraction(serviceSid, sessionSid, participantSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1MessageInteractionApi#fetchMessageInteraction");
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
| **participantSid** | **String**| The SID of the [Participant](https://www.twilio.com/docs/proxy/api/participant) resource. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the MessageInteraction resource to fetch. | |

### Return type

[**ProxyV1ServiceSessionParticipantMessageInteraction**](ProxyV1ServiceSessionParticipantMessageInteraction.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listMessageInteraction"></a>
# **listMessageInteraction**
> ListMessageInteractionResponse listMessageInteraction(serviceSid, sessionSid, participantSid, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1MessageInteractionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1MessageInteractionApi apiInstance = new ProxyV1MessageInteractionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) to read the resources from.
    String sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) to read the resources from.
    String participantSid = "participantSid_example"; // String | The SID of the [Participant](https://www.twilio.com/docs/proxy/api/participant) to read the resources from.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListMessageInteractionResponse result = apiInstance.listMessageInteraction(serviceSid, sessionSid, participantSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1MessageInteractionApi#listMessageInteraction");
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
| **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) to read the resources from. | |
| **sessionSid** | **String**| The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) to read the resources from. | |
| **participantSid** | **String**| The SID of the [Participant](https://www.twilio.com/docs/proxy/api/participant) to read the resources from. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListMessageInteractionResponse**](ListMessageInteractionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

