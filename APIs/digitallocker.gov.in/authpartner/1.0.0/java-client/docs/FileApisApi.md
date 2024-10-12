# FileApisApi

All URIs are relative to *https://betaapi.digitallocker.gov.in/public*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCertificateDataInXMLFormatFromURIId**](FileApisApi.md#getCertificateDataInXMLFormatFromURIId) | **GET** /oauth2/1/xml/{uri} | Get Certificate Data in XML Format from URI |
| [**getEAadhaarDataInXMLFormatId**](FileApisApi.md#getEAadhaarDataInXMLFormatId) | **GET** /oauth2/2/xml/eaadhaar | Get e-Aadhaar Data in XML Format |
| [**getFileFromURIId**](FileApisApi.md#getFileFromURIId) | **GET** /oauth2/1/file/{uri} | Get File from URI |
| [**getListOfIssuedDocumentsId**](FileApisApi.md#getListOfIssuedDocumentsId) | **GET** /oauth2/2/files/issued | Issued Documents |
| [**getListOfIssuedDocumentsVersion1Id**](FileApisApi.md#getListOfIssuedDocumentsVersion1Id) | **GET** /oauth2/1/files/issued | Issued Documents |
| [**getListOfSelfUploadedDocuments**](FileApisApi.md#getListOfSelfUploadedDocuments) | **GET** /oauth2/1/files/ | Get List of Self Uploaded Documents |
| [**getListOfSelfUploadedDocumentsId**](FileApisApi.md#getListOfSelfUploadedDocumentsId) | **GET** /oauth2/1/files/{id} | Get List of Self Uploaded Documents |
| [**pullDocumentId**](FileApisApi.md#pullDocumentId) | **POST** /oauth2/1/pull/pulldocument | Pull Document |
| [**uploadFileToLockerId**](FileApisApi.md#uploadFileToLockerId) | **POST** /oauth2/1/file/upload | Upload file to locker |


<a id="getCertificateDataInXMLFormatFromURIId"></a>
# **getCertificateDataInXMLFormatFromURIId**
> XMLFormatSchema getCertificateDataInXMLFormatFromURIId(uri)

Get Certificate Data in XML Format from URI

Returns the certificate data in machine readable XML format for a URI. This API can be used to only for issued documents. The XML data may not be available for all documents. If the XML data is available for a particular document, the mime parameter in Get List of Issued Documents API will contain application/xml. Please refer to Digital Locker XML Certificate Formats for more details of XML formats of various documents.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    FileApisApi apiInstance = new FileApisApi(defaultClient);
    String uri = "uri_example"; // String | 
    try {
      XMLFormatSchema result = apiInstance.getCertificateDataInXMLFormatFromURIId(uri);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileApisApi#getCertificateDataInXMLFormatFromURIId");
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
| **uri** | **String**|  | |

### Return type

[**XMLFormatSchema**](XMLFormatSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized error |  -  |
| **404** | Not found |  -  |
| **500** | Internal Error |  -  |
| **503** | Gateway timeout |  -  |

<a id="getEAadhaarDataInXMLFormatId"></a>
# **getEAadhaarDataInXMLFormatId**
> EaadharXamlSchema getEAadhaarDataInXMLFormatId()

Get e-Aadhaar Data in XML Format

Returns e-Aadhaar data in XML format for the account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    FileApisApi apiInstance = new FileApisApi(defaultClient);
    try {
      EaadharXamlSchema result = apiInstance.getEAadhaarDataInXMLFormatId();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileApisApi#getEAadhaarDataInXMLFormatId");
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

[**EaadharXamlSchema**](EaadharXamlSchema.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **401** | Unauthorized error |  -  |
| **404** | Not found |  -  |
| **500** | Internal Error |  -  |
| **503** | Gateway timeout |  -  |

<a id="getFileFromURIId"></a>
# **getFileFromURIId**
> String getFileFromURIId(uri)

Get File from URI

Returns a file from URI. This API can be used to fetch both issued document and uploaded document.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    FileApisApi apiInstance = new FileApisApi(defaultClient);
    String uri = "uri_example"; // String | This is the unique identifier of the document.
    try {
      String result = apiInstance.getFileFromURIId(uri);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileApisApi#getFileFromURIId");
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
| **uri** | **String**| This is the unique identifier of the document. | |

### Return type

**String**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, image/jpeg, image/jpg, image/png, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized error |  -  |
| **404** | Not found |  -  |
| **500** | Internal Error |  -  |
| **503** | Gateway timeout |  -  |

<a id="getListOfIssuedDocumentsId"></a>
# **getListOfIssuedDocumentsId**
> GetListOfIssuedDocumentsId200Response getListOfIssuedDocumentsId()

Issued Documents

Returns the list of meta-data about issued documents in user’s DigiLocker.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");

    FileApisApi apiInstance = new FileApisApi(defaultClient);
    try {
      GetListOfIssuedDocumentsId200Response result = apiInstance.getListOfIssuedDocumentsId();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileApisApi#getListOfIssuedDocumentsId");
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

[**GetListOfIssuedDocumentsId200Response**](GetListOfIssuedDocumentsId200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **401** | Unauthorized error |  -  |
| **500** | Internal Error |  -  |

<a id="getListOfIssuedDocumentsVersion1Id"></a>
# **getListOfIssuedDocumentsVersion1Id**
> Sample2 getListOfIssuedDocumentsVersion1Id()

Issued Documents

Returns the list of meta-data about issued documents in user’s DigiLocker.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    FileApisApi apiInstance = new FileApisApi(defaultClient);
    try {
      Sample2 result = apiInstance.getListOfIssuedDocumentsVersion1Id();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileApisApi#getListOfIssuedDocumentsVersion1Id");
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

[**Sample2**](Sample2.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **401** | Unauthorized error |  -  |
| **500** | Internal Error |  -  |

<a id="getListOfSelfUploadedDocuments"></a>
# **getListOfSelfUploadedDocuments**
> Sample1 getListOfSelfUploadedDocuments()

Get List of Self Uploaded Documents

Returns the list of meta-data about documents or folders in user’s DigiLocker in a specific location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    FileApisApi apiInstance = new FileApisApi(defaultClient);
    try {
      Sample1 result = apiInstance.getListOfSelfUploadedDocuments();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileApisApi#getListOfSelfUploadedDocuments");
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

[**Sample1**](Sample1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **401** | Unauthorized error |  -  |
| **404** | Not found |  -  |
| **500** | Internal Error |  -  |

<a id="getListOfSelfUploadedDocumentsId"></a>
# **getListOfSelfUploadedDocumentsId**
> Sample3 getListOfSelfUploadedDocumentsId(id)

Get List of Self Uploaded Documents

Returns the list of meta-data about documents or folders in user’s DigiLocker in a specific location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    FileApisApi apiInstance = new FileApisApi(defaultClient);
    String id = "id_example"; // String | The id of the folder to list. To list the files of root folder of a user’s locker, do not send this parameter. This is sent as a part of the URL.
    try {
      Sample3 result = apiInstance.getListOfSelfUploadedDocumentsId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileApisApi#getListOfSelfUploadedDocumentsId");
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
| **id** | **String**| The id of the folder to list. To list the files of root folder of a user’s locker, do not send this parameter. This is sent as a part of the URL. | |

### Return type

[**Sample3**](Sample3.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **401** | Unauthorized error |  -  |
| **404** | Not found |  -  |
| **500** | Internal Error |  -  |

<a id="pullDocumentId"></a>
# **pullDocumentId**
> Sample4 pullDocumentId(chasisNo, consent, doctype, orgid, regNo)

Pull Document

This API allows a client application to search a document/certificate from issuer’s repository using the parameters provided by a user. The searched document is saved in user’s issued document section of DigiLocker if the search is successful.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    FileApisApi apiInstance = new FileApisApi(defaultClient);
    String chasisNo = "chasisNo_example"; // String | Other parameters required for fetching a document as listed in paramname field of Get Search Parameters API.
    String consent = "consent_example"; // String | The consent indicator from the user for performing demographic authentication using Aadhaar details. This Partner Application must capture the user consent for performing the Aadhaar demographic authentication. The possible values are ‘Y’ and ‘N’. The sign up request will be processed only when this indicator is ‘Y’.
    String doctype = "doctype_example"; // String | A 5 character unique document type provided by DigiLocker.
    String orgid = "orgid_example"; // String | The organization id for the issuer in DigiLocker. This organization id is returned in Get List of Issuers API mentioned above.
    String regNo = "regNo_example"; // String | Other parameters required for fetching a document as listed in paramname field of Get Search Parameters API.
    try {
      Sample4 result = apiInstance.pullDocumentId(chasisNo, consent, doctype, orgid, regNo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileApisApi#pullDocumentId");
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
| **chasisNo** | **String**| Other parameters required for fetching a document as listed in paramname field of Get Search Parameters API. | [optional] |
| **consent** | **String**| The consent indicator from the user for performing demographic authentication using Aadhaar details. This Partner Application must capture the user consent for performing the Aadhaar demographic authentication. The possible values are ‘Y’ and ‘N’. The sign up request will be processed only when this indicator is ‘Y’. | [optional] |
| **doctype** | **String**| A 5 character unique document type provided by DigiLocker. | [optional] |
| **orgid** | **String**| The organization id for the issuer in DigiLocker. This organization id is returned in Get List of Issuers API mentioned above. | [optional] |
| **regNo** | **String**| Other parameters required for fetching a document as listed in paramname field of Get Search Parameters API. | [optional] |

### Return type

[**Sample4**](Sample4.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized error |  -  |
| **404** | Not found |  -  |
| **500** | Internal Error |  -  |

<a id="uploadFileToLockerId"></a>
# **uploadFileToLockerId**
> FileUploadResponse uploadFileToLockerId(path, hmac, fileUpload)

Upload file to locker

This API can be used to save/upload a file to uploaded documents in DigiLocker. The allowed file types are JPG, JPEG, PNG and PDF. The file size must not exceed 10MB.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://betaapi.digitallocker.gov.in/public");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    FileApisApi apiInstance = new FileApisApi(defaultClient);
    String path = "path_example"; // String | The destination path of the file in DigiLocker including filename.
    String hmac = "hmac_example"; // String | This is used to verify the integrity of the file data. The client app calculates the hash message authentication code (HMAC) of the file content using SHA256 hashing algorithm and the client secret as the hashing key. The resulting HMAC is converted to Base64 format and sent in this parameter. Upon upload of file, DigiLocker calculates the HMAC of the file data and compares it with this HMAC..
    FileUpload fileUpload = new FileUpload(); // FileUpload | 
    try {
      FileUploadResponse result = apiInstance.uploadFileToLockerId(path, hmac, fileUpload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileApisApi#uploadFileToLockerId");
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
| **path** | **String**| The destination path of the file in DigiLocker including filename. | [optional] |
| **hmac** | **String**| This is used to verify the integrity of the file data. The client app calculates the hash message authentication code (HMAC) of the file content using SHA256 hashing algorithm and the client secret as the hashing key. The resulting HMAC is converted to Base64 format and sent in this parameter. Upon upload of file, DigiLocker calculates the HMAC of the file data and compares it with this HMAC.. | [optional] |
| **fileUpload** | [**FileUpload**](FileUpload.md)|  | [optional] |

### Return type

[**FileUploadResponse**](FileUploadResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream, image/jpeg, image/jpg, image/pdf, image/png
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized error |  -  |
| **500** | Internal Error |  -  |

