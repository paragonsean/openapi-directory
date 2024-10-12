# DefaultApi

All URIs are relative to *https://stellastra.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postReviewPost**](DefaultApi.md#postReviewPost) | **POST** /post-review | Posts the user&#39;s review to Stellastra |


<a id="postReviewPost"></a>
# **postReviewPost**
> PostReviewPost200Response postReviewPost(userEmail, rating, postReviewPostRequest, userName)

Posts the user&#39;s review to Stellastra

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://stellastra.com/api");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String userEmail = "{\"user_email\":\"johnsmith@companyxyz.com\"}"; // String | User's email to which the review verification will be sent. 
    Integer rating = 1; // Integer | The user's star rating, must be a single integer from [1, 2, 3, 4, 5]
    PostReviewPostRequest postReviewPostRequest = new PostReviewPostRequest(); // PostReviewPostRequest | The request body requires the user_email and rating. The parameter use_name is optional. 
    String userName = "{\"user_name\":\"John\"}"; // String | The user's name, defaults to empty string \"\".  Thus, if this is omitted, the email to the user will not use the user's name. 
    try {
      PostReviewPost200Response result = apiInstance.postReviewPost(userEmail, rating, postReviewPostRequest, userName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#postReviewPost");
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
| **userEmail** | **String**| User&#39;s email to which the review verification will be sent.  | |
| **rating** | **Integer**| The user&#39;s star rating, must be a single integer from [1, 2, 3, 4, 5] | [enum: 1, 2, 3, 4, 5] |
| **postReviewPostRequest** | [**PostReviewPostRequest**](PostReviewPostRequest.md)| The request body requires the user_email and rating. The parameter use_name is optional.  | |
| **userName** | **String**| The user&#39;s name, defaults to empty string \&quot;\&quot;.  Thus, if this is omitted, the email to the user will not use the user&#39;s name.  | [optional] |

### Return type

[**PostReviewPost200Response**](PostReviewPost200Response.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A response code of 200 means the request was succesful, and the user has been sent an email confirming their review. |  -  |
| **400** | A status code of 400 is returned when a required parameter is mising, such as &#39;rating&#39; or &#39;user_email&#39;. |  -  |
| **401** | This can appear because the authorization header is missing or malformed, or because the auth email and key pair is not authorized. |  -  |
| **403** | The 403 response can have many detailed response messages related to the user&#39;s email address validation |  -  |

