# Class1GettingStartedApi

All URIs are relative to *https://api.taggun.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postApiReceiptV1SimpleFile**](Class1GettingStartedApi.md#postApiReceiptV1SimpleFile) | **POST** /api/receipt/v1/simple/file | transcribe a receipt by uploading an image file |
| [**postApiReceiptV1VerboseFile**](Class1GettingStartedApi.md#postApiReceiptV1VerboseFile) | **POST** /api/receipt/v1/verbose/file | transcribe a receipt by uploading an image file and return detailed result |


<a id="postApiReceiptV1SimpleFile"></a>
# **postApiReceiptV1SimpleFile**
> ReceiptResult postApiReceiptV1SimpleFile(apikey, _file, refresh, incognito, ipAddress, near, ignoreMerchantName, language, extractTime, subAccountId, referenceId)

transcribe a receipt by uploading an image file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class1GettingStartedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taggun.io");

    Class1GettingStartedApi apiInstance = new Class1GettingStartedApi(defaultClient);
    String apikey = "apikey_example"; // String | API authentication key.
    File _file = new File("/path/to/file"); // File | file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC
    Boolean refresh = false; // Boolean | Set true to force re-process image transcription if the receipt is already in storage
    Boolean incognito = false; // Boolean | Set true to avoid saving the receipt in storage
    String ipAddress = "ipAddress_example"; // String | IP Address of the end user
    String near = "near_example"; // String | A geo location to search for merchant. Typically in the format of city, state, country.
    String ignoreMerchantName = "ignoreMerchantName_example"; // String | Ignore this merchant name if detected on the receipt. Use this field to avoid detecting the customer name as the merchant name.
    String language = "en"; // String | Set language as a hint. Leave empty for auto detect. Supported languages: , en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh 
    Boolean extractTime = false; // Boolean | Set true to return time if found on the receipt. Otherwise, the time is always set to 12:00:00.000.
    String subAccountId = "subAccountId_example"; // String | Tag a request with sub-account ID for billing purposes
    String referenceId = "referenceId_example"; // String | Tag a request with a unique reference ID for feedback and training purposes
    try {
      ReceiptResult result = apiInstance.postApiReceiptV1SimpleFile(apikey, _file, refresh, incognito, ipAddress, near, ignoreMerchantName, language, extractTime, subAccountId, referenceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class1GettingStartedApi#postApiReceiptV1SimpleFile");
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
| **_file** | **File**| file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC | [optional] |
| **refresh** | **Boolean**| Set true to force re-process image transcription if the receipt is already in storage | [optional] [default to false] |
| **incognito** | **Boolean**| Set true to avoid saving the receipt in storage | [optional] [default to false] |
| **ipAddress** | **String**| IP Address of the end user | [optional] |
| **near** | **String**| A geo location to search for merchant. Typically in the format of city, state, country. | [optional] |
| **ignoreMerchantName** | **String**| Ignore this merchant name if detected on the receipt. Use this field to avoid detecting the customer name as the merchant name. | [optional] |
| **language** | **String**| Set language as a hint. Leave empty for auto detect. Supported languages: , en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh  | [optional] [enum: en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh] |
| **extractTime** | **Boolean**| Set true to return time if found on the receipt. Otherwise, the time is always set to 12:00:00.000. | [optional] [default to false] |
| **subAccountId** | **String**| Tag a request with sub-account ID for billing purposes | [optional] |
| **referenceId** | **String**| Tag a request with a unique reference ID for feedback and training purposes | [optional] |

### Return type

[**ReceiptResult**](ReceiptResult.md)

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

<a id="postApiReceiptV1VerboseFile"></a>
# **postApiReceiptV1VerboseFile**
> ReceiptVerboseResult postApiReceiptV1VerboseFile(apikey, _file, refresh, incognito, ipAddress, near, ignoreMerchantName, language, extractTime, subAccountId, referenceId)

transcribe a receipt by uploading an image file and return detailed result

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class1GettingStartedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taggun.io");

    Class1GettingStartedApi apiInstance = new Class1GettingStartedApi(defaultClient);
    String apikey = "apikey_example"; // String | API authentication key.
    File _file = new File("/path/to/file"); // File | file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC
    Boolean refresh = false; // Boolean | Set true to force re-process image transcription if the receipt is already in storage
    Boolean incognito = false; // Boolean | Set true to avoid saving the receipt in storage
    String ipAddress = "ipAddress_example"; // String | IP Address of the end user
    String near = "near_example"; // String | A geo location to search for merchant. Typically in the format of city, state, country.
    String ignoreMerchantName = "ignoreMerchantName_example"; // String | Ignore this merchant name if detected on the receipt. Use this field to avoid detecting the customer name as the merchant name.
    String language = "en"; // String | Set language as a hint. Leave empty for auto detect. Supported languages: , en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh 
    Boolean extractTime = false; // Boolean | Set true to return time if found on the receipt. Otherwise, the time is always set to 12:00:00.000.
    String subAccountId = "subAccountId_example"; // String | Tag a request with sub-account ID for billing purposes
    String referenceId = "referenceId_example"; // String | Tag a request with a unique reference ID for feedback and training purposes
    try {
      ReceiptVerboseResult result = apiInstance.postApiReceiptV1VerboseFile(apikey, _file, refresh, incognito, ipAddress, near, ignoreMerchantName, language, extractTime, subAccountId, referenceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class1GettingStartedApi#postApiReceiptV1VerboseFile");
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
| **_file** | **File**| file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC | [optional] |
| **refresh** | **Boolean**| Set true to force re-process image transcription if the receipt is already in storage | [optional] [default to false] |
| **incognito** | **Boolean**| Set true to avoid saving the receipt in storage | [optional] [default to false] |
| **ipAddress** | **String**| IP Address of the end user | [optional] |
| **near** | **String**| A geo location to search for merchant. Typically in the format of city, state, country. | [optional] |
| **ignoreMerchantName** | **String**| Ignore this merchant name if detected on the receipt. Use this field to avoid detecting the customer name as the merchant name. | [optional] |
| **language** | **String**| Set language as a hint. Leave empty for auto detect. Supported languages: , en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh  | [optional] [enum: en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh] |
| **extractTime** | **Boolean**| Set true to return time if found on the receipt. Otherwise, the time is always set to 12:00:00.000. | [optional] [default to false] |
| **subAccountId** | **String**| Tag a request with sub-account ID for billing purposes | [optional] |
| **referenceId** | **String**| Tag a request with a unique reference ID for feedback and training purposes | [optional] |

### Return type

[**ReceiptVerboseResult**](ReceiptVerboseResult.md)

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

