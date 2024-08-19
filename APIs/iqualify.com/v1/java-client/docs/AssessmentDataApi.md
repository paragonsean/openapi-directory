# AssessmentDataApi

All URIs are relative to *https://api.iqualify.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**offeringsOfferingIdAnalyticsActivitiesResponsesGet**](AssessmentDataApi.md#offeringsOfferingIdAnalyticsActivitiesResponsesGet) | **GET** /offerings/{offeringId}/analytics/activities/responses | Find open response activity attempts |
| [**offeringsOfferingIdAnalyticsMarksAssignmentsGet**](AssessmentDataApi.md#offeringsOfferingIdAnalyticsMarksAssignmentsGet) | **GET** /offerings/{offeringId}/analytics/marks/assignments | Find assessment marks |
| [**offeringsOfferingIdAnalyticsMarksQuizzesGet**](AssessmentDataApi.md#offeringsOfferingIdAnalyticsMarksQuizzesGet) | **GET** /offerings/{offeringId}/analytics/marks/quizzes | Find quiz marks |
| [**offeringsOfferingIdAnalyticsSubmissionsAssignmentsGet**](AssessmentDataApi.md#offeringsOfferingIdAnalyticsSubmissionsAssignmentsGet) | **GET** /offerings/{offeringId}/analytics/submissions/assignments | Find submissions to assessments, including marks if any |
| [**offeringsOfferingIdAnalyticsSubmissionsOpenResponseAssessmentIdGet**](AssessmentDataApi.md#offeringsOfferingIdAnalyticsSubmissionsOpenResponseAssessmentIdGet) | **GET** /offerings/{offeringId}/analytics/submissions/open-response/{assessmentId} | Find submissions to a specified open response assessment, including marks if any |
| [**offeringsOfferingIdAnalyticsSubmissionsUserEmailAssignmentsAssessmentIdGet**](AssessmentDataApi.md#offeringsOfferingIdAnalyticsSubmissionsUserEmailAssignmentsAssessmentIdGet) | **GET** /offerings/{offeringId}/analytics/submissions/{userEmail}/assignments/{assessmentId} | Find a learner&#39;s submission to a specified assessment, including marks if any |


<a id="offeringsOfferingIdAnalyticsActivitiesResponsesGet"></a>
# **offeringsOfferingIdAnalyticsActivitiesResponsesGet**
> List&lt;ActivityAttemptOpenResponse&gt; offeringsOfferingIdAnalyticsActivitiesResponsesGet(offeringId)

Find open response activity attempts

Responds with all learner activity attempts for open response activities in an offering matching the offeringId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentDataApi apiInstance = new AssessmentDataApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    try {
      List<ActivityAttemptOpenResponse> result = apiInstance.offeringsOfferingIdAnalyticsActivitiesResponsesGet(offeringId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentDataApi#offeringsOfferingIdAnalyticsActivitiesResponsesGet");
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
| **offeringId** | **String**| offering&#39;s id | |

### Return type

[**List&lt;ActivityAttemptOpenResponse&gt;**](ActivityAttemptOpenResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Offering activity attempt open responses |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdAnalyticsMarksAssignmentsGet"></a>
# **offeringsOfferingIdAnalyticsMarksAssignmentsGet**
> List&lt;AssignmentMarkResponse&gt; offeringsOfferingIdAnalyticsMarksAssignmentsGet(offeringId)

Find assessment marks

Responds with all learner assessment marks in an offering matching the offeringId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentDataApi apiInstance = new AssessmentDataApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    try {
      List<AssignmentMarkResponse> result = apiInstance.offeringsOfferingIdAnalyticsMarksAssignmentsGet(offeringId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentDataApi#offeringsOfferingIdAnalyticsMarksAssignmentsGet");
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
| **offeringId** | **String**| offering&#39;s id | |

### Return type

[**List&lt;AssignmentMarkResponse&gt;**](AssignmentMarkResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Assignments marks |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdAnalyticsMarksQuizzesGet"></a>
# **offeringsOfferingIdAnalyticsMarksQuizzesGet**
> List&lt;QuizMarkResponse&gt; offeringsOfferingIdAnalyticsMarksQuizzesGet(offeringId)

Find quiz marks

Responds with all learner quiz marks in an offering matching the offeringId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentDataApi apiInstance = new AssessmentDataApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    try {
      List<QuizMarkResponse> result = apiInstance.offeringsOfferingIdAnalyticsMarksQuizzesGet(offeringId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentDataApi#offeringsOfferingIdAnalyticsMarksQuizzesGet");
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
| **offeringId** | **String**| offering&#39;s id | |

### Return type

[**List&lt;QuizMarkResponse&gt;**](QuizMarkResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Quizzes marks |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdAnalyticsSubmissionsAssignmentsGet"></a>
# **offeringsOfferingIdAnalyticsSubmissionsAssignmentsGet**
> List&lt;AssignmentMarkResponse&gt; offeringsOfferingIdAnalyticsSubmissionsAssignmentsGet(offeringId)

Find submissions to assessments, including marks if any

Responds with all learner assessment submissions and marks, if any, in an offering matching the offeringId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentDataApi apiInstance = new AssessmentDataApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    try {
      List<AssignmentMarkResponse> result = apiInstance.offeringsOfferingIdAnalyticsSubmissionsAssignmentsGet(offeringId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentDataApi#offeringsOfferingIdAnalyticsSubmissionsAssignmentsGet");
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
| **offeringId** | **String**| offering&#39;s id | |

### Return type

[**List&lt;AssignmentMarkResponse&gt;**](AssignmentMarkResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Assignments submissions |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdAnalyticsSubmissionsOpenResponseAssessmentIdGet"></a>
# **offeringsOfferingIdAnalyticsSubmissionsOpenResponseAssessmentIdGet**
> List&lt;SubmissionMarkResponse&gt; offeringsOfferingIdAnalyticsSubmissionsOpenResponseAssessmentIdGet(offeringId, assessmentId)

Find submissions to a specified open response assessment, including marks if any

Responds with all learner assessment submissions and marks, if any, in a specified open response assessment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentDataApi apiInstance = new AssessmentDataApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String assessmentId = "assessmentId_example"; // String | assessment's id
    try {
      List<SubmissionMarkResponse> result = apiInstance.offeringsOfferingIdAnalyticsSubmissionsOpenResponseAssessmentIdGet(offeringId, assessmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentDataApi#offeringsOfferingIdAnalyticsSubmissionsOpenResponseAssessmentIdGet");
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
| **offeringId** | **String**| offering&#39;s id | |
| **assessmentId** | **String**| assessment&#39;s id | |

### Return type

[**List&lt;SubmissionMarkResponse&gt;**](SubmissionMarkResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Responds with assignment submissions for the specified assignment. |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdAnalyticsSubmissionsUserEmailAssignmentsAssessmentIdGet"></a>
# **offeringsOfferingIdAnalyticsSubmissionsUserEmailAssignmentsAssessmentIdGet**
> List&lt;SubmissionMarkResponse&gt; offeringsOfferingIdAnalyticsSubmissionsUserEmailAssignmentsAssessmentIdGet(offeringId, userEmail, assessmentId)

Find a learner&#39;s submission to a specified assessment, including marks if any

Responds with the learner&#39;s assessment submission and any marks for the submission.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentDataApi apiInstance = new AssessmentDataApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String userEmail = "userEmail_example"; // String | user's email
    String assessmentId = "assessmentId_example"; // String | assessment's id
    try {
      List<SubmissionMarkResponse> result = apiInstance.offeringsOfferingIdAnalyticsSubmissionsUserEmailAssignmentsAssessmentIdGet(offeringId, userEmail, assessmentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentDataApi#offeringsOfferingIdAnalyticsSubmissionsUserEmailAssignmentsAssessmentIdGet");
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
| **offeringId** | **String**| offering&#39;s id | |
| **userEmail** | **String**| user&#39;s email | |
| **assessmentId** | **String**| assessment&#39;s id | |

### Return type

[**List&lt;SubmissionMarkResponse&gt;**](SubmissionMarkResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Responds with the learner&#39;s assessment submission and any marks for the submission. |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

