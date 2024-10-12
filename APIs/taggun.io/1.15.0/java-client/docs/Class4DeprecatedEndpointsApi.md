# Class4DeprecatedEndpointsApi

All URIs are relative to *https://api.taggun.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postApiReceiptV1MatchFile**](Class4DeprecatedEndpointsApi.md#postApiReceiptV1MatchFile) | **POST** /api/receipt/v1/match/file | detect and match a receipt against keywords and metadata by uploading an image file |
| [**postApiReceiptV1SimpleStorage**](Class4DeprecatedEndpointsApi.md#postApiReceiptV1SimpleStorage) | **POST** /api/receipt/v1/simple/storage | transcribe a receipt in storage |
| [**postApiReceiptV1VerboseStorage**](Class4DeprecatedEndpointsApi.md#postApiReceiptV1VerboseStorage) | **POST** /api/receipt/v1/verbose/storage | transcribe a receipt in storage and return detailed result |


<a id="postApiReceiptV1MatchFile"></a>
# **postApiReceiptV1MatchFile**
> ReceiptMatchResult postApiReceiptV1MatchFile(apikey, _file, refresh, incognito, ipAddress, primaryKeywords, secondaryKeywords, stopWords, language)

detect and match a receipt against keywords and metadata by uploading an image file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class4DeprecatedEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taggun.io");

    Class4DeprecatedEndpointsApi apiInstance = new Class4DeprecatedEndpointsApi(defaultClient);
    String apikey = "apikey_example"; // String | API authentication key.
    File _file = new File("/path/to/file"); // File | file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF
    Boolean refresh = false; // Boolean | Set true to force re-process image transcription if the receipt is already in storage
    Boolean incognito = false; // Boolean | Set true to avoid saving the receipt in storage
    String ipAddress = "ipAddress_example"; // String | IP Address of the end user
    List<String> primaryKeywords = Arrays.asList(); // List<String> | An array of primary keywords to match
    List<String> secondaryKeywords = Arrays.asList(); // List<String> | An array of secondary keywords to match (lower confidence level than primaryKeywords)
    List<String> stopWords = Arrays.asList(); // List<String> | An array of stop words that negate the result to be UNLIKELY
    String language = "en"; // String | Set language as a hint. Leave empty for auto detect. Supported languages: , en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh 
    try {
      ReceiptMatchResult result = apiInstance.postApiReceiptV1MatchFile(apikey, _file, refresh, incognito, ipAddress, primaryKeywords, secondaryKeywords, stopWords, language);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class4DeprecatedEndpointsApi#postApiReceiptV1MatchFile");
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
| **apikey** | **String**| API authentication key. | |
| **_file** | **File**| file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF | [optional] |
| **refresh** | **Boolean**| Set true to force re-process image transcription if the receipt is already in storage | [optional] [default to false] |
| **incognito** | **Boolean**| Set true to avoid saving the receipt in storage | [optional] [default to false] |
| **ipAddress** | **String**| IP Address of the end user | [optional] |
| **primaryKeywords** | [**List&lt;String&gt;**](String.md)| An array of primary keywords to match | [optional] |
| **secondaryKeywords** | [**List&lt;String&gt;**](String.md)| An array of secondary keywords to match (lower confidence level than primaryKeywords) | [optional] |
| **stopWords** | [**List&lt;String&gt;**](String.md)| An array of stop words that negate the result to be UNLIKELY | [optional] |
| **language** | **String**| Set language as a hint. Leave empty for auto detect. Supported languages: , en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh  | [optional] [enum: en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh] |

### Return type

[**ReceiptMatchResult**](ReceiptMatchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="postApiReceiptV1SimpleStorage"></a>
# **postApiReceiptV1SimpleStorage**
> ReceiptResult postApiReceiptV1SimpleStorage(apikey, body)

transcribe a receipt in storage

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class4DeprecatedEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taggun.io");

    Class4DeprecatedEndpointsApi apiInstance = new Class4DeprecatedEndpointsApi(defaultClient);
    String apikey = "apikey_example"; // String | API authentication key.
    StoragePayload body = new StoragePayload(); // StoragePayload | 
    try {
      ReceiptResult result = apiInstance.postApiReceiptV1SimpleStorage(apikey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class4DeprecatedEndpointsApi#postApiReceiptV1SimpleStorage");
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
| **apikey** | **String**| API authentication key. | |
| **body** | [**StoragePayload**](StoragePayload.md)|  | [optional] |

### Return type

[**ReceiptResult**](ReceiptResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="postApiReceiptV1VerboseStorage"></a>
# **postApiReceiptV1VerboseStorage**
> ReceiptVerboseResult postApiReceiptV1VerboseStorage(apikey, body)

transcribe a receipt in storage and return detailed result

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class4DeprecatedEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taggun.io");

    Class4DeprecatedEndpointsApi apiInstance = new Class4DeprecatedEndpointsApi(defaultClient);
    String apikey = "apikey_example"; // String | API authentication key.
    StoragePayload body = new StoragePayload(); // StoragePayload | 
    try {
      ReceiptVerboseResult result = apiInstance.postApiReceiptV1VerboseStorage(apikey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class4DeprecatedEndpointsApi#postApiReceiptV1VerboseStorage");
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
| **apikey** | **String**| API authentication key. | |
| **body** | [**StoragePayload**](StoragePayload.md)|  | [optional] |

### Return type

[**ReceiptVerboseResult**](ReceiptVerboseResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

