# VictorOps.ScheduledOverridesApi

All URIs are relative to *https://api.victorops.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPublicV1OverridesGet**](ScheduledOverridesApi.md#apiPublicV1OverridesGet) | **GET** /api-public/v1/overrides | List the scheduled overrides
[**apiPublicV1OverridesPost**](ScheduledOverridesApi.md#apiPublicV1OverridesPost) | **POST** /api-public/v1/overrides | Creates a new scheduled override
[**apiPublicV1OverridesPublicIdAssignmentsGet**](ScheduledOverridesApi.md#apiPublicV1OverridesPublicIdAssignmentsGet) | **GET** /api-public/v1/overrides/{publicId}/assignments | Get the specified scheduled override
[**apiPublicV1OverridesPublicIdAssignmentsPolicySlugDelete**](ScheduledOverridesApi.md#apiPublicV1OverridesPublicIdAssignmentsPolicySlugDelete) | **DELETE** /api-public/v1/overrides/{publicId}/assignments/{policySlug} | Delete the scheduled override assignment
[**apiPublicV1OverridesPublicIdAssignmentsPolicySlugGet**](ScheduledOverridesApi.md#apiPublicV1OverridesPublicIdAssignmentsPolicySlugGet) | **GET** /api-public/v1/overrides/{publicId}/assignments/{policySlug} | Get the specified scheduled override assignment
[**apiPublicV1OverridesPublicIdAssignmentsPolicySlugPut**](ScheduledOverridesApi.md#apiPublicV1OverridesPublicIdAssignmentsPolicySlugPut) | **PUT** /api-public/v1/overrides/{publicId}/assignments/{policySlug} | Update the scheduled override assignment
[**apiPublicV1OverridesPublicIdDelete**](ScheduledOverridesApi.md#apiPublicV1OverridesPublicIdDelete) | **DELETE** /api-public/v1/overrides/{publicId} | Deletes a scheduled override
[**apiPublicV1OverridesPublicIdGet**](ScheduledOverridesApi.md#apiPublicV1OverridesPublicIdGet) | **GET** /api-public/v1/overrides/{publicId} | Get the specified scheduled override



## apiPublicV1OverridesGet

> ApiPublicV1OverridesGet200Response apiPublicV1OverridesGet(xVOApiId, xVOApiKey)

List the scheduled overrides

List all the scheduled overrides on the organization  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.ScheduledOverridesApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
apiInstance.apiPublicV1OverridesGet(xVOApiId, xVOApiKey, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 

### Return type

[**ApiPublicV1OverridesGet200Response**](ApiPublicV1OverridesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1OverridesPost

> ApiPublicV1OverridesPost200Response apiPublicV1OverridesPost(xVOApiId, xVOApiKey, body)

Creates a new scheduled override

Creates a new scheduled override. Start and end dates are in ISO8601 format. E.g. &#x60;2018-09-28&#39;T&#39;05:00:00Z&#x60;  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.ScheduledOverridesApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let body = new VictorOps.ScheduledOverridePayload(); // ScheduledOverridePayload | 
apiInstance.apiPublicV1OverridesPost(xVOApiId, xVOApiKey, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **body** | [**ScheduledOverridePayload**](ScheduledOverridePayload.md)|  | 

### Return type

[**ApiPublicV1OverridesPost200Response**](ApiPublicV1OverridesPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1OverridesPublicIdAssignmentsGet

> [Assignment] apiPublicV1OverridesPublicIdAssignmentsGet(xVOApiId, xVOApiKey, publicId)

Get the specified scheduled override

Get the specified scheduled override assignments  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.ScheduledOverridesApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let publicId = "publicId_example"; // String | The publicId of the scheduled override
apiInstance.apiPublicV1OverridesPublicIdAssignmentsGet(xVOApiId, xVOApiKey, publicId, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **publicId** | **String**| The publicId of the scheduled override | 

### Return type

[**[Assignment]**](Assignment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1OverridesPublicIdAssignmentsPolicySlugDelete

> Assignment apiPublicV1OverridesPublicIdAssignmentsPolicySlugDelete(xVOApiId, xVOApiKey, publicId, policySlug)

Delete the scheduled override assignment

Delete the scheduled override assignment  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.ScheduledOverridesApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let publicId = "publicId_example"; // String | The publicId of the scheduled override
let policySlug = "policySlug_example"; // String | The policySlug of the assignment
apiInstance.apiPublicV1OverridesPublicIdAssignmentsPolicySlugDelete(xVOApiId, xVOApiKey, publicId, policySlug, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **publicId** | **String**| The publicId of the scheduled override | 
 **policySlug** | **String**| The policySlug of the assignment | 

### Return type

[**Assignment**](Assignment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1OverridesPublicIdAssignmentsPolicySlugGet

> Assignment apiPublicV1OverridesPublicIdAssignmentsPolicySlugGet(xVOApiId, xVOApiKey, publicId, policySlug)

Get the specified scheduled override assignment

Get the specified scheduled override assignments  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.ScheduledOverridesApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let publicId = "publicId_example"; // String | The publicId of the scheduled override
let policySlug = "policySlug_example"; // String | The policySlug of the assignment
apiInstance.apiPublicV1OverridesPublicIdAssignmentsPolicySlugGet(xVOApiId, xVOApiKey, publicId, policySlug, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **publicId** | **String**| The publicId of the scheduled override | 
 **policySlug** | **String**| The policySlug of the assignment | 

### Return type

[**Assignment**](Assignment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1OverridesPublicIdAssignmentsPolicySlugPut

> Assignment apiPublicV1OverridesPublicIdAssignmentsPolicySlugPut(xVOApiId, xVOApiKey, publicId, policySlug, body)

Update the scheduled override assignment

Update the scheduled override assignment  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.ScheduledOverridesApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let publicId = "publicId_example"; // String | The publicId of the scheduled override
let policySlug = "policySlug_example"; // String | The policySlug of the assignment
let body = new VictorOps.UpdateAssignment(); // UpdateAssignment | The policy and username we are assigning
apiInstance.apiPublicV1OverridesPublicIdAssignmentsPolicySlugPut(xVOApiId, xVOApiKey, publicId, policySlug, body, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **publicId** | **String**| The publicId of the scheduled override | 
 **policySlug** | **String**| The policySlug of the assignment | 
 **body** | [**UpdateAssignment**](UpdateAssignment.md)| The policy and username we are assigning | 

### Return type

[**Assignment**](Assignment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1OverridesPublicIdDelete

> apiPublicV1OverridesPublicIdDelete(xVOApiId, xVOApiKey, publicId)

Deletes a scheduled override

Deletes a scheduled override  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.ScheduledOverridesApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let publicId = "publicId_example"; // String | The publicId of the scheduled override
apiInstance.apiPublicV1OverridesPublicIdDelete(xVOApiId, xVOApiKey, publicId, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **publicId** | **String**| The publicId of the scheduled override | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiPublicV1OverridesPublicIdGet

> ApiPublicV1OverridesPublicIdGet200Response apiPublicV1OverridesPublicIdGet(xVOApiId, xVOApiKey, publicId)

Get the specified scheduled override

Get the specified scheduled override  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.ScheduledOverridesApi();
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let publicId = "publicId_example"; // String | The publicId of the scheduled override
apiInstance.apiPublicV1OverridesPublicIdGet(xVOApiId, xVOApiKey, publicId, (error, data, response) => {
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
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **publicId** | **String**| The publicId of the scheduled override | 

### Return type

[**ApiPublicV1OverridesPublicIdGet200Response**](ApiPublicV1OverridesPublicIdGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

