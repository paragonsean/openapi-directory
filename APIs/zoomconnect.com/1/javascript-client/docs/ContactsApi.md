# WwwZoomconnectCom.ContactsApi

All URIs are relative to *https://www.zoomconnect.com/app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiRestV1ContactsAllGet**](ContactsApi.md#apiRestV1ContactsAllGet) | **GET** /api/rest/v1/contacts/all | all
[**apiRestV1ContactsContactIdAddFromGroupGroupIdGet**](ContactsApi.md#apiRestV1ContactsContactIdAddFromGroupGroupIdGet) | **GET** /api/rest/v1/contacts/{contactId}/addFromGroup/{groupId} | removeFromGroup
[**apiRestV1ContactsContactIdAddFromGroupGroupIdPost**](ContactsApi.md#apiRestV1ContactsContactIdAddFromGroupGroupIdPost) | **POST** /api/rest/v1/contacts/{contactId}/addFromGroup/{groupId} | removeFromGroup
[**apiRestV1ContactsContactIdAddToGroupGroupIdGet**](ContactsApi.md#apiRestV1ContactsContactIdAddToGroupGroupIdGet) | **GET** /api/rest/v1/contacts/{contactId}/addToGroup/{groupId} | addToGroup
[**apiRestV1ContactsContactIdAddToGroupGroupIdPost**](ContactsApi.md#apiRestV1ContactsContactIdAddToGroupGroupIdPost) | **POST** /api/rest/v1/contacts/{contactId}/addToGroup/{groupId} | addToGroup
[**apiRestV1ContactsContactIdDelete**](ContactsApi.md#apiRestV1ContactsContactIdDelete) | **DELETE** /api/rest/v1/contacts/{contactId} | delete
[**apiRestV1ContactsContactIdGet**](ContactsApi.md#apiRestV1ContactsContactIdGet) | **GET** /api/rest/v1/contacts/{contactId} | get
[**apiRestV1ContactsContactIdPost**](ContactsApi.md#apiRestV1ContactsContactIdPost) | **POST** /api/rest/v1/contacts/{contactId} | update
[**apiRestV1ContactsCreatePost**](ContactsApi.md#apiRestV1ContactsCreatePost) | **POST** /api/rest/v1/contacts/create | create



## apiRestV1ContactsAllGet

> WebServiceContacts apiRestV1ContactsAllGet()

all

Returns all contacts

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.ContactsApi();
apiInstance.apiRestV1ContactsAllGet((error, data, response) => {
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

[**WebServiceContacts**](WebServiceContacts.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## apiRestV1ContactsContactIdAddFromGroupGroupIdGet

> apiRestV1ContactsContactIdAddFromGroupGroupIdGet(contactId, groupId)

removeFromGroup

Remove a contact from a group

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.ContactsApi();
let contactId = "contactId_example"; // String | contactId
let groupId = "groupId_example"; // String | groupId
apiInstance.apiRestV1ContactsContactIdAddFromGroupGroupIdGet(contactId, groupId, (error, data, response) => {
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
 **contactId** | **String**| contactId | 
 **groupId** | **String**| groupId | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiRestV1ContactsContactIdAddFromGroupGroupIdPost

> apiRestV1ContactsContactIdAddFromGroupGroupIdPost(contactId, groupId)

removeFromGroup

Remove a contact from a group

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.ContactsApi();
let contactId = "contactId_example"; // String | contactId
let groupId = "groupId_example"; // String | groupId
apiInstance.apiRestV1ContactsContactIdAddFromGroupGroupIdPost(contactId, groupId, (error, data, response) => {
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
 **contactId** | **String**| contactId | 
 **groupId** | **String**| groupId | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiRestV1ContactsContactIdAddToGroupGroupIdGet

> apiRestV1ContactsContactIdAddToGroupGroupIdGet(contactId, groupId)

addToGroup

Add a contact to a group

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.ContactsApi();
let contactId = "contactId_example"; // String | contactId
let groupId = "groupId_example"; // String | groupId
apiInstance.apiRestV1ContactsContactIdAddToGroupGroupIdGet(contactId, groupId, (error, data, response) => {
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
 **contactId** | **String**| contactId | 
 **groupId** | **String**| groupId | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiRestV1ContactsContactIdAddToGroupGroupIdPost

> apiRestV1ContactsContactIdAddToGroupGroupIdPost(contactId, groupId)

addToGroup

Add a contact to a group

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.ContactsApi();
let contactId = "contactId_example"; // String | contactId
let groupId = "groupId_example"; // String | groupId
apiInstance.apiRestV1ContactsContactIdAddToGroupGroupIdPost(contactId, groupId, (error, data, response) => {
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
 **contactId** | **String**| contactId | 
 **groupId** | **String**| groupId | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiRestV1ContactsContactIdDelete

> apiRestV1ContactsContactIdDelete(contactId)

delete

Deletes a  contact

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.ContactsApi();
let contactId = "contactId_example"; // String | contactId
apiInstance.apiRestV1ContactsContactIdDelete(contactId, (error, data, response) => {
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
 **contactId** | **String**| contactId | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiRestV1ContactsContactIdGet

> WebServiceContact apiRestV1ContactsContactIdGet(contactId)

get

Returns details for a single contact

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.ContactsApi();
let contactId = "contactId_example"; // String | contactId
apiInstance.apiRestV1ContactsContactIdGet(contactId, (error, data, response) => {
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
 **contactId** | **String**| contactId | 

### Return type

[**WebServiceContact**](WebServiceContact.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## apiRestV1ContactsContactIdPost

> WebServiceContact apiRestV1ContactsContactIdPost(contactId, opts)

update

Updates a  contact

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.ContactsApi();
let contactId = "contactId_example"; // String | contactId
let opts = {
  'body': new WwwZoomconnectCom.WebServiceContact() // WebServiceContact | webServiceContact
};
apiInstance.apiRestV1ContactsContactIdPost(contactId, opts, (error, data, response) => {
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
 **contactId** | **String**| contactId | 
 **body** | [**WebServiceContact**](WebServiceContact.md)| webServiceContact | [optional] 

### Return type

[**WebServiceContact**](WebServiceContact.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## apiRestV1ContactsCreatePost

> WebServiceContact apiRestV1ContactsCreatePost(opts)

create

Creates a  contact

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.ContactsApi();
let opts = {
  'body': new WwwZoomconnectCom.WebServiceContact() // WebServiceContact | webServiceContact
};
apiInstance.apiRestV1ContactsCreatePost(opts, (error, data, response) => {
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
 **body** | [**WebServiceContact**](WebServiceContact.md)| webServiceContact | [optional] 

### Return type

[**WebServiceContact**](WebServiceContact.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

