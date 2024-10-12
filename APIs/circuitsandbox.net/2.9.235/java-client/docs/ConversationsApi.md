# ConversationsApi

All URIs are relative to *https://circuitsandbox.net/rest/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addFavorite**](ConversationsApi.md#addFavorite) | **POST** /conversations/{convId}/favorite | Adds a conversation to the favorites |
| [**addLabel**](ConversationsApi.md#addLabel) | **POST** /users/labels | Add a user label |
| [**addModerators**](ConversationsApi.md#addModerators) | **POST** /conversations/{convId}/moderators | Add moderators |
| [**addParticipantCommunity**](ConversationsApi.md#addParticipantCommunity) | **POST** /conversations/community/{convId}/participants | Adds participants to a community |
| [**addParticipantGroup**](ConversationsApi.md#addParticipantGroup) | **POST** /conversations/group/{convId}/participants | Adds participants to a group conversation |
| [**addTextItem**](ConversationsApi.md#addTextItem) | **POST** /conversations/{convId}/messages | Adds a message to a conversation |
| [**addTextItemWithParent**](ConversationsApi.md#addTextItemWithParent) | **POST** /conversations/{convId}/messages/{itemId} | Adds a message to an item |
| [**archiveConversation**](ConversationsApi.md#archiveConversation) | **POST** /conversations/{convId}/archive | Archives conversation |
| [**assignLabel**](ConversationsApi.md#assignLabel) | **POST** /conversations/{convId}/label | Adds a label to a conversation |
| [**createCommunityConversation**](ConversationsApi.md#createCommunityConversation) | **POST** /conversations/community | Creates a community conversation |
| [**createDirectConversation**](ConversationsApi.md#createDirectConversation) | **POST** /conversations/direct | Creates a 1-to-1 conversation |
| [**createGroupConversation**](ConversationsApi.md#createGroupConversation) | **POST** /conversations/group | Creates a group conversation |
| [**deleteFavorite**](ConversationsApi.md#deleteFavorite) | **DELETE** /conversations/{convId}/favorite | Removes a conversation from favorites |
| [**deleteTextItem**](ConversationsApi.md#deleteTextItem) | **DELETE** /conversations/{convId}/messages/{itemId} | Deletes a message from a conversation |
| [**flagItem**](ConversationsApi.md#flagItem) | **POST** /conversations/{convId}/messages/{itemId}/flag | Adds a flag to a message in a conversation |
| [**getCommunityConversations**](ConversationsApi.md#getCommunityConversations) | **GET** /conversations/community | Gets a list of communities |
| [**getConversationItems**](ConversationsApi.md#getConversationItems) | **GET** /conversations/{convId}/items | Gets a list of conversation items |
| [**getConversationbyId**](ConversationsApi.md#getConversationbyId) | **GET** /conversations/{convId} | Gets a conversation |
| [**getConversations**](ConversationsApi.md#getConversations) | **GET** /conversations | Gets a list of conversations |
| [**getConversationsById**](ConversationsApi.md#getConversationsById) | **GET** /conversations/byIds | Gets conversations |
| [**getConversationsByLabel**](ConversationsApi.md#getConversationsByLabel) | **GET** /conversations/label/{labelId} | Returns conversations with a certain label |
| [**getDirectConversation**](ConversationsApi.md#getDirectConversation) | **GET** /conversations/direct | Checks for a 1-to-1 conversation |
| [**getFavoriteConversations**](ConversationsApi.md#getFavoriteConversations) | **GET** /conversations/favorite | Gets favorite conversations |
| [**getFlagItem**](ConversationsApi.md#getFlagItem) | **GET** /conversations/{convId}/messages/flag | Gets a list of the flagged messages of a conversation |
| [**getFlagItemConv**](ConversationsApi.md#getFlagItemConv) | **GET** /conversations/messages/flag | Gets a list of the flagged messages |
| [**getJoinDetails**](ConversationsApi.md#getJoinDetails) | **GET** /conversations/{convId}/conversationdetails | Gets the conference details of a conversation |
| [**getJoinDetailsMultiple**](ConversationsApi.md#getJoinDetailsMultiple) | **GET** /conversations/conversationdetails | Gets the conference details for multiple conversations |
| [**getParticipantsByConvId**](ConversationsApi.md#getParticipantsByConvId) | **GET** /conversations/{convId}/participants | Performs a list of participants |
| [**getPinnedConversations**](ConversationsApi.md#getPinnedConversations) | **GET** /conversations/{convId}/pins | Returns pinned topics of a conversation |
| [**getSingleConversationtem**](ConversationsApi.md#getSingleConversationtem) | **GET** /conversations/messages/{itemId} | Returns a text item |
| [**joinCommunityConversation**](ConversationsApi.md#joinCommunityConversation) | **POST** /conversations/community/{convId}/join | Adds the authenticated user to a community |
| [**likeItem**](ConversationsApi.md#likeItem) | **POST** /conversations/{convId}/messages/{itemId}/like | Adds a \&quot;like\&quot; to a message |
| [**moderateConversation**](ConversationsApi.md#moderateConversation) | **POST** /conversations/moderate/{convId} | Set conversation moderated |
| [**pinAConversation**](ConversationsApi.md#pinAConversation) | **POST** /conversations/{convId}/pins/{itemId} | Pins a topic of a conversation |
| [**removeLabel**](ConversationsApi.md#removeLabel) | **DELETE** /users/labels/{labelId} | Remove a user label |
| [**removeModerators**](ConversationsApi.md#removeModerators) | **DELETE** /conversations/{convId}/moderators | Remove moderators |
| [**removeParticipantCommunity**](ConversationsApi.md#removeParticipantCommunity) | **DELETE** /conversations/community/{convId}/participants | Removes participants from a community |
| [**removeParticipantGroup**](ConversationsApi.md#removeParticipantGroup) | **DELETE** /conversations/group/{convId}/participants | Removes participants from a group conversation |
| [**resolveInvitationToken**](ConversationsApi.md#resolveInvitationToken) | **GET** /conversations/resolveinvitetoken | Resolves an invite token to a conversation |
| [**searchConversations**](ConversationsApi.md#searchConversations) | **GET** /conversations/search | Performs a conversation search |
| [**unFlagItem**](ConversationsApi.md#unFlagItem) | **DELETE** /conversations/{convId}/messages/{itemId}/flag | Removes the flag from a message |
| [**unPinAConversation**](ConversationsApi.md#unPinAConversation) | **DELETE** /conversations/{convId}/pins/{itemId} | Unpins a topic of a conversation |
| [**unassignLabel**](ConversationsApi.md#unassignLabel) | **DELETE** /conversations/{convId}/label/{labelId} | Removes a label from a conversation |
| [**undoArchiveConversation**](ConversationsApi.md#undoArchiveConversation) | **DELETE** /conversations/{convId}/archive | Unmute conversation |
| [**unlikeItem**](ConversationsApi.md#unlikeItem) | **DELETE** /conversations/{convId}/messages/{itemId}/like | Removes a \&quot;like\&quot; from a message |
| [**unmoderateConversation**](ConversationsApi.md#unmoderateConversation) | **POST** /conversations/unmoderate/{convId} | Set conversation unmoderated |
| [**updateConversationCommunity**](ConversationsApi.md#updateConversationCommunity) | **PUT** /conversations/community/{convId} | Updates the information of a community |
| [**updateConversationGroup**](ConversationsApi.md#updateConversationGroup) | **PUT** /conversations/group/{convId} | Updates the information of a group conversation |
| [**updateProfile**](ConversationsApi.md#updateProfile) | **PUT** /users/profile | Updates the user profile |
| [**updateTextItem**](ConversationsApi.md#updateTextItem) | **PUT** /conversations/{convId}/messages/{itemId} | Updates a message |


<a id="addFavorite"></a>
# **addFavorite**
> addFavorite(convId)

Adds a conversation to the favorites

Adds a conversation to the favorites. Favorites can be displayed in a separate side tab inside of the Circuit client to have a better overview of important conversations. OauthScopes: WRITE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation which will be marked as favorite
    try {
      apiInstance.addFavorite(convId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#addFavorite");
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
| **convId** | **String**| The ID of the conversation which will be marked as favorite | |

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
| **200** | The conversation was successfully marked |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the user is no participant of the conversation&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="addLabel"></a>
# **addLabel**
> Label addLabel(label)

Add a user label

Add a label to the list of user labels OauthScopes: WRITE_USER_PROFILE, ORGANIZE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String label = "label_example"; // String | The label value to add
    try {
      Label result = apiInstance.addLabel(label);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#addLabel");
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
| **label** | **String**| The label value to add | |

### Return type

[**Label**](Label.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The label was successfully added |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="addModerators"></a>
# **addModerators**
> addModerators(convId, moderators)

Add moderators

Adds a list of moderators to a conversation OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation to which the moderators are added
    List<String> moderators = Arrays.asList(); // List<String> | The list of moderator ids to add 
    try {
      apiInstance.addModerators(convId, moderators);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#addModerators");
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
| **convId** | **String**| The ID of the conversation to which the moderators are added | |
| **moderators** | [**List&lt;String&gt;**](String.md)| The list of moderator ids to add  | |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The moderators were successfully added |  -  |
| **400** | Error reading list of moderators to add |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="addParticipantCommunity"></a>
# **addParticipantCommunity**
> Conversation addParticipantCommunity(convId, participants)

Adds participants to a community

Adds one or more participants to the given community. This operation can only be performed by a user who is already a member of the community. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation to which the participant has to be added.
    List<String> participants = Arrays.asList(); // List<String> | The IDs or the unique email addresses of the Circuit users that should to be added.
    try {
      Conversation result = apiInstance.addParticipantCommunity(convId, participants);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#addParticipantCommunity");
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
| **convId** | **String**| The ID of the conversation to which the participant has to be added. | |
| **participants** | [**List&lt;String&gt;**](String.md)| The IDs or the unique email addresses of the Circuit users that should to be added. | |

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the conversation object to which the participants were added. |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the userIds passed as parameter are not provided in the correct format&lt;/li&gt;&lt;li&gt; or an valid email address&lt;/li&gt;&lt;li&gt;or one or more of the user do not exist&lt;/li&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the conversation is not of type COMMUNITY&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="addParticipantGroup"></a>
# **addParticipantGroup**
> Conversation addParticipantGroup(convId, participants)

Adds participants to a group conversation

Adds one or more participants to the given group conversation. This operation can only be performed by a user who is already a member of the conversation. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation to which the participant has to be added.
    List<String> participants = Arrays.asList(); // List<String> | The IDs or the unique email addresses of the Circuit users that should to be added.
    try {
      Conversation result = apiInstance.addParticipantGroup(convId, participants);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#addParticipantGroup");
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
| **convId** | **String**| The ID of the conversation to which the participant has to be added. | |
| **participants** | [**List&lt;String&gt;**](String.md)| The IDs or the unique email addresses of the Circuit users that should to be added. | |

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the conversation object to which the participants were added. |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the userIds passed as parameter are not provided in the correct format&lt;/li&gt;&lt;li&gt; or an valid email address&lt;/li&gt;&lt;li&gt;or one or more of the user do not exist&lt;/li&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the conversation is not of type GROUP&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="addTextItem"></a>
# **addTextItem**
> ConversationItem addTextItem(convId, attachments, content, formMetaData, subject)

Adds a message to a conversation

Adds a message to the given conversation. This operation can be only performed on behalf of a user who is already a member of the conversation. OauthScopes: WRITE_CONVERSATIONS, CREATE_CONVERSATIONS_CONTENT

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation to which the new item has to be added
    List<String> attachments = Arrays.asList(); // List<String> | A comma separated list of attachment IDs from the file API.
    String content = "content_example"; // String | The actual content of the item, is mandatory unless an attachment is added
    String formMetaData = "formMetaData_example"; // String | The form meta data of the new text item
    String subject = "subject_example"; // String | The subject (headline) of the new text item
    try {
      ConversationItem result = apiInstance.addTextItem(convId, attachments, content, formMetaData, subject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#addTextItem");
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
| **convId** | **String**| The ID of the conversation to which the new item has to be added | |
| **attachments** | [**List&lt;String&gt;**](String.md)| A comma separated list of attachment IDs from the file API. | [optional] |
| **content** | **String**| The actual content of the item, is mandatory unless an attachment is added | [optional] |
| **formMetaData** | **String**| The form meta data of the new text item | [optional] |
| **subject** | **String**| The subject (headline) of the new text item | [optional] |

### Return type

[**ConversationItem**](ConversationItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the new text item object |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the user is no participant of the conversation&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="addTextItemWithParent"></a>
# **addTextItemWithParent**
> ConversationItem addTextItemWithParent(convId, itemId, attachments, content, formMetaData, subject)

Adds a message to an item

Adds a message to the existing item. The added message will be a child item of the message with the given itemId. OauthScopes: WRITE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation to which the new item has to be added
    String itemId = "itemId_example"; // String | The ID of the item to which the new one has to be added as child
    List<String> attachments = Arrays.asList(); // List<String> | A comma separated list of attachment IDs from the file API.
    String content = "content_example"; // String | The actual content of the item
    String formMetaData = "formMetaData_example"; // String | The form meta data of the new text item
    String subject = "subject_example"; // String | The subject (headline) of the new text item
    try {
      ConversationItem result = apiInstance.addTextItemWithParent(convId, itemId, attachments, content, formMetaData, subject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#addTextItemWithParent");
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
| **convId** | **String**| The ID of the conversation to which the new item has to be added | |
| **itemId** | **String**| The ID of the item to which the new one has to be added as child | |
| **attachments** | [**List&lt;String&gt;**](String.md)| A comma separated list of attachment IDs from the file API. | [optional] |
| **content** | **String**| The actual content of the item | [optional] |
| **formMetaData** | **String**| The form meta data of the new text item | [optional] |
| **subject** | **String**| The subject (headline) of the new text item | [optional] |

### Return type

[**ConversationItem**](ConversationItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the new text item object |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the parent item does not exist&lt;/li&gt;&lt;li&gt;the user is no participant of the conversation&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="archiveConversation"></a>
# **archiveConversation**
> archiveConversation(convId)

Archives conversation

Archives a conversation by muting it OauthScopes: WRITE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation which will be archived
    try {
      apiInstance.archiveConversation(convId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#archiveConversation");
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
| **convId** | **String**| The ID of the conversation which will be archived | |

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
| **200** | The conversation was successfully archived |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the user is no participant of the conversation&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="assignLabel"></a>
# **assignLabel**
> Label assignLabel(convId, label)

Adds a label to a conversation

Adds a label to a conversation, you can search and organize your conversations based on these labels OauthScopes: WRITE_CONVERSATIONS, ORGANIZE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation to which the label is added
    String label = "label_example"; // String | The actual label 
    try {
      Label result = apiInstance.assignLabel(convId, label);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#assignLabel");
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
| **convId** | **String**| The ID of the conversation to which the label is added | |
| **label** | **String**| The actual label  | |

### Return type

[**Label**](Label.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The label was successfully added |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;li&gt;you reached the maximum of 250 labels&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="createCommunityConversation"></a>
# **createCommunityConversation**
> Conversation createCommunityConversation(topic, description, participants)

Creates a community conversation

Creates a community. Communities are open conversations that anyone in a Circuit domain (tenant) can join without having to be added by another user. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String topic = "topic_example"; // String | An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used)
    String description = "description_example"; // String | An optional description for the community conversation
    List<String> participants = Arrays.asList(); // List<String> | list of participants that will be part of this conversation, specified by the Circuit user ID or the unique email address. At least one participant needs to be added
    try {
      Conversation result = apiInstance.createCommunityConversation(topic, description, participants);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#createCommunityConversation");
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
| **topic** | **String**| An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used) | |
| **description** | **String**| An optional description for the community conversation | [optional] |
| **participants** | [**List&lt;String&gt;**](String.md)| list of participants that will be part of this conversation, specified by the Circuit user ID or the unique email address. At least one participant needs to be added | [optional] |

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The conversation was created successfully and can be accessed via the conversation ID |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the userIds passed as parameter are not provided in the correct format&lt;/li&gt;&lt;li&gt; or an valid email address&lt;/li&gt;&lt;li&gt;or one or more of the user do not exist&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="createDirectConversation"></a>
# **createDirectConversation**
> Conversation createDirectConversation(participant)

Creates a 1-to-1 conversation

Creates a 1-to-1 conversation between the authenticated user and the user with the provided userId. In case there is already an existing 1-to-1 conversation between these users, the endpoint returns the existing conversation. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String participant = "participant_example"; // String | The participant that will be part of this conversation together with the creator, specified by the Circuit user ID or the unique email address
    try {
      Conversation result = apiInstance.createDirectConversation(participant);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#createDirectConversation");
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
| **participant** | **String**| The participant that will be part of this conversation together with the creator, specified by the Circuit user ID or the unique email address | |

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The conversation was created successfully and can be accessed via the conversation ID |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the data format of the passed user does not match either a UUID (user primary key)&lt;/li&gt;&lt;li&gt; or an valid email address&lt;/li&gt;&lt;li&gt;or the user does not exist&lt;/li&gt;&lt;li&gt;or the user is the same who initiates the request&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **409** | A conversation already exists. The response contains this conversation. |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="createGroupConversation"></a>
# **createGroupConversation**
> Conversation createGroupConversation(participants, topic)

Creates a group conversation

Creates a group conversation between three or more users. The authenticated user is directly added to this conversation. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    List<String> participants = Arrays.asList(); // List<String> | A list of participants that will be part of this conversation, specified by the Circuit user ID or the unique email address. At least one participant needs to be added
    String topic = "topic_example"; // String | An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used)
    try {
      Conversation result = apiInstance.createGroupConversation(participants, topic);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#createGroupConversation");
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
| **participants** | [**List&lt;String&gt;**](String.md)| A list of participants that will be part of this conversation, specified by the Circuit user ID or the unique email address. At least one participant needs to be added | |
| **topic** | **String**| An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used) | [optional] |

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The conversation was created successfully and can be accessed via the conversation ID |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the userIds passed as parameter are not provided in the correct format&lt;/li&gt;&lt;li&gt; or an valid email address&lt;/li&gt;&lt;li&gt;or one or more of the user do not exist&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="deleteFavorite"></a>
# **deleteFavorite**
> deleteFavorite(convId)

Removes a conversation from favorites

Removes a conversation from favorites. Favorites can be displayed in a separate side tab inside of the Circuit client to have a better overview of important conversations. OauthScopes: WRITE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation which will be unmarked as favorite
    try {
      apiInstance.deleteFavorite(convId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#deleteFavorite");
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
| **convId** | **String**| The ID of the conversation which will be unmarked as favorite | |

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
| **200** | The conversation was successfully unmarked |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the user is no participant of the conversation&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;li&gt;the conversation was not marked before&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="deleteTextItem"></a>
# **deleteTextItem**
> ConversationItem deleteTextItem(convId, itemId)

Deletes a message from a conversation

Marks a message in the given conversation as deleted. Deleted messages are still part of the conversation, but their content is no more visible. This operation can only be performed on behalf of the message&#39;s creator. OauthScopes: WRITE_CONVERSATIONS, DELETE_CONVERSATIONS_CONTENT

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation to which the item belongs
    String itemId = "itemId_example"; // String | The ID of the item that will be deleted
    try {
      ConversationItem result = apiInstance.deleteTextItem(convId, itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#deleteTextItem");
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
| **convId** | **String**| The ID of the conversation to which the item belongs | |
| **itemId** | **String**| The ID of the item that will be deleted | |

### Return type

[**ConversationItem**](ConversationItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the deleted text item object |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the item does not exist&lt;/li&gt;&lt;li&gt;the user is no participant of the conversation&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="flagItem"></a>
# **flagItem**
> flagItem(convId, itemId, itemCreationTime, parentId)

Adds a flag to a message in a conversation

Adds a flag to the given message in the given conversation. OauthScopes: WRITE_CONVERSATIONS, ORGANIZE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation to which the item belongs
    String itemId = "itemId_example"; // String | The ID of the item that will be flagged
    String itemCreationTime = "itemCreationTime_example"; // String | The time when the item was created
    String parentId = "parentId_example"; // String | The ID of the item's parent
    try {
      apiInstance.flagItem(convId, itemId, itemCreationTime, parentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#flagItem");
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
| **convId** | **String**| The ID of the conversation to which the item belongs | |
| **itemId** | **String**| The ID of the item that will be flagged | |
| **itemCreationTime** | **String**| The time when the item was created | [optional] |
| **parentId** | **String**| The ID of the item&#39;s parent | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The item was successful flagged |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the item does not exist&lt;/li&gt;&lt;li&gt;the user is no participant of the conversation&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getCommunityConversations"></a>
# **getCommunityConversations**
> List&lt;Conversation&gt; getCommunityConversations(sort, order, includeOwn, startIndex, results)

Gets a list of communities

Gets a list of communities. This endpoint can be used to explore the communities the authenticated user could join. OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String sort = "ALPHABETICALLY"; // String | Defines the type of sorting for the community conversations (default is alphabetical)
    String order = "ASCENDING"; // String | Defines the ordering of the conversations (default is ascending)
    Boolean includeOwn = false; // Boolean | If set to false only conversations are returned where the user is no member of, otherwise all community conversations are returned
    BigDecimal startIndex = new BigDecimal("0"); // BigDecimal | The index of the conversation that is the first one that has to be returned. E.g. if a request starts with startIndex 40 and results 20 the conversations 40 to 60 are returned
    BigDecimal results = new BigDecimal("25"); // BigDecimal | The maximum number of returned results (default 25). The maximum allowed value is 100.
    try {
      List<Conversation> result = apiInstance.getCommunityConversations(sort, order, includeOwn, startIndex, results);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#getCommunityConversations");
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
| **sort** | **String**| Defines the type of sorting for the community conversations (default is alphabetical) | [optional] [default to ALPHABETICALLY] [enum: ALPHABETICALLY, RECENT_ACTIVITY, POPULARITY] |
| **order** | **String**| Defines the ordering of the conversations (default is ascending) | [optional] [default to ASCENDING] [enum: ASCENDING, DESCENDING] |
| **includeOwn** | **Boolean**| If set to false only conversations are returned where the user is no member of, otherwise all community conversations are returned | [optional] [default to false] |
| **startIndex** | **BigDecimal**| The index of the conversation that is the first one that has to be returned. E.g. if a request starts with startIndex 40 and results 20 the conversations 40 to 60 are returned | [optional] [default to 0] |
| **results** | **BigDecimal**| The maximum number of returned results (default 25). The maximum allowed value is 100. | [optional] [default to 25] |

### Return type

[**List&lt;Conversation&gt;**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The matching conversations |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;a field constraint is violated&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getConversationItems"></a>
# **getConversationItems**
> List&lt;ConversationItem&gt; getConversationItems(convId, modTime, direction, results)

Gets a list of conversation items

Gets a list of conversation items. OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation to which the items belong
    OffsetDateTime modTime = OffsetDateTime.now(); // OffsetDateTime | The modification time of the item in UTC format. During the query the items before (default) or after this timestamps are returned. In case no timestamp is specified the current server time in UTC is used, i.e. the last 25 modified items are returned
    String direction = "BEFORE"; // String | The direction of the search based on the modification time. Valid values are either BEFORE (default) or AFTER
    BigDecimal results = new BigDecimal("25"); // BigDecimal | The maximum number of returned results (default 25). The maximum allowed value is 100.
    try {
      List<ConversationItem> result = apiInstance.getConversationItems(convId, modTime, direction, results);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#getConversationItems");
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
| **convId** | **String**| The ID of the conversation to which the items belong | |
| **modTime** | **OffsetDateTime**| The modification time of the item in UTC format. During the query the items before (default) or after this timestamps are returned. In case no timestamp is specified the current server time in UTC is used, i.e. the last 25 modified items are returned | [optional] |
| **direction** | **String**| The direction of the search based on the modification time. Valid values are either BEFORE (default) or AFTER | [optional] [default to BEFORE] [enum: BEFORE, AFTER] |
| **results** | **BigDecimal**| The maximum number of returned results (default 25). The maximum allowed value is 100. | [optional] [default to 25] |

### Return type

[**List&lt;ConversationItem&gt;**](ConversationItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The matching conversation items |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getConversationbyId"></a>
# **getConversationbyId**
> Conversation getConversationbyId(convId)

Gets a conversation

Gets a conversation based on the given ID. OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation which should be updated
    try {
      Conversation result = apiInstance.getConversationbyId(convId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#getConversationbyId");
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
| **convId** | **String**| The ID of the conversation which should be updated | |

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the conversation object |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getConversations"></a>
# **getConversations**
> List&lt;Conversation&gt; getConversations(modTime, direction, results)

Gets a list of conversations

Gets a list of conversations and communities the authenticated user participates in. OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    OffsetDateTime modTime = OffsetDateTime.now(); // OffsetDateTime | The modification time of the conversation in UTC format. During the query the conversations before (<i>default</i>) or after this timestamp are returned. In case no timestamp is specified the current server time in UTC is used, i.e. the last 25 modified conversations are returned
    String direction = "BEFORE"; // String | The direction of the search based on the modification time. Valid values are either BEFORE (default) or AFTER
    BigDecimal results = new BigDecimal("25"); // BigDecimal | The maximum number of returned results (default 25). The maximum allowed value is 100.
    try {
      List<Conversation> result = apiInstance.getConversations(modTime, direction, results);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#getConversations");
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
| **modTime** | **OffsetDateTime**| The modification time of the conversation in UTC format. During the query the conversations before (&lt;i&gt;default&lt;/i&gt;) or after this timestamp are returned. In case no timestamp is specified the current server time in UTC is used, i.e. the last 25 modified conversations are returned | [optional] |
| **direction** | **String**| The direction of the search based on the modification time. Valid values are either BEFORE (default) or AFTER | [optional] [default to BEFORE] [enum: BEFORE, AFTER] |
| **results** | **BigDecimal**| The maximum number of returned results (default 25). The maximum allowed value is 100. | [optional] [default to 25] |

### Return type

[**List&lt;Conversation&gt;**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The matching conversations |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getConversationsById"></a>
# **getConversationsById**
> List&lt;Conversation&gt; getConversationsById(convIds)

Gets conversations

Gets conversation based on the given IDs. OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    List<String> convIds = Arrays.asList(); // List<String> | The array of IDs of the conversations which should be retrieved
    try {
      List<Conversation> result = apiInstance.getConversationsById(convIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#getConversationsById");
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
| **convIds** | [**List&lt;String&gt;**](String.md)| The array of IDs of the conversations which should be retrieved | |

### Return type

[**List&lt;Conversation&gt;**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of existing conversations successfully retrieved. |  -  |
| **400** | missing documentation |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getConversationsByLabel"></a>
# **getConversationsByLabel**
> ConversationsPage getConversationsByLabel(labelId, nextPagePointer, pageSize)

Returns conversations with a certain label

Returns conversations with matching labels and paginated  OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String labelId = "labelId_example"; // String | Id of the label to look for
    String nextPagePointer = "nextPagePointer_example"; // String | Pointer to the next page of conversations if there are any
    BigDecimal pageSize = new BigDecimal("25"); // BigDecimal | Numbers of max conversations per page
    try {
      ConversationsPage result = apiInstance.getConversationsByLabel(labelId, nextPagePointer, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#getConversationsByLabel");
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
| **labelId** | **String**| Id of the label to look for | |
| **nextPagePointer** | **String**| Pointer to the next page of conversations if there are any | [optional] |
| **pageSize** | **BigDecimal**| Numbers of max conversations per page | [optional] [default to 25] |

### Return type

[**ConversationsPage**](ConversationsPage.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of conversations that are tagged with a certain label |  -  |
| **400** | he request cannot be fulfilled due to bad syntax |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getDirectConversation"></a>
# **getDirectConversation**
> Conversation getDirectConversation(participant)

Checks for a 1-to-1 conversation

Checks if a 1-to-1 conversation between the authenticated user and the user with the provided userId exists. OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String participant = "participant_example"; // String | The participant that will be part of this conversation together with the creator, specified by the Circuit user ID or the unique email address
    try {
      Conversation result = apiInstance.getDirectConversation(participant);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#getDirectConversation");
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
| **participant** | **String**| The participant that will be part of this conversation together with the creator, specified by the Circuit user ID or the unique email address | |

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The conversation was found and can be accessed via the conversation ID |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the data format of the passed user does not match either a UUID (user primary key)&lt;/li&gt;&lt;li&gt; or an valid email address&lt;/li&gt;&lt;li&gt;or the user does not exist&lt;/li&gt;&lt;li&gt;or the user is the same who initiates the request&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getFavoriteConversations"></a>
# **getFavoriteConversations**
> List&lt;String&gt; getFavoriteConversations()

Gets favorite conversations

Gets the conversationIds which are marked as favorites. OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    try {
      List<String> result = apiInstance.getFavoriteConversations();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#getFavoriteConversations");
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

**List&lt;String&gt;**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of marked conversations or an empty response. |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the user is no participant of the conversation&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getFlagItem"></a>
# **getFlagItem**
> List&lt;ConversationItem&gt; getFlagItem(convId)

Gets a list of the flagged messages of a conversation

Gets a list of all the flagged messages in the given conversation. OauthScopes: READ_CONVERSATIONS, ORGANIZE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation to which the item belongs
    try {
      List<ConversationItem> result = apiInstance.getFlagItem(convId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#getFlagItem");
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
| **convId** | **String**| The ID of the conversation to which the item belongs | |

### Return type

[**List&lt;ConversationItem&gt;**](ConversationItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the list of flagged items |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getFlagItemConv"></a>
# **getFlagItemConv**
> List&lt;ConversationItem&gt; getFlagItemConv()

Gets a list of the flagged messages

Gets a list of all the messages the authenticated user has flagged. This endpoint should be used carefully in case where the authenticated user has a lot of flagged messages. OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    try {
      List<ConversationItem> result = apiInstance.getFlagItemConv();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#getFlagItemConv");
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

[**List&lt;ConversationItem&gt;**](ConversationItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the list of flagged items |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getJoinDetails"></a>
# **getJoinDetails**
> ConversationDetails getJoinDetails(convId)

Gets the conference details of a conversation

Gets the conference details of the given conversation. Conference details include the URL, which is used to join the conference through a web or mobile application, as well as the dial-in phone numbers and conference PIN, which are used to join the conference by phone. OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation for which the join details should be returned
    try {
      ConversationDetails result = apiInstance.getJoinDetails(convId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#getJoinDetails");
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
| **convId** | **String**| The ID of the conversation for which the join details should be returned | |

### Return type

[**ConversationDetails**](ConversationDetails.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The join details. |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getJoinDetailsMultiple"></a>
# **getJoinDetailsMultiple**
> List&lt;ConversationDetails&gt; getJoinDetailsMultiple(convIds)

Gets the conference details for multiple conversations

Gets the conference details of the given conversations. Conference details include the URL, which is used to join the conference through a web or mobile application, as well as the dial-in phone numbers and conference PIN, which are used to join the conference by phone. OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    List<String> convIds = Arrays.asList(); // List<String> | An array of IDs of the conversations for which the join details should be returned
    try {
      List<ConversationDetails> result = apiInstance.getJoinDetailsMultiple(convIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#getJoinDetailsMultiple");
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
| **convIds** | [**List&lt;String&gt;**](String.md)| An array of IDs of the conversations for which the join details should be returned | |

### Return type

[**List&lt;ConversationDetails&gt;**](ConversationDetails.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The join details. |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getParticipantsByConvId"></a>
# **getParticipantsByConvId**
> List&lt;ConversationParticipantsList&gt; getParticipantsByConvId(convId, pageSize, name, type, searchPointer)

Performs a list of participants

Performs a search for participants. The max number of participants is configurable. If more participants are available a search pointer is returned for consecutive calls. OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The id of the conversation the participants are searched for.
    BigDecimal pageSize = new BigDecimal(78); // BigDecimal | The page size of the hit list
    String name = "name_example"; // String | Part of name to filter the results
    String type = "REGULAR"; // String | Type of participant to filter the results
    String searchPointer = "searchPointer_example"; // String | Pointer for paged output. Add to consecutive request to get next page
    try {
      List<ConversationParticipantsList> result = apiInstance.getParticipantsByConvId(convId, pageSize, name, type, searchPointer);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#getParticipantsByConvId");
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
| **convId** | **String**| The id of the conversation the participants are searched for. | |
| **pageSize** | **BigDecimal**| The page size of the hit list | |
| **name** | **String**| Part of name to filter the results | [optional] |
| **type** | **String**| Type of participant to filter the results | [optional] [default to REGULAR] [enum: REGULAR, MODERATOR, GUEST, FORMER, BOT] |
| **searchPointer** | **String**| Pointer for paged output. Add to consecutive request to get next page | [optional] |

### Return type

[**List&lt;ConversationParticipantsList&gt;**](ConversationParticipantsList.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of conversations and items that match the term |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the user is no participant of the conversation&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getPinnedConversations"></a>
# **getPinnedConversations**
> List&lt;PinnedTopic&gt; getPinnedConversations(convId)

Returns pinned topics of a conversation

Returns pinned topics of a conversation OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | ID of the conversation
    try {
      List<PinnedTopic> result = apiInstance.getPinnedConversations(convId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#getPinnedConversations");
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
| **convId** | **String**| ID of the conversation | |

### Return type

[**List&lt;PinnedTopic&gt;**](PinnedTopic.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The pinned topics |  -  |
| **400** | The request cannot be fulfilled due to bad syntax |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getSingleConversationtem"></a>
# **getSingleConversationtem**
> ConversationItem getSingleConversationtem(itemId)

Returns a text item

Returns a text item for a given item id OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String itemId = "itemId_example"; // String | The ID of the item that will be returned
    try {
      ConversationItem result = apiInstance.getSingleConversationtem(itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#getSingleConversationtem");
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
| **itemId** | **String**| The ID of the item that will be returned | |

### Return type

[**ConversationItem**](ConversationItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The item was successful returned |  -  |
| **400** | The item with the given id was not found |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="joinCommunityConversation"></a>
# **joinCommunityConversation**
> Conversation joinCommunityConversation(convId)

Adds the authenticated user to a community

Adds the authenticated user to the given community (i.e., allows the user to join this community). Contrary to the operation of adding a new participant, this operation can only be performed by a user who is not yet a member of the community. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation which the user will join
    try {
      Conversation result = apiInstance.joinCommunityConversation(convId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#joinCommunityConversation");
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
| **convId** | **String**| The ID of the conversation which the user will join | |

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the conversation object to which the participants was added |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the userIds passed as parameter are not provided in the correct format&lt;/li&gt;&lt;li&gt; or an valid email address&lt;/li&gt;&lt;li&gt;or one or more of the user do not exist&lt;/li&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the conversation is not of type COMMUNITY&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="likeItem"></a>
# **likeItem**
> likeItem(convId, itemId)

Adds a \&quot;like\&quot; to a message

Adds a \&quot;like\&quot; to the given message in the given conversation OauthScopes: WRITE_CONVERSATIONS, UPDATE_CONVERSATION_CONTENT

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation to which the item belongs
    String itemId = "itemId_example"; // String | The ID of the item that will be liked
    try {
      apiInstance.likeItem(convId, itemId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#likeItem");
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
| **convId** | **String**| The ID of the conversation to which the item belongs | |
| **itemId** | **String**| The ID of the item that will be liked | |

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
| **200** | The item was successful liked |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the item does not exist&lt;/li&gt;&lt;li&gt;the user is no participant of the conversation&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="moderateConversation"></a>
# **moderateConversation**
> moderateConversation(convId)

Set conversation moderated

Set a conversation in moderatd mode. Moderators can be added and removed OauthScopes: WRITE_CONVERSATIONS, MODERATE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation which will be set to moderated state
    try {
      apiInstance.moderateConversation(convId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#moderateConversation");
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
| **convId** | **String**| The ID of the conversation which will be set to moderated state | |

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
| **200** | The conversation is in moderated mode |  -  |
| **401** | Permission denied |  -  |
| **403** | Forbidden to edit this conversation |  -  |
| **500** | Internal server error |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="pinAConversation"></a>
# **pinAConversation**
> Conversation pinAConversation(convId, itemId)

Pins a topic of a conversation

Pins a topic of a conversation OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation
    String itemId = "itemId_example"; // String | The ID of the topic
    try {
      Conversation result = apiInstance.pinAConversation(convId, itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#pinAConversation");
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
| **convId** | **String**| The ID of the conversation | |
| **itemId** | **String**| The ID of the topic | |

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the pinned conversation conversation after pinning a topic |  -  |
| **400** | The request cannot be fulfilled due to bad syntax |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="removeLabel"></a>
# **removeLabel**
> Label removeLabel(labelId)

Remove a user label

Remove a label from the list of user labels OauthScopes: WRITE_USER_PROFILE, ORGANIZE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String labelId = "labelId_example"; // String | The label value to remove, either the unique ID or the label value
    try {
      Label result = apiInstance.removeLabel(labelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#removeLabel");
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
| **labelId** | **String**| The label value to remove, either the unique ID or the label value | |

### Return type

[**Label**](Label.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The label was successfully removed |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;li&gt;the label does not exist&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="removeModerators"></a>
# **removeModerators**
> removeModerators(convId, moderators)

Remove moderators

Removes a list of moderators from a conversation OauthScopes: WRITE_CONVERSATIONS, MODERATE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation where the moderators are removed
    List<String> moderators = Arrays.asList(); // List<String> | The list of moderator ids to remove
    try {
      apiInstance.removeModerators(convId, moderators);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#removeModerators");
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
| **convId** | **String**| The ID of the conversation where the moderators are removed | |
| **moderators** | [**List&lt;String&gt;**](String.md)| The list of moderator ids to remove | |

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The moderators were successfully removed |  -  |
| **400** | Failure in moderators list |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="removeParticipantCommunity"></a>
# **removeParticipantCommunity**
> Conversation removeParticipantCommunity(convId, participants)

Removes participants from a community

Removes one or more participants from the given community. The last participant of a community cannot be removed. This operation can only be performed by a user who is already a member of the community. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation from which the participant have to be removed
    List<String> participants = Arrays.asList(); // List<String> | The IDs or the unique email addresses of the Circuit users that have to be removed
    try {
      Conversation result = apiInstance.removeParticipantCommunity(convId, participants);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#removeParticipantCommunity");
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
| **convId** | **String**| The ID of the conversation from which the participant have to be removed | |
| **participants** | [**List&lt;String&gt;**](String.md)| The IDs or the unique email addresses of the Circuit users that have to be removed | |

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the conversation object from which the participants were removed. |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;/li&gt;the userIds passed as parameter are not provided in the correct format&lt;/li&gt;&lt;li&gt; or an valid email address&lt;/li&gt;&lt;li&gt;or one or more of the user do not exist&lt;/li&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the conversation is not of type COMMUNITY&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="removeParticipantGroup"></a>
# **removeParticipantGroup**
> Conversation removeParticipantGroup(convId, participants)

Removes participants from a group conversation

Removes one or more participants from the given group conversation. The last participant of a group conversation cannot be removed. This operation can only be performed on behalf of a user who is already a member of the conversation. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation from which the participant have to be removed
    List<String> participants = Arrays.asList(); // List<String> | The IDs or the unique email addresses of the Circuit users that have to be removed
    try {
      Conversation result = apiInstance.removeParticipantGroup(convId, participants);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#removeParticipantGroup");
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
| **convId** | **String**| The ID of the conversation from which the participant have to be removed | |
| **participants** | [**List&lt;String&gt;**](String.md)| The IDs or the unique email addresses of the Circuit users that have to be removed | |

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the conversation object from which the participants were removed. |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the userIds passed as parameter are not provided in the correct format&lt;/li&gt;&lt;li&gt; or an valid email address&lt;/li&gt;&lt;li&gt;or one or more of the user do not exist&lt;/li&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the conversation is not of type GROUP&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="resolveInvitationToken"></a>
# **resolveInvitationToken**
> Conversation resolveInvitationToken(token)

Resolves an invite token to a conversation

Resolves an invite token to a conversation OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String token = "token_example"; // String | The invite token to resolve
    try {
      Conversation result = apiInstance.resolveInvitationToken(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#resolveInvitationToken");
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
| **token** | **String**| The invite token to resolve | |

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the conversation object that belongs to the invite token if you are member of the conversation |  -  |
| **400** | In case no invitation token was send |  -  |
| **401** | The authentication was not successful |  -  |
| **404** | If the token does not exist or you are not member of the conversation  |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="searchConversations"></a>
# **searchConversations**
> ConversationSearchResult searchConversations(term, includeItemIds, scope)

Performs a conversation search

Performs a search for conversation content. A maximum of 100 conversations is returned. If you hit this limit you should refine the search term. OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String term = "term_example"; // String | The search term
    Boolean includeItemIds = false; // Boolean | Optional parameter to specify if a deep or normal search is executed. In a deep search all matching item IDs inside every conversation are returned (up to a maximum of 100). For a normal search only the conversation IDs are returned. Default is a normal search (without item IDs).
    String scope = "FILES"; // String | The search scope, FILES||PEOPLE||MEMBERS||MESSAGES||SENTBY||ALL||CONVERSATIONS||LABEL||FILTER
    try {
      ConversationSearchResult result = apiInstance.searchConversations(term, includeItemIds, scope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#searchConversations");
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
| **term** | **String**| The search term | |
| **includeItemIds** | **Boolean**| Optional parameter to specify if a deep or normal search is executed. In a deep search all matching item IDs inside every conversation are returned (up to a maximum of 100). For a normal search only the conversation IDs are returned. Default is a normal search (without item IDs). | [optional] [default to false] |
| **scope** | **String**| The search scope, FILES||PEOPLE||MEMBERS||MESSAGES||SENTBY||ALL||CONVERSATIONS||LABEL||FILTER | [optional] [default to ALL] [enum: FILES, PEOPLE, MEMBERS, MESSAGES, SENTBY, ALL, CONVERSATIONS, LABEL, FILTER] |

### Return type

[**ConversationSearchResult**](ConversationSearchResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of conversations and items that match the term |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the user is no participant of the conversation&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="unFlagItem"></a>
# **unFlagItem**
> unFlagItem(convId, itemId)

Removes the flag from a message

Removes the flag from a given message that is posted to the given conversation. OauthScopes: WRITE_CONVERSATIONS, ORGANIZE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation to which the item belongs
    String itemId = "itemId_example"; // String | The ID of the item that will be flagged
    try {
      apiInstance.unFlagItem(convId, itemId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#unFlagItem");
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
| **convId** | **String**| The ID of the conversation to which the item belongs | |
| **itemId** | **String**| The ID of the item that will be flagged | |

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
| **200** | The flagged state of item was successfully removed |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the item does not exist&lt;/li&gt;&lt;li&gt;the user is no participant of the conversation&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="unPinAConversation"></a>
# **unPinAConversation**
> Conversation unPinAConversation(convId, itemId)

Unpins a topic of a conversation

Unpins a topic of a conversation OauthScopes: READ_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation
    String itemId = "itemId_example"; // String | The ID of the topic
    try {
      Conversation result = apiInstance.unPinAConversation(convId, itemId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#unPinAConversation");
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
| **convId** | **String**| The ID of the conversation | |
| **itemId** | **String**| The ID of the topic | |

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the pinned conversation conversation after unpinning a topic |  -  |
| **400** | The request cannot be fulfilled due to bad syntax |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="unassignLabel"></a>
# **unassignLabel**
> Label unassignLabel(convId, labelId)

Removes a label from a conversation

Removes a label from a conversation, you can search and organize your conversations based on these labels OauthScopes: WRITE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation from which the label is removed
    String labelId = "labelId_example"; // String | The actual label 
    try {
      Label result = apiInstance.unassignLabel(convId, labelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#unassignLabel");
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
| **convId** | **String**| The ID of the conversation from which the label is removed | |
| **labelId** | **String**| The actual label  | |

### Return type

[**Label**](Label.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The label was successfully removed |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;li&gt;the label was not assigned to the conversation&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="undoArchiveConversation"></a>
# **undoArchiveConversation**
> undoArchiveConversation(convId)

Unmute conversation

The conversation will no longer be archived but active again OauthScopes: WRITE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation which will be unmarked as muted
    try {
      apiInstance.undoArchiveConversation(convId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#undoArchiveConversation");
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
| **convId** | **String**| The ID of the conversation which will be unmarked as muted | |

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
| **200** | The conversation was successfully unmarked |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the user is no participant of the conversation&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;li&gt;the conversation was not marked before&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="unlikeItem"></a>
# **unlikeItem**
> unlikeItem(convId, itemId)

Removes a \&quot;like\&quot; from a message

Removes a \&quot;like\&quot; from the given message in the given conversation OauthScopes: WRITE_CONVERSATIONS, UPDATE_CONVERSATION_CONTENT

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation to which the item belongs
    String itemId = "itemId_example"; // String | The ID of the item that will be unliked
    try {
      apiInstance.unlikeItem(convId, itemId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#unlikeItem");
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
| **convId** | **String**| The ID of the conversation to which the item belongs | |
| **itemId** | **String**| The ID of the item that will be unliked | |

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
| **200** | The item was successful unliked |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the item does not exist&lt;/li&gt;&lt;li&gt;the user is no participant of the conversation&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="unmoderateConversation"></a>
# **unmoderateConversation**
> unmoderateConversation(convId)

Set conversation unmoderated

Set a conversation to unmoderatd mode OauthScopes: WRITE_CONVERSATIONS, MODERATE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation which will be set to unmoderated state
    try {
      apiInstance.unmoderateConversation(convId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#unmoderateConversation");
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
| **convId** | **String**| The ID of the conversation which will be set to unmoderated state | |

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
| **200** | The conversation is in unmoderated mode |  -  |
| **401** | Forbidden to edit this conversation |  -  |
| **403** | Permission denied |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="updateConversationCommunity"></a>
# **updateConversationCommunity**
> Conversation updateConversationCommunity(convId, description, topic)

Updates the information of a community

Updates the information of the given community. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation which should be updated
    String description = "description_example"; // String | An optional description for the community conversation
    String topic = "topic_example"; // String | An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used)
    try {
      Conversation result = apiInstance.updateConversationCommunity(convId, description, topic);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#updateConversationCommunity");
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
| **convId** | **String**| The ID of the conversation which should be updated | |
| **description** | **String**| An optional description for the community conversation | [optional] |
| **topic** | **String**| An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used) | [optional] |

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the updated conversation object with the new topic / description |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the conversation is not of type COMMUNITY&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="updateConversationGroup"></a>
# **updateConversationGroup**
> Conversation updateConversationGroup(convId, topic)

Updates the information of a group conversation

Updates the information of the given group conversation. OauthScopes: WRITE_CONVERSATIONS, MANAGE_CONVERSATIONS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation which should be updated
    String topic = "topic_example"; // String | An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used)
    try {
      Conversation result = apiInstance.updateConversationGroup(convId, topic);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#updateConversationGroup");
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
| **convId** | **String**| The ID of the conversation which should be updated | |
| **topic** | **String**| An optional topic of the conversation. If not set the Circuit client will render the names of the participants as topic of the conversation (the first 4 names will be used) | [optional] |

### Return type

[**Conversation**](Conversation.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the updated conversation object with the new topic |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the conversation is not of type GROUP&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="updateProfile"></a>
# **updateProfile**
> User updateProfile(firstname, jobTitle, lastname, locale)

Updates the user profile

Updates the user profile of the authenticated user OauthScopes: WRITE_USER_PROFILE

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String firstname = "firstname_example"; // String | The new firstname of the user
    String jobTitle = "jobTitle_example"; // String | The new job title of the user
    String lastname = "lastname_example"; // String | The new lastname of the user
    String locale = "EN_US"; // String | The new locale of the user. One of EN_US, DE_DE, EN_GB, ES_ES, FR_FR, IT_IT, RU_RU, ZH_HANS_CN.
    try {
      User result = apiInstance.updateProfile(firstname, jobTitle, lastname, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#updateProfile");
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
| **firstname** | **String**| The new firstname of the user | [optional] |
| **jobTitle** | **String**| The new job title of the user | [optional] |
| **lastname** | **String**| The new lastname of the user | [optional] |
| **locale** | **String**| The new locale of the user. One of EN_US, DE_DE, EN_GB, ES_ES, FR_FR, IT_IT, RU_RU, ZH_HANS_CN. | [optional] [enum: EN_US, DE_DE, EN_GB, ES_ES, FR_FR, IT_IT, RU_RU, ZH_HANS_CN, PT_BR, NL_NL, CA_ES] |

### Return type

[**User**](User.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The modified user object. |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the user does not exist&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="updateTextItem"></a>
# **updateTextItem**
> ConversationItem updateTextItem(convId, itemId, attachments, content, formMetaData, subject)

Updates a message

Updates the content or subject of the existing message. Only the creator of the message is allowed to perform this operation. OauthScopes: WRITE_CONVERSATIONS, UPDATE_CONVERSATION_CONTENT

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConversationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    ConversationsApi apiInstance = new ConversationsApi(defaultClient);
    String convId = "convId_example"; // String | The ID of the conversation to which the item belongs
    String itemId = "itemId_example"; // String | The ID of the item to update
    List<String> attachments = Arrays.asList(); // List<String> | A comma separated list of attachment IDs from the file API.
    String content = "content_example"; // String | The actual content of the item
    String formMetaData = "formMetaData_example"; // String | The form meta data of the new text item
    String subject = "subject_example"; // String | The subject (headline) of the new text item
    try {
      ConversationItem result = apiInstance.updateTextItem(convId, itemId, attachments, content, formMetaData, subject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConversationsApi#updateTextItem");
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
| **convId** | **String**| The ID of the conversation to which the item belongs | |
| **itemId** | **String**| The ID of the item to update | |
| **attachments** | [**List&lt;String&gt;**](String.md)| A comma separated list of attachment IDs from the file API. | [optional] |
| **content** | **String**| The actual content of the item | [optional] |
| **formMetaData** | **String**| The form meta data of the new text item | [optional] |
| **subject** | **String**| The subject (headline) of the new text item | [optional] |

### Return type

[**ConversationItem**](ConversationItem.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Gets the modified text item object |  -  |
| **400** | The request cannot be fulfilled due to bad syntax: &lt;ul&gt;&lt;li&gt;the conversation does not exist&lt;/li&gt;&lt;li&gt;the user is no participant of the conversation&lt;/li&gt;&lt;li&gt;a field constraint is violated&lt;/li&gt;&lt;/ul&gt; |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

