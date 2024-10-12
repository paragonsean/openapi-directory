# SpacesApi

All URIs are relative to *https://circuitsandbox.net/rest/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addParticipantsToSpace**](SpacesApi.md#addParticipantsToSpace) | **POST** /spaces/{id}/participant | Add Participant to Space |
| [**addRecentSpaceSearch**](SpacesApi.md#addRecentSpaceSearch) | **PUT** /spaces/search/add/recent | Add recent search  |
| [**assignLabels**](SpacesApi.md#assignLabels) | **POST** /spaces/{id}/labels/assign | Assign labels |
| [**cancelSpaceSearch**](SpacesApi.md#cancelSpaceSearch) | **PUT** /spaces/search/cancel/{searchId} | Cancels a space search of a client. |
| [**createReply**](SpacesApi.md#createReply) | **POST** /spaces/{spaceId}/topic/{topicId}/reply | creates a reply to a topic |
| [**createSpace**](SpacesApi.md#createSpace) | **POST** /spaces/create | Create a space |
| [**createSpaceTopic**](SpacesApi.md#createSpaceTopic) | **POST** /spaces/{spaceId}/topic | creates a new space topic |
| [**deleteSpace**](SpacesApi.md#deleteSpace) | **DELETE** /spaces/{id} | Delete a space |
| [**deleteSpaceItem**](SpacesApi.md#deleteSpaceItem) | **DELETE** /spaces/item/{itemId} | deletes a space item |
| [**denySpaceAcces**](SpacesApi.md#denySpaceAcces) | **POST** /spaces/{spaceId}/participant/{participantId}/deny | Deny access for a space |
| [**existsSpaceName**](SpacesApi.md#existsSpaceName) | **GET** /spaces/exists/{name} | Space name exists |
| [**flagSpaceItem**](SpacesApi.md#flagSpaceItem) | **PUT** /spaces/flag/{itemId} | flag a space item |
| [**getDirectory**](SpacesApi.md#getDirectory) | **GET** /spaces/directory | Get the directory |
| [**getFlaggedItems**](SpacesApi.md#getFlaggedItems) | **GET** /spaces/flagged | Get flagged items |
| [**getLikes**](SpacesApi.md#getLikes) | **GET** /spaces/likes/{itemId} | Get the likes of an item |
| [**getParticipantsImportData**](SpacesApi.md#getParticipantsImportData) | **GET** /spaces/{spaceId}/participant/import/ | missing documentation |
| [**getPendingParticipants**](SpacesApi.md#getPendingParticipants) | **GET** /spaces/{id}/participants/pending | Get the pending participants of a space |
| [**getPinnedTopics**](SpacesApi.md#getPinnedTopics) | **GET** /spaces/{id}/pinnedTopics | Retrieve pinned topics |
| [**getRecentSearches**](SpacesApi.md#getRecentSearches) | **GET** /spaces/search/recent | Retrieve recent space searches |
| [**getSpaceParticipants**](SpacesApi.md#getSpaceParticipants) | **GET** /spaces/{id}/participants | Get the participants of a space |
| [**getSpaceReplies**](SpacesApi.md#getSpaceReplies) | **GET** /spaces/{spaceId}/topic/{topicId}/reply | Gets space replies |
| [**getSpaceTopics**](SpacesApi.md#getSpaceTopics) | **GET** /spaces/{spaceId}/topics | Gets space topics |
| [**getSpaces**](SpacesApi.md#getSpaces) | **GET** /spaces | Get the spaces |
| [**getSpacesByIds**](SpacesApi.md#getSpacesByIds) | **GET** /spaces/ids | Get the spaces by their ids |
| [**grantSpaceAcces**](SpacesApi.md#grantSpaceAcces) | **POST** /spaces/{spaceId}/participant/{participantId}/grant | grant access for a space |
| [**joinSpace**](SpacesApi.md#joinSpace) | **POST** /spaces/{id}/join | Join a space |
| [**leaveSpace**](SpacesApi.md#leaveSpace) | **POST** /spaces/{id}/leave | Leave a space |
| [**likeSpaceItem**](SpacesApi.md#likeSpaceItem) | **PUT** /spaces/like/{itemId} | Like a space item |
| [**pinTopic**](SpacesApi.md#pinTopic) | **PUT** /spaces/{topicId}/pin | Pin a topic |
| [**requestSpaceAcces**](SpacesApi.md#requestSpaceAcces) | **POST** /spaces/{spaceId}/participant/request | request access for a space |
| [**searchParticipantsToAdd**](SpacesApi.md#searchParticipantsToAdd) | **GET** /spaces/{id}/searchParticipantsToAdd | Finds participants to add to add to a space  |
| [**searchSpaceParticipants**](SpacesApi.md#searchSpaceParticipants) | **GET** /spaces/{id}/searchSpaceParticipants | Get the participants of a space |
| [**startBasicSpacesSearch**](SpacesApi.md#startBasicSpacesSearch) | **GET** /spaces/search/startBasic | starts a basic search in spaces |
| [**startDetailedSpaceSearch**](SpacesApi.md#startDetailedSpaceSearch) | **GET** /spaces/search/startDetailed | starts a detailed search in a space |
| [**unassignLabels**](SpacesApi.md#unassignLabels) | **DELETE** /spaces/{id}/labels/unassign | Unassign labels |
| [**unflagSpaceItem**](SpacesApi.md#unflagSpaceItem) | **PUT** /spaces/unflag/{itemId} | Unflag a space item |
| [**unlikeSpaceItem**](SpacesApi.md#unlikeSpaceItem) | **PUT** /spaces/unlike/{itemId} | Unlike a space item |
| [**unpinTopic**](SpacesApi.md#unpinTopic) | **PUT** /spaces/{topicId}/unpin | Unpin a topic |
| [**updateParticipantInSpace**](SpacesApi.md#updateParticipantInSpace) | **PUT** /spaces/{spaceId}/participant | Update participant |
| [**updateReadTimestamp**](SpacesApi.md#updateReadTimestamp) | **PUT** /spaces/{id}/updateTimestamp | Update read timestamp |
| [**updateSpace**](SpacesApi.md#updateSpace) | **PUT** /spaces/{id} | Update a space |
| [**updateSpaceReply**](SpacesApi.md#updateSpaceReply) | **PUT** /spaces/{spaceId}/topic/{topicId}/reply/{replyId} | Updates a space reply |
| [**updateSpaceTopic**](SpacesApi.md#updateSpaceTopic) | **PUT** /spaces/{spaceId}/topic/{topicId} | Updates a topic |
| [**updateTopicTags**](SpacesApi.md#updateTopicTags) | **PUT** /spaces/topic/{topicId}/updateTags | Update tags |
| [**v2GetTopicWithReplies**](SpacesApi.md#v2GetTopicWithReplies) | **GET** /spaces/{spaceId}/topic/{topicId} | Gets space replies and a topic |
| [**v2RemoveParticipantsFromSpace**](SpacesApi.md#v2RemoveParticipantsFromSpace) | **POST** /spaces/{id}/participant/remove | Removes participants from a space |
| [**v2UpdateWelcomeBoxContent**](SpacesApi.md#v2UpdateWelcomeBoxContent) | **PUT** /spaces/{spaceId}/welcomebox/{content} | Update content of welcome box |


<a id="addParticipantsToSpace"></a>
# **addParticipantsToSpace**
> List&lt;Object&gt; addParticipantsToSpace(id, role, userId)

Add Participant to Space

Add a participant to a space OauthScopes: WRITE_SPACE, MANAGE_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String id = "id_example"; // String | The id of the space
    String role = "DEFAULT"; // String | The name of the role of the participant
    List<String> userId = Arrays.asList(); // List<String> | The user id of the participant
    try {
      List<Object> result = apiInstance.addParticipantsToSpace(id, role, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#addParticipantsToSpace");
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
| **id** | **String**| The id of the space | |
| **role** | **String**| The name of the role of the participant | [default to DEFAULT] [enum: DEFAULT, MODERATOR, AUTHOR, PARTICIPANT, READER] |
| **userId** | [**List&lt;String&gt;**](String.md)| The user id of the participant | |

### Return type

**List&lt;Object&gt;**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully added participant. |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="addRecentSpaceSearch"></a>
# **addRecentSpaceSearch**
> addRecentSpaceSearch(scope, searchTerm, endTime, startTime)

Add recent search 

Add recent search of a client to search controller. OauthScopes: WRITE_SPACE, MANAGE_SPACE, ORGANIZE_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String scope = "ALL"; // String | The scope of the search.
    String searchTerm = "searchTerm_example"; // String | The term to search for.
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime | The end time.
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime | The start time.
    try {
      apiInstance.addRecentSpaceSearch(scope, searchTerm, endTime, startTime);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#addRecentSpaceSearch");
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
| **scope** | **String**| The scope of the search. | [enum: ALL, SPACES, TOPICBY, FILES, TAGS, LABELS, DATE] |
| **searchTerm** | **String**| The term to search for. | |
| **endTime** | **OffsetDateTime**| The end time. | [optional] |
| **startTime** | **OffsetDateTime**| The start time. | [optional] |

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
| **200** | Search successfully added. |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="assignLabels"></a>
# **assignLabels**
> List&lt;LabelIds&gt; assignLabels(id, labels)

Assign labels

Assign labels to space OauthScopes: WRITE_SPACE, ORGANIZE_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String id = "id_example"; // String | The id of the space.
    List<String> labels = Arrays.asList(); // List<String> | The labels to assign to the space
    try {
      List<LabelIds> result = apiInstance.assignLabels(id, labels);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#assignLabels");
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
| **id** | **String**| The id of the space. | |
| **labels** | [**List&lt;String&gt;**](String.md)| The labels to assign to the space | |

### Return type

[**List&lt;LabelIds&gt;**](LabelIds.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Labels successfully assigned |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="cancelSpaceSearch"></a>
# **cancelSpaceSearch**
> cancelSpaceSearch(searchId)

Cancels a space search of a client.

Cancels a space search of a client. OauthScopes: WRITE_SPACE, MANAGE_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String searchId = "searchId_example"; // String | The id of the search to cancel
    try {
      apiInstance.cancelSpaceSearch(searchId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#cancelSpaceSearch");
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
| **searchId** | **String**| The id of the search to cancel | |

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
| **200** | Search successfully cancelled. |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="createReply"></a>
# **createReply**
> SpaceReply createReply(spaceId, topicId, attachments, complex, content, formMetaData, mentionedUser)

creates a reply to a topic

creates a reply to a topic OauthScopes: WRITE_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String spaceId = "spaceId_example"; // String | ID of the space
    String topicId = "topicId_example"; // String | ID of the topic
    List<String> attachments = Arrays.asList(); // List<String> | the attached files
    Boolean complex = true; // Boolean | complex or not
    String content = "content_example"; // String | Content of the reply
    String formMetaData = "formMetaData_example"; // String | formMetaData used in the reply
    String mentionedUser = "mentionedUser_example"; // String | the user mentioned in the reply
    try {
      SpaceReply result = apiInstance.createReply(spaceId, topicId, attachments, complex, content, formMetaData, mentionedUser);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#createReply");
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
| **spaceId** | **String**| ID of the space | |
| **topicId** | **String**| ID of the topic | |
| **attachments** | [**List&lt;String&gt;**](String.md)| the attached files | [optional] |
| **complex** | **Boolean**| complex or not | [optional] |
| **content** | **String**| Content of the reply | [optional] |
| **formMetaData** | **String**| formMetaData used in the reply | [optional] |
| **mentionedUser** | **String**| the user mentioned in the reply | [optional] |

### Return type

[**SpaceReply**](SpaceReply.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | returns the created reply |  -  |
| **400** | invalid input |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="createSpace"></a>
# **createSpace**
> Object createSpace(accessModeType, name, role, status, type, description, largePictureBase64, smallPictureBase64, tags)

Create a space

Create a space OauthScopes: WRITE_SPACE, MANAGE_SPACE, CREATE_SPACE_CONTENT

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String accessModeType = "INTERNAL_ONLY"; // String | Access mode
    String name = "name_example"; // String | name of the space
    String role = "MODERATOR"; // String | role
    String status = "ENABLED"; // String | status
    String type = "OPEN"; // String | type
    String description = "description_example"; // String | description of the space
    String largePictureBase64 = "largePictureBase64_example"; // String | large picture
    String smallPictureBase64 = "smallPictureBase64_example"; // String | small picture
    List<String> tags = Arrays.asList(); // List<String> | tags of the space
    try {
      Object result = apiInstance.createSpace(accessModeType, name, role, status, type, description, largePictureBase64, smallPictureBase64, tags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#createSpace");
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
| **accessModeType** | **String**| Access mode | [default to INTERNAL_ONLY] [enum: INTERNAL_ONLY, INTERNAL_EXTERNAL] |
| **name** | **String**| name of the space | |
| **role** | **String**| role | [default to AUTHOR] [enum: MODERATOR, AUTHOR, PARTICIPANT, READER] |
| **status** | **String**| status | [default to ENABLED] [enum: ENABLED, DISABLED] |
| **type** | **String**| type | [default to SECRET] [enum: OPEN, CLOSED, SECRET] |
| **description** | **String**| description of the space | [optional] |
| **largePictureBase64** | **String**| large picture | [optional] |
| **smallPictureBase64** | **String**| small picture | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| tags of the space | [optional] |

### Return type

**Object**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Space successfully created. |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="createSpaceTopic"></a>
# **createSpaceTopic**
> SpaceTopic createSpaceTopic(spaceId, subject, attachments, complex, content, contentTags, formMetaData, mentionedUser, tags)

creates a new space topic

creates a new space topic OauthScopes: WRITE_SPACE, MANAGE_SPACE, CREATE_SPACE_CONTENT

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String spaceId = "spaceId_example"; // String | The ID of the space
    String subject = "subject_example"; // String | The subject of the topic
    List<String> attachments = Arrays.asList(); // List<String> | the attached files
    Boolean complex = true; // Boolean | complex or not
    String content = "content_example"; // String | The content of this topic
    List<String> contentTags = Arrays.asList(); // List<String> | the content tags
    String formMetaData = "formMetaData_example"; // String | The formMetaData
    String mentionedUser = "mentionedUser_example"; // String | A list of mentioned users
    List<String> tags = Arrays.asList(); // List<String> | the tags
    try {
      SpaceTopic result = apiInstance.createSpaceTopic(spaceId, subject, attachments, complex, content, contentTags, formMetaData, mentionedUser, tags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#createSpaceTopic");
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
| **spaceId** | **String**| The ID of the space | |
| **subject** | **String**| The subject of the topic | |
| **attachments** | [**List&lt;String&gt;**](String.md)| the attached files | [optional] |
| **complex** | **Boolean**| complex or not | [optional] |
| **content** | **String**| The content of this topic | [optional] |
| **contentTags** | [**List&lt;String&gt;**](String.md)| the content tags | [optional] |
| **formMetaData** | **String**| The formMetaData | [optional] |
| **mentionedUser** | **String**| A list of mentioned users | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| the tags | [optional] |

### Return type

[**SpaceTopic**](SpaceTopic.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | returns the created topic |  -  |
| **400** | something went wrong |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="deleteSpace"></a>
# **deleteSpace**
> deleteSpace(id)

Delete a space

Delete a space OauthScopes: WRITE_SPACE, MANAGE_SPACE, DELETE_SPACE_CONTENT

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String id = "id_example"; // String | id of the space
    try {
      apiInstance.deleteSpace(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#deleteSpace");
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
| **id** | **String**| id of the space | |

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
| **200** | Space successfully deleted. |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="deleteSpaceItem"></a>
# **deleteSpaceItem**
> deleteSpaceItem(itemId)

deletes a space item

deletes a space item OauthScopes: WRITE_SPACE, DELETE_SPACE_CONTENT

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String itemId = "itemId_example"; // String | the id of the spaceItem
    try {
      apiInstance.deleteSpaceItem(itemId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#deleteSpaceItem");
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
| **itemId** | **String**| the id of the spaceItem | |

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
| **200** | the deletion was a success |  -  |
| **400** | invalid itemid |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="denySpaceAcces"></a>
# **denySpaceAcces**
> denySpaceAcces(spaceId, participantId, reason)

Deny access for a space

Deny access for a space OauthScopes: WRITE_SPACE, MANAGE_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String spaceId = "spaceId_example"; // String | Id of the space
    String participantId = "participantId_example"; // String | Id of the participant
    String reason = "reason_example"; // String | Reason why the request has been denied
    try {
      apiInstance.denySpaceAcces(spaceId, participantId, reason);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#denySpaceAcces");
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
| **spaceId** | **String**| Id of the space | |
| **participantId** | **String**| Id of the participant | |
| **reason** | **String**| Reason why the request has been denied | [optional] |

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
| **200** | Access denied |  -  |
| **400** | Invalid parameter |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="existsSpaceName"></a>
# **existsSpaceName**
> existsSpaceName(name)

Space name exists

Find out if a space name already exists for non-secret spaces. OauthScopes: READ_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String name = "name_example"; // String | The name to check for existence.
    try {
      apiInstance.existsSpaceName(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#existsSpaceName");
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
| **name** | **String**| The name to check for existence. | |

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
| **200** | Check performed successfully, returning true if found, false if not found. |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="flagSpaceItem"></a>
# **flagSpaceItem**
> flagSpaceItem(itemId)

flag a space item

flag a space item OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String itemId = "itemId_example"; // String | the id of the item you want to flag
    try {
      apiInstance.flagSpaceItem(itemId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#flagSpaceItem");
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
| **itemId** | **String**| the id of the item you want to flag | |

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
| **200** | Space item successfully flagged |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getDirectory"></a>
# **getDirectory**
> DirectoryResult getDirectory(sortBy, sortOrder, filter, query, pagePointer, numberOfResults)

Get the directory

Get the directory by a search query in ordered way OauthScopes: READ_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String sortBy = "LAST_CONTENT"; // String | sort the spaces by LAST_CONTENT, NAME, NUMBER_OF_USERS or CREATION_DATE
    String sortOrder = "ASCENDING"; // String | ascending or descending
    String filter = "NONE"; // String | filter for spaces (JOINED, REQUESTED, OPEN, CLOSED or NOT_JOINED_REQUESTED)
    String query = "query_example"; // String | some sort of query
    String pagePointer = "pagePointer_example"; // String | page pointer, start with nothing and for next query use returned pointer
    BigDecimal numberOfResults = new BigDecimal("25"); // BigDecimal | number of results to return, 25 by default.
    try {
      DirectoryResult result = apiInstance.getDirectory(sortBy, sortOrder, filter, query, pagePointer, numberOfResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#getDirectory");
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
| **sortBy** | **String**| sort the spaces by LAST_CONTENT, NAME, NUMBER_OF_USERS or CREATION_DATE | [default to LAST_CONTENT] [enum: LAST_CONTENT, NAME, NUMBER_OF_USERS, CREATION_DATE] |
| **sortOrder** | **String**| ascending or descending | [default to ASCENDING] [enum: ASCENDING, DESCENDING] |
| **filter** | **String**| filter for spaces (JOINED, REQUESTED, OPEN, CLOSED or NOT_JOINED_REQUESTED) | [default to NONE] [enum: NONE, JOINED, REQUESTED, OPEN, CLOSED, NOT_JOINED_REQUESTED] |
| **query** | **String**| some sort of query | [optional] |
| **pagePointer** | **String**| page pointer, start with nothing and for next query use returned pointer | [optional] |
| **numberOfResults** | **BigDecimal**| number of results to return, 25 by default. | [optional] [default to 25] |

### Return type

[**DirectoryResult**](DirectoryResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Spaces successfully retrieved. |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getFlaggedItems"></a>
# **getFlaggedItems**
> FlaggedItemsResult getFlaggedItems(searchDirection, timestamp, searchPointer, numberOfResults)

Get flagged items

Get flagged items OauthScopes: READ_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String searchDirection = "BEFORE"; // String | before or after the time stamp
    OffsetDateTime timestamp = OffsetDateTime.now(); // OffsetDateTime | The timestamp according to which you want to retrieve the flagged items
    String searchPointer = "searchPointer_example"; // String | The searchpointer for the search (initially not set).
    BigDecimal numberOfResults = new BigDecimal("25"); // BigDecimal | The number of results you want to retrieve.
    try {
      FlaggedItemsResult result = apiInstance.getFlaggedItems(searchDirection, timestamp, searchPointer, numberOfResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#getFlaggedItems");
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
| **searchDirection** | **String**| before or after the time stamp | [default to BEFORE] [enum: BEFORE, AFTER] |
| **timestamp** | **OffsetDateTime**| The timestamp according to which you want to retrieve the flagged items | |
| **searchPointer** | **String**| The searchpointer for the search (initially not set). | [optional] |
| **numberOfResults** | **BigDecimal**| The number of results you want to retrieve. | [optional] [default to 25] |

### Return type

[**FlaggedItemsResult**](FlaggedItemsResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Flagged items successfully retrieved |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getLikes"></a>
# **getLikes**
> ParticipantsLikeResult getLikes(itemId, searchPointer, numberOfResults)

Get the likes of an item

Get the likes of an item OauthScopes: READ_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String itemId = "itemId_example"; // String | The id of the item to retrieve the likes from
    String searchPointer = "searchPointer_example"; // String | The searchpointer for the search (initially not set).
    BigDecimal numberOfResults = new BigDecimal("25"); // BigDecimal | The number of results you want to retrieve.
    try {
      ParticipantsLikeResult result = apiInstance.getLikes(itemId, searchPointer, numberOfResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#getLikes");
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
| **itemId** | **String**| The id of the item to retrieve the likes from | |
| **searchPointer** | **String**| The searchpointer for the search (initially not set). | [optional] |
| **numberOfResults** | **BigDecimal**| The number of results you want to retrieve. | [optional] [default to 25] |

### Return type

[**ParticipantsLikeResult**](ParticipantsLikeResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Likes successfully retrieved |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getParticipantsImportData"></a>
# **getParticipantsImportData**
> ParticipantsImportDataResult getParticipantsImportData(spaceId)

missing documentation

missing documentation OauthScopes: READ_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String spaceId = "spaceId_example"; // String | missing documentation
    try {
      ParticipantsImportDataResult result = apiInstance.getParticipantsImportData(spaceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#getParticipantsImportData");
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
| **spaceId** | **String**| missing documentation | |

### Return type

[**ParticipantsImportDataResult**](ParticipantsImportDataResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | missing documentation |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getPendingParticipants"></a>
# **getPendingParticipants**
> ParticipantsSearchResult getPendingParticipants(id, searchPointer, numberOfResults)

Get the pending participants of a space

Get the pending participants of a space OauthScopes: WRITE_SPACE, MANAGE_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String id = "id_example"; // String | The id of the space.
    String searchPointer = "searchPointer_example"; // String | The search pointer (leave empty initially).
    BigDecimal numberOfResults = new BigDecimal("25"); // BigDecimal | number of results to return, 25 by default.
    try {
      ParticipantsSearchResult result = apiInstance.getPendingParticipants(id, searchPointer, numberOfResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#getPendingParticipants");
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
| **id** | **String**| The id of the space. | |
| **searchPointer** | **String**| The search pointer (leave empty initially). | [optional] |
| **numberOfResults** | **BigDecimal**| number of results to return, 25 by default. | [optional] [default to 25] |

### Return type

[**ParticipantsSearchResult**](ParticipantsSearchResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pending participants successfully retrieved |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getPinnedTopics"></a>
# **getPinnedTopics**
> List&lt;SpacePinnedTopic&gt; getPinnedTopics(id)

Retrieve pinned topics

Retrieve pinned topics of a space OauthScopes: READ_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String id = "id_example"; // String | The id of the space.
    try {
      List<SpacePinnedTopic> result = apiInstance.getPinnedTopics(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#getPinnedTopics");
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
| **id** | **String**| The id of the space. | |

### Return type

[**List&lt;SpacePinnedTopic&gt;**](SpacePinnedTopic.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pinned topics successfully retrieved (or none available).  |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getRecentSearches"></a>
# **getRecentSearches**
> List&lt;SpacesSearchTermResult&gt; getRecentSearches()

Retrieve recent space searches

Retrieve recent space searches for a user. OauthScopes: READ_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    try {
      List<SpacesSearchTermResult> result = apiInstance.getRecentSearches();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#getRecentSearches");
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

[**List&lt;SpacesSearchTermResult&gt;**](SpacesSearchTermResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Recent searches successfully retrieved (or none available). |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getSpaceParticipants"></a>
# **getSpaceParticipants**
> ParticipantsSearchResult getSpaceParticipants(id, sortBy, sortOrder, filterType, filterValue, query, searchPointer, numberOfResults)

Get the participants of a space

Get the participants of a space OauthScopes: READ_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String id = "id_example"; // String | The id of the space.
    String sortBy = "DISPLAY_NAME"; // String | sort the spaces by LAST_CONTENT, NAME, NUMBER_OF_USERS or CREATION_DATE
    String sortOrder = "ASCENDING"; // String | ascending or descending
    String filterType = "NONE"; // String | filtertype for participants (ACCESS_TYPE, ROLE or STATE)
    String filterValue = "filterValue_example"; // String | value for the filter
    String query = "query_example"; // String | some sort of query
    String searchPointer = "searchPointer_example"; // String | The search pointer (leave empty initially).
    BigDecimal numberOfResults = new BigDecimal("25"); // BigDecimal | number of results to return, 25 by default.
    try {
      ParticipantsSearchResult result = apiInstance.getSpaceParticipants(id, sortBy, sortOrder, filterType, filterValue, query, searchPointer, numberOfResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#getSpaceParticipants");
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
| **id** | **String**| The id of the space. | |
| **sortBy** | **String**| sort the spaces by LAST_CONTENT, NAME, NUMBER_OF_USERS or CREATION_DATE | [default to NAME] [enum: DISPLAY_NAME, NAME, FIRST_NAME] |
| **sortOrder** | **String**| ascending or descending | [default to ASCENDING] [enum: ASCENDING, DESCENDING] |
| **filterType** | **String**| filtertype for participants (ACCESS_TYPE, ROLE or STATE) | [enum: NONE, ACCESS_TYPE, ROLE, STATE] |
| **filterValue** | **String**| value for the filter | [optional] |
| **query** | **String**| some sort of query | [optional] |
| **searchPointer** | **String**| The search pointer (leave empty initially). | [optional] |
| **numberOfResults** | **BigDecimal**| number of results to return, 25 by default. | [optional] [default to 25] |

### Return type

[**ParticipantsSearchResult**](ParticipantsSearchResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Participants successfully retrieved |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getSpaceReplies"></a>
# **getSpaceReplies**
> SpaceReply getSpaceReplies(spaceId, topicId, searchDirection, timestamp, numberOfResults)

Gets space replies

Gets a number of Space replies OauthScopes: READ_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String spaceId = "spaceId_example"; // String | Id of the containing space
    String topicId = "topicId_example"; // String | Id of the topic
    String searchDirection = "BEFORE"; // String | Search before or after a certain timestamp
    OffsetDateTime timestamp = OffsetDateTime.now(); // OffsetDateTime | Timestamp to start the search from
    BigDecimal numberOfResults = new BigDecimal("25"); // BigDecimal | The number of results that should be returned
    try {
      SpaceReply result = apiInstance.getSpaceReplies(spaceId, topicId, searchDirection, timestamp, numberOfResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#getSpaceReplies");
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
| **spaceId** | **String**| Id of the containing space | |
| **topicId** | **String**| Id of the topic | |
| **searchDirection** | **String**| Search before or after a certain timestamp | [default to BEFORE] [enum: BEFORE, AFTER] |
| **timestamp** | **OffsetDateTime**| Timestamp to start the search from | [optional] |
| **numberOfResults** | **BigDecimal**| The number of results that should be returned | [optional] [default to 25] |

### Return type

[**SpaceReply**](SpaceReply.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the replies |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getSpaceTopics"></a>
# **getSpaceTopics**
> List&lt;SpaceTopic&gt; getSpaceTopics(spaceId, searchDirection, timestamp, numberOfResults)

Gets space topics

Gets a number of Space topics OauthScopes: READ_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String spaceId = "spaceId_example"; // String | Id of the space
    String searchDirection = "BEFORE"; // String | Search before or after a certain timestamp
    OffsetDateTime timestamp = OffsetDateTime.now(); // OffsetDateTime | Timestamp to start the search from
    BigDecimal numberOfResults = new BigDecimal("25"); // BigDecimal | The number of results that should be returned
    try {
      List<SpaceTopic> result = apiInstance.getSpaceTopics(spaceId, searchDirection, timestamp, numberOfResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#getSpaceTopics");
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
| **spaceId** | **String**| Id of the space | |
| **searchDirection** | **String**| Search before or after a certain timestamp | [default to BEFORE] [enum: BEFORE, AFTER] |
| **timestamp** | **OffsetDateTime**| Timestamp to start the search from | [optional] |
| **numberOfResults** | **BigDecimal**| The number of results that should be returned | [optional] [default to 25] |

### Return type

[**List&lt;SpaceTopic&gt;**](SpaceTopic.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the the topics |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getSpaces"></a>
# **getSpaces**
> Object getSpaces(timestamp, numberOfResults)

Get the spaces

Get the spaces OauthScopes: READ_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    OffsetDateTime timestamp = OffsetDateTime.now(); // OffsetDateTime | a beautiful timestamp
    BigDecimal numberOfResults = new BigDecimal(78); // BigDecimal | the number of results you want
    try {
      Object result = apiInstance.getSpaces(timestamp, numberOfResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#getSpaces");
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
| **timestamp** | **OffsetDateTime**| a beautiful timestamp | [optional] |
| **numberOfResults** | **BigDecimal**| the number of results you want | [optional] |

### Return type

**Object**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Spaces successfully retrieved. |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="getSpacesByIds"></a>
# **getSpacesByIds**
> Object getSpacesByIds(ids)

Get the spaces by their ids

Get the spaces by their ids OauthScopes: READ_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | an array of ids
    try {
      Object result = apiInstance.getSpacesByIds(ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#getSpacesByIds");
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
| **ids** | [**List&lt;String&gt;**](String.md)| an array of ids | |

### Return type

**Object**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Spaces successfully retrieved. |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="grantSpaceAcces"></a>
# **grantSpaceAcces**
> grantSpaceAcces(spaceId, participantId)

grant access for a space

grant access for a space OauthScopes: WRITE_SPACE, MANAGE_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String spaceId = "spaceId_example"; // String | Id of the space
    String participantId = "participantId_example"; // String | Id of the participant
    try {
      apiInstance.grantSpaceAcces(spaceId, participantId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#grantSpaceAcces");
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
| **spaceId** | **String**| Id of the space | |
| **participantId** | **String**| Id of the participant | |

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
| **200** | access granted |  -  |
| **400** | invalid parameter |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="joinSpace"></a>
# **joinSpace**
> Object joinSpace(id)

Join a space

Join a space OauthScopes: WRITE_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String id = "id_example"; // String | The id of the space
    try {
      Object result = apiInstance.joinSpace(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#joinSpace");
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
| **id** | **String**| The id of the space | |

### Return type

**Object**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Space successfully joined |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="leaveSpace"></a>
# **leaveSpace**
> leaveSpace(id)

Leave a space

Leave a space OauthScopes: WRITE_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String id = "id_example"; // String | The id of the space
    try {
      apiInstance.leaveSpace(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#leaveSpace");
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
| **id** | **String**| The id of the space | |

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
| **200** | Space successfully left |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="likeSpaceItem"></a>
# **likeSpaceItem**
> likeSpaceItem(itemId)

Like a space item

Like a space item OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String itemId = "itemId_example"; // String | The id of the item you want to like
    try {
      apiInstance.likeSpaceItem(itemId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#likeSpaceItem");
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
| **itemId** | **String**| The id of the item you want to like | |

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
| **200** | Space item successfully liked |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="pinTopic"></a>
# **pinTopic**
> pinTopic(topicId, position)

Pin a topic

Pin a topic OauthScopes: WRITE_SPACE, MANAGE_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String topicId = "topicId_example"; // String | The id of the topic
    BigDecimal position = new BigDecimal(78); // BigDecimal | The position to pin to
    try {
      apiInstance.pinTopic(topicId, position);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#pinTopic");
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
| **topicId** | **String**| The id of the topic | |
| **position** | **BigDecimal**| The position to pin to | |

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
| **200** | Topic successfully pinned. |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="requestSpaceAcces"></a>
# **requestSpaceAcces**
> requestSpaceAcces(spaceId, reason)

request access for a space

request access for a space OauthScopes: READ_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String spaceId = "spaceId_example"; // String | Id of the space
    String reason = "reason_example"; // String | Reason why the Access has been requested
    try {
      apiInstance.requestSpaceAcces(spaceId, reason);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#requestSpaceAcces");
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
| **spaceId** | **String**| Id of the space | |
| **reason** | **String**| Reason why the Access has been requested | [optional] |

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
| **200** | request is recieved |  -  |
| **400** | invalid parameter |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="searchParticipantsToAdd"></a>
# **searchParticipantsToAdd**
> List&lt;AddParticipantsSearchResult&gt; searchParticipantsToAdd(id, query)

Finds participants to add to add to a space 

Finds participants to add to a space  OauthScopes: WRITE_SPACE, MANAGE_SPACE, ORGANIZE_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String id = "id_example"; // String | The id of the space
    String query = "query_example"; // String | The query 
    try {
      List<AddParticipantsSearchResult> result = apiInstance.searchParticipantsToAdd(id, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#searchParticipantsToAdd");
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
| **id** | **String**| The id of the space | |
| **query** | **String**| The query  | |

### Return type

[**List&lt;AddParticipantsSearchResult&gt;**](AddParticipantsSearchResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | participants successfully found |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="searchSpaceParticipants"></a>
# **searchSpaceParticipants**
> List&lt;ParticipantsSearchResultLarge&gt; searchSpaceParticipants(id, query)

Get the participants of a space

Get the participants of a space OauthScopes: READ_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String id = "id_example"; // String | The id of the space.
    String query = "query_example"; // String | The query to search with. If searchpointer/hasMotre is returned, refine query.
    try {
      List<ParticipantsSearchResultLarge> result = apiInstance.searchSpaceParticipants(id, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#searchSpaceParticipants");
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
| **id** | **String**| The id of the space. | |
| **query** | **String**| The query to search with. If searchpointer/hasMotre is returned, refine query. | |

### Return type

[**List&lt;ParticipantsSearchResultLarge&gt;**](ParticipantsSearchResultLarge.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Participants successfully retrieved |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="startBasicSpacesSearch"></a>
# **startBasicSpacesSearch**
> BasicSearchResult startBasicSpacesSearch(scope, searchTerm, startTime, endTime, prioritySpaces)

starts a basic search in spaces

starts a basic search in spaces OauthScopes: READ_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String scope = "ALL"; // String | the scope of the search
    String searchTerm = "searchTerm_example"; // String | the term to search for
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime | the starttime
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime | the end time
    List<String> prioritySpaces = Arrays.asList(); // List<String> | list of prioritized spaces
    try {
      BasicSearchResult result = apiInstance.startBasicSpacesSearch(scope, searchTerm, startTime, endTime, prioritySpaces);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#startBasicSpacesSearch");
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
| **scope** | **String**| the scope of the search | [enum: ALL, SPACES, TOPICBY, FILES, TAGS, LABELS, DATE] |
| **searchTerm** | **String**| the term to search for | |
| **startTime** | **OffsetDateTime**| the starttime | [optional] |
| **endTime** | **OffsetDateTime**| the end time | [optional] |
| **prioritySpaces** | [**List&lt;String&gt;**](String.md)| list of prioritized spaces | [optional] |

### Return type

[**BasicSearchResult**](BasicSearchResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search successfully executed |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="startDetailedSpaceSearch"></a>
# **startDetailedSpaceSearch**
> List&lt;SpaceSearchResultDetailedBack&gt; startDetailedSpaceSearch(scope, searchTerm, spaceId, startTime, endTime, searchId)

starts a detailed search in a space

starts a detailed search in a space OauthScopes: READ_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String scope = "ALL"; // String | the scope of the search
    String searchTerm = "searchTerm_example"; // String | the term to search for
    String spaceId = "spaceId_example"; // String | missing documentation
    OffsetDateTime startTime = OffsetDateTime.now(); // OffsetDateTime | the starttime
    OffsetDateTime endTime = OffsetDateTime.now(); // OffsetDateTime | the end time
    String searchId = "searchId_example"; // String | missing documentation
    try {
      List<SpaceSearchResultDetailedBack> result = apiInstance.startDetailedSpaceSearch(scope, searchTerm, spaceId, startTime, endTime, searchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#startDetailedSpaceSearch");
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
| **scope** | **String**| the scope of the search | [enum: ALL, SPACES, TOPICBY, FILES, TAGS, LABELS, DATE] |
| **searchTerm** | **String**| the term to search for | |
| **spaceId** | **String**| missing documentation | |
| **startTime** | **OffsetDateTime**| the starttime | [optional] |
| **endTime** | **OffsetDateTime**| the end time | [optional] |
| **searchId** | **String**| missing documentation | [optional] |

### Return type

[**List&lt;SpaceSearchResultDetailedBack&gt;**](SpaceSearchResultDetailedBack.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | search successfully executed |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="unassignLabels"></a>
# **unassignLabels**
> List&lt;LabelIds&gt; unassignLabels(id, labelIds)

Unassign labels

Unassign labels from a space OauthScopes: WRITE_SPACE, ORGANIZE_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String id = "id_example"; // String | The id of the space.
    List<String> labelIds = Arrays.asList(); // List<String> | missing documentation
    try {
      List<LabelIds> result = apiInstance.unassignLabels(id, labelIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#unassignLabels");
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
| **id** | **String**| The id of the space. | |
| **labelIds** | [**List&lt;String&gt;**](String.md)| missing documentation | |

### Return type

[**List&lt;LabelIds&gt;**](LabelIds.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Labels successfully unassigned |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="unflagSpaceItem"></a>
# **unflagSpaceItem**
> unflagSpaceItem(itemId)

Unflag a space item

Unflag a space item OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String itemId = "itemId_example"; // String | the id of the item you want to unflag
    try {
      apiInstance.unflagSpaceItem(itemId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#unflagSpaceItem");
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
| **itemId** | **String**| the id of the item you want to unflag | |

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
| **200** | Space item successfully unflagged. |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="unlikeSpaceItem"></a>
# **unlikeSpaceItem**
> unlikeSpaceItem(itemId)

Unlike a space item

Unlike a space item OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String itemId = "itemId_example"; // String | The id of the item you want to unlike
    try {
      apiInstance.unlikeSpaceItem(itemId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#unlikeSpaceItem");
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
| **itemId** | **String**| The id of the item you want to unlike | |

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
| **200** | Space item successfully unliked. |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="unpinTopic"></a>
# **unpinTopic**
> unpinTopic(topicId)

Unpin a topic

Unpin a topic OauthScopes: WRITE_SPACE, MANAGE_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String topicId = "topicId_example"; // String | The id of the topic to unpin
    try {
      apiInstance.unpinTopic(topicId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#unpinTopic");
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
| **topicId** | **String**| The id of the topic to unpin | |

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
| **200** | Topic successfully unpinned. |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="updateParticipantInSpace"></a>
# **updateParticipantInSpace**
> updateParticipantInSpace(spaceId, role, userId)

Update participant

Update participant in space OauthScopes: WRITE_SPACE, MANAGE_SPACE, ORGANIZE_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String spaceId = "spaceId_example"; // String | Id of the space
    String role = "MODERATOR"; // String | updated role of participant
    String userId = "userId_example"; // String | The id of the participant to update
    try {
      apiInstance.updateParticipantInSpace(spaceId, role, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#updateParticipantInSpace");
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
| **spaceId** | **String**| Id of the space | |
| **role** | **String**| updated role of participant | [enum: MODERATOR, AUTHOR, PARTICIPANT, READER] |
| **userId** | **String**| The id of the participant to update | |

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
| **200** | Role successfully updated |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="updateReadTimestamp"></a>
# **updateReadTimestamp**
> updateReadTimestamp(id, timestamp)

Update read timestamp

Update read timestamp OauthScopes: READ_SPACE, WRITE_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String id = "id_example"; // String | Id of a space
    OffsetDateTime timestamp = OffsetDateTime.now(); // OffsetDateTime | The new timestamp
    try {
      apiInstance.updateReadTimestamp(id, timestamp);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#updateReadTimestamp");
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
| **id** | **String**| Id of a space | |
| **timestamp** | **OffsetDateTime**| The new timestamp | |

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
| **200** | Read timestamp successfully updated. |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="updateSpace"></a>
# **updateSpace**
> Object updateSpace(id, accessModeType, description, largePictureBase64, name, ownerId, role, smallPictureBase64, status, tags, type)

Update a space

Update a space OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String id = "id_example"; // String | id of the space
    String accessModeType = "INTERNAL_ONLY"; // String | Access mode
    String description = "description_example"; // String | description of the space
    String largePictureBase64 = "largePictureBase64_example"; // String | large picture
    String name = "name_example"; // String | name of the space
    String ownerId = "ownerId_example"; // String | ownerid of the space
    String role = "MODERATOR"; // String | role
    String smallPictureBase64 = "smallPictureBase64_example"; // String | small picture
    String status = "ENABLED"; // String | status
    List<String> tags = Arrays.asList(); // List<String> | tags of the space
    String type = "OPEN"; // String | type
    try {
      Object result = apiInstance.updateSpace(id, accessModeType, description, largePictureBase64, name, ownerId, role, smallPictureBase64, status, tags, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#updateSpace");
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
| **id** | **String**| id of the space | |
| **accessModeType** | **String**| Access mode | [optional] [default to NO_CHANGE] [enum: INTERNAL_ONLY, INTERNAL_EXTERNAL, NO_CHANGE] |
| **description** | **String**| description of the space | [optional] |
| **largePictureBase64** | **String**| large picture | [optional] |
| **name** | **String**| name of the space | [optional] |
| **ownerId** | **String**| ownerid of the space | [optional] |
| **role** | **String**| role | [optional] [default to NO_CHANGE] [enum: MODERATOR, AUTHOR, PARTICIPANT, READER, NO_CHANGE] |
| **smallPictureBase64** | **String**| small picture | [optional] |
| **status** | **String**| status | [optional] [default to ENABLED] [enum: ENABLED, DISABLED] |
| **tags** | [**List&lt;String&gt;**](String.md)| tags of the space | [optional] |
| **type** | **String**| type | [optional] [default to NO_CHANGE] [enum: OPEN, CLOSED, SECRET, NO_CHANGE] |

### Return type

**Object**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Space successfully updated. |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="updateSpaceReply"></a>
# **updateSpaceReply**
> SpaceReply updateSpaceReply(spaceId, topicId, replyId, attachments, complex, content, formMetaData, mentionedUsers)

Updates a space reply

Updates a space reply OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String spaceId = "spaceId_example"; // String | ID of the space
    String topicId = "topicId_example"; // String | ID of the topic
    String replyId = "replyId_example"; // String | id of the reply
    List<String> attachments = Arrays.asList(); // List<String> | the attached files
    Boolean complex = true; // Boolean | complex or not
    String content = "content_example"; // String | the content of the reply
    String formMetaData = "formMetaData_example"; // String | formMetaData of the reply
    List<String> mentionedUsers = Arrays.asList(); // List<String> | the mentioned users in the reply
    try {
      SpaceReply result = apiInstance.updateSpaceReply(spaceId, topicId, replyId, attachments, complex, content, formMetaData, mentionedUsers);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#updateSpaceReply");
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
| **spaceId** | **String**| ID of the space | |
| **topicId** | **String**| ID of the topic | |
| **replyId** | **String**| id of the reply | |
| **attachments** | [**List&lt;String&gt;**](String.md)| the attached files | [optional] |
| **complex** | **Boolean**| complex or not | [optional] |
| **content** | **String**| the content of the reply | [optional] |
| **formMetaData** | **String**| formMetaData of the reply | [optional] |
| **mentionedUsers** | [**List&lt;String&gt;**](String.md)| the mentioned users in the reply | [optional] |

### Return type

[**SpaceReply**](SpaceReply.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated space reply |  -  |
| **400** | Invalid input |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="updateSpaceTopic"></a>
# **updateSpaceTopic**
> SpaceTopic updateSpaceTopic(spaceId, topicId, attachments, complex, content, contentTags, formMetaData, mentionedUsers, subject, tags)

Updates a topic

Updates a topic OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String spaceId = "spaceId_example"; // String | ID of the space
    String topicId = "topicId_example"; // String | Id of the topic to update
    List<String> attachments = Arrays.asList(); // List<String> | the attached files
    Boolean complex = true; // Boolean | complex or not
    String content = "content_example"; // String | content of the topic
    List<String> contentTags = Arrays.asList(); // List<String> | the content tags
    String formMetaData = "formMetaData_example"; // String | formMetaData to update
    List<String> mentionedUsers = Arrays.asList(); // List<String> | the updated mentioned users
    String subject = "subject_example"; // String | the subject of the topic
    List<String> tags = Arrays.asList(); // List<String> | the tags
    try {
      SpaceTopic result = apiInstance.updateSpaceTopic(spaceId, topicId, attachments, complex, content, contentTags, formMetaData, mentionedUsers, subject, tags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#updateSpaceTopic");
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
| **spaceId** | **String**| ID of the space | |
| **topicId** | **String**| Id of the topic to update | |
| **attachments** | [**List&lt;String&gt;**](String.md)| the attached files | [optional] |
| **complex** | **Boolean**| complex or not | [optional] |
| **content** | **String**| content of the topic | [optional] |
| **contentTags** | [**List&lt;String&gt;**](String.md)| the content tags | [optional] |
| **formMetaData** | **String**| formMetaData to update | [optional] |
| **mentionedUsers** | [**List&lt;String&gt;**](String.md)| the updated mentioned users | [optional] |
| **subject** | **String**| the subject of the topic | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| the tags | [optional] |

### Return type

[**SpaceTopic**](SpaceTopic.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the updated space topic |  -  |
| **400** | Http_bad_request |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="updateTopicTags"></a>
# **updateTopicTags**
> SpaceTopic updateTopicTags(topicId, tags)

Update tags

Update the tags of a topic   OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String topicId = "topicId_example"; // String | The id of the topic
    List<String> tags = Arrays.asList(); // List<String> | The tags to update
    try {
      SpaceTopic result = apiInstance.updateTopicTags(topicId, tags);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#updateTopicTags");
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
| **topicId** | **String**| The id of the topic | |
| **tags** | [**List&lt;String&gt;**](String.md)| The tags to update | |

### Return type

[**SpaceTopic**](SpaceTopic.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | tags successfully updated |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="v2GetTopicWithReplies"></a>
# **v2GetTopicWithReplies**
> SpaceTopicWithReplies v2GetTopicWithReplies(spaceId, topicId, numberOfReplies)

Gets space replies and a topic

Gets a number of Space replies with a matching topic OauthScopes: READ_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String spaceId = "spaceId_example"; // String | Id of the topic
    String topicId = "topicId_example"; // String | ID of the topic
    BigDecimal numberOfReplies = new BigDecimal("25"); // BigDecimal | The number of replies
    try {
      SpaceTopicWithReplies result = apiInstance.v2GetTopicWithReplies(spaceId, topicId, numberOfReplies);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#v2GetTopicWithReplies");
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
| **spaceId** | **String**| Id of the topic | |
| **topicId** | **String**| ID of the topic | |
| **numberOfReplies** | **BigDecimal**| The number of replies | [optional] [default to 25] |

### Return type

[**SpaceTopicWithReplies**](SpaceTopicWithReplies.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the replies with a topic |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="v2RemoveParticipantsFromSpace"></a>
# **v2RemoveParticipantsFromSpace**
> v2RemoveParticipantsFromSpace(id, userIds)

Removes participants from a space

removes Participants from a space OauthScopes: WRITE_SPACE, MANAGE_SPACE, ORGANIZE_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String id = "id_example"; // String | The id of the space
    List<String> userIds = Arrays.asList(); // List<String> | The ids of the participants to remove 
    try {
      apiInstance.v2RemoveParticipantsFromSpace(id, userIds);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#v2RemoveParticipantsFromSpace");
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
| **id** | **String**| The id of the space | |
| **userIds** | [**List&lt;String&gt;**](String.md)| The ids of the participants to remove  | |

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
| **200** | participants successfully removed |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

<a id="v2UpdateWelcomeBoxContent"></a>
# **v2UpdateWelcomeBoxContent**
> v2UpdateWelcomeBoxContent(spaceId, content, displayWelcomeBox)

Update content of welcome box

Update content of the welcome box of a space OauthScopes: MANAGE_SPACE, WRITE_SPACE

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
    defaultClient.setBasePath("https://circuitsandbox.net/rest/v2");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    SpacesApi apiInstance = new SpacesApi(defaultClient);
    String spaceId = "spaceId_example"; // String | Id of the space
    String content = "content_example"; // String | The new content
    Boolean displayWelcomeBox = false; // Boolean | True, false, default:false
    try {
      apiInstance.v2UpdateWelcomeBoxContent(spaceId, content, displayWelcomeBox);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpacesApi#v2UpdateWelcomeBoxContent");
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
| **spaceId** | **String**| Id of the space | |
| **content** | **String**| The new content | |
| **displayWelcomeBox** | **Boolean**| True, false, default:false | [optional] [default to false] |

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
| **200** | missing documentation |  -  |
| **401** | The authentication was not successful |  -  |
| **500** | The server encountered an internal error and the operation could not be completed. |  -  |
| **503** | The server is currently unable to receive requests. |  -  |

