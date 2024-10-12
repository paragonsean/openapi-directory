# MembersApi.ReferenceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiReferenceAnsweringBodiesGet**](ReferenceApi.md#apiReferenceAnsweringBodiesGet) | **GET** /api/Reference/AnsweringBodies | Returns a list of answering bodies.
[**apiReferenceDepartmentsGet**](ReferenceApi.md#apiReferenceDepartmentsGet) | **GET** /api/Reference/Departments | Returns a list of departments.
[**apiReferenceDepartmentsIdLogoGet**](ReferenceApi.md#apiReferenceDepartmentsIdLogoGet) | **GET** /api/Reference/Departments/{id}/Logo | Returns department logo.
[**apiReferencePolicyInterestsGet**](ReferenceApi.md#apiReferencePolicyInterestsGet) | **GET** /api/Reference/PolicyInterests | Returns a list of policy interest.



## apiReferenceAnsweringBodiesGet

> [AnsweringBody] apiReferenceAnsweringBodiesGet(opts)

Returns a list of answering bodies.

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.ReferenceApi();
let opts = {
  'id': 56, // Number | 
  'nameContains': "nameContains_example" // String | 
};
apiInstance.apiReferenceAnsweringBodiesGet(opts, (error, data, response) => {
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
 **id** | **Number**|  | [optional] 
 **nameContains** | **String**|  | [optional] 

### Return type

[**[AnsweringBody]**](AnsweringBody.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiReferenceDepartmentsGet

> [GovernmentDepartment] apiReferenceDepartmentsGet(opts)

Returns a list of departments.

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.ReferenceApi();
let opts = {
  'id': 56, // Number | 
  'nameContains': "nameContains_example" // String | 
};
apiInstance.apiReferenceDepartmentsGet(opts, (error, data, response) => {
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
 **id** | **Number**|  | [optional] 
 **nameContains** | **String**|  | [optional] 

### Return type

[**[GovernmentDepartment]**](GovernmentDepartment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiReferenceDepartmentsIdLogoGet

> apiReferenceDepartmentsIdLogoGet(id)

Returns department logo.

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.ReferenceApi();
let id = 56; // Number | Logo by department ID
apiInstance.apiReferenceDepartmentsIdLogoGet(id, (error, data, response) => {
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
 **id** | **Number**| Logo by department ID | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiReferencePolicyInterestsGet

> [GenericReferenceData] apiReferencePolicyInterestsGet()

Returns a list of policy interest.

### Example

```javascript
import MembersApi from 'members_api';

let apiInstance = new MembersApi.ReferenceApi();
apiInstance.apiReferencePolicyInterestsGet((error, data, response) => {
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

[**[GenericReferenceData]**](GenericReferenceData.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

