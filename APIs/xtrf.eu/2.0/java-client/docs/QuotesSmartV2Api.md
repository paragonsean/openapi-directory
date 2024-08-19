# QuotesSmartV2Api

All URIs are relative to *https://presentation.s.xtrf.eu/home-api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addFiles2**](QuotesSmartV2Api.md#addFiles2) | **PUT** /v2/quotes/{quoteId}/files/add | Adds files to the quote as added by PM. |
| [**archive1**](QuotesSmartV2Api.md#archive1) | **POST** /v2/quotes/files/archive | Prepares a ZIP archive that contains the specified files. |
| [**changeStatus3**](QuotesSmartV2Api.md#changeStatus3) | **PUT** /v2/quotes/{quoteId}/status | Changes quote status if possible (400 Bad Request is returned otherwise). |
| [**create7**](QuotesSmartV2Api.md#create7) | **POST** /v2/quotes | Creates a new Smart Quote. |
| [**createPayable3**](QuotesSmartV2Api.md#createPayable3) | **POST** /v2/quotes/{quoteId}/finance/payables | Adds a payable to a quote. |
| [**createReceivable3**](QuotesSmartV2Api.md#createReceivable3) | **POST** /v2/quotes/{quoteId}/finance/receivables | Adds a receivable to a quote. |
| [**deletePayable3**](QuotesSmartV2Api.md#deletePayable3) | **DELETE** /v2/quotes/{quoteId}/finance/payables/{payableId} | Deletes a payable. |
| [**deleteReceivable3**](QuotesSmartV2Api.md#deleteReceivable3) | **DELETE** /v2/quotes/{quoteId}/finance/receivables/{receivableId} | Deletes a receivable. |
| [**getById10**](QuotesSmartV2Api.md#getById10) | **GET** /v2/quotes/{quoteId} | Returns quote details. |
| [**getContacts3**](QuotesSmartV2Api.md#getContacts3) | **GET** /v2/quotes/{quoteId}/clientContacts | Returns Client Contacts information for a quote. |
| [**getCustomFields9**](QuotesSmartV2Api.md#getCustomFields9) | **GET** /v2/quotes/{quoteId}/customFields | Returns a list of custom field keys and values for a project. |
| [**getFileById3**](QuotesSmartV2Api.md#getFileById3) | **GET** /v2/quotes/files/{fileId} | Returns details of a file. |
| [**getFileContentById1**](QuotesSmartV2Api.md#getFileContentById1) | **GET** /v2/quotes/files/{fileId}/download/{fileName} | Downloads a file content. |
| [**getFiles1**](QuotesSmartV2Api.md#getFiles1) | **GET** /v2/quotes/{quoteId}/files | Returns list of files in a quote. |
| [**getFinance3**](QuotesSmartV2Api.md#getFinance3) | **GET** /v2/quotes/{quoteId}/finance | Returns finance information for a quote. |
| [**getJobs1**](QuotesSmartV2Api.md#getJobs1) | **GET** /v2/quotes/{quoteId}/jobs | Returns list of jobs in a quote. |
| [**updateBusinessDays**](QuotesSmartV2Api.md#updateBusinessDays) | **PUT** /v2/quotes/{quoteId}/businessDays | Updates Business Days for a quote. |
| [**updateClientNotes1**](QuotesSmartV2Api.md#updateClientNotes1) | **PUT** /v2/quotes/{quoteId}/clientNotes | Updates Client Notes for a quote. |
| [**updateClientReferenceNumber1**](QuotesSmartV2Api.md#updateClientReferenceNumber1) | **PUT** /v2/quotes/{quoteId}/clientReferenceNumber | Updates Client Reference Number for a quote. |
| [**updateContacts3**](QuotesSmartV2Api.md#updateContacts3) | **PUT** /v2/quotes/{quoteId}/clientContacts | Updates Client Contacts for a quote. |
| [**updateCustomField3**](QuotesSmartV2Api.md#updateCustomField3) | **PUT** /v2/quotes/{quoteId}/customFields/{key} | Updates a custom field with a specified key in a quote. |
| [**updateExpectedDeliveryDate**](QuotesSmartV2Api.md#updateExpectedDeliveryDate) | **PUT** /v2/quotes/{quoteId}/expectedDeliveryDate | Updates Expected Delivery Date for a quote. |
| [**updateInternalNotes1**](QuotesSmartV2Api.md#updateInternalNotes1) | **PUT** /v2/quotes/{quoteId}/internalNotes | Updates Internal Notes for a quote. |
| [**updatePayable3**](QuotesSmartV2Api.md#updatePayable3) | **PUT** /v2/quotes/{quoteId}/finance/payables/{payableId} | Updates a payable. |
| [**updateQuoteExpiry**](QuotesSmartV2Api.md#updateQuoteExpiry) | **PUT** /v2/quotes/{quoteId}/quoteExpiry | Updates Quote Expiry Date for a quote. |
| [**updateReceivable3**](QuotesSmartV2Api.md#updateReceivable3) | **PUT** /v2/quotes/{quoteId}/finance/receivables/{receivableId} | Updates a receivable. |
| [**updateSourceLanguage1**](QuotesSmartV2Api.md#updateSourceLanguage1) | **PUT** /v2/quotes/{quoteId}/sourceLanguage | Updates source language for a quote. |
| [**updateSpecialization1**](QuotesSmartV2Api.md#updateSpecialization1) | **PUT** /v2/quotes/{quoteId}/specialization | Updates specialization for a quote. |
| [**updateTargetLanguages1**](QuotesSmartV2Api.md#updateTargetLanguages1) | **PUT** /v2/quotes/{quoteId}/targetLanguages | Updates target languages for a quote. |
| [**updateVendorInstructions1**](QuotesSmartV2Api.md#updateVendorInstructions1) | **PUT** /v2/quotes/{quoteId}/vendorInstructions | Updates instructions for all vendors performing the jobs in a quote. |
| [**updateVolume1**](QuotesSmartV2Api.md#updateVolume1) | **PUT** /v2/quotes/{quoteId}/volume | Updates volume for a quote. |
| [**uploadFile3**](QuotesSmartV2Api.md#uploadFile3) | **POST** /v2/quotes/{quoteId}/files/upload | Uploads file to the quote as a file uploaded by PM. |


<a id="addFiles2"></a>
# **addFiles2**
> addFiles2(quoteId, timeDTO)

Adds files to the quote as added by PM.

Adds files to the quote as added by PM. The files have to be uploaded beforehand (see \&quot;POST v2/quotes/{quoteId}/files/upload\&quot; operation). The following properties can be specified for each file:&lt;ul&gt;&lt;li&gt;category (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;languageIds – when the file category depends on a list of languages&lt;/li&gt;&lt;li&gt;languageCombinationIds – when the file category depends on a list of language combinations&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    TimeDTO timeDTO = new TimeDTO(); // TimeDTO | Added files to the quote as added by PM.
    try {
      apiInstance.addFiles2(quoteId, timeDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#addFiles2");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **timeDTO** | [**TimeDTO**](TimeDTO.md)| Added files to the quote as added by PM. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="archive1"></a>
# **archive1**
> FilesArchiveDto archive1(filesDto)

Prepares a ZIP archive that contains the specified files.

Prepares a ZIP archive that contains the specified files.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    FilesDto filesDto = new FilesDto(); // FilesDto | Prepared ZIP archive that contains the specified files.
    try {
      FilesArchiveDto result = apiInstance.archive1(filesDto);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#archive1");
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
| **filesDto** | [**FilesDto**](FilesDto.md)| Prepared ZIP archive that contains the specified files. | |

### Return type

[**FilesArchiveDto**](FilesArchiveDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="changeStatus3"></a>
# **changeStatus3**
> changeStatus3(quoteId, projectStatusDTO)

Changes quote status if possible (400 Bad Request is returned otherwise).

Changes quote status if possible (400 Bad Request is returned otherwise). The status has to be specified using one of the following keys: &lt;ul&gt;&lt;li&gt;PENDING – available when the job has one of the following statuses: REQUESTED, REJECTED&lt;/li&gt;&lt;li&gt;SENT – available when the job has one of the following statuses: PENDING&lt;/li&gt;&lt;li&gt;APPROVED – available when the job has one of the following statuses: REQUESTED, PENDING, SENT, APPROVED_BY_CLIENT&lt;/li&gt;&lt;li&gt;REJECTED – available when the job has one of the following statuses: REQUESTED, PENDING, SENT&lt;/li&gt;&lt;/ul&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    ProjectStatusDTO projectStatusDTO = new ProjectStatusDTO(); // ProjectStatusDTO | Changed Quote status.
    try {
      apiInstance.changeStatus3(quoteId, projectStatusDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#changeStatus3");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **projectStatusDTO** | [**ProjectStatusDTO**](ProjectStatusDTO.md)| Changed Quote status. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="create7"></a>
# **create7**
> QuoteDTOv2 create7(quoteCreateDTO)

Creates a new Smart Quote.

Creates a new Smart Quote. If the specified service ID refers to Classic Quote, 400 Bad Request is returned instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    QuoteCreateDTO quoteCreateDTO = new QuoteCreateDTO(); // QuoteCreateDTO | Project to create
    try {
      QuoteDTOv2 result = apiInstance.create7(quoteCreateDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#create7");
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
| **quoteCreateDTO** | [**QuoteCreateDTO**](QuoteCreateDTO.md)| Project to create | [optional] |

### Return type

[**QuoteDTOv2**](QuoteDTOv2.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |

<a id="createPayable3"></a>
# **createPayable3**
> PayableDTO createPayable3(quoteId, payableCreateDTO)

Adds a payable to a quote.

Adds a payable to a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    PayableCreateDTO payableCreateDTO = new PayableCreateDTO(); // PayableCreateDTO | 
    try {
      PayableDTO result = apiInstance.createPayable3(quoteId, payableCreateDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#createPayable3");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **payableCreateDTO** | [**PayableCreateDTO**](PayableCreateDTO.md)|  | |

### Return type

[**PayableDTO**](PayableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="createReceivable3"></a>
# **createReceivable3**
> ReceivableDTO createReceivable3(quoteId, receivableCreateDTO)

Adds a receivable to a quote.

Adds a receivable to a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    ReceivableCreateDTO receivableCreateDTO = new ReceivableCreateDTO(); // ReceivableCreateDTO | 
    try {
      ReceivableDTO result = apiInstance.createReceivable3(quoteId, receivableCreateDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#createReceivable3");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **receivableCreateDTO** | [**ReceivableCreateDTO**](ReceivableCreateDTO.md)|  | |

### Return type

[**ReceivableDTO**](ReceivableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="deletePayable3"></a>
# **deletePayable3**
> deletePayable3(quoteId, payableId)

Deletes a payable.

Deletes a payable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    Long payableId = 56L; // Long | payable's internal identifier
    try {
      apiInstance.deletePayable3(quoteId, payableId);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#deletePayable3");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **payableId** | **Long**| payable&#39;s internal identifier | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="deleteReceivable3"></a>
# **deleteReceivable3**
> deleteReceivable3(quoteId, receivableId)

Deletes a receivable.

Deletes a receivable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    Long receivableId = 56L; // Long | receivable's internal identifier
    try {
      apiInstance.deleteReceivable3(quoteId, receivableId);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#deleteReceivable3");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **receivableId** | **Long**| receivable&#39;s internal identifier | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="getById10"></a>
# **getById10**
> QuoteDTOv2 getById10(quoteId)

Returns quote details.

Returns quote details. If the specified quote ID refers to Classic Quote, 400 Bad Request is returned instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    try {
      QuoteDTOv2 result = apiInstance.getById10(quoteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#getById10");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |

### Return type

[**QuoteDTOv2**](QuoteDTOv2.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getContacts3"></a>
# **getContacts3**
> SmartContactsDTO getContacts3(quoteId)

Returns Client Contacts information for a quote.

Returns Client Contacts information for a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    try {
      SmartContactsDTO result = apiInstance.getContacts3(quoteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#getContacts3");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |

### Return type

[**SmartContactsDTO**](SmartContactsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getCustomFields9"></a>
# **getCustomFields9**
> List&lt;CustomFieldDTO&gt; getCustomFields9(quoteId)

Returns a list of custom field keys and values for a project.

Returns a list of custom field keys and values for a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    try {
      List<CustomFieldDTO> result = apiInstance.getCustomFields9(quoteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#getCustomFields9");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |

### Return type

[**List&lt;CustomFieldDTO&gt;**](CustomFieldDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getFileById3"></a>
# **getFileById3**
> ProjectFileDto getFileById3(fileId)

Returns details of a file.

Returns details of a file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String fileId = "fileId_example"; // String | file's internal identifier
    try {
      ProjectFileDto result = apiInstance.getFileById3(fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#getFileById3");
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
| **fileId** | **String**| file&#39;s internal identifier | |

### Return type

[**ProjectFileDto**](ProjectFileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getFileContentById1"></a>
# **getFileContentById1**
> getFileContentById1(fileId, fileName)

Downloads a file content.

Downloads a file content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String fileId = "fileId_example"; // String | file's internal identifier
    String fileName = "fileName_example"; // String | file's name
    try {
      apiInstance.getFileContentById1(fileId, fileName);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#getFileContentById1");
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
| **fileId** | **String**| file&#39;s internal identifier | |
| **fileName** | **String**| file&#39;s name | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: multipart/form-data

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getFiles1"></a>
# **getFiles1**
> List&lt;ProjectFileDto&gt; getFiles1(quoteId)

Returns list of files in a quote.

Returns list of files in a quote. Only files added to the quote (i.e. files that have assigned category and languages) are listed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    try {
      List<ProjectFileDto> result = apiInstance.getFiles1(quoteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#getFiles1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |

### Return type

[**List&lt;ProjectFileDto&gt;**](ProjectFileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | ok |  -  |

<a id="getFinance3"></a>
# **getFinance3**
> FinanceDTO getFinance3(quoteId)

Returns finance information for a quote.

Returns finance information for a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    try {
      FinanceDTO result = apiInstance.getFinance3(quoteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#getFinance3");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |

### Return type

[**FinanceDTO**](FinanceDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="getJobs1"></a>
# **getJobs1**
> List&lt;JobDto&gt; getJobs1(quoteId)

Returns list of jobs in a quote.

Returns list of jobs in a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    try {
      List<JobDto> result = apiInstance.getJobs1(quoteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#getJobs1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |

### Return type

[**List&lt;JobDto&gt;**](JobDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updateBusinessDays"></a>
# **updateBusinessDays**
> updateBusinessDays(quoteId, body)

Updates Business Days for a quote.

Updates Business Days for a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    Integer body = /home-api/assets/examples/v2/quotes/updateBusinessDays.json#requestBody; // Integer | Updated Business Days for a quote.
    try {
      apiInstance.updateBusinessDays(quoteId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#updateBusinessDays");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **body** | **Integer**| Updated Business Days for a quote. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="updateClientNotes1"></a>
# **updateClientNotes1**
> updateClientNotes1(quoteId, stringDTO)

Updates Client Notes for a quote.

Updates Client Notes for a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    StringDTO stringDTO = new StringDTO(); // StringDTO | Updated Client Notes for a quote.
    try {
      apiInstance.updateClientNotes1(quoteId, stringDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#updateClientNotes1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **stringDTO** | [**StringDTO**](StringDTO.md)| Updated Client Notes for a quote. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="updateClientReferenceNumber1"></a>
# **updateClientReferenceNumber1**
> updateClientReferenceNumber1(quoteId, stringDTO)

Updates Client Reference Number for a quote.

Updates Client Reference Number for a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    StringDTO stringDTO = new StringDTO(); // StringDTO | Updated Client Reference Number for a quote.
    try {
      apiInstance.updateClientReferenceNumber1(quoteId, stringDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#updateClientReferenceNumber1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **stringDTO** | [**StringDTO**](StringDTO.md)| Updated Client Reference Number for a quote. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="updateContacts3"></a>
# **updateContacts3**
> SmartContactsDTO updateContacts3(quoteId, smartContactsDTO)

Updates Client Contacts for a quote.

Updates Client Contacts for a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    SmartContactsDTO smartContactsDTO = new SmartContactsDTO(); // SmartContactsDTO | Updated Client Contacts for a quote.
    try {
      SmartContactsDTO result = apiInstance.updateContacts3(quoteId, smartContactsDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#updateContacts3");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **smartContactsDTO** | [**SmartContactsDTO**](SmartContactsDTO.md)| Updated Client Contacts for a quote. | |

### Return type

[**SmartContactsDTO**](SmartContactsDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updateCustomField3"></a>
# **updateCustomField3**
> updateCustomField3(quoteId, key, smartCustomFieldDTO)

Updates a custom field with a specified key in a quote.

Updates a custom field with a specified key in a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    String key = "key_example"; // String | custom field's key
    SmartCustomFieldDTO smartCustomFieldDTO = new SmartCustomFieldDTO(); // SmartCustomFieldDTO | Updated custom field with a specified key in a quote.
    try {
      apiInstance.updateCustomField3(quoteId, key, smartCustomFieldDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#updateCustomField3");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **key** | **String**| custom field&#39;s key | |
| **smartCustomFieldDTO** | [**SmartCustomFieldDTO**](SmartCustomFieldDTO.md)| Updated custom field with a specified key in a quote. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="updateExpectedDeliveryDate"></a>
# **updateExpectedDeliveryDate**
> updateExpectedDeliveryDate(quoteId, timeDTO)

Updates Expected Delivery Date for a quote.

Updates Expected Delivery Date for a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    TimeDTO timeDTO = new TimeDTO(); // TimeDTO | Updated Expected Delivery Date for a quote.
    try {
      apiInstance.updateExpectedDeliveryDate(quoteId, timeDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#updateExpectedDeliveryDate");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **timeDTO** | [**TimeDTO**](TimeDTO.md)| Updated Expected Delivery Date for a quote. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="updateInternalNotes1"></a>
# **updateInternalNotes1**
> updateInternalNotes1(quoteId, stringDTO)

Updates Internal Notes for a quote.

Updates Internal Notes for a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    StringDTO stringDTO = new StringDTO(); // StringDTO | Updated Internal Notes for a quote.
    try {
      apiInstance.updateInternalNotes1(quoteId, stringDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#updateInternalNotes1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **stringDTO** | [**StringDTO**](StringDTO.md)| Updated Internal Notes for a quote. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="updatePayable3"></a>
# **updatePayable3**
> PayableDTO updatePayable3(quoteId, payableId, payableDTO)

Updates a payable.

Updates a payable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    Long payableId = 56L; // Long | payable's internal identifier
    PayableDTO payableDTO = new PayableDTO(); // PayableDTO | 
    try {
      PayableDTO result = apiInstance.updatePayable3(quoteId, payableId, payableDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#updatePayable3");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **payableId** | **Long**| payable&#39;s internal identifier | |
| **payableDTO** | [**PayableDTO**](PayableDTO.md)|  | |

### Return type

[**PayableDTO**](PayableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updateQuoteExpiry"></a>
# **updateQuoteExpiry**
> updateQuoteExpiry(quoteId, timeDTO)

Updates Quote Expiry Date for a quote.

Updates Quote Expiry Date for a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    TimeDTO timeDTO = new TimeDTO(); // TimeDTO | Updated Quote Expiry Date for a quote.
    try {
      apiInstance.updateQuoteExpiry(quoteId, timeDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#updateQuoteExpiry");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **timeDTO** | [**TimeDTO**](TimeDTO.md)| Updated Quote Expiry Date for a quote. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="updateReceivable3"></a>
# **updateReceivable3**
> ReceivableDTO updateReceivable3(quoteId, receivableId, receivableDTO)

Updates a receivable.

Updates a receivable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    Long receivableId = 56L; // Long | receivable's internal identifier
    ReceivableDTO receivableDTO = new ReceivableDTO(); // ReceivableDTO | 
    try {
      ReceivableDTO result = apiInstance.updateReceivable3(quoteId, receivableId, receivableDTO);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#updateReceivable3");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **receivableId** | **Long**| receivable&#39;s internal identifier | |
| **receivableDTO** | [**ReceivableDTO**](ReceivableDTO.md)|  | |

### Return type

[**ReceivableDTO**](ReceivableDTO.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

<a id="updateSourceLanguage1"></a>
# **updateSourceLanguage1**
> updateSourceLanguage1(quoteId, sourceLanguageDTO)

Updates source language for a quote.

Updates source language for a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    SourceLanguageDTO sourceLanguageDTO = new SourceLanguageDTO(); // SourceLanguageDTO | Updated source language for a quote.
    try {
      apiInstance.updateSourceLanguage1(quoteId, sourceLanguageDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#updateSourceLanguage1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **sourceLanguageDTO** | [**SourceLanguageDTO**](SourceLanguageDTO.md)| Updated source language for a quote. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="updateSpecialization1"></a>
# **updateSpecialization1**
> updateSpecialization1(quoteId, specializationDTO)

Updates specialization for a quote.

Updates specialization for a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    SpecializationDTO specializationDTO = new SpecializationDTO(); // SpecializationDTO | Updated specialization for a quote.
    try {
      apiInstance.updateSpecialization1(quoteId, specializationDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#updateSpecialization1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **specializationDTO** | [**SpecializationDTO**](SpecializationDTO.md)| Updated specialization for a quote. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="updateTargetLanguages1"></a>
# **updateTargetLanguages1**
> updateTargetLanguages1(quoteId, targetLanguagesDTO)

Updates target languages for a quote.

Updates target languages for a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    TargetLanguagesDTO targetLanguagesDTO = new TargetLanguagesDTO(); // TargetLanguagesDTO | Updated target languages for a quote.
    try {
      apiInstance.updateTargetLanguages1(quoteId, targetLanguagesDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#updateTargetLanguages1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **targetLanguagesDTO** | [**TargetLanguagesDTO**](TargetLanguagesDTO.md)| Updated target languages for a quote. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="updateVendorInstructions1"></a>
# **updateVendorInstructions1**
> updateVendorInstructions1(quoteId, stringDTO)

Updates instructions for all vendors performing the jobs in a quote.

Updates instructions for all vendors performing the jobs in a quote. See also \&quot;PUT /jobs/{jobId}/instructions\&quot; for updating instructions for a specific job in a project or quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    StringDTO stringDTO = new StringDTO(); // StringDTO | Updated instructions for all vendors performing the jobs in a quote.
    try {
      apiInstance.updateVendorInstructions1(quoteId, stringDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#updateVendorInstructions1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **stringDTO** | [**StringDTO**](StringDTO.md)| Updated instructions for all vendors performing the jobs in a quote. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="updateVolume1"></a>
# **updateVolume1**
> updateVolume1(quoteId, bigDecimalDTO)

Updates volume for a quote.

Updates volume for a quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    BigDecimalDTO bigDecimalDTO = new BigDecimalDTO(); // BigDecimalDTO | Updated volume for a quote.
    try {
      apiInstance.updateVolume1(quoteId, bigDecimalDTO);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#updateVolume1");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **bigDecimalDTO** | [**BigDecimalDTO**](BigDecimalDTO.md)| Updated volume for a quote. | |

### Return type

null (empty response body)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="uploadFile3"></a>
# **uploadFile3**
> FileDto uploadFile3(quoteId, _file)

Uploads file to the quote as a file uploaded by PM.

Uploads file to the quote as a file uploaded by PM. Only one file can be uploaded at once. When the upload is finished the file has to be added by specifying its category and languages (see \&quot;PUT /v2/quotes/{quoteId}/files/add\&quot; operation).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.QuotesSmartV2Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://presentation.s.xtrf.eu/home-api");
    
    // Configure API key authorization: X-AUTH-ACCESS-TOKEN
    ApiKeyAuth X-AUTH-ACCESS-TOKEN = (ApiKeyAuth) defaultClient.getAuthentication("X-AUTH-ACCESS-TOKEN");
    X-AUTH-ACCESS-TOKEN.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AUTH-ACCESS-TOKEN.setApiKeyPrefix("Token");

    QuotesSmartV2Api apiInstance = new QuotesSmartV2Api(defaultClient);
    String quoteId = "quoteId_example"; // String | quote's internal identifier
    File _file = new File("/path/to/file"); // File | 
    try {
      FileDto result = apiInstance.uploadFile3(quoteId, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling QuotesSmartV2Api#uploadFile3");
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
| **quoteId** | **String**| quote&#39;s internal identifier | |
| **_file** | **File**|  | [optional] |

### Return type

[**FileDto**](FileDto.md)

### Authorization

[X-AUTH-ACCESS-TOKEN](../README.md#X-AUTH-ACCESS-TOKEN)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Success |  -  |

