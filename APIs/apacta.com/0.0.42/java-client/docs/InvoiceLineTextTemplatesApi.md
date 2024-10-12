# InvoiceLineTextTemplatesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**invoiceLineTextTemplateGet**](InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplateGet) | **GET** /invoice_line_text_template | Get a list of invoice line text templates |
| [**invoiceLineTextTemplateInvoiceLineTextTemplateIdDelete**](InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplateInvoiceLineTextTemplateIdDelete) | **DELETE** /invoice_line_text_template/{invoice_line_text_template_id} | Delete an invoice line text template |
| [**invoiceLineTextTemplateInvoiceLineTextTemplateIdGet**](InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplateInvoiceLineTextTemplateIdGet) | **GET** /invoice_line_text_template/{invoice_line_text_template_id} | Get a single invoice line text template |
| [**invoiceLineTextTemplateInvoiceLineTextTemplateIdPost**](InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplateInvoiceLineTextTemplateIdPost) | **POST** /invoice_line_text_template/{invoice_line_text_template_id} | Edit an invoice line text template |
| [**invoiceLineTextTemplatePost**](InvoiceLineTextTemplatesApi.md#invoiceLineTextTemplatePost) | **POST** /invoice_line_text_template | Add a new invoice line text template |


<a id="invoiceLineTextTemplateGet"></a>
# **invoiceLineTextTemplateGet**
> InvoiceLineTextTemplateGet200Response invoiceLineTextTemplateGet()

Get a list of invoice line text templates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceLineTextTemplatesApi;

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

    InvoiceLineTextTemplatesApi apiInstance = new InvoiceLineTextTemplatesApi(defaultClient);
    try {
      InvoiceLineTextTemplateGet200Response result = apiInstance.invoiceLineTextTemplateGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceLineTextTemplatesApi#invoiceLineTextTemplateGet");
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

[**InvoiceLineTextTemplateGet200Response**](InvoiceLineTextTemplateGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="invoiceLineTextTemplateInvoiceLineTextTemplateIdDelete"></a>
# **invoiceLineTextTemplateInvoiceLineTextTemplateIdDelete**
> EmptySuccessResponse invoiceLineTextTemplateInvoiceLineTextTemplateIdDelete(invoiceLineTextTemplateId)

Delete an invoice line text template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceLineTextTemplatesApi;

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

    InvoiceLineTextTemplatesApi apiInstance = new InvoiceLineTextTemplatesApi(defaultClient);
    UUID invoiceLineTextTemplateId = UUID.randomUUID(); // UUID | 
    try {
      EmptySuccessResponse result = apiInstance.invoiceLineTextTemplateInvoiceLineTextTemplateIdDelete(invoiceLineTextTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceLineTextTemplatesApi#invoiceLineTextTemplateInvoiceLineTextTemplateIdDelete");
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
| **invoiceLineTextTemplateId** | **UUID**|  | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="invoiceLineTextTemplateInvoiceLineTextTemplateIdGet"></a>
# **invoiceLineTextTemplateInvoiceLineTextTemplateIdGet**
> InvoiceLineTextTemplateInvoiceLineTextTemplateIdGet200Response invoiceLineTextTemplateInvoiceLineTextTemplateIdGet(invoiceLineTextTemplateId)

Get a single invoice line text template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceLineTextTemplatesApi;

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

    InvoiceLineTextTemplatesApi apiInstance = new InvoiceLineTextTemplatesApi(defaultClient);
    UUID invoiceLineTextTemplateId = UUID.randomUUID(); // UUID | 
    try {
      InvoiceLineTextTemplateInvoiceLineTextTemplateIdGet200Response result = apiInstance.invoiceLineTextTemplateInvoiceLineTextTemplateIdGet(invoiceLineTextTemplateId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceLineTextTemplatesApi#invoiceLineTextTemplateInvoiceLineTextTemplateIdGet");
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
| **invoiceLineTextTemplateId** | **UUID**|  | |

### Return type

[**InvoiceLineTextTemplateInvoiceLineTextTemplateIdGet200Response**](InvoiceLineTextTemplateInvoiceLineTextTemplateIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="invoiceLineTextTemplateInvoiceLineTextTemplateIdPost"></a>
# **invoiceLineTextTemplateInvoiceLineTextTemplateIdPost**
> EmptySuccessResponse invoiceLineTextTemplateInvoiceLineTextTemplateIdPost(invoiceLineTextTemplateId, html, image)

Edit an invoice line text template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceLineTextTemplatesApi;

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

    InvoiceLineTextTemplatesApi apiInstance = new InvoiceLineTextTemplatesApi(defaultClient);
    UUID invoiceLineTextTemplateId = UUID.randomUUID(); // UUID | 
    String html = "html_example"; // String | 
    File image = new File("/path/to/file"); // File | 
    try {
      EmptySuccessResponse result = apiInstance.invoiceLineTextTemplateInvoiceLineTextTemplateIdPost(invoiceLineTextTemplateId, html, image);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceLineTextTemplatesApi#invoiceLineTextTemplateInvoiceLineTextTemplateIdPost");
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
| **invoiceLineTextTemplateId** | **UUID**|  | |
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
| **404** | Not found |  -  |
| **422** | Validation error |  -  |

<a id="invoiceLineTextTemplatePost"></a>
# **invoiceLineTextTemplatePost**
> CreateSuccessResponse invoiceLineTextTemplatePost(html, image)

Add a new invoice line text template

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceLineTextTemplatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    InvoiceLineTextTemplatesApi apiInstance = new InvoiceLineTextTemplatesApi(defaultClient);
    String html = "html_example"; // String | 
    File image = new File("/path/to/file"); // File | 
    try {
      CreateSuccessResponse result = apiInstance.invoiceLineTextTemplatePost(html, image);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceLineTextTemplatesApi#invoiceLineTextTemplatePost");
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
| **image** | **File**|  | [optional] |

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **422** | Validation error |  -  |

