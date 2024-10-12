# NooshApiApplication.TeamMemberRoleApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMemberRoles**](TeamMemberRoleApi.md#getMemberRoles) | **GET** /v1/workgroups/{workgroup_id}/projects/{project_id}/memberroles/{user_id} | List all the role options for the user



## getMemberRoles

> RoleListVO getMemberRoles(workgroupId, projectId, userId)

List all the role options for the user

List all the role options for the user

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.TeamMemberRoleApi();
let workgroupId = "workgroupId_example"; // String | 
let projectId = "projectId_example"; // String | 
let userId = "userId_example"; // String | 
apiInstance.getMemberRoles(workgroupId, projectId, userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

[**RoleListVO**](RoleListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

