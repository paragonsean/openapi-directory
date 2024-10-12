# QueryApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getQuerySuggestions**](QueryApi.md#getQuerySuggestions) | **GET** /query/suggestions | Retrieve query suggestions |
| [**getQuerySuggestionsName**](QueryApi.md#getQuerySuggestionsName) | **GET** /query/suggestions/{name} | Retrieve query suggestions for a branching suggestion |
| [**postQuery**](QueryApi.md#postQuery) | **POST** /query | Query InfluxDB |
| [**postQueryAnalyze**](QueryApi.md#postQueryAnalyze) | **POST** /query/analyze | Analyze an InfluxQL or Flux query |
| [**postQueryAst**](QueryApi.md#postQueryAst) | **POST** /query/ast | Generate an Abstract Syntax Tree (AST) from a query |


<a id="getQuerySuggestions"></a>
# **getQuerySuggestions**
> FluxSuggestions getQuerySuggestions(zapTraceSpan)

Retrieve query suggestions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    QueryApi apiInstance = new QueryApi(defaultClient);
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      FluxSuggestions result = apiInstance.getQuerySuggestions(zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#getQuerySuggestions");
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
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**FluxSuggestions**](FluxSuggestions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Suggestions for next functions in call chain |  -  |
| **0** | Any response other than 200 is an internal server error |  -  |

<a id="getQuerySuggestionsName"></a>
# **getQuerySuggestionsName**
> FluxSuggestion getQuerySuggestionsName(name, zapTraceSpan)

Retrieve query suggestions for a branching suggestion

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    QueryApi apiInstance = new QueryApi(defaultClient);
    String name = "name_example"; // String | The name of the branching suggestion.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      FluxSuggestion result = apiInstance.getQuerySuggestionsName(name, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#getQuerySuggestionsName");
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
| **name** | **String**| The name of the branching suggestion. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**FluxSuggestion**](FluxSuggestion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Suggestions for next functions in call chain |  -  |
| **0** | Any response other than 200 is an internal server error |  -  |

<a id="postQuery"></a>
# **postQuery**
> File postQuery(zapTraceSpan, acceptEncoding, contentType, org, orgID, postQueryRequest)

Query InfluxDB

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    QueryApi apiInstance = new QueryApi(defaultClient);
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String acceptEncoding = "gzip"; // String | The Accept-Encoding request HTTP header advertises which content encoding, usually a compression algorithm, the client is able to understand.
    String contentType = "application/json"; // String | 
    String org = "org_example"; // String | Specifies the name of the organization executing the query. Takes either the ID or Name interchangeably. If both `orgID` and `org` are specified, `org` takes precedence.
    String orgID = "orgID_example"; // String | Specifies the ID of the organization executing the query. If both `orgID` and `org` are specified, `org` takes precedence.
    PostQueryRequest postQueryRequest = new PostQueryRequest(); // PostQueryRequest | Flux query or specification to execute
    try {
      File result = apiInstance.postQuery(zapTraceSpan, acceptEncoding, contentType, org, orgID, postQueryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#postQuery");
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
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **acceptEncoding** | **String**| The Accept-Encoding request HTTP header advertises which content encoding, usually a compression algorithm, the client is able to understand. | [optional] [default to identity] [enum: gzip, identity] |
| **contentType** | **String**|  | [optional] [enum: application/json, application/vnd.flux] |
| **org** | **String**| Specifies the name of the organization executing the query. Takes either the ID or Name interchangeably. If both &#x60;orgID&#x60; and &#x60;org&#x60; are specified, &#x60;org&#x60; takes precedence. | [optional] |
| **orgID** | **String**| Specifies the ID of the organization executing the query. If both &#x60;orgID&#x60; and &#x60;org&#x60; are specified, &#x60;org&#x60; takes precedence. | [optional] |
| **postQueryRequest** | [**PostQueryRequest**](PostQueryRequest.md)| Flux query or specification to execute | [optional] |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.flux
 - **Accept**: application/vnd.influx.arrow, text/csv, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Query results |  * Content-Encoding - The Content-Encoding entity header is used to compress the media-type.  When present, its value indicates which encodings were applied to the entity-body <br>  * Trace-Id - The Trace-Id header reports the request&#39;s trace ID, if one was generated. <br>  |
| **429** | Token is temporarily over quota. The Retry-After header describes when to try the read again. |  * Retry-After - A non-negative decimal integer indicating the seconds to delay after the response is received. <br>  |
| **0** | Error processing query |  -  |

<a id="postQueryAnalyze"></a>
# **postQueryAnalyze**
> AnalyzeQueryResponse postQueryAnalyze(zapTraceSpan, contentType, query)

Analyze an InfluxQL or Flux query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    QueryApi apiInstance = new QueryApi(defaultClient);
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String contentType = "application/json"; // String | 
    Query query = new Query(); // Query | Flux or InfluxQL query to analyze
    try {
      AnalyzeQueryResponse result = apiInstance.postQueryAnalyze(zapTraceSpan, contentType, query);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#postQueryAnalyze");
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
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **contentType** | **String**|  | [optional] [enum: application/json] |
| **query** | [**Query**](Query.md)| Flux or InfluxQL query to analyze | [optional] |

### Return type

[**AnalyzeQueryResponse**](AnalyzeQueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Query analyze results. Errors will be empty if the query is valid. |  -  |
| **0** | Internal server error |  * X-Influx-Error - Error string describing the problem <br>  * X-Influx-Reference - Reference code unique to the error type <br>  |

<a id="postQueryAst"></a>
# **postQueryAst**
> ASTResponse postQueryAst(zapTraceSpan, contentType, languageRequest)

Generate an Abstract Syntax Tree (AST) from a query

Analyzes flux query and generates a query specification.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    QueryApi apiInstance = new QueryApi(defaultClient);
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String contentType = "application/json"; // String | 
    LanguageRequest languageRequest = new LanguageRequest(); // LanguageRequest | Analyzed Flux query to generate abstract syntax tree.
    try {
      ASTResponse result = apiInstance.postQueryAst(zapTraceSpan, contentType, languageRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApi#postQueryAst");
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
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **contentType** | **String**|  | [optional] [enum: application/json] |
| **languageRequest** | [**LanguageRequest**](LanguageRequest.md)| Analyzed Flux query to generate abstract syntax tree. | [optional] |

### Return type

[**ASTResponse**](ASTResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Abstract syntax tree of the flux query. |  -  |
| **0** | Any response other than 200 is an internal server error |  -  |

