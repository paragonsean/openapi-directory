# SalesEntriesApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesEntriesDelete**](SalesEntriesApi.md#salesEntriesDelete) | **DELETE** /v1/salesEntries/{id} | Removes an existing Sales Entry. |
| [**salesEntriesGet**](SalesEntriesApi.md#salesEntriesGet) | **GET** /v1/salesEntries | Returns a list of company&#39;s Sales Entries. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field. |
| [**salesEntriesPost**](SalesEntriesApi.md#salesEntriesPost) | **POST** /v1/salesEntries | Creates a new Sales Entry. |
| [**salesEntriesProcessBatch**](SalesEntriesApi.md#salesEntriesProcessBatch) | **PUT** /v1/salesEntries/batch | Processes a batch of Sales Entries. |
| [**salesEntriesPut**](SalesEntriesApi.md#salesEntriesPut) | **PUT** /v1/salesEntries/{id} | Updates an existing Sales Entry. |
| [**v1SalesEntriesIdGet**](SalesEntriesApi.md#v1SalesEntriesIdGet) | **GET** /v1/salesEntries/{id} | Returns information about a single Sales Entry. |


<a id="salesEntriesDelete"></a>
# **salesEntriesDelete**
> Object salesEntriesDelete(id, timestamp)

Removes an existing Sales Entry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesEntriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesEntriesApi apiInstance = new SalesEntriesApi(defaultClient);
    Long id = 56L; // Long | Id of Sales Entry to remove.
    String timestamp = "timestamp_example"; // String | Timestamp of Sales Entry to remove. Should be encoded in Base64.
    try {
      Object result = apiInstance.salesEntriesDelete(id, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesEntriesApi#salesEntriesDelete");
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
| **id** | **Long**| Id of Sales Entry to remove. | |
| **timestamp** | **String**| Timestamp of Sales Entry to remove. Should be encoded in Base64. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesEntriesGet"></a>
# **salesEntriesGet**
> PageResultSalesEntryQueryDto salesEntriesGet()

Returns a list of company&#39;s Sales Entries. Supports OData querying protocol.  Filtering is allowed by \&quot;entryDate\&quot; field.  Ordering is allowed by \&quot;id\&quot; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesEntriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesEntriesApi apiInstance = new SalesEntriesApi(defaultClient);
    try {
      PageResultSalesEntryQueryDto result = apiInstance.salesEntriesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesEntriesApi#salesEntriesGet");
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

[**PageResultSalesEntryQueryDto**](PageResultSalesEntryQueryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesEntriesPost"></a>
# **salesEntriesPost**
> Object salesEntriesPost(salesEntryDto)

Creates a new Sales Entry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesEntriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesEntriesApi apiInstance = new SalesEntriesApi(defaultClient);
    SalesEntryDto salesEntryDto = new SalesEntryDto(); // SalesEntryDto | Information of Sales Entry to create.
    try {
      Object result = apiInstance.salesEntriesPost(salesEntryDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesEntriesApi#salesEntriesPost");
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
| **salesEntryDto** | [**SalesEntryDto**](SalesEntryDto.md)| Information of Sales Entry to create. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesEntriesProcessBatch"></a>
# **salesEntriesProcessBatch**
> Object salesEntriesProcessBatch(batchItemSalesEntryDto)

Processes a batch of Sales Entries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesEntriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesEntriesApi apiInstance = new SalesEntriesApi(defaultClient);
    List<BatchItemSalesEntryDto> batchItemSalesEntryDto = Arrays.asList(); // List<BatchItemSalesEntryDto> | Batch of Sales Entries to process.
    try {
      Object result = apiInstance.salesEntriesProcessBatch(batchItemSalesEntryDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesEntriesApi#salesEntriesProcessBatch");
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
| **batchItemSalesEntryDto** | [**List&lt;BatchItemSalesEntryDto&gt;**](BatchItemSalesEntryDto.md)| Batch of Sales Entries to process. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="salesEntriesPut"></a>
# **salesEntriesPut**
> Object salesEntriesPut(id, salesEntryDto)

Updates an existing Sales Entry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesEntriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesEntriesApi apiInstance = new SalesEntriesApi(defaultClient);
    Long id = 56L; // Long | Id of Sales Entry to update.
    SalesEntryDto salesEntryDto = new SalesEntryDto(); // SalesEntryDto | Information of Sales Entry to update.
    try {
      Object result = apiInstance.salesEntriesPut(id, salesEntryDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesEntriesApi#salesEntriesPut");
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
| **id** | **Long**| Id of Sales Entry to update. | |
| **salesEntryDto** | [**SalesEntryDto**](SalesEntryDto.md)| Information of Sales Entry to update. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="v1SalesEntriesIdGet"></a>
# **v1SalesEntriesIdGet**
> SalesEntryDto v1SalesEntriesIdGet(id)

Returns information about a single Sales Entry.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesEntriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    SalesEntriesApi apiInstance = new SalesEntriesApi(defaultClient);
    Long id = 56L; // Long | Id of Sales Entry to return.
    try {
      SalesEntryDto result = apiInstance.v1SalesEntriesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesEntriesApi#v1SalesEntriesIdGet");
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
| **id** | **Long**| Id of Sales Entry to return. | |

### Return type

[**SalesEntryDto**](SalesEntryDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

