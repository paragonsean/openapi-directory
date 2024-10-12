# DefaultApi

All URIs are relative to *https://polls.apiblueprint.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createANewQuestion**](DefaultApi.md#createANewQuestion) | **POST** /questions | Create a New Question |
| [**listAllQuestions**](DefaultApi.md#listAllQuestions) | **GET** /questions | List All Questions |


<a id="createANewQuestion"></a>
# **createANewQuestion**
> createANewQuestion(createANewQuestionRequest)

Create a New Question

You may create your own question using this action. It takes a JSON object containing a question and a collection of answers in the form of choices.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://polls.apiblueprint.org");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CreateANewQuestionRequest createANewQuestionRequest = new CreateANewQuestionRequest(); // CreateANewQuestionRequest | 
    try {
      apiInstance.createANewQuestion(createANewQuestionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createANewQuestion");
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
| **createANewQuestionRequest** | [**CreateANewQuestionRequest**](CreateANewQuestionRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * Location -  <br>  |

<a id="listAllQuestions"></a>
# **listAllQuestions**
> listAllQuestions()

List All Questions



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://polls.apiblueprint.org");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.listAllQuestions();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAllQuestions");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

