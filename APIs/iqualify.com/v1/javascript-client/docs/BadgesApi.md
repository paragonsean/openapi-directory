# IQualifyManagementApi.BadgesApi

All URIs are relative to *https://api.iqualify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offeringsOfferingIdBadgesGet**](BadgesApi.md#offeringsOfferingIdBadgesGet) | **GET** /offerings/{offeringId}/badges | Find offering badges
[**offeringsOfferingIdUsersUserEmailBadgesAwardPost**](BadgesApi.md#offeringsOfferingIdUsersUserEmailBadgesAwardPost) | **POST** /offerings/{offeringId}/users/{userEmail}/badges/award | Award badge
[**usersUserEmailBadgesGet**](BadgesApi.md#usersUserEmailBadgesGet) | **GET** /users/{userEmail}/badges | Find user&#39;s badges



## offeringsOfferingIdBadgesGet

> Badge offeringsOfferingIdBadgesGet(offeringId)

Find offering badges

Responds with the badge for an offering matching the offeringId.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.BadgesApi();
let offeringId = "offeringId_example"; // String | offering's id
apiInstance.offeringsOfferingIdBadgesGet(offeringId, (error, data, response) => {
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

[**Badge**](Badge.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdUsersUserEmailBadgesAwardPost

> AwardedResponse offeringsOfferingIdUsersUserEmailBadgesAwardPost(offeringId, userEmail)

Award badge

Awards a badge to a user in the offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.BadgesApi();
let offeringId = "offeringId_example"; // String | offering's id
let userEmail = "userEmail_example"; // String | user's email
apiInstance.offeringsOfferingIdUsersUserEmailBadgesAwardPost(offeringId, userEmail, (error, data, response) => {
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

[**AwardedResponse**](AwardedResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserEmailBadgesGet

> [UserBadge] usersUserEmailBadgesGet(userEmail)

Find user&#39;s badges

Responds with all badges that the specified user has been awarded.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.BadgesApi();
let userEmail = "userEmail_example"; // String | user's email
apiInstance.usersUserEmailBadgesGet(userEmail, (error, data, response) => {
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

[**[UserBadge]**](UserBadge.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

