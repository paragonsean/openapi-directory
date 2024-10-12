# Learnifier.ProjectsApi

All URIs are relative to *http://learnifier.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extprojectGet**](ProjectsApi.md#extprojectGet) | **GET** /extproject | Gets Organization Unit by external id
[**orgunitsOrgidProjectsGet**](ProjectsApi.md#orgunitsOrgidProjectsGet) | **GET** /orgunits/{orgid}/projects | Organization Unit Projects
[**orgunitsOrgidProjectsPost**](ProjectsApi.md#orgunitsOrgidProjectsPost) | **POST** /orgunits/{orgid}/projects | Create project
[**orgunitsOrgidProjectsProjectidDelete**](ProjectsApi.md#orgunitsOrgidProjectsProjectidDelete) | **DELETE** /orgunits/{orgid}/projects/{projectid} | Deletes the project
[**orgunitsOrgidProjectsProjectidGet**](ProjectsApi.md#orgunitsOrgidProjectsProjectidGet) | **GET** /orgunits/{orgid}/projects/{projectid} | Project information
[**orgunitsOrgidProjectsProjectidParticipantsGet**](ProjectsApi.md#orgunitsOrgidProjectsProjectidParticipantsGet) | **GET** /orgunits/{orgid}/projects/{projectid}/participants | Project participants
[**orgunitsOrgidProjectsProjectidParticipantsParticipantIdActivatePost**](ProjectsApi.md#orgunitsOrgidProjectsProjectidParticipantsParticipantIdActivatePost) | **POST** /orgunits/{orgid}/projects/{projectid}/participants/${participantId}/activate | Activate participant
[**orgunitsOrgidProjectsProjectidParticipantsParticipantIdDelete**](ProjectsApi.md#orgunitsOrgidProjectsProjectidParticipantsParticipantIdDelete) | **DELETE** /orgunits/{orgid}/projects/{projectid}/participants/${participantId} | Deletes a participant
[**orgunitsOrgidProjectsProjectidParticipantsParticipantIdLoginlinkPost**](ProjectsApi.md#orgunitsOrgidProjectsProjectidParticipantsParticipantIdLoginlinkPost) | **POST** /orgunits/{orgid}/projects/{projectid}/participants/${participantId}/loginlink | Participant login link
[**orgunitsOrgidProjectsProjectidParticipantsPost**](ProjectsApi.md#orgunitsOrgidProjectsProjectidParticipantsPost) | **POST** /orgunits/{orgid}/projects/{projectid}/participants | Add participant
[**orgunitsOrgidProjectsProjectidPatch**](ProjectsApi.md#orgunitsOrgidProjectsProjectidPatch) | **PATCH** /orgunits/{orgid}/projects/{projectid} | Update project information
[**orgunitsOrgidProjectsProjectidTeammembersGet**](ProjectsApi.md#orgunitsOrgidProjectsProjectidTeammembersGet) | **GET** /orgunits/{orgid}/projects/{projectid}/teammembers | Project team members



## extprojectGet

> Project extprojectGet(extid)

Gets Organization Unit by external id

Gets an Organization Unit by external id

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.ProjectsApi();
let extid = "extid_example"; // String | The external id of the organization unit
apiInstance.extprojectGet(extid, (error, data, response) => {
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
 **extid** | **String**| The external id of the organization unit | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsOrgidProjectsGet

> [Project] orgunitsOrgidProjectsGet(orgid)

Organization Unit Projects

Returns the available projects for the organization unit 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.ProjectsApi();
let orgid = 3.4; // Number | Id of the organization unit
apiInstance.orgunitsOrgidProjectsGet(orgid, (error, data, response) => {
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
 **orgid** | **Number**| Id of the organization unit | 

### Return type

[**[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsOrgidProjectsPost

> Project orgunitsOrgidProjectsPost(orgid, body)

Create project

Creates a new project 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.ProjectsApi();
let orgid = 56; // Number | Id of the organization unit
let body = new Learnifier.AddProject(); // AddProject | 
apiInstance.orgunitsOrgidProjectsPost(orgid, body, (error, data, response) => {
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
 **orgid** | **Number**| Id of the organization unit | 
 **body** | [**AddProject**](AddProject.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsOrgidProjectsProjectidDelete

> orgunitsOrgidProjectsProjectidDelete(orgid, projectid)

Deletes the project

Deletes the project. The project can only be deleted if the project do not contain any participants. 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.ProjectsApi();
let orgid = 56; // Number | Id of the organization unit
let projectid = 56; // Number | Id of the project
apiInstance.orgunitsOrgidProjectsProjectidDelete(orgid, projectid, (error, data, response) => {
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
 **orgid** | **Number**| Id of the organization unit | 
 **projectid** | **Number**| Id of the project | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsOrgidProjectsProjectidGet

> Project orgunitsOrgidProjectsProjectidGet(orgid, projectid)

Project information

Returns project information 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.ProjectsApi();
let orgid = 56; // Number | Id of the organization unit
let projectid = 56; // Number | Id of the project
apiInstance.orgunitsOrgidProjectsProjectidGet(orgid, projectid, (error, data, response) => {
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
 **orgid** | **Number**| Id of the organization unit | 
 **projectid** | **Number**| Id of the project | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsOrgidProjectsProjectidParticipantsGet

> [Participation] orgunitsOrgidProjectsProjectidParticipantsGet(orgid, projectid)

Project participants

Returns project participants 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.ProjectsApi();
let orgid = 56; // Number | Id of the organization unit
let projectid = 56; // Number | Id of the project
apiInstance.orgunitsOrgidProjectsProjectidParticipantsGet(orgid, projectid, (error, data, response) => {
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
 **orgid** | **Number**| Id of the organization unit | 
 **projectid** | **Number**| Id of the project | 

### Return type

[**[Participation]**](Participation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsOrgidProjectsProjectidParticipantsParticipantIdActivatePost

> orgunitsOrgidProjectsProjectidParticipantsParticipantIdActivatePost(orgid, projectid, participantId)

Activate participant

Activates a participant so that it can be used 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.ProjectsApi();
let orgid = 56; // Number | Id of the organization unit
let projectid = 56; // Number | Id of the project
let participantId = 56; // Number | Id of the participant
apiInstance.orgunitsOrgidProjectsProjectidParticipantsParticipantIdActivatePost(orgid, projectid, participantId, (error, data, response) => {
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
 **orgid** | **Number**| Id of the organization unit | 
 **projectid** | **Number**| Id of the project | 
 **participantId** | **Number**| Id of the participant | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsOrgidProjectsProjectidParticipantsParticipantIdDelete

> orgunitsOrgidProjectsProjectidParticipantsParticipantIdDelete(orgid, projectid, participantId)

Deletes a participant

Deletes a participant. The user itself will still remain but any state related to the project will be deleted. It might not be possible due to constraints from the products in the project to delete the participant. However this can only be determined at the time of the delete. If a delete fails the participant will have their inError flag set. 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.ProjectsApi();
let orgid = 56; // Number | Id of the organization unit
let projectid = 56; // Number | Id of the project
let participantId = 56; // Number | Participant id
apiInstance.orgunitsOrgidProjectsProjectidParticipantsParticipantIdDelete(orgid, projectid, participantId, (error, data, response) => {
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
 **orgid** | **Number**| Id of the organization unit | 
 **projectid** | **Number**| Id of the project | 
 **participantId** | **Number**| Participant id | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsOrgidProjectsProjectidParticipantsParticipantIdLoginlinkPost

> LoginLink orgunitsOrgidProjectsProjectidParticipantsParticipantIdLoginlinkPost(orgid, projectid, participantId)

Participant login link

Returns a single sign on link for the participant. The link is only usable once and should be used directly. The link expires after a few minutes.  This operation requires the *login link* permission. 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.ProjectsApi();
let orgid = 56; // Number | Id of the organization unit
let projectid = 56; // Number | Id of the project
let participantId = 56; // Number | Id of the participant
apiInstance.orgunitsOrgidProjectsProjectidParticipantsParticipantIdLoginlinkPost(orgid, projectid, participantId, (error, data, response) => {
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
 **orgid** | **Number**| Id of the organization unit | 
 **projectid** | **Number**| Id of the project | 
 **participantId** | **Number**| Id of the participant | 

### Return type

[**LoginLink**](LoginLink.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsOrgidProjectsProjectidParticipantsPost

> orgunitsOrgidProjectsProjectidParticipantsPost(orgid, projectid, body)

Add participant

Add a user to the project. Participant information is created for the user. In the body object, only one of either email or userid must be specified. The participant needs to be activated before it the user can access it. 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.ProjectsApi();
let orgid = 56; // Number | Id of the organization unit
let projectid = 56; // Number | Id of the project
let body = new Learnifier.AddParticipant(); // AddParticipant | 
apiInstance.orgunitsOrgidProjectsProjectidParticipantsPost(orgid, projectid, body, (error, data, response) => {
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
 **orgid** | **Number**| Id of the organization unit | 
 **projectid** | **Number**| Id of the project | 
 **body** | [**AddParticipant**](AddParticipant.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsOrgidProjectsProjectidPatch

> Project orgunitsOrgidProjectsProjectidPatch(orgid, projectid, body)

Update project information

Updates information about a project. Values are only updated if the fields are specified in the input 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.ProjectsApi();
let orgid = 56; // Number | Id of the organization unit
let projectid = 56; // Number | Id of the project
let body = new Learnifier.UpdateProject(); // UpdateProject | 
apiInstance.orgunitsOrgidProjectsProjectidPatch(orgid, projectid, body, (error, data, response) => {
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
 **orgid** | **Number**| Id of the organization unit | 
 **projectid** | **Number**| Id of the project | 
 **body** | [**UpdateProject**](UpdateProject.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgunitsOrgidProjectsProjectidTeammembersGet

> [ProjectTeamMember] orgunitsOrgidProjectsProjectidTeammembersGet(orgid, projectid)

Project team members

Returns the project team members. A team member is a .... 

### Example

```javascript
import Learnifier from 'learnifier';

let apiInstance = new Learnifier.ProjectsApi();
let orgid = 56; // Number | Id of the organization unit
let projectid = 56; // Number | Id of the project
apiInstance.orgunitsOrgidProjectsProjectidTeammembersGet(orgid, projectid, (error, data, response) => {
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
 **orgid** | **Number**| Id of the organization unit | 
 **projectid** | **Number**| Id of the project | 

### Return type

[**[ProjectTeamMember]**](ProjectTeamMember.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

