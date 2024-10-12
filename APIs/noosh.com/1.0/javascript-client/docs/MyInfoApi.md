# NooshApiApplication.MyInfoApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAutomaticInvitationList**](MyInfoApi.md#getAutomaticInvitationList) | **GET** /v1/workgroups/{workgroup_id}/automaticInvitations | List current user&#39;s automatic invitations info 
[**getTeamTemplateDetail**](MyInfoApi.md#getTeamTemplateDetail) | **GET** /v1/workgroups/{workgroup_id}/teamTemplates/{team_template_id} | Get current user&#39;s team template detal info 
[**getTeamTemplateList**](MyInfoApi.md#getTeamTemplateList) | **GET** /v1/workgroups/{workgroup_id}/teamTemplates | List current user&#39;s team templates info 
[**uploadProfileImage**](MyInfoApi.md#uploadProfileImage) | **POST** /v1/workgroups/{workgroup_id}/profileImage | Upload Profile Image.  A multipart/form-data request with a name \&quot;file\&quot;



## getAutomaticInvitationList

> AutomaticInvitationsListVO getAutomaticInvitationList(workgroupId)

List current user&#39;s automatic invitations info 

List current user&#39;s automatic invitations info 

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.MyInfoApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getAutomaticInvitationList(workgroupId, (error, data, response) => {
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

### Return type

[**AutomaticInvitationsListVO**](AutomaticInvitationsListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getTeamTemplateDetail

> TeamTemplateExpandVO getTeamTemplateDetail(workgroupId, teamTemplateId)

Get current user&#39;s team template detal info 

Get current user&#39;s team template detal info 

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.MyInfoApi();
let workgroupId = "workgroupId_example"; // String | 
let teamTemplateId = "teamTemplateId_example"; // String | 
apiInstance.getTeamTemplateDetail(workgroupId, teamTemplateId, (error, data, response) => {
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
 **teamTemplateId** | **String**|  | 

### Return type

[**TeamTemplateExpandVO**](TeamTemplateExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getTeamTemplateList

> TeamTemplateListVO getTeamTemplateList(workgroupId)

List current user&#39;s team templates info 

List current user&#39;s team templates info 

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.MyInfoApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getTeamTemplateList(workgroupId, (error, data, response) => {
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

### Return type

[**TeamTemplateListVO**](TeamTemplateListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## uploadProfileImage

> ProfileImageVO uploadProfileImage(workgroupId, opts)

Upload Profile Image.  A multipart/form-data request with a name \&quot;file\&quot;

Upload Profile Image.  A multipart/form-data request with a name \&quot;file\&quot;

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.MyInfoApi();
let workgroupId = "workgroupId_example"; // String | 
let opts = {
  'body': "/path/to/file" // File | 
};
apiInstance.uploadProfileImage(workgroupId, opts, (error, data, response) => {
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
 **body** | **File**|  | [optional] 

### Return type

[**ProfileImageVO**](ProfileImageVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

