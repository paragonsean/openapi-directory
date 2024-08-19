# PersonalizedOffers.UserSavingsApi

All URIs are relative to *https://api.mastercard.com/plo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersavingsGet**](UserSavingsApi.md#usersavingsGet) | **GET** /usersavings | Returns Savings for the User



## usersavingsGet

> UserSavingsResponse usersavingsGet(fId, userToken)

Returns Savings for the User

This resource returns the accumulated and potential savings for a Personalized Offers user. 

### Example

```javascript
import PersonalizedOffers from 'personalized_offers';

let apiInstance = new PersonalizedOffers.UserSavingsApi();
let fId = "999999"; // String | Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
let userToken = "userToken_example"; // String | Session identifier as returned by the UserToken resource.
apiInstance.usersavingsGet(fId, userToken, (error, data, response) => {
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
 **fId** | **String**| Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation. | 
 **userToken** | **String**| Session identifier as returned by the UserToken resource. | 

### Return type

[**UserSavingsResponse**](UserSavingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

