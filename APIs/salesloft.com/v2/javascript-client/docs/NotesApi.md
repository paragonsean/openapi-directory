# SalesLoftPlatform.NotesApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2NotesIdJsonDelete**](NotesApi.md#v2NotesIdJsonDelete) | **DELETE** /v2/notes/{id}.json | Delete a note
[**v2NotesIdJsonGet**](NotesApi.md#v2NotesIdJsonGet) | **GET** /v2/notes/{id}.json | Fetch a note
[**v2NotesIdJsonPut**](NotesApi.md#v2NotesIdJsonPut) | **PUT** /v2/notes/{id}.json | Update a note
[**v2NotesJsonGet**](NotesApi.md#v2NotesJsonGet) | **GET** /v2/notes.json | List notes
[**v2NotesJsonPost**](NotesApi.md#v2NotesJsonPost) | **POST** /v2/notes.json | Create a note



## v2NotesIdJsonDelete

> v2NotesIdJsonDelete(id)

Delete a note

Deletes a note owned by authorized account. This operation is not reversible without contacting support. This operation can be called multiple times successfully. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.NotesApi();
let id = "id_example"; // String | Note ID
apiInstance.v2NotesIdJsonDelete(id, (error, data, response) => {
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
 **id** | **String**| Note ID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## v2NotesIdJsonGet

> Note v2NotesIdJsonGet(id)

Fetch a note

Fetches a note, by ID only. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.NotesApi();
let id = "id_example"; // String | Note ID
apiInstance.v2NotesIdJsonGet(id, (error, data, response) => {
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
 **id** | **String**| Note ID | 

### Return type

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2NotesIdJsonPut

> Person v2NotesIdJsonPut(id, content, opts)

Update a note

Updates a note. Any changes to the note or associated records will not reflect in your CRM. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.NotesApi();
let id = "id_example"; // String | Note ID
let content = "content_example"; // String | The content of the note
let opts = {
  'callId': 56 // Number | ID of the call with which the note is associated. The call cannot already have a note. If the note is associated to a call already, it will become associated to the requested call
};
apiInstance.v2NotesIdJsonPut(id, content, opts, (error, data, response) => {
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
 **id** | **String**| Note ID | 
 **content** | **String**| The content of the note | 
 **callId** | **Number**| ID of the call with which the note is associated. The call cannot already have a note. If the note is associated to a call already, it will become associated to the requested call | [optional] 

### Return type

[**Person**](Person.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*


## v2NotesJsonGet

> [Note] v2NotesJsonGet(opts)

List notes

Fetches multiple note records. The records can be filtered, paged, and sorted according to the respective parameters. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.NotesApi();
let opts = {
  'associatedWithType': "associatedWithType_example", // String | Case insensitive type of item with which the note is associated.  Value must be one of: person, account
  'associatedWithId': 56, // Number | ID of the item with which the note is associated.  The associated_with_type must also be present if this parameter is used
  'updatedAt': ["null"], // [String] | Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\"type\":\"object\",\"keys\":[{\"name\":\"gt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"gte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lt\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\"},{\"name\":\"lte\",\"type\":\"iso8601 string\",\"description\":\"Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\"}]} 
  'ids': [null], // [Number] | IDs of notes to fetch. If a record can't be found, that record won't be returned and your request will be successful
  'sortBy': "sortBy_example", // String | Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at
  'sortDirection': "sortDirection_example", // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
  'perPage': 56, // Number | How many records to show per page in the range [1, 100]. Defaults to 25
  'page': 56, // Number | The current page to fetch results from. Defaults to 1
  'includePagingCounts': true, // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
  'limitPagingCounts': true // Boolean | Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data
};
apiInstance.v2NotesJsonGet(opts, (error, data, response) => {
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
 **associatedWithType** | **String**| Case insensitive type of item with which the note is associated.  Value must be one of: person, account | [optional] 
 **associatedWithId** | **Number**| ID of the item with which the note is associated.  The associated_with_type must also be present if this parameter is used | [optional] 
 **updatedAt** | [**[String]**](String.md)| Equality filters that are applied to the updated_at field. A single filter can be used by itself or combined with other filters to create a range.  ---CUSTOM--- {\&quot;type\&quot;:\&quot;object\&quot;,\&quot;keys\&quot;:[{\&quot;name\&quot;:\&quot;gt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;gte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are greater than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lt\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;},{\&quot;name\&quot;:\&quot;lte\&quot;,\&quot;type\&quot;:\&quot;iso8601 string\&quot;,\&quot;description\&quot;:\&quot;Returns all matching records that are less than or equal to the provided iso8601 timestamp. The comparison is done using microsecond precision.\&quot;}]}  | [optional] 
 **ids** | [**[Number]**](Number.md)| IDs of notes to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] 
 **sortBy** | **String**| Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at | [optional] 
 **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] 
 **perPage** | **Number**| How many records to show per page in the range [1, 100]. Defaults to 25 | [optional] 
 **page** | **Number**| The current page to fetch results from. Defaults to 1 | [optional] 
 **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] 
 **limitPagingCounts** | **Boolean**| Specifies whether the max limit of 10k records should be applied to pagination counts. Affects the total_count and total_pages data | [optional] 

### Return type

[**[Note]**](Note.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## v2NotesJsonPost

> Note v2NotesJsonPost(associatedWithId, associatedWithType, content, opts)

Create a note

Creates a note. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.NotesApi();
let associatedWithId = 56; // Number | ID of the item with which the note is associated
let associatedWithType = "associatedWithType_example"; // String | Case insensitive type of item with which the note is associated.  Value must be one of: person, account
let content = "content_example"; // String | The content of the note
let opts = {
  'callId': 56, // Number | ID of the call with which the note is associated. The call cannot already have a note
  'skipCrmSync': true, // Boolean | Boolean indicating if the CRM sync should be skipped.  No syncing will occur if true
  'subject': "subject_example", // String | The subject of the note's crm activity, defaults to 'Note'
  'userGuid': "userGuid_example" // String | The user to create the note for. Only team admins may create notes on behalf of other users. Defaults to the requesting user
};
apiInstance.v2NotesJsonPost(associatedWithId, associatedWithType, content, opts, (error, data, response) => {
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
 **associatedWithId** | **Number**| ID of the item with which the note is associated | 
 **associatedWithType** | **String**| Case insensitive type of item with which the note is associated.  Value must be one of: person, account | 
 **content** | **String**| The content of the note | 
 **callId** | **Number**| ID of the call with which the note is associated. The call cannot already have a note | [optional] 
 **skipCrmSync** | **Boolean**| Boolean indicating if the CRM sync should be skipped.  No syncing will occur if true | [optional] 
 **subject** | **String**| The subject of the note&#39;s crm activity, defaults to &#39;Note&#39; | [optional] 
 **userGuid** | **String**| The user to create the note for. Only team admins may create notes on behalf of other users. Defaults to the requesting user | [optional] 

### Return type

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: */*

