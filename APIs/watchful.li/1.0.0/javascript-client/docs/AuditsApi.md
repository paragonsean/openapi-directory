# WatchfulLi.AuditsApi

All URIs are relative to *https://watchful.li/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteAuditById**](AuditsApi.md#deleteAuditById) | **DELETE** /audits/{id} | Delete a specific audit
[**getAuditById**](AuditsApi.md#getAuditById) | **GET** /audits/{id} | Find audit by ID
[**getAudits**](AuditsApi.md#getAudits) | **GET** /audits | Get a list of audits
[**getFieldsAudits**](AuditsApi.md#getFieldsAudits) | **GET** /audits/metadata | Get the list of fields



## deleteAuditById

> String deleteAuditById(id)

Delete a specific audit

Delete a specific audit

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.AuditsApi();
let id = 789; // Number | ID of audit that needs to be deleted
apiInstance.deleteAuditById(id, (error, data, response) => {
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
 **id** | **Number**| ID of audit that needs to be deleted | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## getAuditById

> Audit getAuditById(id, opts)

Find audit by ID

Returns a audit based on ID

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.AuditsApi();
let id = 789; // Number | ID of audit that needs to be fetched
let opts = {
  'fields': "fields_example" // String | Fields to return separate by comas: name,id
};
apiInstance.getAuditById(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of audit that needs to be fetched | 
 **fields** | **String**| Fields to return separate by comas: name,id | [optional] 

### Return type

[**Audit**](Audit.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## getAudits

> Audit getAudits(opts)

Get a list of audits

Returns a list of audits

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.AuditsApi();
let opts = {
  'limit': 789, // Number | Number of object to return (max 100, default 25)
  'limitstart': 789, // Number | Start of the return (default 0)
  'order': "order_example" // String | ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name-
};
apiInstance.getAudits(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of object to return (max 100, default 25) | [optional] 
 **limitstart** | **Number**| Start of the return (default 0) | [optional] 
 **order** | **String**| ORDER by this field separete by comas. Add + / - after field for set ASC / DESC: type+,name- | [optional] 

### Return type

[**Audit**](Audit.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain


## getFieldsAudits

> String getFieldsAudits()

Get the list of fields

Returns a list of fields

### Example

```javascript
import WatchfulLi from 'watchful_li';

let apiInstance = new WatchfulLi.AuditsApi();
apiInstance.getFieldsAudits((error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/plain

