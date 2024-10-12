# DefaultApi

All URIs are relative to *https://api.pdfblocks.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addImageWatermarkV1**](DefaultApi.md#addImageWatermarkV1) | **POST** /v1/add_watermark/image | Add an image watermark to a PDF |
| [**addPasswordV1**](DefaultApi.md#addPasswordV1) | **POST** /v1/add_password | Add a password to a PDF |
| [**addRestrictionsV1**](DefaultApi.md#addRestrictionsV1) | **POST** /v1/add_restrictions | Add restrictions to a PDF |
| [**addTextWatermarkV1**](DefaultApi.md#addTextWatermarkV1) | **POST** /v1/add_watermark/text | Add a text watermark to a PDF |
| [**extractPagesV1**](DefaultApi.md#extractPagesV1) | **POST** /v1/extract_pages | Extract pages from a PDF |
| [**mergeDocumentsV1**](DefaultApi.md#mergeDocumentsV1) | **POST** /v1/merge_documents | Merge PDF documents |
| [**removePagesV1**](DefaultApi.md#removePagesV1) | **POST** /v1/remove_pages | Remove pages from a PDF |
| [**removePasswordV1**](DefaultApi.md#removePasswordV1) | **POST** /v1/remove_password | Remove the password from a PDF |
| [**removeRestrictionsV1**](DefaultApi.md#removeRestrictionsV1) | **POST** /v1/remove_restrictions | Remove the restrictions from a PDF |
| [**removeSignaturesV1**](DefaultApi.md#removeSignaturesV1) | **POST** /v1/remove_signatures | Remove the signatures from a PDF |
| [**reversePagesV1**](DefaultApi.md#reversePagesV1) | **POST** /v1/reverse_pages | Reverse the pages of a PDF |
| [**rotatePagesV1**](DefaultApi.md#rotatePagesV1) | **POST** /v1/rotate_pages | Rotate pages in a PDF |


<a id="addImageWatermarkV1"></a>
# **addImageWatermarkV1**
> File addImageWatermarkV1(_file, image, margin, transparency)

Add an image watermark to a PDF

Add an image watermark to each page of a PDF document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pdfblocks.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The input PDF document
    File image = new File("/path/to/file"); // File | The image to add as a watermark. The format of the image can be either PNG or JPEG.
    Float margin = 1F; // Float | The distance in inches from the border of the page to the image watermark.
    Integer transparency = 50; // Integer | The transparency level for the image watermark from 0 (opaque) to 100 (transparent).
    try {
      File result = apiInstance.addImageWatermarkV1(_file, image, margin, transparency);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addImageWatermarkV1");
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
| **_file** | **File**| The input PDF document | |
| **image** | **File**| The image to add as a watermark. The format of the image can be either PNG or JPEG. | |
| **margin** | **Float**| The distance in inches from the border of the page to the image watermark. | [optional] [default to 1] |
| **transparency** | **Integer**| The transparency level for the image watermark from 0 (opaque) to 100 (transparent). | [optional] [default to 50] |

### Return type

[**File**](File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/pdf, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The document was processed succesfully. |  -  |
| **4XX** | Error |  -  |

<a id="addPasswordV1"></a>
# **addPasswordV1**
> File addPasswordV1(_file, password, encryptionAlgorithm)

Add a password to a PDF

Protect a PDF document with a password. Encrypt the PDF document to prevent unauthorized access.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pdfblocks.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The input PDF document
    String password = "password_example"; // String | The password required to open the file.
    String encryptionAlgorithm = "AES-128"; // String | The algorithm used to encrypt the PDF document.
    try {
      File result = apiInstance.addPasswordV1(_file, password, encryptionAlgorithm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addPasswordV1");
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
| **_file** | **File**| The input PDF document | |
| **password** | **String**| The password required to open the file. | |
| **encryptionAlgorithm** | **String**| The algorithm used to encrypt the PDF document. | [optional] [default to AES-128] [enum: AES-128, AES-256] |

### Return type

[**File**](File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/pdf, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The document was processed succesfully. |  -  |
| **4XX** | Error |  -  |

<a id="addRestrictionsV1"></a>
# **addRestrictionsV1**
> File addRestrictionsV1(_file, ownerPassword, allowAccessibility, allowAssembleDocument, allowChangeContent, allowCommentAndFillForm, allowCopyContent, allowFillForm, allowPrint, allowPrintHighResolution, encryptionAlgorithm, userPassword)

Add restrictions to a PDF

Add restrictions to prevent copying, printing, and modifying a PDF document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pdfblocks.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The input PDF document
    String ownerPassword = "ownerPassword_example"; // String | The password required to open and change permissions of the PDF document.
    Boolean allowAccessibility = true; // Boolean | If false, accessibility programs can't read the text or images of the document.
    Boolean allowAssembleDocument = true; // Boolean | If false, the user can't assemble or manipulate the document.
    Boolean allowChangeContent = true; // Boolean | If false, the user can't change the content of the document.
    Boolean allowCommentAndFillForm = true; // Boolean | If false, the user can't add, edit or modify annotations or fill form fields.
    Boolean allowCopyContent = true; // Boolean | If false, the user can't copy text and images to the clipboard.
    Boolean allowFillForm = true; // Boolean | If false, the user can't fill forms fields.
    Boolean allowPrint = true; // Boolean | If false, the user can't print the document.
    Boolean allowPrintHighResolution = true; // Boolean | If false, the user can't print the document in high resolution.
    String encryptionAlgorithm = "AES-128"; // String | The algorithm used to encrypt the PDF document.
    String userPassword = "userPassword_example"; // String | The password required to open the PDF document. If the `user_password` is not set, the user will be able to open the document without a password.
    try {
      File result = apiInstance.addRestrictionsV1(_file, ownerPassword, allowAccessibility, allowAssembleDocument, allowChangeContent, allowCommentAndFillForm, allowCopyContent, allowFillForm, allowPrint, allowPrintHighResolution, encryptionAlgorithm, userPassword);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addRestrictionsV1");
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
| **_file** | **File**| The input PDF document | |
| **ownerPassword** | **String**| The password required to open and change permissions of the PDF document. | |
| **allowAccessibility** | **Boolean**| If false, accessibility programs can&#39;t read the text or images of the document. | [optional] [default to true] |
| **allowAssembleDocument** | **Boolean**| If false, the user can&#39;t assemble or manipulate the document. | [optional] [default to true] |
| **allowChangeContent** | **Boolean**| If false, the user can&#39;t change the content of the document. | [optional] [default to true] |
| **allowCommentAndFillForm** | **Boolean**| If false, the user can&#39;t add, edit or modify annotations or fill form fields. | [optional] [default to true] |
| **allowCopyContent** | **Boolean**| If false, the user can&#39;t copy text and images to the clipboard. | [optional] [default to true] |
| **allowFillForm** | **Boolean**| If false, the user can&#39;t fill forms fields. | [optional] [default to true] |
| **allowPrint** | **Boolean**| If false, the user can&#39;t print the document. | [optional] [default to true] |
| **allowPrintHighResolution** | **Boolean**| If false, the user can&#39;t print the document in high resolution. | [optional] [default to true] |
| **encryptionAlgorithm** | **String**| The algorithm used to encrypt the PDF document. | [optional] [default to AES-128] [enum: AES-128, AES-256] |
| **userPassword** | **String**| The password required to open the PDF document. If the &#x60;user_password&#x60; is not set, the user will be able to open the document without a password. | [optional] |

### Return type

[**File**](File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/pdf, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The document was processed succesfully. |  -  |
| **4XX** | Error |  -  |

<a id="addTextWatermarkV1"></a>
# **addTextWatermarkV1**
> File addTextWatermarkV1(_file, line1, color, line2, line3, margin, template, transparency)

Add a text watermark to a PDF

Add a text watermark to each page of a PDF document. Choose from several watermark templates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pdfblocks.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The input PDF document
    String line1 = "line1_example"; // String | The first line of text of the watermark.
    String color = "Red"; // String | The color of the text watermark.
    String line2 = "line2_example"; // String | The second line of text of the watermark.
    String line3 = "line3_example"; // String | The third line of text of the watermark.
    Float margin = 1F; // Float | The distance in inches from the border of the page to the text watermark.
    Integer template = 1001; // Integer | The [id of the text watermark template](https://www.pdfblocks.com/docs/api/v1/text-watermark-templates.pdf).
    Integer transparency = 75; // Integer | The transparency level for the text watermark from 0 (opaque) to 100 (transparent).
    try {
      File result = apiInstance.addTextWatermarkV1(_file, line1, color, line2, line3, margin, template, transparency);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addTextWatermarkV1");
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
| **_file** | **File**| The input PDF document | |
| **line1** | **String**| The first line of text of the watermark. | |
| **color** | **String**| The color of the text watermark. | [optional] [default to Gray] [enum: Red, Blue, Gray, Black] |
| **line2** | **String**| The second line of text of the watermark. | [optional] |
| **line3** | **String**| The third line of text of the watermark. | [optional] |
| **margin** | **Float**| The distance in inches from the border of the page to the text watermark. | [optional] [default to 1] |
| **template** | **Integer**| The [id of the text watermark template](https://www.pdfblocks.com/docs/api/v1/text-watermark-templates.pdf). | [optional] [default to 1001] |
| **transparency** | **Integer**| The transparency level for the text watermark from 0 (opaque) to 100 (transparent). | [optional] [default to 75] |

### Return type

[**File**](File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/pdf, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The document was processed succesfully. |  -  |
| **4XX** | Error |  -  |

<a id="extractPagesV1"></a>
# **extractPagesV1**
> File extractPagesV1(_file, firstPage, lastPage)

Extract pages from a PDF

Extract one or more pages from a PDF document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pdfblocks.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The input PDF document
    Integer firstPage = 56; // Integer | The first page of the range to extract. If empty, it defaults to the first page of the PDF document.
    Integer lastPage = 56; // Integer | The last page of the range to extract. If empty, it defaults to the last page of the PDF document.
    try {
      File result = apiInstance.extractPagesV1(_file, firstPage, lastPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#extractPagesV1");
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
| **_file** | **File**| The input PDF document | |
| **firstPage** | **Integer**| The first page of the range to extract. If empty, it defaults to the first page of the PDF document. | [optional] |
| **lastPage** | **Integer**| The last page of the range to extract. If empty, it defaults to the last page of the PDF document. | [optional] |

### Return type

[**File**](File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/pdf, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The document was processed succesfully. |  -  |
| **4XX** | Error |  -  |

<a id="mergeDocumentsV1"></a>
# **mergeDocumentsV1**
> File mergeDocumentsV1(_file)

Merge PDF documents

Combine multiple PDF documents into a single PDF document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pdfblocks.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    List<File> _file = Arrays.asList(); // List<File> | The array of PDF documents. PDF documents will be merged in the same order they are inserted into this array.
    try {
      File result = apiInstance.mergeDocumentsV1(_file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#mergeDocumentsV1");
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
| **_file** | **List&lt;File&gt;**| The array of PDF documents. PDF documents will be merged in the same order they are inserted into this array. | [optional] |

### Return type

[**File**](File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/pdf, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The document was processed succesfully. |  -  |
| **4XX** | Error |  -  |

<a id="removePagesV1"></a>
# **removePagesV1**
> File removePagesV1(_file, firstPage, lastPage)

Remove pages from a PDF

Remove one or more pages from a PDF document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pdfblocks.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The input PDF document
    Integer firstPage = 56; // Integer | The first page of the range to remove from the PDF document. If empty, it defaults to the first page of the document.
    Integer lastPage = 56; // Integer | The last page of the range to remove from the PDF document. If empty, it defaults to the last page of the document.
    try {
      File result = apiInstance.removePagesV1(_file, firstPage, lastPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removePagesV1");
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
| **_file** | **File**| The input PDF document | |
| **firstPage** | **Integer**| The first page of the range to remove from the PDF document. If empty, it defaults to the first page of the document. | [optional] |
| **lastPage** | **Integer**| The last page of the range to remove from the PDF document. If empty, it defaults to the last page of the document. | [optional] |

### Return type

[**File**](File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/pdf, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The document was processed succesfully. |  -  |
| **4XX** | Error |  -  |

<a id="removePasswordV1"></a>
# **removePasswordV1**
> File removePasswordV1(_file, password)

Remove the password from a PDF

Remove the password from an encrypted PDF document. The PDF document will no longer require a password to open.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pdfblocks.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The input PDF document
    String password = "password_example"; // String | The password required to open the file.
    try {
      File result = apiInstance.removePasswordV1(_file, password);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removePasswordV1");
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
| **_file** | **File**| The input PDF document | |
| **password** | **String**| The password required to open the file. | |

### Return type

[**File**](File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/pdf, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The document was processed succesfully. |  -  |
| **4XX** | Error |  -  |

<a id="removeRestrictionsV1"></a>
# **removeRestrictionsV1**
> File removeRestrictionsV1(_file)

Remove the restrictions from a PDF

Remove all the restrictions from a PDF document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pdfblocks.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The input PDF document
    try {
      File result = apiInstance.removeRestrictionsV1(_file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeRestrictionsV1");
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
| **_file** | **File**| The input PDF document | |

### Return type

[**File**](File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/pdf, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The document was processed succesfully. |  -  |
| **4XX** | Error |  -  |

<a id="removeSignaturesV1"></a>
# **removeSignaturesV1**
> File removeSignaturesV1(_file)

Remove the signatures from a PDF

Remove the cryptographic signatures and timestamps from a PDF document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pdfblocks.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The input PDF document
    try {
      File result = apiInstance.removeSignaturesV1(_file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeSignaturesV1");
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
| **_file** | **File**| The input PDF document | |

### Return type

[**File**](File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/pdf, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The document was processed succesfully. |  -  |
| **4XX** | Error |  -  |

<a id="reversePagesV1"></a>
# **reversePagesV1**
> File reversePagesV1(_file)

Reverse the pages of a PDF

Reverse the order of the pages of a PDF document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pdfblocks.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    File _file = new File("/path/to/file"); // File | The input PDF document
    try {
      File result = apiInstance.reversePagesV1(_file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#reversePagesV1");
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
| **_file** | **File**| The input PDF document | |

### Return type

[**File**](File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/pdf, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The document was processed succesfully. |  -  |
| **4XX** | Error |  -  |

<a id="rotatePagesV1"></a>
# **rotatePagesV1**
> File rotatePagesV1(angle, _file, firstPage, lastPage)

Rotate pages in a PDF

Rotate one or more pages in a PDF document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pdfblocks.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer angle = 0; // Integer | The angle of rotation of the pages. Positive angles rotate the pages clockwise. Negative angles rotate the pages counter-clockwise.
    File _file = new File("/path/to/file"); // File | The input PDF document
    Integer firstPage = 56; // Integer | The first page of the range to rotate in the PDF document. If empty, it defaults to the first page of the document.
    Integer lastPage = 56; // Integer | The last page of the range to rotate in the PDF document. If empty, it defaults to the last page of the document.
    try {
      File result = apiInstance.rotatePagesV1(angle, _file, firstPage, lastPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#rotatePagesV1");
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
| **angle** | **Integer**| The angle of rotation of the pages. Positive angles rotate the pages clockwise. Negative angles rotate the pages counter-clockwise. | [enum: 0, 90, 180, 270, -90, -180, -270] |
| **_file** | **File**| The input PDF document | |
| **firstPage** | **Integer**| The first page of the range to rotate in the PDF document. If empty, it defaults to the first page of the document. | [optional] |
| **lastPage** | **Integer**| The last page of the range to rotate in the PDF document. If empty, it defaults to the last page of the document. | [optional] |

### Return type

[**File**](File.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/pdf, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The document was processed succesfully. |  -  |
| **4XX** | Error |  -  |

