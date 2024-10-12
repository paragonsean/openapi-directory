# RestApiVersion2.SpacesApi

All URIs are relative to *https://circuitsandbox.net/rest/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addParticipantsToSpace**](SpacesApi.md#addParticipantsToSpace) | **POST** /spaces/{id}/participant | Add Participant to Space
[**addRecentSpaceSearch**](SpacesApi.md#addRecentSpaceSearch) | **PUT** /spaces/search/add/recent | Add recent search 
[**assignLabels**](SpacesApi.md#assignLabels) | **POST** /spaces/{id}/labels/assign | Assign labels
[**cancelSpaceSearch**](SpacesApi.md#cancelSpaceSearch) | **PUT** /spaces/search/cancel/{searchId} | Cancels a space search of a client.
[**createReply**](SpacesApi.md#createReply) | **POST** /spaces/{spaceId}/topic/{topicId}/reply | creates a reply to a topic
[**createSpace**](SpacesApi.md#createSpace) | **POST** /spaces/create | Create a space
[**createSpaceTopic**](SpacesApi.md#createSpaceTopic) | **POST** /spaces/{spaceId}/topic | creates a new space topic
[**deleteSpace**](SpacesApi.md#deleteSpace) | **DELETE** /spaces/{id} | Delete a space
[**deleteSpaceItem**](SpacesApi.md#deleteSpaceItem) | **DELETE** /spaces/item/{itemId} | deletes a space item
[**denySpaceAcces**](SpacesApi.md#denySpaceAcces) | **POST** /spaces/{spaceId}/participant/{participantId}/deny | Deny access for a space
[**existsSpaceName**](SpacesApi.md#existsSpaceName) | **GET** /spaces/exists/{name} | Space name exists
[**flagSpaceItem**](SpacesApi.md#flagSpaceItem) | **PUT** /spaces/flag/{itemId} | flag a space item
[**getDirectory**](SpacesApi.md#getDirectory) | **GET** /spaces/directory | Get the directory
[**getFlaggedItems**](SpacesApi.md#getFlaggedItems) | **GET** /spaces/flagged | Get flagged items
[**getLikes**](SpacesApi.md#getLikes) | **GET** /spaces/likes/{itemId} | Get the likes of an item
[**getParticipantsImportData**](SpacesApi.md#getParticipantsImportData) | **GET** /spaces/{spaceId}/participant/import/ | missing documentation
[**getPendingParticipants**](SpacesApi.md#getPendingParticipants) | **GET** /spaces/{id}/participants/pending | Get the pending participants of a space
[**getPinnedTopics**](SpacesApi.md#getPinnedTopics) | **GET** /spaces/{id}/pinnedTopics | Retrieve pinned topics
[**getRecentSearches**](SpacesApi.md#getRecentSearches) | **GET** /spaces/search/recent | Retrieve recent space searches
[**getSpaceParticipants**](SpacesApi.md#getSpaceParticipants) | **GET** /spaces/{id}/participants | Get the participants of a space
[**getSpaceReplies**](SpacesApi.md#getSpaceReplies) | **GET** /spaces/{spaceId}/topic/{topicId}/reply | Gets space replies
[**getSpaceTopics**](SpacesApi.md#getSpaceTopics) | **GET** /spaces/{spaceId}/topics | Gets space topics
[**getSpaces**](SpacesApi.md#getSpaces) | **GET** /spaces | Get the spaces
[**getSpacesByIds**](SpacesApi.md#getSpacesByIds) | **GET** /spaces/ids | Get the spaces by their ids
[**grantSpaceAcces**](SpacesApi.md#grantSpaceAcces) | **POST** /spaces/{spaceId}/participant/{participantId}/grant | grant access for a space
[**joinSpace**](SpacesApi.md#joinSpace) | **POST** /spaces/{id}/join | Join a space
[**leaveSpace**](SpacesApi.md#leaveSpace) | **POST** /spaces/{id}/leave | Leave a space
[**likeSpaceItem**](SpacesApi.md#likeSpaceItem) | **PUT** /spaces/like/{itemId} | Like a space item
[**pinTopic**](SpacesApi.md#pinTopic) | **PUT** /spaces/{topicId}/pin | Pin a topic
[**requestSpaceAcces**](SpacesApi.md#requestSpaceAcces) | **POST** /spaces/{spaceId}/participant/request | request access for a space
[**searchParticipantsToAdd**](SpacesApi.md#searchParticipantsToAdd) | **GET** /spaces/{id}/searchParticipantsToAdd | Finds participants to add to add to a space 
[**searchSpaceParticipants**](SpacesApi.md#searchSpaceParticipants) | **GET** /spaces/{id}/searchSpaceParticipants | Get the participants of a space
[**startBasicSpacesSearch**](SpacesApi.md#startBasicSpacesSearch) | **GET** /spaces/search/startBasic | starts a basic search in spaces
[**startDetailedSpaceSearch**](SpacesApi.md#startDetailedSpaceSearch) | **GET** /spaces/search/startDetailed | starts a detailed search in a space
[**unassignLabels**](SpacesApi.md#unassignLabels) | **DELETE** /spaces/{id}/labels/unassign | Unassign labels
[**unflagSpaceItem**](SpacesApi.md#unflagSpaceItem) | **PUT** /spaces/unflag/{itemId} | Unflag a space item
[**unlikeSpaceItem**](SpacesApi.md#unlikeSpaceItem) | **PUT** /spaces/unlike/{itemId} | Unlike a space item
[**unpinTopic**](SpacesApi.md#unpinTopic) | **PUT** /spaces/{topicId}/unpin | Unpin a topic
[**updateParticipantInSpace**](SpacesApi.md#updateParticipantInSpace) | **PUT** /spaces/{spaceId}/participant | Update participant
[**updateReadTimestamp**](SpacesApi.md#updateReadTimestamp) | **PUT** /spaces/{id}/updateTimestamp | Update read timestamp
[**updateSpace**](SpacesApi.md#updateSpace) | **PUT** /spaces/{id} | Update a space
[**updateSpaceReply**](SpacesApi.md#updateSpaceReply) | **PUT** /spaces/{spaceId}/topic/{topicId}/reply/{replyId} | Updates a space reply
[**updateSpaceTopic**](SpacesApi.md#updateSpaceTopic) | **PUT** /spaces/{spaceId}/topic/{topicId} | Updates a topic
[**updateTopicTags**](SpacesApi.md#updateTopicTags) | **PUT** /spaces/topic/{topicId}/updateTags | Update tags
[**v2GetTopicWithReplies**](SpacesApi.md#v2GetTopicWithReplies) | **GET** /spaces/{spaceId}/topic/{topicId} | Gets space replies and a topic
[**v2RemoveParticipantsFromSpace**](SpacesApi.md#v2RemoveParticipantsFromSpace) | **POST** /spaces/{id}/participant/remove | Removes participants from a space
[**v2UpdateWelcomeBoxContent**](SpacesApi.md#v2UpdateWelcomeBoxContent) | **PUT** /spaces/{spaceId}/welcomebox/{content} | Update content of welcome box



## addParticipantsToSpace

> [Object] addParticipantsToSpace(id, role, userId)

Add Participant to Space

Add a participant to a space OauthScopes: WRITE_SPACE, MANAGE_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let id = "id_example"; // String | The id of the space
let role = "'DEFAULT'"; // String | The name of the role of the participant
let userId = ["null"]; // [String] | The user id of the participant
apiInstance.addParticipantsToSpace(id, role, userId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The id of the space | 
 **role** | **String**| The name of the role of the participant | [default to &#39;DEFAULT&#39;]
 **userId** | [**[String]**](String.md)| The user id of the participant | 

### Return type

**[Object]**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## addRecentSpaceSearch

> addRecentSpaceSearch(scope, searchTerm, opts)

Add recent search 

Add recent search of a client to search controller. OauthScopes: WRITE_SPACE, MANAGE_SPACE, ORGANIZE_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let scope = "scope_example"; // String | The scope of the search.
let searchTerm = "searchTerm_example"; // String | The term to search for.
let opts = {
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | The end time.
  'startTime': new Date("2013-10-20T19:20:30+01:00") // Date | The start time.
};
apiInstance.addRecentSpaceSearch(scope, searchTerm, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **String**| The scope of the search. | 
 **searchTerm** | **String**| The term to search for. | 
 **endTime** | **Date**| The end time. | [optional] 
 **startTime** | **Date**| The start time. | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## assignLabels

> [LabelIds] assignLabels(id, labels)

Assign labels

Assign labels to space OauthScopes: WRITE_SPACE, ORGANIZE_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let id = "id_example"; // String | The id of the space.
let labels = ["null"]; // [String] | The labels to assign to the space
apiInstance.assignLabels(id, labels, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The id of the space. | 
 **labels** | [**[String]**](String.md)| The labels to assign to the space | 

### Return type

[**[LabelIds]**](LabelIds.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## cancelSpaceSearch

> cancelSpaceSearch(searchId)

Cancels a space search of a client.

Cancels a space search of a client. OauthScopes: WRITE_SPACE, MANAGE_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let searchId = "searchId_example"; // String | The id of the search to cancel
apiInstance.cancelSpaceSearch(searchId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchId** | **String**| The id of the search to cancel | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createReply

> SpaceReply createReply(spaceId, topicId, opts)

creates a reply to a topic

creates a reply to a topic OauthScopes: WRITE_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let spaceId = "spaceId_example"; // String | ID of the space
let topicId = "topicId_example"; // String | ID of the topic
let opts = {
  'attachments': ["null"], // [String] | the attached files
  'complex': true, // Boolean | complex or not
  'content': "content_example", // String | Content of the reply
  'formMetaData': "formMetaData_example", // String | formMetaData used in the reply
  'mentionedUser': "mentionedUser_example" // String | the user mentioned in the reply
};
apiInstance.createReply(spaceId, topicId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spaceId** | **String**| ID of the space | 
 **topicId** | **String**| ID of the topic | 
 **attachments** | [**[String]**](String.md)| the attached files | [optional] 
 **complex** | **Boolean**| complex or not | [optional] 
 **content** | **String**| Content of the reply | [optional] 
 **formMetaData** | **String**| formMetaData used in the reply | [optional] 
 **mentionedUser** | **String**| the user mentioned in the reply | [optional] 

### Return type

[**SpaceReply**](SpaceReply.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## createSpace

> Object createSpace(accessModeType, name, role, status, type, opts)

Create a space

Create a space OauthScopes: WRITE_SPACE, MANAGE_SPACE, CREATE_SPACE_CONTENT

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let accessModeType = "'INTERNAL_ONLY'"; // String | Access mode
let name = "name_example"; // String | name of the space
let role = "'AUTHOR'"; // String | role
let status = "'ENABLED'"; // String | status
let type = "'SECRET'"; // String | type
let opts = {
  'description': "description_example", // String | description of the space
  'largePictureBase64': "largePictureBase64_example", // String | large picture
  'smallPictureBase64': "smallPictureBase64_example", // String | small picture
  'tags': ["null"] // [String] | tags of the space
};
apiInstance.createSpace(accessModeType, name, role, status, type, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessModeType** | **String**| Access mode | [default to &#39;INTERNAL_ONLY&#39;]
 **name** | **String**| name of the space | 
 **role** | **String**| role | [default to &#39;AUTHOR&#39;]
 **status** | **String**| status | [default to &#39;ENABLED&#39;]
 **type** | **String**| type | [default to &#39;SECRET&#39;]
 **description** | **String**| description of the space | [optional] 
 **largePictureBase64** | **String**| large picture | [optional] 
 **smallPictureBase64** | **String**| small picture | [optional] 
 **tags** | [**[String]**](String.md)| tags of the space | [optional] 

### Return type

**Object**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## createSpaceTopic

> SpaceTopic createSpaceTopic(spaceId, subject, opts)

creates a new space topic

creates a new space topic OauthScopes: WRITE_SPACE, MANAGE_SPACE, CREATE_SPACE_CONTENT

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let spaceId = "spaceId_example"; // String | The ID of the space
let subject = "subject_example"; // String | The subject of the topic
let opts = {
  'attachments': ["null"], // [String] | the attached files
  'complex': true, // Boolean | complex or not
  'content': "content_example", // String | The content of this topic
  'contentTags': ["null"], // [String] | the content tags
  'formMetaData': "formMetaData_example", // String | The formMetaData
  'mentionedUser': "mentionedUser_example", // String | A list of mentioned users
  'tags': ["null"] // [String] | the tags
};
apiInstance.createSpaceTopic(spaceId, subject, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spaceId** | **String**| The ID of the space | 
 **subject** | **String**| The subject of the topic | 
 **attachments** | [**[String]**](String.md)| the attached files | [optional] 
 **complex** | **Boolean**| complex or not | [optional] 
 **content** | **String**| The content of this topic | [optional] 
 **contentTags** | [**[String]**](String.md)| the content tags | [optional] 
 **formMetaData** | **String**| The formMetaData | [optional] 
 **mentionedUser** | **String**| A list of mentioned users | [optional] 
 **tags** | [**[String]**](String.md)| the tags | [optional] 

### Return type

[**SpaceTopic**](SpaceTopic.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## deleteSpace

> deleteSpace(id)

Delete a space

Delete a space OauthScopes: WRITE_SPACE, MANAGE_SPACE, DELETE_SPACE_CONTENT

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let id = "id_example"; // String | id of the space
apiInstance.deleteSpace(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| id of the space | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSpaceItem

> deleteSpaceItem(itemId)

deletes a space item

deletes a space item OauthScopes: WRITE_SPACE, DELETE_SPACE_CONTENT

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let itemId = "itemId_example"; // String | the id of the spaceItem
apiInstance.deleteSpaceItem(itemId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemId** | **String**| the id of the spaceItem | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## denySpaceAcces

> denySpaceAcces(spaceId, participantId, opts)

Deny access for a space

Deny access for a space OauthScopes: WRITE_SPACE, MANAGE_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let spaceId = "spaceId_example"; // String | Id of the space
let participantId = "participantId_example"; // String | Id of the participant
let opts = {
  'reason': "reason_example" // String | Reason why the request has been denied
};
apiInstance.denySpaceAcces(spaceId, participantId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spaceId** | **String**| Id of the space | 
 **participantId** | **String**| Id of the participant | 
 **reason** | **String**| Reason why the request has been denied | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## existsSpaceName

> existsSpaceName(name)

Space name exists

Find out if a space name already exists for non-secret spaces. OauthScopes: READ_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let name = "name_example"; // String | The name to check for existence.
apiInstance.existsSpaceName(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| The name to check for existence. | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## flagSpaceItem

> flagSpaceItem(itemId)

flag a space item

flag a space item OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let itemId = "itemId_example"; // String | the id of the item you want to flag
apiInstance.flagSpaceItem(itemId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemId** | **String**| the id of the item you want to flag | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDirectory

> DirectoryResult getDirectory(sortBy, sortOrder, filter, opts)

Get the directory

Get the directory by a search query in ordered way OauthScopes: READ_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let sortBy = "'LAST_CONTENT'"; // String | sort the spaces by LAST_CONTENT, NAME, NUMBER_OF_USERS or CREATION_DATE
let sortOrder = "'ASCENDING'"; // String | ascending or descending
let filter = "'NONE'"; // String | filter for spaces (JOINED, REQUESTED, OPEN, CLOSED or NOT_JOINED_REQUESTED)
let opts = {
  'query': "query_example", // String | some sort of query
  'pagePointer': "pagePointer_example", // String | page pointer, start with nothing and for next query use returned pointer
  'numberOfResults': 25 // Number | number of results to return, 25 by default.
};
apiInstance.getDirectory(sortBy, sortOrder, filter, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortBy** | **String**| sort the spaces by LAST_CONTENT, NAME, NUMBER_OF_USERS or CREATION_DATE | [default to &#39;LAST_CONTENT&#39;]
 **sortOrder** | **String**| ascending or descending | [default to &#39;ASCENDING&#39;]
 **filter** | **String**| filter for spaces (JOINED, REQUESTED, OPEN, CLOSED or NOT_JOINED_REQUESTED) | [default to &#39;NONE&#39;]
 **query** | **String**| some sort of query | [optional] 
 **pagePointer** | **String**| page pointer, start with nothing and for next query use returned pointer | [optional] 
 **numberOfResults** | **Number**| number of results to return, 25 by default. | [optional] [default to 25]

### Return type

[**DirectoryResult**](DirectoryResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getFlaggedItems

> FlaggedItemsResult getFlaggedItems(searchDirection, timestamp, opts)

Get flagged items

Get flagged items OauthScopes: READ_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let searchDirection = "'BEFORE'"; // String | before or after the time stamp
let timestamp = new Date("2013-10-20T19:20:30+01:00"); // Date | The timestamp according to which you want to retrieve the flagged items
let opts = {
  'searchPointer': "searchPointer_example", // String | The searchpointer for the search (initially not set).
  'numberOfResults': 25 // Number | The number of results you want to retrieve.
};
apiInstance.getFlaggedItems(searchDirection, timestamp, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **searchDirection** | **String**| before or after the time stamp | [default to &#39;BEFORE&#39;]
 **timestamp** | **Date**| The timestamp according to which you want to retrieve the flagged items | 
 **searchPointer** | **String**| The searchpointer for the search (initially not set). | [optional] 
 **numberOfResults** | **Number**| The number of results you want to retrieve. | [optional] [default to 25]

### Return type

[**FlaggedItemsResult**](FlaggedItemsResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getLikes

> ParticipantsLikeResult getLikes(itemId, opts)

Get the likes of an item

Get the likes of an item OauthScopes: READ_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let itemId = "itemId_example"; // String | The id of the item to retrieve the likes from
let opts = {
  'searchPointer': "searchPointer_example", // String | The searchpointer for the search (initially not set).
  'numberOfResults': 25 // Number | The number of results you want to retrieve.
};
apiInstance.getLikes(itemId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemId** | **String**| The id of the item to retrieve the likes from | 
 **searchPointer** | **String**| The searchpointer for the search (initially not set). | [optional] 
 **numberOfResults** | **Number**| The number of results you want to retrieve. | [optional] [default to 25]

### Return type

[**ParticipantsLikeResult**](ParticipantsLikeResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getParticipantsImportData

> ParticipantsImportDataResult getParticipantsImportData(spaceId)

missing documentation

missing documentation OauthScopes: READ_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let spaceId = "spaceId_example"; // String | missing documentation
apiInstance.getParticipantsImportData(spaceId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spaceId** | **String**| missing documentation | 

### Return type

[**ParticipantsImportDataResult**](ParticipantsImportDataResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getPendingParticipants

> ParticipantsSearchResult getPendingParticipants(id, opts)

Get the pending participants of a space

Get the pending participants of a space OauthScopes: WRITE_SPACE, MANAGE_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let id = "id_example"; // String | The id of the space.
let opts = {
  'searchPointer': "searchPointer_example", // String | The search pointer (leave empty initially).
  'numberOfResults': 25 // Number | number of results to return, 25 by default.
};
apiInstance.getPendingParticipants(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The id of the space. | 
 **searchPointer** | **String**| The search pointer (leave empty initially). | [optional] 
 **numberOfResults** | **Number**| number of results to return, 25 by default. | [optional] [default to 25]

### Return type

[**ParticipantsSearchResult**](ParticipantsSearchResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getPinnedTopics

> [SpacePinnedTopic] getPinnedTopics(id)

Retrieve pinned topics

Retrieve pinned topics of a space OauthScopes: READ_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let id = "id_example"; // String | The id of the space.
apiInstance.getPinnedTopics(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The id of the space. | 

### Return type

[**[SpacePinnedTopic]**](SpacePinnedTopic.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getRecentSearches

> [SpacesSearchTermResult] getRecentSearches()

Retrieve recent space searches

Retrieve recent space searches for a user. OauthScopes: READ_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
apiInstance.getRecentSearches((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[SpacesSearchTermResult]**](SpacesSearchTermResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getSpaceParticipants

> ParticipantsSearchResult getSpaceParticipants(id, sortBy, sortOrder, filterType, opts)

Get the participants of a space

Get the participants of a space OauthScopes: READ_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let id = "id_example"; // String | The id of the space.
let sortBy = "'NAME'"; // String | sort the spaces by LAST_CONTENT, NAME, NUMBER_OF_USERS or CREATION_DATE
let sortOrder = "'ASCENDING'"; // String | ascending or descending
let filterType = "filterType_example"; // String | filtertype for participants (ACCESS_TYPE, ROLE or STATE)
let opts = {
  'filterValue': "filterValue_example", // String | value for the filter
  'query': "query_example", // String | some sort of query
  'searchPointer': "searchPointer_example", // String | The search pointer (leave empty initially).
  'numberOfResults': 25 // Number | number of results to return, 25 by default.
};
apiInstance.getSpaceParticipants(id, sortBy, sortOrder, filterType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The id of the space. | 
 **sortBy** | **String**| sort the spaces by LAST_CONTENT, NAME, NUMBER_OF_USERS or CREATION_DATE | [default to &#39;NAME&#39;]
 **sortOrder** | **String**| ascending or descending | [default to &#39;ASCENDING&#39;]
 **filterType** | **String**| filtertype for participants (ACCESS_TYPE, ROLE or STATE) | 
 **filterValue** | **String**| value for the filter | [optional] 
 **query** | **String**| some sort of query | [optional] 
 **searchPointer** | **String**| The search pointer (leave empty initially). | [optional] 
 **numberOfResults** | **Number**| number of results to return, 25 by default. | [optional] [default to 25]

### Return type

[**ParticipantsSearchResult**](ParticipantsSearchResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getSpaceReplies

> SpaceReply getSpaceReplies(spaceId, topicId, searchDirection, opts)

Gets space replies

Gets a number of Space replies OauthScopes: READ_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let spaceId = "spaceId_example"; // String | Id of the containing space
let topicId = "topicId_example"; // String | Id of the topic
let searchDirection = "'BEFORE'"; // String | Search before or after a certain timestamp
let opts = {
  'timestamp': new Date("2013-10-20T19:20:30+01:00"), // Date | Timestamp to start the search from
  'numberOfResults': 25 // Number | The number of results that should be returned
};
apiInstance.getSpaceReplies(spaceId, topicId, searchDirection, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spaceId** | **String**| Id of the containing space | 
 **topicId** | **String**| Id of the topic | 
 **searchDirection** | **String**| Search before or after a certain timestamp | [default to &#39;BEFORE&#39;]
 **timestamp** | **Date**| Timestamp to start the search from | [optional] 
 **numberOfResults** | **Number**| The number of results that should be returned | [optional] [default to 25]

### Return type

[**SpaceReply**](SpaceReply.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getSpaceTopics

> [SpaceTopic] getSpaceTopics(spaceId, searchDirection, opts)

Gets space topics

Gets a number of Space topics OauthScopes: READ_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let spaceId = "spaceId_example"; // String | Id of the space
let searchDirection = "'BEFORE'"; // String | Search before or after a certain timestamp
let opts = {
  'timestamp': new Date("2013-10-20T19:20:30+01:00"), // Date | Timestamp to start the search from
  'numberOfResults': 25 // Number | The number of results that should be returned
};
apiInstance.getSpaceTopics(spaceId, searchDirection, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spaceId** | **String**| Id of the space | 
 **searchDirection** | **String**| Search before or after a certain timestamp | [default to &#39;BEFORE&#39;]
 **timestamp** | **Date**| Timestamp to start the search from | [optional] 
 **numberOfResults** | **Number**| The number of results that should be returned | [optional] [default to 25]

### Return type

[**[SpaceTopic]**](SpaceTopic.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getSpaces

> Object getSpaces(opts)

Get the spaces

Get the spaces OauthScopes: READ_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let opts = {
  'timestamp': new Date("2013-10-20T19:20:30+01:00"), // Date | a beautiful timestamp
  'numberOfResults': 3.4 // Number | the number of results you want
};
apiInstance.getSpaces(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **Date**| a beautiful timestamp | [optional] 
 **numberOfResults** | **Number**| the number of results you want | [optional] 

### Return type

**Object**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getSpacesByIds

> Object getSpacesByIds(ids)

Get the spaces by their ids

Get the spaces by their ids OauthScopes: READ_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let ids = ["null"]; // [String] | an array of ids
apiInstance.getSpacesByIds(ids, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**[String]**](String.md)| an array of ids | 

### Return type

**Object**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## grantSpaceAcces

> grantSpaceAcces(spaceId, participantId)

grant access for a space

grant access for a space OauthScopes: WRITE_SPACE, MANAGE_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let spaceId = "spaceId_example"; // String | Id of the space
let participantId = "participantId_example"; // String | Id of the participant
apiInstance.grantSpaceAcces(spaceId, participantId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spaceId** | **String**| Id of the space | 
 **participantId** | **String**| Id of the participant | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## joinSpace

> Object joinSpace(id)

Join a space

Join a space OauthScopes: WRITE_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let id = "id_example"; // String | The id of the space
apiInstance.joinSpace(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The id of the space | 

### Return type

**Object**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## leaveSpace

> leaveSpace(id)

Leave a space

Leave a space OauthScopes: WRITE_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let id = "id_example"; // String | The id of the space
apiInstance.leaveSpace(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The id of the space | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## likeSpaceItem

> likeSpaceItem(itemId)

Like a space item

Like a space item OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let itemId = "itemId_example"; // String | The id of the item you want to like
apiInstance.likeSpaceItem(itemId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemId** | **String**| The id of the item you want to like | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## pinTopic

> pinTopic(topicId, position)

Pin a topic

Pin a topic OauthScopes: WRITE_SPACE, MANAGE_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let topicId = "topicId_example"; // String | The id of the topic
let position = 3.4; // Number | The position to pin to
apiInstance.pinTopic(topicId, position, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topicId** | **String**| The id of the topic | 
 **position** | **Number**| The position to pin to | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## requestSpaceAcces

> requestSpaceAcces(spaceId, opts)

request access for a space

request access for a space OauthScopes: READ_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let spaceId = "spaceId_example"; // String | Id of the space
let opts = {
  'reason': "reason_example" // String | Reason why the Access has been requested
};
apiInstance.requestSpaceAcces(spaceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spaceId** | **String**| Id of the space | 
 **reason** | **String**| Reason why the Access has been requested | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## searchParticipantsToAdd

> [AddParticipantsSearchResult] searchParticipantsToAdd(id, query)

Finds participants to add to add to a space 

Finds participants to add to a space  OauthScopes: WRITE_SPACE, MANAGE_SPACE, ORGANIZE_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let id = "id_example"; // String | The id of the space
let query = "query_example"; // String | The query 
apiInstance.searchParticipantsToAdd(id, query, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The id of the space | 
 **query** | **String**| The query  | 

### Return type

[**[AddParticipantsSearchResult]**](AddParticipantsSearchResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## searchSpaceParticipants

> [ParticipantsSearchResultLarge] searchSpaceParticipants(id, query)

Get the participants of a space

Get the participants of a space OauthScopes: READ_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let id = "id_example"; // String | The id of the space.
let query = "query_example"; // String | The query to search with. If searchpointer/hasMotre is returned, refine query.
apiInstance.searchSpaceParticipants(id, query, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The id of the space. | 
 **query** | **String**| The query to search with. If searchpointer/hasMotre is returned, refine query. | 

### Return type

[**[ParticipantsSearchResultLarge]**](ParticipantsSearchResultLarge.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## startBasicSpacesSearch

> BasicSearchResult startBasicSpacesSearch(scope, searchTerm, opts)

starts a basic search in spaces

starts a basic search in spaces OauthScopes: READ_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let scope = "scope_example"; // String | the scope of the search
let searchTerm = "searchTerm_example"; // String | the term to search for
let opts = {
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | the starttime
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | the end time
  'prioritySpaces': ["null"] // [String] | list of prioritized spaces
};
apiInstance.startBasicSpacesSearch(scope, searchTerm, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **String**| the scope of the search | 
 **searchTerm** | **String**| the term to search for | 
 **startTime** | **Date**| the starttime | [optional] 
 **endTime** | **Date**| the end time | [optional] 
 **prioritySpaces** | [**[String]**](String.md)| list of prioritized spaces | [optional] 

### Return type

[**BasicSearchResult**](BasicSearchResult.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## startDetailedSpaceSearch

> [SpaceSearchResultDetailedBack] startDetailedSpaceSearch(scope, searchTerm, spaceId, opts)

starts a detailed search in a space

starts a detailed search in a space OauthScopes: READ_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let scope = "scope_example"; // String | the scope of the search
let searchTerm = "searchTerm_example"; // String | the term to search for
let spaceId = "spaceId_example"; // String | missing documentation
let opts = {
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | the starttime
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | the end time
  'searchId': "searchId_example" // String | missing documentation
};
apiInstance.startDetailedSpaceSearch(scope, searchTerm, spaceId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **String**| the scope of the search | 
 **searchTerm** | **String**| the term to search for | 
 **spaceId** | **String**| missing documentation | 
 **startTime** | **Date**| the starttime | [optional] 
 **endTime** | **Date**| the end time | [optional] 
 **searchId** | **String**| missing documentation | [optional] 

### Return type

[**[SpaceSearchResultDetailedBack]**](SpaceSearchResultDetailedBack.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## unassignLabels

> [LabelIds] unassignLabels(id, labelIds)

Unassign labels

Unassign labels from a space OauthScopes: WRITE_SPACE, ORGANIZE_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let id = "id_example"; // String | The id of the space.
let labelIds = ["null"]; // [String] | missing documentation
apiInstance.unassignLabels(id, labelIds, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The id of the space. | 
 **labelIds** | [**[String]**](String.md)| missing documentation | 

### Return type

[**[LabelIds]**](LabelIds.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## unflagSpaceItem

> unflagSpaceItem(itemId)

Unflag a space item

Unflag a space item OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let itemId = "itemId_example"; // String | the id of the item you want to unflag
apiInstance.unflagSpaceItem(itemId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemId** | **String**| the id of the item you want to unflag | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## unlikeSpaceItem

> unlikeSpaceItem(itemId)

Unlike a space item

Unlike a space item OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let itemId = "itemId_example"; // String | The id of the item you want to unlike
apiInstance.unlikeSpaceItem(itemId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **itemId** | **String**| The id of the item you want to unlike | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## unpinTopic

> unpinTopic(topicId)

Unpin a topic

Unpin a topic OauthScopes: WRITE_SPACE, MANAGE_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let topicId = "topicId_example"; // String | The id of the topic to unpin
apiInstance.unpinTopic(topicId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topicId** | **String**| The id of the topic to unpin | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateParticipantInSpace

> updateParticipantInSpace(spaceId, role, userId)

Update participant

Update participant in space OauthScopes: WRITE_SPACE, MANAGE_SPACE, ORGANIZE_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let spaceId = "spaceId_example"; // String | Id of the space
let role = "role_example"; // String | updated role of participant
let userId = "userId_example"; // String | The id of the participant to update
apiInstance.updateParticipantInSpace(spaceId, role, userId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spaceId** | **String**| Id of the space | 
 **role** | **String**| updated role of participant | 
 **userId** | **String**| The id of the participant to update | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## updateReadTimestamp

> updateReadTimestamp(id, timestamp)

Update read timestamp

Update read timestamp OauthScopes: READ_SPACE, WRITE_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let id = "id_example"; // String | Id of a space
let timestamp = new Date("2013-10-20T19:20:30+01:00"); // Date | The new timestamp
apiInstance.updateReadTimestamp(id, timestamp, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Id of a space | 
 **timestamp** | **Date**| The new timestamp | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## updateSpace

> Object updateSpace(id, opts)

Update a space

Update a space OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let id = "id_example"; // String | id of the space
let opts = {
  'accessModeType': "'NO_CHANGE'", // String | Access mode
  'description': "description_example", // String | description of the space
  'largePictureBase64': "largePictureBase64_example", // String | large picture
  'name': "name_example", // String | name of the space
  'ownerId': "ownerId_example", // String | ownerid of the space
  'role': "'NO_CHANGE'", // String | role
  'smallPictureBase64': "smallPictureBase64_example", // String | small picture
  'status': "'ENABLED'", // String | status
  'tags': ["null"], // [String] | tags of the space
  'type': "'NO_CHANGE'" // String | type
};
apiInstance.updateSpace(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| id of the space | 
 **accessModeType** | **String**| Access mode | [optional] [default to &#39;NO_CHANGE&#39;]
 **description** | **String**| description of the space | [optional] 
 **largePictureBase64** | **String**| large picture | [optional] 
 **name** | **String**| name of the space | [optional] 
 **ownerId** | **String**| ownerid of the space | [optional] 
 **role** | **String**| role | [optional] [default to &#39;NO_CHANGE&#39;]
 **smallPictureBase64** | **String**| small picture | [optional] 
 **status** | **String**| status | [optional] [default to &#39;ENABLED&#39;]
 **tags** | [**[String]**](String.md)| tags of the space | [optional] 
 **type** | **String**| type | [optional] [default to &#39;NO_CHANGE&#39;]

### Return type

**Object**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## updateSpaceReply

> SpaceReply updateSpaceReply(spaceId, topicId, replyId, opts)

Updates a space reply

Updates a space reply OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let spaceId = "spaceId_example"; // String | ID of the space
let topicId = "topicId_example"; // String | ID of the topic
let replyId = "replyId_example"; // String | id of the reply
let opts = {
  'attachments': ["null"], // [String] | the attached files
  'complex': true, // Boolean | complex or not
  'content': "content_example", // String | the content of the reply
  'formMetaData': "formMetaData_example", // String | formMetaData of the reply
  'mentionedUsers': ["null"] // [String] | the mentioned users in the reply
};
apiInstance.updateSpaceReply(spaceId, topicId, replyId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spaceId** | **String**| ID of the space | 
 **topicId** | **String**| ID of the topic | 
 **replyId** | **String**| id of the reply | 
 **attachments** | [**[String]**](String.md)| the attached files | [optional] 
 **complex** | **Boolean**| complex or not | [optional] 
 **content** | **String**| the content of the reply | [optional] 
 **formMetaData** | **String**| formMetaData of the reply | [optional] 
 **mentionedUsers** | [**[String]**](String.md)| the mentioned users in the reply | [optional] 

### Return type

[**SpaceReply**](SpaceReply.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## updateSpaceTopic

> SpaceTopic updateSpaceTopic(spaceId, topicId, opts)

Updates a topic

Updates a topic OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let spaceId = "spaceId_example"; // String | ID of the space
let topicId = "topicId_example"; // String | Id of the topic to update
let opts = {
  'attachments': ["null"], // [String] | the attached files
  'complex': true, // Boolean | complex or not
  'content': "content_example", // String | content of the topic
  'contentTags': ["null"], // [String] | the content tags
  'formMetaData': "formMetaData_example", // String | formMetaData to update
  'mentionedUsers': ["null"], // [String] | the updated mentioned users
  'subject': "subject_example", // String | the subject of the topic
  'tags': ["null"] // [String] | the tags
};
apiInstance.updateSpaceTopic(spaceId, topicId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spaceId** | **String**| ID of the space | 
 **topicId** | **String**| Id of the topic to update | 
 **attachments** | [**[String]**](String.md)| the attached files | [optional] 
 **complex** | **Boolean**| complex or not | [optional] 
 **content** | **String**| content of the topic | [optional] 
 **contentTags** | [**[String]**](String.md)| the content tags | [optional] 
 **formMetaData** | **String**| formMetaData to update | [optional] 
 **mentionedUsers** | [**[String]**](String.md)| the updated mentioned users | [optional] 
 **subject** | **String**| the subject of the topic | [optional] 
 **tags** | [**[String]**](String.md)| the tags | [optional] 

### Return type

[**SpaceTopic**](SpaceTopic.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## updateTopicTags

> SpaceTopic updateTopicTags(topicId, tags)

Update tags

Update the tags of a topic   OauthScopes: WRITE_SPACE, UPDATE_SPACE_CONTENT

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let topicId = "topicId_example"; // String | The id of the topic
let tags = ["null"]; // [String] | The tags to update
apiInstance.updateTopicTags(topicId, tags, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topicId** | **String**| The id of the topic | 
 **tags** | [**[String]**](String.md)| The tags to update | 

### Return type

[**SpaceTopic**](SpaceTopic.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json, application/xml


## v2GetTopicWithReplies

> SpaceTopicWithReplies v2GetTopicWithReplies(spaceId, topicId, opts)

Gets space replies and a topic

Gets a number of Space replies with a matching topic OauthScopes: READ_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let spaceId = "spaceId_example"; // String | Id of the topic
let topicId = "topicId_example"; // String | ID of the topic
let opts = {
  'numberOfReplies': 25 // Number | The number of replies
};
apiInstance.v2GetTopicWithReplies(spaceId, topicId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spaceId** | **String**| Id of the topic | 
 **topicId** | **String**| ID of the topic | 
 **numberOfReplies** | **Number**| The number of replies | [optional] [default to 25]

### Return type

[**SpaceTopicWithReplies**](SpaceTopicWithReplies.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## v2RemoveParticipantsFromSpace

> v2RemoveParticipantsFromSpace(id, userIds)

Removes participants from a space

removes Participants from a space OauthScopes: WRITE_SPACE, MANAGE_SPACE, ORGANIZE_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let id = "id_example"; // String | The id of the space
let userIds = ["null"]; // [String] | The ids of the participants to remove 
apiInstance.v2RemoveParticipantsFromSpace(id, userIds, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The id of the space | 
 **userIds** | [**[String]**](String.md)| The ids of the participants to remove  | 

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined


## v2UpdateWelcomeBoxContent

> v2UpdateWelcomeBoxContent(spaceId, content, opts)

Update content of welcome box

Update content of the welcome box of a space OauthScopes: MANAGE_SPACE, WRITE_SPACE

### Example

```javascript
import RestApiVersion2 from 'rest_api_version_2';
let defaultClient = RestApiVersion2.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RestApiVersion2.SpacesApi();
let spaceId = "spaceId_example"; // String | Id of the space
let content = "content_example"; // String | The new content
let opts = {
  'displayWelcomeBox': false // Boolean | True, false, default:false
};
apiInstance.v2UpdateWelcomeBoxContent(spaceId, content, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spaceId** | **String**| Id of the space | 
 **content** | **String**| The new content | 
 **displayWelcomeBox** | **Boolean**| True, false, default:false | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: Not defined

