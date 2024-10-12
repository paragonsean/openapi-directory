# NooshApiApplication.ContactApi

All URIs are relative to *http://example.com:80/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getBillingRecipients**](ContactApi.md#getBillingRecipients) | **GET** /v1/workgroups/{workgroup_id}/billingRecipients | List Billing Recipients
[**getContactList**](ContactApi.md#getContactList) | **GET** /v1/workgroups/{workgroup_id}/contacts | List the contacts
[**getContactUserInfo**](ContactApi.md#getContactUserInfo) | **GET** /v1/workgroups/{workgroup_id}/contacts/{user_id} | Contact Info



## getBillingRecipients

> ContactsListVO getBillingRecipients(workgroupId)

List Billing Recipients

List Billing Recipients

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ContactApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getBillingRecipients(workgroupId, (error, data, response) => {
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

[**ContactsListVO**](ContactsListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getContactList

> ContactsListVO getContactList(workgroupId)

List the contacts

List the contacts

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ContactApi();
let workgroupId = "workgroupId_example"; // String | 
apiInstance.getContactList(workgroupId, (error, data, response) => {
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

[**ContactsListVO**](ContactsListVO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json, application/x-json-smile, application/x-yaml, application/xml, text/csv, text/x-yaml, text/xml


## getContactUserInfo

> UserDetailsExpandVO getContactUserInfo(workgroupId, userId)

Contact Info

Contact Info

### Example

```javascript
import NooshApiApplication from 'noosh_api_application';

let apiInstance = new NooshApiApplication.ContactApi();
let workgroupId = "workgroupId_example"; // String | 
let userId = "userId_example"; // String | 
apiInstance.getContactUserInfo(workgroupId, userId, (error, data, response) => {
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

