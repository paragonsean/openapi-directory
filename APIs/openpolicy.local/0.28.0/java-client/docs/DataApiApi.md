# DataApiApi

All URIs are relative to *http://openpolicy.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteDocument**](DataApiApi.md#deleteDocument) | **DELETE** /v1/data/{path} | Delete a document |
| [**getDocument**](DataApiApi.md#getDocument) | **GET** /v1/data/{path} | Get a document |
| [**getDocumentWithPath**](DataApiApi.md#getDocumentWithPath) | **POST** /v1/data/{path} | Get a document (with input) |
| [**getDocumentWithWebHook**](DataApiApi.md#getDocumentWithWebHook) | **POST** /v0/data/{path} | Get a document (with webhook) |
| [**patchDocument**](DataApiApi.md#patchDocument) | **PATCH** /v1/data/{path} | Update a document |
| [**putDocument**](DataApiApi.md#putDocument) | **PUT** /v1/data/{path} | Create or overwrite a document |


<a id="deleteDocument"></a>
# **deleteDocument**
> deleteDocument(path)

Delete a document

This API endpoint deletes an existing document from the server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openpolicy.local");

    DataApiApi apiInstance = new DataApiApi(defaultClient);
    String path = "opa/examples/public_servers"; // String | A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404.
    try {
      apiInstance.deleteDocument(path);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApiApi#deleteDocument");
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
| **path** | **String**| A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404. | |

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
| **204** | Success |  -  |
| **404** | Not found (for example, a requested policy module or document does not exist) |  -  |
| **500** | Server error |  -  |

<a id="getDocument"></a>
# **getDocument**
> GetDocumentWithWebHook200Response getDocument(path, input, pretty, provenance, explain, metrics, instrument)

Get a document

This API endpoint returns the document specified by &#x60;path&#x60;.  The server will return a *bad request* (400) response if either: - The query requires an input document and you do not provide it - You provide the input document but the query has already defined it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openpolicy.local");

    DataApiApi apiInstance = new DataApiApi(defaultClient);
    String path = "opa/examples/public_servers"; // String | A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404.
    Map<String, Object> input = new HashMap(); // Map<String, Object> | Provide the text for an [input document](https://www.openpolicyagent.org/docs/latest/kubernetes-primer/#input-document) in JSON format
    Boolean pretty = true; // Boolean | If true, response will be in a human-readable format.
    Boolean provenance = false; // Boolean | If true, response will include build and version information in addition to the result.
    String explain = "full"; // String | If set to *full*, response will include query explanations in addition to the result.
    Boolean metrics = false; // Boolean | If true, compiler performance metrics will be returned in the response.
    Boolean instrument = false; // Boolean | If true, response will return additional performance metrics in addition to the result and the standard metrics.  **Caution:** This can add significant overhead to query evaluation. The recommendation is to only use this parameter if you are debugging a performance problem.
    try {
      GetDocumentWithWebHook200Response result = apiInstance.getDocument(path, input, pretty, provenance, explain, metrics, instrument);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApiApi#getDocument");
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
| **path** | **String**| A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404. | |
| **input** | [**Map&lt;String, Object&gt;**](Object.md)| Provide the text for an [input document](https://www.openpolicyagent.org/docs/latest/kubernetes-primer/#input-document) in JSON format | [optional] |
| **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] |
| **provenance** | **Boolean**| If true, response will include build and version information in addition to the result. | [optional] |
| **explain** | **String**| If set to *full*, response will include query explanations in addition to the result. | [optional] |
| **metrics** | **Boolean**| If true, compiler performance metrics will be returned in the response. | [optional] |
| **instrument** | **Boolean**| If true, response will return additional performance metrics in addition to the result and the standard metrics.  **Caution:** This can add significant overhead to query evaluation. The recommendation is to only use this parameter if you are debugging a performance problem. | [optional] |

### Return type

[**GetDocumentWithWebHook200Response**](GetDocumentWithWebHook200Response.md)

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

<a id="getDocumentWithPath"></a>
# **getDocumentWithPath**
> GetDocumentWithWebHook200Response getDocumentWithPath(path, requestBody, pretty, provenance, explain, metrics, instrument)

Get a document (with input)

The server will return a *bad request* (400) response if either: - The query requires an input document and you do not provide it - You provided an input document but the query has already defined it.  If &#x60;path&#x60; indexes into an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, a *not found* response (404) will be returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openpolicy.local");

    DataApiApi apiInstance = new DataApiApi(defaultClient);
    String path = "opa/examples/public_servers"; // String | A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404.
    Map<String, Object> requestBody = null; // Map<String, Object> | The input document (in JSON format)
    Boolean pretty = true; // Boolean | If true, response will be in a human-readable format.
    Boolean provenance = false; // Boolean | If true, response will include build and version information in addition to the result.
    String explain = "full"; // String | If set to *full*, response will include query explanations in addition to the result.
    Boolean metrics = false; // Boolean | If true, compiler performance metrics will be returned in the response.
    Boolean instrument = false; // Boolean | If true, response will return additional performance metrics in addition to the result and the standard metrics.  **Caution:** This can add significant overhead to query evaluation. The recommendation is to only use this parameter if you are debugging a performance problem.
    try {
      GetDocumentWithWebHook200Response result = apiInstance.getDocumentWithPath(path, requestBody, pretty, provenance, explain, metrics, instrument);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApiApi#getDocumentWithPath");
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
| **path** | **String**| A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404. | |
| **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)| The input document (in JSON format) | |
| **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] |
| **provenance** | **Boolean**| If true, response will include build and version information in addition to the result. | [optional] |
| **explain** | **String**| If set to *full*, response will include query explanations in addition to the result. | [optional] |
| **metrics** | **Boolean**| If true, compiler performance metrics will be returned in the response. | [optional] |
| **instrument** | **Boolean**| If true, response will return additional performance metrics in addition to the result and the standard metrics.  **Caution:** This can add significant overhead to query evaluation. The recommendation is to only use this parameter if you are debugging a performance problem. | [optional] |

### Return type

[**GetDocumentWithWebHook200Response**](GetDocumentWithWebHook200Response.md)

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

<a id="getDocumentWithWebHook"></a>
# **getDocumentWithWebHook**
> GetDocumentWithWebHook200Response getDocumentWithWebHook(path, requestBody, pretty)

Get a document (with webhook)

The example given here assumes you have created a policy (with &#x60;PUT /v1/policies/{path}&#x60;), such as:    &#x60;&#x60;&#x60;yaml   package opa.examples   import input.example.flag   allow_request { flag &#x3D;&#x3D; true }   &#x60;&#x60;&#x60;  The server will return a *not found* (404) response if the requested document is missing or undefined. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openpolicy.local");

    DataApiApi apiInstance = new DataApiApi(defaultClient);
    String path = "opa/examples/allow_request"; // String | A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404.
    Map<String, Object> requestBody = null; // Map<String, Object> | The input document (in JSON format)
    Boolean pretty = true; // Boolean | If true, response will be in a human-readable format.
    try {
      GetDocumentWithWebHook200Response result = apiInstance.getDocumentWithWebHook(path, requestBody, pretty);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApiApi#getDocumentWithWebHook");
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
| **path** | **String**| A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404. | |
| **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)| The input document (in JSON format) | |
| **pretty** | **Boolean**| If true, response will be in a human-readable format. | [optional] |

### Return type

[**GetDocumentWithWebHook200Response**](GetDocumentWithWebHook200Response.md)

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
| **404** | Not found (for example, a requested policy module or document does not exist) |  -  |
| **500** | Server error |  -  |

<a id="patchDocument"></a>
# **patchDocument**
> patchDocument(path, patchesSchemaInner)

Update a document

This API endpoint updates an existing document on the server by describing the changes required (using [JSON patch operations](http://jsonpatch.com/))

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openpolicy.local");

    DataApiApi apiInstance = new DataApiApi(defaultClient);
    String path = "opa/examples/public_servers"; // String | A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404.
    List<PatchesSchemaInner> patchesSchemaInner = Arrays.asList(); // List<PatchesSchemaInner> | The list of JSON patch operations.
    try {
      apiInstance.patchDocument(path, patchesSchemaInner);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApiApi#patchDocument");
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
| **path** | **String**| A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404. | |
| **patchesSchemaInner** | [**List&lt;PatchesSchemaInner&gt;**](PatchesSchemaInner.md)| The list of JSON patch operations. | |

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
| **204** | Success |  -  |
| **400** | Bad request |  -  |
| **404** | Not found (for example, a requested policy module or document does not exist) |  -  |
| **500** | Server error |  -  |

<a id="putDocument"></a>
# **putDocument**
> putDocument(path, body, ifNoneMatch)

Create or overwrite a document

If the path does not refer to an existing document (for example *us-west/servers*), the server will attempt to create all the necessary containing documents.  This behavior is similar to the Unix command [mkdir -p](https://en.wikipedia.org/wiki/Mkdir#Options).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://openpolicy.local");

    DataApiApi apiInstance = new DataApiApi(defaultClient);
    String path = "opa/examples/public_servers"; // String | A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404.
    Object body = null; // Object | The JSON document to write to the specified path.
    String ifNoneMatch = "*"; // String | The server will respect the If-None-Match header if it is set to * (in other words, it will not overwrite an existing document located at the specified `path`).
    try {
      apiInstance.putDocument(path, body, ifNoneMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataApiApi#putDocument");
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
| **path** | **String**| A backslash (/) delimited path to access values inside object and array documents. If the path points to an array, the server will attempt to convert the array index to an integer. If the path element cannot be converted to an integer, the server will respond with 404. | |
| **body** | **Object**| The JSON document to write to the specified path. | |
| **ifNoneMatch** | **String**| The server will respect the If-None-Match header if it is set to * (in other words, it will not overwrite an existing document located at the specified &#x60;path&#x60;). | [optional] |

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
| **204** | Success |  -  |
| **304** | Document was not modified |  -  |
| **400** | Bad request |  -  |
| **404** | Not found (for example, a requested policy module or document does not exist) |  -  |
| **500** | Server error |  -  |

