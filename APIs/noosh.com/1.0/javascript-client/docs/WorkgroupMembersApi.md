# NooshApiApplication.WorkgroupMembersApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getWorkgroupMemberInfo**](WorkgroupMembersApi.md#getWorkgroupMemberInfo) | **GET** /v1/workgroups/{workgroup_id}/workgroupMembers/{user_id} | Workgroup Member Info
[**getWorkgroupMemberList**](WorkgroupMembersApi.md#getWorkgroupMemberList) | **GET** /v1/workgroups/{workgroup_id}/workgroupMembers | List the workgroup members



## getWorkgroupMemberInfo

> UserDetailsExpandVO getWorkgroupMemberInfo(workgroupId, userId)

Workgroup Member Info

Workgroup Member Info

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.WorkgroupMembersApi();
let workgroupId = "workgroupId_example"; // String | 
let userId = "userId_example"; // String | 
apiInstance.getWorkgroupMemberInfo(workgroupId, userId, (error, data, response) => {
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
 **userId** | **String**|  | 

### Return type

[**UserDetailsExpandVO**](UserDetailsExpandVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getWorkgroupMemberList

> WorkgroupMembersListVO getWorkgroupMemberList(workgroupId)

List the workgroup members

List the workgroup members

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.WorkgroupMembersApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getWorkgroupMemberList(workgroupId, (error, data, response) => {
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

[**WorkgroupMembersListVO**](WorkgroupMembersListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml

