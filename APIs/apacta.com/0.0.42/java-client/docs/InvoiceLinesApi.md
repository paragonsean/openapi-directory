# InvoiceLinesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**invoiceLineTextsInvoiceLineTextIdPost**](InvoiceLinesApi.md#invoiceLineTextsInvoiceLineTextIdPost) | **POST** /invoice_line_texts/{invoice_line_text_id} | Edit invoice line text |
| [**invoiceLineTextsPost**](InvoiceLinesApi.md#invoiceLineTextsPost) | **POST** /invoice_line_texts/ | Add invoice line text |
| [**invoiceLinesGet**](InvoiceLinesApi.md#invoiceLinesGet) | **GET** /invoice_lines | View list of invoice lines |
| [**invoiceLinesInvoiceLineIdDelete**](InvoiceLinesApi.md#invoiceLinesInvoiceLineIdDelete) | **DELETE** /invoice_lines/{invoice_line_id} | Delete invoice line |
| [**invoiceLinesInvoiceLineIdGet**](InvoiceLinesApi.md#invoiceLinesInvoiceLineIdGet) | **GET** /invoice_lines/{invoice_line_id} | View invoice line |
| [**invoiceLinesInvoiceLineIdPut**](InvoiceLinesApi.md#invoiceLinesInvoiceLineIdPut) | **PUT** /invoice_lines/{invoice_line_id} | Edit invoice line |
| [**invoiceLinesPost**](InvoiceLinesApi.md#invoiceLinesPost) | **POST** /invoice_lines | Add invoice line |


<a id="invoiceLineTextsInvoiceLineTextIdPost"></a>
# **invoiceLineTextsInvoiceLineTextIdPost**
> EmptySuccessResponse invoiceLineTextsInvoiceLineTextIdPost(invoiceLineTextId, html, image)

Edit invoice line text

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceLinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    InvoiceLinesApi apiInstance = new InvoiceLinesApi(defaultClient);
    String invoiceLineTextId = "invoiceLineTextId_example"; // String | Automatically added
    String html = "html_example"; // String | 
    File image = new File("/path/to/file"); // File | 
    try {
      EmptySuccessResponse result = apiInstance.invoiceLineTextsInvoiceLineTextIdPost(invoiceLineTextId, html, image);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceLinesApi#invoiceLineTextsInvoiceLineTextIdPost");
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
| **invoiceLineTextId** | **String**| Automatically added | |
| **html** | **String**|  | |
| **image** | **File**|  | [optional] |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |

<a id="invoiceLineTextsPost"></a>
# **invoiceLineTextsPost**
> CreateSuccessResponse invoiceLineTextsPost(html, invoiceId, image, placement)

Add invoice line text

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceLinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    InvoiceLinesApi apiInstance = new InvoiceLinesApi(defaultClient);
    String html = "html_example"; // String | 
    UUID invoiceId = UUID.randomUUID(); // UUID | 
    File image = new File("/path/to/file"); // File | 
    Integer placement = 56; // Integer | 
    try {
      CreateSuccessResponse result = apiInstance.invoiceLineTextsPost(html, invoiceId, image, placement);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceLinesApi#invoiceLineTextsPost");
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
| **html** | **String**|  | |
| **invoiceId** | **UUID**|  | |
| **image** | **File**|  | [optional] |
| **placement** | **Integer**|  | [optional] |

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **400** | Bad Request |  -  |
| **404** | Not found |  -  |

<a id="invoiceLinesGet"></a>
# **invoiceLinesGet**
> InvoiceLinesGet200Response invoiceLinesGet(invoiceId, productId, userId, name, discountText)

View list of invoice lines

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceLinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    InvoiceLinesApi apiInstance = new InvoiceLinesApi(defaultClient);
    UUID invoiceId = UUID.randomUUID(); // UUID | 
    UUID productId = UUID.randomUUID(); // UUID | 
    UUID userId = UUID.randomUUID(); // UUID | 
    String name = "name_example"; // String | 
    String discountText = "discountText_example"; // String | 
    try {
      InvoiceLinesGet200Response result = apiInstance.invoiceLinesGet(invoiceId, productId, userId, name, discountText);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceLinesApi#invoiceLinesGet");
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
| **invoiceId** | **UUID**|  | [optional] |
| **productId** | **UUID**|  | [optional] |
| **userId** | **UUID**|  | [optional] |
| **name** | **String**|  | [optional] |
| **discountText** | **String**|  | [optional] |

### Return type

[**InvoiceLinesGet200Response**](InvoiceLinesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoiceLinesInvoiceLineIdDelete"></a>
# **invoiceLinesInvoiceLineIdDelete**
> ClockingRecordsClockingRecordIdPut200Response invoiceLinesInvoiceLineIdDelete(invoiceLineId)

Delete invoice line

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceLinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    InvoiceLinesApi apiInstance = new InvoiceLinesApi(defaultClient);
    UUID invoiceLineId = UUID.randomUUID(); // UUID | 
    try {
      ClockingRecordsClockingRecordIdPut200Response result = apiInstance.invoiceLinesInvoiceLineIdDelete(invoiceLineId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceLinesApi#invoiceLinesInvoiceLineIdDelete");
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
| **invoiceLineId** | **UUID**|  | |

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoiceLinesInvoiceLineIdGet"></a>
# **invoiceLinesInvoiceLineIdGet**
> InvoiceLinesInvoiceLineIdGet200Response invoiceLinesInvoiceLineIdGet(invoiceLineId)

View invoice line

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceLinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    InvoiceLinesApi apiInstance = new InvoiceLinesApi(defaultClient);
    UUID invoiceLineId = UUID.randomUUID(); // UUID | 
    try {
      InvoiceLinesInvoiceLineIdGet200Response result = apiInstance.invoiceLinesInvoiceLineIdGet(invoiceLineId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceLinesApi#invoiceLinesInvoiceLineIdGet");
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
| **invoiceLineId** | **UUID**|  | |

### Return type

[**InvoiceLinesInvoiceLineIdGet200Response**](InvoiceLinesInvoiceLineIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoiceLinesInvoiceLineIdPut"></a>
# **invoiceLinesInvoiceLineIdPut**
> ClockingRecordsClockingRecordIdPut200Response invoiceLinesInvoiceLineIdPut(invoiceLineId, invoiceLinesInvoiceLineIdPutRequest)

Edit invoice line

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceLinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    InvoiceLinesApi apiInstance = new InvoiceLinesApi(defaultClient);
    UUID invoiceLineId = UUID.randomUUID(); // UUID | 
    InvoiceLinesInvoiceLineIdPutRequest invoiceLinesInvoiceLineIdPutRequest = new InvoiceLinesInvoiceLineIdPutRequest(); // InvoiceLinesInvoiceLineIdPutRequest | 
    try {
      ClockingRecordsClockingRecordIdPut200Response result = apiInstance.invoiceLinesInvoiceLineIdPut(invoiceLineId, invoiceLinesInvoiceLineIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceLinesApi#invoiceLinesInvoiceLineIdPut");
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
| **invoiceLineId** | **UUID**|  | |
| **invoiceLinesInvoiceLineIdPutRequest** | [**InvoiceLinesInvoiceLineIdPutRequest**](InvoiceLinesInvoiceLineIdPutRequest.md)|  | [optional] |

### Return type

[**ClockingRecordsClockingRecordIdPut200Response**](ClockingRecordsClockingRecordIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoiceLinesPost"></a>
# **invoiceLinesPost**
> ClockingRecordsPost201Response invoiceLinesPost(invoiceLinesPostRequest)

Add invoice line

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceLinesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    InvoiceLinesApi apiInstance = new InvoiceLinesApi(defaultClient);
    InvoiceLinesPostRequest invoiceLinesPostRequest = new InvoiceLinesPostRequest(); // InvoiceLinesPostRequest | 
    try {
      ClockingRecordsPost201Response result = apiInstance.invoiceLinesPost(invoiceLinesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceLinesApi#invoiceLinesPost");
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
| **invoiceLinesPostRequest** | [**InvoiceLinesPostRequest**](InvoiceLinesPostRequest.md)|  | [optional] |

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **422** | Validation error |  -  |

