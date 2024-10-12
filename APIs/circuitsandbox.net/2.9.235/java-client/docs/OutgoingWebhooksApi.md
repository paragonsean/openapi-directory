# OutgoingWebhooksApi

All URIs are relative to *https://circuitsandbox.net/rest/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addPresenceWebHook**](OutgoingWebhooksApi.md#addPresenceWebHook) | **POST** /webhooks/presence | Registers Presence WebHook registration |
| [**addWebHook**](OutgoingWebhooksApi.md#addWebHook) | **POST** /webhooks | Registers a WebHook |
| [**getWebHook**](OutgoingWebhooksApi.md#getWebHook) | **GET** /webhooks | Gets a list of webHooks |
| [**getWebHookById**](OutgoingWebhooksApi.md#getWebHookById) | **GET** /webhooks/{id} | Gets a webHook |
| [**removeWebHook**](OutgoingWebhooksApi.md#removeWebHook) | **DELETE** /webhooks/{id} | Removes a registered webHook |
| [**removeWebHooks**](OutgoingWebhooksApi.md#removeWebHooks) | **DELETE** /webhooks | Removes all webHooks |
| [**updatePresenceWebHook**](OutgoingWebhooksApi.md#updatePresenceWebHook) | **PUT** /webhooks/presence/{id} | Updates a Presence WebHook registration |
| [**updateWebHook**](OutgoingWebhooksApi.md#updateWebHook) | **PUT** /webhooks/{id} | Updates a WebHook registration |


<a id="addPresenceWebHook"></a>
# **addPresenceWebHook**
> WebHook addPresenceWebHook(url, userIds)

Registers Presence WebHook registration

Registers a webHook that has a presence filter with the given URL and userIds. There is a maximum number of userIds allowed OauthScopes: READ_USER

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OutgoingWebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    OutgoingWebhooksApi apiInstance = new OutgoingWebhooksApi(defaultClient);
    String url = "url_example"; // String | WebHook callback URL
    List<String> userIds = Arrays.asList(); // List<String> | The IDs of the users to subscribe for their presence
    try {
      WebHook result = apiInstance.addPresenceWebHook(url, userIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OutgoingWebhooksApi#addPresenceWebHook");
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
| **url** | **String**| WebHook callback URL | |
| **userIds** | [**List&lt;String&gt;**](String.md)| The IDs of the users to subscribe for their presence | |

### Return type

[**WebHook**](WebHook.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The webHook was successfully registered |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;an invalid URL&lt;/li&gt;&lt;li&gt;one or more invalid userIds&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **403** | The maximum number of allowed userIds is reached or the maximum number of allowed webHook is reached |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="addWebHook"></a>
# **addWebHook**
> WebHook addWebHook(filter, url)

Registers a WebHook

Registers the webHook with the given filter and callback URL. OauthScopes: READ_CONVERSATIONS, READ_USER

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OutgoingWebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    OutgoingWebhooksApi apiInstance = new OutgoingWebhooksApi(defaultClient);
    List<String> filter = Arrays.asList(); // List<String> | A filter for WebHooks that checks for a list of configured events. This filter will use a regular expression to determine if it is interested in the events or not. The event itself is converted into a string of format AREA.EVENT. Examples: CONVERSATION.CREATE / USER.UPDATE
    String url = "url_example"; // String | WebHook callback URL
    try {
      WebHook result = apiInstance.addWebHook(filter, url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OutgoingWebhooksApi#addWebHook");
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
| **filter** | [**List&lt;String&gt;**](String.md)| A filter for WebHooks that checks for a list of configured events. This filter will use a regular expression to determine if it is interested in the events or not. The event itself is converted into a string of format AREA.EVENT. Examples: CONVERSATION.CREATE / USER.UPDATE | [enum: CONVERSATION.CREATE, CONVERSATION.UPDATE, CONVERSATION.ADD_ITEM, CONVERSATION.UPDATE_ITEM, USER.INCOMING_CALL, USER.USER_UPDATED, USER.USER_SETTING_UPDATED, USER.SUBMIT_FORM_DATA] |
| **url** | **String**| WebHook callback URL | |

### Return type

[**WebHook**](WebHook.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The webHook was successfully registered |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;an invalid URL&lt;/li&gt;&lt;li&gt;an invalid event filter&lt;/li&gt;&lt;li&gt;an unsupported event filter&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **403** | The maximum number of allowed webHook is reached |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getWebHook"></a>
# **getWebHook**
> List&lt;WebHook&gt; getWebHook()

Gets a list of webHooks

Gets the list of webHooks registered for this user or API. OauthScopes: READ_CONVERSATIONS, READ_USER

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OutgoingWebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    OutgoingWebhooksApi apiInstance = new OutgoingWebhooksApi(defaultClient);
    try {
      List<WebHook> result = apiInstance.getWebHook();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OutgoingWebhooksApi#getWebHook");
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

[**List&lt;WebHook&gt;**](WebHook.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of registered webHooks |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getWebHookById"></a>
# **getWebHookById**
> WebHook getWebHookById(id)

Gets a webHook

Gets the registered webHook with the given ID. OauthScopes: READ_CONVERSATIONS, READ_USER

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OutgoingWebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    OutgoingWebhooksApi apiInstance = new OutgoingWebhooksApi(defaultClient);
    String id = "id_example"; // String | The unique ID of the webHook to fetch
    try {
      WebHook result = apiInstance.getWebHookById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OutgoingWebhooksApi#getWebHookById");
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
| **id** | **String**| The unique ID of the webHook to fetch | |

### Return type

[**WebHook**](WebHook.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The registered webHook with the given ID |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the data format of the given id does not match a UUID&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **404** | The webHook does not exist |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="removeWebHook"></a>
# **removeWebHook**
> removeWebHook(id)

Removes a registered webHook

Unregisters the webHook with the given ID. OauthScopes: READ_CONVERSATIONS, READ_USER

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OutgoingWebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    OutgoingWebhooksApi apiInstance = new OutgoingWebhooksApi(defaultClient);
    String id = "id_example"; // String | The unique ID of the webHook to remove
    try {
      apiInstance.removeWebHook(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling OutgoingWebhooksApi#removeWebHook");
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
| **id** | **String**| The unique ID of the webHook to remove | |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The operation was successful |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the data format of the given id does not match a UUID&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **404** | The webHook does not exist |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="removeWebHooks"></a>
# **removeWebHooks**
> removeWebHooks()

Removes all webHooks

Unregisters all webHooks of the authenticated user OauthScopes: READ_CONVERSATIONS, READ_USER

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OutgoingWebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    OutgoingWebhooksApi apiInstance = new OutgoingWebhooksApi(defaultClient);
    try {
      apiInstance.removeWebHooks();
    } catch (ApiException e) {
      System.err.println("Exception when calling OutgoingWebhooksApi#removeWebHooks");
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

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The operation was successful |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="updatePresenceWebHook"></a>
# **updatePresenceWebHook**
> WebHook updatePresenceWebHook(id, url, userIds)

Updates a Presence WebHook registration

Updates a registration of a webHook that has a presence filter. The update can be performed either on the URL and/or the userIds. The new userIds, if any, will override any existing userIds. OauthScopes: READ_USER

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OutgoingWebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    OutgoingWebhooksApi apiInstance = new OutgoingWebhooksApi(defaultClient);
    String id = "id_example"; // String | The unique ID of the webHook to update
    String url = "url_example"; // String | WebHook callback URL
    List<String> userIds = Arrays.asList(); // List<String> | The IDs of the users to subscribe for their presence
    try {
      WebHook result = apiInstance.updatePresenceWebHook(id, url, userIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OutgoingWebhooksApi#updatePresenceWebHook");
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
| **id** | **String**| The unique ID of the webHook to update | |
| **url** | **String**| WebHook callback URL | [optional] |
| **userIds** | [**List&lt;String&gt;**](String.md)| The IDs of the users to subscribe for their presence | [optional] |

### Return type

[**WebHook**](WebHook.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The webHook registration was successfully updated |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;an invalid URL&lt;/li&gt;&lt;li&gt;one or more invalid userIds&lt;/li&gt;&lt;li&gt;no input parameter is provided&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **403** | The maximum number of allowed userIds is reached |  -  |
| **404** | The webHook does not exist |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="updateWebHook"></a>
# **updateWebHook**
> WebHook updateWebHook(id, filter, url)

Updates a WebHook registration

Updates a webHook registration with the given filter and callback URL. OauthScopes: READ_CONVERSATIONS, READ_USER

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OutgoingWebhooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    OutgoingWebhooksApi apiInstance = new OutgoingWebhooksApi(defaultClient);
    String id = "id_example"; // String | The unique ID of the webHook to update
    List<String> filter = Arrays.asList(); // List<String> | A filter for WebHooks that checks for a list of configured events. This filter will use a regular expression to determine if it is interested in the events or not. The event itself is converted into a string of format AREA.EVENT. Examples: CONVERSATION.CREATE / USER.UPDATE
    String url = "url_example"; // String | WebHook callback URL
    try {
      WebHook result = apiInstance.updateWebHook(id, filter, url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OutgoingWebhooksApi#updateWebHook");
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
| **id** | **String**| The unique ID of the webHook to update | |
| **filter** | [**List&lt;String&gt;**](String.md)| A filter for WebHooks that checks for a list of configured events. This filter will use a regular expression to determine if it is interested in the events or not. The event itself is converted into a string of format AREA.EVENT. Examples: CONVERSATION.CREATE / USER.UPDATE | [optional] [enum: CONVERSATION.CREATE, CONVERSATION.UPDATE, CONVERSATION.ADD_ITEM, CONVERSATION.UPDATE_ITEM, USER.INCOMING_CALL, USER.USER_UPDATED, USER.USER_SETTING_UPDATED, USER.SUBMIT_FORM_DATA] |
| **url** | **String**| WebHook callback URL | [optional] |

### Return type

[**WebHook**](WebHook.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The webHook registration was successfully updated |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;an invalid URL&lt;/li&gt;&lt;li&gt;an invalid event filter&lt;/li&gt;&lt;li&gt;an unsupported event filter&lt;/li&gt;&lt;li&gt;no input parameter is provided&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **404** | The webHook does not exist |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

