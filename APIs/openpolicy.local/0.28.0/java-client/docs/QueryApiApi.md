# QueryApiApi

All URIs are relative to *http://openpolicy.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getQuery**](QueryApiApi.md#getQuery) | **GET** /v1/query | Execute an ad-hoc query (simple) |
| [**postQuery**](QueryApiApi.md#postQuery) | **POST** /v1/query | Execute an ad-hoc query (complex) |
| [**postSimpleQuery**](QueryApiApi.md#postSimpleQuery) | **POST** / | Execute a simple query |


<a id="getQuery"></a>
# **getQuery**
> PostCompile200Response getQuery(q, pretty, explain, metrics)

Execute an ad-hoc query (simple)

This API endpoint returns bindings for the variables in the query.  For more complex JSON queries, use &#x60;POST /v1/query&#x60; instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openpolicy.local");

    QueryApiApi apiInstance = new QueryApiApi(defaultClient);
    String q = "{\"query\": \"data.servers[i].ports[_] = \\\"p2\\\"; data.servers[i].name = name\"}"; // String | The [URL-encoded](https://www.w3schools.com/tags/ref_urlencode.ASP) ad-hoc query to execute.
    Boolean pretty = true; // Boolean | If true, response will be in a human-readable format.
    String explain = "full"; // String | If set to *full*, response will include query explanations in addition to the result.
    Boolean metrics = false; // Boolean | If true, compiler performance metrics will be returned in the response.
    try {
      PostCompile200Response result = apiInstance.getQuery(q, pretty, explain, metrics);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApiApi#getQuery");
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
| **q** | **String**| The [URL-encoded](https://www.w3schools.com/tags/ref_urlencode.ASP) ad-hoc query to execute. | |
| **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] |
| **explain** | **String**| If set to *full*, response will include query explanations in addition to the result. | [optional] |
| **metrics** | **Boolean**| If true, compiler performance metrics will be returned in the response. | [optional] |

### Return type

[**PostCompile200Response**](PostCompile200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **500** | Server error |  -  |

<a id="postQuery"></a>
# **postQuery**
> PostCompile200Response postQuery(requestBody, pretty, explain, metrics)

Execute an ad-hoc query (complex)

This API endpoint returns bindings for the variables in the query.  For simpler JSON queries, you may use &#x60;GET /v1/query&#x60; instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openpolicy.local");

    QueryApiApi apiInstance = new QueryApiApi(defaultClient);
    Map<String, Object> requestBody = null; // Map<String, Object> | The test of the query (in JSON format)
    Boolean pretty = true; // Boolean | If true, response will be in a human-readable format.
    String explain = "full"; // String | If set to *full*, response will include query explanations in addition to the result.
    Boolean metrics = false; // Boolean | If true, compiler performance metrics will be returned in the response.
    try {
      PostCompile200Response result = apiInstance.postQuery(requestBody, pretty, explain, metrics);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApiApi#postQuery");
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
| **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)| The test of the query (in JSON format) | |
| **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] |
| **explain** | **String**| If set to *full*, response will include query explanations in addition to the result. | [optional] |
| **metrics** | **Boolean**| If true, compiler performance metrics will be returned in the response. | [optional] |

### Return type

[**PostCompile200Response**](PostCompile200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-yaml
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **500** | Server error |  -  |
| **501** | Streaming not implemented |  -  |

<a id="postSimpleQuery"></a>
# **postSimpleQuery**
> postSimpleQuery(requestBody, pretty)

Execute a simple query

This API queries the document at *_/data/system/main* by default (however, you can [configure OPA](https://www.openpolicyagent.org/docs/latest/configuration/) to use a different path to serve these queries). That document defines the response. For example, use the following in &#x60;PUT /v1/policies/{path}&#x60;) to define a rule that will produce a value for the *_/data/system/main* document:    &#x60;&#x60;&#x60;yaml   package system   main &#x3D; msg {     msg :&#x3D; sprintf(\&quot;hello, %v\&quot;, input.user)   }   &#x60;&#x60;&#x60;  The server will return a *not found* (404) response if *_/data/system/main* is undefined.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QueryApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openpolicy.local");

    QueryApiApi apiInstance = new QueryApiApi(defaultClient);
    Map<String, Object> requestBody = null; // Map<String, Object> | The text of the input document (in JSON format)
    Boolean pretty = true; // Boolean | If true, response will be in a human-readable format.
    try {
      apiInstance.postSimpleQuery(requestBody, pretty);
    } catch (ApiException e) {
      System.err.println("Exception when calling QueryApiApi#postSimpleQuery");
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
| **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)| The text of the input document (in JSON format) | |
| **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] |

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
| **200** | Success |  -  |
| **400** | Bad request |  -  |
| **404** | Not found (for example, a requested policy module or document does not exist) |  -  |
| **500** | Server error |  -  |

