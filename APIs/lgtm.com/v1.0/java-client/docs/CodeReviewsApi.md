# CodeReviewsApi

All URIs are relative to *https://lgtm.com/api/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCodeReview**](CodeReviewsApi.md#getCodeReview) | **GET** /codereviews/{review-id} | Get results of code review |
| [**requestReview**](CodeReviewsApi.md#requestReview) | **POST** /codereviews/{project-id} | Run code review for a patch |


<a id="getCodeReview"></a>
# **getCodeReview**
> List&lt;CodeReview&gt; getCodeReview(reviewId)

Get results of code review

Get the results of a code review using the review identifier for the task.  When you request a code review, the response includes a task result URL of the form: &#x60;/codereviews/{review-id}&#x60;.  This endpoint reports the results of a complete code review, or the status of a review  that&#39;s still in progress. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodeReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://lgtm.com/api/v1.0");
    
    // Configure HTTP bearer authorization: access-token
    HttpBearerAuth access-token = (HttpBearerAuth) defaultClient.getAuthentication("access-token");
    access-token.setBearerToken("BEARER TOKEN");

    CodeReviewsApi apiInstance = new CodeReviewsApi(defaultClient);
    String reviewId = "reviewId_example"; // String | The identifier for the review (from the `task-result-url`).
    try {
      List<CodeReview> result = apiInstance.getCodeReview(reviewId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodeReviewsApi#getCodeReview");
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
| **reviewId** | **String**| The identifier for the review (from the &#x60;task-result-url&#x60;). | |

### Return type

[**List&lt;CodeReview&gt;**](CodeReview.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. Requested data returned. |  -  |

<a id="requestReview"></a>
# **requestReview**
> Operation requestReview(projectId, base, externalId, body, reviewUrl, callbackUrl, callbackSecret)

Run code review for a patch

Trigger the code review of a patch. This is available for projects with Git repositories.  Your request must include:    * Identifier for the base commit   * Patch generated using &#x60;git diff --binary&#x60; (see [git diff](https://git-scm.com/docs/git-diff))   * Header &#x60;Content-Type: application/octet-stream&#x60;   * For both LGTM.com and LGTM Enterprise, an access token with the &#x60;codereviews:write&#x60; scope  Note that if you make a request using Curl, you&#39;ll also need to add &#x60;--data-binary&#x60; to the request to ensure that the patch you supply in the body is sent with newlines unchanged. You can track the progress of the review using the task result URL returned on creation of the task, or by calling the &#x60;/operations&#x60; endpoint with the operations identifier returned by the request. For more information, see [Get operation status](https://lgtm.com/help/lgtm/api/api-v1#opIdgetOperation). Alternatively, if you supply a callback URL you&#39;ll get a post-back automatically on completion of the review.  When the review is complete, you can access the results using the task result URL. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CodeReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://lgtm.com/api/v1.0");
    
    // Configure HTTP bearer authorization: access-token
    HttpBearerAuth access-token = (HttpBearerAuth) defaultClient.getAuthentication("access-token");
    access-token.setBearerToken("BEARER TOKEN");

    CodeReviewsApi apiInstance = new CodeReviewsApi(defaultClient);
    Long projectId = 56L; // Long | The numeric project identifier.
    String base = "base_example"; // String | The identifier for the base commit.
    Integer externalId = integer; // Integer | Your reference number for the code review.
    File body = The contents of a binary patch file; // File | The patch containing the code changes for review.
    String reviewUrl = "reviewUrl_example"; // String | An informative back-link to an external system.
    String callbackUrl = "callbackUrl_example"; // String | The callback URL for LGTM to post to on completion of the review. When the code review is complete, the API sends an HTTP POST request to the callback URL with the result of the code review in the request body. The code review results in the request body are identical to the results accessed through the [`/codereviews/{review-id}`](https://lgtm.com/help/lgtm/api/api-v1#opIdgetCodeReview) end-point. If you specify a `callback-secret`, the request also includes an `x-lgtm-signature` header with a digital signature of the request's contents. 
    String callbackSecret = "callbackSecret_example"; // String | The `callback-secret` is used to compute a signature which is included in the `x-lgtm-signature` header of the callback response. The receiver of the callback can check the validity of the response by computing the signature using HMAC-SHA1 and verifying that it matches the `x-lgtm-signature` header value. The HMAC algorithm requires byte sequences as inputs for both the secret and the message. The callback secret string must be converted to bytes using UTF-8 encoding. The response body should ideally be read as a plain byte sequence. Conversion to, for example a JSON object, and back to a byte sequence might change the formatting, and would invalidate the signature. 
    try {
      Operation result = apiInstance.requestReview(projectId, base, externalId, body, reviewUrl, callbackUrl, callbackSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CodeReviewsApi#requestReview");
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
| **projectId** | **Long**| The numeric project identifier. | |
| **base** | **String**| The identifier for the base commit. | |
| **externalId** | **Integer**| Your reference number for the code review. | |
| **body** | **File**| The patch containing the code changes for review. | |
| **reviewUrl** | **String**| An informative back-link to an external system. | [optional] |
| **callbackUrl** | **String**| The callback URL for LGTM to post to on completion of the review. When the code review is complete, the API sends an HTTP POST request to the callback URL with the result of the code review in the request body. The code review results in the request body are identical to the results accessed through the [&#x60;/codereviews/{review-id}&#x60;](https://lgtm.com/help/lgtm/api/api-v1#opIdgetCodeReview) end-point. If you specify a &#x60;callback-secret&#x60;, the request also includes an &#x60;x-lgtm-signature&#x60; header with a digital signature of the request&#39;s contents.  | [optional] |
| **callbackSecret** | **String**| The &#x60;callback-secret&#x60; is used to compute a signature which is included in the &#x60;x-lgtm-signature&#x60; header of the callback response. The receiver of the callback can check the validity of the response by computing the signature using HMAC-SHA1 and verifying that it matches the &#x60;x-lgtm-signature&#x60; header value. The HMAC algorithm requires byte sequences as inputs for both the secret and the message. The callback secret string must be converted to bytes using UTF-8 encoding. The response body should ideally be read as a plain byte sequence. Conversion to, for example a JSON object, and back to a byte sequence might change the formatting, and would invalidate the signature.  | [optional] |

### Return type

[**Operation**](Operation.md)

### Authorization

[access-token](../README.md#access-token)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted. Code review triggered. Tracking data returned. |  -  |

