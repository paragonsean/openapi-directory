# OralQuestionsApi

All URIs are relative to *http://oralquestionsandmotions-api.parliament.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**publishedOralQuestionGet**](OralQuestionsApi.md#publishedOralQuestionGet) | **GET** /oralquestions/list | Returns a list of oral questions |


<a id="publishedOralQuestionGet"></a>
# **publishedOralQuestionGet**
> ApiResponseListPublishedWrittenQuestion publishedOralQuestionGet(parametersAnsweringDateStart, parametersAnsweringDateEnd, parametersQuestionType, parametersOralQuestionTimeId, parametersAskingMemberIds, parametersUINs, parametersAnsweringBodyIds, parametersSkip, parametersTake)

Returns a list of oral questions

A list of oral questions meeting the specified criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OralQuestionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://oralquestionsandmotions-api.parliament.uk");

    OralQuestionsApi apiInstance = new OralQuestionsApi(defaultClient);
    OffsetDateTime parametersAnsweringDateStart = OffsetDateTime.now(); // OffsetDateTime | Oral Questions where the answering date has been set on or after the date provided. Date format YYYY-MM-DD.
    OffsetDateTime parametersAnsweringDateEnd = OffsetDateTime.now(); // OffsetDateTime | Oral Questions where the answering date has been set on or before the date provided. Date format YYYY-MM-DD.
    String parametersQuestionType = "Substantive"; // String | Oral Questions where the question type is the selected type, substantive or topical.
    Integer parametersOralQuestionTimeId = 56; // Integer | Oral Questions where the question is within the question time with the ID provided
    List<Integer> parametersAskingMemberIds = Arrays.asList(); // List<Integer> | The ID of the member asking the question. Lists of member IDs for each house are available <a href=\"http://data.parliament.uk/membersdataplatform/services/mnis/members/query/house=Commons\" target=\"_blank\">Commons</a> and <a href=\"http://data.parliament.uk/membersdataplatform/services/mnis/members/query/house=Lords\" target=\"_blank\">Lords</a>.
    List<Integer> parametersUINs = Arrays.asList(); // List<Integer> | The UIN for the question - note that UINs reset at the start of each Parliamentary session.
    List<Integer> parametersAnsweringBodyIds = Arrays.asList(); // List<Integer> | Which answering body is to respond. A list of answering bodies can be found <a target=\"_blank\" href=\"http://data.parliament.uk/membersdataplatform/services/mnis/referencedata/AnsweringBodies/\">here</a>.
    Integer parametersSkip = 56; // Integer | The number of records to skip from the first, default is 0.
    Integer parametersTake = 56; // Integer | The number of records to return, default is 25, maximum is 100.
    try {
      ApiResponseListPublishedWrittenQuestion result = apiInstance.publishedOralQuestionGet(parametersAnsweringDateStart, parametersAnsweringDateEnd, parametersQuestionType, parametersOralQuestionTimeId, parametersAskingMemberIds, parametersUINs, parametersAnsweringBodyIds, parametersSkip, parametersTake);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OralQuestionsApi#publishedOralQuestionGet");
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
| **parametersAnsweringDateStart** | **OffsetDateTime**| Oral Questions where the answering date has been set on or after the date provided. Date format YYYY-MM-DD. | [optional] |
| **parametersAnsweringDateEnd** | **OffsetDateTime**| Oral Questions where the answering date has been set on or before the date provided. Date format YYYY-MM-DD. | [optional] |
| **parametersQuestionType** | **String**| Oral Questions where the question type is the selected type, substantive or topical. | [optional] [enum: Substantive, Topical] |
| **parametersOralQuestionTimeId** | **Integer**| Oral Questions where the question is within the question time with the ID provided | [optional] |
| **parametersAskingMemberIds** | [**List&lt;Integer&gt;**](Integer.md)| The ID of the member asking the question. Lists of member IDs for each house are available &lt;a href&#x3D;\&quot;http://data.parliament.uk/membersdataplatform/services/mnis/members/query/house&#x3D;Commons\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Commons&lt;/a&gt; and &lt;a href&#x3D;\&quot;http://data.parliament.uk/membersdataplatform/services/mnis/members/query/house&#x3D;Lords\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Lords&lt;/a&gt;. | [optional] |
| **parametersUINs** | [**List&lt;Integer&gt;**](Integer.md)| The UIN for the question - note that UINs reset at the start of each Parliamentary session. | [optional] |
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

