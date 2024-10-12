# WwwZoomconnectCom.GroupsApi

All URIs are relative to *https://www.zoomconnect.com/app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiRestV1GroupsAllGet**](GroupsApi.md#apiRestV1GroupsAllGet) | **GET** /api/rest/v1/groups/all | all
[**apiRestV1GroupsCreatePost**](GroupsApi.md#apiRestV1GroupsCreatePost) | **POST** /api/rest/v1/groups/create | create
[**apiRestV1GroupsGroupIdAddContactContactIdGet**](GroupsApi.md#apiRestV1GroupsGroupIdAddContactContactIdGet) | **GET** /api/rest/v1/groups/{groupId}/addContact/{contactId} | addContact
[**apiRestV1GroupsGroupIdAddContactContactIdPost**](GroupsApi.md#apiRestV1GroupsGroupIdAddContactContactIdPost) | **POST** /api/rest/v1/groups/{groupId}/addContact/{contactId} | addContact
[**apiRestV1GroupsGroupIdDelete**](GroupsApi.md#apiRestV1GroupsGroupIdDelete) | **DELETE** /api/rest/v1/groups/{groupId} | delete
[**apiRestV1GroupsGroupIdGet**](GroupsApi.md#apiRestV1GroupsGroupIdGet) | **GET** /api/rest/v1/groups/{groupId} | get
[**apiRestV1GroupsGroupIdPost**](GroupsApi.md#apiRestV1GroupsGroupIdPost) | **POST** /api/rest/v1/groups/{groupId} | update
[**apiRestV1GroupsGroupIdRemoveContactContactIdGet**](GroupsApi.md#apiRestV1GroupsGroupIdRemoveContactContactIdGet) | **GET** /api/rest/v1/groups/{groupId}/removeContact/{contactId} | removeContact
[**apiRestV1GroupsGroupIdRemoveContactContactIdPost**](GroupsApi.md#apiRestV1GroupsGroupIdRemoveContactContactIdPost) | **POST** /api/rest/v1/groups/{groupId}/removeContact/{contactId} | removeContact



## apiRestV1GroupsAllGet

> WebServiceGroups apiRestV1GroupsAllGet()

all

Returns all groups

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.GroupsApi();
apiInstance.apiRestV1GroupsAllGet((error, data, response) => {
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

[**WebServiceGroups**](WebServiceGroups.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## apiRestV1GroupsCreatePost

> WebServiceGroup apiRestV1GroupsCreatePost(opts)

create

Create a  group

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.GroupsApi();
let opts = {
  'body': new WwwZoomconnectCom.WebServiceGroup() // WebServiceGroup | webServiceGroup
};
apiInstance.apiRestV1GroupsCreatePost(opts, (error, data, response) => {
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
 **body** | [**WebServiceGroup**](WebServiceGroup.md)| webServiceGroup | [optional] 

### Return type

[**WebServiceGroup**](WebServiceGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## apiRestV1GroupsGroupIdAddContactContactIdGet

> apiRestV1GroupsGroupIdAddContactContactIdGet(groupId, contactId)

addContact

Add a contact to a group

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.GroupsApi();
let groupId = "groupId_example"; // String | groupId
let contactId = "contactId_example"; // String | contactId
apiInstance.apiRestV1GroupsGroupIdAddContactContactIdGet(groupId, contactId, (error, data, response) => {
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
 **groupId** | **String**| groupId | 
 **contactId** | **String**| contactId | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiRestV1GroupsGroupIdAddContactContactIdPost

> apiRestV1GroupsGroupIdAddContactContactIdPost(groupId, contactId)

addContact

Add a contact to a group

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.GroupsApi();
let groupId = "groupId_example"; // String | groupId
let contactId = "contactId_example"; // String | contactId
apiInstance.apiRestV1GroupsGroupIdAddContactContactIdPost(groupId, contactId, (error, data, response) => {
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
 **groupId** | **String**| groupId | 
 **contactId** | **String**| contactId | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiRestV1GroupsGroupIdDelete

> apiRestV1GroupsGroupIdDelete(groupId)

delete

Deletes a  group

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.GroupsApi();
let groupId = "groupId_example"; // String | groupId
apiInstance.apiRestV1GroupsGroupIdDelete(groupId, (error, data, response) => {
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
 **groupId** | **String**| groupId | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiRestV1GroupsGroupIdGet

> WebServiceGroup apiRestV1GroupsGroupIdGet(groupId)

get

Returns details for a single group

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.GroupsApi();
let groupId = "groupId_example"; // String | groupId
apiInstance.apiRestV1GroupsGroupIdGet(groupId, (error, data, response) => {
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
 **groupId** | **String**| groupId | 

### Return type

[**WebServiceGroup**](WebServiceGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## apiRestV1GroupsGroupIdPost

> WebServiceGroup apiRestV1GroupsGroupIdPost(groupId, opts)

update

Update a  group

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.GroupsApi();
let groupId = "groupId_example"; // String | groupId
let opts = {
  'body': new WwwZoomconnectCom.WebServiceGroup() // WebServiceGroup | webServiceGroup
};
apiInstance.apiRestV1GroupsGroupIdPost(groupId, opts, (error, data, response) => {
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
 **groupId** | **String**| groupId | 
 **body** | [**WebServiceGroup**](WebServiceGroup.md)| webServiceGroup | [optional] 

### Return type

[**WebServiceGroup**](WebServiceGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## apiRestV1GroupsGroupIdRemoveContactContactIdGet

> apiRestV1GroupsGroupIdRemoveContactContactIdGet(groupId, contactId)

removeContact

Remove a contact from a group

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.GroupsApi();
let groupId = "groupId_example"; // String | groupId
let contactId = "contactId_example"; // String | contactId
apiInstance.apiRestV1GroupsGroupIdRemoveContactContactIdGet(groupId, contactId, (error, data, response) => {
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
 **groupId** | **String**| groupId | 
 **contactId** | **String**| contactId | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiRestV1GroupsGroupIdRemoveContactContactIdPost

> apiRestV1GroupsGroupIdRemoveContactContactIdPost(groupId, contactId)

removeContact

Remove a contact from a group

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.GroupsApi();
let groupId = "groupId_example"; // String | groupId
let contactId = "contactId_example"; // String | contactId
apiInstance.apiRestV1GroupsGroupIdRemoveContactContactIdPost(groupId, contactId, (error, data, response) => {
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
 **groupId** | **String**| groupId | 
 **contactId** | **String**| contactId | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

