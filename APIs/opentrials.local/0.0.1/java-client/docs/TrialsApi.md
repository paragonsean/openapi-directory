# TrialsApi

All URIs are relative to *http://opentrials.local/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRecord**](TrialsApi.md#getRecord) | **GET** /trials/{trialId}/records/{id} |  |
| [**getRecords**](TrialsApi.md#getRecords) | **GET** /trials/{id}/records |  |
| [**getTrial**](TrialsApi.md#getTrial) | **GET** /trials/{id} |  |
| [**searchTrials**](TrialsApi.md#searchTrials) | **GET** /search |  |


<a id="getRecord"></a>
# **getRecord**
> Record getRecord(trialId, id)



Returns a trial&#39;s raw record from its sources

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://opentrials.local/v1");

    TrialsApi apiInstance = new TrialsApi(defaultClient);
    String trialId = "trialId_example"; // String | ID of the trial
    String id = "id_example"; // String | ID of the trial's record
    try {
      Record result = apiInstance.getRecord(trialId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrialsApi#getRecord");
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
| **trialId** | **String**| ID of the trial | |
| **id** | **String**| ID of the trial&#39;s record | |

### Return type

[**Record**](Record.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Trial not found |  -  |

<a id="getRecords"></a>
# **getRecords**
> List&lt;Record&gt; getRecords(id)



Returns a trial&#39;s raw records from its sources

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://opentrials.local/v1");

    TrialsApi apiInstance = new TrialsApi(defaultClient);
    String id = "id_example"; // String | ID of the trial
    try {
      List<Record> result = apiInstance.getRecords(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrialsApi#getRecords");
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
| **id** | **String**| ID of the trial | |

### Return type

[**List&lt;Record&gt;**](Record.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Trial not found |  -  |

<a id="getTrial"></a>
# **getTrial**
> Trial getTrial(id)



Returns a trial&#39;s details and related entities (e.g. &#x60;conditions&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://opentrials.local/v1");

    TrialsApi apiInstance = new TrialsApi(defaultClient);
    String id = "id_example"; // String | ID of the trial
    try {
      Trial result = apiInstance.getTrial(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrialsApi#getTrial");
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
| **id** | **String**| ID of the trial | |

### Return type

[**Trial**](Trial.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Trial not found |  -  |
| **0** | Error |  -  |

<a id="searchTrials"></a>
# **searchTrials**
> TrialSearchResults searchTrials(q, page, perPage)



Returns trials based on a search query. By default, it&#39;ll search in all of a trial&#39;s attributes. - &#x60;q&#x60; is a [ElasticSearch query string](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-query-string-query.html#query-string-syntax) (e.g. &#x60;public_title:(depressive OR depression)&#x60;) - &#x60;page&#x60; can take a value between &#x60;1&#x60; and &#x60;100&#x60; - &#x60;per_page&#x60; can take a value between &#x60;10&#x60; and &#x60;100&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://opentrials.local/v1");

    TrialsApi apiInstance = new TrialsApi(defaultClient);
    String q = "q_example"; // String | The search query (follows the [ElasticSearch Query String](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-query-string-query.html#query-string-syntax) syntax)
    Integer page = 1; // Integer | The page number
    Integer perPage = 20; // Integer | Number of items per page
    try {
      TrialSearchResults result = apiInstance.searchTrials(q, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrialsApi#searchTrials");
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
| **q** | **String**| The search query (follows the [ElasticSearch Query String](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-query-string-query.html#query-string-syntax) syntax) | [optional] |
| **page** | **Integer**| The page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of items per page | [optional] [default to 20] |

### Return type

[**TrialSearchResults**](TrialSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

