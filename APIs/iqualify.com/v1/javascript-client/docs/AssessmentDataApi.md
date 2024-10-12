# IQualifyManagementApi.AssessmentDataApi

All URIs are relative to *https://api.iqualify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offeringsOfferingIdAnalyticsActivitiesResponsesGet**](AssessmentDataApi.md#offeringsOfferingIdAnalyticsActivitiesResponsesGet) | **GET** /offerings/{offeringId}/analytics/activities/responses | Find open response activity attempts
[**offeringsOfferingIdAnalyticsMarksAssignmentsGet**](AssessmentDataApi.md#offeringsOfferingIdAnalyticsMarksAssignmentsGet) | **GET** /offerings/{offeringId}/analytics/marks/assignments | Find assessment marks
[**offeringsOfferingIdAnalyticsMarksQuizzesGet**](AssessmentDataApi.md#offeringsOfferingIdAnalyticsMarksQuizzesGet) | **GET** /offerings/{offeringId}/analytics/marks/quizzes | Find quiz marks
[**offeringsOfferingIdAnalyticsSubmissionsAssignmentsGet**](AssessmentDataApi.md#offeringsOfferingIdAnalyticsSubmissionsAssignmentsGet) | **GET** /offerings/{offeringId}/analytics/submissions/assignments | Find submissions to assessments, including marks if any
[**offeringsOfferingIdAnalyticsSubmissionsOpenResponseAssessmentIdGet**](AssessmentDataApi.md#offeringsOfferingIdAnalyticsSubmissionsOpenResponseAssessmentIdGet) | **GET** /offerings/{offeringId}/analytics/submissions/open-response/{assessmentId} | Find submissions to a specified open response assessment, including marks if any
[**offeringsOfferingIdAnalyticsSubmissionsUserEmailAssignmentsAssessmentIdGet**](AssessmentDataApi.md#offeringsOfferingIdAnalyticsSubmissionsUserEmailAssignmentsAssessmentIdGet) | **GET** /offerings/{offeringId}/analytics/submissions/{userEmail}/assignments/{assessmentId} | Find a learner&#39;s submission to a specified assessment, including marks if any



## offeringsOfferingIdAnalyticsActivitiesResponsesGet

> [ActivityAttemptOpenResponse] offeringsOfferingIdAnalyticsActivitiesResponsesGet(offeringId)

Find open response activity attempts

Responds with all learner activity attempts for open response activities in an offering matching the offeringId.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentDataApi();
let offeringId = "offeringId_example"; // String | offering's id
apiInstance.offeringsOfferingIdAnalyticsActivitiesResponsesGet(offeringId, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 

### Return type

[**[ActivityAttemptOpenResponse]**](ActivityAttemptOpenResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdAnalyticsMarksAssignmentsGet

> [AssignmentMarkResponse] offeringsOfferingIdAnalyticsMarksAssignmentsGet(offeringId)

Find assessment marks

Responds with all learner assessment marks in an offering matching the offeringId.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentDataApi();
let offeringId = "offeringId_example"; // String | offering's id
apiInstance.offeringsOfferingIdAnalyticsMarksAssignmentsGet(offeringId, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 

### Return type

[**[AssignmentMarkResponse]**](AssignmentMarkResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdAnalyticsMarksQuizzesGet

> [QuizMarkResponse] offeringsOfferingIdAnalyticsMarksQuizzesGet(offeringId)

Find quiz marks

Responds with all learner quiz marks in an offering matching the offeringId.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentDataApi();
let offeringId = "offeringId_example"; // String | offering's id
apiInstance.offeringsOfferingIdAnalyticsMarksQuizzesGet(offeringId, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 

### Return type

[**[QuizMarkResponse]**](QuizMarkResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdAnalyticsSubmissionsAssignmentsGet

> [AssignmentMarkResponse] offeringsOfferingIdAnalyticsSubmissionsAssignmentsGet(offeringId)

Find submissions to assessments, including marks if any

Responds with all learner assessment submissions and marks, if any, in an offering matching the offeringId.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentDataApi();
let offeringId = "offeringId_example"; // String | offering's id
apiInstance.offeringsOfferingIdAnalyticsSubmissionsAssignmentsGet(offeringId, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 

### Return type

[**[AssignmentMarkResponse]**](AssignmentMarkResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdAnalyticsSubmissionsOpenResponseAssessmentIdGet

> [SubmissionMarkResponse] offeringsOfferingIdAnalyticsSubmissionsOpenResponseAssessmentIdGet(offeringId, assessmentId)

Find submissions to a specified open response assessment, including marks if any

Responds with all learner assessment submissions and marks, if any, in a specified open response assessment.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentDataApi();
let offeringId = "offeringId_example"; // String | offering's id
let assessmentId = "assessmentId_example"; // String | assessment's id
apiInstance.offeringsOfferingIdAnalyticsSubmissionsOpenResponseAssessmentIdGet(offeringId, assessmentId, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **assessmentId** | **String**| assessment&#39;s id | 

### Return type

[**[SubmissionMarkResponse]**](SubmissionMarkResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdAnalyticsSubmissionsUserEmailAssignmentsAssessmentIdGet

> [SubmissionMarkResponse] offeringsOfferingIdAnalyticsSubmissionsUserEmailAssignmentsAssessmentIdGet(offeringId, userEmail, assessmentId)

Find a learner&#39;s submission to a specified assessment, including marks if any

Responds with the learner&#39;s assessment submission and any marks for the submission.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentDataApi();
let offeringId = "offeringId_example"; // String | offering's id
let userEmail = "userEmail_example"; // String | user's email
let assessmentId = "assessmentId_example"; // String | assessment's id
apiInstance.offeringsOfferingIdAnalyticsSubmissionsUserEmailAssignmentsAssessmentIdGet(offeringId, userEmail, assessmentId, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **userEmail** | **String**| user&#39;s email | 
 **assessmentId** | **String**| assessment&#39;s id | 

### Return type

[**[SubmissionMarkResponse]**](SubmissionMarkResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

