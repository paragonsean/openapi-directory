# FlexV1InsightsAssessmentsCommentApi

All URIs are relative to *https://flex-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInsightsAssessmentsComment**](FlexV1InsightsAssessmentsCommentApi.md#createInsightsAssessmentsComment) | **POST** /v1/Insights/QualityManagement/Assessments/Comments |  |
| [**listInsightsAssessmentsComment**](FlexV1InsightsAssessmentsCommentApi.md#listInsightsAssessmentsComment) | **GET** /v1/Insights/QualityManagement/Assessments/Comments |  |


<a id="createInsightsAssessmentsComment"></a>
# **createInsightsAssessmentsComment**
> FlexV1InsightsAssessmentsComment createInsightsAssessmentsComment(agentId, categoryId, categoryName, comment, offset, segmentId, authorization)



To create a comment assessment for a conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InsightsAssessmentsCommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InsightsAssessmentsCommentApi apiInstance = new FlexV1InsightsAssessmentsCommentApi(defaultClient);
    String agentId = "agentId_example"; // String | The id of the agent.
    String categoryId = "categoryId_example"; // String | The ID of the category
    String categoryName = "categoryName_example"; // String | The name of the category
    String comment = "comment_example"; // String | The Assessment comment.
    BigDecimal offset = new BigDecimal(78); // BigDecimal | The offset
    String segmentId = "segmentId_example"; // String | The id of the segment.
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    try {
      FlexV1InsightsAssessmentsComment result = apiInstance.createInsightsAssessmentsComment(agentId, categoryId, categoryName, comment, offset, segmentId, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InsightsAssessmentsCommentApi#createInsightsAssessmentsComment");
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
| **agentId** | **String**| The id of the agent. | |
| **categoryId** | **String**| The ID of the category | |
| **categoryName** | **String**| The name of the category | |
| **comment** | **String**| The Assessment comment. | |
| **offset** | **BigDecimal**| The offset | |
| **segmentId** | **String**| The id of the segment. | |
| **authorization** | **String**| The Authorization HTTP request header | [optional] |

### Return type

[**FlexV1InsightsAssessmentsComment**](FlexV1InsightsAssessmentsComment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="listInsightsAssessmentsComment"></a>
# **listInsightsAssessmentsComment**
> ListInsightsAssessmentsCommentResponse listInsightsAssessmentsComment(authorization, segmentId, agentId, pageSize, page, pageToken)



To create a comment assessment for a conversation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InsightsAssessmentsCommentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InsightsAssessmentsCommentApi apiInstance = new FlexV1InsightsAssessmentsCommentApi(defaultClient);
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    String segmentId = "segmentId_example"; // String | The id of the segment.
    String agentId = "agentId_example"; // String | The id of the agent.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListInsightsAssessmentsCommentResponse result = apiInstance.listInsightsAssessmentsComment(authorization, segmentId, agentId, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InsightsAssessmentsCommentApi#listInsightsAssessmentsComment");
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
| **agentId** | **String**| The id of the agent. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListInsightsAssessmentsCommentResponse**](ListInsightsAssessmentsCommentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

