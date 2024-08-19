# UserFeedbackApi

All URIs are relative to *https://api.mastercard.com/plo/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userfeedbackPost**](UserFeedbackApi.md#userfeedbackPost) | **POST** /userfeedback | Provide User Feedback on Offer |


<a id="userfeedbackPost"></a>
# **userfeedbackPost**
> UserFeedbackResponse userfeedbackPost(fid, userToken, offerId, feedback)

Provide User Feedback on Offer

This resource allows a user to provide a thumbs-up or a thumbs-down rating of the specified offer. Offer matches that are disliked will be supressed from the results of future calls to Matched Offers. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserFeedbackApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/plo/v1");

    UserFeedbackApi apiInstance = new UserFeedbackApi(defaultClient);
    String fid = "999999"; // String | Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
    String userToken = "userToken_example"; // String | Session identifier as returned by the UserToken resource.
    String offerId = "d82e1e7c-c6b9-3b46-acd0-5498731c2838"; // String | System-wide identifier for the campaign, not intended for end-user display.
    Integer feedback = 1; // Integer | User response to the offer. 0- Dislike offer. 1- Like offer.
    try {
      UserFeedbackResponse result = apiInstance.userfeedbackPost(fid, userToken, offerId, feedback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserFeedbackApi#userfeedbackPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **fid** | **String**| Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation. | |
| **userToken** | **String**| Session identifier as returned by the UserToken resource. | |
| **offerId** | **String**| System-wide identifier for the campaign, not intended for end-user display. | |
| **feedback** | **Integer**| User response to the offer. 0- Dislike offer. 1- Like offer. | |

### Return type

[**UserFeedbackResponse**](UserFeedbackResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This resource returns the user rating of the specified offer. |  -  |
| **0** | Unexpected error |  -  |

