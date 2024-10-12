# WebhooksApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**webhooksGet**](WebhooksApi.md#webhooksGet) | **GET** /webhooks |  |
| [**webhooksIDDelete**](WebhooksApi.md#webhooksIDDelete) | **DELETE** /webhooks/{ID} |  |
| [**webhooksPost**](WebhooksApi.md#webhooksPost) | **POST** /webhooks |  |


<a id="webhooksGet"></a>
# **webhooksGet**
> EndpointGetWebhooks webhooksGet()



Fetch a listing of all webhooks owned by the current user/bubble combination.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    try {
      EndpointGetWebhooks result = apiInstance.webhooksGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EndpointGetWebhooks**](EndpointGetWebhooks.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="webhooksIDDelete"></a>
# **webhooksIDDelete**
> EndpointDeleteWebhooksID webhooksIDDelete(ID)



Delete a webhook that was previously registered by the current user/bubble combination.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    Integer ID = 56; // Integer | 
    try {
      EndpointDeleteWebhooksID result = apiInstance.webhooksIDDelete(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksIDDelete");
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
| **ID** | **Integer**|  | |

### Return type

[**EndpointDeleteWebhooksID**](EndpointDeleteWebhooksID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="webhooksPost"></a>
# **webhooksPost**
> EndpointPostWebhooks webhooksPost(event, name, uri, bubbled, objectId)



Register a new webhook for the current user/bubble combination. Specify an object_id to only be notified on an event related to that specific Conversation ID, Group ID, or User ID. Your access token must have access to the user being tracked, user you are in the conversation with, or user who created the group. You must be connected with a user in order to keep track of their online status. Alternatively, do not specify an object_id to be notified on all events that are related to conversations you&#39;re in, groups you&#39;re a member of, or users you are in conversations with. You may only have one webhook for each object_id/event. The webhook URI must reside on your own server. Webhooks do not expire when the access token used to create them expires. However, they will temporarily cease to function if the user who created them deauthorizes access to the application (effectively no longer existing within the bubble), unless/until the user reauthorizes the application using OAuth.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.daniweb.com/connect/api/v4");
    
    // Configure OAuth2 access token for authorization: implicit_flow
    OAuth implicit_flow = (OAuth) defaultClient.getAuthentication("implicit_flow");
    implicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: explicit_flow
    OAuth explicit_flow = (OAuth) defaultClient.getAuthentication("explicit_flow");
    explicit_flow.setAccessToken("YOUR ACCESS TOKEN");

    WebhooksApi apiInstance = new WebhooksApi(defaultClient);
    String event = "conversation_message"; // String | 
    String name = "name_example"; // String | 
    String uri = "uri_example"; // String | 
    Boolean bubbled = false; // Boolean | 
    Integer objectId = 56; // Integer | 
    try {
      EndpointPostWebhooks result = apiInstance.webhooksPost(event, name, uri, bubbled, objectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WebhooksApi#webhooksPost");
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
| **event** | **String**|  | [enum: conversation_message, conversation_seen, group_update, group_message, group_seen, user_online, user_update] |
| **name** | **String**|  | |
| **uri** | **String**|  | |
| **bubbled** | **Boolean**|  | [optional] [default to false] |
| **objectId** | **Integer**|  | [optional] |

### Return type

[**EndpointPostWebhooks**](EndpointPostWebhooks.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

