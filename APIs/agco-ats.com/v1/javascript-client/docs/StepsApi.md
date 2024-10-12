# AgcoApi.StepsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stepsGetStep**](StepsApi.md#stepsGetStep) | **GET** /api/v2/steps/{stepID} | Get a Step by ID
[**stepsGetSteps**](StepsApi.md#stepsGetSteps) | **GET** /api/v2/steps | Get Steps
[**stepsPostStep**](StepsApi.md#stepsPostStep) | **POST** /api/v2/steps | Create a Step
[**stepsPutStep**](StepsApi.md#stepsPutStep) | **PUT** /api/v2/steps/{stepID} | Update a Step



## stepsGetStep

> BuildSystemSharedDTOStep stepsGetStep(stepID, opts)

Get a Step by ID

Gets a Step by ID. When successful, the response is the requested Step.              If unsuccessful, an appropriate ApiError is returned.  Steps.Read permission is required.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.StepsApi();
let stepID = 56; // Number | The ID of the Step to get.
let opts = {
  'isIncludeDeleted': true // Boolean | Does it include deleted step, or not
};
apiInstance.stepsGetStep(stepID, opts, (error, data, response) => {
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
 **stepID** | **Number**| The ID of the Step to get. | 
 **isIncludeDeleted** | **Boolean**| Does it include deleted step, or not | [optional] 

### Return type

[**BuildSystemSharedDTOStep**](BuildSystemSharedDTOStep.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## stepsGetSteps

> APIPagedResponseBuildSystemSharedDTOStep stepsGetSteps(opts)

Get Steps

Gets a collection of Steps. When successful, the response is a PagedResponse of Steps.              If unsuccessful, an appropriate ApiError is returned.  Steps.Read permission is required.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.StepsApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit.  If not specified, the default page limit is 10.
  'offset': 56, // Number | Optional. The page offset.  If not specified, the default page offset is 0.
  'includeDeleted': true // Boolean | Does it include deleted step, or not
};
apiInstance.stepsGetSteps(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] 
 **includeDeleted** | **Boolean**| Does it include deleted step, or not | [optional] 

### Return type

[**APIPagedResponseBuildSystemSharedDTOStep**](APIPagedResponseBuildSystemSharedDTOStep.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## stepsPostStep

> Number stepsPostStep(buildSystemSharedDTOStep)

Create a Step

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.StepsApi();
let buildSystemSharedDTOStep = new AgcoApi.BuildSystemSharedDTOStep(); // BuildSystemSharedDTOStep | The step to create
apiInstance.stepsPostStep(buildSystemSharedDTOStep, (error, data, response) => {
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
 **buildSystemSharedDTOStep** | [**BuildSystemSharedDTOStep**](BuildSystemSharedDTOStep.md)| The step to create | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## stepsPutStep

> stepsPutStep(stepID, buildSystemSharedDTOStep)

Update a Step

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.StepsApi();
let stepID = 56; // Number | The step ID of the step to update
let buildSystemSharedDTOStep = new AgcoApi.BuildSystemSharedDTOStep(); // BuildSystemSharedDTOStep | The updated step
apiInstance.stepsPutStep(stepID, buildSystemSharedDTOStep, (error, data, response) => {
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
 **stepID** | **Number**| The step ID of the step to update | 
 **buildSystemSharedDTOStep** | [**BuildSystemSharedDTOStep**](BuildSystemSharedDTOStep.md)| The updated step | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

