# OralQuestionTimesApi

All URIs are relative to *http://oralquestionsandmotions-api.parliament.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**publishedOralQuestionTimeGet**](OralQuestionTimesApi.md#publishedOralQuestionTimeGet) | **GET** /oralquestiontimes/list | Returns a list of oral question times |


<a id="publishedOralQuestionTimeGet"></a>
# **publishedOralQuestionTimeGet**
> ApiResponseListPublishedWrittenQuestion publishedOralQuestionTimeGet(parametersAnsweringDateStart, parametersAnsweringDateEnd, parametersDeadlineDateStart, parametersDeadlineDateEnd, parametersOralQuestionTimeId, parametersAnsweringBodyIds, parametersSkip, parametersTake)

Returns a list of oral question times

A list of oral question times meeting the specified criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OralQuestionTimesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://oralquestionsandmotions-api.parliament.uk");

    OralQuestionTimesApi apiInstance = new OralQuestionTimesApi(defaultClient);
    OffsetDateTime parametersAnsweringDateStart = OffsetDateTime.now(); // OffsetDateTime | Oral Questions Time where the answering date has been set on or after the date provided. Date format YYYY-MM-DD.
    OffsetDateTime parametersAnsweringDateEnd = OffsetDateTime.now(); // OffsetDateTime | Oral Questions Time where the answering date has been set on or before the date provided. Date format YYYY-MM-DD.
    OffsetDateTime parametersDeadlineDateStart = OffsetDateTime.now(); // OffsetDateTime | Oral Questions Time where the deadline date has been set on or after the date provided. Date format YYYY-MM-DD.
    OffsetDateTime parametersDeadlineDateEnd = OffsetDateTime.now(); // OffsetDateTime | Oral Questions Time where the deadline date has been set on or before the date provided. Date format YYYY-MM-DD.
    Integer parametersOralQuestionTimeId = 56; // Integer | Identifier of the OQT
    List<Integer> parametersAnsweringBodyIds = Arrays.asList(); // List<Integer> | Which answering body is to respond. A list of answering bodies can be found <a target=\"_blank\" href=\"http://data.parliament.uk/membersdataplatform/services/mnis/referencedata/AnsweringBodies/\">here</a>.
    Integer parametersSkip = 56; // Integer | The number of records to skip from the first, default is 0.
    Integer parametersTake = 56; // Integer | The number of records to return, default is 25, maximum is 100.
    try {
      ApiResponseListPublishedWrittenQuestion result = apiInstance.publishedOralQuestionTimeGet(parametersAnsweringDateStart, parametersAnsweringDateEnd, parametersDeadlineDateStart, parametersDeadlineDateEnd, parametersOralQuestionTimeId, parametersAnsweringBodyIds, parametersSkip, parametersTake);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OralQuestionTimesApi#publishedOralQuestionTimeGet");
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
| **parametersAnsweringDateStart** | **OffsetDateTime**| Oral Questions Time where the answering date has been set on or after the date provided. Date format YYYY-MM-DD. | [optional] |
| **parametersAnsweringDateEnd** | **OffsetDateTime**| Oral Questions Time where the answering date has been set on or before the date provided. Date format YYYY-MM-DD. | [optional] |
| **parametersDeadlineDateStart** | **OffsetDateTime**| Oral Questions Time where the deadline date has been set on or after the date provided. Date format YYYY-MM-DD. | [optional] |
| **parametersDeadlineDateEnd** | **OffsetDateTime**| Oral Questions Time where the deadline date has been set on or before the date provided. Date format YYYY-MM-DD. | [optional] |
| **parametersOralQuestionTimeId** | **Integer**| Identifier of the OQT | [optional] |
| **parametersAnsweringBodyIds** | [**List&lt;Integer&gt;**](Integer.md)| Which answering body is to respond. A list of answering bodies can be found &lt;a target&#x3D;\&quot;_blank\&quot; href&#x3D;\&quot;http://data.parliament.uk/membersdataplatform/services/mnis/referencedata/AnsweringBodies/\&quot;&gt;here&lt;/a&gt;. | [optional] |
| **parametersSkip** | **Integer**| The number of records to skip from the first, default is 0. | [optional] |
| **parametersTake** | **Integer**| The number of records to return, default is 25, maximum is 100. | [optional] |

### Return type

[**ApiResponseListPublishedWrittenQuestion**](ApiResponseListPublishedWrittenQuestion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | BadRequest |  -  |

