# WrittenQuestionsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiWrittenquestionsQuestionsDateUinGet**](WrittenQuestionsApi.md#apiWrittenquestionsQuestionsDateUinGet) | **GET** /api/writtenquestions/questions/{date}/{uin} | Returns a written question |
| [**apiWrittenquestionsQuestionsGet**](WrittenQuestionsApi.md#apiWrittenquestionsQuestionsGet) | **GET** /api/writtenquestions/questions | Returns a list of written questions |
| [**apiWrittenquestionsQuestionsIdGet**](WrittenQuestionsApi.md#apiWrittenquestionsQuestionsIdGet) | **GET** /api/writtenquestions/questions/{id} | Returns a written question |


<a id="apiWrittenquestionsQuestionsDateUinGet"></a>
# **apiWrittenquestionsQuestionsDateUinGet**
> QuestionsViewModelItem apiWrittenquestionsQuestionsDateUinGet(date, uin, expandMember)

Returns a written question

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WrittenQuestionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    WrittenQuestionsApi apiInstance = new WrittenQuestionsApi(defaultClient);
    OffsetDateTime date = OffsetDateTime.now(); // OffsetDateTime | Written question on date specified
    String uin = "uin_example"; // String | Written question with uid specified
    Boolean expandMember = true; // Boolean | Expand the details of Members in the results
    try {
      QuestionsViewModelItem result = apiInstance.apiWrittenquestionsQuestionsDateUinGet(date, uin, expandMember);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WrittenQuestionsApi#apiWrittenquestionsQuestionsDateUinGet");
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
| **date** | **OffsetDateTime**| Written question on date specified | |
| **uin** | **String**| Written question with uid specified | |
| **expandMember** | **Boolean**| Expand the details of Members in the results | [optional] |

### Return type

[**QuestionsViewModelItem**](QuestionsViewModelItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiWrittenquestionsQuestionsGet"></a>
# **apiWrittenquestionsQuestionsGet**
> QuestionsViewModelSearchResult apiWrittenquestionsQuestionsGet(askingMemberId, answeringMemberId, tabledWhenFrom, tabledWhenTo, answered, answeredWhenFrom, answeredWhenTo, questionStatus, includeWithdrawn, expandMember, correctedWhenFrom, correctedWhenTo, searchTerm, uIN, answeringBodies, members, house, skip, take)

Returns a list of written questions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WrittenQuestionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    WrittenQuestionsApi apiInstance = new WrittenQuestionsApi(defaultClient);
    Integer askingMemberId = 56; // Integer | Written questions asked by member with member ID specified
    Integer answeringMemberId = 56; // Integer | Written questions answered by member with member ID specified
    OffsetDateTime tabledWhenFrom = OffsetDateTime.now(); // OffsetDateTime | Written questions tabled on or after the date specified. Date format yyyy-mm-dd
    OffsetDateTime tabledWhenTo = OffsetDateTime.now(); // OffsetDateTime | Written questions tabled on or before the date specified. Date format yyyy-mm-dd
    Answered answered = Answered.fromValue("Any"); // Answered | Written questions that have been answered, unanswered or either.
    OffsetDateTime answeredWhenFrom = OffsetDateTime.now(); // OffsetDateTime | Written questions answered on or after the date specified. Date format yyyy-mm-dd
    OffsetDateTime answeredWhenTo = OffsetDateTime.now(); // OffsetDateTime | Written questions answered on or before the date specified. Date format yyyy-mm-dd
    QuestionStatusEnum questionStatus = QuestionStatusEnum.fromValue("NotAnswered"); // QuestionStatusEnum | Written questions with the status specified
    Boolean includeWithdrawn = true; // Boolean | Include written questions that have been withdrawn
    Boolean expandMember = true; // Boolean | Expand the details of Members in the results
    OffsetDateTime correctedWhenFrom = OffsetDateTime.now(); // OffsetDateTime | Written questions corrected on or after the date specified. Date format yyyy-mm-dd
    OffsetDateTime correctedWhenTo = OffsetDateTime.now(); // OffsetDateTime | Written questions corrected on or before the date specified. Date format yyyy-mm-dd
    String searchTerm = "searchTerm_example"; // String | Written questions / statements containing the search term specified, searches item content
    String uIN = "uIN_example"; // String | Written questions / statements with the uin specified
    List<Integer> answeringBodies = Arrays.asList(); // List<Integer> | Written questions / statements relating to the answering bodies with the IDs specified
    List<Integer> members = Arrays.asList(); // List<Integer> | Written questions / statements relating to the members with the IDs specified
    HouseEnum house = HouseEnum.fromValue("Bicameral"); // HouseEnum | Written questions / statements relating to the House specified
    Integer skip = 56; // Integer | Number of records to skip, default is 0
    Integer take = 56; // Integer | Number of records to take, default is 20
    try {
      QuestionsViewModelSearchResult result = apiInstance.apiWrittenquestionsQuestionsGet(askingMemberId, answeringMemberId, tabledWhenFrom, tabledWhenTo, answered, answeredWhenFrom, answeredWhenTo, questionStatus, includeWithdrawn, expandMember, correctedWhenFrom, correctedWhenTo, searchTerm, uIN, answeringBodies, members, house, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WrittenQuestionsApi#apiWrittenquestionsQuestionsGet");
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
| **askingMemberId** | **Integer**| Written questions asked by member with member ID specified | [optional] |
| **answeringMemberId** | **Integer**| Written questions answered by member with member ID specified | [optional] |
| **tabledWhenFrom** | **OffsetDateTime**| Written questions tabled on or after the date specified. Date format yyyy-mm-dd | [optional] |
| **tabledWhenTo** | **OffsetDateTime**| Written questions tabled on or before the date specified. Date format yyyy-mm-dd | [optional] |
| **answered** | [**Answered**](.md)| Written questions that have been answered, unanswered or either. | [optional] [enum: Any, Answered, Unanswered] |
| **answeredWhenFrom** | **OffsetDateTime**| Written questions answered on or after the date specified. Date format yyyy-mm-dd | [optional] |
| **answeredWhenTo** | **OffsetDateTime**| Written questions answered on or before the date specified. Date format yyyy-mm-dd | [optional] |
| **questionStatus** | [**QuestionStatusEnum**](.md)| Written questions with the status specified | [optional] [enum: NotAnswered, AnsweredOnly, AllQuestions] |
| **includeWithdrawn** | **Boolean**| Include written questions that have been withdrawn | [optional] |
| **expandMember** | **Boolean**| Expand the details of Members in the results | [optional] |
| **correctedWhenFrom** | **OffsetDateTime**| Written questions corrected on or after the date specified. Date format yyyy-mm-dd | [optional] |
| **correctedWhenTo** | **OffsetDateTime**| Written questions corrected on or before the date specified. Date format yyyy-mm-dd | [optional] |
| **searchTerm** | **String**| Written questions / statements containing the search term specified, searches item content | [optional] |
| **uIN** | **String**| Written questions / statements with the uin specified | [optional] |
| **answeringBodies** | [**List&lt;Integer&gt;**](Integer.md)| Written questions / statements relating to the answering bodies with the IDs specified | [optional] |
| **members** | [**List&lt;Integer&gt;**](Integer.md)| Written questions / statements relating to the members with the IDs specified | [optional] |
| **house** | [**HouseEnum**](.md)| Written questions / statements relating to the House specified | [optional] [enum: Bicameral, Commons, Lords] |
| **skip** | **Integer**| Number of records to skip, default is 0 | [optional] |
| **take** | **Integer**| Number of records to take, default is 20 | [optional] |

### Return type

[**QuestionsViewModelSearchResult**](QuestionsViewModelSearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="apiWrittenquestionsQuestionsIdGet"></a>
# **apiWrittenquestionsQuestionsIdGet**
> QuestionsViewModelItem apiWrittenquestionsQuestionsIdGet(id, expandMember)

Returns a written question

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WrittenQuestionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    WrittenQuestionsApi apiInstance = new WrittenQuestionsApi(defaultClient);
    Integer id = 56; // Integer | written question with ID specified
    Boolean expandMember = true; // Boolean | Expand the details of Members in the result
    try {
      QuestionsViewModelItem result = apiInstance.apiWrittenquestionsQuestionsIdGet(id, expandMember);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WrittenQuestionsApi#apiWrittenquestionsQuestionsIdGet");
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
| **id** | **Integer**| written question with ID specified | |
| **expandMember** | **Boolean**| Expand the details of Members in the result | [optional] |

### Return type

[**QuestionsViewModelItem**](QuestionsViewModelItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

