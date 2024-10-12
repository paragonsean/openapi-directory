# ConversationsV1UserApi

All URIs are relative to *https://conversations.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createServiceUser**](ConversationsV1UserApi.md#createServiceUser) | **POST** /v1/Services/{ChatServiceSid}/Users |  |
| [**createUser**](ConversationsV1UserApi.md#createUser) | **POST** /v1/Users |  |
| [**deleteServiceUser**](ConversationsV1UserApi.md#deleteServiceUser) | **DELETE** /v1/Services/{ChatServiceSid}/Users/{Sid} |  |
| [**deleteUser**](ConversationsV1UserApi.md#deleteUser) | **DELETE** /v1/Users/{Sid} |  |
| [**fetchServiceUser**](ConversationsV1UserApi.md#fetchServiceUser) | **GET** /v1/Services/{ChatServiceSid}/Users/{Sid} |  |
| [**fetchUser**](ConversationsV1UserApi.md#fetchUser) | **GET** /v1/Users/{Sid} |  |
| [**listServiceUser**](ConversationsV1UserApi.md#listServiceUser) | **GET** /v1/Services/{ChatServiceSid}/Users |  |
| [**listUser**](ConversationsV1UserApi.md#listUser) | **GET** /v1/Users |  |
| [**updateServiceUser**](ConversationsV1UserApi.md#updateServiceUser) | **POST** /v1/Services/{ChatServiceSid}/Users/{Sid} |  |
| [**updateUser**](ConversationsV1UserApi.md#updateUser) | **POST** /v1/Users/{Sid} |  |


<a id="createServiceUser"></a>
# **createServiceUser**
> ConversationsV1ServiceServiceUser createServiceUser(chatServiceSid, identity, xTwilioWebhookEnabled, attributes, friendlyName, roleSid)



Add a new conversation user to your service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1UserApi apiInstance = new ConversationsV1UserApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the User resource is associated with.
    String identity = "identity_example"; // String | The application-defined string that uniquely identifies the resource's User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive.
    ServiceUserEnumWebhookEnabledType xTwilioWebhookEnabled = ServiceUserEnumWebhookEnabledType.fromValue("true"); // ServiceUserEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
    String roleSid = "roleSid_example"; // String | The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.
    try {
      ConversationsV1ServiceServiceUser result = apiInstance.createServiceUser(chatServiceSid, identity, xTwilioWebhookEnabled, attributes, friendlyName, roleSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1UserApi#createServiceUser");
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
| **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the User resource is associated with. | |
| **identity** | **String**| The application-defined string that uniquely identifies the resource&#39;s User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive. | |
| **xTwilioWebhookEnabled** | **ServiceUserEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| The JSON Object string that stores application-specific data. If attributes have not been set, &#x60;{}&#x60; is returned. | [optional] |
| **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] |
| **roleSid** | **String**| The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user. | [optional] |

### Return type

[**ConversationsV1ServiceServiceUser**](ConversationsV1ServiceServiceUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="createUser"></a>
# **createUser**
> ConversationsV1User createUser(identity, xTwilioWebhookEnabled, attributes, friendlyName, roleSid)



Add a new conversation user to your account&#39;s default service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1UserApi apiInstance = new ConversationsV1UserApi(defaultClient);
    String identity = "identity_example"; // String | The application-defined string that uniquely identifies the resource's User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive.
    UserEnumWebhookEnabledType xTwilioWebhookEnabled = UserEnumWebhookEnabledType.fromValue("true"); // UserEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
    String roleSid = "roleSid_example"; // String | The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.
    try {
      ConversationsV1User result = apiInstance.createUser(identity, xTwilioWebhookEnabled, attributes, friendlyName, roleSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1UserApi#createUser");
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
| **identity** | **String**| The application-defined string that uniquely identifies the resource&#39;s User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive. | |
| **xTwilioWebhookEnabled** | **UserEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| The JSON Object string that stores application-specific data. If attributes have not been set, &#x60;{}&#x60; is returned. | [optional] |
| **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] |
| **roleSid** | **String**| The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user. | [optional] |

### Return type

[**ConversationsV1User**](ConversationsV1User.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteServiceUser"></a>
# **deleteServiceUser**
> deleteServiceUser(chatServiceSid, sid, xTwilioWebhookEnabled)



Remove a conversation user from your service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1UserApi apiInstance = new ConversationsV1UserApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to delete the User resource from.
    String sid = "sid_example"; // String | The SID of the User resource to delete. This value can be either the `sid` or the `identity` of the User resource to delete.
    ServiceUserEnumWebhookEnabledType xTwilioWebhookEnabled = ServiceUserEnumWebhookEnabledType.fromValue("true"); // ServiceUserEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    try {
      apiInstance.deleteServiceUser(chatServiceSid, sid, xTwilioWebhookEnabled);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1UserApi#deleteServiceUser");
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
| **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to delete the User resource from. | |
| **sid** | **String**| The SID of the User resource to delete. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to delete. | |
| **xTwilioWebhookEnabled** | **ServiceUserEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |

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

<a id="deleteUser"></a>
# **deleteUser**
> deleteUser(sid, xTwilioWebhookEnabled)



Remove a conversation user from your account&#39;s default service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1UserApi apiInstance = new ConversationsV1UserApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the User resource to delete. This value can be either the `sid` or the `identity` of the User resource to delete.
    UserEnumWebhookEnabledType xTwilioWebhookEnabled = UserEnumWebhookEnabledType.fromValue("true"); // UserEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    try {
      apiInstance.deleteUser(sid, xTwilioWebhookEnabled);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1UserApi#deleteUser");
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
| **sid** | **String**| The SID of the User resource to delete. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to delete. | |
| **xTwilioWebhookEnabled** | **UserEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |

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

<a id="fetchServiceUser"></a>
# **fetchServiceUser**
> ConversationsV1ServiceServiceUser fetchServiceUser(chatServiceSid, sid)



Fetch a conversation user from your service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1UserApi apiInstance = new ConversationsV1UserApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to fetch the User resource from.
    String sid = "sid_example"; // String | The SID of the User resource to fetch. This value can be either the `sid` or the `identity` of the User resource to fetch.
    try {
      ConversationsV1ServiceServiceUser result = apiInstance.fetchServiceUser(chatServiceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1UserApi#fetchServiceUser");
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
| **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to fetch the User resource from. | |
| **sid** | **String**| The SID of the User resource to fetch. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to fetch. | |

### Return type

[**ConversationsV1ServiceServiceUser**](ConversationsV1ServiceServiceUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="fetchUser"></a>
# **fetchUser**
> ConversationsV1User fetchUser(sid)



Fetch a conversation user from your account&#39;s default service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1UserApi apiInstance = new ConversationsV1UserApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the User resource to fetch. This value can be either the `sid` or the `identity` of the User resource to fetch.
    try {
      ConversationsV1User result = apiInstance.fetchUser(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1UserApi#fetchUser");
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
| **sid** | **String**| The SID of the User resource to fetch. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to fetch. | |

### Return type

[**ConversationsV1User**](ConversationsV1User.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listServiceUser"></a>
# **listServiceUser**
> ListServiceUserResponse listServiceUser(chatServiceSid, pageSize, page, pageToken)



Retrieve a list of all conversation users in your service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1UserApi apiInstance = new ConversationsV1UserApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to read the User resources from.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListServiceUserResponse result = apiInstance.listServiceUser(chatServiceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1UserApi#listServiceUser");
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
| **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) to read the User resources from. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListServiceUserResponse**](ListServiceUserResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listUser"></a>
# **listUser**
> ListUserResponse listUser(pageSize, page, pageToken)



Retrieve a list of all conversation users in your account&#39;s default service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1UserApi apiInstance = new ConversationsV1UserApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListUserResponse result = apiInstance.listUser(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1UserApi#listUser");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListUserResponse**](ListUserResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateServiceUser"></a>
# **updateServiceUser**
> ConversationsV1ServiceServiceUser updateServiceUser(chatServiceSid, sid, xTwilioWebhookEnabled, attributes, friendlyName, roleSid)



Update an existing conversation user in your service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1UserApi apiInstance = new ConversationsV1UserApi(defaultClient);
    String chatServiceSid = "chatServiceSid_example"; // String | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the User resource is associated with.
    String sid = "sid_example"; // String | The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
    ServiceUserEnumWebhookEnabledType xTwilioWebhookEnabled = ServiceUserEnumWebhookEnabledType.fromValue("true"); // ServiceUserEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
    String roleSid = "roleSid_example"; // String | The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.
    try {
      ConversationsV1ServiceServiceUser result = apiInstance.updateServiceUser(chatServiceSid, sid, xTwilioWebhookEnabled, attributes, friendlyName, roleSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1UserApi#updateServiceUser");
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
| **chatServiceSid** | **String**| The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the User resource is associated with. | |
| **sid** | **String**| The SID of the User resource to update. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to update. | |
| **xTwilioWebhookEnabled** | **ServiceUserEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| The JSON Object string that stores application-specific data. If attributes have not been set, &#x60;{}&#x60; is returned. | [optional] |
| **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] |
| **roleSid** | **String**| The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user. | [optional] |

### Return type

[**ConversationsV1ServiceServiceUser**](ConversationsV1ServiceServiceUser.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateUser"></a>
# **updateUser**
> ConversationsV1User updateUser(sid, xTwilioWebhookEnabled, attributes, friendlyName, roleSid)



Update an existing conversation user in your account&#39;s default service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsV1UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://conversations.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ConversationsV1UserApi apiInstance = new ConversationsV1UserApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
    UserEnumWebhookEnabledType xTwilioWebhookEnabled = UserEnumWebhookEnabledType.fromValue("true"); // UserEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
    String attributes = "attributes_example"; // String | The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
    String friendlyName = "friendlyName_example"; // String | The string that you assigned to describe the resource.
    String roleSid = "roleSid_example"; // String | The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.
    try {
      ConversationsV1User result = apiInstance.updateUser(sid, xTwilioWebhookEnabled, attributes, friendlyName, roleSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsV1UserApi#updateUser");
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
| **sid** | **String**| The SID of the User resource to update. This value can be either the &#x60;sid&#x60; or the &#x60;identity&#x60; of the User resource to update. | |
| **xTwilioWebhookEnabled** | **UserEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] [enum: true, false] |
| **attributes** | **String**| The JSON Object string that stores application-specific data. If attributes have not been set, &#x60;{}&#x60; is returned. | [optional] |
| **friendlyName** | **String**| The string that you assigned to describe the resource. | [optional] |
| **roleSid** | **String**| The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user. | [optional] |

### Return type

[**ConversationsV1User**](ConversationsV1User.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

