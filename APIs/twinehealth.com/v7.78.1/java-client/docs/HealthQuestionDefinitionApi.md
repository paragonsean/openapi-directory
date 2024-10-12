# HealthQuestionDefinitionApi

All URIs are relative to *https://api.twinehealth.com/pub*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchHealthQuestionDefinition**](HealthQuestionDefinitionApi.md#fetchHealthQuestionDefinition) | **GET** /health_question_definition/{id} | Get a health question definition |
| [**fetchHealthQuestionDefinitions**](HealthQuestionDefinitionApi.md#fetchHealthQuestionDefinitions) | **GET** /health_question_definition | List health question definitions |


<a id="fetchHealthQuestionDefinition"></a>
# **fetchHealthQuestionDefinition**
> FetchHealthQuestionDefinitionResponse fetchHealthQuestionDefinition(id)

Get a health question definition

Get a health question definition by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthQuestionDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    HealthQuestionDefinitionApi apiInstance = new HealthQuestionDefinitionApi(defaultClient);
    String id = "id_example"; // String | Health question definition identifier
    try {
      FetchHealthQuestionDefinitionResponse result = apiInstance.fetchHealthQuestionDefinition(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthQuestionDefinitionApi#fetchHealthQuestionDefinition");
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
| **id** | **String**| Health question definition identifier | |

### Return type

[**FetchHealthQuestionDefinitionResponse**](FetchHealthQuestionDefinitionResponse.md)

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

<a id="fetchHealthQuestionDefinitions"></a>
# **fetchHealthQuestionDefinitions**
> FetchHealthQuestionDefinitionsResponse fetchHealthQuestionDefinitions()

List health question definitions

Get a list of all health question definitions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HealthQuestionDefinitionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twinehealth.com/pub");

    HealthQuestionDefinitionApi apiInstance = new HealthQuestionDefinitionApi(defaultClient);
    try {
      FetchHealthQuestionDefinitionsResponse result = apiInstance.fetchHealthQuestionDefinitions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HealthQuestionDefinitionApi#fetchHealthQuestionDefinitions");
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

[**FetchHealthQuestionDefinitionsResponse**](FetchHealthQuestionDefinitionsResponse.md)

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

