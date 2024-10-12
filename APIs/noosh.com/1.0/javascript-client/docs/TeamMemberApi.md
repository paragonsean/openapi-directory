# NooshApiApplication.TeamMemberApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteTeamMemberOfProject**](TeamMemberApi.md#deleteTeamMemberOfProject) | **DELETE** /v1/workgroups/{workgroup_id}/projects/{project_id}/teammembers/{teammember_id} | Delete a team member for the specific project.
[**getTeamMemberListOfClientProject**](TeamMemberApi.md#getTeamMemberListOfClientProject) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/teamMembersOfClientProject | List team member of client project side.
[**getTeamMemberListOfProject**](TeamMemberApi.md#getTeamMemberListOfProject) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/teammembers | List team member of project.
[**postTeamMemberOfProject**](TeamMemberApi.md#postTeamMemberOfProject) | **POST** /1.1/workgroups/{workgroup_id}/projects/{project_id}/teammembers | Invite a team member or all the members of team template for the specific project.
[**v1WorkgroupsWorkgroupIdProjectsProjectIdTeammembersPost**](TeamMemberApi.md#v1WorkgroupsWorkgroupIdProjectsProjectIdTeammembersPost) | **POST** /v1/workgroups/{workgroup_id}/projects/{project_id}/teammembers | Deprecated, please use 1.1 Version



## deleteTeamMemberOfProject

> TeamMemberBaseInfVO deleteTeamMemberOfProject(workgroupId, projectId, teammemberId)

Delete a team member for the specific project.

Delete a team member for the specific project.

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TeamMemberApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let teammemberId = "teammemberId_example"; // String | 
apiInstance.deleteTeamMemberOfProject(workgroupId, projectId, teammemberId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **teammemberId** | **String**|  | 

### Return type

[**TeamMemberBaseInfVO**](TeamMemberBaseInfVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getTeamMemberListOfClientProject

> TeamMemberListVO getTeamMemberListOfClientProject(workgroupId, projectId)

List team member of client project side.

List team member of client project side.

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TeamMemberApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
apiInstance.getTeamMemberListOfClientProject(workgroupId, projectId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 

### Return type

[**TeamMemberListVO**](TeamMemberListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getTeamMemberListOfProject

> TeamMemberListVO getTeamMemberListOfProject(workgroupId, projectId)

List team member of project.

List team member of project.

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TeamMemberApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
apiInstance.getTeamMemberListOfProject(workgroupId, projectId, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 

### Return type

[**TeamMemberListVO**](TeamMemberListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## postTeamMemberOfProject

> V1x1InvitedTeamMemberResultsVO postTeamMemberOfProject(workgroupId, projectId, opts)

Invite a team member or all the members of team template for the specific project.

Invite a team member or all the members of team template for the specific project.

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TeamMemberApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let opts = {
  'teamMemberPO': new NooshApiApplication.TeamMemberPO() // TeamMemberPO | 
};
apiInstance.postTeamMemberOfProject(workgroupId, projectId, opts, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **teamMemberPO** | [**TeamMemberPO**](TeamMemberPO.md)|  | [optional] 

### Return type

[**V1x1InvitedTeamMemberResultsVO**](V1x1InvitedTeamMemberResultsVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## v1WorkgroupsWorkgroupIdProjectsProjectIdTeammembersPost

> TeamMemberBaseInfVO v1WorkgroupsWorkgroupIdProjectsProjectIdTeammembersPost(workgroupId, projectId, opts)

Deprecated, please use 1.1 Version

Deprecated, please use 1.1 Version

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TeamMemberApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let opts = {
  'contactUserVO': new NooshApiApplication.ContactUserVO() // ContactUserVO | 
};
apiInstance.v1WorkgroupsWorkgroupIdProjectsProjectIdTeammembersPost(workgroupId, projectId, opts, (error, data, response) => {
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
 **workgroupId** | **String**|  | 
 **projectId** | **String**|  | 
 **contactUserVO** | [**ContactUserVO**](ContactUserVO.md)|  | [optional] 

### Return type

[**TeamMemberBaseInfVO**](TeamMemberBaseInfVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

