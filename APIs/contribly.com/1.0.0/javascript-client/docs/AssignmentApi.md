# Contribly.AssignmentApi

All URIs are relative to *https://api.contribly.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignmentsGet**](AssignmentApi.md#assignmentsGet) | **GET** /assignments | List assignments
[**assignmentsIdDelete**](AssignmentApi.md#assignmentsIdDelete) | **DELETE** /assignments/{id} | Delete this assignment and all of it&#39;s contributions
[**assignmentsIdGet**](AssignmentApi.md#assignmentsIdGet) | **GET** /assignments/{id} | Get a single assigment by id
[**assignmentsPost**](AssignmentApi.md#assignmentsPost) | **POST** /assignments | Create a new assignment



## assignmentsGet

> [Assignment] assignmentsGet(opts)

List assignments

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.AssignmentApi();
let opts = {
  'ownedBy': "ownedBy_example", // String | Restrict results to assignments owned by this user.
  'page': 56, // Number | Pagination page
  'pageSize': 56, // Number | Pagination page size
  'q': "q_example", // String | Restrict results to assignments whose name or description matches this keyword.
  'urlWords': "urlWords_example", // String | Select an assignment by urlWords.
  'open': true, // Boolean | Select open or closed assignments
  'alwaysOpen': true, // Boolean | Select assignments with no closing date.
  'tag': "tag_example", // String | Restrict results to assignments which are tagged with this tag.
  'name': "name_example" // String | Restrict results to the assignment (or potentially assignments) with this exact name
};
apiInstance.assignmentsGet(opts, (error, data, response) => {
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
 **ownedBy** | **String**| Restrict results to assignments owned by this user. | [optional] 
 **page** | **Number**| Pagination page | [optional] 
 **pageSize** | **Number**| Pagination page size | [optional] 
 **q** | **String**| Restrict results to assignments whose name or description matches this keyword. | [optional] 
 **urlWords** | **String**| Select an assignment by urlWords. | [optional] 
 **open** | **Boolean**| Select open or closed assignments | [optional] 
 **alwaysOpen** | **Boolean**| Select assignments with no closing date. | [optional] 
 **tag** | **String**| Restrict results to assignments which are tagged with this tag. | [optional] 
 **name** | **String**| Restrict results to the assignment (or potentially assignments) with this exact name | [optional] 

### Return type

[**[Assignment]**](Assignment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assignmentsIdDelete

> assignmentsIdDelete(id)

Delete this assignment and all of it&#39;s contributions

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.AssignmentApi();
let id = "id_example"; // String | Id of the assignment to return
apiInstance.assignmentsIdDelete(id, (error, data, response) => {
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
 **id** | **String**| Id of the assignment to return | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## assignmentsIdGet

> Assignment assignmentsIdGet(id)

Get a single assigment by id

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.AssignmentApi();
let id = "id_example"; // String | Id of the assignment to return
apiInstance.assignmentsIdGet(id, (error, data, response) => {
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
 **id** | **String**| Id of the assignment to return | 

### Return type

[**Assignment**](Assignment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assignmentsPost

> Assignment assignmentsPost(assignmentSubmission)

Create a new assignment

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.AssignmentApi();
let assignmentSubmission = new Contribly.AssignmentSubmission(); // AssignmentSubmission | Assignment object to be created
apiInstance.assignmentsPost(assignmentSubmission, (error, data, response) => {
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
 **assignmentSubmission** | [**AssignmentSubmission**](AssignmentSubmission.md)| Assignment object to be created | 

### Return type

[**Assignment**](Assignment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

