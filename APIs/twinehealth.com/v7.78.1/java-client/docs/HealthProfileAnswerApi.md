# HealthProfileAnswerApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchHealthProfileAnswer**](HealthProfileAnswerApi.md#fetchHealthProfileAnswer) | **GET** /health_profile_answer/{id} | Get a health profile answer |
| [**fetchHealthProfileAnswers**](HealthProfileAnswerApi.md#fetchHealthProfileAnswers) | **GET** /health_profile_answer | List health profile answers |


<a id="fetchHealthProfileAnswer"></a>
# **fetchHealthProfileAnswer**
> FetchHealthProfileAnswerResponse fetchHealthProfileAnswer(id, include)

Get a health profile answer

Get a health profile answer by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthProfileAnswerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    HealthProfileAnswerApi apiInstance = new HealthProfileAnswerApi(defaultClient);
    String id = "id_example"; // String | Health profile answer identifier
    String include = "patient"; // String | List of related resources to include in the response
    try {
      FetchHealthProfileAnswerResponse result = apiInstance.fetchHealthProfileAnswer(id, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthProfileAnswerApi#fetchHealthProfileAnswer");
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
| **id** | **String**| Health profile answer identifier | |
| **include** | **String**| List of related resources to include in the response | [optional] [enum: patient] |

### Return type

[**FetchHealthProfileAnswerResponse**](FetchHealthProfileAnswerResponse.md)

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

<a id="fetchHealthProfileAnswers"></a>
# **fetchHealthProfileAnswers**
> FetchHealthProfileAnswersResponse fetchHealthProfileAnswers(filterPatient, filterGroups, filterOrganization, pageNumber, pageSize, pageLimit, pageCursor, include)

List health profile answers

Get a list of health profile answers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthProfileAnswerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    HealthProfileAnswerApi apiInstance = new HealthProfileAnswerApi(defaultClient);
    String filterPatient = "filterPatient_example"; // String | Patient id to fetch healt profile answers. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, or `filter[organization]`. 
    String filterGroups = "filterGroups_example"; // String | Comma-separated list of group ids. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, or `filter[organization]`. 
    String filterOrganization = "filterOrganization_example"; // String | Fitbit Plus organization id. Note that one of the following filters must be specified: `filter[patient]`, `filter[group]`, or `filter[organization]`. 
    Integer pageNumber = 1; // Integer | Page number
    Integer pageSize = 50; // Integer | Page size
    Integer pageLimit = 50; // Integer | Page limit
    String pageCursor = "pageCursor_example"; // String | Page cursor
    String include = "patient"; // String | List of related resources to include in the response
    try {
      FetchHealthProfileAnswersResponse result = apiInstance.fetchHealthProfileAnswers(filterPatient, filterGroups, filterOrganization, pageNumber, pageSize, pageLimit, pageCursor, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthProfileAnswerApi#fetchHealthProfileAnswers");
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
| **filterPatient** | **String**| Patient id to fetch healt profile answers. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;.  | [optional] |
| **filterGroups** | **String**| Comma-separated list of group ids. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;.  | [optional] |
| **filterOrganization** | **String**| Fitbit Plus organization id. Note that one of the following filters must be specified: &#x60;filter[patient]&#x60;, &#x60;filter[group]&#x60;, or &#x60;filter[organization]&#x60;.  | [optional] |
| **pageNumber** | **Integer**| Page number | [optional] [default to 1] |
| **pageSize** | **Integer**| Page size | [optional] [default to 50] |
| **pageLimit** | **Integer**| Page limit | [optional] [default to 50] |
| **pageCursor** | **String**| Page cursor | [optional] |
| **include** | **String**| List of related resources to include in the response | [optional] [enum: patient] |

### Return type

[**FetchHealthProfileAnswersResponse**](FetchHealthProfileAnswersResponse.md)

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

