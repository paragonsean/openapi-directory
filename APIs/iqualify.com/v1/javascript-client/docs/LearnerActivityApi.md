# IQualifyManagementApi.LearnerActivityApi

All URIs are relative to *https://api.iqualify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offeringsOfferingIdAnalyticsLearnersProgressGet**](LearnerActivityApi.md#offeringsOfferingIdAnalyticsLearnersProgressGet) | **GET** /offerings/{offeringId}/analytics/learners-progress | Find learner progress in a specified offering
[**offeringsOfferingIdAnalyticsSocialNotesGet**](LearnerActivityApi.md#offeringsOfferingIdAnalyticsSocialNotesGet) | **GET** /offerings/{offeringId}/analytics/social-notes | Find shared social notes in an offering
[**offeringsOfferingIdAnalyticsUnitReactionsGet**](LearnerActivityApi.md#offeringsOfferingIdAnalyticsUnitReactionsGet) | **GET** /offerings/{offeringId}/analytics/unit-reactions | Find unit reactions
[**usersAllProgressGet**](LearnerActivityApi.md#usersAllProgressGet) | **GET** /users/all/progress | Find learner progress in all offerings
[**usersUserEmailOfferingsOfferingIdProgressGet**](LearnerActivityApi.md#usersUserEmailOfferingsOfferingIdProgressGet) | **GET** /users/{userEmail}/offerings/{offeringId}/progress | Find learner&#39;s progress in a specified offering
[**usersUserEmailProgressGet**](LearnerActivityApi.md#usersUserEmailProgressGet) | **GET** /users/{userEmail}/progress | Find learner&#39;s progress in offerings



## offeringsOfferingIdAnalyticsLearnersProgressGet

> [LearnerProgressResponse] offeringsOfferingIdAnalyticsLearnersProgressGet(offeringId)

Find learner progress in a specified offering

Responds with all learner progress in the offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.LearnerActivityApi();
let offeringId = "offeringId_example"; // String | offering's id
apiInstance.offeringsOfferingIdAnalyticsLearnersProgressGet(offeringId, (error, data, response) => {
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

[**[LearnerProgressResponse]**](LearnerProgressResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdAnalyticsSocialNotesGet

> [SocialNotesResponse] offeringsOfferingIdAnalyticsSocialNotesGet(offeringId)

Find shared social notes in an offering

Responds with all shared social notes in a specified offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.LearnerActivityApi();
let offeringId = "offeringId_example"; // String | offering's id
apiInstance.offeringsOfferingIdAnalyticsSocialNotesGet(offeringId, (error, data, response) => {
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

[**[SocialNotesResponse]**](SocialNotesResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdAnalyticsUnitReactionsGet

> [UnitReactionsAnalyticsResponse] offeringsOfferingIdAnalyticsUnitReactionsGet(offeringId)

Find unit reactions

Responds with user reactions to units in a specified offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.LearnerActivityApi();
let offeringId = "offeringId_example"; // String | offering's id
apiInstance.offeringsOfferingIdAnalyticsUnitReactionsGet(offeringId, (error, data, response) => {
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

[**[UnitReactionsAnalyticsResponse]**](UnitReactionsAnalyticsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersAllProgressGet

> UsersAllProgressGet200Response usersAllProgressGet(opts)

Find learner progress in all offerings

Responds with all learners&#39; progress in all offerings.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.LearnerActivityApi();
let opts = {
  'top': "'50'", // String | Returns only the first n results.
  'orderby': "orderby_example", // String | Sorts the results.
  'filter': "filter_example" // String | Filters the results, based on a Boolean condition.
};
apiInstance.usersAllProgressGet(opts, (error, data, response) => {
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
 **top** | **String**| Returns only the first n results. | [optional] [default to &#39;50&#39;]
 **orderby** | **String**| Sorts the results. | [optional] 
 **filter** | **String**| Filters the results, based on a Boolean condition. | [optional] 

### Return type

[**UsersAllProgressGet200Response**](UsersAllProgressGet200Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserEmailOfferingsOfferingIdProgressGet

> UsersUserEmailOfferingsOfferingIdProgressGet200Response usersUserEmailOfferingsOfferingIdProgressGet(userEmail, offeringId)

Find learner&#39;s progress in a specified offering

Responds with the learner&#39;s progress in a specified offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.LearnerActivityApi();
let userEmail = "userEmail_example"; // String | user's email
let offeringId = "offeringId_example"; // String | offering's id
apiInstance.usersUserEmailOfferingsOfferingIdProgressGet(userEmail, offeringId, (error, data, response) => {
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
 **userEmail** | **String**| user&#39;s email | 
 **offeringId** | **String**| offering&#39;s id | 

### Return type

[**UsersUserEmailOfferingsOfferingIdProgressGet200Response**](UsersUserEmailOfferingsOfferingIdProgressGet200Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserEmailProgressGet

> LearnerResponse usersUserEmailProgressGet(userEmail)

Find learner&#39;s progress in offerings

Responds with the specified learner&#39;s progress in all offerings.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.LearnerActivityApi();
let userEmail = "userEmail_example"; // String | user's email
apiInstance.usersUserEmailProgressGet(userEmail, (error, data, response) => {
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
 **userEmail** | **String**| user&#39;s email | 

### Return type

[**LearnerResponse**](LearnerResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

