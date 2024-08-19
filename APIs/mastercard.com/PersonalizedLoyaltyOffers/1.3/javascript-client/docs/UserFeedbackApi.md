# PersonalizedOffers.UserFeedbackApi

All URIs are relative to *https://api.mastercard.com/plo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userfeedbackPost**](UserFeedbackApi.md#userfeedbackPost) | **POST** /userfeedback | Provide User Feedback on Offer



## userfeedbackPost

> UserFeedbackResponse userfeedbackPost(fId, userToken, offerId, feedback)

Provide User Feedback on Offer

This resource allows a user to provide a thumbs-up or a thumbs-down rating of the specified offer. Offer matches that are disliked will be supressed from the results of future calls to Matched Offers. 

### Example

```javascript
import PersonalizedOffers from 'personalized_offers';

let apiInstance = new PersonalizedOffers.UserFeedbackApi();
let fId = "999999"; // String | Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
let userToken = "userToken_example"; // String | Session identifier as returned by the UserToken resource.
let offerId = "d82e1e7c-c6b9-3b46-acd0-5498731c2838"; // String | System-wide identifier for the campaign, not intended for end-user display.
let feedback = 1; // Number | User response to the offer. 0- Dislike offer. 1- Like offer.
apiInstance.userfeedbackPost(fId, userToken, offerId, feedback, (error, data, response) => {
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
 **offerId** | **String**| System-wide identifier for the campaign, not intended for end-user display. | 
 **feedback** | **Number**| User response to the offer. 0- Dislike offer. 1- Like offer. | 

### Return type

[**UserFeedbackResponse**](UserFeedbackResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

