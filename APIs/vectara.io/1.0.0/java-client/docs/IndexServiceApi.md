# IndexServiceApi

All URIs are relative to *https://api.vectara.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**delete**](IndexServiceApi.md#delete) | **POST** /v1/delete-doc |  |
| [**fileUpload**](IndexServiceApi.md#fileUpload) | **POST** /v1/upload |  |
| [**index**](IndexServiceApi.md#index) | **POST** /v1/index |  |


<a id="delete"></a>
# **delete**
> Object delete(customerId, vectaraDeleteDocumentRequest)



Delete

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vectara.io");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oAuth
    OAuth oAuth = (OAuth) defaultClient.getAuthentication("oAuth");
    oAuth.setAccessToken("YOUR ACCESS TOKEN");

    IndexServiceApi apiInstance = new IndexServiceApi(defaultClient);
    Integer customerId = 56; // Integer | The Customer ID to use for the request.
    VectaraDeleteDocumentRequest vectaraDeleteDocumentRequest = new VectaraDeleteDocumentRequest(); // VectaraDeleteDocumentRequest | 
    try {
      Object result = apiInstance.delete(customerId, vectaraDeleteDocumentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexServiceApi#delete");
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
| **customerId** | **Integer**| The Customer ID to use for the request. | |
| **vectaraDeleteDocumentRequest** | [**VectaraDeleteDocumentRequest**](VectaraDeleteDocumentRequest.md)|  | |

### Return type

**Object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a id="fileUpload"></a>
# **fileUpload**
> FileUpload200Response fileUpload(c, o, d, docMetadata, _file)



File Upload

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vectara.io");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oAuth
    OAuth oAuth = (OAuth) defaultClient.getAuthentication("oAuth");
    oAuth.setAccessToken("YOUR ACCESS TOKEN");

    IndexServiceApi apiInstance = new IndexServiceApi(defaultClient);
    Integer c = 56; // Integer | Customer ID
    Integer o = 56; // Integer | Corpus ID
    Boolean d = true; // Boolean | If true, the server returns the extracted document that was indexed
    String docMetadata = "docMetadata_example"; // String | A JSON string of any additional metadata you want attached to the file.
    File _file = new File("/path/to/file"); // File | The file to be indexed into Vectara.
    try {
      FileUpload200Response result = apiInstance.fileUpload(c, o, d, docMetadata, _file);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexServiceApi#fileUpload");
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
| **c** | **Integer**| Customer ID | |
| **o** | **Integer**| Corpus ID | |
| **d** | **Boolean**| If true, the server returns the extracted document that was indexed | [optional] |
| **docMetadata** | **String**| A JSON string of any additional metadata you want attached to the file. | [optional] |
| **_file** | **File**| The file to be indexed into Vectara. | [optional] |

### Return type

[**FileUpload200Response**](FileUpload200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response |  -  |
| **400** | An invalid request was sent.  e.g. one or more parameters was missing, or the corpus does not exist. |  -  |
| **401** | The request was not authenticated |  -  |
| **403** | The caller is not authorized to add documents to the corpus |  -  |
| **409** | A document already exists in the corpus with the same document ID, yet the contents of the indexed document are different than the file being uploaded. Since the indexer is idempotent, the same document (identified by the document ID) can be uploaded multiple times. The indexer does not support updates yet, so an error is returned when a different document is uploaded for the same document ID Note that when a raw file is uploaded, the file name is used as the document ID. |  -  |
| **507** | There is no more indexing quota left for the corpus or customer to index more documents.  Upgrade your account, add a credit card, or contact sales. |  -  |

<a id="index"></a>
# **index**
> VectaraIndexDocumentResponse index(customerId, vectaraIndexDocumentRequest)



Index

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IndexServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vectara.io");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oAuth
    OAuth oAuth = (OAuth) defaultClient.getAuthentication("oAuth");
    oAuth.setAccessToken("YOUR ACCESS TOKEN");

    IndexServiceApi apiInstance = new IndexServiceApi(defaultClient);
    Integer customerId = 56; // Integer | The Customer ID to use for the request.
    VectaraIndexDocumentRequest vectaraIndexDocumentRequest = new VectaraIndexDocumentRequest(); // VectaraIndexDocumentRequest | 
    try {
      VectaraIndexDocumentResponse result = apiInstance.index(customerId, vectaraIndexDocumentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IndexServiceApi#index");
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
| **customerId** | **Integer**| The Customer ID to use for the request. | |
| **vectaraIndexDocumentRequest** | [**VectaraIndexDocumentRequest**](VectaraIndexDocumentRequest.md)|  | |

### Return type

[**VectaraIndexDocumentResponse**](VectaraIndexDocumentResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

