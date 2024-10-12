# InvoiceFilesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createInvoiceFile**](InvoiceFilesApi.md#createInvoiceFile) | **POST** /invoices/{invoice_id}/files | Create a new invoice file |
| [**getInvoiceFiles**](InvoiceFilesApi.md#getInvoiceFiles) | **GET** /invoices/{invoice_id}/files | Get list of invoice files |
| [**getOneInvoiceFiles**](InvoiceFilesApi.md#getOneInvoiceFiles) | **GET** /invoices/{invoice_id}/files/{file_id} | Get an invoice files |
| [**invoicesInvoiceIdFilesFileIdDelete**](InvoiceFilesApi.md#invoicesInvoiceIdFilesFileIdDelete) | **DELETE** /invoices/{invoice_id}/files/{file_id} | Delete invoice file |


<a id="createInvoiceFile"></a>
# **createInvoiceFile**
> CreateSuccessResponse createInvoiceFile(invoiceId, fileId, invoiceId2, type)

Create a new invoice file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceFilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    InvoiceFilesApi apiInstance = new InvoiceFilesApi(defaultClient);
    UUID invoiceId = UUID.randomUUID(); // UUID | 
    UUID fileId = UUID.randomUUID(); // UUID | 
    UUID invoiceId2 = UUID.randomUUID(); // UUID | 
    String type = "type_example"; // String | 
    try {
      CreateSuccessResponse result = apiInstance.createInvoiceFile(invoiceId, fileId, invoiceId2, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceFilesApi#createInvoiceFile");
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
| **invoiceId** | **UUID**|  | |
| **fileId** | **UUID**|  | |
| **invoiceId2** | **UUID**|  | |
| **type** | **String**|  | [optional] |

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unautorized |  -  |
| **404** | Not found |  -  |
| **422** | Validation error |  -  |

<a id="getInvoiceFiles"></a>
# **getInvoiceFiles**
> GetInvoiceFiles200Response getInvoiceFiles(invoiceId)

Get list of invoice files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceFilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    InvoiceFilesApi apiInstance = new InvoiceFilesApi(defaultClient);
    UUID invoiceId = UUID.randomUUID(); // UUID | 
    try {
      GetInvoiceFiles200Response result = apiInstance.getInvoiceFiles(invoiceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceFilesApi#getInvoiceFiles");
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
| **invoiceId** | **UUID**|  | |

### Return type

[**GetInvoiceFiles200Response**](GetInvoiceFiles200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="getOneInvoiceFiles"></a>
# **getOneInvoiceFiles**
> GetOneInvoiceFiles200Response getOneInvoiceFiles(invoiceId, fileId)

Get an invoice files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceFilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    InvoiceFilesApi apiInstance = new InvoiceFilesApi(defaultClient);
    UUID invoiceId = UUID.randomUUID(); // UUID | 
    UUID fileId = UUID.randomUUID(); // UUID | 
    try {
      GetOneInvoiceFiles200Response result = apiInstance.getOneInvoiceFiles(invoiceId, fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceFilesApi#getOneInvoiceFiles");
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
| **invoiceId** | **UUID**|  | |
| **fileId** | **UUID**|  | |

### Return type

[**GetOneInvoiceFiles200Response**](GetOneInvoiceFiles200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="invoicesInvoiceIdFilesFileIdDelete"></a>
# **invoicesInvoiceIdFilesFileIdDelete**
> ClockingRecordsClockingRecordIdPut200Response invoicesInvoiceIdFilesFileIdDelete(invoiceId, fileId)

Delete invoice file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoiceFilesApi;

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

    InvoiceFilesApi apiInstance = new InvoiceFilesApi(defaultClient);
    UUID invoiceId = UUID.randomUUID(); // UUID | 
    UUID fileId = UUID.randomUUID(); // UUID | 
    try {
      ClockingRecordsClockingRecordIdPut200Response result = apiInstance.invoicesInvoiceIdFilesFileIdDelete(invoiceId, fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoiceFilesApi#invoicesInvoiceIdFilesFileIdDelete");
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
| **invoiceId** | **UUID**|  | |
| **fileId** | **UUID**|  | |

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
| **401** | Unautorized |  -  |

