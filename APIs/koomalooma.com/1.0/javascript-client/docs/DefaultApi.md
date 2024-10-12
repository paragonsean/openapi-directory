# KoomaloomaPartnerApi.DefaultApi

All URIs are relative to *https://api.koomalooma.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersPost**](DefaultApi.md#usersPost) | **POST** /users | Create a User
[**usersUserIdCommitmentsPost**](DefaultApi.md#usersUserIdCommitmentsPost) | **POST** /users/{user_id}/commitments | Assign points to a User



## usersPost

> User usersPost()

Create a User

### Example

```javascript
import KoomaloomaPartnerApi from 'koomalooma_partner_api';
let defaultClient = KoomaloomaPartnerApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new KoomaloomaPartnerApi.DefaultApi();
apiInstance.usersPost((error, data, response) => {
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

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## usersUserIdCommitmentsPost

> Commitment usersUserIdCommitmentsPost(userId, commitmentRequest)

Assign points to a User

### Example

```javascript
import KoomaloomaPartnerApi from 'koomalooma_partner_api';
let defaultClient = KoomaloomaPartnerApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new KoomaloomaPartnerApi.DefaultApi();
let userId = "userId_example"; // String | user_id of the user to assign points to
let commitmentRequest = new KoomaloomaPartnerApi.CommitmentRequest(); // CommitmentRequest | 
apiInstance.usersUserIdCommitmentsPost(userId, commitmentRequest, (error, data, response) => {
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
 **userId** | **String**| user_id of the user to assign points to | 
 **commitmentRequest** | [**CommitmentRequest**](CommitmentRequest.md)|  | 

### Return type

[**Commitment**](Commitment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

