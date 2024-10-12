# MatchApi.AcquirerContactRequestApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fraudMerchantV3CommonContactDetailsPost**](AcquirerContactRequestApi.md#fraudMerchantV3CommonContactDetailsPost) | **POST** /fraud/merchant/v3/common/contact-details | Returns the contact information for the acquirer id requested. When MATCH returns a possible merchant match, this resource assists users by retrieving the contact information associated with the Acquirer ID/ICA that added the merchant to MATCH.



## fraudMerchantV3CommonContactDetailsPost

> ContactResponseSchema fraudMerchantV3CommonContactDetailsPost(contactRequest)

Returns the contact information for the acquirer id requested. When MATCH returns a possible merchant match, this resource assists users by retrieving the contact information associated with the Acquirer ID/ICA that added the merchant to MATCH.

Returns the contact information for the acquirer id requested. When MATCH returns a possible merchant match, this resource assists users by retrieving the contact information associated with the Acquirer ID/ICA that added the merchant to MATCH. 

### Example

```javascript
import MatchApi from 'match_api';

let apiInstance = new MatchApi.AcquirerContactRequestApi();
let contactRequest = new MatchApi.ContactRequestSchema(); // ContactRequestSchema | The contact request object
apiInstance.fraudMerchantV3CommonContactDetailsPost(contactRequest, (error, data, response) => {
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
 **contactRequest** | [**ContactRequestSchema**](ContactRequestSchema.md)| The contact request object | 

### Return type

[**ContactResponseSchema**](ContactResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

