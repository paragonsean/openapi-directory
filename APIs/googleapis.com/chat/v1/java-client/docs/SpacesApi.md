# SpacesApi

All URIs are relative to *https://chat.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chatSpacesCompleteImport**](SpacesApi.md#chatSpacesCompleteImport) | **POST** /v1/{name}:completeImport |  |
| [**chatSpacesCreate**](SpacesApi.md#chatSpacesCreate) | **POST** /v1/spaces |  |
| [**chatSpacesFindDirectMessage**](SpacesApi.md#chatSpacesFindDirectMessage) | **GET** /v1/spaces:findDirectMessage |  |
| [**chatSpacesList**](SpacesApi.md#chatSpacesList) | **GET** /v1/spaces |  |
| [**chatSpacesMembersCreate**](SpacesApi.md#chatSpacesMembersCreate) | **POST** /v1/{parent}/members |  |
| [**chatSpacesMembersList**](SpacesApi.md#chatSpacesMembersList) | **GET** /v1/{parent}/members |  |
| [**chatSpacesMessagesAttachmentsGet**](SpacesApi.md#chatSpacesMessagesAttachmentsGet) | **GET** /v1/{name} |  |
| [**chatSpacesMessagesCreate**](SpacesApi.md#chatSpacesMessagesCreate) | **POST** /v1/{parent}/messages |  |
| [**chatSpacesMessagesList**](SpacesApi.md#chatSpacesMessagesList) | **GET** /v1/{parent}/messages |  |
| [**chatSpacesMessagesPatch**](SpacesApi.md#chatSpacesMessagesPatch) | **PATCH** /v1/{name} |  |
| [**chatSpacesMessagesReactionsCreate**](SpacesApi.md#chatSpacesMessagesReactionsCreate) | **POST** /v1/{parent}/reactions |  |
| [**chatSpacesMessagesReactionsDelete**](SpacesApi.md#chatSpacesMessagesReactionsDelete) | **DELETE** /v1/{name} |  |
| [**chatSpacesMessagesReactionsList**](SpacesApi.md#chatSpacesMessagesReactionsList) | **GET** /v1/{parent}/reactions |  |
| [**chatSpacesMessagesUpdate**](SpacesApi.md#chatSpacesMessagesUpdate) | **PUT** /v1/{name} |  |
| [**chatSpacesSetup**](SpacesApi.md#chatSpacesSetup) | **POST** /v1/spaces:setup |  |


<a id="chatSpacesCompleteImport"></a>
# **chatSpacesCompleteImport**
> CompleteImportSpaceResponse chatSpacesCompleteImport(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, body)



Completes the [import process](https://developers.google.com/chat/api/guides/import-data) for the specified space and makes it visible to users. Requires app authentication and domain-wide delegation. For more information, see [Authorize Google Chat apps to import data](https://developers.google.com/chat/api/guides/authorize-import).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String name = "name_example"; // String | Required. Resource name of the import mode space. Format: `spaces/{space}`
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Object body = null; // Object | 
    try {
      CompleteImportSpaceResponse result = apiInstance.chatSpacesCompleteImport(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#chatSpacesCompleteImport");
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
| **name** | **String**| Required. Resource name of the import mode space. Format: &#x60;spaces/{space}&#x60; | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **body** | **Object**|  | [optional] |

### Return type

[**CompleteImportSpaceResponse**](CompleteImportSpaceResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="chatSpacesCreate"></a>
# **chatSpacesCreate**
> Space chatSpacesCreate($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, requestId, space)



Creates a named space. Spaces grouped by topics aren&#39;t supported. For an example, see [Create a space](https://developers.google.com/chat/api/guides/v1/spaces/create). If you receive the error message &#x60;ALREADY_EXISTS&#x60; when creating a space, try a different &#x60;displayName&#x60;. An existing space within the Google Workspace organization might already use this display name. Requires [user authentication](https://developers.google.com/chat/api/guides/auth/users).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String requestId = "requestId_example"; // String | Optional. A unique identifier for this request. A random UUID is recommended. Specifying an existing request ID returns the space created with that ID instead of creating a new space. Specifying an existing request ID from the same Chat app with a different authenticated user returns an error.
    Space space = new Space(); // Space | 
    try {
      Space result = apiInstance.chatSpacesCreate($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, requestId, space);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#chatSpacesCreate");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **requestId** | **String**| Optional. A unique identifier for this request. A random UUID is recommended. Specifying an existing request ID returns the space created with that ID instead of creating a new space. Specifying an existing request ID from the same Chat app with a different authenticated user returns an error. | [optional] |
| **space** | [**Space**](Space.md)|  | [optional] |

### Return type

[**Space**](Space.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="chatSpacesFindDirectMessage"></a>
# **chatSpacesFindDirectMessage**
> Space chatSpacesFindDirectMessage($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, name)



Returns the existing direct message with the specified user. If no direct message space is found, returns a &#x60;404 NOT_FOUND&#x60; error. For an example, see [Find a direct message](/chat/api/guides/v1/spaces/find-direct-message). With [user authentication](https://developers.google.com/chat/api/guides/auth/users), returns the direct message space between the specified user and the authenticated user. With [app authentication](https://developers.google.com/chat/api/guides/auth/service-accounts), returns the direct message space between the specified user and the calling Chat app. Requires [user authentication](https://developers.google.com/chat/api/guides/auth/users) or [app authentication](https://developers.google.com/chat/api/guides/auth/service-accounts).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String name = "name_example"; // String | Required. Resource name of the user to find direct message with. Format: `users/{user}`, where `{user}` is either the `id` for the [person](https://developers.google.com/people/api/rest/v1/people) from the People API, or the `id` for the [user](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users) in the Directory API. For example, if the People API profile ID is `123456789`, you can find a direct message with that person by using `users/123456789` as the `name`. When [authenticated as a user](https://developers.google.com/chat/api/guides/auth/users), you can use the email as an alias for `{user}`. For example, `users/example@gmail.com` where `example@gmail.com` is the email of the Google Chat user.
    try {
      Space result = apiInstance.chatSpacesFindDirectMessage($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#chatSpacesFindDirectMessage");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **name** | **String**| Required. Resource name of the user to find direct message with. Format: &#x60;users/{user}&#x60;, where &#x60;{user}&#x60; is either the &#x60;id&#x60; for the [person](https://developers.google.com/people/api/rest/v1/people) from the People API, or the &#x60;id&#x60; for the [user](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users) in the Directory API. For example, if the People API profile ID is &#x60;123456789&#x60;, you can find a direct message with that person by using &#x60;users/123456789&#x60; as the &#x60;name&#x60;. When [authenticated as a user](https://developers.google.com/chat/api/guides/auth/users), you can use the email as an alias for &#x60;{user}&#x60;. For example, &#x60;users/example@gmail.com&#x60; where &#x60;example@gmail.com&#x60; is the email of the Google Chat user. | [optional] |

### Return type

[**Space**](Space.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="chatSpacesList"></a>
# **chatSpacesList**
> ListSpacesResponse chatSpacesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken)



Lists spaces the caller is a member of. Group chats and DMs aren&#39;t listed until the first message is sent. For an example, see [List spaces](https://developers.google.com/chat/api/guides/v1/spaces/list). Requires [authentication](https://developers.google.com/chat/api/guides/auth). Supports [app authentication](https://developers.google.com/chat/api/guides/auth/service-accounts) and [user authentication](https://developers.google.com/chat/api/guides/auth/users). Lists spaces visible to the caller or authenticated user. Group chats and DMs aren&#39;t listed until the first message is sent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String filter = "filter_example"; // String | Optional. A query filter. You can filter spaces by the space type ([`space_type`](https://developers.google.com/chat/api/reference/rest/v1/spaces#spacetype)). To filter by space type, you must specify valid enum value, such as `SPACE` or `GROUP_CHAT` (the `space_type` can't be `SPACE_TYPE_UNSPECIFIED`). To query for multiple space types, use the `OR` operator. For example, the following queries are valid: ``` space_type = \"SPACE\" spaceType = \"GROUP_CHAT\" OR spaceType = \"DIRECT_MESSAGE\" ``` Invalid queries are rejected by the server with an `INVALID_ARGUMENT` error.
    Integer pageSize = 56; // Integer | Optional. The maximum number of spaces to return. The service might return fewer than this value. If unspecified, at most 100 spaces are returned. The maximum value is 1,000. If you use a value more than 1,000, it's automatically changed to 1,000. Negative values return an `INVALID_ARGUMENT` error.
    String pageToken = "pageToken_example"; // String | Optional. A page token, received from a previous list spaces call. Provide this parameter to retrieve the subsequent page. When paginating, the filter value should match the call that provided the page token. Passing a different value may lead to unexpected results.
    try {
      ListSpacesResponse result = apiInstance.chatSpacesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#chatSpacesList");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **filter** | **String**| Optional. A query filter. You can filter spaces by the space type ([&#x60;space_type&#x60;](https://developers.google.com/chat/api/reference/rest/v1/spaces#spacetype)). To filter by space type, you must specify valid enum value, such as &#x60;SPACE&#x60; or &#x60;GROUP_CHAT&#x60; (the &#x60;space_type&#x60; can&#39;t be &#x60;SPACE_TYPE_UNSPECIFIED&#x60;). To query for multiple space types, use the &#x60;OR&#x60; operator. For example, the following queries are valid: &#x60;&#x60;&#x60; space_type &#x3D; \&quot;SPACE\&quot; spaceType &#x3D; \&quot;GROUP_CHAT\&quot; OR spaceType &#x3D; \&quot;DIRECT_MESSAGE\&quot; &#x60;&#x60;&#x60; Invalid queries are rejected by the server with an &#x60;INVALID_ARGUMENT&#x60; error. | [optional] |
| **pageSize** | **Integer**| Optional. The maximum number of spaces to return. The service might return fewer than this value. If unspecified, at most 100 spaces are returned. The maximum value is 1,000. If you use a value more than 1,000, it&#39;s automatically changed to 1,000. Negative values return an &#x60;INVALID_ARGUMENT&#x60; error. | [optional] |
| **pageToken** | **String**| Optional. A page token, received from a previous list spaces call. Provide this parameter to retrieve the subsequent page. When paginating, the filter value should match the call that provided the page token. Passing a different value may lead to unexpected results. | [optional] |

### Return type

[**ListSpacesResponse**](ListSpacesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="chatSpacesMembersCreate"></a>
# **chatSpacesMembersCreate**
> Membership chatSpacesMembersCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, membership)



Creates a human membership or app membership for the calling app. Creating memberships for other apps isn&#39;t supported. For an example, see [ Create a membership](https://developers.google.com/chat/api/guides/v1/members/create). When creating a membership, if the specified member has their auto-accept policy turned off, then they&#39;re invited, and must accept the space invitation before joining. Otherwise, creating a membership adds the member directly to the specified space. Requires [user authentication](https://developers.google.com/chat/api/guides/auth/users). To specify the member to add, set the &#x60;membership.member.name&#x60; in the &#x60;CreateMembershipRequest&#x60;: - To add the calling app to a space or a direct message between two human users, use &#x60;users/app&#x60;. Unable to add other apps to the space. - To add a human user, use &#x60;users/{user}&#x60;, where &#x60;{user}&#x60; can be the email address for the user. For users in the same Workspace organization &#x60;{user}&#x60; can also be the &#x60;id&#x60; for the person from the People API, or the &#x60;id&#x60; for the user in the Directory API. For example, if the People API Person profile ID for &#x60;user@example.com&#x60; is &#x60;123456789&#x60;, you can add the user to the space by setting the &#x60;membership.member.name&#x60; to &#x60;users/user@example.com&#x60; or &#x60;users/123456789&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String parent = "parent_example"; // String | Required. The resource name of the space for which to create the membership. Format: spaces/{space}
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Membership membership = new Membership(); // Membership | 
    try {
      Membership result = apiInstance.chatSpacesMembersCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, membership);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#chatSpacesMembersCreate");
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
| **parent** | **String**| Required. The resource name of the space for which to create the membership. Format: spaces/{space} | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **membership** | [**Membership**](Membership.md)|  | [optional] |

### Return type

[**Membership**](Membership.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="chatSpacesMembersList"></a>
# **chatSpacesMembersList**
> ListMembershipsResponse chatSpacesMembersList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken, showGroups, showInvited)



Lists memberships in a space. For an example, see [List memberships](https://developers.google.com/chat/api/guides/v1/members/list). Listing memberships with [app authentication](https://developers.google.com/chat/api/guides/auth/service-accounts) lists memberships in spaces that the Chat app has access to, but excludes Chat app memberships, including its own. Listing memberships with [User authentication](https://developers.google.com/chat/api/guides/auth/users) lists memberships in spaces that the authenticated user has access to. Requires [authentication](https://developers.google.com/chat/api/guides/auth). Supports [app authentication](https://developers.google.com/chat/api/guides/auth/service-accounts) and [user authentication](https://developers.google.com/chat/api/guides/auth/users).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String parent = "parent_example"; // String | Required. The resource name of the space for which to fetch a membership list. Format: spaces/{space}
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String filter = "filter_example"; // String | Optional. A query filter. You can filter memberships by a member's role ([`role`](https://developers.google.com/chat/api/reference/rest/v1/spaces.members#membershiprole)) and type ([`member.type`](https://developers.google.com/chat/api/reference/rest/v1/User#type)). To filter by role, set `role` to `ROLE_MEMBER` or `ROLE_MANAGER`. To filter by type, set `member.type` to `HUMAN` or `BOT`. To filter by both role and type, use the `AND` operator. To filter by either role or type, use the `OR` operator. For example, the following queries are valid: ``` role = \"ROLE_MANAGER\" OR role = \"ROLE_MEMBER\" member.type = \"HUMAN\" AND role = \"ROLE_MANAGER\" ``` The following queries are invalid: ``` member.type = \"HUMAN\" AND member.type = \"BOT\" role = \"ROLE_MANAGER\" AND role = \"ROLE_MEMBER\" ``` Invalid queries are rejected by the server with an `INVALID_ARGUMENT` error.
    Integer pageSize = 56; // Integer | Optional. The maximum number of memberships to return. The service might return fewer than this value. If unspecified, at most 100 memberships are returned. The maximum value is 1,000. If you use a value more than 1,000, it's automatically changed to 1,000. Negative values return an `INVALID_ARGUMENT` error.
    String pageToken = "pageToken_example"; // String | Optional. A page token, received from a previous call to list memberships. Provide this parameter to retrieve the subsequent page. When paginating, all other parameters provided should match the call that provided the page token. Passing different values to the other parameters might lead to unexpected results.
    Boolean showGroups = true; // Boolean | Optional. When `true`, also returns memberships associated with a Google Group, in addition to other types of memberships. If a filter is set, Google Group memberships that don't match the filter criteria aren't returned.
    Boolean showInvited = true; // Boolean | Optional. When `true`, also returns memberships associated with invited members, in addition to other types of memberships. If a filter is set, invited memberships that don't match the filter criteria aren't returned. Currently requires [user authentication](https://developers.google.com/chat/api/guides/auth/users).
    try {
      ListMembershipsResponse result = apiInstance.chatSpacesMembersList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken, showGroups, showInvited);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#chatSpacesMembersList");
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
| **parent** | **String**| Required. The resource name of the space for which to fetch a membership list. Format: spaces/{space} | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **filter** | **String**| Optional. A query filter. You can filter memberships by a member&#39;s role ([&#x60;role&#x60;](https://developers.google.com/chat/api/reference/rest/v1/spaces.members#membershiprole)) and type ([&#x60;member.type&#x60;](https://developers.google.com/chat/api/reference/rest/v1/User#type)). To filter by role, set &#x60;role&#x60; to &#x60;ROLE_MEMBER&#x60; or &#x60;ROLE_MANAGER&#x60;. To filter by type, set &#x60;member.type&#x60; to &#x60;HUMAN&#x60; or &#x60;BOT&#x60;. To filter by both role and type, use the &#x60;AND&#x60; operator. To filter by either role or type, use the &#x60;OR&#x60; operator. For example, the following queries are valid: &#x60;&#x60;&#x60; role &#x3D; \&quot;ROLE_MANAGER\&quot; OR role &#x3D; \&quot;ROLE_MEMBER\&quot; member.type &#x3D; \&quot;HUMAN\&quot; AND role &#x3D; \&quot;ROLE_MANAGER\&quot; &#x60;&#x60;&#x60; The following queries are invalid: &#x60;&#x60;&#x60; member.type &#x3D; \&quot;HUMAN\&quot; AND member.type &#x3D; \&quot;BOT\&quot; role &#x3D; \&quot;ROLE_MANAGER\&quot; AND role &#x3D; \&quot;ROLE_MEMBER\&quot; &#x60;&#x60;&#x60; Invalid queries are rejected by the server with an &#x60;INVALID_ARGUMENT&#x60; error. | [optional] |
| **pageSize** | **Integer**| Optional. The maximum number of memberships to return. The service might return fewer than this value. If unspecified, at most 100 memberships are returned. The maximum value is 1,000. If you use a value more than 1,000, it&#39;s automatically changed to 1,000. Negative values return an &#x60;INVALID_ARGUMENT&#x60; error. | [optional] |
| **pageToken** | **String**| Optional. A page token, received from a previous call to list memberships. Provide this parameter to retrieve the subsequent page. When paginating, all other parameters provided should match the call that provided the page token. Passing different values to the other parameters might lead to unexpected results. | [optional] |
| **showGroups** | **Boolean**| Optional. When &#x60;true&#x60;, also returns memberships associated with a Google Group, in addition to other types of memberships. If a filter is set, Google Group memberships that don&#39;t match the filter criteria aren&#39;t returned. | [optional] |
| **showInvited** | **Boolean**| Optional. When &#x60;true&#x60;, also returns memberships associated with invited members, in addition to other types of memberships. If a filter is set, invited memberships that don&#39;t match the filter criteria aren&#39;t returned. Currently requires [user authentication](https://developers.google.com/chat/api/guides/auth/users). | [optional] |

### Return type

[**ListMembershipsResponse**](ListMembershipsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="chatSpacesMessagesAttachmentsGet"></a>
# **chatSpacesMessagesAttachmentsGet**
> Attachment chatSpacesMessagesAttachmentsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Gets the metadata of a message attachment. The attachment data is fetched using the [media API](https://developers.google.com/chat/api/reference/rest/v1/media/download). For an example, see [Get a message attachment](https://developers.google.com/chat/api/guides/v1/media-and-attachments/get). Requires [app authentication](https://developers.google.com/chat/api/guides/auth/service-accounts).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String name = "name_example"; // String | Required. Resource name of the attachment, in the form `spaces/_*_/messages/_*_/attachments/_*`.
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    try {
      Attachment result = apiInstance.chatSpacesMessagesAttachmentsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#chatSpacesMessagesAttachmentsGet");
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
| **name** | **String**| Required. Resource name of the attachment, in the form &#x60;spaces/_*_/messages/_*_/attachments/_*&#x60;. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |

### Return type

[**Attachment**](Attachment.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="chatSpacesMessagesCreate"></a>
# **chatSpacesMessagesCreate**
> Message chatSpacesMessagesCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, messageId, messageReplyOption, requestId, threadKey, message)



Creates a message in a Google Chat space. For an example, see [Create a message](https://developers.google.com/chat/api/guides/v1/messages/create). Calling this method requires [authentication](https://developers.google.com/chat/api/guides/auth) and supports the following authentication types: - For text messages, user authentication or app authentication are supported. - For card messages, only app authentication is supported. (Only Chat apps can create card messages.)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String parent = "parent_example"; // String | Required. The resource name of the space in which to create a message. Format: `spaces/{space}`
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String messageId = "messageId_example"; // String | Optional. A custom ID for a message. Lets Chat apps get, update, or delete a message without needing to store the system-assigned ID in the message's resource name (represented in the message `name` field). The value for this field must meet the following requirements: * Begins with `client-`. For example, `client-custom-name` is a valid custom ID, but `custom-name` is not. * Contains up to 63 characters and only lowercase letters, numbers, and hyphens. * Is unique within a space. A Chat app can't use the same custom ID for different messages. For details, see [Name a message](https://developers.google.com/chat/api/guides/v1/messages/create#name_a_created_message).
    String messageReplyOption = "MESSAGE_REPLY_OPTION_UNSPECIFIED"; // String | Optional. Specifies whether a message starts a thread or replies to one. Only supported in named spaces.
    String requestId = "requestId_example"; // String | Optional. A unique request ID for this message. Specifying an existing request ID returns the message created with that ID instead of creating a new message.
    String threadKey = "threadKey_example"; // String | Optional. Deprecated: Use thread.thread_key instead. ID for the thread. Supports up to 4000 characters. To start or add to a thread, create a message and specify a `threadKey` or the thread.name. For example usage, see [Start or reply to a message thread](https://developers.google.com/chat/api/guides/v1/messages/create#create-message-thread).
    Message message = new Message(); // Message | 
    try {
      Message result = apiInstance.chatSpacesMessagesCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, messageId, messageReplyOption, requestId, threadKey, message);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#chatSpacesMessagesCreate");
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
| **parent** | **String**| Required. The resource name of the space in which to create a message. Format: &#x60;spaces/{space}&#x60; | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **messageId** | **String**| Optional. A custom ID for a message. Lets Chat apps get, update, or delete a message without needing to store the system-assigned ID in the message&#39;s resource name (represented in the message &#x60;name&#x60; field). The value for this field must meet the following requirements: * Begins with &#x60;client-&#x60;. For example, &#x60;client-custom-name&#x60; is a valid custom ID, but &#x60;custom-name&#x60; is not. * Contains up to 63 characters and only lowercase letters, numbers, and hyphens. * Is unique within a space. A Chat app can&#39;t use the same custom ID for different messages. For details, see [Name a message](https://developers.google.com/chat/api/guides/v1/messages/create#name_a_created_message). | [optional] |
| **messageReplyOption** | **String**| Optional. Specifies whether a message starts a thread or replies to one. Only supported in named spaces. | [optional] [enum: MESSAGE_REPLY_OPTION_UNSPECIFIED, REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD, REPLY_MESSAGE_OR_FAIL] |
| **requestId** | **String**| Optional. A unique request ID for this message. Specifying an existing request ID returns the message created with that ID instead of creating a new message. | [optional] |
| **threadKey** | **String**| Optional. Deprecated: Use thread.thread_key instead. ID for the thread. Supports up to 4000 characters. To start or add to a thread, create a message and specify a &#x60;threadKey&#x60; or the thread.name. For example usage, see [Start or reply to a message thread](https://developers.google.com/chat/api/guides/v1/messages/create#create-message-thread). | [optional] |
| **message** | [**Message**](Message.md)|  | [optional] |

### Return type

[**Message**](Message.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="chatSpacesMessagesList"></a>
# **chatSpacesMessagesList**
> ListMessagesResponse chatSpacesMessagesList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, orderBy, pageSize, pageToken, showDeleted)



Lists messages in a space that the caller is a member of, including messages from blocked members and spaces. For an example, see [List messages](/chat/api/guides/v1/messages/list). Requires [user authentication](https://developers.google.com/chat/api/guides/auth/users).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String parent = "parent_example"; // String | Required. The resource name of the space to list messages from. Format: `spaces/{space}`
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String filter = "filter_example"; // String | A query filter. You can filter messages by date (`create_time`) and thread (`thread.name`). To filter messages by the date they were created, specify the `create_time` with a timestamp in [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339) format and double quotation marks. For example, `\"2023-04-21T11:30:00-04:00\"`. You can use the greater than operator `>` to list messages that were created after a timestamp, or the less than operator `<` to list messages that were created before a timestamp. To filter messages within a time interval, use the `AND` operator between two timestamps. To filter by thread, specify the `thread.name`, formatted as `spaces/{space}/threads/{thread}`. You can only specify one `thread.name` per query. To filter by both thread and date, use the `AND` operator in your query. For example, the following queries are valid: ``` create_time > \"2012-04-21T11:30:00-04:00\" create_time > \"2012-04-21T11:30:00-04:00\" AND thread.name = spaces/AAAAAAAAAAA/threads/123 create_time > \"2012-04-21T11:30:00+00:00\" AND create_time < \"2013-01-01T00:00:00+00:00\" AND thread.name = spaces/AAAAAAAAAAA/threads/123 thread.name = spaces/AAAAAAAAAAA/threads/123 ``` Invalid queries are rejected by the server with an `INVALID_ARGUMENT` error.
    String orderBy = "orderBy_example"; // String | Optional, if resuming from a previous query. How the list of messages is ordered. Specify a value to order by an ordering operation. Valid ordering operation values are as follows: - `ASC` for ascending. - `DESC` for descending. The default ordering is `create_time ASC`.
    Integer pageSize = 56; // Integer | The maximum number of messages returned. The service might return fewer messages than this value. If unspecified, at most 25 are returned. The maximum value is 1,000. If you use a value more than 1,000, it's automatically changed to 1,000. Negative values return an `INVALID_ARGUMENT` error.
    String pageToken = "pageToken_example"; // String | Optional, if resuming from a previous query. A page token received from a previous list messages call. Provide this parameter to retrieve the subsequent page. When paginating, all other parameters provided should match the call that provided the page token. Passing different values to the other parameters might lead to unexpected results.
    Boolean showDeleted = true; // Boolean | Whether to include deleted messages. Deleted messages include deleted time and metadata about their deletion, but message content is unavailable.
    try {
      ListMessagesResponse result = apiInstance.chatSpacesMessagesList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, orderBy, pageSize, pageToken, showDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#chatSpacesMessagesList");
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
| **parent** | **String**| Required. The resource name of the space to list messages from. Format: &#x60;spaces/{space}&#x60; | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **filter** | **String**| A query filter. You can filter messages by date (&#x60;create_time&#x60;) and thread (&#x60;thread.name&#x60;). To filter messages by the date they were created, specify the &#x60;create_time&#x60; with a timestamp in [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339) format and double quotation marks. For example, &#x60;\&quot;2023-04-21T11:30:00-04:00\&quot;&#x60;. You can use the greater than operator &#x60;&gt;&#x60; to list messages that were created after a timestamp, or the less than operator &#x60;&lt;&#x60; to list messages that were created before a timestamp. To filter messages within a time interval, use the &#x60;AND&#x60; operator between two timestamps. To filter by thread, specify the &#x60;thread.name&#x60;, formatted as &#x60;spaces/{space}/threads/{thread}&#x60;. You can only specify one &#x60;thread.name&#x60; per query. To filter by both thread and date, use the &#x60;AND&#x60; operator in your query. For example, the following queries are valid: &#x60;&#x60;&#x60; create_time &gt; \&quot;2012-04-21T11:30:00-04:00\&quot; create_time &gt; \&quot;2012-04-21T11:30:00-04:00\&quot; AND thread.name &#x3D; spaces/AAAAAAAAAAA/threads/123 create_time &gt; \&quot;2012-04-21T11:30:00+00:00\&quot; AND create_time &lt; \&quot;2013-01-01T00:00:00+00:00\&quot; AND thread.name &#x3D; spaces/AAAAAAAAAAA/threads/123 thread.name &#x3D; spaces/AAAAAAAAAAA/threads/123 &#x60;&#x60;&#x60; Invalid queries are rejected by the server with an &#x60;INVALID_ARGUMENT&#x60; error. | [optional] |
| **orderBy** | **String**| Optional, if resuming from a previous query. How the list of messages is ordered. Specify a value to order by an ordering operation. Valid ordering operation values are as follows: - &#x60;ASC&#x60; for ascending. - &#x60;DESC&#x60; for descending. The default ordering is &#x60;create_time ASC&#x60;. | [optional] |
| **pageSize** | **Integer**| The maximum number of messages returned. The service might return fewer messages than this value. If unspecified, at most 25 are returned. The maximum value is 1,000. If you use a value more than 1,000, it&#39;s automatically changed to 1,000. Negative values return an &#x60;INVALID_ARGUMENT&#x60; error. | [optional] |
| **pageToken** | **String**| Optional, if resuming from a previous query. A page token received from a previous list messages call. Provide this parameter to retrieve the subsequent page. When paginating, all other parameters provided should match the call that provided the page token. Passing different values to the other parameters might lead to unexpected results. | [optional] |
| **showDeleted** | **Boolean**| Whether to include deleted messages. Deleted messages include deleted time and metadata about their deletion, but message content is unavailable. | [optional] |

### Return type

[**ListMessagesResponse**](ListMessagesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="chatSpacesMessagesPatch"></a>
# **chatSpacesMessagesPatch**
> Message chatSpacesMessagesPatch(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, allowMissing, updateMask, message)



Updates a message. There&#39;s a difference between the &#x60;patch&#x60; and &#x60;update&#x60; methods. The &#x60;patch&#x60; method uses a &#x60;patch&#x60; request while the &#x60;update&#x60; method uses a &#x60;put&#x60; request. We recommend using the &#x60;patch&#x60; method. For an example, see [Update a message](https://developers.google.com/chat/api/guides/v1/messages/update). Requires [authentication](https://developers.google.com/chat/api/guides/auth). Supports [app authentication](https://developers.google.com/chat/api/guides/auth/service-accounts) and [user authentication](https://developers.google.com/chat/api/guides/auth/users). When using app authentication, requests can only update messages created by the calling Chat app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String name = "name_example"; // String | Resource name of the message. Format: `spaces/{space}/messages/{message}` Where `{space}` is the ID of the space where the message is posted and `{message}` is a system-assigned ID for the message. For example, `spaces/AAAAAAAAAAA/messages/BBBBBBBBBBB.BBBBBBBBBBB`. If you set a custom ID when you create a message, you can use this ID to specify the message in a request by replacing `{message}` with the value from the `clientAssignedMessageId` field. For example, `spaces/AAAAAAAAAAA/messages/client-custom-name`. For details, see [Name a message](https://developers.google.com/chat/api/guides/v1/messages/create#name_a_created_message).
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Boolean allowMissing = true; // Boolean | Optional. If `true` and the message isn't found, a new message is created and `updateMask` is ignored. The specified message ID must be [client-assigned](https://developers.google.com/chat/api/guides/v1/messages/create#name_a_created_message) or the request fails.
    String updateMask = "updateMask_example"; // String | Required. The field paths to update. Separate multiple values with commas or use `*` to update all field paths. Currently supported field paths: - `text` - `attachment` - `cards` (Requires [app authentication](/chat/api/guides/auth/service-accounts).) - `cards_v2` (Requires [app authentication](/chat/api/guides/auth/service-accounts).) - Developer Preview: `accessory_widgets` (Requires [app authentication](/chat/api/guides/auth/service-accounts).)
    Message message = new Message(); // Message | 
    try {
      Message result = apiInstance.chatSpacesMessagesPatch(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, allowMissing, updateMask, message);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#chatSpacesMessagesPatch");
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
| **name** | **String**| Resource name of the message. Format: &#x60;spaces/{space}/messages/{message}&#x60; Where &#x60;{space}&#x60; is the ID of the space where the message is posted and &#x60;{message}&#x60; is a system-assigned ID for the message. For example, &#x60;spaces/AAAAAAAAAAA/messages/BBBBBBBBBBB.BBBBBBBBBBB&#x60;. If you set a custom ID when you create a message, you can use this ID to specify the message in a request by replacing &#x60;{message}&#x60; with the value from the &#x60;clientAssignedMessageId&#x60; field. For example, &#x60;spaces/AAAAAAAAAAA/messages/client-custom-name&#x60;. For details, see [Name a message](https://developers.google.com/chat/api/guides/v1/messages/create#name_a_created_message). | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **allowMissing** | **Boolean**| Optional. If &#x60;true&#x60; and the message isn&#39;t found, a new message is created and &#x60;updateMask&#x60; is ignored. The specified message ID must be [client-assigned](https://developers.google.com/chat/api/guides/v1/messages/create#name_a_created_message) or the request fails. | [optional] |
| **updateMask** | **String**| Required. The field paths to update. Separate multiple values with commas or use &#x60;*&#x60; to update all field paths. Currently supported field paths: - &#x60;text&#x60; - &#x60;attachment&#x60; - &#x60;cards&#x60; (Requires [app authentication](/chat/api/guides/auth/service-accounts).) - &#x60;cards_v2&#x60; (Requires [app authentication](/chat/api/guides/auth/service-accounts).) - Developer Preview: &#x60;accessory_widgets&#x60; (Requires [app authentication](/chat/api/guides/auth/service-accounts).) | [optional] |
| **message** | [**Message**](Message.md)|  | [optional] |

### Return type

[**Message**](Message.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="chatSpacesMessagesReactionsCreate"></a>
# **chatSpacesMessagesReactionsCreate**
> Reaction chatSpacesMessagesReactionsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, reaction)



Creates a reaction and adds it to a message. For an example, see [Create a reaction](https://developers.google.com/chat/api/guides/v1/reactions/create). Requires [user authentication](https://developers.google.com/chat/api/guides/auth/users). Only unicode emoji are supported.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String parent = "parent_example"; // String | Required. The message where the reaction is created. Format: `spaces/{space}/messages/{message}`
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Reaction reaction = new Reaction(); // Reaction | 
    try {
      Reaction result = apiInstance.chatSpacesMessagesReactionsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, reaction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#chatSpacesMessagesReactionsCreate");
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
| **parent** | **String**| Required. The message where the reaction is created. Format: &#x60;spaces/{space}/messages/{message}&#x60; | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **reaction** | [**Reaction**](Reaction.md)|  | [optional] |

### Return type

[**Reaction**](Reaction.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="chatSpacesMessagesReactionsDelete"></a>
# **chatSpacesMessagesReactionsDelete**
> Object chatSpacesMessagesReactionsDelete(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, force)



Deletes a reaction to a message. For an example, see [Delete a reaction](https://developers.google.com/chat/api/guides/v1/reactions/delete). Requires [user authentication](https://developers.google.com/chat/api/guides/auth/users).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String name = "name_example"; // String | Required. Name of the reaction to delete. Format: `spaces/{space}/messages/{message}/reactions/{reaction}`
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Boolean force = true; // Boolean | When `true`, deleting a message also deletes its threaded replies. When `false`, if a message has threaded replies, deletion fails. Only applies when [authenticating as a user](https://developers.google.com/chat/api/guides/auth/users). Has no effect when [authenticating as a Chat app] (https://developers.google.com/chat/api/guides/auth/service-accounts).
    try {
      Object result = apiInstance.chatSpacesMessagesReactionsDelete(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, force);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#chatSpacesMessagesReactionsDelete");
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
| **name** | **String**| Required. Name of the reaction to delete. Format: &#x60;spaces/{space}/messages/{message}/reactions/{reaction}&#x60; | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **force** | **Boolean**| When &#x60;true&#x60;, deleting a message also deletes its threaded replies. When &#x60;false&#x60;, if a message has threaded replies, deletion fails. Only applies when [authenticating as a user](https://developers.google.com/chat/api/guides/auth/users). Has no effect when [authenticating as a Chat app] (https://developers.google.com/chat/api/guides/auth/service-accounts). | [optional] |

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="chatSpacesMessagesReactionsList"></a>
# **chatSpacesMessagesReactionsList**
> ListReactionsResponse chatSpacesMessagesReactionsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken)



Lists reactions to a message. For an example, see [List reactions](https://developers.google.com/chat/api/guides/v1/reactions/list). Requires [user authentication](https://developers.google.com/chat/api/guides/auth/users).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String parent = "parent_example"; // String | Required. The message users reacted to. Format: `spaces/{space}/messages/{message}`
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String filter = "filter_example"; // String | Optional. A query filter. You can filter reactions by [emoji](https://developers.google.com/chat/api/reference/rest/v1/Emoji) (either `emoji.unicode` or `emoji.custom_emoji.uid`) and [user](https://developers.google.com/chat/api/reference/rest/v1/User) (`user.name`). To filter reactions for multiple emojis or users, join similar fields with the `OR` operator, such as `emoji.unicode = \"🙂\" OR emoji.unicode = \"👍\"` and `user.name = \"users/AAAAAA\" OR user.name = \"users/BBBBBB\"`. To filter reactions by emoji and user, use the `AND` operator, such as `emoji.unicode = \"🙂\" AND user.name = \"users/AAAAAA\"`. If your query uses both `AND` and `OR`, group them with parentheses. For example, the following queries are valid: ``` user.name = \"users/{user}\" emoji.unicode = \"🙂\" emoji.custom_emoji.uid = \"{uid}\" emoji.unicode = \"🙂\" OR emoji.unicode = \"👍\" emoji.unicode = \"🙂\" OR emoji.custom_emoji.uid = \"{uid}\" emoji.unicode = \"🙂\" AND user.name = \"users/{user}\" (emoji.unicode = \"🙂\" OR emoji.custom_emoji.uid = \"{uid}\") AND user.name = \"users/{user}\" ``` The following queries are invalid: ``` emoji.unicode = \"🙂\" AND emoji.unicode = \"👍\" emoji.unicode = \"🙂\" AND emoji.custom_emoji.uid = \"{uid}\" emoji.unicode = \"🙂\" OR user.name = \"users/{user}\" emoji.unicode = \"🙂\" OR emoji.custom_emoji.uid = \"{uid}\" OR user.name = \"users/{user}\" emoji.unicode = \"🙂\" OR emoji.custom_emoji.uid = \"{uid}\" AND user.name = \"users/{user}\" ``` Invalid queries are rejected by the server with an `INVALID_ARGUMENT` error.
    Integer pageSize = 56; // Integer | Optional. The maximum number of reactions returned. The service can return fewer reactions than this value. If unspecified, the default value is 25. The maximum value is 200; values above 200 are changed to 200.
    String pageToken = "pageToken_example"; // String | Optional. (If resuming from a previous query.) A page token received from a previous list reactions call. Provide this to retrieve the subsequent page. When paginating, the filter value should match the call that provided the page token. Passing a different value might lead to unexpected results.
    try {
      ListReactionsResponse result = apiInstance.chatSpacesMessagesReactionsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#chatSpacesMessagesReactionsList");
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
| **parent** | **String**| Required. The message users reacted to. Format: &#x60;spaces/{space}/messages/{message}&#x60; | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **filter** | **String**| Optional. A query filter. You can filter reactions by [emoji](https://developers.google.com/chat/api/reference/rest/v1/Emoji) (either &#x60;emoji.unicode&#x60; or &#x60;emoji.custom_emoji.uid&#x60;) and [user](https://developers.google.com/chat/api/reference/rest/v1/User) (&#x60;user.name&#x60;). To filter reactions for multiple emojis or users, join similar fields with the &#x60;OR&#x60; operator, such as &#x60;emoji.unicode &#x3D; \&quot;🙂\&quot; OR emoji.unicode &#x3D; \&quot;👍\&quot;&#x60; and &#x60;user.name &#x3D; \&quot;users/AAAAAA\&quot; OR user.name &#x3D; \&quot;users/BBBBBB\&quot;&#x60;. To filter reactions by emoji and user, use the &#x60;AND&#x60; operator, such as &#x60;emoji.unicode &#x3D; \&quot;🙂\&quot; AND user.name &#x3D; \&quot;users/AAAAAA\&quot;&#x60;. If your query uses both &#x60;AND&#x60; and &#x60;OR&#x60;, group them with parentheses. For example, the following queries are valid: &#x60;&#x60;&#x60; user.name &#x3D; \&quot;users/{user}\&quot; emoji.unicode &#x3D; \&quot;🙂\&quot; emoji.custom_emoji.uid &#x3D; \&quot;{uid}\&quot; emoji.unicode &#x3D; \&quot;🙂\&quot; OR emoji.unicode &#x3D; \&quot;👍\&quot; emoji.unicode &#x3D; \&quot;🙂\&quot; OR emoji.custom_emoji.uid &#x3D; \&quot;{uid}\&quot; emoji.unicode &#x3D; \&quot;🙂\&quot; AND user.name &#x3D; \&quot;users/{user}\&quot; (emoji.unicode &#x3D; \&quot;🙂\&quot; OR emoji.custom_emoji.uid &#x3D; \&quot;{uid}\&quot;) AND user.name &#x3D; \&quot;users/{user}\&quot; &#x60;&#x60;&#x60; The following queries are invalid: &#x60;&#x60;&#x60; emoji.unicode &#x3D; \&quot;🙂\&quot; AND emoji.unicode &#x3D; \&quot;👍\&quot; emoji.unicode &#x3D; \&quot;🙂\&quot; AND emoji.custom_emoji.uid &#x3D; \&quot;{uid}\&quot; emoji.unicode &#x3D; \&quot;🙂\&quot; OR user.name &#x3D; \&quot;users/{user}\&quot; emoji.unicode &#x3D; \&quot;🙂\&quot; OR emoji.custom_emoji.uid &#x3D; \&quot;{uid}\&quot; OR user.name &#x3D; \&quot;users/{user}\&quot; emoji.unicode &#x3D; \&quot;🙂\&quot; OR emoji.custom_emoji.uid &#x3D; \&quot;{uid}\&quot; AND user.name &#x3D; \&quot;users/{user}\&quot; &#x60;&#x60;&#x60; Invalid queries are rejected by the server with an &#x60;INVALID_ARGUMENT&#x60; error. | [optional] |
| **pageSize** | **Integer**| Optional. The maximum number of reactions returned. The service can return fewer reactions than this value. If unspecified, the default value is 25. The maximum value is 200; values above 200 are changed to 200. | [optional] |
| **pageToken** | **String**| Optional. (If resuming from a previous query.) A page token received from a previous list reactions call. Provide this to retrieve the subsequent page. When paginating, the filter value should match the call that provided the page token. Passing a different value might lead to unexpected results. | [optional] |

### Return type

[**ListReactionsResponse**](ListReactionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="chatSpacesMessagesUpdate"></a>
# **chatSpacesMessagesUpdate**
> Message chatSpacesMessagesUpdate(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, allowMissing, updateMask, message)



Updates a message. There&#39;s a difference between the &#x60;patch&#x60; and &#x60;update&#x60; methods. The &#x60;patch&#x60; method uses a &#x60;patch&#x60; request while the &#x60;update&#x60; method uses a &#x60;put&#x60; request. We recommend using the &#x60;patch&#x60; method. For an example, see [Update a message](https://developers.google.com/chat/api/guides/v1/messages/update). Requires [authentication](https://developers.google.com/chat/api/guides/auth). Supports [app authentication](https://developers.google.com/chat/api/guides/auth/service-accounts) and [user authentication](https://developers.google.com/chat/api/guides/auth/users). When using app authentication, requests can only update messages created by the calling Chat app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String name = "name_example"; // String | Resource name of the message. Format: `spaces/{space}/messages/{message}` Where `{space}` is the ID of the space where the message is posted and `{message}` is a system-assigned ID for the message. For example, `spaces/AAAAAAAAAAA/messages/BBBBBBBBBBB.BBBBBBBBBBB`. If you set a custom ID when you create a message, you can use this ID to specify the message in a request by replacing `{message}` with the value from the `clientAssignedMessageId` field. For example, `spaces/AAAAAAAAAAA/messages/client-custom-name`. For details, see [Name a message](https://developers.google.com/chat/api/guides/v1/messages/create#name_a_created_message).
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Boolean allowMissing = true; // Boolean | Optional. If `true` and the message isn't found, a new message is created and `updateMask` is ignored. The specified message ID must be [client-assigned](https://developers.google.com/chat/api/guides/v1/messages/create#name_a_created_message) or the request fails.
    String updateMask = "updateMask_example"; // String | Required. The field paths to update. Separate multiple values with commas or use `*` to update all field paths. Currently supported field paths: - `text` - `attachment` - `cards` (Requires [app authentication](/chat/api/guides/auth/service-accounts).) - `cards_v2` (Requires [app authentication](/chat/api/guides/auth/service-accounts).) - Developer Preview: `accessory_widgets` (Requires [app authentication](/chat/api/guides/auth/service-accounts).)
    Message message = new Message(); // Message | 
    try {
      Message result = apiInstance.chatSpacesMessagesUpdate(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, allowMissing, updateMask, message);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#chatSpacesMessagesUpdate");
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
| **name** | **String**| Resource name of the message. Format: &#x60;spaces/{space}/messages/{message}&#x60; Where &#x60;{space}&#x60; is the ID of the space where the message is posted and &#x60;{message}&#x60; is a system-assigned ID for the message. For example, &#x60;spaces/AAAAAAAAAAA/messages/BBBBBBBBBBB.BBBBBBBBBBB&#x60;. If you set a custom ID when you create a message, you can use this ID to specify the message in a request by replacing &#x60;{message}&#x60; with the value from the &#x60;clientAssignedMessageId&#x60; field. For example, &#x60;spaces/AAAAAAAAAAA/messages/client-custom-name&#x60;. For details, see [Name a message](https://developers.google.com/chat/api/guides/v1/messages/create#name_a_created_message). | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **allowMissing** | **Boolean**| Optional. If &#x60;true&#x60; and the message isn&#39;t found, a new message is created and &#x60;updateMask&#x60; is ignored. The specified message ID must be [client-assigned](https://developers.google.com/chat/api/guides/v1/messages/create#name_a_created_message) or the request fails. | [optional] |
| **updateMask** | **String**| Required. The field paths to update. Separate multiple values with commas or use &#x60;*&#x60; to update all field paths. Currently supported field paths: - &#x60;text&#x60; - &#x60;attachment&#x60; - &#x60;cards&#x60; (Requires [app authentication](/chat/api/guides/auth/service-accounts).) - &#x60;cards_v2&#x60; (Requires [app authentication](/chat/api/guides/auth/service-accounts).) - Developer Preview: &#x60;accessory_widgets&#x60; (Requires [app authentication](/chat/api/guides/auth/service-accounts).) | [optional] |
| **message** | [**Message**](Message.md)|  | [optional] |

### Return type

[**Message**](Message.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="chatSpacesSetup"></a>
# **chatSpacesSetup**
> Space chatSpacesSetup($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, setUpSpaceRequest)



Creates a space and adds specified users to it. The calling user is automatically added to the space, and shouldn&#39;t be specified as a membership in the request. For an example, see [Set up a space](https://developers.google.com/chat/api/guides/v1/spaces/set-up). To specify the human members to add, add memberships with the appropriate &#x60;member.name&#x60; in the &#x60;SetUpSpaceRequest&#x60;. To add a human user, use &#x60;users/{user}&#x60;, where &#x60;{user}&#x60; can be the email address for the user. For users in the same Workspace organization &#x60;{user}&#x60; can also be the &#x60;id&#x60; for the person from the People API, or the &#x60;id&#x60; for the user in the Directory API. For example, if the People API Person profile ID for &#x60;user@example.com&#x60; is &#x60;123456789&#x60;, you can add the user to the space by setting the &#x60;membership.member.name&#x60; to &#x60;users/user@example.com&#x60; or &#x60;users/123456789&#x60;. For a space or group chat, if the caller blocks or is blocked by some members, then those members aren&#39;t added to the created space. To create a direct message (DM) between the calling user and another human user, specify exactly one membership to represent the human user. If one user blocks the other, the request fails and the DM isn&#39;t created. To create a DM between the calling user and the calling app, set &#x60;Space.singleUserBotDm&#x60; to &#x60;true&#x60; and don&#39;t specify any memberships. You can only use this method to set up a DM with the calling app. To add the calling app as a member of a space or an existing DM between two human users, see [create a membership](https://developers.google.com/chat/api/guides/v1/members/create). If a DM already exists between two users, even when one user blocks the other at the time a request is made, then the existing DM is returned. Spaces with threaded replies aren&#39;t supported. If you receive the error message &#x60;ALREADY_EXISTS&#x60; when setting up a space, try a different &#x60;displayName&#x60;. An existing space within the Google Workspace organization might already use this display name. Requires [user authentication](https://developers.google.com/chat/api/guides/auth/users).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://chat.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    SetUpSpaceRequest setUpSpaceRequest = new SetUpSpaceRequest(); // SetUpSpaceRequest | 
    try {
      Space result = apiInstance.chatSpacesSetup($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, setUpSpaceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#chatSpacesSetup");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **setUpSpaceRequest** | [**SetUpSpaceRequest**](SetUpSpaceRequest.md)|  | [optional] |

### Return type

[**Space**](Space.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

