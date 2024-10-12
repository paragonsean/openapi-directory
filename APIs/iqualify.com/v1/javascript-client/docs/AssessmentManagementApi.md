# IQualifyManagementApi.AssessmentManagementApi

All URIs are relative to *https://api.iqualify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offeringsOfferingIdActivitiesOpenresponseGet**](AssessmentManagementApi.md#offeringsOfferingIdActivitiesOpenresponseGet) | **GET** /offerings/{offeringId}/activities/openresponse | Find offering&#39;s activities
[**offeringsOfferingIdAssessmentsAssessmentIdDocumentsDocumentIdDelete**](AssessmentManagementApi.md#offeringsOfferingIdAssessmentsAssessmentIdDocumentsDocumentIdDelete) | **DELETE** /offerings/{offeringId}/assessments/{assessmentId}/documents/{documentId} | Remove assessment document
[**offeringsOfferingIdAssessmentsAssessmentIdPatch**](AssessmentManagementApi.md#offeringsOfferingIdAssessmentsAssessmentIdPatch) | **PATCH** /offerings/{offeringId}/assessments/{assessmentId} | Update assessment details
[**offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatch**](AssessmentManagementApi.md#offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatch) | **PATCH** /offerings/{offeringId}/assessments/{assessmentId}/{userEmail} | Update the due dates for a learner&#39;s quiz attempt
[**offeringsOfferingIdAssessmentsGet**](AssessmentManagementApi.md#offeringsOfferingIdAssessmentsGet) | **GET** /offerings/{offeringId}/assessments | Find offering&#39;s assessments
[**offeringsOfferingIdLearnersPendingSubmissionGet**](AssessmentManagementApi.md#offeringsOfferingIdLearnersPendingSubmissionGet) | **GET** /offerings/{offeringId}/learners/pending-submission | Find learners with assessments pending x days before due date within the specified offeringId
[**offeringsOfferingIdUsersUserEmailAssessmentsAssessmentIdDelete**](AssessmentManagementApi.md#offeringsOfferingIdUsersUserEmailAssessmentsAssessmentIdDelete) | **DELETE** /offerings/{offeringId}/users/{userEmail}/assessments/{assessmentId} | Reset user&#39;s assessment to draft state
[**offeringsOfferingIdUsersUserEmailSubmissionsOpenResponseGet**](AssessmentManagementApi.md#offeringsOfferingIdUsersUserEmailSubmissionsOpenResponseGet) | **GET** /offerings/{offeringId}/users/{userEmail}/submissions/open-response | Find learner&#39;s open response assessment submissions



## offeringsOfferingIdActivitiesOpenresponseGet

> [OfferingActivitiesResponse] offeringsOfferingIdActivitiesOpenresponseGet(offeringId)

Find offering&#39;s activities

Responds with the activities in a specific offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentManagementApi();
let offeringId = "offeringId_example"; // String | offering's id
apiInstance.offeringsOfferingIdActivitiesOpenresponseGet(offeringId, (error, data, response) => {
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

[**[OfferingActivitiesResponse]**](OfferingActivitiesResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdAssessmentsAssessmentIdDocumentsDocumentIdDelete

> offeringsOfferingIdAssessmentsAssessmentIdDocumentsDocumentIdDelete(offeringId, assessmentId, documentId)

Remove assessment document

Removes the assessment document file for a specified assessment in an offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentManagementApi();
let offeringId = "offeringId_example"; // String | offering's id
let assessmentId = "assessmentId_example"; // String | assessment's id
let documentId = "documentId_example"; // String | documents's id
apiInstance.offeringsOfferingIdAssessmentsAssessmentIdDocumentsDocumentIdDelete(offeringId, assessmentId, documentId, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **assessmentId** | **String**| assessment&#39;s id | 
 **documentId** | **String**| documents&#39;s id | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdAssessmentsAssessmentIdPatch

> AssessmentResponse offeringsOfferingIdAssessmentsAssessmentIdPatch(offeringId, assessmentId, assessment)

Update assessment details

Updates the assessment details for a specified assessment in an offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentManagementApi();
let offeringId = "offeringId_example"; // String | offering's id
let assessmentId = "assessmentId_example"; // String | assessment's id
let assessment = new IQualifyManagementApi.Assessment(); // Assessment | 
apiInstance.offeringsOfferingIdAssessmentsAssessmentIdPatch(offeringId, assessmentId, assessment, (error, data, response) => {
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
 **assessment** | [**Assessment**](Assessment.md)|  | 

### Return type

[**AssessmentResponse**](AssessmentResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatch

> offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatch(offeringId, assessmentId, userEmail, offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest)

Update the due dates for a learner&#39;s quiz attempt

Updates the due dates for a learner&#39;s quiz attempt specified by the assessmentId.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentManagementApi();
let offeringId = "offeringId_example"; // String | offering's id
let assessmentId = "assessmentId_example"; // String | assessment's id
let userEmail = "userEmail_example"; // String | user's email
let offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest = new IQualifyManagementApi.OfferingsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest(); // OfferingsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest | 
apiInstance.offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatch(offeringId, assessmentId, userEmail, offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **assessmentId** | **String**| assessment&#39;s id | 
 **userEmail** | **String**| user&#39;s email | 
 **offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest** | [**OfferingsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest**](OfferingsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## offeringsOfferingIdAssessmentsGet

> [AssessmentResponse] offeringsOfferingIdAssessmentsGet(offeringId)

Find offering&#39;s assessments

Responds with all assessments in an offering matching the offeringId.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentManagementApi();
let offeringId = "offeringId_example"; // String | offering's id
apiInstance.offeringsOfferingIdAssessmentsGet(offeringId, (error, data, response) => {
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

[**[AssessmentResponse]**](AssessmentResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdLearnersPendingSubmissionGet

> [AssessmentPendingSubmission] offeringsOfferingIdLearnersPendingSubmissionGet(offeringId, opts)

Find learners with assessments pending x days before due date within the specified offeringId

Responds with learners who have one or more assessments due x days before the due date, with each assessment that is due, where x &#x3D; the number of days specified in the request. The default is 3 days.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentManagementApi();
let offeringId = "offeringId_example"; // String | offering's id
let opts = {
  'days': "days_example" // String | days to assessment due date. Default is 3 days
};
apiInstance.offeringsOfferingIdLearnersPendingSubmissionGet(offeringId, opts, (error, data, response) => {
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
 **days** | **String**| days to assessment due date. Default is 3 days | [optional] 

### Return type

[**[AssessmentPendingSubmission]**](AssessmentPendingSubmission.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdUsersUserEmailAssessmentsAssessmentIdDelete

> offeringsOfferingIdUsersUserEmailAssessmentsAssessmentIdDelete(offeringId, userEmail, assessmentId)

Reset user&#39;s assessment to draft state

Resets the user&#39;s submitted assessment to a draft state.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentManagementApi();
let offeringId = "offeringId_example"; // String | offering's id
let userEmail = "userEmail_example"; // String | user's email
let assessmentId = "assessmentId_example"; // String | assessment's id
apiInstance.offeringsOfferingIdUsersUserEmailAssessmentsAssessmentIdDelete(offeringId, userEmail, assessmentId, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **userEmail** | **String**| user&#39;s email | 
 **assessmentId** | **String**| assessment&#39;s id | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdUsersUserEmailSubmissionsOpenResponseGet

> [Assignments] offeringsOfferingIdUsersUserEmailSubmissionsOpenResponseGet(offeringId, userEmail)

Find learner&#39;s open response assessment submissions

Responds with open response assessment submissions by a learner in an offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentManagementApi();
let offeringId = "offeringId_example"; // String | offering's id
let userEmail = "userEmail_example"; // String | user's email
apiInstance.offeringsOfferingIdUsersUserEmailSubmissionsOpenResponseGet(offeringId, userEmail, (error, data, response) => {
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

### Return type

[**[Assignments]**](Assignments.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

