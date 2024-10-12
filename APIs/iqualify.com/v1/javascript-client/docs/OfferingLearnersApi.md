# IQualifyManagementApi.OfferingLearnersApi

All URIs are relative to *https://api.iqualify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offeringsOfferingIdUsersGet**](OfferingLearnersApi.md#offeringsOfferingIdUsersGet) | **GET** /offerings/{offeringId}/users | Find offering&#39;s users
[**offeringsOfferingIdUsersMarkerEmailMarksDelete**](OfferingLearnersApi.md#offeringsOfferingIdUsersMarkerEmailMarksDelete) | **DELETE** /offerings/{offeringId}/users/{markerEmail}/marks | Remove learners from coach&#39;s marking list
[**offeringsOfferingIdUsersMarkerEmailMarksGet**](OfferingLearnersApi.md#offeringsOfferingIdUsersMarkerEmailMarksGet) | **GET** /offerings/{offeringId}/users/{markerEmail}/marks | Find Learners marked by a coach
[**offeringsOfferingIdUsersMarkerEmailMarksPost**](OfferingLearnersApi.md#offeringsOfferingIdUsersMarkerEmailMarksPost) | **POST** /offerings/{offeringId}/users/{markerEmail}/marks | Add learners to be marked by a coach
[**offeringsOfferingIdUsersPost**](OfferingLearnersApi.md#offeringsOfferingIdUsersPost) | **POST** /offerings/{offeringId}/users | Adds user to the offering
[**offeringsOfferingIdUsersUserEmailDelete**](OfferingLearnersApi.md#offeringsOfferingIdUsersUserEmailDelete) | **DELETE** /offerings/{offeringId}/users/{userEmail} | Removes user from the offering
[**usersUserEmailTransferPatch**](OfferingLearnersApi.md#usersUserEmailTransferPatch) | **PATCH** /users/{userEmail}/transfer | Transfer a user between offerings



## offeringsOfferingIdUsersGet

> [OfferingUserResponse] offeringsOfferingIdUsersGet(offeringId, opts)

Find offering&#39;s users

Responds with a list of users in the offering (facilitators, learners and markers.).

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingLearnersApi();
let offeringId = "offeringId_example"; // String | offering's id
let opts = {
  'facilitators': "'true'", // String | If true, facilitators are included in the results.
  'learners': "'true'", // String | If true, learners are included in the results.
  'markers': "'true'" // String | If true, markers are included in the results.
};
apiInstance.offeringsOfferingIdUsersGet(offeringId, opts, (error, data, response) => {
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
 **facilitators** | **String**| If true, facilitators are included in the results. | [optional] [default to &#39;true&#39;]
 **learners** | **String**| If true, learners are included in the results. | [optional] [default to &#39;true&#39;]
 **markers** | **String**| If true, markers are included in the results. | [optional] [default to &#39;true&#39;]

### Return type

[**[OfferingUserResponse]**](OfferingUserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdUsersMarkerEmailMarksDelete

> [OfferingUser] offeringsOfferingIdUsersMarkerEmailMarksDelete(offeringId, markerEmail, requestBody)

Remove learners from coach&#39;s marking list

Removes an array of learners from coach&#39;s marking list.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingLearnersApi();
let offeringId = "offeringId_example"; // String | offering's id
let markerEmail = "markerEmail_example"; // String | marker's email
let requestBody = ["null"]; // [String] | array of learners e-mails
apiInstance.offeringsOfferingIdUsersMarkerEmailMarksDelete(offeringId, markerEmail, requestBody, (error, data, response) => {
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
 **markerEmail** | **String**| marker&#39;s email | 
 **requestBody** | [**[String]**](String.md)| array of learners e-mails | 

### Return type

[**[OfferingUser]**](OfferingUser.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## offeringsOfferingIdUsersMarkerEmailMarksGet

> [OfferingUser] offeringsOfferingIdUsersMarkerEmailMarksGet(offeringId, markerEmail)

Find Learners marked by a coach

Responds with all learners marked by the specified coach.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingLearnersApi();
let offeringId = "offeringId_example"; // String | offering's id
let markerEmail = "markerEmail_example"; // String | marker's email
apiInstance.offeringsOfferingIdUsersMarkerEmailMarksGet(offeringId, markerEmail, (error, data, response) => {
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
 **markerEmail** | **String**| marker&#39;s email | 

### Return type

[**[OfferingUser]**](OfferingUser.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdUsersMarkerEmailMarksPost

> [OfferingUser] offeringsOfferingIdUsersMarkerEmailMarksPost(offeringId, markerEmail, requestBody)

Add learners to be marked by a coach

Adds an array of learners to be marked by the specified coach.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingLearnersApi();
let offeringId = "offeringId_example"; // String | offering's id
let markerEmail = "markerEmail_example"; // String | marker's email
let requestBody = ["null"]; // [String] | array of learners e-mails
apiInstance.offeringsOfferingIdUsersMarkerEmailMarksPost(offeringId, markerEmail, requestBody, (error, data, response) => {
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
 **markerEmail** | **String**| marker&#39;s email | 
 **requestBody** | [**[String]**](String.md)| array of learners e-mails | 

### Return type

[**[OfferingUser]**](OfferingUser.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## offeringsOfferingIdUsersPost

> [OfferingUserAddResponse] offeringsOfferingIdUsersPost(offeringId, offeringUser)

Adds user to the offering

Adds one or more users to the offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingLearnersApi();
let offeringId = "offeringId_example"; // String | offering's id
let offeringUser = [new IQualifyManagementApi.OfferingUser()]; // [OfferingUser] | 
apiInstance.offeringsOfferingIdUsersPost(offeringId, offeringUser, (error, data, response) => {
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
 **offeringUser** | [**[OfferingUser]**](OfferingUser.md)|  | 

### Return type

[**[OfferingUserAddResponse]**](OfferingUserAddResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## offeringsOfferingIdUsersUserEmailDelete

> offeringsOfferingIdUsersUserEmailDelete(offeringId, userEmail)

Removes user from the offering

Removes a user from the offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingLearnersApi();
let offeringId = "offeringId_example"; // String | offering's id
let userEmail = "userEmail_example"; // String | user's email
apiInstance.offeringsOfferingIdUsersUserEmailDelete(offeringId, userEmail, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserEmailTransferPatch

> usersUserEmailTransferPatch(userEmail, transferRequest)

Transfer a user between offerings

Moves the user&#39;s access and progress from one offering to another.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingLearnersApi();
let userEmail = "userEmail_example"; // String | user's email
let transferRequest = new IQualifyManagementApi.TransferRequest(); // TransferRequest | transfer_data
apiInstance.usersUserEmailTransferPatch(userEmail, transferRequest, (error, data, response) => {
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
 **userEmail** | **String**| user&#39;s email | 
 **transferRequest** | [**TransferRequest**](TransferRequest.md)| transfer_data | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

