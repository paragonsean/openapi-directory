# SchemesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV20DatabaseSchemesBarcodeGet**](SchemesApi.md#apiV20DatabaseSchemesBarcodeGet) | **GET** /api/v2.0/{database}/schemes/{barcode} |  |
| [**apiV20DatabaseSchemesBarcodePost**](SchemesApi.md#apiV20DatabaseSchemesBarcodePost) | **POST** /api/v2.0/{database}/schemes/{barcode} |  |
| [**apiV20DatabaseSchemesBarcodePut**](SchemesApi.md#apiV20DatabaseSchemesBarcodePut) | **PUT** /api/v2.0/{database}/schemes/{barcode} |  |
| [**apiV20DatabaseSchemesGet**](SchemesApi.md#apiV20DatabaseSchemesGet) | **GET** /api/v2.0/{database}/schemes |  |


<a id="apiV20DatabaseSchemesBarcodeGet"></a>
# **apiV20DatabaseSchemesBarcodeGet**
> apiV20DatabaseSchemesBarcodeGet(database, barcode, apiV20DatabaseSchemesBarcodeGetRequest)



Genotyping schemes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchemesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SchemesApi apiInstance = new SchemesApi(defaultClient);
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    String barcode = "barcode_example"; // String | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
    ApiV20DatabaseSchemesBarcodeGetRequest apiV20DatabaseSchemesBarcodeGetRequest = new ApiV20DatabaseSchemesBarcodeGetRequest(); // ApiV20DatabaseSchemesBarcodeGetRequest | 
    try {
      apiInstance.apiV20DatabaseSchemesBarcodeGet(database, barcode, apiV20DatabaseSchemesBarcodeGetRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchemesApi#apiV20DatabaseSchemesBarcodeGet");
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
| **barcode** | **String**| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | |
| **apiV20DatabaseSchemesBarcodeGetRequest** | [**ApiV20DatabaseSchemesBarcodeGetRequest**](ApiV20DatabaseSchemesBarcodeGetRequest.md)|  | [optional] |

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
| **200** | List of schemes objects |  -  |
| **403** | Unauthorised access for this specific resource |  -  |

<a id="apiV20DatabaseSchemesBarcodePost"></a>
# **apiV20DatabaseSchemesBarcodePost**
> apiV20DatabaseSchemesBarcodePost(database, barcode, apiV20DatabaseSchemesBarcodeGetRequest)



Genotyping schemes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchemesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SchemesApi apiInstance = new SchemesApi(defaultClient);
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    String barcode = "barcode_example"; // String | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
    ApiV20DatabaseSchemesBarcodeGetRequest apiV20DatabaseSchemesBarcodeGetRequest = new ApiV20DatabaseSchemesBarcodeGetRequest(); // ApiV20DatabaseSchemesBarcodeGetRequest | 
    try {
      apiInstance.apiV20DatabaseSchemesBarcodePost(database, barcode, apiV20DatabaseSchemesBarcodeGetRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchemesApi#apiV20DatabaseSchemesBarcodePost");
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
| **barcode** | **String**| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | |
| **apiV20DatabaseSchemesBarcodeGetRequest** | [**ApiV20DatabaseSchemesBarcodeGetRequest**](ApiV20DatabaseSchemesBarcodeGetRequest.md)|  | [optional] |

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
| **200** | List of schemes objects |  -  |
| **403** | Unauthorised access for this specific resource |  -  |

<a id="apiV20DatabaseSchemesBarcodePut"></a>
# **apiV20DatabaseSchemesBarcodePut**
> apiV20DatabaseSchemesBarcodePut(database, barcode, apiV20DatabaseSchemesBarcodeGetRequest)



Genotyping schemes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchemesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SchemesApi apiInstance = new SchemesApi(defaultClient);
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    String barcode = "barcode_example"; // String | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
    ApiV20DatabaseSchemesBarcodeGetRequest apiV20DatabaseSchemesBarcodeGetRequest = new ApiV20DatabaseSchemesBarcodeGetRequest(); // ApiV20DatabaseSchemesBarcodeGetRequest | 
    try {
      apiInstance.apiV20DatabaseSchemesBarcodePut(database, barcode, apiV20DatabaseSchemesBarcodeGetRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchemesApi#apiV20DatabaseSchemesBarcodePut");
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
| **barcode** | **String**| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | |
| **apiV20DatabaseSchemesBarcodeGetRequest** | [**ApiV20DatabaseSchemesBarcodeGetRequest**](ApiV20DatabaseSchemesBarcodeGetRequest.md)|  | [optional] |

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

<a id="apiV20DatabaseSchemesGet"></a>
# **apiV20DatabaseSchemesGet**
> apiV20DatabaseSchemesGet(database, barcode, orderby, offset, label, onlyFields, created, lastmodified, sortorder, limit, schemeName, version)



Genotyping schemes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchemesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SchemesApi apiInstance = new SchemesApi(defaultClient);
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    List<String> barcode = Arrays.asList(); // List<String> | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
    String orderby = "barcode"; // String | Field to order by. Default: barcode
    Integer offset = 0; // Integer | Cursor position in results
    String label = "label_example"; // String | 
    List<String> onlyFields = Arrays.asList(); // List<String> | 
    OffsetDateTime created = OffsetDateTime.now(); // OffsetDateTime | 
    OffsetDateTime lastmodified = OffsetDateTime.now(); // OffsetDateTime | 
    String sortorder = "asc"; // String | Order of search results: asc or desc
    Integer limit = 50; // Integer | Number of results per page
    String schemeName = "schemeName_example"; // String | 
    Integer version = 56; // Integer | 
    try {
      apiInstance.apiV20DatabaseSchemesGet(database, barcode, orderby, offset, label, onlyFields, created, lastmodified, sortorder, limit, schemeName, version);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchemesApi#apiV20DatabaseSchemesGet");
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
| **barcode** | [**List&lt;String&gt;**](String.md)| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | [optional] |
| **orderby** | **String**| Field to order by. Default: barcode | [optional] [default to barcode] |
| **offset** | **Integer**| Cursor position in results | [optional] [default to 0] |
| **label** | **String**|  | [optional] |
| **onlyFields** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **created** | **OffsetDateTime**|  | [optional] |
| **lastmodified** | **OffsetDateTime**|  | [optional] |
| **sortorder** | **String**| Order of search results: asc or desc | [optional] [default to asc] |
| **limit** | **Integer**| Number of results per page | [optional] [default to 50] |
| **schemeName** | **String**|  | [optional] |
| **version** | **Integer**|  | [optional] |

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
| **200** | List of schemes objects |  -  |
| **403** | Unauthorised access for this specific resource |  -  |

