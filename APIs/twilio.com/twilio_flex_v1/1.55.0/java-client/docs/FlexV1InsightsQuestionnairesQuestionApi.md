# FlexV1InsightsQuestionnairesQuestionApi

All URIs are relative to *https://flex-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInsightsQuestionnairesQuestion**](FlexV1InsightsQuestionnairesQuestionApi.md#createInsightsQuestionnairesQuestion) | **POST** /v1/Insights/QualityManagement/Questions |  |
| [**deleteInsightsQuestionnairesQuestion**](FlexV1InsightsQuestionnairesQuestionApi.md#deleteInsightsQuestionnairesQuestion) | **DELETE** /v1/Insights/QualityManagement/Questions/{QuestionSid} |  |
| [**listInsightsQuestionnairesQuestion**](FlexV1InsightsQuestionnairesQuestionApi.md#listInsightsQuestionnairesQuestion) | **GET** /v1/Insights/QualityManagement/Questions |  |
| [**updateInsightsQuestionnairesQuestion**](FlexV1InsightsQuestionnairesQuestionApi.md#updateInsightsQuestionnairesQuestion) | **POST** /v1/Insights/QualityManagement/Questions/{QuestionSid} |  |


<a id="createInsightsQuestionnairesQuestion"></a>
# **createInsightsQuestionnairesQuestion**
> FlexV1InsightsQuestionnairesQuestion createInsightsQuestionnairesQuestion(allowNa, answerSetId, categorySid, question, authorization, description)



To create a question for a Category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InsightsQuestionnairesQuestionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InsightsQuestionnairesQuestionApi apiInstance = new FlexV1InsightsQuestionnairesQuestionApi(defaultClient);
    Boolean allowNa = true; // Boolean | The flag to enable for disable NA for answer.
    String answerSetId = "answerSetId_example"; // String | The answer_set for the question.
    String categorySid = "categorySid_example"; // String | The SID of the category
    String question = "question_example"; // String | The question.
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    String description = "description_example"; // String | The description for the question.
    try {
      FlexV1InsightsQuestionnairesQuestion result = apiInstance.createInsightsQuestionnairesQuestion(allowNa, answerSetId, categorySid, question, authorization, description);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InsightsQuestionnairesQuestionApi#createInsightsQuestionnairesQuestion");
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
| **allowNa** | **Boolean**| The flag to enable for disable NA for answer. | |
| **answerSetId** | **String**| The answer_set for the question. | |
| **categorySid** | **String**| The SID of the category | |
| **question** | **String**| The question. | |
| **authorization** | **String**| The Authorization HTTP request header | [optional] |
| **description** | **String**| The description for the question. | [optional] |

### Return type

[**FlexV1InsightsQuestionnairesQuestion**](FlexV1InsightsQuestionnairesQuestion.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteInsightsQuestionnairesQuestion"></a>
# **deleteInsightsQuestionnairesQuestion**
> deleteInsightsQuestionnairesQuestion(questionSid, authorization)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InsightsQuestionnairesQuestionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InsightsQuestionnairesQuestionApi apiInstance = new FlexV1InsightsQuestionnairesQuestionApi(defaultClient);
    String questionSid = "questionSid_example"; // String | The SID of the question
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    try {
      apiInstance.deleteInsightsQuestionnairesQuestion(questionSid, authorization);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InsightsQuestionnairesQuestionApi#deleteInsightsQuestionnairesQuestion");
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
| **questionSid** | **String**| The SID of the question | |
| **authorization** | **String**| The Authorization HTTP request header | [optional] |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="listInsightsQuestionnairesQuestion"></a>
# **listInsightsQuestionnairesQuestion**
> ListInsightsQuestionnairesQuestionResponse listInsightsQuestionnairesQuestion(authorization, categorySid, pageSize, page, pageToken)



To get all the question for the given categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InsightsQuestionnairesQuestionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InsightsQuestionnairesQuestionApi apiInstance = new FlexV1InsightsQuestionnairesQuestionApi(defaultClient);
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    List<String> categorySid = Arrays.asList(); // List<String> | The list of category SIDs
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListInsightsQuestionnairesQuestionResponse result = apiInstance.listInsightsQuestionnairesQuestion(authorization, categorySid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InsightsQuestionnairesQuestionApi#listInsightsQuestionnairesQuestion");
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
| **categorySid** | [**List&lt;String&gt;**](String.md)| The list of category SIDs | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListInsightsQuestionnairesQuestionResponse**](ListInsightsQuestionnairesQuestionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateInsightsQuestionnairesQuestion"></a>
# **updateInsightsQuestionnairesQuestion**
> FlexV1InsightsQuestionnairesQuestion updateInsightsQuestionnairesQuestion(questionSid, allowNa, authorization, answerSetId, categorySid, description, question)



To update the question

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InsightsQuestionnairesQuestionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InsightsQuestionnairesQuestionApi apiInstance = new FlexV1InsightsQuestionnairesQuestionApi(defaultClient);
    String questionSid = "questionSid_example"; // String | The SID of the question
    Boolean allowNa = true; // Boolean | The flag to enable for disable NA for answer.
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    String answerSetId = "answerSetId_example"; // String | The answer_set for the question.
    String categorySid = "categorySid_example"; // String | The SID of the category
    String description = "description_example"; // String | The description for the question.
    String question = "question_example"; // String | The question.
    try {
      FlexV1InsightsQuestionnairesQuestion result = apiInstance.updateInsightsQuestionnairesQuestion(questionSid, allowNa, authorization, answerSetId, categorySid, description, question);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InsightsQuestionnairesQuestionApi#updateInsightsQuestionnairesQuestion");
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
| **questionSid** | **String**| The SID of the question | |
| **allowNa** | **Boolean**| The flag to enable for disable NA for answer. | |
| **authorization** | **String**| The Authorization HTTP request header | [optional] |
| **answerSetId** | **String**| The answer_set for the question. | [optional] |
| **categorySid** | **String**| The SID of the category | [optional] |
| **description** | **String**| The description for the question. | [optional] |
| **question** | **String**| The question. | [optional] |

### Return type

[**FlexV1InsightsQuestionnairesQuestion**](FlexV1InsightsQuestionnairesQuestion.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

