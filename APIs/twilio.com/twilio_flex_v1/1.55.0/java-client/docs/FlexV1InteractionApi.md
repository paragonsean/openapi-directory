# FlexV1InteractionApi

All URIs are relative to *https://flex-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInteraction**](FlexV1InteractionApi.md#createInteraction) | **POST** /v1/Interactions |  |
| [**fetchInteraction**](FlexV1InteractionApi.md#fetchInteraction) | **GET** /v1/Interactions/{Sid} |  |


<a id="createInteraction"></a>
# **createInteraction**
> FlexV1Interaction createInteraction(channel, routing, interactionContextSid)



Create a new Interaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InteractionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InteractionApi apiInstance = new FlexV1InteractionApi(defaultClient);
    Object channel = null; // Object | The Interaction's channel.
    Object routing = null; // Object | The Interaction's routing logic.
    String interactionContextSid = "interactionContextSid_example"; // String | The Interaction context sid is used for adding a context lookup sid
    try {
      FlexV1Interaction result = apiInstance.createInteraction(channel, routing, interactionContextSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InteractionApi#createInteraction");
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
| **channel** | [**Object**](Object.md)| The Interaction&#39;s channel. | |
| **routing** | [**Object**](Object.md)| The Interaction&#39;s routing logic. | |
| **interactionContextSid** | **String**| The Interaction context sid is used for adding a context lookup sid | [optional] |

### Return type

[**FlexV1Interaction**](FlexV1Interaction.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="fetchInteraction"></a>
# **fetchInteraction**
> FlexV1Interaction fetchInteraction(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InteractionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InteractionApi apiInstance = new FlexV1InteractionApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Interaction resource to fetch.
    try {
      FlexV1Interaction result = apiInstance.fetchInteraction(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InteractionApi#fetchInteraction");
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
| **sid** | **String**| The SID of the Interaction resource to fetch. | |

### Return type

[**FlexV1Interaction**](FlexV1Interaction.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

