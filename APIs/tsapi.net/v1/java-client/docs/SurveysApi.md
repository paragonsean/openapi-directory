# SurveysApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**surveysGet**](SurveysApi.md#surveysGet) | **GET** /Surveys | Returns a list of available Surveys |
| [**surveysSurveyIdInterviewsGet**](SurveysApi.md#surveysSurveyIdInterviewsGet) | **GET** /Surveys/{surveyId}/Interviews | Fetches some interview records for a specific survey |
| [**surveysSurveyIdMetadataGet**](SurveysApi.md#surveysSurveyIdMetadataGet) | **GET** /Surveys/{surveyId}/Metadata | Fetches the metadata for a specific survey |


<a id="surveysGet"></a>
# **surveysGet**
> List&lt;SurveyDetail&gt; surveysGet()

Returns a list of available Surveys

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
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: basic
    ApiKeyAuth basic = (ApiKeyAuth) defaultClient.getAuthentication("basic");
    basic.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //basic.setApiKeyPrefix("Token");

    SurveysApi apiInstance = new SurveysApi(defaultClient);
    try {
      List<SurveyDetail> result = apiInstance.surveysGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SurveysApi#surveysGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;SurveyDetail&gt;**](SurveyDetail.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="surveysSurveyIdInterviewsGet"></a>
# **surveysSurveyIdInterviewsGet**
> List&lt;Interview&gt; surveysSurveyIdInterviewsGet(surveyId, start, maxLength)

Fetches some interview records for a specific survey

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
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: basic
    ApiKeyAuth basic = (ApiKeyAuth) defaultClient.getAuthentication("basic");
    basic.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //basic.setApiKeyPrefix("Token");

    SurveysApi apiInstance = new SurveysApi(defaultClient);
    UUID surveyId = UUID.randomUUID(); // UUID | 
    Integer start = 56; // Integer | 
    Integer maxLength = 56; // Integer | 
    try {
      List<Interview> result = apiInstance.surveysSurveyIdInterviewsGet(surveyId, start, maxLength);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SurveysApi#surveysSurveyIdInterviewsGet");
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
| **surveyId** | **UUID**|  | |
| **start** | **Integer**|  | [optional] |
| **maxLength** | **Integer**|  | [optional] |

### Return type

[**List&lt;Interview&gt;**](Interview.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="surveysSurveyIdMetadataGet"></a>
# **surveysSurveyIdMetadataGet**
> SurveyMetadata surveysSurveyIdMetadataGet(surveyId)

Fetches the metadata for a specific survey

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
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: basic
    ApiKeyAuth basic = (ApiKeyAuth) defaultClient.getAuthentication("basic");
    basic.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //basic.setApiKeyPrefix("Token");

    SurveysApi apiInstance = new SurveysApi(defaultClient);
    UUID surveyId = UUID.randomUUID(); // UUID | 
    try {
      SurveyMetadata result = apiInstance.surveysSurveyIdMetadataGet(surveyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SurveysApi#surveysSurveyIdMetadataGet");
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
| **surveyId** | **UUID**|  | |

### Return type

[**SurveyMetadata**](SurveyMetadata.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

