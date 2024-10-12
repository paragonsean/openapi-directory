# ApiForTheCovid19TrackingQrCodeSigninServer.TeamMembersApi

All URIs are relative to *http://c19qrserver.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userPost**](TeamMembersApi.md#userPost) | **POST** /user | Create a user
[**userUserIdDelete**](TeamMembersApi.md#userUserIdDelete) | **DELETE** /user/{userId} | Delete a team member&#39;s user record
[**userUserIdGet**](TeamMembersApi.md#userUserIdGet) | **GET** /user/{userId} | Retrieve the information associated with a team member&#39;s user record
[**usersGet**](TeamMembersApi.md#usersGet) | **GET** /users | Retrieve the information associated with all team members&#39; user records



## userPost

> CreateUserResponse userPost(sample3)

Create a user

Use this endpoint to create a team member (user) record

### Example

```javascript
import ApiForTheCovid19TrackingQrCodeSigninServer from 'api_for_the_covid_19_tracking_qr_code_signin_server_';
let defaultClient = ApiForTheCovid19TrackingQrCodeSigninServer.ApiClient.instance;
// Configure API key authorization: TokenHeader
let TokenHeader = defaultClient.authentications['TokenHeader'];
TokenHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenHeader.apiKeyPrefix = 'Token';

let apiInstance = new ApiForTheCovid19TrackingQrCodeSigninServer.TeamMembersApi();
let sample3 = new ApiForTheCovid19TrackingQrCodeSigninServer.Sample3(); // Sample3 | Create User Payload
apiInstance.userPost(sample3, (error, data, response) => {
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
 **sample3** | [**Sample3**](Sample3.md)| Create User Payload | 

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## userUserIdDelete

> userUserIdDelete(userId)

Delete a team member&#39;s user record

To preserve referential integrity in the database, the user account  will not be deleted from the database. Rather, the password will be set to the empty string, effectively preventing that user from logging in. Furthermore, all active sessions for that user will be deleted, as will any password reset tokens.  

### Example

```javascript
import ApiForTheCovid19TrackingQrCodeSigninServer from 'api_for_the_covid_19_tracking_qr_code_signin_server_';
let defaultClient = ApiForTheCovid19TrackingQrCodeSigninServer.ApiClient.instance;
// Configure API key authorization: TokenHeader
let TokenHeader = defaultClient.authentications['TokenHeader'];
TokenHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenHeader.apiKeyPrefix = 'Token';

let apiInstance = new ApiForTheCovid19TrackingQrCodeSigninServer.TeamMembersApi();
let userId = 1; // Number | The ID of the user record to be deleted.
apiInstance.userUserIdDelete(userId, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user record to be deleted. | 

### Return type

null (empty response body)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## userUserIdGet

> UserRecord userUserIdGet(userId)

Retrieve the information associated with a team member&#39;s user record

Retrieve the information associated with a user&#39;s account 

### Example

```javascript
import ApiForTheCovid19TrackingQrCodeSigninServer from 'api_for_the_covid_19_tracking_qr_code_signin_server_';
let defaultClient = ApiForTheCovid19TrackingQrCodeSigninServer.ApiClient.instance;
// Configure API key authorization: TokenHeader
let TokenHeader = defaultClient.authentications['TokenHeader'];
TokenHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenHeader.apiKeyPrefix = 'Token';

let apiInstance = new ApiForTheCovid19TrackingQrCodeSigninServer.TeamMembersApi();
let userId = 1; // Number | The ID of the user record to be retrieved.
apiInstance.userUserIdGet(userId, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user record to be retrieved. | 

### Return type

[**UserRecord**](UserRecord.md)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersGet

> [UserRecord] usersGet()

Retrieve the information associated with all team members&#39; user records

Retrieve the information associated with all team members&#39; user records 

### Example

```javascript
import ApiForTheCovid19TrackingQrCodeSigninServer from 'api_for_the_covid_19_tracking_qr_code_signin_server_';
let defaultClient = ApiForTheCovid19TrackingQrCodeSigninServer.ApiClient.instance;
// Configure API key authorization: TokenHeader
let TokenHeader = defaultClient.authentications['TokenHeader'];
TokenHeader.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//TokenHeader.apiKeyPrefix = 'Token';

let apiInstance = new ApiForTheCovid19TrackingQrCodeSigninServer.TeamMembersApi();
apiInstance.usersGet((error, data, response) => {
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

[**[UserRecord]**](UserRecord.md)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

