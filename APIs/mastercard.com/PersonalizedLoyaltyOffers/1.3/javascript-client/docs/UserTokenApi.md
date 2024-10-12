# PersonalizedOffers.UserTokenApi

All URIs are relative to *https://api.mastercard.com/plo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usertokenGet**](UserTokenApi.md#usertokenGet) | **GET** /usertoken | Returns User Session Token



## usertokenGet

> UserTokenResponse usertokenGet(fId, authInfo)

Returns User Session Token

This resource creates the user session. It must be called prior to any other API calls for the specified user. The Token value does not expire. 

### Example

```javascript
import PersonalizedOffers from 'personalized_offers';

let apiInstance = new PersonalizedOffers.UserTokenApi();
let fId = "999999"; // String | Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
let authInfo = "authInfo_example"; // String | Authorization Information. AES 128-bit encrypted concatenation of \"User ID as specified in enrollment:FI ID as provided by Mastercard:current Unix time\". Key exchange and establishment of maintenance procedures occur during implementation.
apiInstance.usertokenGet(fId, authInfo, (error, data, response) => {
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
 **authInfo** | **String**| Authorization Information. AES 128-bit encrypted concatenation of \&quot;User ID as specified in enrollment:FI ID as provided by Mastercard:current Unix time\&quot;. Key exchange and establishment of maintenance procedures occur during implementation. | 

### Return type

[**UserTokenResponse**](UserTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

