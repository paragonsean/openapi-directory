# ReviewsApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reviewsAddVideoFrame**](ReviewsApi.md#reviewsAddVideoFrame) | **POST** /contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}/frames |  |
| [**reviewsAddVideoTranscript**](ReviewsApi.md#reviewsAddVideoTranscript) | **PUT** /contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}/transcript |  |
| [**reviewsAddVideoTranscriptModerationResult**](ReviewsApi.md#reviewsAddVideoTranscriptModerationResult) | **PUT** /contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}/transcriptmoderationresult |  |
| [**reviewsCreateJob**](ReviewsApi.md#reviewsCreateJob) | **POST** /contentmoderator/review/v1.0/teams/{teamName}/jobs |  |
| [**reviewsCreateReviews**](ReviewsApi.md#reviewsCreateReviews) | **POST** /contentmoderator/review/v1.0/teams/{teamName}/reviews |  |
| [**reviewsGetJobDetails**](ReviewsApi.md#reviewsGetJobDetails) | **GET** /contentmoderator/review/v1.0/teams/{teamName}/jobs/{JobId} |  |
| [**reviewsGetReview**](ReviewsApi.md#reviewsGetReview) | **GET** /contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId} |  |
| [**reviewsGetVideoFrames**](ReviewsApi.md#reviewsGetVideoFrames) | **GET** /contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}/frames |  |
| [**reviewsPublishVideoReview**](ReviewsApi.md#reviewsPublishVideoReview) | **POST** /contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}/publish |  |


<a id="reviewsAddVideoFrame"></a>
# **reviewsAddVideoFrame**
> reviewsAddVideoFrame(teamName, reviewId, timescale)



The reviews created would show up for Reviewers on your team. As Reviewers complete reviewing, results of the Review would be POSTED (i.e. HTTP POST) on the specified CallBackEndpoint.    &lt;h3&gt;CallBack Schemas &lt;/h3&gt;  &lt;h4&gt;Review Completion CallBack Sample&lt;/h4&gt;  &lt;p&gt;  {&lt;br/&gt;    \&quot;ReviewId\&quot;: \&quot;&lt;Review Id&gt;\&quot;,&lt;br/&gt;    \&quot;ModifiedOn\&quot;: \&quot;2016-10-11T22:36:32.9934851Z\&quot;,&lt;br/&gt;    \&quot;ModifiedBy\&quot;: \&quot;&lt;Name of the Reviewer&gt;\&quot;,&lt;br/&gt;    \&quot;CallBackType\&quot;: \&quot;Review\&quot;,&lt;br/&gt;    \&quot;ContentId\&quot;: \&quot;&lt;The ContentId that was specified input&gt;\&quot;,&lt;br/&gt;    \&quot;Metadata\&quot;: {&lt;br/&gt;      \&quot;adultscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;racyscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    },&lt;br/&gt;    \&quot;ReviewerResultTags\&quot;: {&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    }&lt;br/&gt;  }&lt;br/&gt;    &lt;/p&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ReviewsApi apiInstance = new ReviewsApi(defaultClient);
    String teamName = "teamName_example"; // String | Your team name.
    String reviewId = "reviewId_example"; // String | Id of the review.
    Integer timescale = 56; // Integer | Timescale of the video you are adding frames to.
    try {
      apiInstance.reviewsAddVideoFrame(teamName, reviewId, timescale);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewsApi#reviewsAddVideoFrame");
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
| **teamName** | **String**| Your team name. | |
| **reviewId** | **String**| Id of the review. | |
| **timescale** | **Integer**| Timescale of the video you are adding frames to. | [optional] |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response. |  -  |

<a id="reviewsAddVideoTranscript"></a>
# **reviewsAddVideoTranscript**
> reviewsAddVideoTranscript(teamName, reviewId, contentType, vtTFile)



This API adds a transcript file (text version of all the words spoken in a video) to a video review. The file should be a valid WebVTT format.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ReviewsApi apiInstance = new ReviewsApi(defaultClient);
    String teamName = "teamName_example"; // String | Your team name.
    String reviewId = "reviewId_example"; // String | Id of the review.
    String contentType = "text/plain"; // String | The content type.
    Object vtTFile = null; // Object | Transcript file of the video.
    try {
      apiInstance.reviewsAddVideoTranscript(teamName, reviewId, contentType, vtTFile);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewsApi#reviewsAddVideoTranscript");
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
| **teamName** | **String**| Your team name. | |
| **reviewId** | **String**| Id of the review. | |
| **contentType** | **String**| The content type. | [enum: text/plain] |
| **vtTFile** | **Object**| Transcript file of the video. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error response. |  -  |

<a id="reviewsAddVideoTranscriptModerationResult"></a>
# **reviewsAddVideoTranscriptModerationResult**
> reviewsAddVideoTranscriptModerationResult(contentType, teamName, reviewId, transcriptModerationBody)



This API adds a transcript screen text result file for a video review. Transcript screen text result file is a result of Screen Text API . In order to generate transcript screen text result file , a transcript file has to be screened for profanity using Screen Text API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ReviewsApi apiInstance = new ReviewsApi(defaultClient);
    String contentType = "contentType_example"; // String | The content type.
    String teamName = "teamName_example"; // String | Your team name.
    String reviewId = "reviewId_example"; // String | Id of the review.
    List<ReviewsAddVideoTranscriptModerationResultRequestInner> transcriptModerationBody = Arrays.asList(); // List<ReviewsAddVideoTranscriptModerationResultRequestInner> | Body for add video transcript moderation result API
    try {
      apiInstance.reviewsAddVideoTranscriptModerationResult(contentType, teamName, reviewId, transcriptModerationBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewsApi#reviewsAddVideoTranscriptModerationResult");
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
| **contentType** | **String**| The content type. | |
| **teamName** | **String**| Your team name. | |
| **reviewId** | **String**| Id of the review. | |
| **transcriptModerationBody** | [**List&lt;ReviewsAddVideoTranscriptModerationResultRequestInner&gt;**](ReviewsAddVideoTranscriptModerationResultRequestInner.md)| Body for add video transcript moderation result API | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error response. |  -  |

<a id="reviewsCreateJob"></a>
# **reviewsCreateJob**
> JobId reviewsCreateJob(teamName, contentType, contentId, workflowName, contentType2, content, callBackEndpoint)



A job Id will be returned for the content posted on this endpoint.     Once the content is evaluated against the Workflow provided the review will be created or ignored based on the workflow expression.    &lt;h3&gt;CallBack Schemas &lt;/h3&gt;    &lt;p&gt;  &lt;h4&gt;Job Completion CallBack Sample&lt;/h4&gt;&lt;br/&gt;    {&lt;br/&gt;    \&quot;JobId\&quot;: \&quot;&lt;Job Id&gt;,&lt;br/&gt;    \&quot;ReviewId\&quot;: \&quot;&lt;Review Id, if the Job resulted in a Review to be created&gt;\&quot;,&lt;br/&gt;    \&quot;WorkFlowId\&quot;: \&quot;default\&quot;,&lt;br/&gt;    \&quot;Status\&quot;: \&quot;&lt;This will be one of Complete, InProgress, Error&gt;\&quot;,&lt;br/&gt;    \&quot;ContentType\&quot;: \&quot;Image\&quot;,&lt;br/&gt;    \&quot;ContentId\&quot;: \&quot;&lt;This is the ContentId that was specified on input&gt;\&quot;,&lt;br/&gt;    \&quot;CallBackType\&quot;: \&quot;Job\&quot;,&lt;br/&gt;    \&quot;Metadata\&quot;: {&lt;br/&gt;      \&quot;adultscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;racyscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    }&lt;br/&gt;  }&lt;br/&gt;    &lt;/p&gt;  &lt;p&gt;  &lt;h4&gt;Review Completion CallBack Sample&lt;/h4&gt;&lt;br/&gt;    {    \&quot;ReviewId\&quot;: \&quot;&lt;Review Id&gt;\&quot;,&lt;br/&gt;    \&quot;ModifiedOn\&quot;: \&quot;2016-10-11T22:36:32.9934851Z\&quot;,&lt;br/&gt;    \&quot;ModifiedBy\&quot;: \&quot;&lt;Name of the Reviewer&gt;\&quot;,&lt;br/&gt;    \&quot;CallBackType\&quot;: \&quot;Review\&quot;,&lt;br/&gt;    \&quot;ContentId\&quot;: \&quot;&lt;The ContentId that was specified input&gt;\&quot;,&lt;br/&gt;    \&quot;Metadata\&quot;: {&lt;br/&gt;      \&quot;adultscore\&quot;: \&quot;0.xxx\&quot;,      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;racyscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    },&lt;br/&gt;    \&quot;ReviewerResultTags\&quot;: {&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    }&lt;br/&gt;  }&lt;br/&gt;    &lt;/p&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ReviewsApi apiInstance = new ReviewsApi(defaultClient);
    String teamName = "teamName_example"; // String | Your team name.
    String contentType = "Image"; // String | Image, Text or Video.
    String contentId = "contentId_example"; // String | Id/Name to identify the content submitted.
    String workflowName = "workflowName_example"; // String | Workflow Name that you want to invoke.
    String contentType2 = "application/json"; // String | The content type.
    ReviewsCreateJobRequest content = new ReviewsCreateJobRequest(); // ReviewsCreateJobRequest | Content to evaluate.
    String callBackEndpoint = "callBackEndpoint_example"; // String | Callback endpoint for posting the create job result.
    try {
      JobId result = apiInstance.reviewsCreateJob(teamName, contentType, contentId, workflowName, contentType2, content, callBackEndpoint);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewsApi#reviewsCreateJob");
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
| **teamName** | **String**| Your team name. | |
| **contentType** | **String**| Image, Text or Video. | [enum: Image, Text, Video] |
| **contentId** | **String**| Id/Name to identify the content submitted. | |
| **workflowName** | **String**| Workflow Name that you want to invoke. | |
| **contentType2** | **String**| The content type. | [enum: application/json, image/jpeg] |
| **content** | [**ReviewsCreateJobRequest**](ReviewsCreateJobRequest.md)| Content to evaluate. | |
| **callBackEndpoint** | **String**| Callback endpoint for posting the create job result. | [optional] |

### Return type

[**JobId**](JobId.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json, image/jpeg
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response. |  -  |

<a id="reviewsCreateReviews"></a>
# **reviewsCreateReviews**
> List&lt;String&gt; reviewsCreateReviews(urlContentType, teamName, createReviewBody, subTeam)



The reviews created would show up for Reviewers on your team. As Reviewers complete reviewing, results of the Review would be POSTED (i.e. HTTP POST) on the specified CallBackEndpoint.    &lt;h3&gt;CallBack Schemas &lt;/h3&gt;  &lt;h4&gt;Review Completion CallBack Sample&lt;/h4&gt;  &lt;p&gt;  {&lt;br/&gt;    \&quot;ReviewId\&quot;: \&quot;&lt;Review Id&gt;\&quot;,&lt;br/&gt;    \&quot;ModifiedOn\&quot;: \&quot;2016-10-11T22:36:32.9934851Z\&quot;,&lt;br/&gt;    \&quot;ModifiedBy\&quot;: \&quot;&lt;Name of the Reviewer&gt;\&quot;,&lt;br/&gt;    \&quot;CallBackType\&quot;: \&quot;Review\&quot;,&lt;br/&gt;    \&quot;ContentId\&quot;: \&quot;&lt;The ContentId that was specified input&gt;\&quot;,&lt;br/&gt;    \&quot;Metadata\&quot;: {&lt;br/&gt;      \&quot;adultscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;racyscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    },&lt;br/&gt;    \&quot;ReviewerResultTags\&quot;: {&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    }&lt;br/&gt;  }&lt;br/&gt;    &lt;/p&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ReviewsApi apiInstance = new ReviewsApi(defaultClient);
    String urlContentType = "urlContentType_example"; // String | The content type.
    String teamName = "teamName_example"; // String | Your team name.
    List<ReviewsCreateReviewsRequestInner> createReviewBody = Arrays.asList(); // List<ReviewsCreateReviewsRequestInner> | Body for create reviews API
    String subTeam = "subTeam_example"; // String | SubTeam of your team, you want to assign the created review to.
    try {
      List<String> result = apiInstance.reviewsCreateReviews(urlContentType, teamName, createReviewBody, subTeam);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewsApi#reviewsCreateReviews");
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
| **urlContentType** | **String**| The content type. | |
| **teamName** | **String**| Your team name. | |
| **createReviewBody** | [**List&lt;ReviewsCreateReviewsRequestInner&gt;**](ReviewsCreateReviewsRequestInner.md)| Body for create reviews API | |
| **subTeam** | **String**| SubTeam of your team, you want to assign the created review to. | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response. |  -  |

<a id="reviewsGetJobDetails"></a>
# **reviewsGetJobDetails**
> Job reviewsGetJobDetails(teamName, jobId)



Get the Job Details for a Job Id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ReviewsApi apiInstance = new ReviewsApi(defaultClient);
    String teamName = "teamName_example"; // String | Your Team Name.
    String jobId = "jobId_example"; // String | Id of the job.
    try {
      Job result = apiInstance.reviewsGetJobDetails(teamName, jobId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewsApi#reviewsGetJobDetails");
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
| **teamName** | **String**| Your Team Name. | |
| **jobId** | **String**| Id of the job. | |

### Return type

[**Job**](Job.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response. |  -  |

<a id="reviewsGetReview"></a>
# **reviewsGetReview**
> Review reviewsGetReview(teamName, reviewId)



Returns review details for the review Id passed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ReviewsApi apiInstance = new ReviewsApi(defaultClient);
    String teamName = "teamName_example"; // String | Your Team Name.
    String reviewId = "reviewId_example"; // String | Id of the review.
    try {
      Review result = apiInstance.reviewsGetReview(teamName, reviewId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewsApi#reviewsGetReview");
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
| **teamName** | **String**| Your Team Name. | |
| **reviewId** | **String**| Id of the review. | |

### Return type

[**Review**](Review.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response. |  -  |

<a id="reviewsGetVideoFrames"></a>
# **reviewsGetVideoFrames**
> Frames reviewsGetVideoFrames(teamName, reviewId, startSeed, noOfRecords, filter)



The reviews created would show up for Reviewers on your team. As Reviewers complete reviewing, results of the Review would be POSTED (i.e. HTTP POST) on the specified CallBackEndpoint.    &lt;h3&gt;CallBack Schemas &lt;/h3&gt;  &lt;h4&gt;Review Completion CallBack Sample&lt;/h4&gt;  &lt;p&gt;  {&lt;br/&gt;    \&quot;ReviewId\&quot;: \&quot;&lt;Review Id&gt;\&quot;,&lt;br/&gt;    \&quot;ModifiedOn\&quot;: \&quot;2016-10-11T22:36:32.9934851Z\&quot;,&lt;br/&gt;    \&quot;ModifiedBy\&quot;: \&quot;&lt;Name of the Reviewer&gt;\&quot;,&lt;br/&gt;    \&quot;CallBackType\&quot;: \&quot;Review\&quot;,&lt;br/&gt;    \&quot;ContentId\&quot;: \&quot;&lt;The ContentId that was specified input&gt;\&quot;,&lt;br/&gt;    \&quot;Metadata\&quot;: {&lt;br/&gt;      \&quot;adultscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;racyscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    },&lt;br/&gt;    \&quot;ReviewerResultTags\&quot;: {&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    }&lt;br/&gt;  }&lt;br/&gt;    &lt;/p&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ReviewsApi apiInstance = new ReviewsApi(defaultClient);
    String teamName = "teamName_example"; // String | Your team name.
    String reviewId = "reviewId_example"; // String | Id of the review.
    Integer startSeed = 56; // Integer | Time stamp of the frame from where you want to start fetching the frames.
    Integer noOfRecords = 56; // Integer | Number of frames to fetch.
    String filter = "filter_example"; // String | Get frames filtered by tags.
    try {
      Frames result = apiInstance.reviewsGetVideoFrames(teamName, reviewId, startSeed, noOfRecords, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewsApi#reviewsGetVideoFrames");
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
| **teamName** | **String**| Your team name. | |
| **reviewId** | **String**| Id of the review. | |
| **startSeed** | **Integer**| Time stamp of the frame from where you want to start fetching the frames. | [optional] |
| **noOfRecords** | **Integer**| Number of frames to fetch. | [optional] |
| **filter** | **String**| Get frames filtered by tags. | [optional] |

### Return type

[**Frames**](Frames.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response. |  -  |

<a id="reviewsPublishVideoReview"></a>
# **reviewsPublishVideoReview**
> reviewsPublishVideoReview(teamName, reviewId)



Publish video review to make it available for review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    ReviewsApi apiInstance = new ReviewsApi(defaultClient);
    String teamName = "teamName_example"; // String | Your team name.
    String reviewId = "reviewId_example"; // String | Id of the review.
    try {
      apiInstance.reviewsPublishVideoReview(teamName, reviewId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewsApi#reviewsPublishVideoReview");
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
| **teamName** | **String**| Your team name. | |
| **reviewId** | **String**| Id of the review. | |

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | Error response. |  -  |

