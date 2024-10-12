# IQualifyManagementApi.AssessmentGroupsApi

All URIs are relative to *https://api.iqualify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offeringsOfferingIdGroupsGet**](AssessmentGroupsApi.md#offeringsOfferingIdGroupsGet) | **GET** /offerings/{offeringId}/groups | Find assessment groups
[**offeringsOfferingIdGroupsGroupIdLearnersGet**](AssessmentGroupsApi.md#offeringsOfferingIdGroupsGroupIdLearnersGet) | **GET** /offerings/{offeringId}/groups/{groupId}/learners | Find learners in an assessment group
[**offeringsOfferingIdGroupsGroupIdLearnersPost**](AssessmentGroupsApi.md#offeringsOfferingIdGroupsGroupIdLearnersPost) | **POST** /offerings/{offeringId}/groups/{groupId}/learners | Add a learner to an assessment group
[**offeringsOfferingIdGroupsGroupIdLearnersUserEmailDelete**](AssessmentGroupsApi.md#offeringsOfferingIdGroupsGroupIdLearnersUserEmailDelete) | **DELETE** /offerings/{offeringId}/groups/{groupId}/learners/{userEmail} | Remove a learner from an assessment group
[**offeringsOfferingIdGroupsPost**](AssessmentGroupsApi.md#offeringsOfferingIdGroupsPost) | **POST** /offerings/{offeringId}/groups | Add an assessment group



## offeringsOfferingIdGroupsGet

> [AssessmentGroupResponse] offeringsOfferingIdGroupsGet(offeringId)

Find assessment groups

Responds with a list of assessment groups in an offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentGroupsApi();
let offeringId = "offeringId_example"; // String | offering's id
apiInstance.offeringsOfferingIdGroupsGet(offeringId, (error, data, response) => {
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

[**[AssessmentGroupResponse]**](AssessmentGroupResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdGroupsGroupIdLearnersGet

> [UserResponse] offeringsOfferingIdGroupsGroupIdLearnersGet(offeringId, groupId)

Find learners in an assessment group

Responds with a list of learners in a specified assessment group.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentGroupsApi();
let offeringId = "offeringId_example"; // String | offering's id
let groupId = "groupId_example"; // String | Assessment group id
apiInstance.offeringsOfferingIdGroupsGroupIdLearnersGet(offeringId, groupId, (error, data, response) => {
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
 **groupId** | **String**| Assessment group id | 

### Return type

[**[UserResponse]**](UserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdGroupsGroupIdLearnersPost

> UserResponse offeringsOfferingIdGroupsGroupIdLearnersPost(offeringId, groupId, offeringsOfferingIdGroupsGroupIdLearnersPostRequest)

Add a learner to an assessment group

Adds a learner into the specified assessment group.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentGroupsApi();
let offeringId = "offeringId_example"; // String | offering's id
let groupId = "groupId_example"; // String | Assessment group id
let offeringsOfferingIdGroupsGroupIdLearnersPostRequest = new IQualifyManagementApi.OfferingsOfferingIdGroupsGroupIdLearnersPostRequest(); // OfferingsOfferingIdGroupsGroupIdLearnersPostRequest | 
apiInstance.offeringsOfferingIdGroupsGroupIdLearnersPost(offeringId, groupId, offeringsOfferingIdGroupsGroupIdLearnersPostRequest, (error, data, response) => {
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
 **groupId** | **String**| Assessment group id | 
 **offeringsOfferingIdGroupsGroupIdLearnersPostRequest** | [**OfferingsOfferingIdGroupsGroupIdLearnersPostRequest**](OfferingsOfferingIdGroupsGroupIdLearnersPostRequest.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## offeringsOfferingIdGroupsGroupIdLearnersUserEmailDelete

> offeringsOfferingIdGroupsGroupIdLearnersUserEmailDelete(offeringId, groupId, userEmail)

Remove a learner from an assessment group

Removes a learner from the specified assessment group.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentGroupsApi();
let offeringId = "offeringId_example"; // String | offering's id
let groupId = "groupId_example"; // String | Assessment group id
let userEmail = "userEmail_example"; // String | user's email
apiInstance.offeringsOfferingIdGroupsGroupIdLearnersUserEmailDelete(offeringId, groupId, userEmail, (error, data, response) => {
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
 **groupId** | **String**| Assessment group id | 
 **userEmail** | **String**| user&#39;s email | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdGroupsPost

> AssessmentGroupResponse offeringsOfferingIdGroupsPost(offeringId, assessmentGroupRequired)

Add an assessment group

Creates a new assessment group in an offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.AssessmentGroupsApi();
let offeringId = "offeringId_example"; // String | offering's id
let assessmentGroupRequired = new IQualifyManagementApi.AssessmentGroupRequired(); // AssessmentGroupRequired | 
apiInstance.offeringsOfferingIdGroupsPost(offeringId, assessmentGroupRequired, (error, data, response) => {
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
 **assessmentGroupRequired** | [**AssessmentGroupRequired**](AssessmentGroupRequired.md)|  | 

### Return type

[**AssessmentGroupResponse**](AssessmentGroupResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

