# KnowledgebasesApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**runtimeGenerateAnswer**](KnowledgebasesApi.md#runtimeGenerateAnswer) | **POST** /knowledgebases/{kbId}/generateAnswer | GenerateAnswer call to query the knowledgebase. |
| [**runtimeTrain**](KnowledgebasesApi.md#runtimeTrain) | **POST** /knowledgebases/{kbId}/train | Train call to add suggestions to the knowledgebase. |


<a id="runtimeGenerateAnswer"></a>
# **runtimeGenerateAnswer**
> QnASearchResultList runtimeGenerateAnswer(kbId, generateAnswerPayload)

GenerateAnswer call to query the knowledgebase.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KnowledgebasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KnowledgebasesApi apiInstance = new KnowledgebasesApi(defaultClient);
    String kbId = "kbId_example"; // String | Knowledgebase id.
    QueryDTO generateAnswerPayload = new QueryDTO(); // QueryDTO | Post body of the request.
    try {
      QnASearchResultList result = apiInstance.runtimeGenerateAnswer(kbId, generateAnswerPayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling KnowledgebasesApi#runtimeGenerateAnswer");
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
| **kbId** | **String**| Knowledgebase id. | |
| **generateAnswerPayload** | [**QueryDTO**](QueryDTO.md)| Post body of the request. | |

### Return type

[**QnASearchResultList**](QnASearchResultList.md)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | GenerateAnswer call response. |  -  |
| **0** | Error response. |  -  |

<a id="runtimeTrain"></a>
# **runtimeTrain**
> runtimeTrain(kbId, trainPayload)

Train call to add suggestions to the knowledgebase.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KnowledgebasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");
    
    // Configure API key authorization: auth_key
    ApiKeyAuth auth_key = (ApiKeyAuth) defaultClient.getAuthentication("auth_key");
    auth_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_key.setApiKeyPrefix("Token");

    KnowledgebasesApi apiInstance = new KnowledgebasesApi(defaultClient);
    String kbId = "kbId_example"; // String | Knowledgebase id.
    FeedbackRecordsDTO trainPayload = new FeedbackRecordsDTO(); // FeedbackRecordsDTO | Post body of the request.
    try {
      apiInstance.runtimeTrain(kbId, trainPayload);
    } catch (ApiException e) {
      System.err.println("Exception when calling KnowledgebasesApi#runtimeTrain");
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
| **kbId** | **String**| Knowledgebase id. | |
| **trainPayload** | [**FeedbackRecordsDTO**](FeedbackRecordsDTO.md)| Post body of the request. | |

### Return type

null (empty response body)

### Authorization

[auth_key](../README.md#auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | HTTP 204 No Content. |  -  |
| **0** | Error response. |  -  |

