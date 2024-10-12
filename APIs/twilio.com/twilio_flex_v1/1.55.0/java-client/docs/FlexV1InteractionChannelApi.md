# FlexV1InteractionChannelApi

All URIs are relative to *https://flex-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchInteractionChannel**](FlexV1InteractionChannelApi.md#fetchInteractionChannel) | **GET** /v1/Interactions/{InteractionSid}/Channels/{Sid} |  |
| [**listInteractionChannel**](FlexV1InteractionChannelApi.md#listInteractionChannel) | **GET** /v1/Interactions/{InteractionSid}/Channels |  |
| [**updateInteractionChannel**](FlexV1InteractionChannelApi.md#updateInteractionChannel) | **POST** /v1/Interactions/{InteractionSid}/Channels/{Sid} |  |


<a id="fetchInteractionChannel"></a>
# **fetchInteractionChannel**
> FlexV1InteractionInteractionChannel fetchInteractionChannel(interactionSid, sid)



Fetch a Channel for an Interaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InteractionChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InteractionChannelApi apiInstance = new FlexV1InteractionChannelApi(defaultClient);
    String interactionSid = "interactionSid_example"; // String | The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
    String sid = "sid_example"; // String | The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
    try {
      FlexV1InteractionInteractionChannel result = apiInstance.fetchInteractionChannel(interactionSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InteractionChannelApi#fetchInteractionChannel");
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
| **interactionSid** | **String**| The unique string created by Twilio to identify an Interaction resource, prefixed with KD. | |
| **sid** | **String**| The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO. | |

### Return type

[**FlexV1InteractionInteractionChannel**](FlexV1InteractionInteractionChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listInteractionChannel"></a>
# **listInteractionChannel**
> ListInteractionChannelResponse listInteractionChannel(interactionSid, pageSize, page, pageToken)



List all Channels for an Interaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InteractionChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InteractionChannelApi apiInstance = new FlexV1InteractionChannelApi(defaultClient);
    String interactionSid = "interactionSid_example"; // String | The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListInteractionChannelResponse result = apiInstance.listInteractionChannel(interactionSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InteractionChannelApi#listInteractionChannel");
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
| **interactionSid** | **String**| The unique string created by Twilio to identify an Interaction resource, prefixed with KD. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListInteractionChannelResponse**](ListInteractionChannelResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateInteractionChannel"></a>
# **updateInteractionChannel**
> FlexV1InteractionInteractionChannel updateInteractionChannel(interactionSid, sid, status, routing)



Update an existing Interaction Channel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InteractionChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InteractionChannelApi apiInstance = new FlexV1InteractionChannelApi(defaultClient);
    String interactionSid = "interactionSid_example"; // String | The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
    String sid = "sid_example"; // String | The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
    InteractionChannelEnumUpdateChannelStatus status = InteractionChannelEnumUpdateChannelStatus.fromValue("closed"); // InteractionChannelEnumUpdateChannelStatus | 
    Object routing = null; // Object | It changes the state of associated tasks. Routing status is required, When the channel status is set to `inactive`. Allowed Value for routing status is `closed`. Otherwise Optional, if not specified, all tasks will be set to `wrapping`.
    try {
      FlexV1InteractionInteractionChannel result = apiInstance.updateInteractionChannel(interactionSid, sid, status, routing);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InteractionChannelApi#updateInteractionChannel");
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
| **interactionSid** | **String**| The unique string created by Twilio to identify an Interaction resource, prefixed with KD. | |
| **sid** | **String**| The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO. | |
| **status** | **InteractionChannelEnumUpdateChannelStatus**|  | [enum: closed, inactive] |
| **routing** | [**Object**](Object.md)| It changes the state of associated tasks. Routing status is required, When the channel status is set to &#x60;inactive&#x60;. Allowed Value for routing status is &#x60;closed&#x60;. Otherwise Optional, if not specified, all tasks will be set to &#x60;wrapping&#x60;. | [optional] |

### Return type

[**FlexV1InteractionInteractionChannel**](FlexV1InteractionInteractionChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

