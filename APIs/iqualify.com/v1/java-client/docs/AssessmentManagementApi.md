# AssessmentManagementApi

All URIs are relative to *https://api.iqualify.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**offeringsOfferingIdActivitiesOpenresponseGet**](AssessmentManagementApi.md#offeringsOfferingIdActivitiesOpenresponseGet) | **GET** /offerings/{offeringId}/activities/openresponse | Find offering&#39;s activities |
| [**offeringsOfferingIdAssessmentsAssessmentIdDocumentsDocumentIdDelete**](AssessmentManagementApi.md#offeringsOfferingIdAssessmentsAssessmentIdDocumentsDocumentIdDelete) | **DELETE** /offerings/{offeringId}/assessments/{assessmentId}/documents/{documentId} | Remove assessment document |
| [**offeringsOfferingIdAssessmentsAssessmentIdPatch**](AssessmentManagementApi.md#offeringsOfferingIdAssessmentsAssessmentIdPatch) | **PATCH** /offerings/{offeringId}/assessments/{assessmentId} | Update assessment details |
| [**offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatch**](AssessmentManagementApi.md#offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatch) | **PATCH** /offerings/{offeringId}/assessments/{assessmentId}/{userEmail} | Update the due dates for a learner&#39;s quiz attempt |
| [**offeringsOfferingIdAssessmentsGet**](AssessmentManagementApi.md#offeringsOfferingIdAssessmentsGet) | **GET** /offerings/{offeringId}/assessments | Find offering&#39;s assessments |
| [**offeringsOfferingIdLearnersPendingSubmissionGet**](AssessmentManagementApi.md#offeringsOfferingIdLearnersPendingSubmissionGet) | **GET** /offerings/{offeringId}/learners/pending-submission | Find learners with assessments pending x days before due date within the specified offeringId |
| [**offeringsOfferingIdUsersUserEmailAssessmentsAssessmentIdDelete**](AssessmentManagementApi.md#offeringsOfferingIdUsersUserEmailAssessmentsAssessmentIdDelete) | **DELETE** /offerings/{offeringId}/users/{userEmail}/assessments/{assessmentId} | Reset user&#39;s assessment to draft state |
| [**offeringsOfferingIdUsersUserEmailSubmissionsOpenResponseGet**](AssessmentManagementApi.md#offeringsOfferingIdUsersUserEmailSubmissionsOpenResponseGet) | **GET** /offerings/{offeringId}/users/{userEmail}/submissions/open-response | Find learner&#39;s open response assessment submissions |


<a id="offeringsOfferingIdActivitiesOpenresponseGet"></a>
# **offeringsOfferingIdActivitiesOpenresponseGet**
> List&lt;OfferingActivitiesResponse&gt; offeringsOfferingIdActivitiesOpenresponseGet(offeringId)

Find offering&#39;s activities

Responds with the activities in a specific offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentManagementApi apiInstance = new AssessmentManagementApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    try {
      List<OfferingActivitiesResponse> result = apiInstance.offeringsOfferingIdActivitiesOpenresponseGet(offeringId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentManagementApi#offeringsOfferingIdActivitiesOpenresponseGet");
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

[**List&lt;OfferingActivitiesResponse&gt;**](OfferingActivitiesResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | offering&#39;s learners |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdAssessmentsAssessmentIdDocumentsDocumentIdDelete"></a>
# **offeringsOfferingIdAssessmentsAssessmentIdDocumentsDocumentIdDelete**
> offeringsOfferingIdAssessmentsAssessmentIdDocumentsDocumentIdDelete(offeringId, assessmentId, documentId)

Remove assessment document

Removes the assessment document file for a specified assessment in an offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentManagementApi apiInstance = new AssessmentManagementApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String assessmentId = "assessmentId_example"; // String | assessment's id
    String documentId = "documentId_example"; // String | documents's id
    try {
      apiInstance.offeringsOfferingIdAssessmentsAssessmentIdDocumentsDocumentIdDelete(offeringId, assessmentId, documentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentManagementApi#offeringsOfferingIdAssessmentsAssessmentIdDocumentsDocumentIdDelete");
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
| **documentId** | **String**| documents&#39;s id | |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | assessment document successfully removed |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdAssessmentsAssessmentIdPatch"></a>
# **offeringsOfferingIdAssessmentsAssessmentIdPatch**
> AssessmentResponse offeringsOfferingIdAssessmentsAssessmentIdPatch(offeringId, assessmentId, assessment)

Update assessment details

Updates the assessment details for a specified assessment in an offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentManagementApi apiInstance = new AssessmentManagementApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String assessmentId = "assessmentId_example"; // String | assessment's id
    Assessment assessment = new Assessment(); // Assessment | 
    try {
      AssessmentResponse result = apiInstance.offeringsOfferingIdAssessmentsAssessmentIdPatch(offeringId, assessmentId, assessment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentManagementApi#offeringsOfferingIdAssessmentsAssessmentIdPatch");
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
| **assessment** | [**Assessment**](Assessment.md)|  | |

### Return type

[**AssessmentResponse**](AssessmentResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | assessment successfully updated |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatch"></a>
# **offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatch**
> offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatch(offeringId, assessmentId, userEmail, offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest)

Update the due dates for a learner&#39;s quiz attempt

Updates the due dates for a learner&#39;s quiz attempt specified by the assessmentId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentManagementApi apiInstance = new AssessmentManagementApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String assessmentId = "assessmentId_example"; // String | assessment's id
    String userEmail = "userEmail_example"; // String | user's email
    OfferingsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest = new OfferingsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest(); // OfferingsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest | 
    try {
      apiInstance.offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatch(offeringId, assessmentId, userEmail, offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentManagementApi#offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatch");
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
| **userEmail** | **String**| user&#39;s email | |
| **offeringsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest** | [**OfferingsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest**](OfferingsOfferingIdAssessmentsAssessmentIdUserEmailPatchRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully updated assessment due date. |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdAssessmentsGet"></a>
# **offeringsOfferingIdAssessmentsGet**
> List&lt;AssessmentResponse&gt; offeringsOfferingIdAssessmentsGet(offeringId)

Find offering&#39;s assessments

Responds with all assessments in an offering matching the offeringId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentManagementApi apiInstance = new AssessmentManagementApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    try {
      List<AssessmentResponse> result = apiInstance.offeringsOfferingIdAssessmentsGet(offeringId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentManagementApi#offeringsOfferingIdAssessmentsGet");
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

[**List&lt;AssessmentResponse&gt;**](AssessmentResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | offering&#39;s assessments |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdLearnersPendingSubmissionGet"></a>
# **offeringsOfferingIdLearnersPendingSubmissionGet**
> List&lt;AssessmentPendingSubmission&gt; offeringsOfferingIdLearnersPendingSubmissionGet(offeringId, days)

Find learners with assessments pending x days before due date within the specified offeringId

Responds with learners who have one or more assessments due x days before the due date, with each assessment that is due, where x &#x3D; the number of days specified in the request. The default is 3 days.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentManagementApi apiInstance = new AssessmentManagementApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String days = "days_example"; // String | days to assessment due date. Default is 3 days
    try {
      List<AssessmentPendingSubmission> result = apiInstance.offeringsOfferingIdLearnersPendingSubmissionGet(offeringId, days);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentManagementApi#offeringsOfferingIdLearnersPendingSubmissionGet");
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
| **days** | **String**| days to assessment due date. Default is 3 days | [optional] |

### Return type

[**List&lt;AssessmentPendingSubmission&gt;**](AssessmentPendingSubmission.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | offering&#39;s learners |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdUsersUserEmailAssessmentsAssessmentIdDelete"></a>
# **offeringsOfferingIdUsersUserEmailAssessmentsAssessmentIdDelete**
> offeringsOfferingIdUsersUserEmailAssessmentsAssessmentIdDelete(offeringId, userEmail, assessmentId)

Reset user&#39;s assessment to draft state

Resets the user&#39;s submitted assessment to a draft state.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentManagementApi apiInstance = new AssessmentManagementApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String userEmail = "userEmail_example"; // String | user's email
    String assessmentId = "assessmentId_example"; // String | assessment's id
    try {
      apiInstance.offeringsOfferingIdUsersUserEmailAssessmentsAssessmentIdDelete(offeringId, userEmail, assessmentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentManagementApi#offeringsOfferingIdUsersUserEmailAssessmentsAssessmentIdDelete");
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

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | User&#39;s assessment successfully moved to draft state. |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdUsersUserEmailSubmissionsOpenResponseGet"></a>
# **offeringsOfferingIdUsersUserEmailSubmissionsOpenResponseGet**
> List&lt;Assignments&gt; offeringsOfferingIdUsersUserEmailSubmissionsOpenResponseGet(offeringId, userEmail)

Find learner&#39;s open response assessment submissions

Responds with open response assessment submissions by a learner in an offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentManagementApi apiInstance = new AssessmentManagementApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String userEmail = "userEmail_example"; // String | user's email
    try {
      List<Assignments> result = apiInstance.offeringsOfferingIdUsersUserEmailSubmissionsOpenResponseGet(offeringId, userEmail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentManagementApi#offeringsOfferingIdUsersUserEmailSubmissionsOpenResponseGet");
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

### Return type

[**List&lt;Assignments&gt;**](Assignments.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | user open response submission and mark details |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

