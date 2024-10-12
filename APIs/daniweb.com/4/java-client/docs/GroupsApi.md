# GroupsApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**groupsGet**](GroupsApi.md#groupsGet) | **GET** /groups |  |
| [**groupsIDGet**](GroupsApi.md#groupsIDGet) | **GET** /groups/{ID} |  |
| [**groupsIDMembershipsDelete**](GroupsApi.md#groupsIDMembershipsDelete) | **DELETE** /groups/{ID}/memberships |  |
| [**groupsIDMembershipsGet**](GroupsApi.md#groupsIDMembershipsGet) | **GET** /groups/{ID}/memberships |  |
| [**groupsIDMembershipsPatch**](GroupsApi.md#groupsIDMembershipsPatch) | **PATCH** /groups/{ID}/memberships |  |
| [**groupsIDMembershipsPost**](GroupsApi.md#groupsIDMembershipsPost) | **POST** /groups/{ID}/memberships |  |
| [**groupsIDMessagesGet**](GroupsApi.md#groupsIDMessagesGet) | **GET** /groups/{ID}/messages |  |
| [**groupsIDMessagesPost**](GroupsApi.md#groupsIDMessagesPost) | **POST** /groups/{ID}/messages |  |
| [**groupsIDPatch**](GroupsApi.md#groupsIDPatch) | **PATCH** /groups/{ID} |  |
| [**groupsIDSchedulesPost**](GroupsApi.md#groupsIDSchedulesPost) | **POST** /groups/{ID}/schedules |  |
| [**groupsIDStatusesGet**](GroupsApi.md#groupsIDStatusesGet) | **GET** /groups/{ID}/statuses |  |
| [**groupsMessagesIDDelete**](GroupsApi.md#groupsMessagesIDDelete) | **DELETE** /groups/messages/{ID} |  |
| [**groupsMessagesIDGet**](GroupsApi.md#groupsMessagesIDGet) | **GET** /groups/messages/{ID} |  |
| [**groupsMessagesIDMetadataCollectionsGet**](GroupsApi.md#groupsMessagesIDMetadataCollectionsGet) | **GET** /groups/messages/{ID}/metadata/collections |  |
| [**groupsMessagesIDMetadataGet**](GroupsApi.md#groupsMessagesIDMetadataGet) | **GET** /groups/messages/{ID}/metadata |  |
| [**groupsMessagesIDMetadataPost**](GroupsApi.md#groupsMessagesIDMetadataPost) | **POST** /groups/messages/{ID}/metadata |  |
| [**groupsMessagesMetadataFiltersPost**](GroupsApi.md#groupsMessagesMetadataFiltersPost) | **POST** /groups/messages/metadata/filters |  |
| [**groupsPost**](GroupsApi.md#groupsPost) | **POST** /groups |  |
| [**groupsSchedulesPost**](GroupsApi.md#groupsSchedulesPost) | **POST** /groups/schedules |  |
| [**groupsStatusesGet**](GroupsApi.md#groupsStatusesGet) | **GET** /groups/statuses |  |


<a id="groupsGet"></a>
# **groupsGet**
> EndpointGetGroups groupsGet(offset, limit)



Fetch an array of all groups that were created by users existing within the current access token&#39;s bubble. The groups must be either Public or you must be a member of them. Unlisted and Private groups that you are not a member of are not listed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer offset = 0; // Integer | 
    Integer limit = 50; // Integer | 
    try {
      EndpointGetGroups result = apiInstance.groupsGet(offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsGet");
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
| **offset** | **Integer**|  | [optional] [default to 0] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**EndpointGetGroups**](EndpointGetGroups.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsIDGet"></a>
# **groupsIDGet**
> EndpointGetGroupsID groupsIDGet(ID)



Fetch an array of groups. You can only retrieve groups created by users existing within the current access token&#39;s bubble.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    List<Integer> ID = Arrays.asList(); // List<Integer> | 
    try {
      EndpointGetGroupsID result = apiInstance.groupsIDGet(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsIDGet");
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

[**EndpointGetGroupsID**](EndpointGetGroupsID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsIDMembershipsDelete"></a>
# **groupsIDMembershipsDelete**
> EndpointDeleteGroupsIDMemberships groupsIDMembershipsDelete(ID)



Leave a group that you are a member of and that was created by a user who exists within the current access token&#39;s bubble.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer ID = 56; // Integer | 
    try {
      EndpointDeleteGroupsIDMemberships result = apiInstance.groupsIDMembershipsDelete(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsIDMembershipsDelete");
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

[**EndpointDeleteGroupsIDMemberships**](EndpointDeleteGroupsIDMemberships.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsIDMembershipsGet"></a>
# **groupsIDMembershipsGet**
> EndpointGetGroupsIDMemberships groupsIDMembershipsGet(ID, moderatorsOnly, offset)



Fetch an array of users who are members of specific groups that you are also a member of. You can only retrieve users existing within the current access token&#39;s bubble.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    List<Integer> ID = Arrays.asList(); // List<Integer> | 
    Boolean moderatorsOnly = false; // Boolean | 
    Integer offset = 0; // Integer | 
    try {
      EndpointGetGroupsIDMemberships result = apiInstance.groupsIDMembershipsGet(ID, moderatorsOnly, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsIDMembershipsGet");
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
| **moderatorsOnly** | **Boolean**|  | [optional] [default to false] |
| **offset** | **Integer**|  | [optional] [default to 0] |

### Return type

[**EndpointGetGroupsIDMemberships**](EndpointGetGroupsIDMemberships.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsIDMembershipsPatch"></a>
# **groupsIDMembershipsPatch**
> EndpointPatchGroupsIDMemberships groupsIDMembershipsPatch(ID, userId, moderator)



Promote or demote a member&#39;s privileges within a group that you created. The user must exist within the current access token&#39;s bubble and be an existing member of the group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer ID = 56; // Integer | 
    Integer userId = 56; // Integer | 
    Boolean moderator = false; // Boolean | 
    try {
      EndpointPatchGroupsIDMemberships result = apiInstance.groupsIDMembershipsPatch(ID, userId, moderator);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsIDMembershipsPatch");
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
| **userId** | **Integer**|  | |
| **moderator** | **Boolean**|  | [optional] [default to false] |

### Return type

[**EndpointPatchGroupsIDMemberships**](EndpointPatchGroupsIDMemberships.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsIDMembershipsPost"></a>
# **groupsIDMembershipsPost**
> EndpointPostGroupsIDMemberships groupsIDMembershipsPost(ID, passphrase, userId)



Join a group that was created by a user who exists within the current access token&#39;s bubble, or join other users into a group that you created. If you are the group owner, you can pass in a user_id to create membership records for a user you are in a conversation with. The user must exist within the current access token&#39;s bubble. If the group is private, you must successfully pass in its passphrase in order to join. You can obtain the passphrase from the group&#39;s owner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer ID = 56; // Integer | 
    String passphrase = "passphrase_example"; // String | 
    Integer userId = 56; // Integer | 
    try {
      EndpointPostGroupsIDMemberships result = apiInstance.groupsIDMembershipsPost(ID, passphrase, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsIDMembershipsPost");
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
| **passphrase** | **String**|  | [optional] |
| **userId** | **Integer**|  | [optional] |

### Return type

[**EndpointPostGroupsIDMemberships**](EndpointPostGroupsIDMemberships.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsIDMessagesGet"></a>
# **groupsIDMessagesGet**
> EndpointGetGroupsIDMessages groupsIDMessagesGet(ID, gtMessageId, excludeSelf, includeDeleted, date, bubbled, recordSeen, timeout, offset, limit)



Retrieve the last {limit} messages in the group, for messages authored by users within the current access token&#39;s bubble. If a timeout is 0 or greater, the batch is sorted oldest first. Otherwise, if timeout is a negative number, the transcript is paginated and sorted newest first. Specify a timeout for long polling (which delays the server sending back results for up to n seconds or until results are available, whichever comes first), or default to 0 for immediate results. Optionally record your status as online along with sharing the latest message you&#39;ve seen with other group members. Optionally specify a gt_message_id to retrieve only messages with an ID greater than that specified (such as greater than the latest message ID received in the last poll). Optionally only poll for messages authored by other members of the group, and echo messages authored by you when sending, for a perceived increase in performance. Optionally only retrieve messages that were posted from within the current access token&#39;s bubble. Optionally specify a date formatted as YYYY-MM-DD to retrieve a transcript of messages from a single day. When record_seen is set to true, the new message count for the group is reset to zero.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer ID = 56; // Integer | 
    Integer gtMessageId = 56; // Integer | 
    Boolean excludeSelf = false; // Boolean | 
    Boolean includeDeleted = false; // Boolean | 
    String date = "date_example"; // String | 
    Boolean bubbled = false; // Boolean | 
    Boolean recordSeen = false; // Boolean | 
    Integer timeout = 0; // Integer | 
    Integer offset = 0; // Integer | 
    Integer limit = 50; // Integer | 
    try {
      EndpointGetGroupsIDMessages result = apiInstance.groupsIDMessagesGet(ID, gtMessageId, excludeSelf, includeDeleted, date, bubbled, recordSeen, timeout, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsIDMessagesGet");
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
| **gtMessageId** | **Integer**|  | [optional] |
| **excludeSelf** | **Boolean**|  | [optional] [default to false] |
| **includeDeleted** | **Boolean**|  | [optional] [default to false] |
| **date** | **String**|  | [optional] |
| **bubbled** | **Boolean**|  | [optional] [default to false] |
| **recordSeen** | **Boolean**|  | [optional] [default to false] |
| **timeout** | **Integer**|  | [optional] [default to 0] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**EndpointGetGroupsIDMessages**](EndpointGetGroupsIDMessages.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsIDMessagesPost"></a>
# **groupsIDMessagesPost**
> EndpointPostGroupsIDMessages groupsIDMessagesPost(ID, textRaw, metadata0Key, metadata0Privacy, metadata0Values, metadata1Key, metadata1Privacy, metadata1Values, metadata2Key, metadata2Privacy, metadata2Values, textEmoticons)



Post a message to a group that you are a member of and that was created by a user who exists within the current access token&#39;s bubble. Optionally specify whether emoticons should be parsed into smiley images. Additionally, optionally attach a single metadata key/value pair to the group message upon submission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer ID = 56; // Integer | 
    String textRaw = "textRaw_example"; // String | 
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
    try {
      EndpointPostGroupsIDMessages result = apiInstance.groupsIDMessagesPost(ID, textRaw, metadata0Key, metadata0Privacy, metadata0Values, metadata1Key, metadata1Privacy, metadata1Values, metadata2Key, metadata2Privacy, metadata2Values, textEmoticons);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsIDMessagesPost");
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
| **textRaw** | **String**|  | |
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

### Return type

[**EndpointPostGroupsIDMessages**](EndpointPostGroupsIDMessages.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsIDPatch"></a>
# **groupsIDPatch**
> EndpointPatchGroupsID groupsIDPatch(ID, description, name, passphrase, privacy, slug)



Modify a group you previously created.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer ID = 56; // Integer | 
    String description = "description_example"; // String | 
    String name = "name_example"; // String | 
    String passphrase = "passphrase_example"; // String | 
    String privacy = "Public"; // String | 
    String slug = "slug_example"; // String | 
    try {
      EndpointPatchGroupsID result = apiInstance.groupsIDPatch(ID, description, name, passphrase, privacy, slug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsIDPatch");
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
| **description** | **String**|  | [optional] |
| **name** | **String**|  | [optional] |
| **passphrase** | **String**|  | [optional] |
| **privacy** | **String**|  | [optional] [enum: Public, Unlisted, Private] |
| **slug** | **String**|  | [optional] |

### Return type

[**EndpointPatchGroupsID**](EndpointPatchGroupsID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsIDSchedulesPost"></a>
# **groupsIDSchedulesPost**
> EndpointPostGroupsIDSchedules groupsIDSchedulesPost(ID, date, limit, offset, rollUp, sort)



Paginated report of information about group messages contributed by conversation and date. Only groups you&#39;re a member of and group messages authored by users existing within the current access token&#39;s bubble are considered in the calculations. Optionally roll up all groups to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages within the group discussion(s).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    List<Integer> ID = Arrays.asList(); // List<Integer> | 
    String date = "date_example"; // String | 
    Integer limit = 50; // Integer | 
    Integer offset = 0; // Integer | 
    Boolean rollUp = false; // Boolean | 
    String sort = "asc"; // String | 
    try {
      EndpointPostGroupsIDSchedules result = apiInstance.groupsIDSchedulesPost(ID, date, limit, offset, rollUp, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsIDSchedulesPost");
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
| **date** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **rollUp** | **Boolean**|  | [optional] [default to false] |
| **sort** | **String**|  | [optional] [default to desc] [enum: asc, desc] |

### Return type

[**EndpointPostGroupsIDSchedules**](EndpointPostGroupsIDSchedules.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsIDStatusesGet"></a>
# **groupsIDStatusesGet**
> EndpointGetGroupsIDStatuses groupsIDStatusesGet(ID)



Status information about your current relationship with one or more groups you are a member of, provided the users who created the groups exist within the current access token&#39;s bubble.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    List<Integer> ID = Arrays.asList(); // List<Integer> | 
    try {
      EndpointGetGroupsIDStatuses result = apiInstance.groupsIDStatusesGet(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsIDStatusesGet");
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

[**EndpointGetGroupsIDStatuses**](EndpointGetGroupsIDStatuses.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsMessagesIDDelete"></a>
# **groupsMessagesIDDelete**
> EndpointDeleteGroupsMessagesID groupsMessagesIDDelete(ID)



Delete an array of group messages. You must be the owner or moderator of the group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    List<Integer> ID = Arrays.asList(); // List<Integer> | 
    try {
      EndpointDeleteGroupsMessagesID result = apiInstance.groupsMessagesIDDelete(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsMessagesIDDelete");
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

[**EndpointDeleteGroupsMessagesID**](EndpointDeleteGroupsMessagesID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsMessagesIDGet"></a>
# **groupsMessagesIDGet**
> EndpointGetGroupsMessagesID groupsMessagesIDGet(ID)



Fetch an array of group messages. You can only retrieve messages authored by you or by users existing within the current access token&#39;s bubble.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    List<Integer> ID = Arrays.asList(); // List<Integer> | 
    try {
      EndpointGetGroupsMessagesID result = apiInstance.groupsMessagesIDGet(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsMessagesIDGet");
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

[**EndpointGetGroupsMessagesID**](EndpointGetGroupsMessagesID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsMessagesIDMetadataCollectionsGet"></a>
# **groupsMessagesIDMetadataCollectionsGet**
> EndpointGetGroupsMessagesIDMetadataCollections groupsMessagesIDMetadataCollectionsGet(ID)



Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who created the group exists within the current access token&#39;s bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. Metadata will be grouped by key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer ID = 56; // Integer | 
    try {
      EndpointGetGroupsMessagesIDMetadataCollections result = apiInstance.groupsMessagesIDMetadataCollectionsGet(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsMessagesIDMetadataCollectionsGet");
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

[**EndpointGetGroupsMessagesIDMetadataCollections**](EndpointGetGroupsMessagesIDMetadataCollections.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsMessagesIDMetadataGet"></a>
# **groupsMessagesIDMetadataGet**
> EndpointGetGroupsMessagesIDMetadata groupsMessagesIDMetadataGet(ID, offset, limit)



Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who created the group exists within the current access token&#39;s bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer ID = 56; // Integer | 
    Integer offset = 0; // Integer | 
    Integer limit = 50; // Integer | 
    try {
      EndpointGetGroupsMessagesIDMetadata result = apiInstance.groupsMessagesIDMetadataGet(ID, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsMessagesIDMetadataGet");
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

[**EndpointGetGroupsMessagesIDMetadata**](EndpointGetGroupsMessagesIDMetadata.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsMessagesIDMetadataPost"></a>
# **groupsMessagesIDMetadataPost**
> EndpointPostGroupsMessagesIDMetadata groupsMessagesIDMetadataPost(ID, metadata0Key, metadata0Privacy, metadata0Values, metadata1Key, metadata1Privacy, metadata1Values, metadata2Key, metadata2Privacy, metadata2Values)



Attach one-to-many key/value pairs of metadata to a group message, so long as the user who authored the message exists within the current access token&#39;s bubble and you are a member of their group. A key is unique for each author/bubble combination. Attaching metadata with an existing key that was previously created by you, from within the same bubble, overwrites the key with the new value or set of values. The privacy setting allows you to specify who will have access to the metadata: Public metadata by anyone using an access token which grants them access to the user who authored the message and who is also a member of the group the message belongs to; Bubbled metadata by anyone using an access token existing within the current bubble who is also a member of the group the message belongs to; User metadata by you, so long as you are using an access token which grants you access to the user who authored the message and you remain a member of the group; Private metadata by you, so long as you are using an access token existing within the current bubble and you remain a member of the group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
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
      EndpointPostGroupsMessagesIDMetadata result = apiInstance.groupsMessagesIDMetadataPost(ID, metadata0Key, metadata0Privacy, metadata0Values, metadata1Key, metadata1Privacy, metadata1Values, metadata2Key, metadata2Privacy, metadata2Values);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsMessagesIDMetadataPost");
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

[**EndpointPostGroupsMessagesIDMetadata**](EndpointPostGroupsMessagesIDMetadata.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsMessagesMetadataFiltersPost"></a>
# **groupsMessagesMetadataFiltersPost**
> EndpointPostGroupsMessagesMetadataFilters groupsMessagesMetadataFiltersPost(limit, metadata0Key, metadata0Values, metadata1Key, metadata1Values, metadata2Key, metadata2Values, offset)



Paginated listing of messages filtered by arbitrary metadata criteria. Messages must match on all key/value pairs passed in. Messages may only match on one value of an array passed in. However, messages are sorted based on how many distinct values they match on (most matches first).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer limit = 50; // Integer | 
    String metadata0Key = "metadata0Key_example"; // String | 
    List<String> metadata0Values = Arrays.asList(); // List<String> | 
    String metadata1Key = "metadata1Key_example"; // String | 
    List<String> metadata1Values = Arrays.asList(); // List<String> | 
    String metadata2Key = "metadata2Key_example"; // String | 
    List<String> metadata2Values = Arrays.asList(); // List<String> | 
    Integer offset = 0; // Integer | 
    try {
      EndpointPostGroupsMessagesMetadataFilters result = apiInstance.groupsMessagesMetadataFiltersPost(limit, metadata0Key, metadata0Values, metadata1Key, metadata1Values, metadata2Key, metadata2Values, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsMessagesMetadataFiltersPost");
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

[**EndpointPostGroupsMessagesMetadataFilters**](EndpointPostGroupsMessagesMetadataFilters.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsPost"></a>
# **groupsPost**
> EndpointPostGroups groupsPost(description, name, privacy, slug, passphrase)



Create a new group for other members to join. Any user who is using an access token whose bubble you exist in can join your group provided it is not a private group. Private groups can only be joined by members who know its passphrase. Unlisted groups can be joined by anybody as long as they know the Group ID, but they are not referenced anywhere to non-members. Public groups can be joined by anybody, are discoverable, and anyone can see the public groups a user is a member of, provided the group owner exists in their access token&#39;s bubble. Groups each have their own discussions, transcripts, schedules, and ability to list and search their members.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String description = "description_example"; // String | 
    String name = "name_example"; // String | 
    String privacy = "Public"; // String | 
    String slug = "slug_example"; // String | 
    String passphrase = "passphrase_example"; // String | 
    try {
      EndpointPostGroups result = apiInstance.groupsPost(description, name, privacy, slug, passphrase);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsPost");
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
| **description** | **String**|  | |
| **name** | **String**|  | |
| **privacy** | **String**|  | [enum: Public, Unlisted, Private] |
| **slug** | **String**|  | |
| **passphrase** | **String**|  | [optional] |

### Return type

[**EndpointPostGroups**](EndpointPostGroups.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsSchedulesPost"></a>
# **groupsSchedulesPost**
> EndpointPostGroupsSchedules groupsSchedulesPost(date, limit, offset, rollUp, sort)



Paginated report of information about messages contributed by group and date. Only groups you&#39;re a member of and group messages authored by users the current access token has access to are considered in the calculations. Optionally roll up all groups to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String date = "date_example"; // String | 
    Integer limit = 50; // Integer | 
    Integer offset = 0; // Integer | 
    Boolean rollUp = false; // Boolean | 
    String sort = "asc"; // String | 
    try {
      EndpointPostGroupsSchedules result = apiInstance.groupsSchedulesPost(date, limit, offset, rollUp, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsSchedulesPost");
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
| **date** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **rollUp** | **Boolean**|  | [optional] [default to false] |
| **sort** | **String**|  | [optional] [default to desc] [enum: asc, desc] |

### Return type

[**EndpointPostGroupsSchedules**](EndpointPostGroupsSchedules.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

<a id="groupsStatusesGet"></a>
# **groupsStatusesGet**
> EndpointGetGroupsStatuses groupsStatusesGet(existingMembership, offset, limit)



Retrieve groups that were created by users within the current access token&#39;s bubble, along with your current relationship with the groups. The groups must be either Public or you must be a member of them. Unlisted and Private groups that you are not a member of are not listed. Optionally only retrieve groups that you are a member of.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

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

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Boolean existingMembership = false; // Boolean | 
    Integer offset = 0; // Integer | 
    Integer limit = 50; // Integer | 
    try {
      EndpointGetGroupsStatuses result = apiInstance.groupsStatusesGet(existingMembership, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#groupsStatusesGet");
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
| **existingMembership** | **Boolean**|  | [optional] [default to false] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **limit** | **Integer**|  | [optional] [default to 50] |

### Return type

[**EndpointGetGroupsStatuses**](EndpointGetGroupsStatuses.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid Response |  -  |

