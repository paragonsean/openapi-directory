# FlexV1InsightsQuestionnairesApi

All URIs are relative to *https://flex-api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInsightsQuestionnaires**](FlexV1InsightsQuestionnairesApi.md#createInsightsQuestionnaires) | **POST** /v1/Insights/QualityManagement/Questionnaires |  |
| [**deleteInsightsQuestionnaires**](FlexV1InsightsQuestionnairesApi.md#deleteInsightsQuestionnaires) | **DELETE** /v1/Insights/QualityManagement/Questionnaires/{QuestionnaireSid} |  |
| [**fetchInsightsQuestionnaires**](FlexV1InsightsQuestionnairesApi.md#fetchInsightsQuestionnaires) | **GET** /v1/Insights/QualityManagement/Questionnaires/{QuestionnaireSid} |  |
| [**listInsightsQuestionnaires**](FlexV1InsightsQuestionnairesApi.md#listInsightsQuestionnaires) | **GET** /v1/Insights/QualityManagement/Questionnaires |  |
| [**updateInsightsQuestionnaires**](FlexV1InsightsQuestionnairesApi.md#updateInsightsQuestionnaires) | **POST** /v1/Insights/QualityManagement/Questionnaires/{QuestionnaireSid} |  |


<a id="createInsightsQuestionnaires"></a>
# **createInsightsQuestionnaires**
> FlexV1InsightsQuestionnaires createInsightsQuestionnaires(name, authorization, active, description, questionSids)



To create a Questionnaire

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InsightsQuestionnairesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InsightsQuestionnairesApi apiInstance = new FlexV1InsightsQuestionnairesApi(defaultClient);
    String name = "name_example"; // String | The name of this questionnaire
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    Boolean active = true; // Boolean | The flag to enable or disable questionnaire
    String description = "description_example"; // String | The description of this questionnaire
    List<String> questionSids = Arrays.asList(); // List<String> | The list of questions sids under a questionnaire
    try {
      FlexV1InsightsQuestionnaires result = apiInstance.createInsightsQuestionnaires(name, authorization, active, description, questionSids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InsightsQuestionnairesApi#createInsightsQuestionnaires");
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
| **name** | **String**| The name of this questionnaire | |
| **authorization** | **String**| The Authorization HTTP request header | [optional] |
| **active** | **Boolean**| The flag to enable or disable questionnaire | [optional] |
| **description** | **String**| The description of this questionnaire | [optional] |
| **questionSids** | [**List&lt;String&gt;**](String.md)| The list of questions sids under a questionnaire | [optional] |

### Return type

[**FlexV1InsightsQuestionnaires**](FlexV1InsightsQuestionnaires.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteInsightsQuestionnaires"></a>
# **deleteInsightsQuestionnaires**
> deleteInsightsQuestionnaires(questionnaireSid, authorization)



To delete the questionnaire

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InsightsQuestionnairesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InsightsQuestionnairesApi apiInstance = new FlexV1InsightsQuestionnairesApi(defaultClient);
    String questionnaireSid = "questionnaireSid_example"; // String | The SID of the questionnaire
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    try {
      apiInstance.deleteInsightsQuestionnaires(questionnaireSid, authorization);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InsightsQuestionnairesApi#deleteInsightsQuestionnaires");
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
| **questionnaireSid** | **String**| The SID of the questionnaire | |
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

<a id="fetchInsightsQuestionnaires"></a>
# **fetchInsightsQuestionnaires**
> FlexV1InsightsQuestionnaires fetchInsightsQuestionnaires(questionnaireSid, authorization)



To get the Questionnaire Detail

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InsightsQuestionnairesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InsightsQuestionnairesApi apiInstance = new FlexV1InsightsQuestionnairesApi(defaultClient);
    String questionnaireSid = "questionnaireSid_example"; // String | The SID of the questionnaire
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    try {
      FlexV1InsightsQuestionnaires result = apiInstance.fetchInsightsQuestionnaires(questionnaireSid, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InsightsQuestionnairesApi#fetchInsightsQuestionnaires");
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
| **questionnaireSid** | **String**| The SID of the questionnaire | |
| **authorization** | **String**| The Authorization HTTP request header | [optional] |

### Return type

[**FlexV1InsightsQuestionnaires**](FlexV1InsightsQuestionnaires.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listInsightsQuestionnaires"></a>
# **listInsightsQuestionnaires**
> ListInsightsQuestionnairesResponse listInsightsQuestionnaires(authorization, includeInactive, pageSize, page, pageToken)



To get all questionnaires with questions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InsightsQuestionnairesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InsightsQuestionnairesApi apiInstance = new FlexV1InsightsQuestionnairesApi(defaultClient);
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    Boolean includeInactive = true; // Boolean | Flag indicating whether to include inactive questionnaires or not
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListInsightsQuestionnairesResponse result = apiInstance.listInsightsQuestionnaires(authorization, includeInactive, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InsightsQuestionnairesApi#listInsightsQuestionnaires");
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
| **includeInactive** | **Boolean**| Flag indicating whether to include inactive questionnaires or not | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListInsightsQuestionnairesResponse**](ListInsightsQuestionnairesResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateInsightsQuestionnaires"></a>
# **updateInsightsQuestionnaires**
> FlexV1InsightsQuestionnaires updateInsightsQuestionnaires(questionnaireSid, active, authorization, description, name, questionSids)



To update the questionnaire

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FlexV1InsightsQuestionnairesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://flex-api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    FlexV1InsightsQuestionnairesApi apiInstance = new FlexV1InsightsQuestionnairesApi(defaultClient);
    String questionnaireSid = "questionnaireSid_example"; // String | The SID of the questionnaire
    Boolean active = true; // Boolean | The flag to enable or disable questionnaire
    String authorization = "authorization_example"; // String | The Authorization HTTP request header
    String description = "description_example"; // String | The description of this questionnaire
    String name = "name_example"; // String | The name of this questionnaire
    List<String> questionSids = Arrays.asList(); // List<String> | The list of questions sids under a questionnaire
    try {
      FlexV1InsightsQuestionnaires result = apiInstance.updateInsightsQuestionnaires(questionnaireSid, active, authorization, description, name, questionSids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FlexV1InsightsQuestionnairesApi#updateInsightsQuestionnaires");
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
| **questionnaireSid** | **String**| The SID of the questionnaire | |
| **active** | **Boolean**| The flag to enable or disable questionnaire | |
| **authorization** | **String**| The Authorization HTTP request header | [optional] |
| **description** | **String**| The description of this questionnaire | [optional] |
| **name** | **String**| The name of this questionnaire | [optional] |
| **questionSids** | [**List&lt;String&gt;**](String.md)| The list of questions sids under a questionnaire | [optional] |

### Return type

[**FlexV1InsightsQuestionnaires**](FlexV1InsightsQuestionnaires.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

