# SurveysApi

All URIs are relative to *https://api.motaword.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getQuestions**](SurveysApi.md#getQuestions) | **GET** /surveys/{scope}/{type} | Get survey questions in given scope and type |
| [**submitAnswers**](SurveysApi.md#submitAnswers) | **POST** /surveys/{scope}/{type} | Post survey answers for scope and type |


<a id="getQuestions"></a>
# **getQuestions**
> List&lt;SurveyQuestion&gt; getQuestions(scope, type, attachAnswersForProject)

Get survey questions in given scope and type

Get survey questions in given scope and type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SurveysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    SurveysApi apiInstance = new SurveysApi(defaultClient);
    String scope = "vendor"; // String | Scope
    String type = "profile"; // String | Type
    Long attachAnswersForProject = 74L; // Long | Project ID
    try {
      List<SurveyQuestion> result = apiInstance.getQuestions(scope, type, attachAnswersForProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SurveysApi#getQuestions");
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
| **scope** | **String**| Scope | |
| **type** | **String**| Type | |
| **attachAnswersForProject** | **Long**| Project ID | [optional] |

### Return type

[**List&lt;SurveyQuestion&gt;**](SurveyQuestion.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Survey Questions |  -  |
| **404** | SurveyQuestionsNotFound |  -  |

<a id="submitAnswers"></a>
# **submitAnswers**
> OperationStatus submitAnswers(scope, type, surveyAnswers)

Post survey answers for scope and type

Post survey answers for scope and type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SurveysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    SurveysApi apiInstance = new SurveysApi(defaultClient);
    String scope = "vendor"; // String | Scope
    String type = "profile"; // String | Type
    SurveyAnswers surveyAnswers = new SurveyAnswers(); // SurveyAnswers | 
    try {
      OperationStatus result = apiInstance.submitAnswers(scope, type, surveyAnswers);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SurveysApi#submitAnswers");
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
| **scope** | **String**| Scope | |
| **type** | **String**| Type | |
| **surveyAnswers** | [**SurveyAnswers**](SurveyAnswers.md)|  | [optional] |

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Survey Answers |  -  |
| **500** | FailedToSubmitSurveyAnswers |  -  |

