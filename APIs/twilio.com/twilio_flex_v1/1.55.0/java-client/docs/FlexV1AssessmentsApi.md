# FlexV1AssessmentsApi

All URIs are relative to *https://flex-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInsightsAssessments**](FlexV1AssessmentsApi.md#createInsightsAssessments) | **POST** /v1/Insights/QualityManagement/Assessments |  |
| [**listInsightsAssessments**](FlexV1AssessmentsApi.md#listInsightsAssessments) | **GET** /v1/Insights/QualityManagement/Assessments |  |
| [**updateInsightsAssessments**](FlexV1AssessmentsApi.md#updateInsightsAssessments) | **POST** /v1/Insights/QualityManagement/Assessments/{AssessmentSid} |  |


<a id="createInsightsAssessments"></a>
# **createInsightsAssessments**
> FlexV1InsightsAssessments createInsightsAssessments(agentId, answerId, answerText, categoryName, categorySid, metricId, metricName, offset, questionnaireSid, segmentId, authorization)



Add assessments against conversation to dynamo db. Used in assessments screen by user. Users can select the questionnaire and pick up answers for each and every question.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1AssessmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1AssessmentsApi apiInstance = new FlexV1AssessmentsApi(defaultClient);
    String agentId = "agentId_example"; // String | The id of the Agent
    String answerId = "answerId_example"; // String | The id of the answer selected by user
    String answerText = "answerText_example"; // String | The answer text selected by user
    String categoryName = "categoryName_example"; // String | The name of the category
    String categorySid = "categorySid_example"; // String | The SID of the category 
    String metricId = "metricId_example"; // String | The question SID selected for assessment
    String metricName = "metricName_example"; // String | The question name of the assessment
    BigDecimal offset = new BigDecimal(78); // BigDecimal | The offset of the conversation.
    String questionnaireSid = "questionnaireSid_example"; // String | Questionnaire SID of the associated question
    String segmentId = "segmentId_example"; // String | Segment Id of the conversation
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    try {
      FlexV1InsightsAssessments result = apiInstance.createInsightsAssessments(agentId, answerId, answerText, categoryName, categorySid, metricId, metricName, offset, questionnaireSid, segmentId, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1AssessmentsApi#createInsightsAssessments");
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
| **agentId** | **String**| The id of the Agent | |
| **answerId** | **String**| The id of the answer selected by user | |
| **answerText** | **String**| The answer text selected by user | |
| **categoryName** | **String**| The name of the category | |
| **categorySid** | **String**| The SID of the category  | |
| **metricId** | **String**| The question SID selected for assessment | |
| **metricName** | **String**| The question name of the assessment | |
| **offset** | **BigDecimal**| The offset of the conversation. | |
| **questionnaireSid** | **String**| Questionnaire SID of the associated question | |
| **segmentId** | **String**| Segment Id of the conversation | |
| **authorization** | **String**| The Authorization HTTP request header | [optional] |

### Return type

[**FlexV1InsightsAssessments**](FlexV1InsightsAssessments.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="listInsightsAssessments"></a>
# **listInsightsAssessments**
> ListInsightsAssessmentsResponse listInsightsAssessments(authorization, segmentId, pageSize, page, pageToken)



Get assessments done for a conversation by logged in user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1AssessmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1AssessmentsApi apiInstance = new FlexV1AssessmentsApi(defaultClient);
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    String segmentId = "segmentId_example"; // String | The id of the segment.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListInsightsAssessmentsResponse result = apiInstance.listInsightsAssessments(authorization, segmentId, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1AssessmentsApi#listInsightsAssessments");
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
| **authorization** | **String**| The Authorization HTTP request header | [optional] |
| **segmentId** | **String**| The id of the segment. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListInsightsAssessmentsResponse**](ListInsightsAssessmentsResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateInsightsAssessments"></a>
# **updateInsightsAssessments**
> FlexV1InsightsAssessments updateInsightsAssessments(assessmentSid, answerId, answerText, offset, authorization)



Update a specific Assessment assessed earlier

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1AssessmentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1AssessmentsApi apiInstance = new FlexV1AssessmentsApi(defaultClient);
    String assessmentSid = "assessmentSid_example"; // String | The SID of the assessment to be modified
    String answerId = "answerId_example"; // String | The id of the answer selected by user
    String answerText = "answerText_example"; // String | The answer text selected by user
    BigDecimal offset = new BigDecimal(78); // BigDecimal | The offset of the conversation
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    try {
      FlexV1InsightsAssessments result = apiInstance.updateInsightsAssessments(assessmentSid, answerId, answerText, offset, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1AssessmentsApi#updateInsightsAssessments");
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
| **assessmentSid** | **String**| The SID of the assessment to be modified | |
| **answerId** | **String**| The id of the answer selected by user | |
| **answerText** | **String**| The answer text selected by user | |
| **offset** | **BigDecimal**| The offset of the conversation | |
| **authorization** | **String**| The Authorization HTTP request header | [optional] |

### Return type

[**FlexV1InsightsAssessments**](FlexV1InsightsAssessments.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

