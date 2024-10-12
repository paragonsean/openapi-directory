# ScoreApi

All URIs are relative to *https://api.flat.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addScoreCollaborator**](ScoreApi.md#addScoreCollaborator) | **POST** /scores/{score}/collaborators | Add a new collaborator |
| [**addScoreTrack**](ScoreApi.md#addScoreTrack) | **POST** /scores/{score}/tracks | Add a new video or audio track to the score |
| [**createScore**](ScoreApi.md#createScore) | **POST** /scores | Create a new score |
| [**createScoreRevision**](ScoreApi.md#createScoreRevision) | **POST** /scores/{score}/revisions | Create a new revision |
| [**deleteScore**](ScoreApi.md#deleteScore) | **DELETE** /scores/{score} | Delete a score |
| [**deleteScoreComment**](ScoreApi.md#deleteScoreComment) | **DELETE** /scores/{score}/comments/{comment} | Delete a comment |
| [**deleteScoreTrack**](ScoreApi.md#deleteScoreTrack) | **DELETE** /scores/{score}/tracks/{track} | Remove an audio or video track linked to the score |
| [**editScore**](ScoreApi.md#editScore) | **PUT** /scores/{score} | Edit a score&#39;s metadata |
| [**forkScore**](ScoreApi.md#forkScore) | **POST** /scores/{score}/fork | Fork a score |
| [**gerUserLikes_0**](ScoreApi.md#gerUserLikes_0) | **GET** /users/{user}/likes | List liked scores |
| [**getGroupScores_0**](ScoreApi.md#getGroupScores_0) | **GET** /groups/{group}/scores | List group&#39;s scores |
| [**getScore**](ScoreApi.md#getScore) | **GET** /scores/{score} | Get a score&#39;s metadata |
| [**getScoreCollaborator**](ScoreApi.md#getScoreCollaborator) | **GET** /scores/{score}/collaborators/{collaborator} | Get a collaborator |
| [**getScoreCollaborators**](ScoreApi.md#getScoreCollaborators) | **GET** /scores/{score}/collaborators | List the collaborators |
| [**getScoreComments**](ScoreApi.md#getScoreComments) | **GET** /scores/{score}/comments | List comments |
| [**getScoreRevision**](ScoreApi.md#getScoreRevision) | **GET** /scores/{score}/revisions/{revision} | Get a score revision |
| [**getScoreRevisionData**](ScoreApi.md#getScoreRevisionData) | **GET** /scores/{score}/revisions/{revision}/{format} | Get a score revision data |
| [**getScoreRevisions**](ScoreApi.md#getScoreRevisions) | **GET** /scores/{score}/revisions | List the revisions |
| [**getScoreSubmissions**](ScoreApi.md#getScoreSubmissions) | **GET** /scores/{score}/submissions | List submissions related to the score |
| [**getScoreTrack**](ScoreApi.md#getScoreTrack) | **GET** /scores/{score}/tracks/{track} | Retrieve the details of an audio or video track linked to a score |
| [**getUserScores_0**](ScoreApi.md#getUserScores_0) | **GET** /users/{user}/scores | List user&#39;s scores |
| [**listScoreTracks**](ScoreApi.md#listScoreTracks) | **GET** /scores/{score}/tracks | List the audio or video tracks linked to a score |
| [**markScoreCommentResolved**](ScoreApi.md#markScoreCommentResolved) | **PUT** /scores/{score}/comments/{comment}/resolved | Mark the comment as resolved |
| [**markScoreCommentUnresolved**](ScoreApi.md#markScoreCommentUnresolved) | **DELETE** /scores/{score}/comments/{comment}/resolved | Mark the comment as unresolved |
| [**postScoreComment**](ScoreApi.md#postScoreComment) | **POST** /scores/{score}/comments | Post a new comment |
| [**removeScoreCollaborator**](ScoreApi.md#removeScoreCollaborator) | **DELETE** /scores/{score}/collaborators/{collaborator} | Delete a collaborator |
| [**untrashScore**](ScoreApi.md#untrashScore) | **POST** /scores/{score}/untrash | Untrash a score |
| [**updateScoreComment**](ScoreApi.md#updateScoreComment) | **PUT** /scores/{score}/comments/{comment} | Update an existing comment |
| [**updateScoreTrack**](ScoreApi.md#updateScoreTrack) | **PUT** /scores/{score}/tracks/{track} | Update an audio or video track linked to a score |


<a id="addScoreCollaborator"></a>
# **addScoreCollaborator**
> ResourceCollaborator addScoreCollaborator(score, body)

Add a new collaborator

Share a score with a single user or a group. This API call allows to add, invite and update the collaborators of a resource. - To add an existing Flat user to the resource, specify its unique identifier in the &#x60;user&#x60; property. - To invite an external user to the resource, specify its email in the &#x60;userEmail&#x60; property. - To add a Flat group to the resource, specify its unique identifier in the &#x60;group&#x60; property. - To update an existing collaborator, process the same request with different rights. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    ResourceCollaboratorCreation body = new ResourceCollaboratorCreation(); // ResourceCollaboratorCreation | 
    try {
      ResourceCollaborator result = apiInstance.addScoreCollaborator(score, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#addScoreCollaborator");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **body** | [**ResourceCollaboratorCreation**](ResourceCollaboratorCreation.md)|  | |

### Return type

[**ResourceCollaborator**](ResourceCollaborator.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The newly added collaborator metadata |  -  |
| **402** | Account overquota |  -  |
| **403** | Not granted to manage this score |  -  |
| **404** | Score not found |  -  |
| **0** | Error |  -  |

<a id="addScoreTrack"></a>
# **addScoreTrack**
> ScoreTrack addScoreTrack(score, body)

Add a new video or audio track to the score

Use this method to add new track to the score. This track can then be played on flat.io or in an embedded score. This API method support medias hosted on SoundCloud, YouTube and Vimeo. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    ScoreTrackCreation body = new ScoreTrackCreation(); // ScoreTrackCreation | 
    try {
      ScoreTrack result = apiInstance.addScoreTrack(score, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#addScoreTrack");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **body** | [**ScoreTrackCreation**](ScoreTrackCreation.md)|  | |

### Return type

[**ScoreTrack**](ScoreTrack.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Created track |  -  |
| **403** | Not granted to access to this score |  -  |
| **404** | Score not found |  -  |
| **0** | Error |  -  |

<a id="createScore"></a>
# **createScore**
> ScoreDetails createScore(body)

Create a new score

Use this API method to **create a new music score in the current User account**. You will need a MusicXML 3 (&#x60;vnd.recordare.musicxml&#x60; or &#x60;vnd.recordare.musicxml+xml&#x60;), a MIDI (&#x60;audio/midi&#x60;), Guitar Pro (GP3, GP4, GP5, GPX, GP), PowerTab, TuxGuitar, or MuseScore file to create the new Flat document.  This API call will automatically create the first revision of the document, the score can be modified by the using our web application or by uploading a new revision of this file (&#x60;POST /v2/scores/{score}/revisions/{revision}&#x60;).  The currently authenticated user will be granted owner of the file and will be able to add other collaborators (users and groups).  If no &#x60;collection&#x60; is specified, the API will create the score in the most appropriate collection. This can be the &#x60;root&#x60; collection or a different collection based on the user&#39;s settings or API authentication method. If a &#x60;collection&#x60; is specified and this one has more public privacy settings than the score (e.g. &#x60;public&#x60; vs &#x60;private&#x60; for the score), the privacy settings of the created score will be adjusted to the collection ones. You can check the adjusted privacy settings in the returned score &#x60;privacy&#x60;, and optionally adjust these settings if needed using &#x60;PUT /scores/{score}&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    ScoreCreation body = new ScoreCreation(); // ScoreCreation | 
    try {
      ScoreDetails result = apiInstance.createScore(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#createScore");
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
| **body** | [**ScoreCreation**](ScoreCreation.md)|  | |

### Return type

[**ScoreDetails**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Score created |  -  |
| **400** | Bad score creation request |  -  |
| **402** | Account overquota |  -  |
| **0** | Error |  -  |

<a id="createScoreRevision"></a>
# **createScoreRevision**
> ScoreRevision createScoreRevision(score, body)

Create a new revision

Update a score by uploading a new revision for this one. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    ScoreRevisionCreation body = new ScoreRevisionCreation(); // ScoreRevisionCreation | 
    try {
      ScoreRevision result = apiInstance.createScoreRevision(score, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#createScoreRevision");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **body** | [**ScoreRevisionCreation**](ScoreRevisionCreation.md)|  | |

### Return type

[**ScoreRevision**](ScoreRevision.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The new created revision metadata |  -  |
| **402** | Account overquota |  -  |
| **403** | Not granted to modify this score |  -  |
| **404** | Score not found |  -  |
| **0** | Error |  -  |

<a id="deleteScore"></a>
# **deleteScore**
> deleteScore(score, now)

Delete a score

This method can be used by the owner/admin (&#x60;aclAdmin&#x60; rights) of a score as well as regular collaborators.  When called by an owner/admin, it will schedule the deletion of the score, its revisions, and complete history. The score won&#39;t be accessible anymore after calling this method and the user&#39;s quota will directly be updated.  When called by a regular collaborator (&#x60;aclRead&#x60; / &#x60;aclWrite&#x60;), the score will be unshared (i.e. removed from the account &amp; own collections). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    Boolean now = false; // Boolean | If `true`, the score deletion will be scheduled to be done ASAP
    try {
      apiInstance.deleteScore(score, now);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#deleteScore");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **now** | **Boolean**| If &#x60;true&#x60;, the score deletion will be scheduled to be done ASAP | [optional] [default to false] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The score has been removed |  -  |
| **403** | Not granted to manage this score |  -  |
| **404** | Score not found |  -  |
| **0** | Error |  -  |

<a id="deleteScoreComment"></a>
# **deleteScoreComment**
> deleteScoreComment(score, comment, sharingKey)

Delete a comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    String comment = "comment_example"; // String | Unique identifier of a sheet music comment 
    String sharingKey = "sharingKey_example"; // String | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
    try {
      apiInstance.deleteScoreComment(score, comment, sharingKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#deleteScoreComment");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **comment** | **String**| Unique identifier of a sheet music comment  | |
| **sharingKey** | **String**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The comment has been deleted |  -  |
| **403** | Not granted to access to this score or not the original comment creator |  -  |
| **404** | Score or comment not found |  -  |
| **0** | Error |  -  |

<a id="deleteScoreTrack"></a>
# **deleteScoreTrack**
> deleteScoreTrack(score, track)

Remove an audio or video track linked to the score

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    String track = "track_example"; // String | Unique identifier of a score audio track 
    try {
      apiInstance.deleteScoreTrack(score, track);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#deleteScoreTrack");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **track** | **String**| Unique identifier of a score audio track  | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Track removed |  -  |
| **403** | Not granted to access to this score |  -  |
| **404** | Score or Track not found |  -  |
| **0** | Error |  -  |

<a id="editScore"></a>
# **editScore**
> ScoreDetails editScore(score, body)

Edit a score&#39;s metadata

This API method allows you to change the metadata of a score document (e.g. its &#x60;title&#x60; or &#x60;privacy&#x60;), all the properties are optional.  To edit the file itself, create a new revision using the appropriate method (&#x60;POST /v2/scores/{score}/revisions/{revision}&#x60;).  When editing the &#x60;title&#x60;, &#x60;subtitle&#x60;, &#x60;composer&#x60;, &#x60;lyricist&#x60;, &#x60;arranger&#x60; or &#x60;licenseText&#x60;, the metadatas will be instantly be updated, and a real-time action will be pushed to update the document lazily. This pending document modification will be automatically be saved as a new version by either a connected client or our internal versioning service. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    ScoreModification body = new ScoreModification(); // ScoreModification | 
    try {
      ScoreDetails result = apiInstance.editScore(score, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#editScore");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **body** | [**ScoreModification**](ScoreModification.md)|  | [optional] |

### Return type

[**ScoreDetails**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Score details |  -  |
| **402** | Account overquota |  -  |
| **403** | Not granted to access to this score |  -  |
| **404** | Score not found |  -  |
| **0** | Error |  -  |

<a id="forkScore"></a>
# **forkScore**
> ScoreDetails forkScore(score, body, sharingKey)

Fork a score

This API call will make a copy of the last revision of the specified score and create a new score. The copy of the score will have a privacy set to &#x60;private&#x60;.  When using a [Flat for Education](https://flat.io/edu) account, the inline and contextualized comments will be accessible in the child document. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    ScoreFork body = new ScoreFork(); // ScoreFork | 
    String sharingKey = "sharingKey_example"; // String | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
    try {
      ScoreDetails result = apiInstance.forkScore(score, body, sharingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#forkScore");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **body** | [**ScoreFork**](ScoreFork.md)|  | |
| **sharingKey** | **String**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] |

### Return type

[**ScoreDetails**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Score details |  -  |
| **402** | Account overquota |  -  |
| **403** | Not granted to access to this score |  -  |
| **404** | Score not found |  -  |
| **0** | Error |  -  |

<a id="gerUserLikes_0"></a>
# **gerUserLikes_0**
> List&lt;ScoreDetails&gt; gerUserLikes_0(user, ids)

List liked scores

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String user = "user_example"; // String | Unique identifier of a Flat user. If you authenticated, you can use `me` to refer to the current user. 
    Boolean ids = true; // Boolean | Return only the identifiers of the scores
    try {
      List<ScoreDetails> result = apiInstance.gerUserLikes_0(user, ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#gerUserLikes_0");
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
| **user** | **String**| Unique identifier of a Flat user. If you authenticated, you can use &#x60;me&#x60; to refer to the current user.  | |
| **ids** | **Boolean**| Return only the identifiers of the scores | [optional] |

### Return type

[**List&lt;ScoreDetails&gt;**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of liked scores |  -  |
| **0** | Error |  -  |

<a id="getGroupScores_0"></a>
# **getGroupScores_0**
> List&lt;ScoreDetails&gt; getGroupScores_0(group, parent)

List group&#39;s scores

Get the list of scores shared with a group. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String group = "group_example"; // String | Unique identifier of a Flat group 
    String parent = "parent_example"; // String | Filter the score forked from the score id `parent`
    try {
      List<ScoreDetails> result = apiInstance.getGroupScores_0(group, parent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#getGroupScores_0");
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
| **group** | **String**| Unique identifier of a Flat group  | |
| **parent** | **String**| Filter the score forked from the score id &#x60;parent&#x60; | [optional] |

### Return type

[**List&lt;ScoreDetails&gt;**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The group&#39;s scores |  -  |
| **0** | Error |  -  |

<a id="getScore"></a>
# **getScore**
> ScoreDetails getScore(score, sharingKey)

Get a score&#39;s metadata

Get the details of a score identified by the &#x60;score&#x60; parameter in the URL. The currently authenticated user must have at least a read access to the document to use this API call. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    String sharingKey = "sharingKey_example"; // String | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
    try {
      ScoreDetails result = apiInstance.getScore(score, sharingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#getScore");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **sharingKey** | **String**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] |

### Return type

[**ScoreDetails**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Score details |  -  |
| **402** | Account overquota and this document is out of the granted quota |  -  |
| **403** | Not granted to access to this score |  -  |
| **404** | Score not found |  -  |
| **0** | Error |  -  |

<a id="getScoreCollaborator"></a>
# **getScoreCollaborator**
> ResourceCollaborator getScoreCollaborator(score, collaborator, sharingKey)

Get a collaborator

Get the information about a collaborator (User or Group). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    String collaborator = "collaborator_example"; // String | Unique identifier of a **collaborator permission**, or unique identifier of a **User**, or unique identifier of a **Group** 
    String sharingKey = "sharingKey_example"; // String | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
    try {
      ResourceCollaborator result = apiInstance.getScoreCollaborator(score, collaborator, sharingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#getScoreCollaborator");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **collaborator** | **String**| Unique identifier of a **collaborator permission**, or unique identifier of a **User**, or unique identifier of a **Group**  | |
| **sharingKey** | **String**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] |

### Return type

[**ResourceCollaborator**](ResourceCollaborator.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collaborator information |  -  |
| **402** | Account overquota |  -  |
| **403** | Not granted to access to this score |  -  |
| **404** | Score or collaborator not found |  -  |
| **0** | Error |  -  |

<a id="getScoreCollaborators"></a>
# **getScoreCollaborators**
> List&lt;ResourceCollaborator&gt; getScoreCollaborators(score, sharingKey)

List the collaborators

This API call will list the different collaborators of a score and their rights on the document. The returned list will at least contain the owner of the document.  Collaborators can be a single user (the object &#x60;user&#x60; will be populated) or a group (the object &#x60;group&#x60; will be populated). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    String sharingKey = "sharingKey_example"; // String | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
    try {
      List<ResourceCollaborator> result = apiInstance.getScoreCollaborators(score, sharingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#getScoreCollaborators");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **sharingKey** | **String**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] |

### Return type

[**List&lt;ResourceCollaborator&gt;**](ResourceCollaborator.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of collaborators |  -  |
| **402** | Account overquota |  -  |
| **403** | Not granted to access to this score |  -  |
| **404** | Score not found |  -  |
| **0** | Error |  -  |

<a id="getScoreComments"></a>
# **getScoreComments**
> List&lt;ScoreComment&gt; getScoreComments(score, sharingKey, type, sort, direction)

List comments

This method lists the different comments added on a music score (documents and inline) sorted by their post dates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    String sharingKey = "sharingKey_example"; // String | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
    String type = "document"; // String | Filter the comments by type
    String sort = "date"; // String | Sort
    String direction = "asc"; // String | Sort direction
    try {
      List<ScoreComment> result = apiInstance.getScoreComments(score, sharingKey, type, sort, direction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#getScoreComments");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **sharingKey** | **String**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] |
| **type** | **String**| Filter the comments by type | [optional] [enum: document, inline] |
| **sort** | **String**| Sort | [optional] [enum: date] |
| **direction** | **String**| Sort direction | [optional] [enum: asc, desc] |

### Return type

[**List&lt;ScoreComment&gt;**](ScoreComment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The comments of the score |  -  |
| **402** | Account overquota |  -  |
| **403** | Not granted to access to this score |  -  |
| **404** | Score not found |  -  |
| **0** | Error |  -  |

<a id="getScoreRevision"></a>
# **getScoreRevision**
> ScoreRevision getScoreRevision(score, revision, sharingKey)

Get a score revision

When creating a score or saving a new version of a score, a revision is created in our storage. This method allows you to get a specific revision metadata. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    String revision = "revision_example"; // String | Unique identifier of a score revision. You can use `last` to fetch the information related to the last version created. 
    String sharingKey = "sharingKey_example"; // String | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
    try {
      ScoreRevision result = apiInstance.getScoreRevision(score, revision, sharingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#getScoreRevision");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **revision** | **String**| Unique identifier of a score revision. You can use &#x60;last&#x60; to fetch the information related to the last version created.  | |
| **sharingKey** | **String**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] |

### Return type

[**ScoreRevision**](ScoreRevision.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Revision metadata |  -  |
| **402** | Account overquota |  -  |
| **403** | Not granted to access to this score |  -  |
| **404** | Score not found |  -  |
| **0** | Error |  -  |

<a id="getScoreRevisionData"></a>
# **getScoreRevisionData**
> File getScoreRevisionData(score, revision, format, sharingKey, parts, onlyCached, url)

Get a score revision data

Retrieve the file corresponding to a score revision (the following formats are available): Flat JSON/Adagio JSON &#x60;json&#x60;, MusicXML &#x60;mxl&#x60;/&#x60;xml&#x60;, MP3 &#x60;mp3&#x60;, WAV &#x60;wav&#x60;, MIDI &#x60;midi&#x60;, a tumbnail of the first page &#x60;thumbnail.png&#x60; or auto sync points &#x60;synchronizationPoints&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    String revision = "revision_example"; // String | Unique identifier of a score revision. You can use `last` to fetch the information related to the last version created. 
    String format = "json"; // String | The format of the file you will retrieve
    String sharingKey = "sharingKey_example"; // String | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
    String parts = "parts_example"; // String | An optional a set of parts uuid to be exported. This parameter must be composed of parts uuids separated by commas. For example \"59df645f-bb1c-f1b4-b573-d2afc4491f94,34ef645f-1aef-f3bc-1564-34cca4492b87\". 
    Boolean onlyCached = true; // Boolean | Only return files already generated and cached in Flat's production cache. If the file is not availabe, a 404 will be returned 
    Boolean url = true; // Boolean | Returns a json with the `url` in it instead of redirecting 
    try {
      File result = apiInstance.getScoreRevisionData(score, revision, format, sharingKey, parts, onlyCached, url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#getScoreRevisionData");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **revision** | **String**| Unique identifier of a score revision. You can use &#x60;last&#x60; to fetch the information related to the last version created.  | |
| **format** | **String**| The format of the file you will retrieve | [enum: json, mxl, xml, mp3, wav, midi, thumbnail.png, synchronizationPoints] |
| **sharingKey** | **String**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] |
| **parts** | **String**| An optional a set of parts uuid to be exported. This parameter must be composed of parts uuids separated by commas. For example \&quot;59df645f-bb1c-f1b4-b573-d2afc4491f94,34ef645f-1aef-f3bc-1564-34cca4492b87\&quot;.  | [optional] |
| **onlyCached** | **Boolean**| Only return files already generated and cached in Flat&#39;s production cache. If the file is not availabe, a 404 will be returned  | [optional] |
| **url** | **Boolean**| Returns a json with the &#x60;url&#x60; in it instead of redirecting  | [optional] |

### Return type

[**File**](File.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.recordare.musicxml, application/vnd.recordare.musicxml+xml, audio/midi, audio/mp3, audio/wav, image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Revision data |  -  |
| **402** | Account overquota |  -  |
| **403** | Not granted to access to this score |  -  |
| **404** | Score or associated file not found |  -  |
| **0** | Error |  -  |

<a id="getScoreRevisions"></a>
# **getScoreRevisions**
> List&lt;ScoreRevision&gt; getScoreRevisions(score, sharingKey)

List the revisions

When creating a score or saving a new version of a score, a revision is created in our storage. This method allows you to list all of them, sorted by last modification.  Depending the plan of the account, this list can be trunked to the few last revisions. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    String sharingKey = "sharingKey_example"; // String | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
    try {
      List<ScoreRevision> result = apiInstance.getScoreRevisions(score, sharingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#getScoreRevisions");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **sharingKey** | **String**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] |

### Return type

[**List&lt;ScoreRevision&gt;**](ScoreRevision.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of revisions |  -  |
| **402** | Account overquota |  -  |
| **403** | Not granted to access to this score |  -  |
| **404** | Score not found |  -  |
| **0** | Error |  -  |

<a id="getScoreSubmissions"></a>
# **getScoreSubmissions**
> List&lt;AssignmentSubmission&gt; getScoreSubmissions(score)

List submissions related to the score

This API call will list the different assignments submissions where the score is attached. This method can be used by anyone that are part of the organization and have at least read access to the document. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    try {
      List<AssignmentSubmission> result = apiInstance.getScoreSubmissions(score);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#getScoreSubmissions");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |

### Return type

[**List&lt;AssignmentSubmission&gt;**](AssignmentSubmission.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of submissions |  -  |
| **0** | Error |  -  |

<a id="getScoreTrack"></a>
# **getScoreTrack**
> ScoreTrack getScoreTrack(score, track, sharingKey)

Retrieve the details of an audio or video track linked to a score

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    String track = "track_example"; // String | Unique identifier of a score audio track 
    String sharingKey = "sharingKey_example"; // String | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
    try {
      ScoreTrack result = apiInstance.getScoreTrack(score, track, sharingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#getScoreTrack");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **track** | **String**| Unique identifier of a score audio track  | |
| **sharingKey** | **String**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] |

### Return type

[**ScoreTrack**](ScoreTrack.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Track details |  -  |
| **403** | Not granted to access to this score |  -  |
| **404** | Score or Track not found |  -  |
| **0** | Error |  -  |

<a id="getUserScores_0"></a>
# **getUserScores_0**
> List&lt;ScoreDetails&gt; getUserScores_0(user, parent)

List user&#39;s scores

Get the list of public scores owned by a User.  **DEPRECATED**: Please note that the current behavior will be deprecrated on **2019-01-01**. This method will no longer list private and shared scores, but only public scores of a Flat account. If you want to access to private scores, please use the [Collections API](#tag/Collection) instead. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String user = "user_example"; // String | Unique identifier of a Flat user. If you authenticated, you can use `me` to refer to the current user. 
    String parent = "parent_example"; // String | Filter the score forked from the score id `parent`
    try {
      List<ScoreDetails> result = apiInstance.getUserScores_0(user, parent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#getUserScores_0");
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
| **user** | **String**| Unique identifier of a Flat user. If you authenticated, you can use &#x60;me&#x60; to refer to the current user.  | |
| **parent** | **String**| Filter the score forked from the score id &#x60;parent&#x60; | [optional] |

### Return type

[**List&lt;ScoreDetails&gt;**](ScoreDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The user scores |  -  |
| **0** | Error |  -  |

<a id="listScoreTracks"></a>
# **listScoreTracks**
> List&lt;ScoreTrack&gt; listScoreTracks(score, sharingKey, assignment, listAutoTrack)

List the audio or video tracks linked to a score

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    String sharingKey = "sharingKey_example"; // String | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
    String assignment = "assignment_example"; // String | An assignment id with which all the tracks returned will be related to 
    Boolean listAutoTrack = true; // Boolean | If true, and if available, return last automatically synchronized Flat's mp3 export as an additional track 
    try {
      List<ScoreTrack> result = apiInstance.listScoreTracks(score, sharingKey, assignment, listAutoTrack);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#listScoreTracks");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **sharingKey** | **String**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] |
| **assignment** | **String**| An assignment id with which all the tracks returned will be related to  | [optional] |
| **listAutoTrack** | **Boolean**| If true, and if available, return last automatically synchronized Flat&#39;s mp3 export as an additional track  | [optional] |

### Return type

[**List&lt;ScoreTrack&gt;**](ScoreTrack.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of tracks |  -  |
| **403** | Not granted to access to this score |  -  |
| **404** | Score not found |  -  |
| **0** | Error |  -  |

<a id="markScoreCommentResolved"></a>
# **markScoreCommentResolved**
> markScoreCommentResolved(score, comment, sharingKey)

Mark the comment as resolved

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    String comment = "comment_example"; // String | Unique identifier of a sheet music comment 
    String sharingKey = "sharingKey_example"; // String | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
    try {
      apiInstance.markScoreCommentResolved(score, comment, sharingKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#markScoreCommentResolved");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **comment** | **String**| Unique identifier of a sheet music comment  | |
| **sharingKey** | **String**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The comment has been marked as resolved |  -  |
| **403** | Not granted to mark this comment as resolved |  -  |
| **404** | Score or comment not found |  -  |
| **0** | Error |  -  |

<a id="markScoreCommentUnresolved"></a>
# **markScoreCommentUnresolved**
> markScoreCommentUnresolved(score, comment, sharingKey)

Mark the comment as unresolved

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    String comment = "comment_example"; // String | Unique identifier of a sheet music comment 
    String sharingKey = "sharingKey_example"; // String | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
    try {
      apiInstance.markScoreCommentUnresolved(score, comment, sharingKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#markScoreCommentUnresolved");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **comment** | **String**| Unique identifier of a sheet music comment  | |
| **sharingKey** | **String**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The comment has been unmarked as resolved |  -  |
| **403** | Not granted to unmark this comment as resolved |  -  |
| **404** | Score or comment not found |  -  |
| **0** | Error |  -  |

<a id="postScoreComment"></a>
# **postScoreComment**
> ScoreComment postScoreComment(score, body, sharingKey)

Post a new comment

Post a document or a contextualized comment on a document.  Please note that this method includes an anti-spam system for public scores. We don&#39;t guarantee that your comments will be accepted and displayed to end-user. Comments are be blocked by returning a &#x60;403&#x60; HTTP error and hidden from other users when the &#x60;spam&#x60; property is &#x60;true&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    ScoreCommentCreation body = new ScoreCommentCreation(); // ScoreCommentCreation | 
    String sharingKey = "sharingKey_example"; // String | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
    try {
      ScoreComment result = apiInstance.postScoreComment(score, body, sharingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#postScoreComment");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **body** | [**ScoreCommentCreation**](ScoreCommentCreation.md)|  | |
| **sharingKey** | **String**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] |

### Return type

[**ScoreComment**](ScoreComment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The new comment |  -  |
| **402** | Account overquota |  -  |
| **403** | Not granted to access to this score, to post a comment, or your API call triggered our spam filter. |  -  |
| **404** | Score not found |  -  |
| **0** | Error |  -  |

<a id="removeScoreCollaborator"></a>
# **removeScoreCollaborator**
> removeScoreCollaborator(score, collaborator)

Delete a collaborator

Remove the specified collaborator from the score 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    String collaborator = "collaborator_example"; // String | Unique identifier of a **collaborator permission**, or unique identifier of a **User**, or unique identifier of a **Group** 
    try {
      apiInstance.removeScoreCollaborator(score, collaborator);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#removeScoreCollaborator");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **collaborator** | **String**| Unique identifier of a **collaborator permission**, or unique identifier of a **User**, or unique identifier of a **Group**  | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The collaborator has been removed |  -  |
| **403** | Not granted to manage this score |  -  |
| **404** | Score or collaborator not found |  -  |
| **0** | Error |  -  |

<a id="untrashScore"></a>
# **untrashScore**
> untrashScore(score)

Untrash a score

This method will remove the score from the &#x60;trash&#x60; collection and from the deletion queue, and add it back to the original collections. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    try {
      apiInstance.untrashScore(score);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#untrashScore");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The score has been untrashed |  -  |
| **403** | Not granted to manage this score |  -  |
| **404** | Score not found |  -  |
| **0** | Error |  -  |

<a id="updateScoreComment"></a>
# **updateScoreComment**
> ScoreComment updateScoreComment(score, comment, body, sharingKey)

Update an existing comment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    String comment = "comment_example"; // String | Unique identifier of a sheet music comment 
    ScoreCommentUpdate body = new ScoreCommentUpdate(); // ScoreCommentUpdate | 
    String sharingKey = "sharingKey_example"; // String | This sharing key must be specified to access to a score or collection with a `privacy` mode set to `privateLink` and the current user is not a collaborator of the document. 
    try {
      ScoreComment result = apiInstance.updateScoreComment(score, comment, body, sharingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#updateScoreComment");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **comment** | **String**| Unique identifier of a sheet music comment  | |
| **body** | [**ScoreCommentUpdate**](ScoreCommentUpdate.md)|  | |
| **sharingKey** | **String**| This sharing key must be specified to access to a score or collection with a &#x60;privacy&#x60; mode set to &#x60;privateLink&#x60; and the current user is not a collaborator of the document.  | [optional] |

### Return type

[**ScoreComment**](ScoreComment.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The edited comment |  -  |
| **402** | Account overquota |  -  |
| **403** | Not granted to access to this score or not the original comment creator |  -  |
| **404** | Score not found |  -  |
| **0** | Error |  -  |

<a id="updateScoreTrack"></a>
# **updateScoreTrack**
> ScoreTrack updateScoreTrack(score, track, body)

Update an audio or video track linked to a score

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScoreApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.flat.io/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ScoreApi apiInstance = new ScoreApi(defaultClient);
    String score = "score_example"; // String | Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. `ScoreDetails.id`) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with `drive-` (e.g. `drive-0B000000000`). 
    String track = "track_example"; // String | Unique identifier of a score audio track 
    ScoreTrackUpdate body = new ScoreTrackUpdate(); // ScoreTrackUpdate | 
    try {
      ScoreTrack result = apiInstance.updateScoreTrack(score, track, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScoreApi#updateScoreTrack");
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
| **score** | **String**| Unique identifier of the score document. This can be a Flat Score unique identifier (i.e. &#x60;ScoreDetails.id&#x60;) or, if the score is also a Google Drive file, the Drive file unique identifier prefixed with &#x60;drive-&#x60; (e.g. &#x60;drive-0B000000000&#x60;).  | |
| **track** | **String**| Unique identifier of a score audio track  | |
| **body** | [**ScoreTrackUpdate**](ScoreTrackUpdate.md)|  | |

### Return type

[**ScoreTrack**](ScoreTrack.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated track |  -  |
| **403** | Not granted to access to this score |  -  |
| **404** | Score or Track not found |  -  |
| **0** | Error |  -  |

