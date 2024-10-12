# FlexV1InsightsQuestionnairesCategoryApi

All URIs are relative to *https://flex-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInsightsQuestionnairesCategory**](FlexV1InsightsQuestionnairesCategoryApi.md#createInsightsQuestionnairesCategory) | **POST** /v1/Insights/QualityManagement/Categories |  |
| [**deleteInsightsQuestionnairesCategory**](FlexV1InsightsQuestionnairesCategoryApi.md#deleteInsightsQuestionnairesCategory) | **DELETE** /v1/Insights/QualityManagement/Categories/{CategorySid} |  |
| [**listInsightsQuestionnairesCategory**](FlexV1InsightsQuestionnairesCategoryApi.md#listInsightsQuestionnairesCategory) | **GET** /v1/Insights/QualityManagement/Categories |  |
| [**updateInsightsQuestionnairesCategory**](FlexV1InsightsQuestionnairesCategoryApi.md#updateInsightsQuestionnairesCategory) | **POST** /v1/Insights/QualityManagement/Categories/{CategorySid} |  |


<a id="createInsightsQuestionnairesCategory"></a>
# **createInsightsQuestionnairesCategory**
> FlexV1InsightsQuestionnairesCategory createInsightsQuestionnairesCategory(name, authorization)



To create a category for Questions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InsightsQuestionnairesCategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InsightsQuestionnairesCategoryApi apiInstance = new FlexV1InsightsQuestionnairesCategoryApi(defaultClient);
    String name = "name_example"; // String | The name of this category.
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    try {
      FlexV1InsightsQuestionnairesCategory result = apiInstance.createInsightsQuestionnairesCategory(name, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InsightsQuestionnairesCategoryApi#createInsightsQuestionnairesCategory");
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
| **name** | **String**| The name of this category. | |
| **authorization** | **String**| The Authorization HTTP request header | [optional] |

### Return type

[**FlexV1InsightsQuestionnairesCategory**](FlexV1InsightsQuestionnairesCategory.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteInsightsQuestionnairesCategory"></a>
# **deleteInsightsQuestionnairesCategory**
> deleteInsightsQuestionnairesCategory(categorySid, authorization)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InsightsQuestionnairesCategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InsightsQuestionnairesCategoryApi apiInstance = new FlexV1InsightsQuestionnairesCategoryApi(defaultClient);
    String categorySid = "categorySid_example"; // String | The SID of the category to be deleted
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    try {
      apiInstance.deleteInsightsQuestionnairesCategory(categorySid, authorization);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InsightsQuestionnairesCategoryApi#deleteInsightsQuestionnairesCategory");
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
| **categorySid** | **String**| The SID of the category to be deleted | |
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

<a id="listInsightsQuestionnairesCategory"></a>
# **listInsightsQuestionnairesCategory**
> ListInsightsQuestionnairesCategoryResponse listInsightsQuestionnairesCategory(authorization, pageSize, page, pageToken)



To get all the categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InsightsQuestionnairesCategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InsightsQuestionnairesCategoryApi apiInstance = new FlexV1InsightsQuestionnairesCategoryApi(defaultClient);
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListInsightsQuestionnairesCategoryResponse result = apiInstance.listInsightsQuestionnairesCategory(authorization, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InsightsQuestionnairesCategoryApi#listInsightsQuestionnairesCategory");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListInsightsQuestionnairesCategoryResponse**](ListInsightsQuestionnairesCategoryResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateInsightsQuestionnairesCategory"></a>
# **updateInsightsQuestionnairesCategory**
> FlexV1InsightsQuestionnairesCategory updateInsightsQuestionnairesCategory(categorySid, name, authorization)



To update the category for Questions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InsightsQuestionnairesCategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InsightsQuestionnairesCategoryApi apiInstance = new FlexV1InsightsQuestionnairesCategoryApi(defaultClient);
    String categorySid = "categorySid_example"; // String | The SID of the category to be updated
    String name = "name_example"; // String | The name of this category.
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    try {
      FlexV1InsightsQuestionnairesCategory result = apiInstance.updateInsightsQuestionnairesCategory(categorySid, name, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InsightsQuestionnairesCategoryApi#updateInsightsQuestionnairesCategory");
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
| **categorySid** | **String**| The SID of the category to be updated | |
| **name** | **String**| The name of this category. | |
| **authorization** | **String**| The Authorization HTTP request header | [optional] |

### Return type

[**FlexV1InsightsQuestionnairesCategory**](FlexV1InsightsQuestionnairesCategory.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

