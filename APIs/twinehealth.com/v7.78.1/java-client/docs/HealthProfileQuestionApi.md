# HealthProfileQuestionApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchHealthProfileQuestion**](HealthProfileQuestionApi.md#fetchHealthProfileQuestion) | **GET** /health_profile_question/{id} | Get a health profile question |
| [**fetchHealthProfileQuestions**](HealthProfileQuestionApi.md#fetchHealthProfileQuestions) | **GET** /health_profile_question | List health profile questions |


<a id="fetchHealthProfileQuestion"></a>
# **fetchHealthProfileQuestion**
> FetchHealthProfileQuestionResponse fetchHealthProfileQuestion(id, include)

Get a health profile question

Get a health profile by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthProfileQuestionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    HealthProfileQuestionApi apiInstance = new HealthProfileQuestionApi(defaultClient);
    String id = "id_example"; // String | Health profile question identifier
    String include = "question_definition"; // String | List of related resources to include in the response
    try {
      FetchHealthProfileQuestionResponse result = apiInstance.fetchHealthProfileQuestion(id, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthProfileQuestionApi#fetchHealthProfileQuestion");
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
| **id** | **String**| Health profile question identifier | |
| **include** | **String**| List of related resources to include in the response | [optional] [enum: question_definition, answer] |

### Return type

[**FetchHealthProfileQuestionResponse**](FetchHealthProfileQuestionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="fetchHealthProfileQuestions"></a>
# **fetchHealthProfileQuestions**
> FetchHealthProfileQuestionsResponse fetchHealthProfileQuestions(filterPatient, filterGroups, filterOrganization, include)

List health profile questions

Get a list of health profile questions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthProfileQuestionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    HealthProfileQuestionApi apiInstance = new HealthProfileQuestionApi(defaultClient);
    String filterPatient = "filterPatient_example"; // String | Patient id to fetch healt profile questions. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, or `filter[organization]`. 
    String filterGroups = "filterGroups_example"; // String | Comma-separated list of group ids. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, or `filter[organization]`. 
    String filterOrganization = "filterOrganization_example"; // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, or `filter[organization]`. 
    String include = "question_definition"; // String | List of related resources to include in the response
    try {
      FetchHealthProfileQuestionsResponse result = apiInstance.fetchHealthProfileQuestions(filterPatient, filterGroups, filterOrganization, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthProfileQuestionApi#fetchHealthProfileQuestions");
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
| **filterPatient** | **String**| Patient id to fetch healt profile questions. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;.  | [optional] |
| **filterGroups** | **String**| Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;.  | [optional] |
| **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;.  | [optional] |
| **include** | **String**| List of related resources to include in the response | [optional] [enum: question_definition, answer] |

### Return type

[**FetchHealthProfileQuestionsResponse**](FetchHealthProfileQuestionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **409** | Invalid Request |  -  |

