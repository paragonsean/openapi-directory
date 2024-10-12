# ProxyV1InteractionApi

All URIs are relative to *https://proxy.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteInteraction**](ProxyV1InteractionApi.md#deleteInteraction) | **DELETE** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Interactions/{Sid} |  |
| [**fetchInteraction**](ProxyV1InteractionApi.md#fetchInteraction) | **GET** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Interactions/{Sid} |  |
| [**listInteraction**](ProxyV1InteractionApi.md#listInteraction) | **GET** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Interactions |  |


<a id="deleteInteraction"></a>
# **deleteInteraction**
> deleteInteraction(serviceSid, sessionSid, sid)



Delete a specific Interaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1InteractionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1InteractionApi apiInstance = new ProxyV1InteractionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to delete.
    String sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Interaction resource to delete.
    try {
      apiInstance.deleteInteraction(serviceSid, sessionSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1InteractionApi#deleteInteraction");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Interaction resource to delete. | |

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

<a id="fetchInteraction"></a>
# **fetchInteraction**
> ProxyV1ServiceSessionInteraction fetchInteraction(serviceSid, sessionSid, sid)



Retrieve a list of Interactions for a given [Session](https://www.twilio.com/docs/proxy/api/session).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1InteractionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1InteractionApi apiInstance = new ProxyV1InteractionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to fetch.
    String sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Interaction resource to fetch.
    try {
      ProxyV1ServiceSessionInteraction result = apiInstance.fetchInteraction(serviceSid, sessionSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1InteractionApi#fetchInteraction");
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
| **sid** | **String**| The Twilio-provided string that uniquely identifies the Interaction resource to fetch. | |

### Return type

[**ProxyV1ServiceSessionInteraction**](ProxyV1ServiceSessionInteraction.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listInteraction"></a>
# **listInteraction**
> ListInteractionResponse listInteraction(serviceSid, sessionSid, pageSize, page, pageToken)



Retrieve a list of all Interactions for a Session. A maximum of 100 records will be returned per page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1InteractionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1InteractionApi apiInstance = new ProxyV1InteractionApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) to read the resources from.
    String sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) to read the resources from.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListInteractionResponse result = apiInstance.listInteraction(serviceSid, sessionSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1InteractionApi#listInteraction");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListInteractionResponse**](ListInteractionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

