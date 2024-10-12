# AssembliesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV20DatabaseAssembliesBarcodeGet**](AssembliesApi.md#apiV20DatabaseAssembliesBarcodeGet) | **GET** /api/v2.0/{database}/assemblies/{barcode} |  |
| [**apiV20DatabaseAssembliesBarcodePost**](AssembliesApi.md#apiV20DatabaseAssembliesBarcodePost) | **POST** /api/v2.0/{database}/assemblies/{barcode} |  |
| [**apiV20DatabaseAssembliesBarcodePut**](AssembliesApi.md#apiV20DatabaseAssembliesBarcodePut) | **PUT** /api/v2.0/{database}/assemblies/{barcode} |  |
| [**apiV20DatabaseAssembliesGet**](AssembliesApi.md#apiV20DatabaseAssembliesGet) | **GET** /api/v2.0/{database}/assemblies |  |


<a id="apiV20DatabaseAssembliesBarcodeGet"></a>
# **apiV20DatabaseAssembliesBarcodeGet**
> apiV20DatabaseAssembliesBarcodeGet(database, barcode, apiV20DatabaseAssembliesBarcodeGetRequest)



Genome assemblies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssembliesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AssembliesApi apiInstance = new AssembliesApi(defaultClient);
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    String barcode = "barcode_example"; // String | Unique barcode for Traces records, <database prefix>_<ID code>_AS e.g. SAL_AA0001AA_AS
    ApiV20DatabaseAssembliesBarcodeGetRequest apiV20DatabaseAssembliesBarcodeGetRequest = new ApiV20DatabaseAssembliesBarcodeGetRequest(); // ApiV20DatabaseAssembliesBarcodeGetRequest | 
    try {
      apiInstance.apiV20DatabaseAssembliesBarcodeGet(database, barcode, apiV20DatabaseAssembliesBarcodeGetRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssembliesApi#apiV20DatabaseAssembliesBarcodeGet");
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
| **barcode** | **String**| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_AS e.g. SAL_AA0001AA_AS | |
| **apiV20DatabaseAssembliesBarcodeGetRequest** | [**ApiV20DatabaseAssembliesBarcodeGetRequest**](ApiV20DatabaseAssembliesBarcodeGetRequest.md)|  | [optional] |

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
| **200** | List of assemblies objects |  -  |
| **403** | Unauthorised access for this specific resource |  -  |

<a id="apiV20DatabaseAssembliesBarcodePost"></a>
# **apiV20DatabaseAssembliesBarcodePost**
> apiV20DatabaseAssembliesBarcodePost(database, barcode, apiV20DatabaseAssembliesBarcodeGetRequest)



Genome assemblies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssembliesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AssembliesApi apiInstance = new AssembliesApi(defaultClient);
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    String barcode = "barcode_example"; // String | Unique barcode for Traces records, <database prefix>_<ID code>_AS e.g. SAL_AA0001AA_AS
    ApiV20DatabaseAssembliesBarcodeGetRequest apiV20DatabaseAssembliesBarcodeGetRequest = new ApiV20DatabaseAssembliesBarcodeGetRequest(); // ApiV20DatabaseAssembliesBarcodeGetRequest | 
    try {
      apiInstance.apiV20DatabaseAssembliesBarcodePost(database, barcode, apiV20DatabaseAssembliesBarcodeGetRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssembliesApi#apiV20DatabaseAssembliesBarcodePost");
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
| **barcode** | **String**| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_AS e.g. SAL_AA0001AA_AS | |
| **apiV20DatabaseAssembliesBarcodeGetRequest** | [**ApiV20DatabaseAssembliesBarcodeGetRequest**](ApiV20DatabaseAssembliesBarcodeGetRequest.md)|  | [optional] |

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
| **200** | List of assemblies objects |  -  |
| **403** | Unauthorised access for this specific resource |  -  |

<a id="apiV20DatabaseAssembliesBarcodePut"></a>
# **apiV20DatabaseAssembliesBarcodePut**
> apiV20DatabaseAssembliesBarcodePut(database, barcode, apiV20DatabaseAssembliesBarcodeGetRequest)



Genome assemblies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssembliesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AssembliesApi apiInstance = new AssembliesApi(defaultClient);
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    String barcode = "barcode_example"; // String | Unique barcode for Traces records, <database prefix>_<ID code>_AS e.g. SAL_AA0001AA_AS
    ApiV20DatabaseAssembliesBarcodeGetRequest apiV20DatabaseAssembliesBarcodeGetRequest = new ApiV20DatabaseAssembliesBarcodeGetRequest(); // ApiV20DatabaseAssembliesBarcodeGetRequest | 
    try {
      apiInstance.apiV20DatabaseAssembliesBarcodePut(database, barcode, apiV20DatabaseAssembliesBarcodeGetRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssembliesApi#apiV20DatabaseAssembliesBarcodePut");
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
| **barcode** | **String**| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_AS e.g. SAL_AA0001AA_AS | |
| **apiV20DatabaseAssembliesBarcodeGetRequest** | [**ApiV20DatabaseAssembliesBarcodeGetRequest**](ApiV20DatabaseAssembliesBarcodeGetRequest.md)|  | [optional] |

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

<a id="apiV20DatabaseAssembliesGet"></a>
# **apiV20DatabaseAssembliesGet**
> apiV20DatabaseAssembliesGet(database, n50, barcode, orderby, offset, assemblyStatus, uberstrain, topSpecies, onlyFields, reldate, sortorder, limit, version)



Genome assemblies

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssembliesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AssembliesApi apiInstance = new AssembliesApi(defaultClient);
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    Integer n50 = 56; // Integer | 
    List<String> barcode = Arrays.asList(); // List<String> | Unique barcode for Traces records, <database prefix>_<ID code>_AS e.g. SAL_AA0001AA_AS
    String orderby = "barcode"; // String | Field to order by. Default: barcode
    Integer offset = 0; // Integer | Cursor position in results
    String assemblyStatus = "assemblyStatus_example"; // String | 
    String uberstrain = "uberstrain_example"; // String | 
    String topSpecies = "topSpecies_example"; // String | 
    List<String> onlyFields = Arrays.asList(); // List<String> | 
    Integer reldate = 56; // Integer | 
    String sortorder = "asc"; // String | Order of search results: asc or desc
    Integer limit = 50; // Integer | Number of results per page
    Integer version = 56; // Integer | 
    try {
      apiInstance.apiV20DatabaseAssembliesGet(database, n50, barcode, orderby, offset, assemblyStatus, uberstrain, topSpecies, onlyFields, reldate, sortorder, limit, version);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssembliesApi#apiV20DatabaseAssembliesGet");
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
| **n50** | **Integer**|  | [optional] |
| **barcode** | [**List&lt;String&gt;**](String.md)| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_AS e.g. SAL_AA0001AA_AS | [optional] |
| **orderby** | **String**| Field to order by. Default: barcode | [optional] [default to barcode] |
| **offset** | **Integer**| Cursor position in results | [optional] [default to 0] |
| **assemblyStatus** | **String**|  | [optional] |
| **uberstrain** | **String**|  | [optional] |
| **topSpecies** | **String**|  | [optional] |
| **onlyFields** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **reldate** | **Integer**|  | [optional] |
| **sortorder** | **String**| Order of search results: asc or desc | [optional] [default to asc] |
| **limit** | **Integer**| Number of results per page | [optional] [default to 50] |
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
| **200** | List of assemblies objects |  -  |
| **403** | Unauthorised access for this specific resource |  -  |

