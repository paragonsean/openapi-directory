# VbaDocumentsApi

All URIs are relative to *https://sandbox-api.va.gov/services/vba_documents/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBenefitsDocumentUploadDownload**](VbaDocumentsApi.md#getBenefitsDocumentUploadDownload) | **GET** /uploads/{id}/download | Download zip of \&quot;what the server sees\&quot; |
| [**getBenefitsDocumentUploadStatus**](VbaDocumentsApi.md#getBenefitsDocumentUploadStatus) | **GET** /uploads/{id} | Get status for a previous benefits document upload |
| [**getBenefitsDocumentUploadStatusReport**](VbaDocumentsApi.md#getBenefitsDocumentUploadStatusReport) | **POST** /uploads/report | Get a bulk status report for a list of previous uploads |
| [**postBenefitsDocumentUpload**](VbaDocumentsApi.md#postBenefitsDocumentUpload) | **POST** /uploads | Get a location for subsequent document upload PUT request |
| [**postBenefitsDocumentUploadValidateDocument**](VbaDocumentsApi.md#postBenefitsDocumentUploadValidateDocument) | **POST** /uploads/validate_document | Validate an individual document against system file requirements |
| [**putBenefitsDocumentUpload**](VbaDocumentsApi.md#putBenefitsDocumentUpload) | **PUT** /path | Accepts document upload. |


<a id="getBenefitsDocumentUploadDownload"></a>
# **getBenefitsDocumentUploadDownload**
> File getBenefitsDocumentUploadDownload(id)

Download zip of \&quot;what the server sees\&quot;

An endpoint that will allow you to see exactly what the server sees. We split apart all submitted docs and metadata and zip the file to make it available to you to help with debugging purposes. Files are deleted after 10 days. Only available in testing environments, not production.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VbaDocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.va.gov/services/vba_documents/v1");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    VbaDocumentsApi apiInstance = new VbaDocumentsApi(defaultClient);
    UUID id = UUID.fromString("6d8433c1-cd55-4c24-affd-f592287a7572"); // UUID | ID as returned by a previous create upload request
    try {
      File result = apiInstance.getBenefitsDocumentUploadDownload(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VbaDocumentsApi#getBenefitsDocumentUploadDownload");
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
| **id** | **UUID**| ID as returned by a previous create upload request | |

### Return type

[**File**](File.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Zip file with the contents of your payload as parsed by our server |  -  |
| **401** | Unauthorized request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **429** | Too many requests |  -  |
| **500** | Internal server error |  -  |

<a id="getBenefitsDocumentUploadStatus"></a>
# **getBenefitsDocumentUploadStatus**
> GetBenefitsDocumentUploadStatus200Response getBenefitsDocumentUploadStatus(id)

Get status for a previous benefits document upload

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VbaDocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.va.gov/services/vba_documents/v1");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    VbaDocumentsApi apiInstance = new VbaDocumentsApi(defaultClient);
    UUID id = UUID.fromString("6d8433c1-cd55-4c24-affd-f592287a7572"); // UUID | ID as returned by a previous create upload request
    try {
      GetBenefitsDocumentUploadStatus200Response result = apiInstance.getBenefitsDocumentUploadStatus(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VbaDocumentsApi#getBenefitsDocumentUploadStatus");
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
| **id** | **UUID**| ID as returned by a previous create upload request | |

### Return type

[**GetBenefitsDocumentUploadStatus200Response**](GetBenefitsDocumentUploadStatus200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Upload status retrieved successfully |  -  |
| **401** | Unauthorized request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **429** | Too many requests |  -  |
| **500** | Internal server error |  -  |

<a id="getBenefitsDocumentUploadStatusReport"></a>
# **getBenefitsDocumentUploadStatusReport**
> GetBenefitsDocumentUploadStatusReport200Response getBenefitsDocumentUploadStatusReport(documentUploadStatusGuidList)

Get a bulk status report for a list of previous uploads

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VbaDocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.va.gov/services/vba_documents/v1");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    VbaDocumentsApi apiInstance = new VbaDocumentsApi(defaultClient);
    DocumentUploadStatusGuidList documentUploadStatusGuidList = new DocumentUploadStatusGuidList(); // DocumentUploadStatusGuidList | List of GUIDs for which to retrieve current status
    try {
      GetBenefitsDocumentUploadStatusReport200Response result = apiInstance.getBenefitsDocumentUploadStatusReport(documentUploadStatusGuidList);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VbaDocumentsApi#getBenefitsDocumentUploadStatusReport");
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
| **documentUploadStatusGuidList** | [**DocumentUploadStatusGuidList**](DocumentUploadStatusGuidList.md)| List of GUIDs for which to retrieve current status | |

### Return type

[**GetBenefitsDocumentUploadStatusReport200Response**](GetBenefitsDocumentUploadStatusReport200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Upload status report retrieved successfully |  -  |
| **400** | Bad Request - invalid or missing list of guids |  -  |
| **401** | Unauthorized request |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable Entity |  -  |
| **429** | Too many requests |  -  |
| **500** | Internal server error |  -  |

<a id="postBenefitsDocumentUpload"></a>
# **postBenefitsDocumentUpload**
> PostBenefitsDocumentUpload202Response postBenefitsDocumentUpload()

Get a location for subsequent document upload PUT request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VbaDocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.va.gov/services/vba_documents/v1");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    VbaDocumentsApi apiInstance = new VbaDocumentsApi(defaultClient);
    try {
      PostBenefitsDocumentUpload202Response result = apiInstance.postBenefitsDocumentUpload();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VbaDocumentsApi#postBenefitsDocumentUpload");
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

[**PostBenefitsDocumentUpload202Response**](PostBenefitsDocumentUpload202Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted. Location generated |  -  |
| **401** | Unauthorized request |  -  |
| **403** | Forbidden |  -  |
| **422** | Unprocessable Entity |  -  |
| **429** | Too many requests |  -  |
| **500** | Internal server error |  -  |

<a id="postBenefitsDocumentUploadValidateDocument"></a>
# **postBenefitsDocumentUploadValidateDocument**
> PostBenefitsDocumentUploadValidateDocument200Response postBenefitsDocumentUploadValidateDocument()

Validate an individual document against system file requirements

Using this endpoint will decrease the likelihood of errors associated with individual documents during the submission process. Validations performed: * Document is a valid PDF (Note: &#x60;Content-Type&#x60; header value must be \&quot;application/pdf\&quot;) * Document does not have a user password (an owner password is acceptable) * File size does not exceed 100 MB * Page size does not exceed 21\&quot; x 21\&quot;  Each PDF document is sent as a direct file upload. The request body should contain nothing other than the document in binary format. Binary multipart/form-data encoding is not supported. This endpoint does NOT validate metadata in JSON format.  This endpoint does NOT initiate the claims intake process or submit data to that process. After using this endpoint, individual PDF documents can be combined and submitted as a payload using PUT &#x60;/path&#x60;.  A &#x60;200&#x60; response confirms that the individual document provided passes the system requirements.  A &#x60;422&#x60; response indicates one or more problems with the document that should be resolved before submitting it in the full document submission payload. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VbaDocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.va.gov/services/vba_documents/v1");

    VbaDocumentsApi apiInstance = new VbaDocumentsApi(defaultClient);
    try {
      PostBenefitsDocumentUploadValidateDocument200Response result = apiInstance.postBenefitsDocumentUploadValidateDocument();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VbaDocumentsApi#postBenefitsDocumentUploadValidateDocument");
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

[**PostBenefitsDocumentUploadValidateDocument200Response**](PostBenefitsDocumentUploadValidateDocument200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document passed system requirements |  -  |
| **401** | Unauthorized request |  -  |
| **403** | Forbidden |  -  |
| **422** | Document did NOT pass system requirements |  -  |
| **429** | Too many requests |  -  |
| **500** | Internal server error |  -  |

<a id="putBenefitsDocumentUpload"></a>
# **putBenefitsDocumentUpload**
> putBenefitsDocumentUpload(contentMD5)

Accepts document upload.

Accepts document metadata, document binary, and attachment binaries. Full URL, including query parameters, provided from POST &#x60;/document_uploads&#x60;.  ## Example Payload  The following demonstrates a (redacted) multipart payload suitable for submitting to the PUT endpoint. Most programming languages should have provisions for assembling a multipart payload like this without having to do so manually.  &#x60;&#x60;&#x60; --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name&#x3D;\&quot;metadata\&quot; Content-Type: application/json  {\&quot;veteranFirstName\&quot;: \&quot;Jane\&quot;, \&quot;veteranLastName\&quot;: \&quot;Doe\&quot;, \&quot;fileNumber\&quot;: \&quot;012345678\&quot;, \&quot;zipCode\&quot;: \&quot;97202\&quot;, \&quot;source\&quot;: \&quot;MyVSO\&quot;, \&quot;docType\&quot;: \&quot;21-22\&quot; \&quot;businessLine\&quot;: \&quot;CMP\&quot;} --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name&#x3D;\&quot;content\&quot; Content-Type: application/pdf  &lt;Binary PDF contents&gt; --17de1ed8f01442b2a2d7a93506314b76 Content-Disposition: form-data; name&#x3D;\&quot;attachment1\&quot; Content-Type: application/pdf  &lt;Binary PDF attachment contents&gt; --17de1ed8f01442b2a2d7a93506314b76-- &#x60;&#x60;&#x60;  This PUT request would have an overall HTTP Content-Type header:  &#x60;&#x60;&#x60; Content-Type: multipart/form-data; boundary&#x3D;17de1ed8f01442b2a2d7a93506314b76 &#x60;&#x60;&#x60;  Note that the Content-Disposition parameter \&quot;name\&quot; in each part must be the expected values \&quot;metadata\&quot;, \&quot;content\&quot;, \&quot;attachment1\&quot;...\&quot;attachmentN\&quot;. The attachment attributes must be named  exactly as they are listed here (case sensitive), for example: \&quot;attachment_1\&quot; or \&quot;Attachment2\&quot; are invalid.  This is an example curl command:  &#x60;&#x60;&#x60; curl -v -L -X PUT &#39;&lt;Location from \\uploads&gt;&#39; -F &#39;metadata&#x3D;\&quot;{\\\&quot;veteranFirstName\\\&quot;: \\\&quot;Jane\\\&quot;,\\\&quot;veteranLastName\\\&quot;: \\\&quot;Doe\\\&quot;,\\\&quot;fileNumber\\\&quot;: \\\&quot;012345678\\\&quot;,\\\&quot;zipCode\\\&quot;: \\\&quot;97202\\\&quot;,\\\&quot;source\\\&quot;: \\\&quot;MyVSO\\\&quot;,\\\&quot;docType\\\&quot;: \\\&quot;21-22\\\&quot;,\\\&quot;businessLine\\\&quot;: \\\&quot;CMP\\\&quot;}\&quot;;type&#x3D;application/json&#39; -F &#39;content&#x3D;@\&quot;content.pdf\&quot;&#39; -F &#39;attachment1&#x3D;@\&quot;file1.pdf\&quot;&#39; -F &#39;attachment2&#x3D;@\&quot;another_file.pdf\&quot;&#39; &#x60;&#x60;&#x60; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VbaDocumentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.va.gov/services/vba_documents/v1");

    VbaDocumentsApi apiInstance = new VbaDocumentsApi(defaultClient);
    String contentMD5 = "contentMD5_example"; // String | Base64-encoded 128-bit MD5 digest of the message. Use for integrity control
    try {
      apiInstance.putBenefitsDocumentUpload(contentMD5);
    } catch (ApiException e) {
      System.err.println("Exception when calling VbaDocumentsApi#putBenefitsDocumentUpload");
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
| **contentMD5** | **String**| Base64-encoded 128-bit MD5 digest of the message. Use for integrity control | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Document upload staged |  -  |
| **401** | Unauthorized request |  -  |
| **403** | Document upload failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **429** | Too many requests |  -  |
| **500** | Internal server error |  -  |

