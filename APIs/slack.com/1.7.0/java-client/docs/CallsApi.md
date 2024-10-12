# CallsApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**callsAdd**](CallsApi.md#callsAdd) | **POST** /calls.add |  |
| [**callsEnd**](CallsApi.md#callsEnd) | **POST** /calls.end |  |
| [**callsInfo**](CallsApi.md#callsInfo) | **GET** /calls.info |  |
| [**callsParticipantsAdd_0**](CallsApi.md#callsParticipantsAdd_0) | **POST** /calls.participants.add |  |
| [**callsParticipantsRemove_0**](CallsApi.md#callsParticipantsRemove_0) | **POST** /calls.participants.remove |  |
| [**callsUpdate**](CallsApi.md#callsUpdate) | **POST** /calls.update |  |


<a id="callsAdd"></a>
# **callsAdd**
> DefaultSuccessTemplate callsAdd(token, externalUniqueId, joinUrl, createdBy, dateStart, desktopAppJoinUrl, externalDisplayId, title, users)



Registers a new Call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `calls:write`
    String externalUniqueId = "externalUniqueId_example"; // String | An ID supplied by the 3rd-party Call provider. It must be unique across all Calls from that service.
    String joinUrl = "joinUrl_example"; // String | The URL required for a client to join the Call.
    String createdBy = "createdBy_example"; // String | The valid Slack user ID of the user who created this Call. When this method is called with a user token, the `created_by` field is optional and defaults to the authed user of the token. Otherwise, the field is required.
    Integer dateStart = 56; // Integer | Call start time in UTC UNIX timestamp format
    String desktopAppJoinUrl = "desktopAppJoinUrl_example"; // String | When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL.
    String externalDisplayId = "externalDisplayId_example"; // String | An optional, human-readable ID supplied by the 3rd-party Call provider. If supplied, this ID will be displayed in the Call object.
    String title = "title_example"; // String | The name of the Call.
    String users = "users_example"; // String | The list of users to register as participants in the Call. [Read more on how to specify users here](/apis/calls#users).
    try {
      DefaultSuccessTemplate result = apiInstance.callsAdd(token, externalUniqueId, joinUrl, createdBy, dateStart, desktopAppJoinUrl, externalDisplayId, title, users);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#callsAdd");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;calls:write&#x60; | |
| **externalUniqueId** | **String**| An ID supplied by the 3rd-party Call provider. It must be unique across all Calls from that service. | |
| **joinUrl** | **String**| The URL required for a client to join the Call. | |
| **createdBy** | **String**| The valid Slack user ID of the user who created this Call. When this method is called with a user token, the &#x60;created_by&#x60; field is optional and defaults to the authed user of the token. Otherwise, the field is required. | [optional] |
| **dateStart** | **Integer**| Call start time in UTC UNIX timestamp format | [optional] |
| **desktopAppJoinUrl** | **String**| When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL. | [optional] |
| **externalDisplayId** | **String**| An optional, human-readable ID supplied by the 3rd-party Call provider. If supplied, this ID will be displayed in the Call object. | [optional] |
| **title** | **String**| The name of the Call. | [optional] |
| **users** | **String**| The list of users to register as participants in the Call. [Read more on how to specify users here](/apis/calls#users). | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="callsEnd"></a>
# **callsEnd**
> DefaultSuccessTemplate callsEnd(token, id, duration)



Ends a Call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `calls:write`
    String id = "id_example"; // String | `id` returned when registering the call using the [`calls.add`](/methods/calls.add) method.
    Integer duration = 56; // Integer | Call duration in seconds
    try {
      DefaultSuccessTemplate result = apiInstance.callsEnd(token, id, duration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#callsEnd");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;calls:write&#x60; | |
| **id** | **String**| &#x60;id&#x60; returned when registering the call using the [&#x60;calls.add&#x60;](/methods/calls.add) method. | |
| **duration** | **Integer**| Call duration in seconds | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="callsInfo"></a>
# **callsInfo**
> DefaultSuccessTemplate callsInfo(token, id)



Returns information about a Call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `calls:read`
    String id = "id_example"; // String | `id` of the Call returned by the [`calls.add`](/methods/calls.add) method.
    try {
      DefaultSuccessTemplate result = apiInstance.callsInfo(token, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#callsInfo");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;calls:read&#x60; | |
| **id** | **String**| &#x60;id&#x60; of the Call returned by the [&#x60;calls.add&#x60;](/methods/calls.add) method. | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="callsParticipantsAdd_0"></a>
# **callsParticipantsAdd_0**
> DefaultSuccessTemplate callsParticipantsAdd_0(token, id, users)



Registers new participants added to a Call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `calls:write`
    String id = "id_example"; // String | `id` returned by the [`calls.add`](/methods/calls.add) method.
    String users = "users_example"; // String | The list of users to add as participants in the Call. [Read more on how to specify users here](/apis/calls#users).
    try {
      DefaultSuccessTemplate result = apiInstance.callsParticipantsAdd_0(token, id, users);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#callsParticipantsAdd_0");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;calls:write&#x60; | |
| **id** | **String**| &#x60;id&#x60; returned by the [&#x60;calls.add&#x60;](/methods/calls.add) method. | |
| **users** | **String**| The list of users to add as participants in the Call. [Read more on how to specify users here](/apis/calls#users). | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="callsParticipantsRemove_0"></a>
# **callsParticipantsRemove_0**
> DefaultSuccessTemplate callsParticipantsRemove_0(token, id, users)



Registers participants removed from a Call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `calls:write`
    String id = "id_example"; // String | `id` returned by the [`calls.add`](/methods/calls.add) method.
    String users = "users_example"; // String | The list of users to remove as participants in the Call. [Read more on how to specify users here](/apis/calls#users).
    try {
      DefaultSuccessTemplate result = apiInstance.callsParticipantsRemove_0(token, id, users);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#callsParticipantsRemove_0");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;calls:write&#x60; | |
| **id** | **String**| &#x60;id&#x60; returned by the [&#x60;calls.add&#x60;](/methods/calls.add) method. | |
| **users** | **String**| The list of users to remove as participants in the Call. [Read more on how to specify users here](/apis/calls#users). | |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="callsUpdate"></a>
# **callsUpdate**
> DefaultSuccessTemplate callsUpdate(token, id, desktopAppJoinUrl, joinUrl, title)



Updates information about a Call.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CallsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    CallsApi apiInstance = new CallsApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `calls:write`
    String id = "id_example"; // String | `id` returned by the [`calls.add`](/methods/calls.add) method.
    String desktopAppJoinUrl = "desktopAppJoinUrl_example"; // String | When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL.
    String joinUrl = "joinUrl_example"; // String | The URL required for a client to join the Call.
    String title = "title_example"; // String | The name of the Call.
    try {
      DefaultSuccessTemplate result = apiInstance.callsUpdate(token, id, desktopAppJoinUrl, joinUrl, title);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CallsApi#callsUpdate");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;calls:write&#x60; | |
| **id** | **String**| &#x60;id&#x60; returned by the [&#x60;calls.add&#x60;](/methods/calls.add) method. | |
| **desktopAppJoinUrl** | **String**| When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL. | [optional] |
| **joinUrl** | **String**| The URL required for a client to join the Call. | [optional] |
| **title** | **String**| The name of the Call. | [optional] |

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

