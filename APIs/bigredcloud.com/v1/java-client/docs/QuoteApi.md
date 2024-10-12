# QuoteApi

All URIs are relative to *https://app.bigredcloud.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteClose**](QuoteApi.md#quoteClose) | **PUT** /v1/quotes/close/{id} | Close a Quote. |
| [**quoteDelete**](QuoteApi.md#quoteDelete) | **DELETE** /v1/quotes/{id} | Removes an existing Quote. |
| [**quoteGet**](QuoteApi.md#quoteGet) | **GET** /v1/quotes | Returns a list of company&#39;s Quotes.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot;. |
| [**quotePost**](QuoteApi.md#quotePost) | **POST** /v1/quotes | Creates a new Quote. |
| [**quotePostCreateQuoteWithGeneratingReference**](QuoteApi.md#quotePostCreateQuoteWithGeneratingReference) | **POST** /v1/quotes/createQuoteWithGeneratingReference | Creates a new Quote with auto generating reference. |
| [**quotePostGenerateSaleInvoice**](QuoteApi.md#quotePostGenerateSaleInvoice) | **POST** /v1/quotes/generateSaleInvoice | Generate a sale invoice from a Quote.  When sale invoice is empty, new sale invoice will be generated from Quote. |
| [**quoteProcessBatch**](QuoteApi.md#quoteProcessBatch) | **PUT** /v1/quotes/batch | Processes a batch of Quote. |
| [**quotePut**](QuoteApi.md#quotePut) | **PUT** /v1/quotes/{id} | Updates an existing Quote. |
| [**quoteReopen**](QuoteApi.md#quoteReopen) | **PUT** /v1/quotes/reopen/{id} | Reopen a Quote. |
| [**v1QuotesIdGet**](QuoteApi.md#v1QuotesIdGet) | **GET** /v1/quotes/{id} | Returns information about a single Quote. |


<a id="quoteClose"></a>
# **quoteClose**
> Object quoteClose(id)

Close a Quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    Long id = 56L; // Long | Id of Quote to close
    try {
      Object result = apiInstance.quoteClose(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#quoteClose");
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
| **id** | **Long**| Id of Quote to close | |

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

<a id="quoteDelete"></a>
# **quoteDelete**
> Object quoteDelete(id, timestamp)

Removes an existing Quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    Long id = 56L; // Long | Id of Quote to remove.
    String timestamp = "timestamp_example"; // String | Timestamp of Quote to remove. Should be encoded in Base64.
    try {
      Object result = apiInstance.quoteDelete(id, timestamp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#quoteDelete");
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
| **id** | **Long**| Id of Quote to remove. | |
| **timestamp** | **String**| Timestamp of Quote to remove. Should be encoded in Base64. | |

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

<a id="quoteGet"></a>
# **quoteGet**
> PageResultQuoteDto quoteGet()

Returns a list of company&#39;s Quotes.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    try {
      PageResultQuoteDto result = apiInstance.quoteGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#quoteGet");
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

[**PageResultQuoteDto**](PageResultQuoteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="quotePost"></a>
# **quotePost**
> Object quotePost(quoteDto)

Creates a new Quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    QuoteDto quoteDto = new QuoteDto(); // QuoteDto | Information of Quote to create.
    try {
      Object result = apiInstance.quotePost(quoteDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#quotePost");
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
| **quoteDto** | [**QuoteDto**](QuoteDto.md)| Information of Quote to create. | |

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

<a id="quotePostCreateQuoteWithGeneratingReference"></a>
# **quotePostCreateQuoteWithGeneratingReference**
> Object quotePostCreateQuoteWithGeneratingReference(quoteDto)

Creates a new Quote with auto generating reference.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    QuoteDto quoteDto = new QuoteDto(); // QuoteDto | Information of Quote to create.
    try {
      Object result = apiInstance.quotePostCreateQuoteWithGeneratingReference(quoteDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#quotePostCreateQuoteWithGeneratingReference");
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
| **quoteDto** | [**QuoteDto**](QuoteDto.md)| Information of Quote to create. | |

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

<a id="quotePostGenerateSaleInvoice"></a>
# **quotePostGenerateSaleInvoice**
> Object quotePostGenerateSaleInvoice(quoteGeneratingInvoiceDto)

Generate a sale invoice from a Quote.  When sale invoice is empty, new sale invoice will be generated from Quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    QuoteGeneratingInvoiceDto quoteGeneratingInvoiceDto = new QuoteGeneratingInvoiceDto(); // QuoteGeneratingInvoiceDto | Id of Quote to generate
    try {
      Object result = apiInstance.quotePostGenerateSaleInvoice(quoteGeneratingInvoiceDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#quotePostGenerateSaleInvoice");
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
| **quoteGeneratingInvoiceDto** | [**QuoteGeneratingInvoiceDto**](QuoteGeneratingInvoiceDto.md)| Id of Quote to generate | |

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

<a id="quoteProcessBatch"></a>
# **quoteProcessBatch**
> Object quoteProcessBatch(batchItemQuoteDto)

Processes a batch of Quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    List<BatchItemQuoteDto> batchItemQuoteDto = Arrays.asList(); // List<BatchItemQuoteDto> | Batch of Quote to process.
    try {
      Object result = apiInstance.quoteProcessBatch(batchItemQuoteDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#quoteProcessBatch");
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
| **batchItemQuoteDto** | [**List&lt;BatchItemQuoteDto&gt;**](BatchItemQuoteDto.md)| Batch of Quote to process. | |

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

<a id="quotePut"></a>
# **quotePut**
> Object quotePut(id, quoteDto)

Updates an existing Quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    Long id = 56L; // Long | Id of Quote to update.
    QuoteDto quoteDto = new QuoteDto(); // QuoteDto | Information of Quote to update.
    try {
      Object result = apiInstance.quotePut(id, quoteDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#quotePut");
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
| **id** | **Long**| Id of Quote to update. | |
| **quoteDto** | [**QuoteDto**](QuoteDto.md)| Information of Quote to update. | |

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

<a id="quoteReopen"></a>
# **quoteReopen**
> Object quoteReopen(id)

Reopen a Quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    Long id = 56L; // Long | Id of Quote to reopen
    try {
      Object result = apiInstance.quoteReopen(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#quoteReopen");
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
| **id** | **Long**| Id of Quote to reopen | |

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

<a id="v1QuotesIdGet"></a>
# **v1QuotesIdGet**
> QuoteDto v1QuotesIdGet(id)

Returns information about a single Quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuoteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.bigredcloud.com/api");

    QuoteApi apiInstance = new QuoteApi(defaultClient);
    Long id = 56L; // Long | Id of Sale Rep to return.
    try {
      QuoteDto result = apiInstance.v1QuotesIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuoteApi#v1QuotesIdGet");
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
| **id** | **Long**| Id of Sale Rep to return. | |

### Return type

[**QuoteDto**](QuoteDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

