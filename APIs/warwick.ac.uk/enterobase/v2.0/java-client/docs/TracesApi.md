# TracesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV20DatabaseTracesBarcodeGet**](TracesApi.md#apiV20DatabaseTracesBarcodeGet) | **GET** /api/v2.0/{database}/traces/{barcode} |  |
| [**apiV20DatabaseTracesBarcodePost**](TracesApi.md#apiV20DatabaseTracesBarcodePost) | **POST** /api/v2.0/{database}/traces/{barcode} |  |
| [**apiV20DatabaseTracesBarcodePut**](TracesApi.md#apiV20DatabaseTracesBarcodePut) | **PUT** /api/v2.0/{database}/traces/{barcode} |  |
| [**apiV20DatabaseTracesGet**](TracesApi.md#apiV20DatabaseTracesGet) | **GET** /api/v2.0/{database}/traces |  |


<a id="apiV20DatabaseTracesBarcodeGet"></a>
# **apiV20DatabaseTracesBarcodeGet**
> apiV20DatabaseTracesBarcodeGet(database, barcode, apiV20DatabaseTracesBarcodeGetRequest)



Traces (sequence-reads) metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TracesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    TracesApi apiInstance = new TracesApi(defaultClient);
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    String barcode = "barcode_example"; // String | Unique barcode for Traces records, <database prefix>_<ID code>_TR e.g. SAL_AA0001AA_TR
    ApiV20DatabaseTracesBarcodeGetRequest apiV20DatabaseTracesBarcodeGetRequest = new ApiV20DatabaseTracesBarcodeGetRequest(); // ApiV20DatabaseTracesBarcodeGetRequest | 
    try {
      apiInstance.apiV20DatabaseTracesBarcodeGet(database, barcode, apiV20DatabaseTracesBarcodeGetRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TracesApi#apiV20DatabaseTracesBarcodeGet");
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
| **database** | **String**| Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively | |
| **barcode** | **String**| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_TR e.g. SAL_AA0001AA_TR | |
| **apiV20DatabaseTracesBarcodeGetRequest** | [**ApiV20DatabaseTracesBarcodeGetRequest**](ApiV20DatabaseTracesBarcodeGetRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of traces objects |  -  |
| **403** | Unauthorised access for this specific resource |  -  |

<a id="apiV20DatabaseTracesBarcodePost"></a>
# **apiV20DatabaseTracesBarcodePost**
> apiV20DatabaseTracesBarcodePost(database, barcode, apiV20DatabaseTracesBarcodeGetRequest)



Traces (sequence-reads) metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TracesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    TracesApi apiInstance = new TracesApi(defaultClient);
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    String barcode = "barcode_example"; // String | Unique barcode for Traces records, <database prefix>_<ID code>_TR e.g. SAL_AA0001AA_TR
    ApiV20DatabaseTracesBarcodeGetRequest apiV20DatabaseTracesBarcodeGetRequest = new ApiV20DatabaseTracesBarcodeGetRequest(); // ApiV20DatabaseTracesBarcodeGetRequest | 
    try {
      apiInstance.apiV20DatabaseTracesBarcodePost(database, barcode, apiV20DatabaseTracesBarcodeGetRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TracesApi#apiV20DatabaseTracesBarcodePost");
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
| **database** | **String**| Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively | |
| **barcode** | **String**| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_TR e.g. SAL_AA0001AA_TR | |
| **apiV20DatabaseTracesBarcodeGetRequest** | [**ApiV20DatabaseTracesBarcodeGetRequest**](ApiV20DatabaseTracesBarcodeGetRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of traces objects |  -  |
| **403** | Unauthorised access for this specific resource |  -  |

<a id="apiV20DatabaseTracesBarcodePut"></a>
# **apiV20DatabaseTracesBarcodePut**
> apiV20DatabaseTracesBarcodePut(database, barcode, apiV20DatabaseTracesBarcodeGetRequest)



Traces (sequence-reads) metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TracesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    TracesApi apiInstance = new TracesApi(defaultClient);
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    String barcode = "barcode_example"; // String | Unique barcode for Traces records, <database prefix>_<ID code>_TR e.g. SAL_AA0001AA_TR
    ApiV20DatabaseTracesBarcodeGetRequest apiV20DatabaseTracesBarcodeGetRequest = new ApiV20DatabaseTracesBarcodeGetRequest(); // ApiV20DatabaseTracesBarcodeGetRequest | 
    try {
      apiInstance.apiV20DatabaseTracesBarcodePut(database, barcode, apiV20DatabaseTracesBarcodeGetRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TracesApi#apiV20DatabaseTracesBarcodePut");
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
| **database** | **String**| Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively | |
| **barcode** | **String**| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_TR e.g. SAL_AA0001AA_TR | |
| **apiV20DatabaseTracesBarcodeGetRequest** | [**ApiV20DatabaseTracesBarcodeGetRequest**](ApiV20DatabaseTracesBarcodeGetRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **403** | Unauthorised access for this specific resource |  -  |

<a id="apiV20DatabaseTracesGet"></a>
# **apiV20DatabaseTracesGet**
> apiV20DatabaseTracesGet(database, barcode, orderby, offset, onlyFields, sortorder, limit)



Traces (sequence-reads) metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TracesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    TracesApi apiInstance = new TracesApi(defaultClient);
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    List<String> barcode = Arrays.asList(); // List<String> | Unique barcode for Traces records, <database prefix>_<ID code>_TR e.g. SAL_AA0001AA_TR
    String orderby = "barcode"; // String | Field to order by. Default: barcode
    Integer offset = 0; // Integer | Cursor position in results
    List<String> onlyFields = Arrays.asList(); // List<String> | 
    String sortorder = "asc"; // String | Order of search results: asc or desc
    Integer limit = 50; // Integer | Number of results per page
    try {
      apiInstance.apiV20DatabaseTracesGet(database, barcode, orderby, offset, onlyFields, sortorder, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling TracesApi#apiV20DatabaseTracesGet");
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
| **database** | **String**| Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively | |
| **barcode** | [**List&lt;String&gt;**](String.md)| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_TR e.g. SAL_AA0001AA_TR | [optional] |
| **orderby** | **String**| Field to order by. Default: barcode | [optional] [default to barcode] |
| **offset** | **Integer**| Cursor position in results | [optional] [default to 0] |
| **onlyFields** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **sortorder** | **String**| Order of search results: asc or desc | [optional] [default to asc] |
| **limit** | **Integer**| Number of results per page | [optional] [default to 50] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of traces objects |  -  |
| **403** | Unauthorised access for this specific resource |  -  |

