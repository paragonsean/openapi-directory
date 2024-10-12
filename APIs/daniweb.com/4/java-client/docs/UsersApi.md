# UsersApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersGet**](UsersApi.md#usersGet) | **GET** /users |  |
| [**usersGet_0**](UsersApi.md#usersGet_0) | **GET** /users/~ |  |
| [**usersIDGet**](UsersApi.md#usersIDGet) | **GET** /users/{ID} |  |
| [**usersIDGroupsGet**](UsersApi.md#usersIDGroupsGet) | **GET** /users/{ID}/groups |  |
| [**usersIDGroupsMessagesGet**](UsersApi.md#usersIDGroupsMessagesGet) | **GET** /users/{ID}/groups/messages |  |
| [**usersIDMessagesPost**](UsersApi.md#usersIDMessagesPost) | **POST** /users/{ID}/messages |  |
| [**usersIDMetadataCollectionsGet**](UsersApi.md#usersIDMetadataCollectionsGet) | **GET** /users/{ID}/metadata/collections |  |
| [**usersIDMetadataGet**](UsersApi.md#usersIDMetadataGet) | **GET** /users/{ID}/metadata |  |
| [**usersIDMetadataPost**](UsersApi.md#usersIDMetadataPost) | **POST** /users/{ID}/metadata |  |
| [**usersIDPositionsGet**](UsersApi.md#usersIDPositionsGet) | **GET** /users/{ID}/positions |  |
| [**usersIDSynergiesGet**](UsersApi.md#usersIDSynergiesGet) | **GET** /users/{ID}/synergies |  |
| [**usersIDSynergiesPatch**](UsersApi.md#usersIDSynergiesPatch) | **PATCH** /users/{ID}/synergies |  |
| [**usersInvitesPost**](UsersApi.md#usersInvitesPost) | **POST** /users/invites |  |
| [**usersMetadataFiltersPost**](UsersApi.md#usersMetadataFiltersPost) | **POST** /users/metadata/filters |  |
| [**usersNearbyGet**](UsersApi.md#usersNearbyGet) | **GET** /users/nearby |  |
| [**usersPatch**](UsersApi.md#usersPatch) | **PATCH** /users/~ |  |
| [**usersSearchesPost**](UsersApi.md#usersSearchesPost) | **POST** /users/searches |  |


<a id="usersGet"></a>
# **usersGet**
> EndpointGetUsers usersGet(filter, orderBy, bubbled, offset, limit)



Fetch an array of users that you&#39;ve been matched with, connected with, skipped, or muted. You can only retrieve users existing within the current access token&#39;s bubble. This report may be limited to the last ~500-1000 users you&#39;ve communicated with within the access token&#39;s bubble. Matches are always ordered by synergy, and the order_by parameter is ignored. You can only retrieve bubbled users when retrieving matches, and the bubbled parameter is ignored otherwise. Your 100 best algorithmic matches are based on: Complementary data submitted to Profiles, CVs, and Metadata; Complementary data acquired from third-parties; Location information; Many behavioral data points, such as how responsive users are to connections; Degrees of separation (mutual connections); etc. You may connect with 3 of these algorithmic matches per day for free. However, new members are allowed a grace period of additional daily matches. Each time you choose to meet or mute one of your algorithmic matches, a new match is introduced.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

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

    UsersApi apiInstance = new UsersApi(defaultClient);
    String filter = "connections"; // String | 
    String orderBy = "id"; // String | 
    Boolean bubbled = false; // Boolean | 
    Integer offset = 0; // Integer | 
    Integer limit = 50; // Integer | 
    try {
      EndpointGetUsers result = apiInstance.usersGet(filter, orderBy, bubbled, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersGet");
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
| **filter** | **String**|  | [optional] [default to connections] [enum: connections, matches, skipped, muted] |
| **orderBy** | **String**|  | [optional] [default to id] [enum: id, last_activity, first_name, last_name, industry] |
| **bubbled** | **Boolean**|  | [optional] [default to false] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**EndpointGetUsers**](EndpointGetUsers.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="usersGet_0"></a>
# **usersGet_0**
> EndpointGetUsers usersGet_0()



Retrieve the currently OAuth&#39;ed end-user, based on the access token being used, including private information and settings such as their email address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

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

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      EndpointGetUsers result = apiInstance.usersGet_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersGet_0");
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

[**EndpointGetUsers**](EndpointGetUsers.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="usersIDGet"></a>
# **usersIDGet**
> EndpointGetUsersID usersIDGet(ID)



Fetch an array of users. You can only retrieve users existing within the current access token&#39;s bubble.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

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

    UsersApi apiInstance = new UsersApi(defaultClient);
    List<Integer> ID = Arrays.asList(); // List<Integer> | 
    try {
      EndpointGetUsersID result = apiInstance.usersIDGet(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIDGet");
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
| **ID** | [**List&lt;Integer&gt;**](Integer.md)|  | |

### Return type

[**EndpointGetUsersID**](EndpointGetUsersID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="usersIDGroupsGet"></a>
# **usersIDGroupsGet**
> EndpointGetUsersIDGroups usersIDGroupsGet(ID)



You can only retrieve groups that were created by users existing within the current access token&#39;s bubble.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

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

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer ID = 56; // Integer | 
    try {
      EndpointGetUsersIDGroups result = apiInstance.usersIDGroupsGet(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIDGroupsGet");
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

[**EndpointGetUsersIDGroups**](EndpointGetUsersIDGroups.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="usersIDGroupsMessagesGet"></a>
# **usersIDGroupsMessagesGet**
> EndpointGetUsersIDGroupsMessages usersIDGroupsMessagesGet(ID, offset, limit)



Paginated transcript of group messages authored by an individual user who exists within the current access token&#39;s bubble. Messages are sorted oldest to newest.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

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

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer ID = 56; // Integer | 
    Integer offset = 0; // Integer | 
    Integer limit = 50; // Integer | 
    try {
      EndpointGetUsersIDGroupsMessages result = apiInstance.usersIDGroupsMessagesGet(ID, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIDGroupsMessagesGet");
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
| **offset** | **Integer**|  | [optional] [default to 0] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**EndpointGetUsersIDGroupsMessages**](EndpointGetUsersIDGroupsMessages.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="usersIDMessagesPost"></a>
# **usersIDMessagesPost**
> EndpointPostUsersIDMessages usersIDMessagesPost(ID, bubbled, metadata0Key, metadata0Privacy, metadata0Values, metadata1Key, metadata1Privacy, metadata1Values, metadata2Key, metadata2Privacy, metadata2Values, textEmoticons, textRaw)



Initiate a conversation with a user who exists within the current access token&#39;s bubble by sending them an introductory message. If you aren&#39;t already in a conversation with them, this endpoint meets them first, and then sends the message. Note that if you aren&#39;t in an existing conversation, you still must meet the criteria to meet them, meaning the user must currently be free for you to meet. You will receive an error message unless it is currently free for you to meet the user. You can use the users/{:IDS}/synergies endpoint to first determine if the user isn&#39;t already in a conversation with you and is free for you to meet and, if they aren&#39;t, how to pay to meet them. If you don&#39;t specify a message, it defaults to your custom introductory message defined in your settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

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

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer ID = 56; // Integer | 
    Boolean bubbled = false; // Boolean | 
    String metadata0Key = "metadata0Key_example"; // String | 
    String metadata0Privacy = "Public"; // String | 
    List<String> metadata0Values = Arrays.asList(); // List<String> | 
    String metadata1Key = "metadata1Key_example"; // String | 
    String metadata1Privacy = "Public"; // String | 
    List<String> metadata1Values = Arrays.asList(); // List<String> | 
    String metadata2Key = "metadata2Key_example"; // String | 
    String metadata2Privacy = "Public"; // String | 
    List<String> metadata2Values = Arrays.asList(); // List<String> | 
    Boolean textEmoticons = false; // Boolean | 
    String textRaw = "textRaw_example"; // String | 
    try {
      EndpointPostUsersIDMessages result = apiInstance.usersIDMessagesPost(ID, bubbled, metadata0Key, metadata0Privacy, metadata0Values, metadata1Key, metadata1Privacy, metadata1Values, metadata2Key, metadata2Privacy, metadata2Values, textEmoticons, textRaw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIDMessagesPost");
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
| **bubbled** | **Boolean**|  | [optional] [default to false] |
| **metadata0Key** | **String**|  | [optional] |
| **metadata0Privacy** | **String**|  | [optional] [enum: Public, Private, Bubbled, User] |
| **metadata0Values** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **metadata1Key** | **String**|  | [optional] |
| **metadata1Privacy** | **String**|  | [optional] [enum: Public, Private, Bubbled, User] |
| **metadata1Values** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **metadata2Key** | **String**|  | [optional] |
| **metadata2Privacy** | **String**|  | [optional] [enum: Public, Private, Bubbled, User] |
| **metadata2Values** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **textEmoticons** | **Boolean**|  | [optional] [default to false] |
| **textRaw** | **String**|  | [optional] |

### Return type

[**EndpointPostUsersIDMessages**](EndpointPostUsersIDMessages.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="usersIDMetadataCollectionsGet"></a>
# **usersIDMetadataCollectionsGet**
> EndpointGetUsersIDMetadataCollections usersIDMetadataCollectionsGet(ID)



Retrieve all key/value pairs attached to the current user that you have access to, so long as the user exists within the current access token&#39;s bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. You will receive an error message unless either the current access token is bubbled, the user is an algorithmic match for you and you have not reached your quota of new introductions for the day, or you have paid to meet them. However, you can always use the /users/metadata/filters endpoint to filter across all users, including those that are unmatched, existing within the current access token&#39;s bubble based on preknown metadata key/value pairs. Metadata will be grouped by key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

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

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer ID = 56; // Integer | 
    try {
      EndpointGetUsersIDMetadataCollections result = apiInstance.usersIDMetadataCollectionsGet(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIDMetadataCollectionsGet");
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

[**EndpointGetUsersIDMetadataCollections**](EndpointGetUsersIDMetadataCollections.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="usersIDMetadataGet"></a>
# **usersIDMetadataGet**
> EndpointGetUsersIDMetadata usersIDMetadataGet(ID, offset, limit)



Retrieve all key/value pairs attached to the current user that you have access to, so long as the user exists within the current access token&#39;s bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. You will receive an error message unless either the current access token is bubbled, the user is an algorithmic match for you and you have not reached your quota of new introductions for the day, or you have paid to meet them. However, you can always use the /users/metadata/filters endpoint to filter across all users, including those that are unmatched, existing within the current access token&#39;s bubble based on preknown metadata key/value pairs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

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

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer ID = 56; // Integer | 
    Integer offset = 0; // Integer | 
    Integer limit = 50; // Integer | 
    try {
      EndpointGetUsersIDMetadata result = apiInstance.usersIDMetadataGet(ID, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIDMetadataGet");
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
| **offset** | **Integer**|  | [optional] [default to 0] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**EndpointGetUsersIDMetadata**](EndpointGetUsersIDMetadata.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="usersIDMetadataPost"></a>
# **usersIDMetadataPost**
> EndpointPostUsersIDMetadata usersIDMetadataPost(ID, metadata0Key, metadata0Privacy, metadata0Values, metadata1Key, metadata1Privacy, metadata1Values, metadata2Key, metadata2Privacy, metadata2Values)



Attach one-to-many key/value pairs of metadata to a user, so long as the user exists within the current access token&#39;s bubble. You can set one key at a time, with one or many values. A key is unique for each author/bubble combination. Attaching metadata with an existing key that was previously created by you, from within the same bubble, overwrites the key with the new value or set of values. The privacy setting allows you to specify who will have access to the metadata: Public metadata by anyone using an access token which grants them access to the user; Bubbled metadata by anyone using an access token existing within the current bubble; User metadata by you, so long as you are using an access token which grants you access to the user; Private metadata by you, so long as you are using an access token existing within the current bubble.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

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

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer ID = 56; // Integer | 
    String metadata0Key = "metadata0Key_example"; // String | 
    String metadata0Privacy = "Public"; // String | 
    List<String> metadata0Values = Arrays.asList(); // List<String> | 
    String metadata1Key = "metadata1Key_example"; // String | 
    String metadata1Privacy = "Public"; // String | 
    List<String> metadata1Values = Arrays.asList(); // List<String> | 
    String metadata2Key = "metadata2Key_example"; // String | 
    String metadata2Privacy = "Public"; // String | 
    List<String> metadata2Values = Arrays.asList(); // List<String> | 
    try {
      EndpointPostUsersIDMetadata result = apiInstance.usersIDMetadataPost(ID, metadata0Key, metadata0Privacy, metadata0Values, metadata1Key, metadata1Privacy, metadata1Values, metadata2Key, metadata2Privacy, metadata2Values);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIDMetadataPost");
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
| **metadata0Key** | **String**|  | [optional] |
| **metadata0Privacy** | **String**|  | [optional] [enum: Public, Private, Bubbled, User] |
| **metadata0Values** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **metadata1Key** | **String**|  | [optional] |
| **metadata1Privacy** | **String**|  | [optional] [enum: Public, Private, Bubbled, User] |
| **metadata1Values** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **metadata2Key** | **String**|  | [optional] |
| **metadata2Privacy** | **String**|  | [optional] [enum: Public, Private, Bubbled, User] |
| **metadata2Values** | [**List&lt;String&gt;**](String.md)|  | [optional] |

### Return type

[**EndpointPostUsersIDMetadata**](EndpointPostUsersIDMetadata.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="usersIDPositionsGet"></a>
# **usersIDPositionsGet**
> EndpointGetUsersIDPositions usersIDPositionsGet(ID, bubbled)



Retrieve the CV of a user who exists within the current access token&#39;s bubble. You will receive an error message unless either the current access token is bubbled, the user is an algorithmic match for you and you have not reached your quota of new introductions for the day, or you have paid to meet them. You can only record CV data to your own account. However, any app that you have OAuth&#39;ed against can do so. By default, you will receive CV data that all apps have recorded for the user. Optionally, you can choose to only receive data that the current access token&#39;s bubble has recorded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

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

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer ID = 56; // Integer | 
    Boolean bubbled = false; // Boolean | 
    try {
      EndpointGetUsersIDPositions result = apiInstance.usersIDPositionsGet(ID, bubbled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIDPositionsGet");
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
| **bubbled** | **Boolean**|  | [optional] [default to false] |

### Return type

[**EndpointGetUsersIDPositions**](EndpointGetUsersIDPositions.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="usersIDSynergiesGet"></a>
# **usersIDSynergiesGet**
> EndpointGetUsersIDSynergies usersIDSynergiesGet(ID)



Determine your match relationship with one or more users who exist within the current access token&#39;s bubble. Under some conditions, the price to meet the user will be $0. However, if this is not the case, the PayPal URL payment method will be provided along with the price to meet the user. The PayPal API can be leveraged to send payments programatically, provided the parameters passed in remain the same to ensure that the payment is correctly recorded. Once the payment has been recorded via PayPal IPN, the price to meet the user changes to $0. You can then call the users/{:ID}/meet endpoint to meet the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

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

    UsersApi apiInstance = new UsersApi(defaultClient);
    List<Integer> ID = Arrays.asList(); // List<Integer> | 
    try {
      EndpointGetUsersIDSynergies result = apiInstance.usersIDSynergiesGet(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIDSynergiesGet");
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
| **ID** | [**List&lt;Integer&gt;**](Integer.md)|  | |

### Return type

[**EndpointGetUsersIDSynergies**](EndpointGetUsersIDSynergies.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="usersIDSynergiesPatch"></a>
# **usersIDSynergiesPatch**
> EndpointPatchUsersIDSynergies usersIDSynergiesPatch(ID, relationshipMuted, relationshipSkipped)



Skip, mute or unmute a user you&#39;ve been matched with. Skipped matches are only presented as algorithmic matches after all other candidates have been exhausted. You cannot be matched with or meet muted users. You can only skip, mute or unmute users existing within the same bubble.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

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

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer ID = 56; // Integer | 
    Boolean relationshipMuted = true; // Boolean | 
    Boolean relationshipSkipped = true; // Boolean | 
    try {
      EndpointPatchUsersIDSynergies result = apiInstance.usersIDSynergiesPatch(ID, relationshipMuted, relationshipSkipped);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIDSynergiesPatch");
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
| **relationshipMuted** | **Boolean**|  | [optional] |
| **relationshipSkipped** | **Boolean**|  | [optional] |

### Return type

[**EndpointPatchUsersIDSynergies**](EndpointPatchUsersIDSynergies.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="usersInvitesPost"></a>
# **usersInvitesPost**
> EndpointPostUsersInvites usersInvitesPost(csv, emails)



Invite users to into your current access token&#39;s bubble by having Dazah send out email invitations on your behalf. The invitation sends users to begin the OAuth flow for the current application (based on the settings specified in the application&#39;s profile), and therefore they will be redirected to the application upon signing up / logging in. Upon doing so, if they aren&#39;t already, they will automatically be connected with you as well. If your current access token does not escape the bubble, the invitation will specify you wish to connect within the application&#39;s name. If your current access token escapes the bubble, the invitation will specify you wish to connect within Dazah. Submit either a list of emails, or a LinkedIn or Outlook CSV file. You can retrieve your LinkedIn CSV file by exporting your LinkedIn Connections at https://www.linkedin.com/people/export-settings. You can retrieve your Outlook CSV file by using the Outlook Import and Export Wizard. This endpoint buckets the invitations into four categories: Existing invites are existing users who are already connected with you within the current bubble, and are therefore not emailed; Discovered invites are existing Dazah users who are available to be connected with within the current bubble, and are therefore not emailed. Now that they have been discovered, the users/{:ID}/meet API endpoint may be used to connect with them; Invalid invites are existing Dazah users who are unavailable to be connected with, because they have deactivated accounts, are muting you, etc., and are therefore not emailed; Emailed invites are queued to receive an invitation within approximately 1 hour. Note that if you are attempting to invite an existing Dazah user who does not currently exist within your current access token&#39;s bubble, they will fall within the Discovered bucket if your current access token escapes the bubble, but will be emailed an invitation to join the application if your current access token does not escape the bubble.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

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

    UsersApi apiInstance = new UsersApi(defaultClient);
    File csv = new File("/path/to/file"); // File | 
    List<String> emails = Arrays.asList(); // List<String> | 
    try {
      EndpointPostUsersInvites result = apiInstance.usersInvitesPost(csv, emails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersInvitesPost");
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
| **csv** | **File**|  | [optional] |
| **emails** | [**List&lt;String&gt;**](String.md)|  | [optional] |

### Return type

[**EndpointPostUsersInvites**](EndpointPostUsersInvites.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="usersMetadataFiltersPost"></a>
# **usersMetadataFiltersPost**
> EndpointPostUsersMetadataFilters usersMetadataFiltersPost(limit, metadata0Key, metadata0Values, metadata1Key, metadata1Values, metadata2Key, metadata2Values, offset)



Paginated listing of users filtered by arbitrary metadata criteria. Users must match on all key/value pairs passed in. Users may only match on one value of an array passed in. However, users are sorted based on how many distinct values they match on (most matches first).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

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

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer limit = 50; // Integer | 
    String metadata0Key = "metadata0Key_example"; // String | 
    List<String> metadata0Values = Arrays.asList(); // List<String> | 
    String metadata1Key = "metadata1Key_example"; // String | 
    List<String> metadata1Values = Arrays.asList(); // List<String> | 
    String metadata2Key = "metadata2Key_example"; // String | 
    List<String> metadata2Values = Arrays.asList(); // List<String> | 
    Integer offset = 0; // Integer | 
    try {
      EndpointPostUsersMetadataFilters result = apiInstance.usersMetadataFiltersPost(limit, metadata0Key, metadata0Values, metadata1Key, metadata1Values, metadata2Key, metadata2Values, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersMetadataFiltersPost");
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
| **limit** | **Integer**|  | [optional] [default to 50] |
| **metadata0Key** | **String**|  | [optional] |
| **metadata0Values** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **metadata1Key** | **String**|  | [optional] |
| **metadata1Values** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **metadata2Key** | **String**|  | [optional] |
| **metadata2Values** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **offset** | **Integer**|  | [optional] [default to 0] |

### Return type

[**EndpointPostUsersMetadataFilters**](EndpointPostUsersMetadataFilters.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="usersNearbyGet"></a>
# **usersNearbyGet**
> EndpointGetUsersNearby usersNearbyGet(latitude, longitude, offset, limit)



Fetch an array of users that are geographically close to a set of coordinates. You can only retrieve users existing within the current access token&#39;s bubble.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

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

    UsersApi apiInstance = new UsersApi(defaultClient);
    Float latitude = 3.4F; // Float | 
    Float longitude = 3.4F; // Float | 
    Integer offset = 0; // Integer | 
    Integer limit = 50; // Integer | 
    try {
      EndpointGetUsersNearby result = apiInstance.usersNearbyGet(latitude, longitude, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersNearbyGet");
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
| **latitude** | **Float**|  | [optional] |
| **longitude** | **Float**|  | [optional] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**EndpointGetUsersNearby**](EndpointGetUsersNearby.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="usersPatch"></a>
# **usersPatch**
> EndpointPatchUsers usersPatch(company, companySize, firstName, goals, headline, industry, introduction, jobPosition, lastName, locationImportance, matchTags, pitch, tags, targetedIndustry, url)



Update the OAuth&#39;ed end user&#39;s account profile. At this time, for anti-spam reasons, restrictions preclude the ability to update email address and some other settings via the API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

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

    UsersApi apiInstance = new UsersApi(defaultClient);
    String company = "company_example"; // String | 
    String companySize = "Self-employed"; // String | 
    String firstName = "firstName_example"; // String | 
    List<String> goals = Arrays.asList(); // List<String> | 
    String headline = "headline_example"; // String | 
    String industry = "Accounting"; // String | 
    String introduction = "introduction_example"; // String | 
    String jobPosition = "Executive Management (C-level)"; // String | 
    String lastName = "lastName_example"; // String | 
    String locationImportance = "true"; // String | 
    List<String> matchTags = Arrays.asList(); // List<String> | 
    String pitch = "pitch_example"; // String | 
    List<String> tags = Arrays.asList(); // List<String> | 
    String targetedIndustry = "Accounting"; // String | 
    String url = "url_example"; // String | 
    try {
      EndpointPatchUsers result = apiInstance.usersPatch(company, companySize, firstName, goals, headline, industry, introduction, jobPosition, lastName, locationImportance, matchTags, pitch, tags, targetedIndustry, url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersPatch");
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
| **company** | **String**|  | [optional] |
| **companySize** | **String**|  | [optional] [enum: Self-employed, 2 - 9 Employees, 10 - 49 Employees, 50 - 99 Employees, 100 - 499 Employees, 500 - 999 Employees, 1000 - 4999 Employees, 5000+ Employees, Don't Know] |
| **firstName** | **String**|  | [optional] |
| **goals** | [**List&lt;String&gt;**](String.md)|  | [optional] [enum: Find business partnerships, Find prospective clients, Hire employees, Find a job, Find a co-founder, Receive mentorship from others, Mentor others] |
| **headline** | **String**|  | [optional] |
| **industry** | **String**|  | [optional] [enum: Accounting, Airlines/Aviation, Alternative Dispute Resolution, Alternative Medicine, Animation, Apparel & Fashion, Architecture & Planning, Arts and Crafts, Automotive, Aviation & Aerospace, Banking, Biotechnology, Broadcast Media, Building Materials, Business Supplies and Equipment, Capital Markets, Chemicals, Civic & Social Organization, Civil Engineering, Commercial Real Estate, Computer & Network Security, Computer Games, Computer Hardware, Computer Networking, Computer Software, Construction, Consumer Electronics, Consumer Goods, Consumer Services, Cosmetics, Dairy, Defense & Space, Design, E-Learning, Education Management, Electrical/Electronic Manufacturing, Entertainment, Environmental Services, Events Services, Executive Office, Facilities Services, Farming, Financial Services, Fine Art, Fishery, Food & Beverages, Food Production, Fund-Raising, Furniture, Gambling & Casinos, Glass, Ceramics & Concrete, Government Administration, Government Relations, Graphic Design, Health, Wellness and Fitness, Higher Education, Hospital & Health Care, Hospitality, Human Resources, Import and Export, Individual & Family Services, Industrial Automation, Information Services, Information Technology and Services, Insurance, International Affairs, International Trade and Development, Internet, Investment Banking, Investment Management, Judiciary, Law Enforcement, Law Practice, Legal Services, Legislative Office, Leisure, Travel & Tourism, Libraries, Logistics and Supply Chain, Luxury Goods & Jewelry, Machinery, Management Consulting, Maritime, Market Research, Marketing and Advertising, Mechanical or Industrial Engineering, Media Production, Medical Devices, Medical Practice, Mental Health Care, Military, Mining & Metals, Motion Pictures and Film, Museums and Institutions, Music, Nanotechnology, Newspapers, Non-Profit Organization Management, Oil & Energy, Online Media, Outsourcing/Offshoring, Package/Freight Delivery, Packaging and Containers, Paper & Forest Products, Performing Arts, Pharmaceuticals, Philanthropy, Photography, Plastics, Political Organization, Primary/Secondary Education, Printing, Professional Training & Coaching, Program Development, Public Policy, Public Relations and Communications, Public Safety, Publishing, Railroad Manufacture, Ranching, Real Estate, Recreational Facilities and Services, Religious Institutions, Renewables & Environment, Research, Restaurants, Retail, Security and Investigations, Semiconductors, Shipbuilding, Sporting Goods, Sports, Staffing and Recruiting, Supermarkets, Telecommunications, Textiles, Think Tanks, Tobacco, Translation and Localization, Transportation/Trucking/Railroad, Utilities, Venture Capital & Private Equity, Veterinary, Warehousing, Wholesale, Wine and Spirits, Wireless, Writing and Editing] |
| **introduction** | **String**|  | [optional] |
| **jobPosition** | **String**|  | [optional] [enum: Executive Management (C-level), VP-level Executive, Manager / Director / Supervisor, Systems Development, Software Development, Web Developer, IT Consultant, Technical Support, Sales, Other technology related, Other non-technology related, Student, Retired] |
| **lastName** | **String**|  | [optional] |
| **locationImportance** | **String**|  | [optional] [enum: true, Somewhat, false] |
| **matchTags** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **pitch** | **String**|  | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **targetedIndustry** | **String**|  | [optional] [enum: Accounting, Airlines/Aviation, Alternative Dispute Resolution, Alternative Medicine, Animation, Apparel & Fashion, Architecture & Planning, Arts and Crafts, Automotive, Aviation & Aerospace, Banking, Biotechnology, Broadcast Media, Building Materials, Business Supplies and Equipment, Capital Markets, Chemicals, Civic & Social Organization, Civil Engineering, Commercial Real Estate, Computer & Network Security, Computer Games, Computer Hardware, Computer Networking, Computer Software, Construction, Consumer Electronics, Consumer Goods, Consumer Services, Cosmetics, Dairy, Defense & Space, Design, E-Learning, Education Management, Electrical/Electronic Manufacturing, Entertainment, Environmental Services, Events Services, Executive Office, Facilities Services, Farming, Financial Services, Fine Art, Fishery, Food & Beverages, Food Production, Fund-Raising, Furniture, Gambling & Casinos, Glass, Ceramics & Concrete, Government Administration, Government Relations, Graphic Design, Health, Wellness and Fitness, Higher Education, Hospital & Health Care, Hospitality, Human Resources, Import and Export, Individual & Family Services, Industrial Automation, Information Services, Information Technology and Services, Insurance, International Affairs, International Trade and Development, Internet, Investment Banking, Investment Management, Judiciary, Law Enforcement, Law Practice, Legal Services, Legislative Office, Leisure, Travel & Tourism, Libraries, Logistics and Supply Chain, Luxury Goods & Jewelry, Machinery, Management Consulting, Maritime, Market Research, Marketing and Advertising, Mechanical or Industrial Engineering, Media Production, Medical Devices, Medical Practice, Mental Health Care, Military, Mining & Metals, Motion Pictures and Film, Museums and Institutions, Music, Nanotechnology, Newspapers, Non-Profit Organization Management, Oil & Energy, Online Media, Outsourcing/Offshoring, Package/Freight Delivery, Packaging and Containers, Paper & Forest Products, Performing Arts, Pharmaceuticals, Philanthropy, Photography, Plastics, Political Organization, Primary/Secondary Education, Printing, Professional Training & Coaching, Program Development, Public Policy, Public Relations and Communications, Public Safety, Publishing, Railroad Manufacture, Ranching, Real Estate, Recreational Facilities and Services, Religious Institutions, Renewables & Environment, Research, Restaurants, Retail, Security and Investigations, Semiconductors, Shipbuilding, Sporting Goods, Sports, Staffing and Recruiting, Supermarkets, Telecommunications, Textiles, Think Tanks, Tobacco, Translation and Localization, Transportation/Trucking/Railroad, Utilities, Venture Capital & Private Equity, Veterinary, Warehousing, Wholesale, Wine and Spirits, Wireless, Writing and Editing] |
| **url** | **String**|  | [optional] |

### Return type

[**EndpointPatchUsers**](EndpointPatchUsers.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="usersSearchesPost"></a>
# **usersSearchesPost**
> EndpointPostUsersSearches usersSearchesPost(activeWithinXDays, audienceIds, bubbled, excludeConnections, excludeMatches, excludeMuted, excludeSkipped, geoLatitude, geoLongitude, geoMilesAway, groupId, limit, locationCityQuery, locationCityWeight, locationCountryQuery, locationCountryWeight, locationRegionQuery, locationRegionWeight, metadata0Key, metadata0Query, metadata0Weight, metadata1Key, metadata1Query, metadata1Weight, metadata2Key, metadata2Query, metadata2Weight, offset, positionOrganizationQuery, positionOrganizationWeight, positionRoleQuery, positionRoleWeight, positionSummaryQuery, positionSummaryWeight, profileFirstNameQuery, profileFirstNameWeight, profileGoalsQuery, profileGoalsWeight, profileHeadlineQuery, profileHeadlineWeight, profileIndustryQuery, profileIndustryWeight, profileLastNameQuery, profileLastNameWeight, profilePitchQuery, profilePitchWeight)



Filter and perform a weighted search against user profile fields, CV fields, and metadata by specifying a string to search on for each individual field. By default, results are filtered such that all words in the string must exist, unless you seprate the words with OR. To perform a weighted search (as opposed to filtering), specify the weight (from 0-100) the search algorithm should assign to the field. You can optionally exclude users who you are already in or not in conversations with, exclude users who you previously skipped, or exclude users who you are muting. By doing so, you can effectively customize your own matching algorithm. You can specify geo coordinates to only find users a certain distance away from a specific location, or only find users within a certain distance from the OAuth&#39;ed end-user&#39;s last known location. If your app utilizes multiple audience segments, you can specify which audiences you would like to search. You can also limit users to just those who have been recently active. You can also choose to only receive users originating from the current access token&#39;s bubble. Only users existing within the current access token&#39;s bubble will be matched, and you can only search within a group created by a bubbled user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

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

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer activeWithinXDays = 56; // Integer | 
    List<Integer> audienceIds = Arrays.asList(); // List<Integer> | 
    Boolean bubbled = false; // Boolean | 
    Boolean excludeConnections = false; // Boolean | 
    Boolean excludeMatches = false; // Boolean | 
    Boolean excludeMuted = false; // Boolean | 
    Boolean excludeSkipped = false; // Boolean | 
    Float geoLatitude = 3.4F; // Float | 
    Float geoLongitude = 3.4F; // Float | 
    Float geoMilesAway = 3.4F; // Float | 
    Integer groupId = 56; // Integer | 
    Integer limit = 50; // Integer | 
    String locationCityQuery = "locationCityQuery_example"; // String | 
    Integer locationCityWeight = 56; // Integer | 
    String locationCountryQuery = "locationCountryQuery_example"; // String | 
    Integer locationCountryWeight = 56; // Integer | 
    String locationRegionQuery = "locationRegionQuery_example"; // String | 
    Integer locationRegionWeight = 56; // Integer | 
    String metadata0Key = "metadata0Key_example"; // String | 
    String metadata0Query = "metadata0Query_example"; // String | 
    Integer metadata0Weight = 56; // Integer | 
    String metadata1Key = "metadata1Key_example"; // String | 
    String metadata1Query = "metadata1Query_example"; // String | 
    Integer metadata1Weight = 56; // Integer | 
    String metadata2Key = "metadata2Key_example"; // String | 
    String metadata2Query = "metadata2Query_example"; // String | 
    Integer metadata2Weight = 56; // Integer | 
    Integer offset = 0; // Integer | 
    String positionOrganizationQuery = "positionOrganizationQuery_example"; // String | 
    Integer positionOrganizationWeight = 56; // Integer | 
    String positionRoleQuery = "positionRoleQuery_example"; // String | 
    Integer positionRoleWeight = 56; // Integer | 
    String positionSummaryQuery = "positionSummaryQuery_example"; // String | 
    Integer positionSummaryWeight = 56; // Integer | 
    String profileFirstNameQuery = "profileFirstNameQuery_example"; // String | 
    Integer profileFirstNameWeight = 56; // Integer | 
    String profileGoalsQuery = "profileGoalsQuery_example"; // String | 
    String profileGoalsWeight = "profileGoalsWeight_example"; // String | 
    String profileHeadlineQuery = "profileHeadlineQuery_example"; // String | 
    Integer profileHeadlineWeight = 56; // Integer | 
    String profileIndustryQuery = "profileIndustryQuery_example"; // String | 
    Integer profileIndustryWeight = 56; // Integer | 
    String profileLastNameQuery = "profileLastNameQuery_example"; // String | 
    Integer profileLastNameWeight = 56; // Integer | 
    String profilePitchQuery = "profilePitchQuery_example"; // String | 
    Integer profilePitchWeight = 56; // Integer | 
    try {
      EndpointPostUsersSearches result = apiInstance.usersSearchesPost(activeWithinXDays, audienceIds, bubbled, excludeConnections, excludeMatches, excludeMuted, excludeSkipped, geoLatitude, geoLongitude, geoMilesAway, groupId, limit, locationCityQuery, locationCityWeight, locationCountryQuery, locationCountryWeight, locationRegionQuery, locationRegionWeight, metadata0Key, metadata0Query, metadata0Weight, metadata1Key, metadata1Query, metadata1Weight, metadata2Key, metadata2Query, metadata2Weight, offset, positionOrganizationQuery, positionOrganizationWeight, positionRoleQuery, positionRoleWeight, positionSummaryQuery, positionSummaryWeight, profileFirstNameQuery, profileFirstNameWeight, profileGoalsQuery, profileGoalsWeight, profileHeadlineQuery, profileHeadlineWeight, profileIndustryQuery, profileIndustryWeight, profileLastNameQuery, profileLastNameWeight, profilePitchQuery, profilePitchWeight);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersSearchesPost");
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
| **activeWithinXDays** | **Integer**|  | [optional] |
| **audienceIds** | [**List&lt;Integer&gt;**](Integer.md)|  | [optional] |
| **bubbled** | **Boolean**|  | [optional] [default to false] |
| **excludeConnections** | **Boolean**|  | [optional] [default to false] |
| **excludeMatches** | **Boolean**|  | [optional] [default to false] |
| **excludeMuted** | **Boolean**|  | [optional] [default to false] |
| **excludeSkipped** | **Boolean**|  | [optional] [default to false] |
| **geoLatitude** | **Float**|  | [optional] |
| **geoLongitude** | **Float**|  | [optional] |
| **geoMilesAway** | **Float**|  | [optional] |
| **groupId** | **Integer**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **locationCityQuery** | **String**|  | [optional] |
| **locationCityWeight** | **Integer**|  | [optional] |
| **locationCountryQuery** | **String**|  | [optional] |
| **locationCountryWeight** | **Integer**|  | [optional] |
| **locationRegionQuery** | **String**|  | [optional] |
| **locationRegionWeight** | **Integer**|  | [optional] |
| **metadata0Key** | **String**|  | [optional] |
| **metadata0Query** | **String**|  | [optional] |
| **metadata0Weight** | **Integer**|  | [optional] |
| **metadata1Key** | **String**|  | [optional] |
| **metadata1Query** | **String**|  | [optional] |
| **metadata1Weight** | **Integer**|  | [optional] |
| **metadata2Key** | **String**|  | [optional] |
| **metadata2Query** | **String**|  | [optional] |
| **metadata2Weight** | **Integer**|  | [optional] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **positionOrganizationQuery** | **String**|  | [optional] |
| **positionOrganizationWeight** | **Integer**|  | [optional] |
| **positionRoleQuery** | **String**|  | [optional] |
| **positionRoleWeight** | **Integer**|  | [optional] |
| **positionSummaryQuery** | **String**|  | [optional] |
| **positionSummaryWeight** | **Integer**|  | [optional] |
| **profileFirstNameQuery** | **String**|  | [optional] |
| **profileFirstNameWeight** | **Integer**|  | [optional] |
| **profileGoalsQuery** | **String**|  | [optional] |
| **profileGoalsWeight** | **String**|  | [optional] |
| **profileHeadlineQuery** | **String**|  | [optional] |
| **profileHeadlineWeight** | **Integer**|  | [optional] |
| **profileIndustryQuery** | **String**|  | [optional] |
| **profileIndustryWeight** | **Integer**|  | [optional] |
| **profileLastNameQuery** | **String**|  | [optional] |
| **profileLastNameWeight** | **Integer**|  | [optional] |
| **profilePitchQuery** | **String**|  | [optional] |
| **profilePitchWeight** | **Integer**|  | [optional] |

### Return type

[**EndpointPostUsersSearches**](EndpointPostUsersSearches.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

