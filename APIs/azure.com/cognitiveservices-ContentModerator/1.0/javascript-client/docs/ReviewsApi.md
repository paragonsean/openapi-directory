# ContentModeratorClient.ReviewsApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reviewsAddVideoFrame**](ReviewsApi.md#reviewsAddVideoFrame) | **POST** /contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}/frames | 
[**reviewsAddVideoTranscript**](ReviewsApi.md#reviewsAddVideoTranscript) | **PUT** /contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}/transcript | 
[**reviewsAddVideoTranscriptModerationResult**](ReviewsApi.md#reviewsAddVideoTranscriptModerationResult) | **PUT** /contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}/transcriptmoderationresult | 
[**reviewsCreateJob**](ReviewsApi.md#reviewsCreateJob) | **POST** /contentmoderator/review/v1.0/teams/{teamName}/jobs | 
[**reviewsCreateReviews**](ReviewsApi.md#reviewsCreateReviews) | **POST** /contentmoderator/review/v1.0/teams/{teamName}/reviews | 
[**reviewsGetJobDetails**](ReviewsApi.md#reviewsGetJobDetails) | **GET** /contentmoderator/review/v1.0/teams/{teamName}/jobs/{JobId} | 
[**reviewsGetReview**](ReviewsApi.md#reviewsGetReview) | **GET** /contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId} | 
[**reviewsGetVideoFrames**](ReviewsApi.md#reviewsGetVideoFrames) | **GET** /contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}/frames | 
[**reviewsPublishVideoReview**](ReviewsApi.md#reviewsPublishVideoReview) | **POST** /contentmoderator/review/v1.0/teams/{teamName}/reviews/{reviewId}/publish | 



## reviewsAddVideoFrame

> reviewsAddVideoFrame(teamName, reviewId, opts)



The reviews created would show up for Reviewers on your team. As Reviewers complete reviewing, results of the Review would be POSTED (i.e. HTTP POST) on the specified CallBackEndpoint.    &lt;h3&gt;CallBack Schemas &lt;/h3&gt;  &lt;h4&gt;Review Completion CallBack Sample&lt;/h4&gt;  &lt;p&gt;  {&lt;br/&gt;    \&quot;ReviewId\&quot;: \&quot;&lt;Review Id&gt;\&quot;,&lt;br/&gt;    \&quot;ModifiedOn\&quot;: \&quot;2016-10-11T22:36:32.9934851Z\&quot;,&lt;br/&gt;    \&quot;ModifiedBy\&quot;: \&quot;&lt;Name of the Reviewer&gt;\&quot;,&lt;br/&gt;    \&quot;CallBackType\&quot;: \&quot;Review\&quot;,&lt;br/&gt;    \&quot;ContentId\&quot;: \&quot;&lt;The ContentId that was specified input&gt;\&quot;,&lt;br/&gt;    \&quot;Metadata\&quot;: {&lt;br/&gt;      \&quot;adultscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;racyscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    },&lt;br/&gt;    \&quot;ReviewerResultTags\&quot;: {&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    }&lt;br/&gt;  }&lt;br/&gt;    &lt;/p&gt;.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ReviewsApi();
let teamName = "teamName_example"; // String | Your team name.
let reviewId = "reviewId_example"; // String | Id of the review.
let opts = {
  'timescale': 56 // Number | Timescale of the video you are adding frames to.
};
apiInstance.reviewsAddVideoFrame(teamName, reviewId, opts, (error, data, response) => {
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
 **teamName** | **String**| Your team name. | 
 **reviewId** | **String**| Id of the review. | 
 **timescale** | **Number**| Timescale of the video you are adding frames to. | [optional] 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reviewsAddVideoTranscript

> reviewsAddVideoTranscript(teamName, reviewId, contentType, vTTFile)



This API adds a transcript file (text version of all the words spoken in a video) to a video review. The file should be a valid WebVTT format.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ReviewsApi();
let teamName = "teamName_example"; // String | Your team name.
let reviewId = "reviewId_example"; // String | Id of the review.
let contentType = "contentType_example"; // String | The content type.
let vTTFile = {key: null}; // Object | Transcript file of the video.
apiInstance.reviewsAddVideoTranscript(teamName, reviewId, contentType, vTTFile, (error, data, response) => {
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
 **teamName** | **String**| Your team name. | 
 **reviewId** | **String**| Id of the review. | 
 **contentType** | **String**| The content type. | 
 **vTTFile** | **Object**| Transcript file of the video. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json


## reviewsAddVideoTranscriptModerationResult

> reviewsAddVideoTranscriptModerationResult(contentType, teamName, reviewId, transcriptModerationBody)



This API adds a transcript screen text result file for a video review. Transcript screen text result file is a result of Screen Text API . In order to generate transcript screen text result file , a transcript file has to be screened for profanity using Screen Text API.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ReviewsApi();
let contentType = "contentType_example"; // String | The content type.
let teamName = "teamName_example"; // String | Your team name.
let reviewId = "reviewId_example"; // String | Id of the review.
let transcriptModerationBody = [new ContentModeratorClient.ReviewsAddVideoTranscriptModerationResultRequestInner()]; // [ReviewsAddVideoTranscriptModerationResultRequestInner] | Body for add video transcript moderation result API
apiInstance.reviewsAddVideoTranscriptModerationResult(contentType, teamName, reviewId, transcriptModerationBody, (error, data, response) => {
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
 **contentType** | **String**| The content type. | 
 **teamName** | **String**| Your team name. | 
 **reviewId** | **String**| Id of the review. | 
 **transcriptModerationBody** | [**[ReviewsAddVideoTranscriptModerationResultRequestInner]**](ReviewsAddVideoTranscriptModerationResultRequestInner.md)| Body for add video transcript moderation result API | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reviewsCreateJob

> JobId reviewsCreateJob(teamName, contentType, contentId, workflowName, contentType2, content, opts)



A job Id will be returned for the content posted on this endpoint.     Once the content is evaluated against the Workflow provided the review will be created or ignored based on the workflow expression.    &lt;h3&gt;CallBack Schemas &lt;/h3&gt;    &lt;p&gt;  &lt;h4&gt;Job Completion CallBack Sample&lt;/h4&gt;&lt;br/&gt;    {&lt;br/&gt;    \&quot;JobId\&quot;: \&quot;&lt;Job Id&gt;,&lt;br/&gt;    \&quot;ReviewId\&quot;: \&quot;&lt;Review Id, if the Job resulted in a Review to be created&gt;\&quot;,&lt;br/&gt;    \&quot;WorkFlowId\&quot;: \&quot;default\&quot;,&lt;br/&gt;    \&quot;Status\&quot;: \&quot;&lt;This will be one of Complete, InProgress, Error&gt;\&quot;,&lt;br/&gt;    \&quot;ContentType\&quot;: \&quot;Image\&quot;,&lt;br/&gt;    \&quot;ContentId\&quot;: \&quot;&lt;This is the ContentId that was specified on input&gt;\&quot;,&lt;br/&gt;    \&quot;CallBackType\&quot;: \&quot;Job\&quot;,&lt;br/&gt;    \&quot;Metadata\&quot;: {&lt;br/&gt;      \&quot;adultscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;racyscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    }&lt;br/&gt;  }&lt;br/&gt;    &lt;/p&gt;  &lt;p&gt;  &lt;h4&gt;Review Completion CallBack Sample&lt;/h4&gt;&lt;br/&gt;    {    \&quot;ReviewId\&quot;: \&quot;&lt;Review Id&gt;\&quot;,&lt;br/&gt;    \&quot;ModifiedOn\&quot;: \&quot;2016-10-11T22:36:32.9934851Z\&quot;,&lt;br/&gt;    \&quot;ModifiedBy\&quot;: \&quot;&lt;Name of the Reviewer&gt;\&quot;,&lt;br/&gt;    \&quot;CallBackType\&quot;: \&quot;Review\&quot;,&lt;br/&gt;    \&quot;ContentId\&quot;: \&quot;&lt;The ContentId that was specified input&gt;\&quot;,&lt;br/&gt;    \&quot;Metadata\&quot;: {&lt;br/&gt;      \&quot;adultscore\&quot;: \&quot;0.xxx\&quot;,      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;racyscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    },&lt;br/&gt;    \&quot;ReviewerResultTags\&quot;: {&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    }&lt;br/&gt;  }&lt;br/&gt;    &lt;/p&gt;.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ReviewsApi();
let teamName = "teamName_example"; // String | Your team name.
let contentType = "contentType_example"; // String | Image, Text or Video.
let contentId = "contentId_example"; // String | Id/Name to identify the content submitted.
let workflowName = "workflowName_example"; // String | Workflow Name that you want to invoke.
let contentType2 = "contentType_example"; // String | The content type.
let content = new ContentModeratorClient.ReviewsCreateJobRequest(); // ReviewsCreateJobRequest | Content to evaluate.
let opts = {
  'callBackEndpoint': "callBackEndpoint_example" // String | Callback endpoint for posting the create job result.
};
apiInstance.reviewsCreateJob(teamName, contentType, contentId, workflowName, contentType2, content, opts, (error, data, response) => {
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
 **teamName** | **String**| Your team name. | 
 **contentType** | **String**| Image, Text or Video. | 
 **contentId** | **String**| Id/Name to identify the content submitted. | 
 **workflowName** | **String**| Workflow Name that you want to invoke. | 
 **contentType2** | **String**| The content type. | 
 **content** | [**ReviewsCreateJobRequest**](ReviewsCreateJobRequest.md)| Content to evaluate. | 
 **callBackEndpoint** | **String**| Callback endpoint for posting the create job result. | [optional] 

### Return type

[**JobId**](JobId.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json, image/jpeg
- **Accept**: application/json, text/json


## reviewsCreateReviews

> [String] reviewsCreateReviews(urlContentType, teamName, createReviewBody, opts)



The reviews created would show up for Reviewers on your team. As Reviewers complete reviewing, results of the Review would be POSTED (i.e. HTTP POST) on the specified CallBackEndpoint.    &lt;h3&gt;CallBack Schemas &lt;/h3&gt;  &lt;h4&gt;Review Completion CallBack Sample&lt;/h4&gt;  &lt;p&gt;  {&lt;br/&gt;    \&quot;ReviewId\&quot;: \&quot;&lt;Review Id&gt;\&quot;,&lt;br/&gt;    \&quot;ModifiedOn\&quot;: \&quot;2016-10-11T22:36:32.9934851Z\&quot;,&lt;br/&gt;    \&quot;ModifiedBy\&quot;: \&quot;&lt;Name of the Reviewer&gt;\&quot;,&lt;br/&gt;    \&quot;CallBackType\&quot;: \&quot;Review\&quot;,&lt;br/&gt;    \&quot;ContentId\&quot;: \&quot;&lt;The ContentId that was specified input&gt;\&quot;,&lt;br/&gt;    \&quot;Metadata\&quot;: {&lt;br/&gt;      \&quot;adultscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;racyscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    },&lt;br/&gt;    \&quot;ReviewerResultTags\&quot;: {&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    }&lt;br/&gt;  }&lt;br/&gt;    &lt;/p&gt;.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ReviewsApi();
let urlContentType = "urlContentType_example"; // String | The content type.
let teamName = "teamName_example"; // String | Your team name.
let createReviewBody = [new ContentModeratorClient.ReviewsCreateReviewsRequestInner()]; // [ReviewsCreateReviewsRequestInner] | Body for create reviews API
let opts = {
  'subTeam': "subTeam_example" // String | SubTeam of your team, you want to assign the created review to.
};
apiInstance.reviewsCreateReviews(urlContentType, teamName, createReviewBody, opts, (error, data, response) => {
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
 **urlContentType** | **String**| The content type. | 
 **teamName** | **String**| Your team name. | 
 **createReviewBody** | [**[ReviewsCreateReviewsRequestInner]**](ReviewsCreateReviewsRequestInner.md)| Body for create reviews API | 
 **subTeam** | **String**| SubTeam of your team, you want to assign the created review to. | [optional] 

### Return type

**[String]**

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reviewsGetJobDetails

> Job reviewsGetJobDetails(teamName, jobId)



Get the Job Details for a Job Id.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ReviewsApi();
let teamName = "teamName_example"; // String | Your Team Name.
let jobId = "jobId_example"; // String | Id of the job.
apiInstance.reviewsGetJobDetails(teamName, jobId, (error, data, response) => {
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
 **teamName** | **String**| Your Team Name. | 
 **jobId** | **String**| Id of the job. | 

### Return type

[**Job**](Job.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reviewsGetReview

> Review reviewsGetReview(teamName, reviewId)



Returns review details for the review Id passed.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ReviewsApi();
let teamName = "teamName_example"; // String | Your Team Name.
let reviewId = "reviewId_example"; // String | Id of the review.
apiInstance.reviewsGetReview(teamName, reviewId, (error, data, response) => {
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
 **teamName** | **String**| Your Team Name. | 
 **reviewId** | **String**| Id of the review. | 

### Return type

[**Review**](Review.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reviewsGetVideoFrames

> Frames reviewsGetVideoFrames(teamName, reviewId, opts)



The reviews created would show up for Reviewers on your team. As Reviewers complete reviewing, results of the Review would be POSTED (i.e. HTTP POST) on the specified CallBackEndpoint.    &lt;h3&gt;CallBack Schemas &lt;/h3&gt;  &lt;h4&gt;Review Completion CallBack Sample&lt;/h4&gt;  &lt;p&gt;  {&lt;br/&gt;    \&quot;ReviewId\&quot;: \&quot;&lt;Review Id&gt;\&quot;,&lt;br/&gt;    \&quot;ModifiedOn\&quot;: \&quot;2016-10-11T22:36:32.9934851Z\&quot;,&lt;br/&gt;    \&quot;ModifiedBy\&quot;: \&quot;&lt;Name of the Reviewer&gt;\&quot;,&lt;br/&gt;    \&quot;CallBackType\&quot;: \&quot;Review\&quot;,&lt;br/&gt;    \&quot;ContentId\&quot;: \&quot;&lt;The ContentId that was specified input&gt;\&quot;,&lt;br/&gt;    \&quot;Metadata\&quot;: {&lt;br/&gt;      \&quot;adultscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;racyscore\&quot;: \&quot;0.xxx\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    },&lt;br/&gt;    \&quot;ReviewerResultTags\&quot;: {&lt;br/&gt;      \&quot;a\&quot;: \&quot;False\&quot;,&lt;br/&gt;      \&quot;r\&quot;: \&quot;True\&quot;&lt;br/&gt;    }&lt;br/&gt;  }&lt;br/&gt;    &lt;/p&gt;.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ReviewsApi();
let teamName = "teamName_example"; // String | Your team name.
let reviewId = "reviewId_example"; // String | Id of the review.
let opts = {
  'startSeed': 56, // Number | Time stamp of the frame from where you want to start fetching the frames.
  'noOfRecords': 56, // Number | Number of frames to fetch.
  'filter': "filter_example" // String | Get frames filtered by tags.
};
apiInstance.reviewsGetVideoFrames(teamName, reviewId, opts, (error, data, response) => {
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
 **teamName** | **String**| Your team name. | 
 **reviewId** | **String**| Id of the review. | 
 **startSeed** | **Number**| Time stamp of the frame from where you want to start fetching the frames. | [optional] 
 **noOfRecords** | **Number**| Number of frames to fetch. | [optional] 
 **filter** | **String**| Get frames filtered by tags. | [optional] 

### Return type

[**Frames**](Frames.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reviewsPublishVideoReview

> reviewsPublishVideoReview(teamName, reviewId)



Publish video review to make it available for review.

### Example

```javascript
import ContentModeratorClient from 'content_moderator_client';
let defaultClient = ContentModeratorClient.ApiClient.instance;
// Configure API key authorization: apim_key
let apim_key = defaultClient.authentications['apim_key'];
apim_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apim_key.apiKeyPrefix = 'Token';

let apiInstance = new ContentModeratorClient.ReviewsApi();
let teamName = "teamName_example"; // String | Your team name.
let reviewId = "reviewId_example"; // String | Id of the review.
apiInstance.reviewsPublishVideoReview(teamName, reviewId, (error, data, response) => {
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
 **teamName** | **String**| Your team name. | 
 **reviewId** | **String**| Id of the review. | 

### Return type

null (empty response body)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

