# Story.StoryCollaboratorsApi

All URIs are relative to */story*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storyIdCollaboratorsGet**](StoryCollaboratorsApi.md#storyIdCollaboratorsGet) | **GET** /{id}/collaborators | Story Collaborators: List
[**storyIdCollaboratorsInactivePost**](StoryCollaboratorsApi.md#storyIdCollaboratorsInactivePost) | **POST** /{id}/collaborators/inactive | Story Collaborators: Edit Inactive User Permission
[**storyIdCollaboratorsPost**](StoryCollaboratorsApi.md#storyIdCollaboratorsPost) | **POST** /{id}/collaborators | Story Collaborators: Add New User
[**storyIdCollaboratorsUseridDelete**](StoryCollaboratorsApi.md#storyIdCollaboratorsUseridDelete) | **DELETE** /{id}/collaborators/{story_collaborator_userid} | Story Collaborators: Remove User
[**storyIdCollaboratorsUseridGet**](StoryCollaboratorsApi.md#storyIdCollaboratorsUseridGet) | **GET** /{id}/collaborators/{story_collaborator_userid} | Story Collaborators: Access Permissions
[**storyIdCollaboratorsUseridPut**](StoryCollaboratorsApi.md#storyIdCollaboratorsUseridPut) | **PUT** /{id}/collaborators/{story_collaborator_userid} | Story Collaborators: Edit Access Rights



## storyIdCollaboratorsGet

> [StoryCollaborator] storyIdCollaboratorsGet(id)

Story Collaborators: List

Gets a list users that can read or edit this story

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryCollaboratorsApi();
let id = "id_example"; // String | the id from the story object
apiInstance.storyIdCollaboratorsGet(id, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 

### Return type

[**[StoryCollaborator]**](StoryCollaborator.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storyIdCollaboratorsInactivePost

> StoryCollaborator storyIdCollaboratorsInactivePost(id, modifyInactiveCollaborator)

Story Collaborators: Edit Inactive User Permission

Edit story permissions for inactive users.  Requires admin rights.

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryCollaboratorsApi();
let id = "id_example"; // String | the id from the story object
let modifyInactiveCollaborator = new Story.ModifyInactiveCollaborator(); // ModifyInactiveCollaborator | Collaborator user id and permission type
apiInstance.storyIdCollaboratorsInactivePost(id, modifyInactiveCollaborator, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 
 **modifyInactiveCollaborator** | [**ModifyInactiveCollaborator**](ModifyInactiveCollaborator.md)| Collaborator user id and permission type | 

### Return type

[**StoryCollaborator**](StoryCollaborator.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storyIdCollaboratorsPost

> StoryCollaborator storyIdCollaboratorsPost(id, addNewCollaboratorRequest)

Story Collaborators: Add New User

Add a colloborator to this story

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryCollaboratorsApi();
let id = "id_example"; // String | the id from the story object
let addNewCollaboratorRequest = new Story.AddNewCollaboratorRequest(); // AddNewCollaboratorRequest | Collaborator user id and permission type
apiInstance.storyIdCollaboratorsPost(id, addNewCollaboratorRequest, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 
 **addNewCollaboratorRequest** | [**AddNewCollaboratorRequest**](AddNewCollaboratorRequest.md)| Collaborator user id and permission type | 

### Return type

[**StoryCollaborator**](StoryCollaborator.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storyIdCollaboratorsUseridDelete

> storyIdCollaboratorsUseridDelete(id, storyCollaboratorUserid)

Story Collaborators: Remove User

Remove a collaborator from this story

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryCollaboratorsApi();
let id = "id_example"; // String | the id from the story object
let storyCollaboratorUserid = "storyCollaboratorUserid_example"; // String | The presalytics userid (NOT the Id of the story_collaborator object)
apiInstance.storyIdCollaboratorsUseridDelete(id, storyCollaboratorUserid, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 
 **storyCollaboratorUserid** | **String**| The presalytics userid (NOT the Id of the story_collaborator object) | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storyIdCollaboratorsUseridGet

> StoryCollaborator storyIdCollaboratorsUseridGet(id, storyCollaboratorUserid)

Story Collaborators: Access Permissions

Data to help you understand the access rights of a particular collaborator on this story

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryCollaboratorsApi();
let id = "id_example"; // String | the id from the story object
let storyCollaboratorUserid = "storyCollaboratorUserid_example"; // String | The presalytics userid (NOT the Id of the story_collaborator object)
apiInstance.storyIdCollaboratorsUseridGet(id, storyCollaboratorUserid, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 
 **storyCollaboratorUserid** | **String**| The presalytics userid (NOT the Id of the story_collaborator object) | 

### Return type

[**StoryCollaborator**](StoryCollaborator.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storyIdCollaboratorsUseridPut

> StoryCollaborator storyIdCollaboratorsUseridPut(id, storyCollaboratorUserid, storyCollaborator)

Story Collaborators: Edit Access Rights

Modify a user&#39;s access right to this story (e.g., grant edit permissions)

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.StoryCollaboratorsApi();
let id = "id_example"; // String | the id from the story object
let storyCollaboratorUserid = "storyCollaboratorUserid_example"; // String | The presalytics userid (NOT the Id of the story_collaborator object)
let storyCollaborator = new Story.StoryCollaborator(); // StoryCollaborator | Collaborator user id (presalytics userid) and permission type
apiInstance.storyIdCollaboratorsUseridPut(id, storyCollaboratorUserid, storyCollaborator, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 
 **storyCollaboratorUserid** | **String**| The presalytics userid (NOT the Id of the story_collaborator object) | 
 **storyCollaborator** | [**StoryCollaborator**](StoryCollaborator.md)| Collaborator user id (presalytics userid) and permission type | 

### Return type

[**StoryCollaborator**](StoryCollaborator.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

